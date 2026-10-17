## TOPIC: AI Finance in Singapore
## TOPIC_SLUG: [lowercase-hyphenated-topic]
## DATE_FILTER: 2026-10-17

## Task

Create a professional daily **newsletter** focused on: **[TOPIC]**

## Objective

Deliver a high-signal, publication-ready news brief that summarizes the most
important developments in the topic area, based on the latest available
information.

---

# Hard Rules

## Session Isolation

- Treat this as a new, standalone session.
- Do NOT use or reference prior conversation history, even if this is run inside a continuing chat.
- Do NOT reuse content from any previous newsletter.

## Date Filtering

- Only include content published on or after [DATE_FILTER].
- Strictly exclude any article, announcement, report, or event published before this date.
- Verify the publication date of every candidate story before writing it up.

## Source & URL Requirements

Every story MUST include a source URL that is:
- Valid, direct, and publicly accessible
- The original publisher's URL (not an aggregator, cache, or search-result page)
- A plain HTTPS URL
- Not a shortened URL
- Not a redirect URL

If your search/browsing tool returns an aggregator, redirect, or cached link
(e.g. a Google News or Bing link), resolve it to the original publisher URL
before including the story. If it cannot be resolved to a direct publisher
URL, exclude the story rather than include the indirect link.

## Citation Formatting Rules

- Do NOT output any internal citation markers, footnote IDs, or tool-generated citation syntax of any kind (e.g. contentReference, oaicite, search result IDs, hidden reference markers).
- Convert every citation into a normal, visible public URL in the story's link. If a source can't be represented as a direct public URL, exclude that source entirely — don't fall back to a bare citation marker.

## Story Limit

- Maximum 10 stories.
- Fewer than 10 is fine and expected if fewer high-quality stories pass validation.
- If zero stories pass validation, output only the front matter plus a single line: "No qualifying stories were published on or after [DATE_FILTER]." Do not fabricate stories to fill the quota.

---

# Workflow

1. Search authoritative news sources related to [TOPIC].
2. Verify the publication date of every candidate article.
3. Remove all articles outside the date window.
4. Remove duplicate stories covering the same event, keeping the most authoritative single source per event.
5. Rank remaining stories by:
  - Real-world impact
  - Industry relevance
  - Audience interest / engagement
  - Strategic importance
  - Long-term market implications
6. Select the top 10 stories maximum.
7. Assign each selected story a category emoji (see list below) based on its content.
8. Draft the one-line executive TL;DR summarizing the day's stories.
9. Final validation before writing output:
  - Every URL is a direct, resolved, original-publisher HTTPS URL.
  - Every date satisfies the filter.
  - No duplicate events.
  - No internal citation markers of any kind appear anywhere in the output.

## Category Emoji Reference

Pick the closest fit per story (extend this list to suit [TOPIC]):
- 🏦 Regulation / policy / licensing
- 🤖 AI / ML / technology
- 💳 Payments / product launch
- 📊 Market / funding / financial results
- 🌐 Cross-border / macro
- 🔒 Security / fraud / risk

---

# Output Format

Generate clean GitHub Pages Markdown only.
- Do NOT wrap the entire response in triple backticks.
- Do NOT add any explanation, preamble, or sign-off before or after the Markdown.

Use this Jekyll front matter:

---
layout: post
title: "[TOPIC] Brief — [DATE_FILTER]"
series: "[TOPIC]"
description: "[one-sentence summary, under 160 characters]"
date: [DATETIME] +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
- keyword1
- keyword2
- keyword3
keywords: [keyword1, keyword2, keyword3]
permalink: /[TOPIC_SLUG]-brief-[DATE_FILTER]/
---

# [TOPIC] Brief — [DATE_FILTER]

**Today:** [One-sentence executive TL;DR of the day's stories — written so a
reader knows in 3 seconds whether today's brief is relevant to them.]

## Top Stories

### 1. 🏦 **[Headline]**

*[Publisher Name] · [Publish Date]*

**Bottom line:** [One sentence — the single takeaway, written to stand alone
even if nothing else in the entry gets read.]

[2–3 sentence summary — supporting facts and context.]

**Why it matters:** [1–2 sentences — strategic, business, or market impact.]

🔗 [Read the full story](https://direct-original-source-url.com/article)

---

[Repeat numbered entries for each story, up to 10, each separated by a
horizontal rule as above.]

---

# Writing Style Requirements

- Professional, concise, insight-driven, executive-level readability.
- High signal-to-noise ratio — no filler.
- Prioritize strategic implications over basic summaries.
- Headlines are factual, not clickbait.
- The "Bottom line" sentence must be self-sufficient — a reader skimming only bold text across all stories should get the full gist of the brief.
- Suitable for GitHub Pages, Substack, Notion, or an investor intelligence briefing.

---

# Final Quality Checklist (internal — verify silently, never output this
section or its checkmarks)

✓ All stories published within the date window
✓ Maximum 10 stories, no duplicates
✓ All URLs are direct, resolved, original-publisher HTTPS URLs
✓ Front matter YAML is valid (tags, keywords, and permalink are top-level keys, not nested under tags)
✓ Every story has a category emoji, a bottom line, and a clickable CTA link
✓ TL;DR line is present under the H1
✓ No internal citation markers, contentReference, oaicite, or hidden references anywhere in the output
✓ Output is clean Markdown only, matching the format above exactly