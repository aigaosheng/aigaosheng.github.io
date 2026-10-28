# Daily Brief Prompt — GitHub Pages / Jekyll

Copy this entire prompt into a new AI chat after replacing the five placeholders.

| Placeholder | What to put | Example |
|---|---|---|
| `[TOPIC]` | One topic name, as written in the Topic table | `Enterprise AI` |
| `[EDITION_DATE]` | Edition date in YYYY-MM-DD format | `2026-10-13` |
| `[PUBLISH_TIME]` | Publication time in HH:MM, 24-hour Singapore time | `20:30` |
| `[SINCE]` | Exclusive publication cutoff, in Singapore time | `2026-10-12 20:30 SGT` |
| `[ALREADY_COVERED]` | Headlines and original article URLs already covered in today's briefs and the previous edition of this topic. Use `none` if empty. | `Company announces AI platform — https://example.com/article` |

After generation, check the original articles and dates. Replace the `MY TAKE` comment with your own `## My take` section or leave the comment unchanged. Save the file as `_posts/[EDITION_DATE]-[TOPIC_SLUG].md`. Do not use a colon in the filename.

This template belongs in `_templates/`, which Jekyll does not publish.

---

## TOPIC: [TOPIC]
## EDITION_DATE: [EDITION_DATE]
## PUBLISH_TIME: [PUBLISH_TIME]
## SINCE: [SINCE]
## ALREADY_COVERED:
[ALREADY_COVERED]

## Task

Write a professional daily news brief on [TOPIC] for executives and practitioners in enterprise AI, fintech and payments, with a Singapore and Asia lens where relevant.

The output must be ready to save directly as a GitHub Pages/Jekyll Markdown post, without any manual formatting corrections.

## Topic table

Find the row matching [TOPIC]. Matching ignores letter case, so `AI for science` matches `AI for Science`. Everywhere in the output, including the title prefix, use the TOPIC spelling from the table, not the supplied spelling. Copy its SERIES, TOPIC_SLUG and FIXED_TAGS exactly. Do not invent or rename them.

| TOPIC | SERIES | TOPIC_SLUG | FIXED_TAGS | IN SCOPE | NOT IN SCOPE |
|---|---|---|---|---|---|
| AI Finance in Singapore | Singapore | ai-finance-singapore | Singapore, Fintech, Artificial Intelligence | AI at Singapore banks, insurers, fintechs; MAS and Singapore government AI/finance moves | Fintech news without a Singapore angle; belongs to AI Fintech |
| AI Fintech | AI & Fintech | ai-fintech | Fintech, AI Fintech, Banking | AI in banking, lending, insurance and wealth outside Singapore | Singapore-specific stories, belong to AI Finance in Singapore; payments and stablecoins, belong to Payments |
| AI for Science | AI for Science | ai-for-science | AI for Science, Scientific Discovery, Deep Tech | AI applied to scientific discovery: drug and protein design, biology, chemistry, materials, climate and weather, physics and mathematics; science foundation models, autonomous labs, and science-focused research funding and partnerships | General LLM releases and benchmarks; belong to AI Research & Open-Source LLM. Quantum computing, including quantum-AI hybrids; belongs to Quantum. Enterprise deployments without a research angle; belong to Enterprise AI |
| AI for Society | AI for Society | ai-for-society | AI for Society, Social Impact, Responsible AI | AI's effects on people and communities: jobs, skills and the future of work; education; healthcare access and public health; public services; inclusion, accessibility and the digital divide; misinformation and elections; consumer wellbeing; AI's energy and environmental footprint; public opinion and adoption research | Laws, regulation and enforcement; belong to AI Governance. Attacks, fraud and safety incidents; belong to AI Security & Risk. Medical and scientific research breakthroughs; belong to AI for Science |
| AI Governance | AI Governance & Regulation | ai-governance | AI Governance, AI Regulation, AI Policy | AI laws, regulation, standards, enforcement and policy | Attacks, breaches and vulnerabilities; belong to AI Security & Risk. Social and workforce impact of AI with no law, regulation or enforcement action; belongs to AI for Society |
| AI Investment & Startup in China | US & China AI | china-ai-investment-startup | China AI, Startups, Venture Capital | Funding rounds, IPOs, valuations and startup launches in China AI | Chips, export controls and US-China rivalry; belong to US AI vs China AI |
| AI Research & Open-Source LLM | AI Research & Open Source | ai-research-open-source-llm | AI Research, Open Source AI, LLM | Model releases, papers, benchmarks and open-weight models | Funding and business deals; belong to Enterprise AI or China investment. AI applied to scientific discovery; belongs to AI for Science |
| AI Security & Risk | AI Security & Risk | ai-security-and-risk | AI Security, Cybersecurity, AI Safety | Attacks on or with AI, vulnerabilities, AI fraud and safety incidents | New laws and regulation; belong to AI Governance |
| Enterprise AI | Enterprise AI | enterprise-ai | Enterprise AI, Agentic AI, AI Agents | Enterprise adoption, vendor platforms, partnerships and deployments | Model research and benchmarks; belong to AI Research. Workforce and social impact of AI adoption; belongs to AI for Society |
| Payments | Payments | payments | Payments, Stablecoins, Digital Payments | Payment rails, cards, wallets, cross-border and real-time payments, stablecoins, tokenised deposits and agentic commerce; global and Asia, including Singapore | AI in banking, lending, insurance and wealth; belong to AI Fintech. AI-driven attacks and breaches; belong to AI Security & Risk |
| Quantum | Quantum Computing | quantum | Quantum Computing, Deep Tech | Quantum hardware, research, companies, funding and post-quantum security | Non-quantum AI news |
| US AI vs China AI | US & China AI | us-ai-vs-china-ai | China AI, US AI, Geopolitics | Chips, export controls, national AI strategies and US-China model competition | China startup funding; belongs to AI Investment & Startup in China |

