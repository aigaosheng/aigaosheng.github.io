---
layout: post
title: "Choosing a Reranker - Cohere Rerank 3.5 vs Opensource Reranker LLM Model"
date: 2026-07-02 12:27:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- RAG
- AI
- Agentic AI
- Enterprise AI
keywords: [Reranker, RAG, Enterprise AI]
permalink: /Choosing-a-Reranker-Cohere-Rerank-vs-Opensource-2026-07-02/
---
# Choosing a Reranker - Cohere Rerank 3.5 vs Opensource Reranker LLM Model

Reranking is the quiet workhorse of a good RAG pipeline. Your vector search casts a wide net; the reranker does the second-pass reasoning that decides what actually rises to the top. Picking one looks simple until you try to compare a managed API against an open-weight model — because they aren't priced, hosted, or even benchmarked the same way.

Here's a practical walk through that comparison, using two strong contenders: **Cohere Rerank 3.5** (managed, via Amazon Bedrock) and **Qwen3-Reranker-0.6B** (open weights, self-hosted).

---

## First, a benchmark caveat

There is no public benchmark that scores both models on the same footing. Qwen's numbers come from its own MTEB-based evaluation. Cohere's come from vendor benchmarks on curated domain sets. So treat any cross-model quality delta as directional, not decimal-precise — and plan to validate on your own data before committing.

---

## The landscape: why these aren't all the same category

Before narrowing to two models, it helps to see the field. Rerankers split along two axes — **modality** (text-only vs multimodal) and **deployment** (open weights you self-host vs a proprietary managed API) — and models sitting in different quadrants aren't really interchangeable.

| Model | Params | Modality | Context | Access | Notable strength |
|---|---|---|---|---|---|
| BAAI/bge-reranker-v2-m3 | ~568M | Text only | 8k | Apache-2.0, self-host | Mature, cheap, low-latency baseline |
| Qwen/Qwen3-Reranker-0.6B | 0.6B | Text only | 32k | Apache-2.0, self-host | Strong text + code reranking, instruction-aware |
| Qwen/Qwen3-VL-Reranker-2B | 2B | Text + image + video | 32k | Self-host | Multimodal / visual-document reranking |
| Cohere Rerank 3.5 | Undisclosed | Text only | 4096 | Proprietary API | Enterprise-tuned, 100+ languages, zero ops |

For a text-heavy pipeline, two of these filter out quickly:

- **BGE-v2-m3** is the veteran baseline — lean, fast, and cheap to run. Worth keeping as a latency fallback, but Qwen3-0.6B generally beats it on English, multilingual, and code reranking, so it's rarely the first choice for a new build.
- **Qwen3-VL-Reranker-2B** only earns its place if you're reranking *visual* content — scanned documents, screenshots, slide decks, or anything where layout carries meaning. For pure text it's overkill and slower.

That leaves the two realistic contenders for most text RAG systems: the strongest small open model (**Qwen3-Reranker-0.6B**) and the leading managed option (**Cohere Rerank 3.5**). The rest of this post focuses on them.

---

## The head-to-head

| Dimension | Cohere Rerank 3.5 (Bedrock) | Qwen3-Reranker-0.6B |
|---|---|---|
| Type | Proprietary managed API | Open weights (Apache-2.0), self-host |
| Architecture | Cross-encoder | Decoder LLM scoring a yes/no relevance token |
| Params | Undisclosed | 0.6B |
| Context | 4096 tokens | 32k tokens |
| Per-doc limit (Bedrock path) | 512 tokens incl. query | None beyond the 32k window |
| Multilingual | 100+ languages, tuned on 10 major ones | 100+ languages |
| Instruction-aware | No | Yes |
| Cost | Per query (~$2 / 1k searches) | Compute only |
| Ops burden | Zero — one API call | You run the serving stack |

**Quality.** Qwen3-0.6B punches above its size. On Qwen's own top-100 reranking evaluation it lands around 65.8 on MTEB-R (English), 66.4 on MMTEB-R (multilingual), and 73.4 on MTEB-Code — ahead of older open baselines like bge-reranker-v2-m3 on English, multilingual, and code. Cohere doesn't publish MTEB reranking figures, but positions Rerank 3.5 as strong on BEIR and enterprise domains (finance, e-commerce, hospitality) with solid handling of semi-structured data like tables, code, and JSON. The honest read: Cohere is validated hard on enterprise domains; Qwen3-0.6B is a strong general open model you should validate on your own corpus.

**Context.** Qwen3-0.6B's 32k window reranks long documents in a single pass. Cohere's is 4096, and on Bedrock specifically each document is capped at 512 tokens (query included) and split if longer — which means more chunking for long content.

**Latency.** Cohere gives elastic throughput with zero effort, at the cost of a network round-trip. Qwen3-0.6B, being LLM-style, has higher per-pair compute than a lean classic cross-encoder, but self-hosting removes the round-trip and gives more predictable tail latency.

---

## Context window vs the Bedrock per-document limit

A subtle point worth spelling out, because both are measured in tokens and easily conflated:

