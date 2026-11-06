---
layout: post
title: "AI Security & Risk Brief: DOJ Charges Trio In $129M AI Voice Fraud"
series: "AI Security & Risk"
description: "DOJ charges AI voice-cloning fraud trio, OpenAI ships Critical-rated GPT-6 Cyber, and researchers expose ChatGPT and ARTEX flaws."
date: 2026-11-06 19:14:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Security
  - Cybersecurity
  - AI Safety
  - OpenAI
keywords:
  - ai voice cloning fraud
  - gpt-6 cyber openai
  - chatgpt lockdown mode bypass
  - artex ai pentest framework
  - ai deepfake wire fraud doj
permalink: /ai-security-and-risk-brief-2026-11-06/
---

# AI Security & Risk Brief: DOJ Charges Trio In $129M AI Voice Fraud

**Today:** A blockbuster US fraud indictment, a frontier model built specifically to hack, and two fresh vulnerability disclosures show how fast AI is reshaping both sides of the attacker-defender equation.

## Top Stories

### 1. 🔒 **DOJ Charges Three With Using AI Voice Cloning to Steal $129 Million**

*ABC News (citing US Attorney's Office, SDNY) · November 6, 2026*

**Bottom line:** US prosecutors charged three men with running an 18-month scheme that used AI-generated voices and video to impersonate CEOs and lawyers, defrauding companies of nearly $130 million.

Jacob Soall, Sharon Hazan and Guy Sheetrit allegedly contacted employees at target companies between July 2024 and February 2026, posing as executives or outside counsel on a "confidential deal" and directing staff to wire funds to accounts they controlled. Victims named in the indictment span a Missouri hospital system, a Rhode Island bank, a UK fintech company and a Massachusetts mutual fund, with individual losses ranging from roughly $2.7 million to $11.6 million. All three defendants were arrested in Spain and the UK earlier this year and await extradition.

**Why it matters:** This is one of the largest disclosed AI-impersonation fraud cases to date and a direct hit on wire-transfer approval workflows — exactly the control point fintechs and payment providers rely on for high-value disbursements. Firms across Singapore and the region should treat voice/video confirmation as compromised by default and require independent out-of-band verification for any payment instruction tied to a "confidential" or time-pressured request.

🔗 [Read the full story](https://abcnews.com/US/trio-ai-impersonate-corporate-execs-defrauding-companies-130/story?id=137894421)

---

### 2. 🤖 **OpenAI Launches GPT-6 Cyber With a "Critical" Risk Rating**

*OpenAI · November 5, 2026*

**Bottom line:** OpenAI released GPT-6 Cyber, a specialised model for finding and fixing software vulnerabilities, and classified it as "Critical" for cybersecurity capability under its own Preparedness Framework.

In internal use, OpenAI said the model found 81 previously unknown high-severity flaws in Firefox (which Mozilla has begun patching) and produced working exploits for 948 Linux kernel vulnerabilities, far more than its predecessor. Access is currently restricted to vetted customers in OpenAI's Daybreak Red programme, and OpenAI said the model stayed within authorised scope in all tested cases when given deployment safety instructions.

**Why it matters:** A model capable of autonomously finding and exploiting zero-days is a double-edged tool — it accelerates patching for defenders like Mozilla, but the same underlying capability raises the bar for what attackers with similar access could eventually achieve. Enterprises should expect vendor patch cadences to quicken and should press cybersecurity vendors on how they plan to use (or defend against) comparable models.

🔗 [Read the full story](https://openai.com/index/introducing-gpt-6-cyber/)

---

### 3. 🔒 **Researchers Find ChatGPT Flaw That Silently Leaked Private Chats**

*GB Hackers (citing Check Point Research) · November 6, 2026*

**Bottom line:** Check Point Research disclosed a now-patched ChatGPT flaw that let attackers bypass Lockdown Mode and exfiltrate full chat histories without any user interaction.

The bug abused nested sandboxed iframes in ChatGPT's HTML-preview feature, letting a malicious page escape sandbox restrictions to open genuine browser popups capable of phishing credentials or pushing fake malware downloads. In the Electron-based ChatGPT Classic desktop app, the exploit required zero clicks — simply viewing a malicious shared conversation could leak data. OpenAI removed the vulnerable permissions on September 18, 2026, and Check Point confirmed the fix holds.

**Why it matters:** Even "locked down" AI consumer tools can leak sensitive conversation data through overlooked browser-sandbox permissions. Firms that allow staff to use ChatGPT for drafting or analysis should confirm their enterprise tier is patched and should treat chat histories pasted with customer or transaction data as a standing data-loss risk.

🔗 [Read the full story](https://gbhackers.com/chatgpt-lockdown-mode-bypass/)

---

### 4. 🔒 **AI Pentesting Tool Linked to Bank Breaches Found Exposed on 1,465 Servers**

*Censys · November 5, 2026*

**Bottom line:** Security researchers at Censys found ARTEX, an open-source LLM-powered autonomous penetration-testing framework, publicly exposed across 1,465 hosts, with roughly 815 distinct deployments after removing duplicate templates.

ARTEX automates reconnaissance, password attacks and credential abuse with minimal human input. CrowdStrike previously tied ARTEX infrastructure to attacks on South Korean financial institutions that breached loan and mobile-work systems, while Microsoft attributed a China-aligned group's compromise of ConnectWise's cloud backup service — reaching more than 2,250 customer tenants — to the same tool. Censys found 155 of the exposed hosts (10.6%) also running other attack tools such as Cobalt Strike, and 32 hosts leaking exploit kits and credentials through open directories.

**Why it matters:** Offensive AI frameworks are now being run so carelessly by their own operators that defenders can map attacker infrastructure directly — but the underlying trend, AI tools compressing the time from credential theft to privileged access in financial systems, is the bigger concern for banks and BaaS providers running API-exposed loan and disbursement systems.

🔗 [Read the full story](https://censys.com/blog/artex-agentic-asbestos)

---

## Key Takeaways

- AI-enabled impersonation has moved from proof-of-concept to a $129 million prosecuted fraud scheme, squarely targeting wire-transfer approval processes used across banking, healthcare and fintech.
- The same frontier AI capability — finding and exploiting software flaws autonomously — is being raced by both defenders (OpenAI's GPT-6 Cyber, Mozilla's patch cycle) and attackers (ARTEX-linked breaches), narrowing the time window institutions have to patch before exploitation.
- Vulnerabilities are surfacing in the AI tooling layer itself (ChatGPT's sandbox escape), meaning enterprise AI governance now needs to cover not just model outputs but the surrounding application infrastructure.

## What to Watch

Watch for Mozilla's continued Firefox patch rollout tied to GPT-6 Cyber's findings, broader Daybreak Red access rollout from OpenAI "in the coming weeks," and whether CrowdStrike or Microsoft publish further attribution linking ARTEX-exposed hosts to new financial-sector breaches.

---
