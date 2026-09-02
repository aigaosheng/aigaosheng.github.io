---
layout: post
title: "AI Agents in Action - Foundations for Evaluation and Governance"
description: "Key Findings & Conclusions · Critical Data & Facts"
date: 2025-12-01 18:28:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI Agents
- LLM
- Governance
keywords: [AI Agents, LLM,Governance]
permalink: /AI Agents in Action - Foundations for Evaluation and Governance/
---

## 📘 **AI Agents in Action: Foundations for Evaluation and Governance**

**Research Topic & Objective**
The paper studies **LLM-based AI agents** and aims to provide a foundation to help organizations **classify, evaluate, assess risks, and govern AI agents responsibly** as they move from prototypes to real-world deployment. 

---

### ✅ **Key Findings & Conclusions**

* Modern AI agents are powered mainly by **large language models (LLMs)** that can plan and adapt, enabling dynamic automation in both digital and physical environments. 

* AI agent systems require a **layered architecture**:

  1. **Application layer** – connects via UI/APIs, applies domain rules, runs in cloud or edge.
  2. **Orchestration layer** – manages tools, memory, workflows, and model switching; remains model-agnostic.
  3. **Reasoning layer** – uses LLMs or other models to make decisions, plan actions, and adapt. 

* **Model Context Protocol (MCP)** is an important emerging standard that enables plug-and-play integration between AI agents and enterprise resources like calendars, email systems, CRM, and databases. It treats interactions as untrusted by default and requires identity and permission checks before granting access. 

* **Agent-to-Agent (A2A) Protocol** helps different agents discover and coordinate tasks with each other using structured “agent cards” describing identity and skills.

* **Risk management must be continuous** and scale with levels of **autonomy** and **authority**, especially in complex or externally connected environments.

* Governance should be **progressive and adaptive**, similar to permissioning human users:

  * **HITL (Human-in-the-loop)** is required for high-risk or unpredictable tasks.
  * **HOTL (Human-on-the-loop)** may be used in stable, bounded environments with human override ability.

* Multi-agent ecosystems introduce new failure modes like **orchestration drift**, **semantic misalignment**, **cascading system failures**, and **expanded cybersecurity attack surfaces**.

* Responsible deployment depends on **least-privilege access**, sandbox testing, automated anomaly detection, audit logging, and human accountability structures.

**Overall conclusion**: With careful evaluation and proportionate governance, AI agents can safely scale to enhance productivity and eventually power more advanced **multi-agent digital ecosystems**. 

---

### 📊 **Critical Data & Facts**

* **82% of organizations plan to integrate AI agents within 1–3 years**, but most are still at pilot or planning stage (not yet full deployment). 

* AI agents differ from classical software because they:

  * generate plans,
  * simulate reasoning,
  * adapt through feedback,
  * call external tools and coordinate with other agents,
  * increase organizational attack surfaces,
  * require human-like onboarding and permissioning models. 

* Core technology paradigms supporting agents:

  * Classical software (rules),
  * Neural networks (stats learning),
  * Foundation models (LLMs),
  * Autonomous control (planning, acting). 

---

### Sources

[1] [AI Agents in Action: Foundations for Evaluation and Governance](https://www.weforum.org/publications/ai-agents-in-action-foundations-for-evaluation-and-governance/)
