---
layout: post
title: "AI Security & Risk Brief: Google Finds AI Agent Weaponising Patches Without Humans"
series: "AI Security & Risk"
description: "Google's GTIG reports autonomous AI exploit agents, CrowdStrike links AI-run Vapor Panda attacks to Korea, and Cohesity flags weak AI-threat readiness."
date: 2026-11-17 19:54:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Security
  - Cybersecurity
  - AI Safety
  - Google
  - CrowdStrike
keywords:
  - autonomous ai cyberattacks
  - agentic pentest frameworks artex
  - ai exploit generation n-day vulnerabilities
  - vapor panda deepseek korea
  - cyber resilience ai threats asia
permalink: /ai-security-and-risk-brief-2026-11-17/
---

# AI Security & Risk Brief: Google Finds AI Agent Weaponising Patches Without Humans

**Today:** Attackers now use AI agents to run whole intrusion chains with little or no human input, and the time defenders have to patch is shrinking faster than most enterprise recovery plans assume.

## Top Stories

### 1. 🔒 **Google Threat Intelligence Says Agentic Attack Activity Has Crossed a Significant Threshold**

*Google Cloud · November 17, 2026*

**Bottom line:** Google's threat researchers found attackers using an AI framework that turns newly published security patches into working exploits and runs them with no human in the loop.

In its latest AI Threat Tracker, the Google Threat Intelligence Group (GTIG) describes a framework called exploit_agent. It was found on an exposed staging server, connected to several frontier and locally hosted language models, and used against French media, entertainment and education websites. The report also says several threat actors are using open-source agentic pentest frameworks, naming ARTEX, CAIRN, CyberStrikeAI, PentAGI and HexStrike AI. GTIG says CAIRN was used against US aerospace targets and PentAGI against organisations in Asia. GTIG counts zero-day exploits rising from a 2025 average of eight a month to 11 a month in 2026, with 22 in August. It also says LLMjacking, the abuse of stolen cloud AI credentials, ran up more than US$100,000 in fraudulent charges in a single day in some cases and about US$1 million in the worst cases.

**Why it matters:** If AI can turn a patch into a working exploit within hours, monthly patch cycles stop being adequate, and that matters most for banks and payment firms with large web-facing estates. Because PentAGI was used against organisations in Asia, regional security teams should treat agent-driven scanning as a current threat, not a future one.

🔗 [Read the full story](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)

---

### 2. 🌐 **CrowdStrike Says China-Linked Vapor Panda Used AI Agents Against Korean Foreign-Policy Groups**

*Korea JoongAng Daily · November 17, 2026*

**Bottom line:** CrowdStrike says a China-linked group used an AI agent-based penetration testing tool, powered mainly by DeepSeek, against South Korean think tanks and diplomacy organisations, and some of those attacks succeeded.

Adam Meyers, CrowdStrike's senior vice president of counter adversary operations, told Korean reporters at a briefing on Tuesday that Vapor Panda had hit multiple Korea-related targets. He did not name the victims or say how far the breaches went. This adds a Korea-specific finding to CrowdStrike's 4 November disclosure that the group used the Artex framework against more than 200 organisations worldwide between 17 and 29 October. Researchers estimated that a single intrusion attempt used about 1.4 billion input tokens. CrowdStrike says this campaign is separate from the Artex-linked attacks on Korea's financial sector last month.

**Why it matters:** This is now a confirmed state-aligned campaign in North Asia using an open-weight Chinese model. Running models on their own infrastructure lets attackers cut costs and avoid provider safeguards, which weakens defences that rely on model-provider abuse monitoring. Meyers said AI mainly makes existing attack techniques faster and more scalable rather than creating new ones, so basic controls still apply. They have to work at machine speed.

🔗 [Read the full story](https://www.koreajoongangdaily.com/business/chinalinked-hackers-target-korean-foreign-policy-organizations-using-ai-tools/12976941)

---

### 3. 🔒 **Cohesity Survey Finds Only 4% of Korean Firms Ready to Recover From Advanced AI-Driven Attacks**

*Seoul Economic Daily · November 17, 2026*

**Bottom line:** Three in four Korean organisations surveyed said they suffered a major cyberattack in the past year, yet almost none said their recovery plans could handle the most advanced AI-driven threats.

The figures come from Cohesity's 2026 Global Cyber Resilience Report, which surveyed 3,200 IT and security decision-makers across 12 countries. According to the report, 75% of Korean respondents had a major attack in the past 12 months, up from 44% a year earlier. Only 39% were confident their resilience strategy matched current threats. Korean firms hit by an attack targeted nine hours to restore core systems but took 15 hours on average. AI models and workflow tools were among the largest gaps in recovery planning, cited by 64% of respondents.

**Why it matters:** The findings are vendor-commissioned, but they point to a real risk: enterprises are adding AI models and agents faster than they are including them in backup, identity and recovery planning. Regulated financial institutions across Asia should check whether their operational resilience plans cover AI systems explicitly.

🔗 [Read the full story](https://en.sedaily.com/business/2026/11/17/75-percent-of-korean-firms-hit-by-major-cyberattacks-only-4)

## Key Takeaways

- Open-source agentic attack frameworks such as ARTEX, CAIRN and PentAGI now appear across criminal and state-aligned activity, so offensive automation is no longer limited to well-resourced attackers.
- Attackers are increasingly turning newly disclosed (n-day) flaws into exploits within hours, which shortens the window for patching web-facing and payment-related systems.
- Defences are falling behind attackers. AI models, agent tooling and stolen AI credentials are now targets in their own right, yet many recovery plans still leave them out.

## What to Watch

Watch whether the Korean organisations CrowdStrike says were breached come forward or are named by authorities, and whether GTIG's next quarterly tracker reports exploit_agent-style automation spreading beyond web applications. Also watch for financial regulators in Asia telling institutions to shorten patch windows for internet-facing systems.

---
