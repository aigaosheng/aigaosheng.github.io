---
layout: post
title: "AI Research & Open-Source LLM Brief - Reflection AI Releases Beam Weights Under Apache 2.0"
series: "AI Research & Open Source"
description: "Reflection AI releases Beam under Apache 2.0, Artificial Analysis benchmarks it, and Anthropic's Claude traces NIST ECDSA curve seeds."
date: 2026-10-17 19:41:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
- AI Research
- Open Source AI
- LLM
- Reflection AI
- Anthropic
keywords: [reflection ai beam, apache 2.0 open-weight llm, beam artificial analysis benchmark, us open-weight models, claude ecdsa curve seeds]
permalink: /ai-research-open-source-llm-brief-2026-10-17/
---

# AI Research & Open-Source LLM Brief: Reflection AI Releases Beam Weights Under Apache 2.0

**Today:** A new US open-weight model with permissive licensing lands with independent benchmark scores the same day, plus a company-reported AI research result on a 25-year-old cryptography puzzle.

## Top Stories

### 1. 🤖 **Reflection AI Releases Beam Weights Under Apache 2.0**
*Reflection AI · October 16, 2026*

**Bottom line:** Reflection AI has published the weights of its 501B-parameter Beam model under Apache 2.0, with more than 40 launch partners.

Beam is a sparse mixture-of-experts model with 501 billion total and 23 billion active parameters, aimed at coding, reasoning and long-horizon agent workloads. Reflection released BF16, FP8 and NVFP4 weights plus a speculative-decoding drafter, a model card with final benchmarks and a safety technical report. It lists day-zero support in Transformers, vLLM and SGLang, availability across major clouds and inference providers, and on-premises delivery through Dell and HPE. Self-distillation recipes for customization are promised in the coming days.

**Why it matters:** For regulated or data-sensitive enterprises in Asia, a permissively licensed model from a Western lab that can be self-hosted behind the firewall widens the open-weight options beyond Chinese-built models. Our read: the 40-plus partner launch suggests the competition is shifting from raw weights to deployment ecosystems.

🔗 [Read the full story](https://reflection.ai/blog/beam-is-available)

---

### 2. 🤖 **Artificial Analysis Ranks Beam Second Among US Open-Weight Models**
*Artificial Analysis · October 16, 2026*

**Bottom line:** An independent evaluator scores Beam 30 on its Intelligence Index, behind only Meta's Muse Spark Open (39) among US open-weight models.

Artificial Analysis places Beam tenth among all open-weight models, one point behind the UAE's K2 Horizon (31), and says Beam uses about 26,000 output tokens per task, roughly half of K2 Horizon. It scores 48.5% on AutomationBench-AA but only 3.0% on Terminal-Bench 4.0. On its knowledge test Beam answers 33% of questions correctly, yet its hallucination rate is 47%, against 26% for K2 Horizon and 30% for Qwen3.8 27B.

**Why it matters:** The profile is token-efficient and strong on agentic workflows but prone to confident wrong answers, so teams considering Beam for finance or compliance work would need retrieval and verification layers rather than trusting raw output.

🔗 [Read the full story](https://artificialanalysis.ai/articles/reflection-beam)

---

### 3. 🤖 **Anthropic Says Claude Traced the Origins of NIST ECDSA Curve Seeds**
*Anthropic · October 16, 2026*

**Bottom line:** Anthropic reports that Claude worked out in under half an hour how the seeds for several standard NIST elliptic curves were generated, and says the result is not a cryptographic break.

According to Anthropic, the P-192, P-224, P-256, P-384 and P-521 seeds were not hash outputs but the output of a 1990s C library random-number generator seeded with Unix timestamps. Claude also traced the base points of six curves to another library's generator, while the seed for the B-163 curve and the base points of four NIST curves remain unexplained. Anthropic says the finding makes deliberate backdoors in the curves less plausible, calls for no action by users, and is donating a $36,864 bounty to the Internet Security Research Group.

**Why it matters:** ECDSA is widely used in signing across payments and digital finance, so closing a long-running trust question is useful. It is also a company-reported example of a frontier model doing open-ended, checkable technical research, which independent cryptographers will want to reproduce.

🔗 [Read the full story](https://www.anthropic.com/research/ecdsa-curve-origins)

---

## Key Takeaways
- Open-weight launches now arrive with partner ecosystems and third-party benchmark scores on day one, not just downloadable weights.
- Capability and reliability diverge: Beam is efficient and agent-capable but hallucinates more than its closest peers.
- Labs are publishing self-verifiable research results, and independent replication is the test that matters.

## What to Watch
Reflection's promised self-distillation recipes for Beam, due in the coming days, and whether more independent evaluations confirm its hallucination and coding results.

---