---
layout: post
title: "Introducing ReasoningBank: AI Agents That Learn from Experience"
date: 2025-10-09 23:45:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI Agent Memory

---
---
[![New memory framework builds AI agents that can handle the real world's unpredictability | VentureBeat](https://images.openai.com/thumbnails/url/2zwsK3icu5meUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7RLfAt9qiIz4gs9kwyN_DM8gitSPQOcHcJjCgqD3Zz0_XKLUxMS6809TBMVyu2NTQAABBeJQk)](https://venturebeat.com/ai/new-memory-framework-builds-ai-agents-that-can-handle-the-real-worlds)

# 🧠 Introducing ReasoningBank: AI Agents That Learn from Experience

Imagine an AI assistant that doesn't just follow instructions but learns from every success and failure, refining its approach over time. That's the promise of ReasoningBank, a groundbreaking memory framework developed by researchers at the University of Illinois Urbana-Champaign and Google Cloud AI Research. This innovative system enables large language model (LLM) agents to organize their experiences into a memory bank, allowing them to improve at complex tasks as they accumulate knowledge.

## 🔍 What Is ReasoningBank?

ReasoningBank is a memory framework designed to enhance the adaptability and reliability of LLM agents. Unlike traditional memory mechanisms that passively store past interactions, ReasoningBank actively distills "generalizable reasoning strategies" from both successful and failed attempts to solve problems. These distilled strategies are stored as structured memory items that the agent can retrieve during inference to avoid repeating past mistakes and make better decisions in future tasks.

The framework operates in a closed loop: when an agent faces a new task, it uses an embedding-based search to retrieve relevant memories from ReasoningBank. These memories are then incorporated into the agent’s system prompt, providing context for its decision-making. After completing the task, the agent analyzes the outcome, extracts insights, and updates its memory bank with new knowledge, continuously evolving and improving its capabilities.

## 🚀 Real-World Impact

The researchers found that ReasoningBank consistently outperforms classic memory mechanisms across various benchmarks, including web browsing and software engineering tasks. By combining ReasoningBank with test-time scaling techniques—where an agent makes multiple attempts at a problem—the performance and efficiency of LLM agents are significantly enhanced. This combination offers a practical path toward building more adaptive and reliable AI agents for enterprise applications.

For instance, consider an AI agent tasked with finding Sony headphones. Without ReasoningBank, a broad search query might return thousands of irrelevant products. With ReasoningBank, the agent analyzes the failure, distills strategies like "optimize search query" and "confine products with category filtering," and incorporates these strategies into its memory. In future tasks, the agent can apply these learned strategies to achieve better results.

## 🧠 Why Memory Matters

Traditional LLM agents process each task in isolation, often forgetting valuable insights from past experiences. This lack of memory leads to repeated mistakes and missed opportunities for improvement. ReasoningBank addresses this limitation by enabling agents to learn from their experiences, both successes and failures, and apply this knowledge to future tasks. This capability is crucial for developing AI agents that can handle the unpredictability and complexity of real-world applications.

## 📚 Glossary

* **Large Language Model (LLM):** A type of AI model trained on vast amounts of text data to understand and generate human language.

* **Embedding-Based Search:** A method of retrieving information by converting data into numerical vectors (embeddings) and finding similar vectors in a database.

* **Test-Time Scaling:** A technique where an agent generates multiple independent answers to the same question to improve performance.

* **Inference:** The process by which an AI model makes predictions or decisions based on input data.

## 🔗 Source

For more in-depth information, read the full article on VentureBeat:
👉 [New memory framework builds AI agents that can handle the real world's unpredictability](https://venturebeat.com/ai/new-memory-framework-builds-ai-agents-that-can-handle-the-real-worlds)