If [TOPIC] does not match any topic in the table, ignoring letter case, stop and output only:

Unknown topic: [TOPIC]

---

# Hard rules

## 1. Session isolation

- Treat this as a standalone research task.
- Do not reuse articles, facts or content from earlier conversations or newsletters.
- The only permitted record of previous coverage is ALREADY_COVERED above.

## 2. No repeats and topic boundaries

- Exclude events already covered in ALREADY_COVERED, even if another publisher reports them.
- Include a follow-up only when a material new fact has emerged, such as a completed deal, new decision or newly disclosed figure. Clearly identify the new development.
- Exclude stories outside the selected topic's IN SCOPE definition.
- Merge reports about the same underlying event and retain the most authoritative original source.

## 3. Date window

- Include only articles whose publication timestamp is strictly later than [SINCE].
- Interpret [SINCE], [EDITION_DATE] and [PUBLISH_TIME] in Singapore time (SGT, UTC+08:00).
- Verify the original article's publication date and, where relevant, its publication time.
- Distinguish publication date from the date an event occurred.
- Do not infer, fabricate or assume publication dates.
- If the publication time cannot be verified and it is unclear whether an article qualifies, exclude it.

## 4. Research and sources

- Search authoritative, relevant sources for the selected topic.
- Prefer original company announcements, regulatory publications, official research releases and reputable financial or technology journalism.
- Every story must link directly to its original publisher's public HTTPS article URL.
- Do not use search-result URLs, aggregators, caches, shortened URLs or redirect links.
- If an aggregator reports a story, locate the original article. If the original cannot be verified, exclude the story.
- Open and verify the source before including it. Confirm that the article supports the claims in the summary.
- Do not fabricate sources, article titles, URLs, quotations, names, numbers or dates.
- If browsing is unavailable or the required evidence cannot be verified, do not invent a news brief.

## 5. Accuracy and copyright

- Paraphrase all source material.
- Never copy a source's sentences verbatim.
- Do not reproduce quotations longer than 15 words.
- Attribute reported figures and claims to their sources where appropriate.
- Do not turn a company's claim into an independently verified fact.
- Do not speculate beyond available evidence. Clearly label opinion as opinion.
- If a fact cannot be verified, omit it.

## 6. Story limit and ranking

- Include no more than 10 stories. Fewer stories are acceptable.
- Rank stories by real-world impact, industry relevance, reader interest, strategic importance and long-term market implications.
- Story 1 must be the lead story and must determine the post title.
- Give each story exactly one relevant category emoji.

If no stories qualify, output the required front matter followed by this single body sentence:

No qualifying stories were published after [SINCE].

