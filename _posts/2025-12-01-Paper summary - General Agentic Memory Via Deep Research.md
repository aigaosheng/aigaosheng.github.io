---
layout: post
title: "Paper summary - General Agentic Memory Via Deep Research"
date: 2025-12-01 12:50:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- agent memory
- long-context
- retrieval
keywords: [agent memory, long-context, retrieval]
permalink: /Paper summary - General Agentic Memory Via Deep Research/
---

**Paper summary: General Agentic Memory Via Deep Research**

---

## 📚 Research topic and objective

* The paper addresses the problem of **memory management for AI agents** (e.g. agents based on large language models, LLMs) — specifically how to store, recall, and reuse past work or context when agents run long multi-step tasks (e.g. multi-step reasoning, research, tool use). ([arXiv][1])
* Classical memory systems often build a **static, compressed memory ahead-of-time (AOT)**. But that leads to **loss of detail** and poor adaptability if the future requests require fine-grained or unexpected info. ([arXiv][1])
* The objective: propose a new memory framework — **General Agentic Memory (GAM)** — that retains full history in a retrievable store, while summarizing key information in light memory; and when a request comes, dynamically “deep-researches” the store to build an optimized context tailored to that request. ([arXiv][1])

---

## 🧠 What is GAM — how it works

GAM uses a **two-part structure**:

* **Memorizer** (offline / as history accumulates):

  * When a new “session” (i.e. a unit of the agent’s past activity) arrives, the Memorizer produces a concise “memo” summarizing the important points. ([arXiv][1])
  * At the same time, it stores the full session (with context header) into a “page-store” (like a database / library of full history), so no raw information is lost. ([arXiv][1])

* **Researcher** (online, when a request arrives):

  * Given the client’s request + the lightweight memory, the Researcher plans what information is needed, then searches the page-store (using retrieval tools such as vector search, keyword search, or ID-based lookup). ([arXiv][1])
  * It integrates retrieved pages, reflects whether the result already suffices; if not, iterates — possibly retrieving more pages — until enough relevant context is collected. ([arXiv][1])
  * Returns to the client a **custom context**: small (efficient) but containing the right detailed info to perform the task. ([arXiv][1])

In effect: GAM trades some offline/online computation and retrieval effort for **lossless memory + flexible, request-specific context** rather than lossy, static summaries. ([arXiv][1])

They further formalize the design as an optimization problem: produce a context that is “as small as possible” while maximizing downstream task performance. ([arXiv][1])

---

## ✅ Key findings and conclusions

From their experiments (on multiple benchmarks), the authors find:

* GAM **consistently outperforms** both memory-free methods (e.g. using a long-context LLM directly, or simple retrieval-augmented generation (RAG)) **and existing memory-based methods** (which rely on static memory) on a broad range of tasks. ([arXiv][2])
* The improvement is especially large on **multi-hop reasoning tasks** requiring tracking and integrating information dispersed across long contexts (e.g. in benchmarks such as HotpotQA and RULER). For example, on RULER’s multi-hop tracing (MT) tasks, GAM achieves **over 90% accuracy**, while many baselines fail. ([arXiv][2])
* GAM’s performance remains **stable across different input-context lengths**, showing that it scales well even when history/context becomes very large. ([arXiv][2])
* The authors show that just increasing LLM context window (e.g. using “long-LLM”) is **not enough** — large context can still lead to degraded performance due to distraction by irrelevant content (a phenomenon known as “context rot”). ([arXiv][2])
* Ablation studies: combining multiple retrieval tools (embedding search + keyword + page-id) yields better performance than any single tool, and both the memorizer and researcher modules are **essential**. Using only memory (without researcher) or only researcher (without memory) dramatically degrades performance. ([arXiv][2])
* Finally, efficiency: GAM’s time cost (offline + online) remains **comparable** with other memory-based systems, and significantly better cost-effectiveness overall: i.e. the benefit in task performance justifies the extra computation. ([arXiv][2])

**Conclusion:** GAM appears to provide an effective, general-purpose memory architecture for LLM-based agents — one that preserves full historical information, yet delivers concise, optimized context on demand; this yields better task performance (especially for long-context and multi-step reasoning) and scales well in both length and complexity. ([arXiv][1])

---

## 🔢 Critical data & facts (especially experimental results)

* On the conversational memory benchmark (LoCoMo), across tasks (single-hop, multi-hop, temporal reasoning, open-domain), GAM achieves F1/BLEU-1 scores like **57.75 / 52.10** (etc.), noticeably higher than baselines such as long-LLM, RAG, MemoryOS, LightMem, etc. ([arXiv][2])
* On long-context reasoning benchmarks:

  * On HotpotQA (with large context: 56 K, 224 K, 448 K tokens), GAM obtains F1 scores like: **63.22, 64.56, 59.81** respectively. ([arXiv][2])
  * On RULER (128 K tokens), in the multi-hop tracing (MT) task: GAM gets **≈ 93.2%** (or “over 90%”) accuracy. ([arXiv][2])
  * On narrative-level tasks (e.g. NarrativeQA), GAM also significantly outperforms baselines, showing robustness over very long inputs (average ≈ 87 K tokens in their test subset). ([arXiv][1])
* Regarding module sensitivity: using a smaller LLM for the researcher degrades performance significantly; the memory module is less sensitive to size reduction. ([arXiv][2])
* Regarding efficiency: For HotpotQA tasks, total processing time (offline build + online serve) for GAM is comparable to other memory-based systems (e.g. similar order to “Mem0” or “MemoryOS”), and much faster than some heavy offline-compression methods. ([arXiv][2])

---

## 🧑‍🏫 What this means (for non-experts)

* For AI agents that need to handle **long histories, complex multi-step reasoning, or long documents** — using a memory system like GAM helps them **remember important details without losing information**, even if the history is huge.
* Instead of pre-compressing everything into a static summary (which might miss details needed later), the system keeps a full “library” + a lightweight index, and only pulls up what is relevant when needed. This is more flexible and powerful, especially when the agent faces **unexpected or complex requests**.
* The approach appears **general and domain-agnostic**, meaning such a memory system could benefit many kinds of AI-agent applications: research assistants, code generation, decision support, long-run dialogues, etc.
* Also suggests that simply giving LLMs a huge context window isn’t enough: you need smart memory management — storing raw material plus ability to dynamically retrieve relevant context.

---

[1]: https://arxiv.org/html/2511.18423v1 "General Agentic Memory Via Deep Research"
[2]: https://arxiv.org/pdf/2511.18423 "General Agentic Memory Via Deep Research"
