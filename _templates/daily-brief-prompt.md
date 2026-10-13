# Daily brief prompt

Copy everything below the line into a new AI chat. Replace the five
placeholders first:

| Placeholder | What to put | Example |
|---|---|---|
| `[TOPIC]` | One topic name, exactly as written in the Topic table | `Enterprise AI` |
| `[EDITION_DATE]` | Today's date, YYYY-MM-DD | `2026-10-13` |
| `[PUBLISH_TIME]` | Time you will push, HH:MM, 24h SGT. Must not be later than the push, or Jekyll hides the post until the next build | `20:30` |
| `[SINCE]` | When the previous edition of this topic went out | `2026-10-12 20:30 SGT` |
| `[ALREADY_COVERED]` | Headline + URL of every story in (a) today's briefs already written and (b) yesterday's brief on this topic. One per line. Write `none` if empty | `Intel CEO says Chinese AI adoption fast — https://www.reuters.com/...` |

After the AI replies: read it, check two or three links, then either replace
the `MY TAKE` comment with your own `## My take` section or leave it (it stays
hidden). Save as `_posts/[EDITION_DATE]-[TOPIC_SLUG].md`, with no `:` in the
filename.

This file lives in `_templates/`, which Jekyll does not publish.

---

## TOPIC: [TOPIC]
## EDITION_DATE: [EDITION_DATE]
## PUBLISH_TIME: [PUBLISH_TIME]
## SINCE: [SINCE]
## ALREADY_COVERED:
[ALREADY_COVERED]

## Task

Write a professional daily **news brief** on **[TOPIC]** for executives and
practitioners in enterprise AI, fintech and payments, with a Singapore and Asia
lens where relevant.

## Topic table

Look up the row for [TOPIC] and use its values exactly. Do not invent a series
name, slug or fixed tag.

| TOPIC | SERIES | TOPIC_SLUG | FIXED_TAGS | IN SCOPE | NOT IN SCOPE (belongs elsewhere) |
|---|---|---|---|---|---|
| AI Finance in Singapore | Singapore | ai-finance-singapore | Singapore, Fintech, Artificial Intelligence | AI at Singapore banks, insurers, fintechs; MAS and Singapore government AI/finance moves | Fintech news with no Singapore angle (AI Fintech) |
| AI Fintech | AI & Fintech | ai-fintech | Fintech, AI Fintech, Banking | AI in banking, lending, insurance, wealth, payments, outside Singapore | Singapore-specific stories (AI Finance in Singapore) |
| AI Governance | AI Governance & Regulation | ai-governance | AI Governance, AI Regulation, AI Policy | AI laws, regulation, standards, enforcement, policy | Attacks, breaches, vulnerabilities (AI Security & Risk) |
| AI Investment & Startup in China | US & China AI | china-ai-investment-startup | China AI, Startups, Venture Capital | Funding rounds, IPOs, valuations, startup launches in China AI | Chips, export controls, US-China rivalry (US AI vs China AI) |
| AI Research & Open-Source LLM | AI Research & Open Source | ai-research-open-source-llm | AI Research, Open Source AI, LLM | Model releases, papers, benchmarks, open-weight models | Funding and business deals (Enterprise AI, China investment) |
| AI Security & Risk | AI Security & Risk | ai-security-and-risk | AI Security, Cybersecurity, AI Safety | Attacks on or with AI, vulnerabilities, AI fraud, safety incidents | New laws and regulation (AI Governance) |
| Enterprise AI | Enterprise AI | enterprise-ai | Enterprise AI, Agentic AI, AI Agents | Enterprise adoption, vendor platforms, partnerships, deployments | Model research and benchmarks (AI Research) |
| Quantum | Quantum Computing | quantum | Quantum Computing, Deep Tech | Quantum hardware, research, companies, funding, post-quantum security | Non-quantum AI news |
| US AI vs China AI | US & China AI | us-ai-vs-china-ai | China AI, US AI, Geopolitics | Chips, export controls, national AI strategies, US-China model competition | China startup funding (AI Investment & Startup in China) |

If [TOPIC] is not in the table, stop and reply only: "Unknown topic: [TOPIC]".

---

# Hard rules

## Session isolation

- Treat this as a standalone session. Do not use prior conversation history or
  reuse content from earlier newsletters.
- The only memory of earlier briefs is ALREADY_COVERED (below).

## No repeats

- Exclude any story whose underlying event appears in ALREADY_COVERED, even if
  a different publisher covers it or it has a new angle. Only include a
  follow-up if there is a material new fact (new numbers, a decision, a
  completed deal), and say what is new.
- Exclude stories that are NOT IN SCOPE for [TOPIC] in the Topic table.

## Date window

- Only include content published after [SINCE].
- Verify the publication date of every candidate. Do not guess dates.

## Sources and URLs

Every story MUST link to the original publisher's article:
- Direct, public, plain HTTPS URL
- Not an aggregator, cache, search-result, shortened or redirect URL

