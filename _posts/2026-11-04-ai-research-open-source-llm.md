---
layout: post
title: "AI Research & Open-Source LLM Brief: Tencent Launches Full Hy4 Model"
series: "AI Research & Open Source"
description: "Tencent ships its full 770B Hy4 model, Xpeng open-sources GroundingPI, and new research cuts LLM reasoning and compute costs."
date: 2026-11-04 19:37:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Tencent
keywords:
  - tencent hunyuan hy4
  - xpeng groundingpi open source
  - open weight llm november 2026
  - llm reasoning efficiency research
  - china open source ai models
permalink: /ai-research-open-source-llm-brief-2026-11-04/
---

# AI Research & Open-Source LLM Brief: Tencent Launches Full Hy4 Model

**Today:** Chinese labs dominated the day's model news, with Tencent and Xpeng both shipping major releases while new research chipped away at the compute and token costs that drive enterprise AI budgets.

## Top Stories

### 1. 🤖 **Tencent Ships Full Hy4 Model With Vision and Computer Use**

*Unite.AI · November 4, 2026*

**Bottom line:** Tencent's full Hy4 release adds vision and computer-operation skills to its 770-billion-parameter model while sharply cutting hallucination rates, though the open weights are still pending.

Tencent scaled up pre-training and post-training from the August preview, and Hy4 can now read fine-grained images and complex charts and operate command-line and graphical interfaces, including Blender, CAD and game engines. Tencent reported hallucinations fell from 15.76% to 5.45% and speculative errors from 23.1% to 5.6%, with Hy4 ranking first among open-weight models on a finance evaluation. Weights and a system card are promised for a later release rather than today.

**Why it matters:** Enterprise teams benchmarking open-weight alternatives to US frontier models now have a stronger, cheaper multimodal option from China, though the delayed weights mean deployment-ready open access isn't here yet; Tencent also said it limited cybersecurity training data to defensive use cases, a safety pattern Asian and Western labs are converging on.

🔗 [Read the full story](https://www.unite.ai/tencent-releases-full-hy4-model-with-vision-and-computer-use/)

---

### 2. 🤖 **Xpeng Open-Sources Perception Model Beating GPT-6 Astra**

*CnEVPost · November 4, 2026*

**Bottom line:** Chinese EV maker Xpeng open-sourced GroundingPI, a compact 4-billion-parameter perception model that outscored OpenAI's GPT-6 Astra on a 34-benchmark suite.

Developed with Peking University and the University of Hong Kong, GroundingPI scored 73.68 against GPT-6 Astra's 71.54 across detection, text recognition and spatial-localization tasks, trained entirely on perception data without robot action labels. Xpeng says systems built on it need only half the demonstration data of baseline approaches to match performance, and the code and weights are posted on GitHub and Hugging Face.

**Why it matters:** An automaker open-sourcing a foundation model that beats a leading US lab's benchmark underscores how fast China's auto and tech sector is feeding back into general-purpose AI research, a trend enterprise AI buyers in Asia should track when evaluating vendor diversity beyond the US hyperscalers.

🔗 [Read the full story](https://cnevpost.com/2026/11/04/xpeng-unveils-groundingpi-pre-trained-model/)

---

### 3. 🔬 **New Method Cuts LLM Reasoning Length by Up to 45%**

*arXiv (Tencent / Xi'an Jiaotong University) · November 3, 2026*

**Bottom line:** Researchers introduced LoCo, a training method that teaches reasoning models when to stop "thinking" early, cutting output length without hurting accuracy.

LoCo identifies points where a model keeps reasoning unnecessarily, generates shorter verified alternative completions, and trains on the resulting preference pairs. The method reduced completion length by 41.7–45.4% on math problems and 23.4–36.3% on code generation, and transferred from math training to code tasks without additional tuning.

**Why it matters:** Reasoning-model inference costs are a growing line item for enterprises running agentic workloads; a validated way to trim token output by roughly 40% without losing accuracy directly lowers the cost of deploying chain-of-thought models at scale.

🔗 [Read the full story](https://arxiv.org/abs/2611.04814)

---

### 4. 🔬 **Byte-Level Model Claims 7,600x Compute Savings**

*arXiv · November 3, 2026*

**Bottom line:** A new architecture called DeepMem reports matching or beating byte-level transformer performance while needing roughly 7,600 times fewer FLOPs at its compute bottleneck.

DeepMem separates semantic compression from exact byte preservation using a multiscale, invertible transform, outperforming a matched byte-level transformer on the FineWeb-Edu and PG19 datasets and achieving the best average performance across the FLORES multilingual benchmark. The efficiency gain applies specifically to the model's bottleneck refinement stage rather than end-to-end training.

**Why it matters:** If the efficiency claims hold up under independent replication, byte-level architectures like this could meaningfully lower the infrastructure cost of training and running large multilingual models, a direct input cost for any firm building or licensing foundation models.

🔗 [Read the full story](https://arxiv.org/abs/2611.05255)

---

## Key Takeaways

- China's model cadence remains relentless, with Tencent and Xpeng both shipping notable releases on the same day, reinforcing open-weight competition even where full weights are delayed, as with Hy4.
- Research focus is shifting from raw capability toward efficiency, with LoCo and DeepMem both targeting the token and compute costs that determine real-world deployment economics.
- Chinese labs are explicitly building safety guardrails into open releases, such as Tencent's restriction of cybersecurity training data to defensive use cases, as a response to dual-use concerns.

## What to Watch

Watch for Tencent's promised release of Hy4's open weights and system card, and whether Alibaba's Qwen4, teased for the week of November 2-8 at Apsara Amsterdam, actually ships with confirmed open weights.

---
