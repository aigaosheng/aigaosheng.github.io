---
layout: post
title: "AI Research & Open-Source LLM Brief: Jensen Huang's Exit Clouds Nvidia Open-Source Push"
series: "AI Research & Open Source"
description: "Nvidia leadership shake-up clouds open-source AI bets; Google launches Gemini 4 Hydrogen; Thinking Machines opens Inkling 2 Small weights."
date: 2026-11-13 19:24:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Nvidia
  - Google
keywords:
  - gemini 4 hydrogen release
  - inkling 2 small open weights
  - nvidia jensen huang resignation open source
  - ibm granite llmon prompt injection
  - thinking machines apache 2.0 model
permalink: /ai-research-open-source-llm-brief-2026-11-13/
---

# AI Research & Open-Source LLM Brief: Jensen Huang's Exit Clouds Nvidia Open-Source Push

**Today:** A leadership shake-up at Nvidia lands alongside fresh model releases from Google, Thinking Machines and IBM, leaving enterprise AI buyers with new options even as the biggest open-source AI backer's future stance is in question.

## Top Stories

### 1. 🌐 **Jensen Huang's Nvidia Exit Raises Doubts Over Open-Source AI Commitment**

*TechCrunch · November 12, 2026*

**Bottom line:** Nvidia CEO Jensen Huang resigned after disclosing an affair with an alleged Chinese intelligence operative, leaving open-source AI advocates uncertain whether the company will keep backing open-weight models and its pending Hugging Face deal.

Nvidia named CFO Colette Kress interim CEO following the resignation, which also raised national-security questions about Huang's past lobbying for looser US chip export rules to China. Huang had personally championed Nvidia's open-weight Nemotron model family, backed open-model startup Reflection AI, and co-signed a letter with Microsoft, Meta and IBM opposing US restrictions on open AI models. Nvidia's roughly $13 billion acquisition of Hugging Face also remains unfinalized; Hugging Face's CEO said the company would keep "fighting for open source," but Kress's approach to the deal and the broader ecosystem is untested.

**Why it matters:** A leadership change at the world's dominant AI-chip maker could reshape how aggressively the US backs open-weight models against a fast-advancing Chinese open-source ecosystem led by DeepSeek, Kimi and GLM — a dynamic that enterprise AI buyers in Asia, including fintechs evaluating model vendors, should watch closely.

🔗 [Read the full story](https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/)

---

### 2. 🤖 **Google Launches Gemini 4 Hydrogen For Agentic Workflows**

*Google · November 12, 2026*

**Bottom line:** Google rolled out Gemini 4 Hydrogen as its new default, high-speed model for coding and agentic workloads, replacing Gemini 3.8 Flash across Search, the Gemini app and its developer APIs.

Positioned beneath flagship reasoning models Gemini 4 Carbon and Argon, Hydrogen runs tasks roughly 2.5 times faster than its predecessor, triples scores on Terminal-Bench 4.1 (57% versus 18.2%), and cuts fabricated claims by more than fivefold, according to Google's own benchmarks. It carries a 1-million-token context window priced at $1.50 per million input tokens and $7.50 per million output tokens.

**Why it matters:** As the default model now powering Google Search and enterprise Gemini API tiers, Hydrogen's speed and pricing will shape the economics of agentic-workflow deployment for enterprises, including fintech back-office and customer-service automation.

🔗 [Read the full story](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

---

### 3. 🤖 **Thinking Machines Opens Inkling 2 Small's 594B-Parameter Weights**

*Hugging Face · November 12, 2026*

**Bottom line:** Mira Murati's Thinking Machines Lab converted Inkling 2 Small from a closed, hosted-only model into a fully downloadable open-weight release under Apache 2.0, a week after its initial launch.

The 594-billion-parameter mixture-of-experts model, which activates 17 billion parameters per token, is now available on Hugging Face and hosting partners including Together AI, Nvidia and Fireworks, with no per-token charge for self-hosting. Independent benchmark comparisons show mixed results against Chinese open models: Inkling trails DeepSeek on coding tests such as FrontierCode v2.0, but outperforms GLM-5.3-Flash and Kimi K3 on several measures, and the lab has not yet published promised external red-teaming results.

**Why it matters:** The release adds a credible US-built entrant to an open-weight field increasingly dominated by Chinese labs, giving enterprises another self-hostable option for regulated environments — though unresolved safety-testing disclosure may give risk-conscious adopters pause.

🔗 [Read the full story](https://huggingface.co/thinkingmachines/Inkling-2-Small)

---

### 4. 🔒 **IBM Releases Granite Models Trained To Resist Prompt Injection**

*IBM / Hugging Face · November 12, 2026*

**Bottom line:** IBM's Granite team open-sourced two experimental models — Granite-4.1-3B and 8B LLMON-preview — built to detect and ignore instructions hidden inside untrusted data, a common attack vector against AI agents.

The models are trained on LLMON, an XML-like markup that explicitly separates trusted instructions from retrieved or tool-supplied data. IBM reports the technique cut indirect prompt-injection attack success rates from 53-100% down to as low as 0.02-5.6% on its internal benchmark, while keeping general task performance broadly in line with standard Granite 4.1 Instruct models. Both are released under Apache 2.0, explicitly for research and evaluation rather than production use.

**Why it matters:** As banks and fintechs deploy AI agents with access to internal systems and customer data, structural defenses against prompt injection could become a meaningful factor in vendor selection — though IBM itself cautions the approach is "not an enforced guarantee."

🔗 [Read the full story](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)

## Key Takeaways

- Leadership transitions at AI infrastructure giants can ripple into open-source strategy and the broader US-China open-model competition, beyond any single model release.
- Major labs are increasingly shipping fast, cheap "default" models optimized for agentic workflows rather than raw reasoning power, reshaping the cost calculus for enterprise AI deployment.
- Open-weight competition is intensifying across US (Thinking Machines) and Chinese (DeepSeek, Kimi, GLM) labs, while security-focused open releases like IBM's LLMON signal growing attention to agentic-AI risk as adoption scales.

## What to Watch

Watch for whether Nvidia's interim CEO Colette Kress reaffirms support for Nemotron and the pending Hugging Face acquisition, and for Thinking Machines to publish the external red-teaming results it promised for Inkling 2 Small.

---
