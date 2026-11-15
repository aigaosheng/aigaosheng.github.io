---
layout: post
title: "Enterprise AI Brief: United Airlines Blocks Third-Party AI Agents"
series: "Enterprise AI"
description: "United Airlines blocks AI agents, Google Cloud widens cross-cloud agent governance, and OutSystems launches agentic insurance claims."
date: 2026-11-12 20:12:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - Enterprise AI
  - Agentic AI
  - AI Agents
  - Google Cloud
  - Agentic Commerce
keywords:
  - enterprise ai agents
  - agentic commerce
  - ai agent governance
  - cross-cloud ai
  - agentic insurance claims
  - ai roi measurement
permalink: /enterprise-ai-brief-2026-11-12/
---

# Enterprise AI Brief: United Airlines Blocks Third-Party AI Agents

**Today:** A carrier drawing a hard line on third-party AI agents, two Google Cloud moves to govern agents across rival clouds and cut their running cost, and new enterprise products in insurance and AI-ROI measurement show the agentic enterprise is now colliding with real operational and governance limits.

## Top Stories

### 1. 🔒 **United Airlines Blocks Third-Party AI Agents From Its Booking Platform**

*CNBC · November 11, 2026*

**Bottom line:** United Airlines will stop third-party AI agents from completing bookings on its digital platforms, citing data-security and regulatory risk rather than waiting for industry-wide standards to mature.

United said letting personal AI assistants hold or use customer account credentials could expose sensitive data and enable unauthorized purchases, account changes or frequent-flyer mile use. It also flagged that automated check-in could breach FAA and DOT rules requiring a human to confirm prohibited items. The airline's systems can distinguish bookings made by people, travel agencies or automated assistants, and it says AI agent booking volume is currently low; the new policy will apply directly on its own platforms and indirectly through travel agencies and aggregators.

**Why it matters:** The move is a concrete signal that enterprises will gate, not just govern, agentic access to transactional systems — a direct precedent for banks, card networks and payment providers building agentic-commerce rails, including those active in Singapore and the wider region.

🔗 [Read the full story](https://www.cnbc.com/2026/11/11/united-airlines-ai-agents.html)

---

### 2. 🤖 **Google Cloud Extends Agent Gateway Governance to Rival Clouds**

*Google Cloud · November 11, 2026*

**Bottom line:** Google Cloud opened a Limited Preview letting enterprises apply its Agent Gateway governance layer to AI agents running on Amazon EKS, Azure AKS, Red Hat OpenShift and bare-metal Kubernetes clusters, not just its own infrastructure.

Each agent gets a verifiable identity registered in Agent Registry, with local Agent Gateway proxies routing LLM, MCP and agent-to-agent traffic while enforcing Model Armor policies; access logs and traces flow into Cloud Logging and Cloud Trace. The cross-cloud preview itself is free, though connected services bill at standard rates.

**Why it matters:** Google is positioning its control plane as the default place enterprises enforce agent identity and policy even when compute sits on a competitor's cloud — a land-grab for governance ahead of equivalent moves from AWS and Microsoft that regional banks and fintechs running multi-cloud estates will need to weigh carefully.

🔗 [Read the full story](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)

---

### 3. 🤖 **Google Launches Gemini Decisions API to Cut Agent Routing Costs**

*Google · November 11, 2026*

**Bottom line:** Google introduced the Gemini Decisions API, a new endpoint built on its Gemini Decision 1 model for fast, bounded choices such as tool selection, policy checks and model routing, rather than open-ended text generation.

The API scores up to 1,000 yes/no, multiple-choice or rubric-scored questions against a single multimodal input in 150–250 milliseconds, priced at $0.10 per million input tokens with no charge for output tokens. Google says it is substantially cheaper on shared benchmarks than running the same routing tasks through a general-purpose model such as Gemini 3.5 Flash-Lite.

**Why it matters:** Decision-only inference tackles one of the biggest hidden costs of agentic systems — the constant internal routing and policy checks agents make before acting — which matters directly to any fintech running high-volume, low-latency agent workflows such as fraud screening or transaction routing.

🔗 [Read the full story](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

---

### 4. 💳 **OutSystems Launches Agentic Claims Tool for Auto Insurers**

*PR Newswire · November 12, 2026*

**Bottom line:** OutSystems introduced Agentic First Notice of Loss, a pre-built agentic solution that lets policyholders report a car accident through a conversational AI agent while keeping coverage and payment decisions with human adjusters.

The agent can check policy coverage, open a claim in the insurer's existing claims system, attach photos and statements, and coordinate roadside towing through a partnership with Honk — all before a human adjuster takes over liability and payment decisions. OutSystems cites industry research that 35% of insurance IT leaders have not yet started AI projects, with legacy systems and scattered data as the top cited barrier.

**Why it matters:** It is a template for how regulated industries are threading agentic AI into customer-facing workflows without ceding regulated decisions to the agent — a pattern relevant to Southeast Asian insurers and banks under similarly tight compliance expectations.

🔗 [Read the full story](https://www.prnewswire.com/apac/news-releases/outsystems-introduces-agentic-claims-solution-to-modernize-policyholder-experiences-302937205.html)

---

### 5. 📊 **Nebuly Raises $21M to Measure What Enterprise AI Agents Are Actually Worth**

*Tech.eu · November 12, 2026*

**Bottom line:** Turin-based Nebuly raised a $21 million Series A led by Planven, with Exor Ventures, Tenacity Capital, TGVG Capital and Fastweb+Vodafone also participating, to build a platform that ties AI agent activity to measurable business results.

Nebuly's software tracks what AI agents built on tools such as Claude, ChatGPT or Microsoft Copilot actually do across an organization's internal and customer-facing workflows, then links that activity to productivity, efficiency and revenue outcomes. The company says almost all of its customers generate more than $100 million in annual revenue, with contracts starting at $100,000 a year; funds will go toward expanding its go-to-market team in the US and Europe.

**Why it matters:** The round is a direct market response to the gap between AI spending and proven returns — a question boards are now pressing every enterprise to answer, and one regional banks and fintechs will face as they scale pilots into production agents.

🔗 [Read the full story](https://tech.eu/2026/11/12/nebuly-raises-21m-series-a-to-turn-ai-investments-into-measurable-results)

---

## Key Takeaways

- Enterprises are starting to actively gate agentic access to transactional systems rather than waiting for industry-wide authorization standards, as seen in United Airlines' restriction.
- Cloud vendors are racing to own the governance and cost layer of agentic AI — identity, policy enforcement and low-cost decisioning — ahead of broader enterprise rollouts.
- Regulated industries such as insurance are converging on a common pattern: let agents handle intake and routine tasks, keep humans on record for compliance-sensitive decisions.
- New funding for AI-ROI measurement tools underscores a widening gap between enterprise AI spending and proof of business value, echoing recent survey findings that full AI integration remains rare.

## What to Watch

Watch whether other airlines, banks or payment networks follow United's lead in restricting third-party AI agent access to transactional systems, and whether Google's cross-cloud Agent Gateway preview draws enterprises running multi-cloud Kubernetes estates, including in Singapore and the wider region, ahead of likely competing announcements from AWS and Microsoft at upcoming cloud conferences.

---