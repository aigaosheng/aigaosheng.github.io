#!/usr/bin/env python3
"""Generate today's brief for every topic from _templates/daily-prompt-template2.md.

    python3 _tools/daily_briefs.py                       # all topics, today (SGT)
    python3 _tools/daily_briefs.py --date 2026-10-28
    python3 _tools/daily_briefs.py --topic Payments --topic Quantum
    python3 _tools/daily_briefs.py --dry-run             # print the filled prompts, call nothing
    python3 _tools/daily_briefs.py --force               # overwrite briefs that already exist

How the placeholders are filled
-------------------------------
    EDITION_DATE     --date, default today in Singapore time
    SINCE            the day before EDITION_DATE at 20:00 SGT (fixed)
    PUBLISH_TIME     --publish-time, default the SGT clock when each topic starts.
                     Jekyll skips future-dated posts (no `future: true` in
                     _config.yml), so a time later than the deploy would hide it.
    ALREADY_COVERED  headline + URL of every story in the previous edition of the
                     same topic and in every brief already saved for EDITION_DATE.
                     Topics run one after another so each one sees the briefs
                     written before it.

Each brief is written by `claude -p` with only WebSearch and WebFetch allowed,
saved to _posts/<EDITION_DATE>-<TOPIC_SLUG>.md. Output that does not start with
YAML front matter or carries the wrong permalink is not saved to _posts; the raw
reply goes to _logs/ (ignored by Jekyll) for a look.

Existing briefs are skipped unless --force, so a re-run only fills the gaps.
Read every brief before pushing: the template asks for a check of the original
articles and dates, and a `## My take` if you want one.
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "_templates", "daily-prompt-template2.md")
POSTS = os.path.join(ROOT, "_posts")
LOGS = os.path.join(ROOT, "_logs")

SGT = dt.timezone(dt.timedelta(hours=8))
SINCE_TIME = "20:00"

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


def generate(prompt, model):
    cmd = ["claude", "-p", "--allowedTools", "WebSearch", "WebFetch"]
    if model:
        cmd += ["--model", model]
    # Run outside the repo so the session has no project context to lean on;
    # the template's rule 1 asks for a standalone research task.
    result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                            timeout=TIMEOUT, cwd=tempfile.gettempdir())
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"claude exited {result.returncode}")
    return result.stdout


def save_failed(edition_date, slug, reply):
    os.makedirs(LOGS, exist_ok=True)
    path = os.path.join(LOGS, f"{edition_date}-{slug}.failed.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(reply)
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", help="edition date YYYY-MM-DD (default: today, SGT)")
    ap.add_argument("--publish-time", help="HH:MM SGT (default: SGT clock when each topic starts)")
    ap.add_argument("--topic", action="append", help="only this topic; repeatable")
    ap.add_argument("--model", help="model passed to claude --model")
    ap.add_argument("--force", action="store_true", help="overwrite briefs that already exist")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, do not call claude")
    args = ap.parse_args()

    edition = (dt.date.fromisoformat(args.date) if args.date
               else dt.datetime.now(SGT).date())
    edition_date = edition.isoformat()
    since = f"{(edition - dt.timedelta(days=1)).isoformat()} {SINCE_TIME} SGT"

    template_text, prompt = load_template()
    slugs = topic_slugs(template_text)
    topics = args.topic or TOPICS

    done, skipped, failed = [], [], []
    for topic in topics:
        slug = slugs.get(topic.lower())
        if not slug:
            print(f"[{topic}] not in the template's topic table -- skipped")
            failed.append(topic)
            continue
        path = os.path.join(POSTS, f"{edition_date}-{slug}.md")
        if os.path.exists(path) and not args.force:
            print(f"[{topic}] {os.path.relpath(path, ROOT)} exists -- skipped")
            skipped.append(topic)
            continue

        publish_time = args.publish_time or dt.datetime.now(SGT).strftime("%H:%M")
        filled = fill(prompt,
                      TOPIC=topic,
                      EDITION_DATE=edition_date,
                      PUBLISH_TIME=publish_time,
                      SINCE=since,
                      ALREADY_COVERED=already_covered(edition_date, slug))

        if args.dry_run:
            print(f"===== {topic} =====\n{filled}\n")
            continue

        print(f"[{topic}] generating (since {since}, publish {publish_time}) ...", flush=True)
        try:
            reply = generate(filled, args.model)
        except (RuntimeError, subprocess.TimeoutExpired) as e:
            print(f"[{topic}] FAILED: {e}")
            failed.append(topic)
            continue

        brief = clean(reply)
        permalink = f"permalink: /{slug}-brief-{edition_date}/"
        if not brief or permalink not in brief:
            log = save_failed(edition_date, slug, reply)
            print(f"[{topic}] FAILED: reply is not a valid brief -- see {os.path.relpath(log, ROOT)}")
            failed.append(topic)
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(brief)
        print(f"[{topic}] wrote {os.path.relpath(path, ROOT)}")
        done.append(topic)

    if not args.dry_run:
        print(f"\n{len(done)} written, {len(skipped)} skipped, {len(failed)} failed"
              + (f": {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
