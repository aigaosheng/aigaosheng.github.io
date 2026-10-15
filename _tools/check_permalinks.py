#!/usr/bin/env python3
"""Fail if a new post has no clean permalink.

    python3 _tools/check_permalinks.py

Runs in the deploy workflow before the build, so a post with a messy URL
stops the deploy instead of going live.

Why this exists
---------------
A post's URL is its `permalink:` when it has one, and otherwise comes from the
file name under `permalink: pretty` -- /2026/10/09/US-AI-vs-China-AI/, or with
categories prefixed, /ai/fintech/2026/10/06/.... About 2,100 live posts have
URLs with spaces, capitals, "&" or apostrophes in them
(/Startup%20&amp;%20VC%20Intelligence/), which break when pasted into chat apps
and look unprofessional when shared.

Live URLs are left alone: changing one loses its search ranking and breaks
every link to it. So the rule applies only to posts dated on or after CUTOFF.
Such a post must set `permalink:` to lowercase letters, digits and hyphens,
in one or more /segments/, e.g. /payments-brief-2026-10-16/ or
/ai-governance/mas-ai-risk-cookbook/.
"""
import os
import re
import sys

CUTOFF = "2026-10-16"
POSTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_posts")
CLEAN = re.compile(r"/(?:[a-z0-9]+(?:-[a-z0-9]+)*/)+")
DATED = re.compile(r"(\d{4}-\d{2}-\d{2})-")


def front_matter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def main():
    bad = []
    for name in sorted(os.listdir(POSTS)):
        m = DATED.match(name)
        if not m or m.group(1) < CUTOFF or not name.lower().endswith((".md", ".markdown", ".html")):
            continue
        fm = front_matter(os.path.join(POSTS, name))
        pm = re.search(r"^permalink:\s*(.*?)\s*$", fm, re.M)
        value = pm.group(1).strip("\"'") if pm else ""
        if not CLEAN.fullmatch(value):
            bad.append((name, value or "(none)"))
    if bad:
        print("New posts need a clean permalink: lowercase letters, digits and")
        print("hyphens between slashes, e.g. permalink: /payments-brief-2026-10-16/\n")
        for name, value in bad:
            print(f"  _posts/{name}\n    permalink: {value}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
