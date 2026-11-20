#!/usr/bin/env python3
"""Generate today's brief for every topic from _templates/daily-prompt-template2.md.

    python3 _tools/daily_briefs.py                       # all topics, today (SGT)
    python3 _tools/daily_briefs.py --date 2026-10-28
    python3 _tools/daily_briefs.py --topic Payments --topic Quantum
    python3 _tools/daily_briefs.py --dry-run             # print the filled prompts, call nothing
    python3 _tools/daily_briefs.py --force               # overwrite briefs that already exist
    python3 _tools/daily_briefs.py --jobs 4              # 4 topics at once
    python3 _tools/daily_briefs.py --effort high         # thinking effort (default: high)
    python3 _tools/daily_briefs.py --provider codex      # use Codex CLI instead of Claude
    python3 _tools/daily_briefs.py --target-stories 8    # aim for 8 verified stories per topic

How the placeholders are filled
-------------------------------
    EDITION_DATE     --date, default today in Singapore time
    SINCE            the day before EDITION_DATE at 20:00 SGT (fixed)
    PUBLISH_TIME     --publish-time, default the SGT clock when each topic starts.
                     Jekyll skips future-dated posts (no `future: true` in
                     _config.yml), so a time later than the deploy would hide it.
    ALREADY_COVERED  headline + URL of every story in the previous edition of the
                     same topic and in every brief already saved for EDITION_DATE.
                     By default topics run one after another so each one sees
                     the briefs written before it. With --jobs N, topics that run
                     at the same time cannot see each other's stories, so expect
                     more cross-topic repeats; the check against each topic's
                     previous edition is unaffected.

Each brief is written by Claude (`claude -p --model sonnet`) or Codex CLI
(`codex exec --search`); choose with --provider. Claude allows only WebSearch
and WebFetch. Codex runs ephemerally outside the repository, with live web
search enabled and shell tools disabled. The brief is saved to
_posts/<EDITION_DATE>-<TOPIC_SLUG>.md. Output that does not start with YAML
front matter or carries the wrong permalink is not saved to _posts; the raw
reply goes to _logs/ (ignored by Jekyll) for a look.

A brief below --target-stories is retried (--retries) with an instruction to
broaden the research. The best valid version is saved even if the target cannot
be met; a zero-story result is treated as a failure unless --allow-empty is set.
No retry may invent or weaken verification requirements to hit the target.

Existing briefs are skipped unless --force, so a re-run only fills the gaps.
Read every brief before pushing: the template asks for a check of the original
articles and dates, and a `## My take` if you want one.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "_templates", "daily-prompt-template2.md")
POSTS = os.path.join(ROOT, "_posts")
LOGS = os.path.join(ROOT, "_logs")

SGT = dt.timezone(dt.timedelta(hours=8))
SINCE_TIME = "20:00"
MAX_STORIES = 10
DEFAULT_STORY_TARGET = 10

TOPICS = (
    "AI Finance in Singapore",
    "AI Fintech",
    "AI Governance",
    "AI Investment & Startup in China",
    "AI Research & Open-Source LLM",
    "AI Security & Risk",
    "Enterprise AI",
    "Payments",
    "Quantum",
    "US AI vs China AI",
    "AI for science",
    "AI for society",
)

# Research can take a while; give each topic up to 20 minutes.
TIMEOUT = 20 * 60

# The prompt proper starts at the "## TOPIC:" line; everything above it is the
# usage note for humans.
PROMPT_START = "## TOPIC:"

STORY_HEADING = re.compile(r'^###\s+\d{1,2}\.\s+.*?\*\*(.+?)\*\*', re.M)
STORY_LINK = re.compile(r'\[Read the full story\]\((https?://[^)\s]+)\)')
TABLE_ROW = re.compile(r'^\|\s*([^|]+?)\s*\|\s*[^|]+?\s*\|\s*([a-z0-9-]+)\s*\|', re.M)
FILE_DATE = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$')


def load_template():
    with open(TEMPLATE, encoding="utf-8") as f:
        text = f.read()
    start = text.find(PROMPT_START)
    if start < 0:
        sys.exit(f"{TEMPLATE}: no '{PROMPT_START}' line found")
    return text, text[start:]


def topic_slugs(template_text):
    """TOPIC (lower case) -> TOPIC_SLUG, read from the template's topic table."""
    slugs = {}
    for name, slug in TABLE_ROW.findall(template_text):
        if not name.startswith("-"):  # skip the |---|---| separator row
            slugs[name.strip().lower()] = slug
    return slugs


def stories(path):
    """[(headline, url)] for each numbered story in a brief."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    out = []
    # One chunk per story: from its ### heading to the next.
    for chunk in re.split(r'^(?=###\s)', text, flags=re.M):
        heading = STORY_HEADING.search(chunk)
        if not heading:
            continue
        link = STORY_LINK.search(chunk)
        out.append((heading.group(1).strip(), link.group(1) if link else ""))
    return out


def already_covered(edition_date, slug):
    """Stories from today's briefs (other topics) and the last edition of this one."""
    today, previous = [], None
    for name in sorted(os.listdir(POSTS)):
        m = FILE_DATE.match(name)
        if not m:
            continue
        date, post_slug = m.groups()
        if date == edition_date and post_slug != slug:
            today.append(name)
        elif post_slug == slug and date < edition_date:
            previous = name  # sorted, so the last match is the latest
    files = today + ([previous] if previous else [])
    lines = []
    for name in files:
        for headline, url in stories(os.path.join(POSTS, name)):
            lines.append(f"- {headline} — {url}" if url else f"- {headline}")
    return "\n".join(lines) or "none"


