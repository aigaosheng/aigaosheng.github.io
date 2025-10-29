---
layout: post
title: "Inside a Coder LLM - Architecture, RAG, Sandbox, and Training Data"
date: 2025-10-29 10:33:00 +0800
type: post
published: true
status: publish
categories: []
tags:

keywords: []
permalink: /Inside a Coder LLM - Architecture, RAG, Sandbox, and Training Data/
---
**Inside a Coder LLM: Architecture, RAG, Sandbox, and Training Data**

---

## 1) Product Scope & Core Features

Start with a lean MVP — **less is more**. Core capabilities:

* Natural-language → code generation (functions, classes, scripts).
* Code editing & refactoring on existing files.
* Code explanation & documentation (docstrings, inline comments).
* Unit-test generation + in-sandbox execution.
* Code diagnostics (linting, static analysis, fix suggestions).
* Project-level context via RAG (multi-file understanding).
* Git integration (diffs, suggested commits, review workflow).

---

## 2) High-Level Architecture

### **1. Frontend / UX**

* Web IDE or VSCode extension (editor, console, file tree, test runner).
* Chat-style interface + spec-to-code composer.

### **2. API / Orchestration Layer**

* Request gateway (auth, rate limits, telemetry).
* Orchestrator coordinating LLM, retriever, sandbox, and evaluation tools.

### **3. Model Layer**

* Base model (open weights or cloud-hosted).
* Fine-tuned coder model (SFT ± RLHF).
* Model serving stack (vLLM/Triton/FastAPI; GPU or quantized CPU).

### **4. Retrieval & Context Store**

* Vector DB (FAISS / Milvus / Chroma) indexing codebases & docs.
* Chunking + embeddings (OpenAI / SentenceTransformers).

### **5. Execution Sandbox**

* Isolated, resource-limited runtime (container per job).
* Virtualized file IO / no host leakage.

### **6. Developer Tooling**

* Linters, static analyzers, formatters, type-checkers.
* pytest test runner, security scanners (bandit/Snyk).

### **7. Observability**

* Metrics, logs, traces, latency dashboards.
* Human-in-the-loop feedback collection (accept/reject signals).

### **8. Storage**

* Metadata DB (Postgres).
* Artifact + model storage (S3/object store).

---

## 3) Data Strategy

Training sources:

* **Public permissive code**: The Stack (license-aware), CodeSearchNet, BigQuery GH samples.
* **Spec→code datasets**: docstring→implementation, before→after refactors.
* **Unit tests**: synthetic + curated sets (MBPP, HumanEval).
* **Golden examples**: internal high-quality reference implementations.
* **Feedback loop**: collect edit diffs + accept/reject labels.

> Strong focus on license auditing and provenance tracking.

---

## 4) Model Selection & Fine-Tuning

Two starting options:

| Option                                   | Pros              | Use Case                 |
| ---------------------------------------- | ----------------- | ------------------------ |
| Hosted APIs (OpenAI/Anthropic)           | Fastest MVP       | Iteration & prototyping  |
| Open-source (Llama3, Mistral, StarCoder) | Control & on-prem | Long-term / cost control |

Training stages:

1. Base model selection
2. Supervised fine-tuning (instruction/code pairs)
3. (Optional) RLHF / preference modeling
4. Safety & secure defaults tuning
5. Quantization / distillation for deployment

---

## 5) Prompting & Decoding Strategy

* Structured prompts: task + constraints + file context.
* Few-shot templates where relevant.
* Stepwise: **plan → code → tests**.
* Deterministic decoding for code (temp 0.0–0.2).
* n-best sampling + re-ranking using static checks / test passes.

---

## 6) RAG for Multi-File Context

* Embed and index repo files.
* Retrieve top-K relevant chunks per request.
* Show provenance (file + line ranges).
* Cache embeddings and auto-refresh on commit.

---

## 7) Execution & Feedback Loop

1. Generate code/tests.
2. Run in sandbox.
3. If failing → automated debugging loop.
4. Show diff + commit suggestion.
5. Log user’s decision → future SFT training data.

---

## 8) Safety, Security, & IP

* Isolated sandbox (no outbound network).
* Redaction of secrets / credentials.
* Prevent malicious OS instructions.
* License provenance + attribution.
* Opt-in/opt-out data retention for user code.

---

## 9) Evaluation & Metrics

* Functional correctness (HumanEval-style pass rate).
* Runtime/latency.
* Edit quality (rated).
* Insecure pattern rate.
* User accept-rate.

---

## 10) Infra & Deployment

* **Training**: AWS/GCP/cluster GPU, DeepSpeed/Accelerate.
* **Serving**: vLLM / Triton; quantized models for local mode.
* **Retriever**: FAISS/Milvus.
* **Ops**: K8s (later), GitHub Actions CI, Prometheus/Grafana.

---

## 11) Developer UX Principles

* Zero-friction onboarding: paste → generate → run.
* Explainability: provenance & “why this change”.
* Preview diffs & commit recommendations.
* Human always in control of patch application.

---

## 12) Minimal MVP Flow

