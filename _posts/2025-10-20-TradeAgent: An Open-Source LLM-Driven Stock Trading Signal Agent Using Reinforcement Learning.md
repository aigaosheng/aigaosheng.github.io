---
layout: post
title: "TradeAgent: An Open-Source LLM-Driven Stock Trading Signal Agent Using Reinforcement Learning"
date: 2025-10-20 22:32:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Financial AI
- LLM Agents
keywords: [AI trading agent, LLM in finance, memory-enhanced trading]
permalink: /TradeAgent - An Open-Source LLM-Driven Stock Trading Signal Agent Using Reinforcement Learning/
---

**TradeAgent: An Open-Source LLM-Driven Stock Trading Signal Agent Using Reinforcement Learning**

### Overview

**TradeAgent** is an open-source trading signal generator that combines reinforcement learning with LLM-based market reasoning. It is inspired by, and partially adapted from, the open-source implementation of **FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design** ([https://github.com/pipiku915/FinMem-LLM-StockTrading](https://github.com/pipiku915/FinMem-LLM-StockTrading)).

I have made substantial modifications to the original architecture so that the agent can **fuse multiple sources of market context**, including:

* Technical indicators
* Historical price sequences
* Corporate news
* Fundamental financial metrics

The agent uses an LLM for **feature extraction, insight generation, internal reflection, and embedding generation** (for RAG retrieval). This architecture makes the agent significantly more “cognitive” than classical RL models. However, it also makes LLM inference expensive — especially when extended to multiple data sources.

Because of this cost, all experiments run on **open-source, locally deployed models** (12GB RTX 4070). Only smaller models can be used in this environment, but even so, **the early results are promising**, outperforming buy-and-hold on selected tickers.

At present, only historical price data is integrated in my testing environment, so early benchmarks are based solely on price sequences.

The project is now available here:
👉 **GitHub:** [https://github.com/aigaosheng/RLtraderAgent](https://github.com/aigaosheng/RLtraderAgent)

If you are interested in collaboration or experimentation, feel free to get in touch. Initial experiments indicate meaningful potential — although the model currently shows **run-to-run instability (low robustness)**, likely due to small model size and sensitivity to sampling. Future versions using stronger proprietary LLMs (ChatGPT, Gemini, Claude, etc.) may improve stability but at much higher API cost. Integration of multi-modal RAG context (news + fundamentals) is the next major milestone.

---

## ✅ Usage

```
# Insight extraction from historical stock price in defined range.
# Structured output is stored in PostgreSQL.
python finAgent/market_intelligent/price_mi.py

# RL agent training
python finagent_rl.py

# Live inference: generate trading signals using the trained model
python finagent_live.py --model FinAgent_result/1105-r5 --train True --start 2024-11-04 --end 2024-11-04 --symbols QQQ
```

---

## 🔍 Summary of the Reference Paper (FinMem)

The reference model, **FinMem**, introduces an LLM-powered trading framework with layered memory and a defined trader profile to improve reasoning depth and risk alignment.

📄 Source: [https://arxiv.org/abs/2311.13743](https://arxiv.org/abs/2311.13743)

### Key Findings

* Outperforms both RL and LLM-based baseline agents on real market data
* Layered memory improves reasoning and timing
* Trader “character” (risk profile) impacts performance outcomes

### Critical Architecture Facts

* Three modules: **Profiling + Memory + Decision Engine**
* Benchmarked against Buy-and-Hold, DRL agents, and LLM baselines
* Shows **higher cumulative returns** across the test assets

### Implications

* Enables more **human-like trading behaviour**
* Blueprint for future **LLM-based decision agents**
* Signals a shift from “chat”-LLMs → “goal-driven LLM agents”
