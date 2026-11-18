---
layout: post
title: "AI Security & Risk Brief: Microsoft Agent Framework PyPI Package Poisoned"
series: "AI Security & Risk"
description: "Microsoft's agent-framework PyPI releases carried a credential stealer; Sumsub says APAC holds a third of global fraud networks."
date: 2026-11-18 20:08:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Security
  - Cybersecurity
  - AI Safety
  - Microsoft
  - Sumsub
keywords:
  - microsoft agent framework pypi compromise
  - ai agent supply chain attack
  - credential stealer python package
  - apac fraud networks sumsub
  - ai agent fraud verification
permalink: /ai-security-and-risk-brief-2026-11-18/
---

# AI Security & Risk Brief: Microsoft Agent Framework PyPI Package Poisoned

**Today:** A supply-chain compromise hit the tooling used to build enterprise AI agents, and new regional data shows fraud networks concentrating in Asia Pacific.

## Top Stories

### 1. 🔒 **Microsoft Agent Framework Releases on PyPI Carried a Credential Stealer**

*SecurityWeek · November 18, 2026*

**Bottom line:** Two malicious releases of Microsoft's agent-framework Python package put cloud and CI/CD credentials at risk, so teams that installed either one need to treat their secrets as exposed.

According to SecurityWeek, versions 1.26.1 and 1.26.2 were published about 33 minutes apart and run credential-harvesting code whenever Python starts. The targets include Azure, Azure DevOps and GitHub Actions credentials. Both releases have been quarantined, and 1.26.0 is the latest clean version. A Microsoft maintainer confirmed in a GitHub discussion that the releases were pulled and an investigation is under way. Researchers from OX Security, Wiz, Endor Labs and SafeDep analysed the incident. SafeDep flagged a maintainer account created on the day of the attack, but the report says its role is unconfirmed and the publishing method is unknown. SecurityWeek puts the package at roughly 190,000 downloads a month. No victim count has been disclosed.

**Why it matters:** Agent frameworks typically run with broad cloud and pipeline permissions, so a poisoned dependency is a direct route to production secrets. Asian enterprises building agents on Azure should pin to the clean version, search lockfiles, CI logs and container images for the bad releases, and rotate any credentials exposed on affected systems.

🔗 [Read the full story](https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/)

---

### 2. 🔒 **Sumsub: Asia Pacific Hosts a Third of Global Fraud Networks**

*Sumsub · November 18, 2026*

**Bottom line:** Sumsub's new identity fraud report says organised, network-based fraud is concentrating in Asia Pacific, and that verified accounts are being used as mule accounts after onboarding.

Sumsub released the Asia Pacific findings of the sixth edition of its Identity Fraud Report at Singapore FinTech Festival 2026. It reports that the region accounts for 33% of fraud networks detected worldwide and has nearly a million fraud attempts, the most of the six regions it tracks. About 2.4% of approved people in the region are linked to a detected network. Roughly a third of those links surface only after verification succeeds, which Sumsub reads as a sign that accounts are later sold on to fraudsters. Its regional complexity index rose from 1.83 to 2.09, and Singapore's rose 9% to 2.13. These figures are the vendor's own platform data and have not been independently verified.

**Why it matters:** If the findings hold, checks at onboarding are not enough, and banks and payment firms in Asia need continuous monitoring of accounts that have already passed KYC. The report also makes this a live issue for Singapore institutions.

🔗 [Read the full story](https://sumsub.com/newsroom/sumsub-advances-trusted-ai-adoption-in-financial-services-at-singapore-fintech-festival-2026)

## Key Takeaways

- The software supply chain is now an attack path into AI agents: tooling that holds cloud and pipeline credentials is a high-value target, so dependency pinning and secret rotation belong in agent security programmes.
- Fraud risk is shifting from the point of onboarding to what happens afterwards, and Sumsub reports that a meaningful share of network links appear only after verification passes.
- Both stories rest on early or vendor-reported data, so treat the figures as signals to test against your own telemetry.

## What to Watch

Look for Microsoft's findings on how the malicious releases were published and whether any victims are disclosed. Also watch for independent data that confirms or challenges Sumsub's APAC fraud-network figures.

---

