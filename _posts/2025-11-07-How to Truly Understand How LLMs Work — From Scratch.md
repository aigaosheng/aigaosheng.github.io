---
layout: post
title: "How to Truly Understand How LLMs Work — From Scratch"
date: 2025-11-07 16:26:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- LLM Training
- Fine-Tuning Models
- Hands-on AI Learning
keywords: [Train your own ChatGPT, Build LLM from scratch,Hugging Face fine-tuning tutorial]
permalink: /How to Truly Understand How LLMs Work — From Scratch/
---

### How to Truly Understand How LLMs Work — From Scratch

If you’re genuinely interested in how ChatGPT or any other large language model (LLM) is trained end-to-end, **the best way is to read and debug the code locally.**

I prefer a **step-by-step debugging approach** — comparing actual code with the algorithms described in research papers. You’ll gain much more **hands-on, practical understanding** this way than just by reading papers.

A great starting point is:
👉 [karpathy/nanochat](https://github.com/karpathy/nanochat) (Python) — a minimal chat model built from scratch that’s easy to understand.

---

### For Those Who Love Low-Level Details

If you’re familiar with **C/C++**, you can dive even deeper into the implementation level:

* [karpathy/llama2.c](https://github.com/karpathy/llama2.c)
* [karpathy’s GitHub](https://github.com/karpathy)

These repositories reveal how each component of an LLM works under the hood — from tokenization to attention to optimization. Once you grasp these details, you can even **optimize C/C++ computation for specific hardware**, improving efficiency or adapting for embedded or edge devices.

---

### Fine-Tuning Existing Models

If you want to **fine-tune open-source models**, use the **[Hugging Face Transformers](https://huggingface.co/docs/transformers)** framework. It supports models like **Qwen, Gemma**, and many others.

You can fine-tune them on your own domain data to improve performance for **niche or specialized applications** — such as legal text, finance, healthcare, or any vertical where data specificity matters.

---

### Hardware Isn’t a Barrier

You don’t need high-end GPUs to start learning. A **consumer GPU with ~10GB VRAM** is enough.
Just tune the parameters (model size, batch size, sequence length, etc.) until your hardware can handle it. The key is to **learn by experimentation**, not just by reading.

---

### My Learning Project

I’ve also forked and started my own experimental repo:
👉 [tiny-llm-learn](https://github.com/aigaosheng/tiny-llm-learn)

My approach:

> **Read → Debug → Modify → Test → Build**

Through this cycle, you’ll be able to create **your own small, niche, and practical LLMs** tailored for specific applications — without needing a data center.

---

💡 **Takeaway:**
Learning LLMs is not just about understanding the math — it’s about connecting **theory with code**. Start small, explore the internals, and gradually build up to models that solve real problems.

---