Do not invent stories to fill the brief. The normal `MY TAKE` comment must still be included.

## 7. Category emoji

- 🏦 Regulation, policy or licensing
- 🤖 AI, machine learning or AI technology
- 💳 Payments or product launches
- 📊 Markets, funding or financial results
- 🌐 Cross-border developments or macroeconomics
- 🔒 Security, fraud or risk
- ⚛️ Quantum computing
- 🔬 Scientific research or discovery
- 👥 Society, work, education or public impact

---

# Output format — strict requirements

## A. Return a raw Markdown document

The final answer must be the actual contents of a `.md` file.

These rules are mandatory:

1. The first character of the response must be the first hyphen of the opening YAML delimiter `---`.
2. The first line must be exactly `---`.
3. Do not include an introduction, explanation, confirmation, sign-off or research commentary outside the document.
4. Do not wrap the entire response in triple-backtick code fences.
5. Do not wrap the document in XML, HTML, `<escape>` tags or any other container.
6. Use real line breaks throughout the document. Never output the entire document as one long line.
7. Do not escape Markdown syntax. Never prefix Markdown characters with unnecessary backslashes.
8. Do not output `\---`, `\#`, `\##`, `\###`, `\*\*`, `\*`, `\[`, `\]` or escaped Markdown links.
9. Use normal Markdown syntax: `**bold**`, `*italic*`, `# Heading` and `[link text](https://example.com)`.
10. Do not substitute literal `\n` sequences for actual line breaks.
11. Do not HTML-encode ordinary Markdown characters.
12. Do not put the front matter, headings, paragraphs or separate list items on a single line.
13. Do not use a code block to display the finished document.

The output must be directly copyable into a plain-text Markdown file.

## B. Front matter

Start the document with the following structure, replacing every placeholder with the correct value:

---
layout: post
title: "[TOPIC] Brief: [LEAD headline, max 8 words, Title Case]"
series: "[SERIES]"
description: "[One sentence, maximum 155 characters, naming the companies or regulators in the top 2-3 stories]"
date: [EDITION_DATE] [PUBLISH_TIME]:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - [FIXED_TAG_1]
  - [FIXED_TAG_2]
  - [FIXED_TAG_3]
keywords:
  - [lowercase search phrase 1]
  - [lowercase search phrase 2]
  - [lowercase search phrase 3]
  - [lowercase search phrase 4]
permalink: /[TOPIC_SLUG]-brief-[EDITION_DATE]/
---

Front matter requirements:

- The opening and closing `---` delimiters must each occupy a line by themselves.
- The front matter must be valid YAML with no blank lines inside it.
- `tags`, `keywords` and `permalink` must be top-level keys.
- Copy every fixed tag from the selected topic row, preserving the exact spelling, capitalization and order.
- Write each tag as an individual YAML list item. Do not combine multiple tags into one list item.
- You may add up to two additional tags for central companies, regulators or products, provided they are supported by the included stories.
- Write 4–6 relevant lowercase search phrases under `keywords`, each as an individual YAML list item.
- Do not put square-bracketed explanatory placeholders in the finished output.
- Quote YAML values when needed to preserve valid parsing, particularly values containing special characters.
- Use the exact series name and topic slug from the topic table.
- Use `date: YYYY-MM-DD HH:MM:00 +0800`, using the supplied edition date and publication time.
- Set the permalink to `/<TOPIC_SLUG>-brief-<EDITION_DATE>/`.
- Do not insert a blank line between the opening delimiter and the first YAML key, or between YAML keys.
- Insert exactly one blank line after the closing delimiter before the first body heading.

## C. Title rules

- The YAML `title` must start with `[TOPIC] Brief:`, using the TOPIC spelling from the table.
- Follow it with a factual, keyword-rich headline describing the lead story.
- Keep the lead headline to no more than eight words after the prefix.
- Use Title Case for the headline.
- Do not include the edition date in the title.
- Do not use an emoji in the title.
- Do not add another colon after the required prefix.
- The first body heading must exactly match the complete YAML title.

Example:

`Enterprise AI Brief: HCLTech and Anthropic Launch Agentic AI Unit`

## D. Body structure

Use the following layout, preserving the Markdown heading levels and blank lines:

# [EXACT SAME TEXT AS YAML TITLE]