def fill(prompt, **values):
    for key, value in values.items():
        prompt = prompt.replace(f"[{key}]", value)
    return prompt


def clean(reply):
    """Drop anything the model put before the front matter, and an outer code fence."""
    lines = reply.strip().splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
    for i, line in enumerate(lines):
        if line.strip() == "---":
            return "\n".join(lines[i:]).rstrip() + "\n"
    return ""


def generate(prompt, provider, model, effort=None):
    """Run the selected CLI and return its final reply text."""
    if provider == "claude":
        cmd = ["claude", "-p", "--output-format", "json",
               "--allowedTools", "WebSearch", "WebFetch"]
        cmd += ["--model", model or "sonnet"]
        if effort:
            cmd += ["--effort", effort]
        # Run outside the repo so the session has no project context to lean on.
        result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                timeout=TIMEOUT, cwd=tempfile.gettempdir())
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip()[:300]
                               or f"claude exited {result.returncode}")
        if result.stderr.strip():
            print(f"    claude stderr: {result.stderr.strip()[:300]}", flush=True)
        try:
            data = json.loads(result.stdout)
            reply = data["result"]
        except (ValueError, KeyError, TypeError):
            return result.stdout
        denials = data.get("permission_denials") or []
        names = sorted({d.get("tool_name", "?") for d in denials if isinstance(d, dict)})
        print(f"    claude turns={data.get('num_turns')} "
              f"denied_tools={', '.join(names) or 'none'}", flush=True)
        return reply

    with tempfile.TemporaryDirectory() as workdir:
        output_path = os.path.join(workdir, "reply.md")
        cmd = [
            "codex", "--search", "--disable", "shell_tool",
            "--ask-for-approval", "never", "exec",
            "--json", "--ephemeral", "--skip-git-repo-check",
            "--sandbox", "read-only",
            "--ignore-user-config", "--ignore-rules",
            "--cd", workdir, "--output-last-message", output_path,
        ]
        if model:
            cmd += ["--model", model]
        if effort:
            cmd += ["--config", f'model_reasoning_effort="{effort}"']
        result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                timeout=TIMEOUT, cwd=workdir)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip()[-300:]
                               or f"codex exited {result.returncode}")
        if not os.path.isfile(output_path):
            raise RuntimeError("codex completed without writing its final reply")
        with open(output_path, encoding="utf-8") as f:
            return f.read()


def story_count(brief):
    """Number of numbered story headings in a generated brief."""
    return len(re.findall(r'^###\s', brief, flags=re.M))


def expanded_research_prompt(prompt, previous_brief, story_count, target):
    """Ask for a broader second pass while preserving the previous verified candidates."""
    previous_headlines = STORY_HEADING.findall(previous_brief)
    candidates = "\n".join(f"- {headline.strip()}" for headline in previous_headlines)
    return (
        f"{prompt}\n\n"
        "## Expanded research pass\n"
        f"The previous attempt found {story_count} qualifying stories, below the target of "
        f"{target}. Do a broader search using additional query angles and relevant source types; "
        "do not stop after one or two results. Preserve these candidates if they still meet all "
        "date, topic, source and verification requirements, and add other distinct qualifying "
        "stories. Return the complete revised Markdown brief, not an addendum. The target is a "
        "research goal, not permission to include weak, duplicate or unverified stories.\n"
        f"Previously found candidate headlines:\n{candidates or '- none'}"
    )


