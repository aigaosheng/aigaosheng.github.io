---
layout: post
# Title shows in the hero, the <title> tag and all post listings. Required.
title: "TITLE — YYYY-MM-DD"
# Which recurring column this is an edition of. Must match a `series:` value in
# one of the pages under series/ exactly, or it will not appear anywhere.
# Run `python3 _tools/assign_series.py` to fill this in from the title, or leave
# it out entirely for a one-off piece that is not part of a column.
series: "Payments"
date: YYYY-MM-DD 20:00:00 +0800
type: post
published: true
status: publish
categories: []
# Use existing tags where possible — check /tags/ before inventing a new one.
# Keep casing and hyphenation consistent (e.g. always "Fintech", never "fintech"/"FinTech").
tags:
  - Tag One
  - Tag Two
keywords: [keyword one, keyword two]
# MUST be unique across the whole site and MUST NOT be "//", "/name/" or "/link name/".
# Convention: lowercase a-z, 0-9 and hyphens only, ending in the date, e.g.
#   /enterprise-ai-brief-2026-10-12/   /payments-weekly-2026-10-11/
# No spaces, "&", ":", apostrophes, em-dashes or Chinese characters: they turn
# into %20-style escapes in the URL that look broken in search results and
# when shared. Never change the permalink of a post that is already live.
#
# Also keep the FILENAME free of ":" (breaks on Windows checkouts). Two files
# with the same permalink make Jekyll warn "Conflict: The following
# destination is shared by multiple files" and silently publish only one.
permalink: /title-words-yyyy-mm-dd/
---

Body starts here.

Structure for a brief — the homepage cards, the series pages and the in-post
table of contents are all built from these headings:

## Top Stories

### 1. **First story headline**

The first `###` under Top Stories becomes the one-line lede on /series/ pages
and the first bullet on the homepage card, so make it a real headline rather
than a label. The heading that repeats the post title is skipped automatically.

* **Source**: Publication · Month D, YYYY
* **Summary**: ...
* **Why It Matters**: ...
* **URL**: https://...

### 2. **Second story headline**

...
