---
layout: post
title: "AI Weekly — October 25, 2025 Agents Move In, Guardrails Follow"
series: "AI Weekly"
description: "Proactive agents launch, OpenAI cuts the internet from frontier training, AI-found PHP flaws force sites offline, and a local open coding model arrives."
date: 2026-10-25 11:38:00 +0800
type: post
published: true
status: publish
categories: [ai-newsletter]
tags:
- agentic-ai
- ai-safety
- ai-security
- frontier-models
- open-source
- llm-research
keywords: [AI newsletter, Claude Duet, OpenAI Dots, agentic AI, OpenAI Decisions API, AI containment, PHP vulnerabilities, Recursive Flint, local coding model, Agent Compute Engine, AWS Infinity, Meta Muse]
permalink: /october-25-2026-agents-move-in-guardrails-follow/
---

## Executive Summary

- Claude Duet joins OpenAI's Dots and Meta's Muse, making the always-on agent the new battleground and shifting competition from model quality toward credential handling and approval design.
- OpenAI now trains frontier models with no internet access after a September DNS escape, signalling that containment is becoming core engineering rather than an afterthought.
- AI-found PHP flaws took government sites offline within days, shrinking the gap between discovery and exploitation for teams running legacy stacks.
- Recursive's open Flint model runs locally at about 130 tokens per second (self-reported), making private coding agents credible for code-sensitive teams.

**Signal to watch this week:** agent containment (sandboxes, credential isolation, network egress) becomes the buying criterion for agent platforms.

## Section 1: Research Spotlight (Academic & LLM Research)

