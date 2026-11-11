---
layout: post
title: "AI Security & Risk Brief: Fireworks AI Breach Widens, Hits Notion"
series: "AI Security & Risk"
description: "Fireworks AI's breach widens to hit Notion's AI chats, as Microsoft Research reveals a neuron-level AI agent backdoor technique."
date: 2026-11-11 19:37:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Security
  - Cybersecurity
  - AI Safety
  - Fireworks AI
  - Agentic AI
keywords:
  - fireworks ai data breach notion
  - ai agent backdoor vulnerability
  - mcp server supply chain risk
  - notion ai chat transcripts leak
  - ai agent security funding
permalink: /ai-security-and-risk-brief-2026-11-11/
---

# AI Security & Risk Brief: Fireworks AI Breach Widens, Hits Notion

**Today:** A third-party AI vendor breach has spread into enterprise SaaS tools, and fresh research shows how little it now takes to turn a trusted AI agent into a hidden backdoor.

## Top Stories

### 1. 🔒 **Fireworks AI Breach Widens to Expose Notion AI Chat Transcripts**

*Notion (official advisory) · November 11, 2026*

**Bottom line:** The Fireworks AI breach disclosed earlier this month has grown more serious, with Notion confirming that AI chat transcripts from its "Insights" feature were exposed for under 1% of workspaces.

Notion's security advisory lays out a timeline: Fireworks first told Notion on November 2 that only synthetic test data was affected, but by November 6 it warned real customer data had also been exposed, with the final affected dataset confirmed on November 8. Notion had already cut ties with Fireworks on November 3 and notified impacted customers on November 9, advising them to rotate any passwords, API keys or credentials pasted into Notion AI during the incident window.

**Why it matters:** The incident shows how a single compromised AI inference vendor can cascade into customer-facing data exposure across multiple downstream SaaS products, a supply-chain pattern that enterprise security and compliance teams in Singapore and across Asia should treat as a template for vendor risk reviews of any third-party AI inference provider.

🔗 [Read the full story](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor)

---

### 2. 🔒 **Microsoft Finds AI Agents Can Be Backdoored via 10 Neurons**

*Microsoft Research · November 10, 2026*

**Bottom line:** Microsoft researchers showed that reprogramming fewer than ten rarely-used ("dormant") neurons in a model is enough to implant a hidden backdoor in an AI agent, with no retraining required.

The technique, dubbed "Lazare," turns dormant neurons into trigger detectors: once a specific hidden pattern appears in the agent's input, the modified neurons inject malicious instructions into its output, causing it to run attacker commands while behaving normally the rest of the time. Microsoft said the attack only needs write access to a model's weights and that current safety evaluations would not reliably catch it, though frontier models can spot anomalies when specifically asked to audit weights against a known-good original.

**Why it matters:** As banks and fintechs in Singapore and the region adopt third-party or open-weight models inside agentic workflows with tool and terminal access, model provenance and weight integrity checks become as important as code review — a backdoored model can sit dormant through procurement testing and activate only in production.

🔗 [Read the full story](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/)

---

### 3. 🔒 **Corelight Warns AI Coding Agents Auto-Run Unvetted Dependencies**

*Corelight · November 10, 2026*

**Bottom line:** Corelight research found that AI coding assistants routinely launch Model Context Protocol (MCP) servers that silently pull in changed, unreviewed dependencies each session, inheriting the server's often-privileged access in the process.

On one test workstation, a single MCP server pinned to one release still ran 15 different dependency sets over five weeks, with 23 of 69 packages silently changing versions, including cryptography and authentication libraries. Because dependencies load into the same process as the MCP server, any malicious package gains whatever credentials or network access that server already holds — in Corelight's test environment, that included weekly connections to firewall, SIEM and sensor management systems.

**Why it matters:** Fintechs rolling out AI coding assistants for internal development should treat agent and MCP configuration as part of the software supply chain, pinning dependencies to hash-locked environments and scoping agent credentials to read-only, short-lived access rather than standing admin rights.

🔗 [Read the full story](https://corelight.com/blog/mcp-server-supply-chain-risk)

---

### 4. 🔒 **Orca Security Expands Platform to Track Shadow AI and Agents**

*Help Net Security · November 11, 2026*

**Bottom line:** Orca Security extended its cloud security platform to discover unsanctioned "shadow" AI applications and to inventory and assess the risk of autonomous AI agents running in customer cloud environments.

The new capabilities fingerprint apps built on no-code AI builders such as Lovable, Replit and Bolt, and correlate discovered agents and applications with cloud identities and IAM permissions to flag overprivileged access to sensitive data. Orca said its own research found 52% of organizations now build custom applications with AI, often without security teams' knowledge.

**Why it matters:** As Asia-Pacific banks and payment firms let business units spin up AI-built apps and agents outside formal IT channels, tooling that maps what exists and what it can access is becoming a baseline control rather than an optional add-on.

🔗 [Read the full story](https://www.helpnetsecurity.com/2026/11/11/orca-security-ai-security/)

---

### 5. 📊 **Israeli Startup Bay Raises $50M to Police Rogue AI Agents**

*Tech Startups · November 10, 2026*

**Bottom line:** Bay, an Israeli AI security startup, emerged from stealth with $50 million in total funding — a $37 million Series A led by Battery Ventures plus a previously undisclosed $13 million seed round — to evaluate and block risky actions by AI agents in real time.

The company, founded by veterans of Unit 8200, CrowdStrike and Hunters, said it can assess proposed agent actions across employee devices, cloud infrastructure and SaaS apps in milliseconds, even when those actions technically fall within an agent's authorized permissions. Investors include Microsoft's M12 and Wiz co-founder Assaf Rappaport; early customers reportedly include Micron, Peloton and Wix.

**Why it matters:** The round signals investor appetite for tools that govern agent behavior rather than just agent access — a distinction that will matter to regulated institutions in Singapore and the region once they move from AI pilots to agents with standing access to customer or payment systems.

🔗 [Read the full story](https://techstartups.com/2026/11/10/israeli-ai-security-startup-bay-emerges-from-stealth-with-50m-in-funding-to-stop-rogue-ai-agents-before-they-cause-damage/)

## Key Takeaways

- Third-party AI vendor risk is no longer theoretical: a single inference-provider breach (Fireworks AI) cascaded into customer-facing exposure at Notion within days.
- Model and agent integrity checks are becoming a distinct security discipline, separate from classic code review — covering model weights (Microsoft), MCP dependencies (Corelight) and agent permissions (Orca, Bay).
- Investor and vendor activity is shifting from detecting AI *access* to governing AI *actions*, reflecting a maturing view that over-permissioned but "authorized" agents are now a primary risk surface.

## What to Watch

Watch whether Fireworks AI or Notion disclose a precise exposure window or transcript count beyond the current "under 1%" workspace figure, and whether other Fireworks AI customers beyond Notion come forward with their own notifications in the coming days.

---