def save_failed(edition_date, slug, reply):
    os.makedirs(LOGS, exist_ok=True)
    path = os.path.join(LOGS, f"{edition_date}-{slug}.failed.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(reply)
    return path


def run_topic(topic, prompt, slugs, edition_date, since, args):
    """Write one brief. Returns "done", "skipped", "failed", or None on a dry run."""
    slug = slugs.get(topic.lower())
    if not slug:
        print(f"[{topic}] not in the template's topic table -- skipped")
        return "failed"
    path = os.path.join(POSTS, f"{edition_date}-{slug}.md")
    if os.path.exists(path) and not args.force:
        print(f"[{topic}] {os.path.relpath(path, ROOT)} exists -- skipped")
        return "skipped"

    publish_time = args.publish_time or dt.datetime.now(SGT).strftime("%H:%M")
    filled = fill(prompt,
                  TOPIC=topic,
                  EDITION_DATE=edition_date,
                  PUBLISH_TIME=publish_time,
                  SINCE=since,
                  TARGET_STORIES=str(args.target_stories),
                  ALREADY_COVERED=already_covered(edition_date, slug))

    if args.dry_run:
        print(f"===== {topic} =====\n{filled}\n")
        return None

    print(f"[{topic}] generating via {args.provider} "
          f"(since {since}, publish {publish_time}) ...", flush=True)
    brief, reply = "", ""
    permalink = f"permalink: /{slug}-brief-{edition_date}/"
    best_brief, best_reply, best_count = "", "", -1
    attempt_prompt = filled
    for attempt in range(1, args.retries + 2):
        try:
            reply = generate(attempt_prompt, args.provider, args.model, args.effort)
        except (RuntimeError, subprocess.TimeoutExpired) as e:
            print(f"[{topic}] FAILED: {e}", flush=True)
            return "failed"

        brief = clean(reply)
        if not brief or permalink not in brief:
            log = save_failed(edition_date, slug, reply)
            print(f"[{topic}] FAILED: reply is not a valid brief -- see {os.path.relpath(log, ROOT)}",
                  flush=True)
            return "failed"

        current_count = story_count(brief)
        if current_count > best_count:
            best_brief, best_reply, best_count = brief, reply, current_count
        if current_count >= args.target_stories or (current_count == 0 and args.allow_empty):
            break
        if attempt <= args.retries:
            print(f"[{topic}] attempt {attempt}: found {current_count} stories; "
                  f"target is {args.target_stories}, expanding research", flush=True)
            attempt_prompt = expanded_research_prompt(
                filled, brief, current_count, args.target_stories)

    if best_count == 0 and not args.allow_empty:
        log = save_failed(edition_date, slug, best_reply)
        print(f"[{topic}] FAILED: 0 stories after {args.retries + 1} attempt(s); not saved. "
              f"Check that the selected CLI's web search works (or pass --allow-empty "
              f"if the day really is empty) -- see {os.path.relpath(log, ROOT)}", flush=True)
        return "failed"

    brief = best_brief
    shortfall = best_count < args.target_stories
    if shortfall:
        print(f"[{topic}] only {best_count} stories in the best response after "
              f"{args.retries + 1} attempt(s); saving below target "
              f"{args.target_stories}", flush=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(brief)
    print(f"[{topic}] wrote {os.path.relpath(path, ROOT)} ({best_count} stories)", flush=True)
    return "short" if shortfall else "done"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", help="edition date YYYY-MM-DD (default: today, SGT)")
    ap.add_argument("--publish-time", help="HH:MM SGT (default: SGT clock when each topic starts)")
    ap.add_argument("--topic", action="append", help="only this topic; repeatable")
    ap.add_argument("--provider", choices=["claude", "codex"], default="claude",
                    help="CLI backend (default: claude)")
    ap.add_argument("--model",
                    help="model passed to the selected CLI (default: sonnet for Claude, "
                         "Codex CLI default for Codex)")
    ap.add_argument("--effort", default="high",
                    choices=["low", "medium", "high", "xhigh", "max"],
                    help="thinking effort passed to the selected CLI (default: high); "
                         "overrides the CLI's configured effort")
    ap.add_argument("--jobs", type=int, default=1,
                    help="topics to generate at once (default 1: one after another)")
    ap.add_argument("--retries", type=int, default=1,
                    help="extra research attempts when below the story target (default 1)")
    ap.add_argument("--target-stories", type=int, default=DEFAULT_STORY_TARGET,
                    help=f"aim for this many verified stories per topic (default {DEFAULT_STORY_TARGET}; "
                         f"maximum {MAX_STORIES})")
    ap.add_argument("--allow-empty", action="store_true",
                    help="save a zero-story brief instead of treating it as a failure")
    ap.add_argument("--force", action="store_true", help="overwrite briefs that already exist")
    ap.add_argument("--dry-run", action="store_true", help="print prompts without calling a CLI")
    args = ap.parse_args()
    if args.jobs < 1:
        ap.error("--jobs must be 1 or more")
    if args.retries < 0:
        ap.error("--retries must be 0 or more")
    if not 1 <= args.target_stories <= MAX_STORIES:
        ap.error(f"--target-stories must be between 1 and {MAX_STORIES}")
    if args.provider == "codex" and args.effort == "max":
        ap.error("--effort max is only supported by Claude; use high or xhigh with Codex")

    edition = (dt.date.fromisoformat(args.date) if args.date
               else dt.datetime.now(SGT).date())
    edition_date = edition.isoformat()
    since = f"{(edition - dt.timedelta(days=1)).isoformat()} {SINCE_TIME} SGT"

    template_text, prompt = load_template()
    slugs = topic_slugs(template_text)
    topics = args.topic or TOPICS

    # A dry run only prints, so keep its output in topic order.
    jobs = 1 if args.dry_run else args.jobs
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = {pool.submit(run_topic, topic, prompt, slugs, edition_date, since, args): topic
                   for topic in topics}
        results = {futures[f]: f.result() for f in as_completed(futures)}

    failed = [t for t in topics if results[t] == "failed"]
    if not args.dry_run:
        count = lambda status: sum(1 for r in results.values() if r == status)
        written = count("done") + count("short")
        print(f"\n{written} written ({count('short')} below target), "
              f"{count('skipped')} skipped, {len(failed)} failed"
              + (f": {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
