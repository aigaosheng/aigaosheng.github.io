---
layout: post
title: AI Safety & Governance: Open-Source Tools & Benchmarks
date: 2025-09-07
type: post
published: true
status: publish
categories: []
tags:
- LLM evaluation
- AI safety
- AI goverance
- Benchmarks
- Open-Source Tools
---

---

# AI Safety & Governance Open-Source Tools & Benchmarks

- A curated list of open-source GitHub repositories for evaluating large language models (LLMs) across various dimensions of safety, fairness, and robustness.

| Dimension              | Tool / Benchmark | Description | GitHub Link |
| ---------------------- | ---------------- | ----------- | ----------- |
| **Accuracy & Factuality**  | TruthfulQA       | Tests whether models provide truthful answers or generate false information | [Link](https://github.com/sylinrl/TruthfulQA) |
|                        | MMLU-Pro          | Evaluates broad language understanding across multiple challenging tasks | [Link](https://github.com/TIGER-AI-Lab/MMLU-Pro) |
|                        | HELM              | Holistic Evaluation of Language Models across tasks and metrics | [Link](https://github.com/stanford-crfm/helm) |
| **Safety & Toxicity**  | ToxiGen          | Dataset for detecting subtle toxic language, especially targeting minority groups | [Link](https://github.com/microsoft/TOXIGEN) |
|                        | HELM (toxicity module) | Evaluates model outputs for toxicity using HELM framework | [Link](https://github.com/stanford-crfm/helm) |
|                        | Safety-Eval      | Tools for comprehensive safety evaluation of LLM outputs | [Link](https://github.com/allenai/safety-eval) |
| **Bias & Fairness**    | CrowS-Pairs      | Dataset to measure stereotypical biases in masked language models | [Link](https://github.com/i-gallegos/Fair-LLM-Benchmark) |
|                        | Fair-LLM-Benchmark | Compilation of bias evaluation datasets for fair model assessment | [Link](https://github.com/i-gallegos/Fair-LLM-Benchmark) |
|                        | FairLangProc     | Fairness metrics, datasets, and algorithms for NLP models | [Link](https://github.com/arturo-perez-peralta/FairLangProc) |
| **Robustness**         | AdvBench         | Benchmark to evaluate adversarial robustness of language models | [Link](https://github.com/IntelLabs/LLMart) |
|                        | JailbreakBench   | Tracks model vulnerabilities to jailbreaking attacks | [Link](https://github.com/JailbreakBench/jailbreakbench) |
|                        | BlackboxBench    | Benchmark for black-box adversarial attacks on LLMs | [Link](https://github.com/SCLBD/BlackboxBench) |
| **Conversational Quality** | MT-Bench       | Evaluates multi-turn conversational abilities of chat models | [Link](https://github.com/leobeeson/llm_benchmarks) |
|                        | Chatbot Arena    | Crowdsourced platform for evaluating chatbots in randomized battles | [Link](https://github.com/lm-sys/FastChat) |
|                        | BotChat          | Compares multi-turn conversational performance across different LLMs | [Link](https://github.com/open-compass/BotChat) |
| **Domain-Specific**    | HELM Enterprise Benchmark | Extends HELM for domain-specific datasets (finance, legal, etc.) | [Link](https://github.com/IBM/helm-enterprise-benchmark) |
|                        | MMLU-CF          | Contamination-free version of MMLU for rigorous evaluation | [Link](https://github.com/microsoft/MMLU-CF) |
|                        | Shopping MMLU    | Multi-task benchmark for LLMs on online shopping tasks | [Link](https://github.com/KL4805/ShoppingMMLU) |

---