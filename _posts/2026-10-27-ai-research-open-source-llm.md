---
layout: post
title: "AI Research & Open-Source LLM Brief - OpenAI Claims AI Disproved Exponential Time Hypothesis"
series: "AI Research & Open Source"
description: "OpenAI claims an AI disproof of the Exponential Time Hypothesis and ships GPT-6.1 Terra; Baidu open-sources Unlimited OCR 2 for long documents."
date: 2026-10-27 20:20:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - OpenAI
  - Baidu
keywords: [exponential time hypothesis openai, gpt-6.1 terra pricing, baidu unlimited ocr 2, open-weight decision model, ai mathematical proof verification]
permalink: /ai-research-open-source-llm-brief-2026-10-27/
---
# AI Research & Open-Source LLM Brief: OpenAI Claims AI Disproved Exponential Time Hypothesis

**Today:** If you track frontier AI capability, model costs, or open-weight tools for document-heavy work, today's four stories matter. They are an unverified but potentially landmark research claim, a cheaper OpenAI model for routine work, and two open-weight releases.

## Top Stories

### 1. 🤖 **OpenAI Says Its Internal Models Refuted the Exponential Time Hypothesis**
*ForkLog · October 27, 2026*

**Bottom line:** OpenAI claims its unreleased internal models produced major results in computer science, mathematics and physics, but outside experts have not yet confirmed any of them.

On October 26, OpenAI said its internal models had refuted the Exponential Time Hypothesis (ETH). ETH is a 1999 conjecture that 3-SAT, a classic logic problem, cannot be solved in subexponential time, and hundreds of papers rely on it to show that problems are hard. OpenAI also claimed a proof of the local smoothing conjecture in all dimensions, which it says settles the Kakeya and Stein restriction conjectures. A third claim is an existence proof for quantum field theories including QCD and pure Yang–Mills. That proof does not address the mass gap, so it does not meet the full Millennium Prize condition.

A group led by Russell Impagliazzo and Ramamohan Paturi (UC San Diego) and Ryan Williams (MIT) will organize open verification of the ETH claim, and stresses that its role is not an endorsement. Nobel laureate David Gross leads the physics review. OpenAI says reviewers are unpaid and are not bound by NDAs. The result does not solve P vs NP, and the algorithm's runtime may still be extremely large in practice.

**Why it matters:** If the claim holds up, it would show AI producing new results that can be checked by machine (in the Lean proof assistant), not just helping people search for them. It also tests a new way of publishing, where AI output is treated as raw research data and experts review it before it is accepted as knowledge. Technical leaders should wait for the independent verification before treating this as a proven capability.

🔗 [Read the full story](https://forklog.com/en/openai-says-its-ai-refuted-the-exponential-time-hypothesis/)

---

### 2. 🤖 **OpenAI Launches GPT-6.1 Terra at Half the Price of Its Predecessor**
*InfoWorld · October 27, 2026*

**Bottom line:** OpenAI's new mid-tier model costs half as much per token as GPT-5.6 Terra, and on OpenAI's own figures it scores within a few points of its premium models on computer-use tasks.

GPT-6.1 Terra replaces GPT-5.6 Terra. It is priced in USD at $1.00 per million input tokens, $5.00 per million output tokens and $0.05 per million cached input tokens. On the Agents' Last Exam benchmark at max effort, it scored 60.0% at $1.01 per task, against 58.6% for GPT-6.1 Sol ($2.00) and 59.3% for GPT-6 Astra ($7.24). Claude Opus 5.5 led at 63.2% ($8.82 per task). On OSWorld 2.1 it reached 74.2%, behind Claude Sonnet 5.5 at 83.9%.

OpenAI says error rates on hard prompts at low reasoning effort fell from 53.6% to 16.7%. The model meets the Critical cybersecurity threshold under OpenAI's Preparedness Framework. All benchmark figures are OpenAI's own.

**Why it matters:** Analysts quoted in the piece name invoice processing and document analysis as target workloads, which are core to payments operations. They also caution that human review time can cancel out token savings. Firms should measure the cost of a correctly completed task, not just the price per token.

🔗 [Read the full story](https://www.infoworld.com/article/4241006/openai-bets-on-ai-economics-with-lower-cost-gpt-6-1-terra.html)

---

### 3. 🤖 **Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Documents**
*MarkTechPost · October 26, 2026*

**Bottom line:** Baidu's 3.34-billion-parameter OCR (text-recognition) model reads documents hundreds of pages long in one request, under the permissive MIT license.

Unlimited OCR 2 follows Baidu's June 2026 Unlimited-OCR and converts ordered page images into structured text. Baidu reports a score of 77.1 on MarathonDocBench (hundred-page documents) and 84.6 on the shorter MPDocBench. By comparison, Qwen3.8-Max falls from 78.3 to 22.9 as documents get longer, and the original Unlimited-OCR scored 0.0 on MarathonDocBench.

Each page costs 273 image tokens in multi-page mode. Baidu tested on a single NVIDIA A800-80GB GPU. All benchmark results are self-reported.

**Why it matters:** Long financial reports, contracts and onboarding document packs are a constant pain point in fintech operations. A small, permissively licensed model that can run on a firm's own hardware lets teams process these documents without sending data to a third-party API. That matters where data-protection rules such as PDPA apply, but independent testing on real documents should come before any production use.

🔗 [Read the full story](https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/)

---

### 4. 🤖 **vLLM Semantic Router Releases d3-ultra Open Decision Model**
*MarkTechPost · October 26, 2026*

**Bottom line:** d3-ultra is an Apache-2.0 open-weight model that does not write text. It reads an input once and returns a probability for each possible answer to a set of typed questions.

The model has 26.09 billion parameters and handles both text and images. In one call it can route requests, classify inputs and run visual and video checks. The team reports a score of 87.2 on its own SR-Text benchmark, and support for serving the model in vLLM Semantic Router's engine was added on October 25.

**Why it matters:** Decision models like this are becoming a separate tier of the AI stack, used for routing, guardrails and triage. They give back scores you can audit rather than free-form text, which makes them easier to set thresholds on and to explain. That suits regulated workflows such as sorting alerts.

🔗 [Read the full story](https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/)

---

## Key Takeaways
- AI labs are announcing bold results first and inviting outside experts to verify them afterward. Claims of AI discovery now need the same diligence as vendor benchmarks.
- Mid-tier models are cutting the cost of computer-use and document tasks. The real cost question is the price of a correct, reviewed result, not the price per token.
- Open-weight releases are increasingly specialized, covering long-document OCR and decision scoring. This lets regulated firms run focused tools on their own hardware instead of relying on general-purpose APIs.

## What to Watch
Watch for early findings from the Impagliazzo–Paturi–Williams group on the ETH claim. Also watch for independent benchmarks of GPT-6.1 Terra and Unlimited OCR 2, since all figures cited so far come from the vendors themselves.

---