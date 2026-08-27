---
layout: post
title: "How Alibaba Is Making “Research Agents” Cheap (No APIs Needed)"
date: 2025-09-28 10:23:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Agentic Artificial Intelligence

---
---
## 🔍 How Alibaba Is Making “Research Agents” Cheap (No APIs Needed)

>
Imagine teaching your AI agent to independently do deep research — web browsing, fact-checking, creative planning — *without* paying a single APTemplateI usage fee. Alibaba’s new method may just turn that dream into reality.

Their trick? An offline data synthesis pipeline that empowers open models to gain “agentic” behaviors before ever seeing a human prompt. That means you build smarter agents in-house, without bleeding dollars on external APIs. Let me walk you through how it works — and why it’s a big deal.

---

## Why Agentic AI Is the New Frontier

In older AI systems, “alignment” meant nudging a language model to produce outputs that humans like. But when your model starts *acting* — chaining tools, self-correcting, rethinking strategy — alignment needs to evolve too. You need **agentic alignment**: the capacity for sustained, safe, goal-oriented behavior in dynamic situations.

Most current methods, like supervised fine-tuning (SFT) or reinforcement learning (RL), struggle here. They tend to overfit to specific behavior traces (i.e. imitate examples) rather than *learn* how to strategize when conditions shift. Alibaba’s researchers argue those approaches miss the inductive bias needed for real agentic behavior. ([Venturebeat][1])

---

## Agentic Continual Pre-training (Agentic CPT): The “Middle Stage” Magic

Alibaba introduces a new training stage, **Agentic CPT**, sandwiched between foundation-model pretraining and downstream fine-tuning. The idea is to produce a “pre-aligned” base model already endowed with agentic instincts. ([Venturebeat][1])

### Two core principles:

1. **Diverse data sources** — don’t restrict yourself to one domain.
2. **Rich behaviors** — include many modes of agentic behavior so the model doesn’t just memorize patterns.

Compared to systems that only post-train on small trajectory sets (e.g. WebSailor), Agentic CPT floods the model with extensive agentic data **before** fine-tuning. ([Venturebeat][1])

The training is broken into two stages:

* **Stage 1**: ~200 billion tokens of agentic data + knowledge reasoning, with 32K context windows
* **Stage 2**: ~100 billion tokens of *higher-quality* data, expanding to 128K context, focusing on complex action planning ([Venturebeat][1])

This gives the model a robust internal foundation for planning, adapting, and rerouting when things go wrong.

---

## The Cost Killer: Offline Data Synthesis (No API, No Human Labels)

One of the most powerful innovations here is how Alibaba *generates* the training data — without external API calls or massive human annotation. That’s because they're doing everything *offline*.

They rely on two synthesis modules:

* **First-order Action Synthesis (FAS):** Converts raw aggregated data into structured “open-world memory” and generates diverse question-answer / task instances.
* **Higher-order Action Synthesis (HAS):** Instead of giving just one correct path, HAS generates *multiple reasoning paths* per task. This pushes the model to understand branching choices.

Together, they let the model see many possible paths — not just the one “canonical” solution. Crucially, both operate entirely offline — no constant API billing. ([Venturebeat][1])

---

## Meet AgentFounder: Alibaba’s Deep Research Agent

Using Agentic CPT, Alibaba built **AgentFounder**, based on Qwen3-30B. The results are impressive:

* Outperforms all open-source agents on several web-search benchmarks
* On the BrowseComp benchmark, exceeds DeepSeek-V3.1 by ~10 percentage points ([Venturebeat][1])
* First open-source system to surpass 30 points on Humanity’s Last Exam (HLE) ([Venturebeat][1])
* Scores 75.3% on Academic Browse, beating other models by a solid margin ([Venturebeat][1])

In practice, that means more reliable, actionable agents for tasks like market analysis, competitive research, literature review, etc. For enterprise use, this also unlocks on-premise deployment and tighter control over data. ([Venturebeat][1])

Alibaba suggests pairing human oversight into the loop, especially for high-stakes decisions—so AI does the heavy lifting, but humans still stay in the driver’s seat.

---

## Why It Matters (and What’s Next)

This is a potential shift in how enterprises build research-grade AI agents. Instead of relying on expensive API usage (or black-box LLMs), organizations could train their own capable agents — tailored to proprietary tools or data — without breaking the bank.

Since the core technique is open-source, we may see more labs adopt Agentic CPT and offline data synthesis in their workflows. One vision: in the near future, many complex tasks may be solvable with *just smart prompt engineering*, because the underlying agent is already aligned.

However, the usual caveats apply: edge cases, hallucinations, domain mismatch. Always good to keep human guards and review mechanisms in place.

---

## Glossary

| Term                                    | Definition                                                                                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agentic Alignment**                   | The capability of an AI agent to behave in a sustained, goal-directed way consistent with human intentions across multiple steps and in unpredictable environments |
| **Foundation Model**                    | A base model trained on broad data; often adapted or fine-tuned for downstream tasks                                                                               |
| **Post-training**                       | The stage after a base model is trained, typically involving domain-specific fine-tuning                                                                           |
| **Agentic CPT**                         | Alibaba’s *Agentic Continual Pre-training* — a middle training stage to embed agentic behavior before traditional fine-tuning                                      |
| **First-order Action Synthesis (FAS)**  | The method of generating basic agentic training data by structuring raw knowledge into tasks/scenarios                                                             |
| **Higher-order Action Synthesis (HAS)** | The method of building multiple alternative reasoning paths for a given task to encourage flexible planning                                                        |
| **Qwen3-30B**                           | The 30-billion-parameter open model used as the base for AgentFounder                                                                                              |

---

**Source:** *Build research agents without API costs: Alibaba’s offline data synthesis breakthrough* — VentureBeat
([https://venturebeat.com/ai/build-research-agents-without-api-costs-alibabas-offline-data-synthesis](https://venturebeat.com/ai/build-research-agents-without-api-costs-alibabas-offline-data-synthesis))

[1]: https://venturebeat.com/ai/build-research-agents-without-api-costs-alibabas-offline-data-synthesis "Build research agents without API costs: Alibaba's offline data synthesis breakthrough | VentureBeat"