- **Context** is a property of the *model* — how much text it can reason over in one scoring pass (query + one document).
- **Per-doc limit** is a cap the *Bedrock Rerank API* layers on top: each document may be up to 512 tokens including the query, and anything longer is broken into multiple documents before scoring.

So the model could attend to 4096 tokens, but the Bedrock API won't hand it a single document larger than 512 — it chunks first. A self-hosted model has no such second layer; its per-doc and context limits are the same number.

Worth noting: the 512 limit is a Bedrock-path behaviour, not an inherent property of the model. Calling Cohere's own API directly is governed by the 4096 model context instead.

---

## How managed reranking actually bills

The intuitive reading — "1,000 documents means 1,000 things to rank" — is wrong. Cohere on Bedrock bills by **chunks reranked per search**, not documents in your store.

- A query holds up to **100 document chunks**. More than 100 counts as multiple queries (350 documents = 4 queries).
- Each chunk is up to 512 tokens; longer documents are split into several chunks.

### Worked example: 1,000 documents, ~10 pages each

Assumptions (adjust to your data):
- ~650 tokens/page → ~6,500 tokens/document
- 512-token chunk cap, ~490 usable after the query → ~14 chunks/document
- 1,000 docs × 14 ≈ **14,000 chunks total**
- Working rate: ~$2.00 per 1,000 searches

**Scenario A — brute force (rank the whole corpus per query):**
14,000 chunks ÷ 100 = 140 billed queries → **$0.28 per search.** At 1,000 searches/day that's ~$8,400/month. Nobody reranks this way in production — it defeats the two-stage design.

**Scenario B — realistic RAG (rerank only the retrieved top candidates):**
Retrieve top 100 chunks, rerank those → 100 chunks = 1 query = **$0.002 per search.** At 30,000 searches/month, that's about **$60/month.**

**The lesson:** rerank cost scales with *(searches × candidates reranked per search)* and is essentially independent of how big your corpus is. Corpus size only affects your index and the one-time brute-force cost. The two levers that move the meter are search volume and candidate depth — and reranking on every step of an agentic loop quietly multiplies both.

A self-hosted model has no per-query meter at all; you pay only for compute.

---

## What about self-hosting the open model on AWS?

"Serverless" on AWS means three different things, and only one is a true GPU fit.

- **SageMaker Serverless Inference (CPU only)** — the only true scale-to-zero option. No GPU. A 0.6B decoder reranker on CPU is slow (hundreds of ms to seconds, plus cold starts). Very cheap (~$5–30/month at 30k searches) but likely misses "real-time." Fine only for loose latency or spiky low volume.
- **SageMaker Real-Time Endpoint on a small GPU** — the practical real-time path. A single A10G-class instance runs ~$1.00–1.40/hr on-demand. Not scale-to-zero, so cost is dominated by hours the endpoint exists, not requests served.
- **Bedrock Custom Model Import** — bills per active model-unit window; tends to cost more than a right-sized SageMaker endpoint with less control.

**Cost at ~100 candidates/search, ~30k searches/month, real-time:**

| Approach | Rough monthly cost | Real-time? |
|---|---|---|
| Managed API (Scenario B) | ~$60 | Yes, zero ops |
| Self-host — Serverless CPU | ~$5–30 | Marginal |
| Self-host — small GPU, business hours | ~$220–300 | Yes |
| Self-host — small GPU, 24/7 | ~$730–1,000 | Yes |

**Break-even:** at 30k searches/month, the managed API is cheaper than a warm GPU endpoint. Self-hosting on rented cloud GPU only wins on cost once the GPU's fixed hourly cost divides below the per-query rate — roughly **350k+ searches/month** against a ~$730/month warm endpoint. Below that, managed is cheaper *and* zero-ops. Above it, self-hosting pulls ahead with flat marginal cost.

Two things shift the crossover: **owned hardware** (if you already have the GPU, marginal cost is effectively zero and self-hosting wins broadly), and **batching** (if "real-time" tolerates a little queueing, one small GPU absorbs far more traffic, lowering the break-even).

---

## The recommendation

- **Own hardware / edge deployment:** self-host the open model. Long context, instruction steering, zero marginal cost, and data never leaves your environment.
- **Cloud serving, low-to-mid volume (< ~350k searches/month):** use the managed API. Cheaper than a warm GPU and zero ops.
- **Cloud serving, high volume (> ~350k searches/month):** self-host on a right-sized GPU endpoint with batching.
- **Multimodal needs (scanned or visual documents):** evaluate a dedicated multimodal reranker for those paths only — a text reranker is the wrong tool there.

And the rule that overrides all of the above: **don't trust a leaderboard lead as proof for your use case.** Build a small evaluation — a few hundred labelled query/document pairs from your own data, scored on nDCG@10 and MRR — and run both models. That number reflects your data. The vendor benchmarks don't.

---

*Cost figures are working estimates. Confirm current provider pricing and cloud instance rates, and run a quick load test, before putting anything in a budget.*