Resolve aggregator links (e.g. Google News, Bing) to the publisher URL. If you
cannot, drop the story.

## Citation formatting

- Never output internal citation markers, footnote IDs or tool syntax (e.g.
  contentReference, oaicite, search result IDs).
- Every citation is a normal visible URL in the story link. If a source cannot
  be a direct public URL, drop that source.

## Accuracy and copyright

- Paraphrase. Never copy sentences from the source; no direct quote longer than
  15 words.
- Every number, name and date must come from the linked source. If unsure,
  leave it out.
- Do not speculate beyond what sources say. Label opinion as opinion.

## Story limit

- Maximum 10 stories. Fewer is fine. Quality over count.
- If zero stories qualify, output the front matter plus one line:
  "No qualifying stories were published after [SINCE]." Do not invent stories.

---

# Workflow

1. Search authoritative sources for [TOPIC] within its IN SCOPE definition.
2. Verify each candidate's publication date; drop anything not after [SINCE].
3. Drop anything matching ALREADY_COVERED or NOT IN SCOPE.
4. Merge duplicates of the same event; keep the most authoritative source.
5. Rank by real-world impact, industry relevance, reader interest, strategic
   importance and long-term market implications.
6. Keep the top 10 at most. The #1 story is the LEAD.
7. Give each story one category emoji (list below).
8. Write the title from the LEAD (see Output format).
9. Final check: URLs direct and resolved, dates in window, no repeats, no
   citation markers.

## Category emoji

- 🏦 Regulation / policy / licensing
- 🤖 AI / ML / technology
- 💳 Payments / product launch
- 📊 Market / funding / financial results
- 🌐 Cross-border / macro
- 🔒 Security / fraud / risk
- ⚛️ Quantum

---

# Output format

Output clean GitHub Pages Markdown only:
- The very first line of output is `---` (no blank line, no preamble, no code
  fence around the whole reply, no sign-off).
- Front matter YAML must be valid: no blank lines inside it; `tags`,
  `keywords` and `permalink` are top-level keys.

Front matter:

---
layout: post
title: "[TOPIC] Brief: [LEAD headline, max 8 words, Title Case]"
series: "[SERIES]"
description: "[One sentence, max 155 characters, naming the companies or regulators in the top 2-3 stories]"
date: [EDITION_DATE] [PUBLISH_TIME]:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - [FIXED_TAGS, one per line, exactly as in the table]
  - [Up to 2 extra tags: company, regulator or product names central to today's stories, Title Case, e.g. Anthropic, MAS, Nvidia]
keywords: [4-6 lowercase search phrases a reader would type, e.g. agentic ai governance, hcltech anthropic partnership]
permalink: /[TOPIC_SLUG]-brief-[EDITION_DATE]/
---

Title rules:
- Always start with "[TOPIC] Brief:", then the LEAD story as a factual,
  keyword-rich headline (who did what). Example:
  "Enterprise AI Brief: HCLTech and Anthropic Launch Agentic AI Unit"
- No date in the title (it is in the URL and on the page).
- No clickbait, no emoji, no colon after the first one.

Body:

# [Same text as the title]

**Today:** [One sentence that tells a reader in 3 seconds whether today's brief matters to them.]

## Top Stories

### 1. 🏦 **[Headline]**

*[Publisher] · [Month D, YYYY]*

**Bottom line:** [One self-contained sentence: the single takeaway.]

[2-3 sentences of paraphrased facts and context.]

**Why it matters:** [1-2 sentences on business, strategic or market impact, for an Asia-based fintech or enterprise reader where relevant.]

🔗 [Read the full story](https://original-publisher-url)

---

[Repeat for each story, numbered, separated by `---`. Every story heading is a
`###` heading; do not use `###` anywhere else.]

## Key Takeaways

- [3 bullets max: the patterns across today's stories, not a repeat of the headlines]

## What to Watch

[1-2 sentences: the next concrete signal or date to watch.]

<!-- MY TAKE: replace this comment with "## My take" and 2-3 sentences of your own view before publishing, or leave it as is (hidden). -->

---

# Writing style

- Professional, concise, executive-level. No filler, no hype words.
- Strategic implications over plain summary.
- Headlines are factual, not clickbait.
- A reader skimming only the bold text gets the full gist.
- British or American spelling, but consistent within the brief.

---

# Final checklist (internal: verify silently, never output this section)

- First output line is `---`; front matter is valid YAML with no blank lines
- Title starts with "[TOPIC] Brief:" and names the LEAD story
- SERIES, TOPIC_SLUG and FIXED_TAGS copied exactly from the Topic table
- All stories published after [SINCE] and IN SCOPE
- No story repeats an event in ALREADY_COVERED
- Max 10 stories, no duplicates, each with emoji, bottom line and direct link
- No copied sentences; no quote over 15 words; numbers match sources
- No citation markers anywhere
- The MY TAKE comment is present, unchanged
