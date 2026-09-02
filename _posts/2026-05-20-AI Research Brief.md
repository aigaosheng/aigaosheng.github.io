---
layout: post
title: "AI Research Brief — 2026-05-20"
series: "AI Research & Open Source"
description: "Nature Publishes Google DeepMind and FutureHouse AI Research Assistants · Google I/O 2026: \"Gemini for Science\" Suite Announced · Incyte Partners with…"
date: 2026-05-20 21:14:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI
- Scientific Discovery
- AI Agents
- LLM
- Biotech
keywords: [AI Research, Scientific Discovery, AI Agents, LLM Optimization, Biotech AI]
permalink: /AI-Research-Brief-2026-05-20/
---

### AI Research Brief — 2026-05-20

## Top Stories

### 1. Nature Publishes Google DeepMind and FutureHouse AI Research Assistants
- **Nature** · 2026-05-19
- **Summary**: Two separate multi-agent AI systems designed to accelerate scientific discovery were published in *Nature*. Google DeepMind’s "Co-Scientist" (built with Gemini 2.0) can generate novel hypotheses and propose drug candidates, while FutureHouse’s "Robin" (using OpenAI and Anthropic models) specializes in designing and interpreting experimental biology tests. Both systems are designed to augment, not replace, human researchers.
- **Why It Matters**: These papers provide rigorous, peer-reviewed validation that agentic workflows can navigate the full research loop—from literature review to experimental validation. This marks a shift from AI as a data-analysis tool to an autonomous reasoning partner in biomedicine.
- **URL**: [Accelerating scientific discovery with Co-Scientist](https://doi.org/10.1038/s41586-026-10644-y)

### 2. Google I/O 2026: "Gemini for Science" Suite Announced
- **Google I/O (via IT之家 & Digital Trends)** · 2026-05-20
- **Summary**: At its I/O developer conference, Google launched "Gemini for Science," an experimental suite designed to integrate AI deeper into research workflows. The suite features Hypothesis Generation (literature synthesis), Computational Discovery (automated experiment design), and Literature Insights (multimodal research summaries). Access is rolling out via Google Labs and Google Cloud.
- **Why It Matters**: This moves Google’s AI capabilities beyond general-purpose chatbots into specialized scientific domains. By integrating with over 30 life science databases, it targets the specific friction points of modern research (information overload and manual coding), potentially accelerating pre-competitive research phases significantly.
- **URL**: [AI system could speed up medical discoveries](https://www.scimex.org/newsfeed/ai-system-could-speed-up-medical-discoveries)

### 3. Incyte Partners with Edison Scientific to Deploy "Kosmos" AI Scientist
- **Business Wire** · 2026-05-19
- **Summary**: Biopharmaceutical giant Incyte announced a strategic collaboration with Edison Scientific (a FutureHouse spinoff) to embed the "Kosmos" AI platform across its R&D lifecycle. Unlike standard analysis tools, Kosmos will be integrated into discovery and translational biology to create a "learning system" from Incyte’s proprietary clinical and experimental data.
- **Why It Matters**: This represents a major commercial validation for agentic AI in pharma. Rather than a one-off analysis, Incyte is betting on a feedback loop where proprietary data becomes a compounding asset, potentially improving decision quality and pipeline productivity over time.
- **URL**: [Incyte and Edison Scientific Announce Strategic Collaboration](https://www.businesswire.com/news/home/20260519992433/en/Incyte-and-Edison-Scientific-Announce-Strategic-Collaboration-to-Employ-the-Kosmos-AI-Platform-for-Research-and-Development)

### 4. Recursive Superintelligence Achieves $4B Valuation to Build Self-Improving AI
- **The Seattle Times** · 2026-05-18
- **Summary**: A new startup, Recursive Superintelligence, has raised over $650 million (valued at $4B+) to pursue "recursive self-improvement"—AI systems that can improve their own code. Founded by veteran researcher Richard Socher and backed by Nvidia and AMD, the team includes alumni from OpenAI and Meta, alongside former Google research director Peter Norvig.
- **Why It Matters**: This signals a major influx of capital into the "automated AI researcher" space. If successful, it could decelerate the need for human-driven prompt engineering and accelerate the timeline to more general intelligence, though the industry remains divided on whether true human-out-of-the-loop recursion is currently feasible.
- **URL**: [Notable researchers join $4 billion effort to build self-improving AI](https://www.seattletimes.com/business/notable-researchers-join-4-billion-effort-to-build-self-improving-ai/)

### 5. Study Reveals LLM Agents as "Greedy Optimizers" in Code Generation
- **arXiv** · 2026-05-19
- **Summary**: A new study on LLM agents in hardware-aware code optimization reveals that models often fail to follow specific size instructions in zero-shot tasks and rely heavily on pre-trained priors rather than iterative feedback. The research found that while performance improves with CUDA feedback loops, it degrades when models operate with low-density languages like TVM IR.
- **Why It Matters**: This provides critical guardrails for AI research assistants. It suggests that simply wrapping an LLM in an agentic loop does not guarantee genuine optimization; performance is highly dependent on the density of the feedback language and the model's pre-existing internal priors, cautioning against over-reliance on LLMs for novel architecture search.
- **URL**: [Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization](https://export.arxiv.org/abs/2605.19782)

### 6. Multi-Model LLM Schedulers Face Performance Bottlenecks
- **arXiv** · 2026-05-19
- **Summary**: A study on multi-model LLM schedulers highlights significant inefficiencies in current serving systems. The research demonstrates that offloading layers to the CPU leads to non-linear degradation in decode throughput—particularly in smaller models—and that preemption overhead is dominated by model state reloading rather than key-value cache transfer.
- **Why It Matters**: As labs run multiple specialized agents (like Co-Scientist or Robin) concurrently, infrastructure efficiency becomes a bottleneck. This research provides the empirical data needed to design next-gen schedulers, informing how AI research platforms should allocate heterogeneous hardware to maintain low latency in agentic workflows.
- **URL**: [Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption](https://arxiv.org/abs/2605.19593)