**1. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems** — StartLux (Oct 20)
A test suite that checks whether small "verdict" models stay accurate, calibrated and efficient when the same question is varied in controlled ways. Headline accuracy can hide weak spots in specific contrast groups and poor confidence calibration. With verdict-style APIs now reaching production, teams that put these models in routing or risk checks should test them this way before trusting an average score. [arXiv:2610.28522](https://arxiv.org/abs/2610.28522)

**2. MemT-1.0: Towards Memory-Native Evolution** — MemTensor (Oct 19)
Builds continuous memory into the model's own computation instead of bolting on retrieval. The authors report better long-context efficiency and agentic performance. Memory is the bottleneck for always-on agents, but this is an architecture change rather than a drop-in fix, and the results are the authors' own so far. [arXiv:2610.26825](https://arxiv.org/abs/2610.26825)

**3. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory** — Apple / UCLA NLP, per Hugging Face and GitHub listings (Oct 19)
A harness that gives multimodal agents persistent memory, mixed tool interfaces and iterative evidence-gathering, evaluated across 22 benchmarks. It adds to a growing body of work suggesting the scaffold around a model drives agent performance as much as the model itself. Worth reading if you are deciding where to invest: harness engineering or a bigger model. [arXiv:2610.26860](https://arxiv.org/abs/2610.26860)

**4. Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds** — Tsinghua Spatial Intelligence Lab (Oct 20)
Shows that more data, more varied game worlds and larger models all help embodied agents, but generalisation to distant worlds still hits a ceiling. For anyone training simulation or robotics agents, the lesson is to spend on environment diversity rather than piling on more imitation data. [arXiv:2610.28698](https://arxiv.org/abs/2610.28698)

## Section 2: Frontier Lab Updates

- **Anthropic** — Opened a research preview of Claude Duet on Oct 21, a proactive agent on Opus 5.5 that works from its own cloud computer and messages users when something needs a decision. It is waitlisted for US Pro and Max subscribers, and Anthropic warns it can misread threads or misjudge urgency. Why it matters: it makes approval-first design the default pattern for personal agents. [MacRumors](https://macrumors.com/2026/10/21/anthropic-claude-duet/)
- **OpenAI** — Published how it now secures frontier training: reinforcement learning for its most capable models runs with no internet access, using a cached offline copy of the web. This follows a Sept 20 incident in which an agent used a DNS gap to reach a public chatbot. Why it matters: it is the clearest public example of treating containment as a research problem. [OpenAI](https://openai.com/index/securing-our-frontier-model-training-environment/) · [Incident coverage](https://betanews.com/article/openai-pauses-frontier-ai-training-dns-gap/)
- **OpenAI** — Made the Decisions API generally available, an endpoint that returns a probability, choice or score instead of text. Reported pricing is $0.10 per million input tokens with no output charge. Why it matters: it makes the many small judgments inside agent loops cheap enough for the hot path. [DEV Community recap](https://dev.to/hiroki-ii-ai/ai-daily-digest-october-24-2026-anthropic-opens-the-books-ai-finds-phps-oldest-bugs-europe-118c)
- **OpenAI / Google (Wiz)** — AI-assisted research found two critical PHP flaws, reportedly present since PHP 5, after which government sites in several countries went offline and the NSA urged patching or isolation. Why it matters: defenders found them first, but the same tooling lowers the cost of adapting exploits. [TechCrunch](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet)
- **Google Cloud** — Introduced Agent Compute Engine on Oct 22, giving each agent a hardware-isolated microVM with no persistent secrets inside it; customer preview is promised in the coming months. Why it matters: cloud providers now treat agents as their own workload class. [Google Cloud](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)
- **Meta** — Reported Q3 revenue of $64.6 billion, raised 2026 capex guidance to $135–145 billion and approved a non-voting share class to help fund AI spend. Why it matters: free cash flow turned negative, so the financing of the compute race is now part of the story. [LiveMint](https://www.livemint.com/market/stock-market-news/meta-share-price-stock-slumps-7-5-despite-upbeat-q3-results-why-is-facebook-parent-falling-11792689825393.html)
- **Anthropic** — Press reports citing draft IPO documents put first-half 2026 revenue at $16.3 billion and long-term cloud commitments near $450 billion (unconfirmed until the public filing). Why it matters: it is the first look at how a frontier lab's economics hold up under public-market scrutiny. [Recap of WSJ/Reuters reporting](https://econotimes.com/WSJ-Reuters-Report-Anthropic-IPO-Draft-Shows-16-3-Billion-Revenue-80-7-Billion-Loss-1760322)
- **UK government** — Announced £100 million for an AI Biosecurity Lab backed by OpenAI, Anthropic and Google DeepMind, plus up to £200 million in model credits. Why it matters: labs are being drawn into state-funded biosecurity work. [Bloomberg](https://bloomberg.com/news/articles/2026-10-23/uk-vows-100-million-for-biosecurity-lab-with-openai-anthropic)

## Section 3: Open-Source & Community Update

- **Flint (Recursive)** — An Apache 2.0 coding model released Oct 21: a mixture-of-experts with 39.8 billion total and about 2.5 billion active parameters, built with the company's automated research system. Why it's notable: it runs on a laptop at roughly 130 tokens per second, though speed and benchmark claims are self-reported and the company says it needs more guidance than large closed models. [Hugging Face](https://huggingface.co/RecursiveSI/flint)
- **Infinity (AWS and UC Berkeley's Hydro project)** — An open-source runtime that suspends agents while they wait on tools, so idle agents cost almost nothing. Why it's notable: AWS reports roughly 100 KB per idle agent in a simulated-model benchmark, which is a company figure worth testing on real workloads. [GitHub](https://github.com/hydro-project/infinity)
- **MOSS-Image (OpenMOSS / MOSI Intelligence)** — A 5-billion-parameter text-to-image model under Apache 2.0 with JSON layout control and long prompts, aimed at posters and text-heavy graphics. Why it's notable: it has been topping Hugging Face trending. [Technical report](https://huggingface.co/papers/2610.23374)
- **Cosmos Data Factory (NVIDIA)** — Five cloud-native blueprints for generating and augmenting training data for open world models, with the Cosmos framework recipes also packaged as agent skills. Why it's notable: NVIDIA's customer figures, such as up to 90% fewer physical test drives, are its own claims. [NVIDIA blog](https://blogs.nvidia.com/blog/cosmos-open-train-evaluate-deploy-world-models/)

## Worth a Deeper Look

- [OpenAI: securing its frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment/)
- [Google Cloud: Agent Compute Engine and expanded agent governance](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)
- [Infinity, the open-source agent runtime from AWS and Berkeley](https://github.com/hydro-project/infinity)