**Today:** [One concise sentence explaining why today's brief matters to the target reader.]

## Top Stories

### 1. 🤖 **[Factual headline]**

*[Original publisher] · [Month D, YYYY]*

**Bottom line:** [One self-contained sentence stating the main takeaway.]

[Two or three sentences of paraphrased facts and context, supported by the linked source.]

**Why it matters:** [One or two sentences explaining the business, strategic or market impact, with an Asia perspective where relevant.]

🔗 [Read the full story](https://original-publisher-url)

---

### 2. 💳 **[Factual headline]**

*[Original publisher] · [Month D, YYYY]*

**Bottom line:** [One self-contained sentence stating the main takeaway.]

[Two or three sentences of paraphrased facts and context.]

**Why it matters:** [One or two sentences explaining the business, strategic or market impact.]

🔗 [Read the full story](https://original-publisher-url)

---

Continue for each qualifying story, numbering consecutively up to 10.

Body formatting rules:

- Use `#` for the main title, `##` for major sections and `###` for individual stories.
- Each story heading must start with its number and exactly one category emoji.
- Use bold for the `Today:`, `Bottom line:` and `Why it matters:` labels.
- Use italics for the publisher and publication date.
- Put the story summary, labels and source link on separate lines or paragraphs as shown.
- Separate consecutive stories with a horizontal rule consisting of exactly three hyphens (`---`) on its own line.
- Insert a blank line before and after each horizontal rule.
- Do not use `###` for any purpose other than story headings.
- Do not add a separate horizontal rule immediately before the first story.
- Do not add a horizontal rule between the last story and `## Key Takeaways`.
- Do not add citations in a separate footnote section. The direct article link within each story is the required source link.

After the stories, output:

## Key Takeaways

- [Cross-story pattern or implication 1]
- [Cross-story pattern or implication 2]
- [Cross-story pattern or implication 3]

## What to Watch

[One or two sentences identifying concrete upcoming signals, decisions, publication dates or measurable developments to monitor. Do not invent future dates.]

<!-- MY TAKE: replace this comment with "## My take" and 2-3 sentences of your own view before publishing, or leave it as is (hidden). -->

The `MY TAKE` comment must appear exactly once at the end of the body. Do not rewrite, remove or expose it as visible prose.

## E. Zero-story format

If no stories qualify, the document must still contain valid front matter using the selected topic's series, tags and slug.

After the closing YAML delimiter and one blank line, output:

No qualifying stories were published after [SINCE].

Then include the unchanged `MY TAKE` comment on a separate line.

Do not include `## Top Stories`, empty story headings, invented links or invented facts in the zero-story case.

---

# Writing style

- Professional, concise and executive-level.
- Focus on strategic implications rather than merely repeating announcements.
- Use factual, non-clickbait headlines.
- Make the bold text useful to readers who skim.
- Use consistent British or American English.
- Avoid hype, filler, unsupported conclusions and repetitive implications.
- Prioritise relevance to enterprise AI, fintech and payments, and the selected topic's scope.

---

# Final validation — perform silently

Before returning the answer, verify every item below. Do not print this checklist.

## Markdown and file integrity

- The first line is exactly `---`.
- The document starts directly with the YAML front matter.
- The YAML opening and closing delimiters occupy separate lines.
- There are no blank lines inside the front matter.
- YAML is syntactically valid.
- All required YAML fields are present.
- Fixed tags match the selected topic row exactly.
- `tags`, `keywords` and `permalink` are top-level fields.
- The first body heading exactly matches the YAML title.
- All headings, paragraphs, lists and story separators occupy the correct lines.
- Markdown syntax is not unnecessarily escaped.
- There are actual newlines, not literal `\n` text.
- No outer code fence or formatting wrapper exists.
- The `MY TAKE` comment is unchanged and appears exactly once.

## Research integrity

- All included stories are within the topic's scope.
- Every included publication date is strictly later than [SINCE].
- No event duplicates ALREADY_COVERED without a material new development.
- There are at most 10 stories.
- Each story has one category emoji, a bottom line, context, business implications and a direct original-source link.
- Links resolve to public HTTPS pages and support the associated claims.
- All figures, names, dates and factual statements are source-supported.
- No internal citation markers or tool syntax appear in the output.

If any validation check fails, fix the output before returning it.

Return only the finished Markdown document.