---
layout: post
title: "AI Research & Open-Source LLM Brief: GPT-6.2 Sol Rivals Claude Opus 5.5 on Cost"
series: "AI Research & Open Source"
description: "The New Stack tests OpenAI's GPT-6.2 Sol against Claude Opus 5.5; Nvidia and Factory lift Nemotron 3 Ultra; Artificial Analysis rates GPT-6.2 style."
date: 2026-11-22 19:50:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - OpenAI
  - Nvidia
keywords:
  - gpt-6.2 sol vs claude opus 5.5
  - llm cost per task benchmark
  - nemotron 3 ultra post-training
  - artificial analysis personalitybench
  - formal verification gpu kernels
permalink: /ai-research-open-source-llm-brief-2026-11-22/
---

# AI Research & Open-Source LLM Brief: GPT-6.2 Sol Rivals Claude Opus 5.5 on Cost

**Today:** Independent tests and research reports published since Saturday evening give enterprise AI teams fresh evidence on model cost per task, post-training for open-weight models, and the trade-offs behind OpenAI's latest style changes.

## Top Stories

### 1. 🤖 **Independent Test: GPT-6.2 Sol Ties Claude Opus 5.5 on Two of Three Tasks at Far Lower Cost**

*The New Stack · November 21, 2026*

**Bottom line:** In one reviewer's hands-on comparison, OpenAI's GPT-6.2 Sol matched or nearly matched Claude Opus 5.5 on accuracy while costing under a fifth as much.

The New Stack's author ran both models once each on an agent task, a coding task and a data-analysis task. Opus 5.5 scored 173 out of 173 on the month-end close task and Sol scored 169, because Sol missed one customer credit. Both models scored perfectly on the billing-library and lab-data tasks. Estimated spend across the three tests was about $2.79 for Opus 5.5 and $0.51 for Sol, with Sol also finishing in roughly half the time. The article lists Sol at $2 per million input tokens and $10 per million output tokens, half of Opus 5.5's list price.

**Why it matters:** The results come from a single run per test by one reviewer, so they are a data point rather than a verdict, and they only partly support OpenAI's own accuracy charts. For fintech and payments teams in Singapore and across Asia running high-volume agent workflows, cost per task is increasingly a bigger selection factor than small accuracy gaps. The reviewer's own advice is to start with Sol on lower-risk work and keep Opus 5.5 as a final check where errors are costly.

🔗 [Read the full story](https://thenewstack.io/gpt-6-2-sol-vs-claude-opus-5-5/)

---

### 2. 🤖 **Nvidia Used Factory's Coding Agent to Generate Post-Training Data for Open Nemotron 3 Ultra**

*The New Stack · November 21, 2026*

**Bottom line:** Nvidia reports that agent-trace data and a reinforcement-learning method called PivotRL lifted its open Nemotron 3 Ultra model's Terminal-Bench 2.0 score from 38.5% to 49%.

According to a Factory case study cited by the article, Nvidia ran Factory's Droid coding-agent harness in an air-gapped network. It used the harness to capture reproducible failures in instruction following, tool calling and error recovery, producing roughly 20,000 rows of post-training data. The article also reports a preliminary Nemotron 3.5 Super VL checkpoint rising from 52.11% to 60.4% on Terminal-Bench 2.1. It notes that Factory has not published an ablation isolating its own contribution. It also reports a separate Hugging Face result, from the company's CEO, in which a Qwen 3.8 27B variant tuned for the Pi harness rose from 39.5% to 55.8% on Terminal-Bench 2.1.

**Why it matters:** The numbers are vendor-reported and not independently reproduced, but they point to harness-specific post-training as a cheap route to better agent performance from open-weight models. That matters to Asian banks and payment firms that want to self-host models for data-residency reasons and tune them on their own workflows.

🔗 [Read the full story](https://thenewstack.io/nvidia-droid-harness-nemotron/)

---

### 3. 🤖 **Artificial Analysis Finds GPT-6.2 Astra and Sol Give Shorter Answers and Admit Uncertainty Less**

*The Decoder · November 22, 2026*

**Bottom line:** An Artificial Analysis style benchmark shows OpenAI's GPT-6.2 models answer more directly but score well below Anthropic's models on transparency.

The Decoder reports that Astra's average answer length fell from 352 to 210 words and Sol's from 337 to 223 words. On the benchmark's "Admits Uncertainty" trait, Astra dropped from 96 to 24 and Sol from 98 to 51. These are relative rankings on a 1 to 100 scale, not rates of behaviour. On the Transparency index, Astra scored 41 and Sol 57, against 81 for Claude Fable 5.2 and 90 for Opus 5.5. The benchmark, AA-PersonalityBench, uses 900 questions with AI judges and measures communication style rather than accuracy.

**Why it matters:** For regulated settings such as credit, advice and customer service, a model that rarely flags uncertainty is a design risk even if its answers read cleanly. Teams should test candidate models on how they hedge, not only on how often they are right.

🔗 [Read the full story](https://the-decoder.com/gpt-6-2-astra-and-sol-get-to-the-point-faster-but-score-lower-on-transparency-than-claude/)

---

### 4. 🤖 **Columbia and CertiK Researchers Introduce TensorLean to Formally Verify GPU Kernels**

*MarkTechPost · November 22, 2026*

**Bottom line:** The TensorLean framework reportedly proved 83 of 149 checked GPU kernel instances correct and found 38 correctness bugs across six projects.

Per MarkTechPost's report, the Lean-based verifier works on compiled PTX code and checks properties such as freedom from data races, termination and output correctness within a tolerance. The kernels checked include FlashAttention-2, -3 and -4 and DeepGEMM, targeting A100, H100 and B200 GPUs. The researchers say it caught a FlashAttention-4 data race that did not show up in 17,760 test runs. These are the authors' reported results, summarised secondhand.

**Why it matters:** Inference and training stacks rest on hand-tuned kernels, and subtle bugs there can silently degrade model output. Formal verification of this kind is early-stage research, but it is a relevant signal for institutions in Singapore and Asia that expect assurance evidence for AI infrastructure.

🔗 [Read the full story](https://www.marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels/)

---

### 5. 🤖 **Nvidia Researchers Argue Very Large Context Windows Are Often Unnecessary**

*The Decoder · November 21, 2026*

**Bottom line:** An Nvidia research team says periodic summaries and targeted lookups often work about as well as feeding a model an entire document set.

The Decoder reports that the team considers huge context windows frequently overkill and expensive. In many of the team's tests, the lighter approaches matched the long-context results. Only the opening of the report was publicly readable, so the specific benchmarks and the underlying paper could not be verified here.

**Why it matters:** If the finding holds, retrieval and summarisation pipelines could cut token costs for document-heavy work such as KYC files, contracts and filings. Treat it as a hypothesis to test on your own data until the paper's methods are available.

🔗 [Read the full story](https://the-decoder.com/nvidia-researchers-argue-huge-ai-context-windows-are-a-dead-end/)

## Key Takeaways

- Cost per completed task is becoming the main differentiator between frontier models, and one independent test suggests list-price comparisons understate the gap.
- Open-weight models are improving through post-training on agent traces, but the headline gains so far are vendor-reported and lack ablations.
- Style and transparency metrics, such as how often a model admits uncertainty, are emerging as separate selection criteria from raw accuracy.

## What to Watch

Look for independent re-runs of the Sol versus Opus 5.5 comparison and any published ablation of Factory's contribution to Nemotron's gains. Also watch for the underlying paper behind Nvidia's context-window claims and for AA-PersonalityBench entries for additional models.

  

---