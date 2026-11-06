---
layout: post
title: "AI Research & Open-Source LLM Brief: Thinking Machines Launches Inkling 2 Small"
series: "AI Research & Open Source"
description: "Thinking Machines Lab debuts Inkling 2 Small; Stanford-linked study finds cracks in coding benchmarks; NVIDIA speeds up robot planning."
date: 2026-11-06 19:09:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Thinking Machines Lab
  - NVIDIA
keywords:
  - inkling 2 small
  - thinking machines lab
  - open weight llm
  - terminal-bench benchmark reliability
  - ai coding benchmarks
  - diffusion language models
permalink: /ai-research-open-source-llm-brief-2026-11-06/
---

# AI Research & Open-Source LLM Brief: Thinking Machines Launches Inkling 2 Small

**Today:** A quieter research day still produced a credible new open-weight contender and a sobering study on benchmark reliability that enterprise AI buyers should read before trusting vendor leaderboard claims.

## Top Stories

### 1. 🤖 **Thinking Machines Lab Unveils 594B-Parameter Inkling 2 Small**

*Thinking Machines Lab · November 5, 2026*

**Bottom line:** Thinking Machines Lab, the startup founded by former OpenAI CTO Mira Murati, released Inkling 2 Small, a 594-billion-parameter mixture-of-experts model it plans to open-source under an Apache 2.0 licence within weeks, pending additional safety testing.

The model routes each token to 8 of 384 experts (17 billion active parameters) and trained on roughly 12.2 trillion tokens using Nvidia GB300 racks. The company's own benchmark figures show strong coding and finance-document scores among open-weight models, alongside disclosed weaknesses in chat conciseness and safety performance relative to closed rivals. It is available now only through Thinking Machines' Tinker platform, with downloadable weights to follow.

**Why it matters:** A well-funded, high-profile lab committing to a permissive licence widens the pool of self-hostable frontier-class models for enterprises that want to keep model weights and inference on their own infrastructure, an increasingly common ask from regulated financial institutions evaluating data-control tradeoffs.

🔗 [Read the full story](https://thinkingmachines.ai/news/inkling-2-small/)

---

### 2. 🤖 **Study Finds Nearly a Third of Terminal-Bench Coding Tasks Needed Fixes**

*arXiv preprint · November 5, 2026*

**Bottom line:** A new paper on AI coding benchmarks found that about 30% of tasks in Terminal-Bench 2.1, one of the most-cited agentic coding benchmarks, contained defects that required repair, with corrected scores shifting by more than 10 percentage points in places.

Researchers Kelly Buchanan, Crystal Zhou, Scott Linderman and Christopher Ré argue benchmarks accumulate "maintenance debt" as models improve and testing infrastructure changes, and that fixed time limits can swing measured performance by 20 to 30 percentage points independent of model quality. They propose a continuous-validation process combining community reports, automated checks and human review rather than one-off benchmark releases.

**Why it matters:** With open-weight vendors this week trading claims over narrow benchmark leads, the finding is a reminder that headline leaderboard scores can be unstable; enterprise buyers evaluating AI coding or agent tools should ask vendors how and when a benchmark was last revalidated, not just what score was reported.

🔗 [Read the full story](https://arxiv.org/abs/2611.08417)

---

### 3. 🤖 **NVIDIA Researchers Publish 25x-Faster Robot Planning Method**

*arXiv preprint (NVIDIA research team) · November 5, 2026*

**Bottom line:** NVIDIA researchers, including GEAR lab lead Jim Fan and VP of Research Jan Kautz, published VFlash, a decoding method that generates visual motion and navigation plans for robots and autonomous systems in one forward pass instead of token-by-token.

The paper reports roughly 25 times faster 3D motion forecasting and an increase in task success rate from 62.6% to 70.2% on tested robot-control benchmarks, by predicting structured spatial primitives such as points, boxes and trajectories directly rather than generating them autoregressively.

**Why it matters:** Cheaper, faster planning inference lowers the compute cost of deploying agentic robotics and physical-AI systems, an area NVIDIA is positioning as a core growth platform alongside its chip business.

🔗 [Read the full story](https://arxiv.org/abs/2611.08449)

---

### 4. 🤖 **New Method Speeds Up Diffusion Language Models by Up to 4.4x**

*arXiv preprint · November 5, 2026*

**Bottom line:** Researchers introduced SpecCTMC, a sampling method that cuts the number of sequential model evaluations needed to generate text with masked diffusion language models by 1.73 to 4.38 times, without changing the underlying output distribution.

Unlike the autoregressive transformers that power most commercial chatbots today, diffusion language models generate tokens non-sequentially; the authors describe an exact correction step that lets the method predict multiple token updates in parallel while mathematically preserving accuracy. Code for the method has been published publicly.

**Why it matters:** Diffusion-based LLMs are a growing architectural alternative pursued by several labs; efficiency gains like this narrow the cost gap with conventional autoregressive models, which matters for any business weighing inference costs in high-volume applications such as customer support or document processing.

🔗 [Read the full story](https://arxiv.org/abs/2611.08362)

## Key Takeaways

- The open-weight race keeps broadening beyond Chinese labs, but US entrants like Thinking Machines Lab are still gating full weight releases behind internal safety review, so "open" launches increasingly arrive in stages.
- Benchmark integrity is becoming a research topic in its own right, which should temper how much weight enterprise buyers put on single leaderboard scores when comparing AI vendors.
- Efficiency research in decoding and sampling is advancing alongside raw model capability, which over time should lower the cost of running agentic and multimodal AI in production.

## What to Watch

Watch for Thinking Machines Lab's promised Apache 2.0 weight release for Inkling 2 Small in the coming week, and whether Alibaba follows through on the Qwen4 launch window its executives flagged for early November.

---
