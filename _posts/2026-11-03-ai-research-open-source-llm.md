---
layout: post
title: "AI Research & Open-Source LLM Brief: Meituan Ships 1.6T LongCat-2.5 Model"
series: "AI Research & Open Source"
description: "Meituan launches its 1.6T-parameter LongCat-2.5 on homegrown chips, while MIT researchers use GPT-6 Astra to edit Qwen's weights directly."
date: 2026-11-03 19:26:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Meituan
keywords:
  - longcat-2.5 meituan
  - open source llm china
  - homegrown chip ai model
  - gpt-6 astra weight editing
  - qwen open weight model
permalink: /ai-research-open-source-llm-brief-2026-11-03/
---

# AI Research & Open-Source LLM Brief: Meituan Ships 1.6T LongCat-2.5 Model

**Today:** Two developments show open-weight AI research advancing on two fronts at once — scale and sovereignty in China, and a new technique for editing model internals directly, both with implications for how enterprises evaluate and deploy open models.

## Top Stories

### 1. 🤖 **Meituan Launches 1.6-Trillion-Parameter LongCat-2.5, Trained Entirely on Domestic Chips**

*Caixin Global · November 3, 2026*

**Bottom line:** Meituan's new LongCat-2.5 model, trained exclusively on Chinese-made chips, signals that domestic hardware can now support frontier-scale model training despite continued US export restrictions.

LongCat-2.5 is a native multimodal mixture-of-experts model with 1.6 trillion total parameters and roughly 48 billion active per token, built for long-horizon agentic work such as coding, browser use and spreadsheet tasks, with a 1-million-token context window. Caixin reported benchmark results placing it between Anthropic's Claude Opus 4.8 and Opus 5, though one developer described real-world performance as only "average." The model is currently available via API, with Meituan's predecessor model, LongCat-2.0, already open-sourced under the MIT license on Hugging Face, and further open releases reportedly planned.

**Why it matters:** For enterprise AI buyers, this is further evidence that Chinese labs can field frontier-scale models without leading-edge foreign chips, narrowing the capability gap that export controls were meant to preserve. For Asia-based fintechs evaluating model vendors, it adds another low-cost, high-capability option to the agentic-coding field, alongside pricing pressure on incumbent US model providers.

🔗 [Read the full story](https://www.caixinglobal.com/2026-11-03/meituan-unveils-new-ai-model-trained-on-homegrown-chips-102500305.html)

---

### 2. 🔬 **MIT Researchers Use GPT-6 Astra to Edit a Rival Model's Weights Directly, Lifting Math Scores Sixfold**

*VentureBeat · November 2, 2026*

**Bottom line:** MIT CSAIL researchers showed that a large model can directly rewrite a smaller open-source model's weights to fix specific capability gaps, without conventional gradient-based training, though the technique's practical limits were substantial.

Researchers fed OpenAI's GPT-6 Astra the weights of Qwen's open-source Qwen3.5-0.8B model along with natural-language instructions to improve math performance; Astra inspected the network and edited parameters directly, lifting the smaller model's MATH-500 score from 7.9% to 48.1% and GSM8K accuracy from 13.8% to 67.1% while altering only about 0.016% of its weights. VentureBeat reported the gain mainly came from fixing a repetition bug rather than adding new knowledge, the process took roughly 20 hours and 158 conversational turns to find the fix, and Astra failed to improve Google's Gemma 3, which didn't share the same flaw.

**Why it matters:** The result is an early, narrow proof of concept rather than a general method — researchers flagged that reproducibility, generalization and cost savings versus standard fine-tuning remain unestablished. Still, it points to a future tooling category where frontier models diagnose and patch open-weight models post hoc, relevant to any enterprise running fine-tuned open models in production.

🔗 [Read the full story](https://venturebeat.com/technology/like-gene-editing-for-neural-networks-mit-researchers-used-gpt-6-astra-to-edit-qwens-open-weights-directly-boosting-math-performance)

## Key Takeaways

- Chinese labs continue to prioritise domestic-chip training pipelines for frontier-scale models, a strategic response to US export controls that is narrowing rather than widening the US-China capability gap.
- Model editing research remains experimental: targeted weight edits can fix specific, diagnosable bugs cheaply, but are not yet a substitute for training or fine-tuning at scale.
- Open-weight releases from major labs (Meituan, Qwen ecosystem) keep arriving with a lag between API availability and public weights, a pattern enterprises should factor into deployment timelines.

## What to Watch

Watch for Meituan's promised GitHub and Hugging Face release of LongCat-2.5 weights, which would make the model independently verifiable and deployable on-premises, and for whether other labs attempt to replicate MIT's weight-editing approach on larger or differently-flawed models.

---
