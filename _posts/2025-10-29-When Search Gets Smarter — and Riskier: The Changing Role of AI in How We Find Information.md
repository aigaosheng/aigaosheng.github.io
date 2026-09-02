---
layout: post
title: "When Search Gets Smarter — and Riskier - The Changing Role of AI in How We Find Information"
description: "What’s really going on · Why it matters (especially for you) · What to watch out for"
date: 2025-10-29 22:20:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI Search
keywords: [search engine, generative AI, information retrieval]
permalink: /When Search Gets Smarter — and Riskier - The Changing Role of AI in How We Find Information/
---

**When Search Gets Smarter — and Riskier: The Changing Role of AI in How We Find Information**

---

Imagine typing a query and not just getting a list of links back—but a generated answer that **looks** right and comes with confidence. That’s where search is heading, and as highlighted in the recent article “Communications of the ACM: *In Search of Better Search*” by Samuel Greengard, we’re entering a complex era of search engines reshaped by AI. ([ACM Digital Library][1])

Here’s what you should know — why this matters, what’s changing, and where the risks lie.

---

### What’s really going on

1. **Search is evolving** — Traditional “query → documents” search is no longer enough. Users don’t just want links; they want insights, summaries, even conversational responses. AI is being layered onto search engines to deliver this richer experience. ([Communications of the ACM][2])
2. **Ambiguous queries pose a growing challenge** — When people don’t know exactly what they’re looking for, or how to ask, search becomes more of a journey than a step. The article underscores how smarter search must handle exploration, context, and user intent — not just keywords. ([Communications of the ACM][2])
3. **AI can help, but it can also mislead** — As search engines adopt generative‑AI or agent‑based features, there’s a tension: on one hand, they can anticipate intent and deliver better results; on the other hand, incorrect or biased answers can surface easier. The article warns of this duality. ([ACM Digital Library][1])
4. **Search is far from 'solved'** — Despite decades of progress, the article reminds us that we still face challenges—such as understanding user context, managing vast and heterogeneous information spaces, and handling new modalities (voice, multimodal, etc.). ([ACM Digital Library][1])
5. **Implications for users and organisations** — For you as a user (or building tools for users): this means search tools you rely on may soon do much more than before, but also require more scrutiny. For organisations: search interfaces, user experience, indexing strategies, and AI‑integration become more critical. The article implicitly invites readers to think about how search failures manifest and how they might be mitigated. ([Communications of the ACM][2])

---

### Why it matters (especially for you)

Given your interests in quantitative research, AI, and building intelligent systems, several angles are relevant:

* If you’re integrating search capabilities (e.g., for your trading platform, email‑processing system, or 3D design assistant), you’ll need to think beyond simple keyword matching — consider user intent, ambiguity, conversational agents, and generative responses.
* AI‑augmented search means you’ll need frameworks for evaluating “good enough” vs. “misleading” results — how do you measure accuracy, relevance, trustworthiness when the system is generating, not just retrieving?
* For end‑users (your designers, analysts, young generation traders): the UX expectations will evolve. They’ll expect immediate answers, context, justification — but they may also fall prey to “plausible but wrong” answers. Your tool must include guardrails.
* Organisations with large knowledge bases (e.g., email archives, documents, 3D design repositories) will face choices: Do you build search + generative summaries? Do you surface unanswered queries? Do you embed user feedback loops? The article suggests the infrastructure and evaluation aspects remain open.

---

### What to watch out for

* **Over‑reliance on AI summarisation**: Even if the system produces an answer, always check for bias, hallucinations, outdated info.
* **Ambiguous queries**: Users often don’t know what they don’t know. Systems must support exploration, not just lookup.
* **Multimodal & heterogeneous data**: Text, images, video, designs — search must handle all these.
* **Trust, transparency, and evaluation**: How does one audit what the “agent” did? How to log query → reasoning → answer?
* **Privacy and indexing**: Especially relevant for your email/ERP/3D‑design systems — indexing internal corpuses brings governance, access, and security concerns.
* **Search metrics must evolve**: Traditional metrics (click‑through rate, dwell time) may no longer suffice when “answers” are generated. The article suggests this remains an unsolved problem. ([ACM Digital Library][1])

---

### Glossary

* **Exploratory search**: A search process in which the seeker doesn’t just want a single fact, but may be investigating, learning, or browsing an unfamiliar topic. The system needs to support iteration, browsing, suggestions. ([ePrints Soton][3])
* **Lookup (or retrieval) search**: Traditional search type where a user has a specific goal (“What’s the capital of France?”) and expects a direct answer/document.
* **Generative‑AI augmentation**: The use of large language models or similar AI to generate responses (not just retrieve documents) based on user queries and available data.
* **Heterogeneous information space**: An environment where data comes from multiple modalities (text, image, audio, video), formats, and domains — making indexing and retrieval more complex.
* **Agent‑based search**: Search systems that incorporate “assistant” or “agent” layers which may proactively interpret intent, ask follow‑up questions, or summarise results rather than just returning links.
* **Semantic context / intent capture**: The process of inferring what the user *means*, rather than just what they typed, using additional signals (user history, domain knowledge, query context, etc.).

---

### Final thoughts

What this article clearly shows is that search is no longer just about *finding* information — it’s about *understanding* information and *serving it* in a way that fits modern user expectations. For tool‑builders and system architects like you, Sheng, this means you’ve got an opportunity — but also a responsibility. Whether you’re designing a trading dashboard, an email analysis system, or a 3D‑design assistant, integrating smarter search means enabling exploration, supporting ambiguity, handling large diverse corpuses, and preventing mis‑navigation.

In short — better search isn’t just a feature; it may become the *core experience*, and getting it right can differentiate your product. But skipping the evaluation, trust, UX, and data‑pipelines could lead to worse outcomes than just “search as usual”.

*Source*: [https://cacm.acm.org/news/in-search-of-better-search/](https://cacm.acm.org/news/in-search-of-better-search/) ([Communications of the ACM][2])

[1]: https://dl.acm.org/doi/10.1145/3760247 "In Search of Better Search | Communications of the ACM"
[2]: https://cacm.acm.org/news/in-search-of-better-search/ "In Search of Better Search"
[3]: https://eprints.soton.ac.uk/263649/1/exploratorySearchSpecialIssueIntro.html "Supporting Exploratory Search: Special Issue CACM ..."