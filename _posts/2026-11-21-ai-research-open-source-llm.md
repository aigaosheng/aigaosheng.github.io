---
layout: post
title: "AI Research & Open-Source LLM Brief: Thinking Machines Releases Inkling 2 Mini"
series: "AI Research & Open Source"
description: "Thinking Machines Lab releases the 26B-parameter Inkling 2 Mini under Apache 2.0, while Tencent publishes Hy4 flash weights and Moonshot AI claims the largest open model with Kimi K3.1 Pro."
date: 2026-11-21 21:07:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Thinking Machines
  - Tencent
keywords: open-weight llm release, inkling 2 mini, tencent hy4 flash, kimi k3.1 pro, looped transformer
permalink: /ai-research-open-source-llm-brief-2026-11-21/
---

# AI Research & Open-Source LLM Brief: Thinking Machines Releases Inkling 2 Mini

**Today:** Three significant open-weight model releases landed within 48 hours, led by Thinking Machines Lab's efficient looped architecture that runs on a laptop, signaling intensifying competition in the small-and-capable open model segment.

## Top Stories

### 1. 🤖 **Thinking Machines Lab Releases Inkling 2 Mini, a 26B Looped Transformer Under Apache 2.0**

*OrcaRouter · Nov 20, 2026*

**Bottom line:** Thinking Machines Lab has released a 26.4B-parameter multimodal model that uses a looped transformer architecture to achieve competitive reasoning performance at roughly 20GB, making it deployable on a single high-memory laptop.

The model activates 3.4B parameters per token and runs its middle twelve layers three times, effectively performing 48 layer applications from 24 stored layers . It scored 20.1 on Artificial Analysis' Intelligence Index v5.0.1, priced at $0.15 per million input tokens and $0.50 per million output tokens . The Apache 2.0 license permits unrestricted commercial use, and the checkpoint is available on Hugging Face alongside support for vLLM, SGLang, and llama.cpp .

**Why it matters:** The looped design demonstrates a viable path to stronger reasoning without proportional parameter growth—a critical efficiency lever for enterprises weighing local deployment against API costs. For Asia-based teams with data residency requirements, a permissively licensed model of this capability opens new architectural options.

🔗 [Read the full story](https://www.orcarouter.ai/blog/inkling-2-mini-released-looped-transformer)

---

### 2. 🤖 **Tencent Publishes Hy4 Flash Weights, Completing Full Hy4 Series Open-Source Release**

*Lucien Engelen · Nov 20, 2026*

**Bottom line:** Tencent has released the full weights for Hy4 flash, a 224B-parameter mixture-of-experts model with 12B active parameters, under a custom license that imposes thresholds on large-scale commercial resellers.

The release follows the Hy4 model and includes instruct, FP8, and base checkpoints on Hugging Face . The Tencent Hy License requires a separate written agreement for model-as-a-service businesses exceeding $50 million in annual revenue or products with more than 100 million monthly users . In Tencent's own blind test with 85 users, Hy4 flash scored 2.79 out of 4 against Claude Haiku 5.5's 2.81, at RMB 0.26 per task .

**Why it matters:** Tencent's license structure signals a deliberate middle path between fully permissive open weights and closed APIs—allowing broad community use while retaining commercial leverage at scale. This template may influence how Chinese labs approach open-weight strategies amid competitive pressure from smaller, faster-moving rivals.

🔗 [Read the full story](https://www.lucienengelen.com/Blog-open-source-ai-daily-2026-11-21.dc.html)

---

### 3. 📊 **Moonshot AI Releases Kimi K3.1 Pro Weights, Claims Largest Open-Source Model by Parameters**

*Gate News · Nov 21, 2026*

**Bottom line:** Moonshot AI has published the complete weights for Kimi K3.1 Pro, which the company describes as the largest open-source model by parameter count, citing a People's Daily report.

The release introduces a hybrid linear attention mechanism designed to process long-context text at lower cost and improve training stability for very large models . The report notes that cumulative global downloads of Chinese open-source models have surpassed 10 billion . Specific parameter counts and benchmark scores were not disclosed in the available source.

**Why it matters:** If verified, this represents a significant escalation in the open-weight parameter race, potentially shifting expectations for what "open" models can match in raw scale. Enterprise buyers should watch for independent benchmarks to assess whether the hybrid attention approach delivers practical efficiency gains.

🔗 [Read the full story](https://www.gatewebsite.com/zh-tw/news/detail/kimi-k31-pro-open-weight-model-pushes-chinese-ai-to-100-billion-downloads-25763755)

---

### 4. 🤖 **Anthropic Mathematician Claims Claude Assisted in Riemann Hypothesis Proof**

*AIToolsRecap / La Nación · Nov 20, 2026*

**Bottom line:** An Anthropic mathematician announced that working with Claude, he discovered a proof of the Riemann Hypothesis and its generalized form, though the claim awaits independent verification.

Levent Alpoge published a four-page document and formalized proof code in Lean, stating the work took under six weeks with Claude's participation . Hours later, Stanford mathematician Ravi Vakil announced a separate 940-page human-authored proof draft of the generalized hypothesis, which he said represents 12 years of research . The Clay Mathematics Institute requires peer-reviewed publication and a two-year scrutiny period for its $1 million Millennium Prize .

**Why it matters:** While unverified, the claim underscores how frontier labs are positioning AI as a tool for breakthrough scientific reasoning—a narrative with implications for research funding and talent competition. The parallel human proof highlights ongoing debate about attribution and the appropriate role of AI in foundational mathematics.

🔗 [Read the full story](https://cdn-www.lanacionpy.arcpublishing.com/mundo/2026/11/21/investigador-de-anthropic-dice-que-claude-resolvio-un-problema-matematico-de-160-anos/)

---

## Key Takeaways

- **Efficiency over scale is gaining traction:** Thinking Machines' looped architecture and Tencent's sparse MoE design both prioritize inference cost and deployability over raw parameter counts, reflecting enterprise demand for practical local deployment.
- **Licensing is the new battleground:** Tencent's custom license with commercial thresholds signals that Chinese labs are experimenting with open-weight release strategies that preserve upside for large-scale monetization.
- **Verification gaps persist:** Both the Kimi K3.1 Pro parameter claim and the Claude-assisted mathematical proof require independent validation before enterprises should treat them as established facts.

## What to Watch

Independent benchmark results for Inkling 2 Mini on agentic coding tasks, and whether Moonshot AI publishes detailed technical specifications for Kimi K3.1 Pro that allow direct comparison with Tencent's Hy4 series.