1. User prompt + repo context.
2. RAG: fetch relevant code chunks.
3. Model generates code/tests.
4. Sandbox validation.
5. Show patch + commit option.

---

## 13) First Experiments / Ablations

* SFT vs SFT+RLHF vs API.
* RAG sensitivity (on/off).
* Temp sweeps + candidate reranking.
* Model family comparison (StarCoder/Llama3/Mistral).

---

## 14) Example Server-Side Orchestrator

```python
def handle_request(spec, repo_files):
    chunks = chunk_and_embed(repo_files)
    ctx = retrieve_top_k(chunks, spec, k=6)
    prompt = build_prompt(spec, ctx)
    candidates = model.generate_n(prompt, n=3, temperature=0.1)
    ranked = rerank_by_static_checks_and_tests(candidates)
    best = ranked[0]
    test_results = run_in_sandbox(best.tests, best.code)
    return {
        "code": best.code,
        "tests": best.tests,
        "test_results": test_results,
        "candidates": ranked
    }
```

---

## 15) Telemetry & Human Labeling

* Log prompt + output + test results.
* Collect accept/reject labels.
* Feed back into SFT pipeline.

---

## 16) Legal & Ethical Checklist

* Clear license terms for generated code.
* Attribution handling where retrieval is used.
* User data isolation & opt-out controls.

---

## 17) Long-Term Evolution

* Whole-project refactors.
* Multi-model orchestration.
* Local/offline privacy-preserving mode.
* CI integration for auto-suggested patches.

---

## ✅ 18) Training Progression (with real dataset samples)

| Stage | Name         | Data Style                        | Goal                                        |
| ----- | ------------ | --------------------------------- | ------------------------------------------- |
| 1     | **Pretrain** | raw code (no prompts)             | teach programming syntax & style            |
| 2     | **Finetune** | spec/docstring → code             | teach mapping “what to build → how to code” |
| 3     | **SFT**      | chat-style structured completions | align with agent workflows                  |

---

### 🟩 Stage 1: Pretraining Sample (raw code only)

No prompts. No JSON. Just code tokens. The model learns patterns, syntax, and idioms.

✅ Good pretraining sample:

```python
def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    while b:
        a, b = b, a % b
    return a
```

Another multi-file snippet (reflecting real-world distribution):

```javascript
export function throttle(fn, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            fn.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
```

> This teaches “how code *looks and behaves*” — no supervision.

---

### 🟨 Stage 2: Fine-Tuning Sample (spec → code)

Partial supervision. The model isn't “chatting” yet — it’s learning to *fulfill a coding request*.

Format is usually `<INPUT> … <OUTPUT>` or JSON-like pairs.

✅ Example 1 — docstring → code

```
<INPUT>
"Write a function that returns the nth Fibonacci number (0-indexed)."
<OUTPUT>
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

✅ Example 2 — signature → implementation

```
<INPUT>
def max_value(nums: list[int]) -> int:
<OUTPUT>
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val
```

✅ Example 3 — tests → code

```
<INPUT>
assert reverse_string("abc") == "cba"
assert reverse_string("") == ""
<OUTPUT>
def reverse_string(s: str) -> str:
    return s[::-1]
```

> Fine-tune stage = learns “given a spec → generate implementation”.

---

### 🟦 Stage 3: SFT (Instruction Fine-Tuning) — agent-style structured training

Now it becomes a *coding agent*: multi-turn, tool-aware, structured output, reasoning steps, patch updates.

✅ Example 1 — Chat-style instruction

````json
{
  "prompt": "Write a Python function that loads a JSON file and returns it as a dict.",
  "completion": "```python\ndef load_json(path: str) -> dict:\n    \"\"\"Load a JSON file and return its contents as a dictionary.\"\"\"\n    import json\n    with open(path) as f:\n        return json.load(f)\n```"
}
````

✅ Example 2 — RAG / existing project context

````json
{
  "prompt": "Here is utils.py:\n```python\ndef read_file(path):\n    with open(path) as f:\n        return f.read()\n```\nAdd a helper `read_lines(path)` consistent with the existing style.",
  "completion": "```python\ndef read_lines(path: str) -> list[str]:\n    return read_file(path).splitlines()\n```"
}
````

✅ Example 3 — Structured output for agent workflow

````json
{
  "prompt": "Implement a sliding-window moving average in Python.",
  "completion": "### PLAN\n1. Validate window size\n2. Use numpy for speed\n\n### CODE\n```python\nimport numpy as np\n\ndef moving_average(arr, window):\n    if window <= 0:\n        raise ValueError(\"window must be > 0\")\n    return np.convolve(arr, np.ones(window) / window, mode='valid')\n```"
}
````

---

## ✅ Side-by-Side Comparison

| Stage     | Input               | Output Style                | Example Input    | Example Output |
| --------- | ------------------- | --------------------------- | ---------------- | -------------- |
| Pretrain  | None                | raw code                    | `<code>`         | `<next token>` |
| Fine-tune | spec/test/signature | code only                   | docstring        | function       |
| SFT       | chat prompt         | code + structured reasoning | full instruction | plan + code    |

---
