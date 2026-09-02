---
layout: post
title: "Agentic Payments and the Future of Autonomous Commerce"
description: "Background: The Evolution of Digital Payments · Architecture of AI Agent Payments · 1 Core Architecture Components · 2 Two Dominant Integration Approaches"
date: 2026-03-05 20:25:00 +0800
categories: []
tags:
- Agentic Payments
keywords: [Agentic payment,AI agent commerce,autonomous payment infrastructure,AI payment security]
published: true
permalink: /Agentic Payments and the Future of Autonomous Commerce/
---

# AGENTIC PAYMENTS AND THE FUTURE OF AUTONOMOUS COMMERCE

**Technology Architecture, Ecosystem Development & Startup Opportunities**

*Research & Analysis Report | March 2026*

*Strategic Insights for Technology Leaders, Fintech Founders, Investors & Policymakers*


## 1. Executive Summary

Agentic payments represent a fundamental shift in how commerce is initiated and executed. Rather than a human consciously opening an app, entering credentials, and confirming a transaction, an AI agent acts autonomously on the user's behalf --- booking a ride, purchasing a subscription, or reordering supplies --- within pre-defined parameters set by the user.

The emergence of this paradigm was underscored by Mastercard's completion of its first live, authenticated agentic transaction in Singapore in early March 2026, conducted in partnership with DBS Bank and United Overseas Bank (UOB). In the demonstration, an AI agent booked a ride to Changi Airport through global mobility provider hoppa via CardInfoLink's AI agent, processing the payment over Mastercard's Agent Pay framework using unique agentic tokens and Mastercard Payment Passkeys. This milestone followed similar authenticated pilots by Mastercard in Australia, New Zealand, and India, and a parallel pilot by Visa's Intelligent Commerce platform with DBS in February 2026.

These concurrent developments signal that agentic payments have crossed from theoretical architecture into live financial infrastructure. The strategic implications are significant:

- Payment networks are racing to establish the identity and authentication standards that will govern AI-initiated commerce globally.
- Banks are positioning themselves as the governance layer --- the issuer-controlled trust anchor --- in agentic transaction flows.
- A new venture ecosystem is forming around agent identity, policy engines, merchant APIs, and AI risk management.
- Regulators must rapidly adapt frameworks designed for human-initiated transactions to address autonomous, multi-agent commerce.

For fintech leaders and investors, the next three to five years will determine which companies establish defensible positions in the infrastructure stack of agentic commerce. Those who act early --- particularly in identity delegation, merchant integration, and AI governance --- will capture outsized value.

---

## 2. Background: The Evolution of Digital Payments

To understand the significance of agentic payments, it is necessary to trace the arc of decision-making authority in commerce --- from entirely human-controlled transactions to the emerging model of delegated autonomy.

| **Era** | **Technology** | **Decision Authority** | **Authentication** |
|---|---|---|---|
| 1\. Cash | Physical currency | Fully human | Physical presence |
| 2\. Card Networks | Magnetic stripe / EMV chip | Human (card present) | PIN / signature |
| 3\. E-Commerce | Browser + payment gateways | Human (online form) | Password + 3DS |
| 4\. Mobile Wallets | NFC / tokenized cards | Human (tap to pay) | Biometric / PIN |
| 5\. Embedded Finance | APIs in non-financial apps | Human (in-app trigger) | OAuth / SSO |
| 6\. Agentic Payments | AI agents + policy engines | AI agent (delegated) | Agentic token + passkey |

The critical distinction across this evolution is the progressive decoupling of the payment decision from real-time human awareness. Embedded finance began this journey by making payments invisible at the point of experience (e.g., Uber's automatic billing). Agentic payments take this further: the AI determines not just how to pay, but when, whether, and to whom to pay, based on contextual reasoning and delegated authority.

Singapore represents an ideal incubator for this shift. A Visa-commissioned study found that close to 77% of Singapore residents already use generative AI tools in their daily lives, and 8 in 10 consumers rely on AI assistance when shopping online. This consumer readiness, combined with a progressive regulatory environment under the Monetary Authority of Singapore (MAS), has made the city-state the global staging ground for concurrent pilots by both major payment networks.

---

## 3. Architecture of AI Agent Payments

Understanding how agentic payments function technically is essential for both builders and risk managers. The architecture comprises several distinct layers that must interact seamlessly.

### 3.1 Core Architecture Components

| **Component** | **Function** | **Real-World Example** |
|---|---|---|
| AI Agent Layer | Reasons about user intent, selects merchant/service, initiates transaction | CardInfoLink AI agent booking hoppa airport ride |
| Delegated Identity | Cryptographic proof that the agent is authorized to act for the user within defined scope | Mastercard Payment Passkeys / Visa Trusted Agent Protocol |
| Agentic Token | Single-use or scoped credential representing a payment authorization for a specific transaction class | Unique agentic token per Mastercard Agent Pay transaction |
| Policy Engine | Enforces user-defined spending limits, merchant whitelist, time windows, and categories | Issuer-defined rules governing what agent can transact |
| Intent Verification | Confirms the agent's action matches the user's stated goal | Consent captured at session start; step-up triggers for anomalies |
| Risk Scoring | Real-time fraud and anomaly detection on agent-initiated flows | Behavioral pattern analysis across agentic and human transactions |
| Payment Network Rails | Routes, clears, and settles the transaction | Mastercard Agent Pay / Visa Intelligent Commerce infrastructure |
| Audit Mechanism | Immutable record of agent actions and authorizations for dispute resolution | Explainability logs; issuer audit trail; compliance records |

### 3.2 Two Dominant Integration Approaches

**API-Based Ordering (Preferred Architecture)**

In this approach, the AI agent interacts with merchant systems via structured APIs. The agent calls a booking or commerce API directly, passing authenticated credentials and policy-compliant parameters. This is the architecture employed in the Mastercard-hoppa-CardInfoLink Singapore pilot: the agent connects to hoppa's airport transport API and executes a structured booking call. The result is deterministic, auditable, and low-risk.

- Advantages: Predictable outputs, complete audit trail, merchant control over available agent actions
- Disadvantages: Requires merchants to build and maintain agent-ready APIs; ecosystem fragmentation in early stages

**Browser Automation (RPA-Style)**

Alternatively, agents can operate a browser, navigating merchant websites and interacting with UI elements as a human would. This requires no merchant cooperation but is significantly less reliable, more susceptible to UI changes, and creates substantial security and compliance risk.

- Advantages: Works with any merchant without integration; rapid deployment for early-stage agents
- Disadvantages: Not auditable at transaction level; vulnerable to prompt injection via web content; fails on multi-factor authentication flows

The industry direction --- as demonstrated by both Mastercard's Agent Pay and Visa's Intelligent Commerce frameworks --- is firmly toward API-based architectures with standardized authentication protocols.

---

## 4. Agent Pay vs. Traditional Payments: A Structural Comparison

| **Dimension** | **Traditional Payments** | **Agentic Payments** |
|---|---|---|
| Transaction Initiation | Human decides and manually triggers payment via app or terminal | AI agent reasons about goal, selects merchant and action, initiates autonomously |
| Authorization Model | Real-time explicit consent per transaction (OTP, biometric tap) | Pre-delegated policy scope; passkey credentials for transaction class |
| Authentication | 3DS, biometric, PIN at point of sale or checkout | Agentic token + passkey; issuer-controlled permission envelope |
| Risk Profile | Known human behavioral patterns, device fingerprinting | New: agent behavioral fingerprinting; hallucination risk; prompt injection vectors |
| Merchant Integration | Standard card acceptance via POS or payment gateway | Agent-ready API endpoints with structured commerce schemas required |
| Audit Trail | Cardholder statement; network transaction logs | End-to-end agent action logs; consent capture; explainability records |
| Dispute Resolution | Chargeback process between cardholder and merchant | Complex new categories: agent reasoning error, hallucination, prompt injection |
| Compliance Scope | PCI-DSS, PSD2 SCA, local card scheme rules | Above plus AI governance frameworks; explainability and audit requirements |

> **Key Insight: The Authorization Gap**
>
> The fundamental legal and technical challenge in agentic payments is the gap between when consent is granted (session start or onboarding) and when the transaction occurs (potentially hours or days later, autonomously). Bridging this gap with cryptographically verifiable, auditable, and revocable authorization is the core infrastructure problem that Mastercard, Visa, and their bank partners are racing to solve.

---

## 5. Ecosystem Requirements to Scale Agentic Payments

The Singapore pilots demonstrate proof of concept. Scaling from demonstration to ubiquity requires a mature, multi-stakeholder ecosystem. Six infrastructure layers must develop in parallel.

### 5.1 Delegated Identity Frameworks

The foundational requirement is a cryptographically verifiable way to establish that Agent X is authorized to act for User Y within Scope Z. Mastercard's approach uses Payment Passkeys linked to agentic tokens. Visa's Trusted Agent Protocol provides similar functionality. However, cross-network, cross-issuer, and cross-platform identity standards remain nascent. The analogy is OAuth 2.0 for web authentication --- agentic payments need an equivalent universal standard.

### 5.2 Merchant Agent-Ready APIs

Merchants must expose structured, authenticated APIs that agents can discover and call reliably. This requires standardized commerce schemas, agent discovery mechanisms, and action-level authorization controls. The hoppa integration in Singapore demonstrates this is technically achievable but demands significant merchant investment. The first wave of agent-ready merchants will be in high-frequency, low-complexity categories: transportation, food, accommodation, and entertainment.

### 5.3 AI Governance and Policy Engines

Banks and issuers are positioning themselves as the governance layer. The issuer's policy engine defines the constraints within which agents operate --- spending limits, merchant categories, geographic restrictions, and time windows. Building these policy engines into core banking infrastructure is a multi-year program for most institutions. Fintechs and middleware providers who offer policy engine capabilities as a service will find significant commercial opportunity in this gap.

### 5.4 Payment Network Integration

Mastercard and Visa are investing heavily in making their rails agentic-native. Both networks have established dedicated frameworks above existing card infrastructure. This is a strategic positioning decision: by owning the agentic authentication layer, networks ensure they remain in the flow of agentic transactions rather than being disintermediated by direct account-to-account transfers or alternative AI payment schemes.

### 5.5 Risk Monitoring Systems

New risk models are required that understand agentic behavioral patterns, detect agent impersonation, and identify anomalous instruction sequences that may indicate prompt injection attacks. Traditional fraud models trained on human behavior will have limited effectiveness against agentic transaction patterns without significant retraining and new feature sets.

### 5.6 Regulatory Frameworks

MAS in Singapore has signaled openness to AI-enabled commerce innovation. The European Banking Authority, US Federal Reserve, and other major regulators are actively studying agentic transaction models. Key unresolved regulatory questions include: Who bears liability when an agent executes an unauthorized transaction due to model error? How do strong customer authentication rules apply to delegated consent? What explainability standards apply to AI payment decisions?

---

## 6. Security and Risk Analysis

Agentic payments introduce novel risk vectors that do not exist in traditional payment systems. Security architecture must evolve accordingly, and industry participants should not assume existing fraud and risk controls will be adequate.

### 6.1 Principal Risk Vectors and Mitigations

| **Risk** | **Description** | **Severity** | **Key Mitigation** |
|---|---|---|---|
| Prompt Injection | Malicious instructions in merchant content or web pages hijack agent behavior to trigger unauthorized transactions | Critical | Sandboxed execution; API-only interactions; content sanitization |
| Unauthorized Agent Actions | Agent exceeds delegated scope due to reasoning errors or ambiguous policy definitions | High | Granular policy constraints; real-time anomaly detection; confirmation triggers for high-value actions |
| Merchant Spoofing | Fake API endpoints impersonate legitimate merchants to capture agentic payments fraudulently | High | Cryptographic merchant identity; PKI certificate chains; network allowlists |
| Model Hallucination | Agent confidently executes incorrect action based on fabricated or misunderstood information | Medium | Grounded tool calls with structured API responses; HITL for high-value transactions |
| Credential Theft | Theft of agentic tokens or passkeys allows attacker to transact as user within policy scope | Critical | Short-lived tokens; device-bound passkeys; step-up authentication on behavioral anomalies |
| Cumulative Overspending | Agent fails to track or apply aggregate spending limits across multiple small authorized transactions | Medium | Hard caps enforced at issuer level; real-time budget tracking; threshold alerts |

### 6.2 Structural Security Principles for Agentic Commerce

- **Principle of Least Privilege:** Agents should be granted the minimum transaction authority required to accomplish a specific defined task, scoped to time, amount, merchant category, and geography.
- **Immutable Audit Logs:** Every agent action --- including intermediate reasoning steps and API calls --- must be logged in a tamper-evident store to enable dispute resolution and regulatory review.
- **Explainability by Design:** The agent must be able to articulate why it took a specific payment action in human-readable terms that satisfy regulatory explainability requirements.
- **Revocability at Any Time:** Users must be able to instantly revoke agent authorization through any issuer channel, with immediate effect across all active agent sessions.
- **Issuer Override Capability:** The issuing bank must retain the ability to block, pause, or reverse agentic transactions at any time, regardless of the agent's authorization state.

> **Singapore Architecture Principle**
>
> Both the Mastercard/DBS/UOB and Visa/DBS pilots in Singapore explicitly position the issuing bank as the governance and trust anchor. All agentic transactions flow through issuer-controlled authentication and policy systems. This architecture is deliberate: it maintains the bank's role as the regulated entity accountable to the customer and regulator, ensuring liability is clearly assigned in the new paradigm.

---

## 7. Startup Opportunity Landscape & Competitive Analysis

The agentic payments ecosystem has seen a dramatic acceleration of both incumbent investment and startup activity since 2024. This section maps the live competitive landscape, profiles key companies by strategic layer, analyzes the protocol wars defining the space, and identifies the highest-potential directions for new ventures.

### 7.1 The Protocol Wars: Competing Standards

The most consequential competitive battle in agentic payments is not between startups --- it is between incompatible open standards being promoted by major technology platforms. Whoever's protocol becomes dominant will extract value from every agentic transaction that flows over it, regardless of which AI agent or payment method is used. Three major protocol camps have emerged:

| **Protocol** | **Led By** | **Key Partners** | **Approach** | **Status** |
|---|---|---|---|---|
| Agentic Commerce Protocol (ACP) | Stripe + OpenAI | Etsy, Shopify, PayPal, Walmart | Structured API: tokenized cart + delegated payment spec; merchant-friendly, open-source (Apache 2.0) | Live --- Instant Checkout in ChatGPT, Sept 2025 |
| Agent Payments Protocol (AP2) | Google Cloud | Mastercard, Amex, PayPal, Shopify, Coinbase, Airwallex, Klarna, Salesforce, 60+ partners | 3-layer mandate chain (Intent → Cart → Payment); on-chain audit trail; designed for delegated and autonomous tasks | Live --- announced Sept 2025, growing ecosystem |
| Intelligent Commerce / TAP | Visa | Microsoft, Nuvei, Shopify, Stripe, Worldpay, DBS | Trusted Agent Protocol (TAP): agent intent signaling, consumer recognition, credential transmission; issuer-controlled | Live pilot --- DBS Singapore Feb 2026 |
| Agent Pay Framework | Mastercard | Microsoft, IBM, Braintree, Checkout.com, PayPal | Agentic tokens + Payment Passkeys; agent registry (Agent Sign-Up); tokenization-first approach | Live --- Singapore, AU, NZ, IN, EU pilots |
| Universal Commerce Protocol (UCP) | Google + Shopify | Chrome (70%+ browser share) | Browser-native agent commerce built into Chrome; standardizes agent checkout across any website | Announced Jan 2026; Chrome integration rolling out |

> **Protocol War Strategic Implication**
>
> Five incompatible standards competing simultaneously risks fragmenting the ecosystem for 2--3 years before consolidation. For merchants, this means multiple integrations. For startups, protocol-agnostic abstraction layers --- tools that enable merchants or agents to work across ACP, AP2, and TAP with a single integration --- represent an immediate commercial opportunity analogous to payment gateway aggregators in the early e-commerce era.

### 7.2 State-of-the-Art Startup Companies by Layer

#### Layer 1: Agent Identity & Payment Infrastructure

The foundational infrastructure layer. Startups here are building the identity, wallet, and payment rails that are native to the AI agent economy rather than retrofitted from human payment systems.

**Skyfire** *(Leader)*

- **Headquarters:** San Francisco, USA
- **Founded:** 2023 \| Founders: Amir Sarhangi (ex-Google/Ripple), Craig DeWitt (ex-Ripple)
- **Funding:** \$9.5M Seed (Coinbase Ventures, a16z CSX, Neuberger Berman, Brevan Howard Digital, Circle, Ripple, Gemini, DRW)
- **Product:** World's first dedicated payment network for AI agents. Provides programmatic wallets with unique AgentID per agent, USDC + traditional rail funding, Know Your Agent (KYA) identity verification, granular spending controls, and a developer SDK for 10-minute integration
- **Open Protocol:** KYAPay --- open standard for agent identity, verified credentials, and payment capability. Compatible with MCP servers, Visa Intelligent Commerce, and existing APIs
- **Key Partners:** Visa Intelligent Commerce, APIFY, BuildShip, Forter, Cequence (security), ORY (identity)
- **Real Deployments:** Denso (auto parts B2B procurement), Payman (AI-to-human payments for task completion)
- **Market Claim:** Agent-to-agent commerce market projected at \$46B in 3 years (internal research)
- **Competitive Edge:** First mover; open protocol (KYAPay); stablecoin + fiat hybrid; Visa partnership; only purpose-built agent identity + payment stack as a service

#### Layer 2: Commerce Protocol & Merchant API Infrastructure

These companies are defining how merchants expose their catalogs, checkout flows, and inventory to AI agents via standardized interfaces.

**Stripe** *(Protocol Leader)*

- **Stage:** Pre-IPO \| Est. valuation ~\$65B \| Processed \$1.4T in payments (2024)
- **Agentic Product:** Agentic Commerce Protocol (ACP, co-developed with OpenAI, open-source Apache 2.0) + Instant Checkout in ChatGPT + Agentic Commerce Suite (Dec 2025) + Stripe MCP + Agent Toolkit
- **ACP Architecture:** Shared Payment Token (scoped per merchant + cart total) isolates credentials; merchant retains brand, order, and fulfillment control; open to any AI agent and any PSP
- **Live Partners:** OpenAI (ChatGPT Instant Checkout), Etsy (launch partner), 1M+ Shopify merchants (coming soon), Glossier, Vuori, Spanx, SKIMS
- **Strategic Position:** Attempting to become the default payment infrastructure for the AI agent era, as it was for the SaaS era. ACP gives Stripe distribution across any AI platform, not just OpenAI
- **Key Risk:** Google's AP2 and Visa's TAP could bifurcate the market; Stripe's open-source stance mitigates lock-in concerns but may commoditize processing fees

**Payrails** *(Challenger)*

- **Headquarters:** Berlin, Germany
- **Funding:** \$32M raised (latest round June 2025); backed by J.P. Morgan, HV Capital, Earlybird
- **Product:** Orchestration infrastructure for enterprise payments: routing, policy engine, and reconciliation across multiple PSPs. Positioning as the control layer for agentic payment flows in B2B and enterprise contexts
- **Agentic Angle:** Policy engine and multi-PSP routing makes Payrails a natural fit for enterprise deployments that need governance over AI agent-initiated transactions across multiple payment methods and geographies
- **Traction:** Strong traction with European enterprise clients; backed by J.P. Morgan's strategic investment signals institutional validation
- **Competitive Edge:** Enterprise trust, European regulatory expertise, multi-PSP orchestration that no single-network solution provides

**Airwallex** *(Challenger)*

- **Stage:** Late-stage / unicorn; present in 150+ countries
- **Agentic Product:** AP2 launch partner (Google Agent Payments Protocol); building agent-native payment infrastructure for global, cross-border agentic transactions
- **Strategic Quote:** AP2 "gives businesses and consumers the confidence to delegate tasks to AI agents" --- Jacob Dai, Co-Founder & CTO
- **Competitive Edge:** Global payment rails across 150+ countries; AP2 founding partner status; strong APAC presence aligns with Singapore-led agentic commerce buildout

#### Layer 3: AI Commerce Agents (Application Layer)

These are the agent platforms closest to the consumer or enterprise end user, building experiences powered by the infrastructure layers above.

**Perplexity** *(Leader)*

- **Stage:** Series D; valuation ~\$9B (2025)
- **Agentic Product:** Buy with Pro --- first AI commerce agent to market in consumer segment (launched November 2024). Expanded to free tier with PayPal partnership (November 2025). Comet browser agent for autonomous web shopping
- **Model:** AI search + commerce in one flow: product discovery, comparison, and one-click checkout without leaving Perplexity
- **Partners:** PayPal (payment layer), Shopify merchants, AP2 (Google)
- **Controversy:** Amazon sent cease-and-desist over Comet browser agent scraping Amazon product pages; highlights legal risk of browser-automation approach
- **Competitive Edge:** First mover in consumer AI shopping; 100M+ MAU distribution; PayPal integration gives immediate payment rails

**OpenAI (Apps)** *(Protocol Leader)*

- **Stage:** ChatGPT: 700M+ weekly active users (2026)
- **Agentic Product:** Instant Checkout (Sept 2025) --- single-item purchase within ChatGPT. Operator (Jan 2025) --- web agent for autonomous task completion including travel, restaurant bookings. ACP protocol co-developer
- **Commerce Model:** Charges merchants a fee per completed Instant Checkout purchase; products ranked by relevance, not ad spend (initially). Expanding to Shopify merchants
- **Partners:** Stripe (payment infrastructure), Etsy (launch), PayPal, Walmart, Target
- **Scale Advantage:** 700M user distribution is unmatched; turns ChatGPT into a commerce channel with no additional acquisition cost for merchants
- **Key Risk:** Regulatory scrutiny as ChatGPT becomes a marketplace; merchant dependency on OpenAI ranking algorithms; competition from Google UCP in Chrome

**Salesforce Agentforce** *(Challenger)*

- **Stage:** Public company; Agentforce launched Sept 2025
- **Agentic Product:** Enterprise AI agent platform with embedded commerce capabilities. ACP-compatible; enables B2B autonomous procurement, customer service, and order management agents
- **Agentic Payments:** AP2 founding partner; integrating autonomous payment execution into enterprise CRM and sales workflows
- **Target Market:** Enterprise B2B; 150,000+ Salesforce customers represent immediate distribution for agentic commerce features
- **Competitive Edge:** Existing enterprise relationships, data, and trust; Agentforce can layer agentic payments onto existing business processes rather than requiring greenfield adoption

#### Layer 4: Agent Risk, Fraud & Compliance Infrastructure

A critical layer that will become mandatory as volumes scale. Existing fraud tools were designed for human transaction patterns and require significant rearchitecting for agent-native risk.

**Sardine** *(Challenger)*

- **Headquarters:** San Francisco, USA
- **Product:** Fraud and compliance platform for fintech and crypto. Sardine is positioned at the forefront of "Know Your Agent" (KYA) risk frameworks, adapting its behavioral analytics to detect anomalous AI agent transactions
- **Agentic Position:** Sardine's Head of Strategy explicitly flagged the agent identity and fraud problem in 2024: "How do you know the AI agent is operating within your consent? How do you link each payment back to a verified identity?" --- making it an early analyst and builder in agent-native risk
- **Competitive Edge:** Deep fintech/crypto fraud expertise; device intelligence + behavioral models adaptable to agent behavioral fingerprinting; strong compliance tooling

**Forter** *(Challenger)*

- **Stage:** Series F; valuation ~\$3B
- **Agentic Product:** Skyfire partner for agent identity verification. Forter's merchant identity network and fraud decisioning platform is being adapted to recognize and score AI agents as a distinct transaction initiator class
- **Competitive Edge:** Merchant network effects (shared fraud signals across thousands of merchants); real-time decisioning; Skyfire partnership gives early agentic agent data

#### Layer 5: B2B Autonomous Procurement

The largest addressable market in agentic commerce. Enterprise procurement and accounts payable represent the most immediate high-value opportunity for fully autonomous AI-initiated payments.

**Zip (formerly Zip Co)** *(Challenger)*

- **Stage:** Public / Growth stage (ASX: ZIP)
- **Agentic Angle:** B2B procurement automation with AI-enhanced purchase approval and payment routing. Positioned to embed agentic payment execution into existing enterprise purchasing workflows
- **Market:** Enterprise procurement software market; agentic layer adds autonomous PO generation, supplier selection, and payment execution

**Payman** *(Emerging)*

- **Headquarters:** USA
- **Product:** Enables AI agents to pay humans for completed tasks --- effectively building the payment rails for human-in-the-loop AI workflows where agents hire and compensate contractors autonomously
- **Skyfire Customer:** One of Skyfire's early reference customers; Payman's AI agents now hire and pay contractors fully autonomously via Skyfire's payment network
- **Market Opportunity:** AI-to-human payment flows are a new category; as AI agents increasingly delegate sub-tasks to human workers or specialized AI services, autonomous micropayment infrastructure becomes essential

### 7.3 Competitive Positioning Matrix

| **Company** | **Layer** | **Focus** | **Protocol Position** | **Funding / Scale** | **Moat Strength** |
|---|---|---|---|---|---|
| Skyfire | Identity + Payment Rail | B2B-first, expanding to consumer | KYAPay (open standard) | \$9.5M Seed | ★★★★ --- Only purpose-built agent identity + payment rail |
| Stripe (ACP) | Commerce Protocol + Processing | Consumer + Enterprise | ACP co-author (open) | Pre-IPO ~\$65B | ★★★★★ --- 15yr payment network + OpenAI distribution |
| Google (AP2/UCP) | Protocol + Browser | Consumer via Chrome (70% share) | AP2 + UCP author | Alphabet subsidiary | ★★★★★ --- Chrome browser ubiquity is unmatched distribution |
| Mastercard (Agent Pay) | Network + Token | Issuer/Bank-facing | Agent Pay + TAP-compatible | Public ~\$460B mkt cap | ★★★★★ --- Network trust + tokenization + bank relationships |
| Visa (Intelligent Commerce) | Network + Protocol | Issuer/Bank-facing | TAP author | Public ~\$560B mkt cap | ★★★★★ --- Largest card network; DBS pioneer partnership |
| OpenAI (Operator/ACP) | AI Agent + Protocol | Consumer (700M users) | ACP co-author | Private ~\$340B val. | ★★★★★ --- 700M user distribution creates instant commerce scale |
| Perplexity (Buy w/ Pro) | AI Commerce Agent | Consumer | AP2 + PayPal | Series D ~\$9B val. | ★★★ --- First mover but browser agent legal risk |
| Payrails | Policy Engine + Orchestration | Enterprise B2B | Multi-PSP agnostic | \$32M, J.P. Morgan backed | ★★★★ --- Enterprise trust + multi-rail governance |
| Airwallex | Cross-border Payments | Global enterprise | AP2 founding partner | Unicorn | ★★★★ --- 150+ country rails + APAC strength |
| Sardine | Fraud + Risk + Compliance | Fintech/Crypto/Enterprise | Network-agnostic | Series C | ★★★★ --- Behavioral data moat; KYA early mover |
| Salesforce (Agentforce) | Enterprise Agent Platform | Enterprise B2B | AP2 + ACP compatible | Public ~\$260B mkt cap | ★★★★ --- 150K enterprise customer base as distribution |
| PayPal | Consumer Wallet + Merchant Network | Consumer + SMB | ACP + AP2 + Agent Pay | Public ~\$80B mkt cap | ★★★★ --- 400M users; multiple protocol hedging strategy |

### 7.4 High-Potential Directions: Identified White Space

Competitive analysis of the current landscape reveals several undercapitalized layers where the largest new companies are likely to emerge. These represent genuine white space --- areas where incumbent investment is insufficient, startup density is low, and market need is structurally large.

> **Direction 1: Protocol-Agnostic Merchant Integration Layer (Highest Conviction)**
>
> The single most acute near-term pain point for merchants is the fragmentation of ACP, AP2, TAP, and Agent Pay into incompatible standards requiring separate integrations. A startup that builds a universal adapter --- enabling merchants to publish once and be discoverable and transactable across all major protocols --- would capture a mandatory infrastructure position in every agentic commerce flow. Analogous to how Stripe unified payment gateway fragmentation in the 2010s. The window to become this layer is open now, before any single protocol achieves dominance. Estimated TAM: Every merchant that wants to sell through AI agents globally.

> **Direction 2: Know Your Agent (KYA) Identity & Reputation Network**
>
> Skyfire has pioneered KYAPay, but the market requires a neutral, cross-network KYA registry that any issuer, merchant, or platform can query to verify agent identity and transaction history. This is not about processing payments --- it is about building the equivalent of a credit bureau for AI agents. An agent's transaction history, dispute rate, and behavioral consistency should inform whether a merchant accepts an agent-initiated order, just as credit history informs a lender. First movers will accumulate proprietary agent reputation data that becomes the foundation of a network-effects business. Estimated TAM: Every issuer, merchant, and platform participating in agentic commerce globally.

> **Direction 3: Enterprise AI Procurement Orchestration (Largest B2B Opportunity)**
>
> B2B commerce represents the majority of global payment volume by value. The enterprise procurement workflow --- requisition, approval, supplier selection, purchase order, payment, reconciliation --- is deeply manual and paper-intensive at most organizations. An AI agent platform that can orchestrate this end-to-end, integrating with ERP systems (SAP, Oracle), existing approval workflows, and agentic payment rails, addresses a problem worth hundreds of billions in operational cost annually. Salesforce Agentforce is approaching this from the CRM side; no pure-play startup has yet achieved dominant enterprise traction. The window is open for a dedicated autonomous procurement agent company built on top of AP2/ACP rails.

> **Direction 4: Agentic Payment Compliance & Audit Infrastructure (Regulatory Moat)**
>
> The EU AI Act's major obligations are taking force in 2026. US regulators are actively studying agentic payments. Every bank, payment network, and enterprise that operates agentic payment flows will require: audit-ready logs of agent actions, explainability reports for regulators, dispute documentation for chargebacks, and compliance monitoring for KYC/AML in agent-initiated flows. No dedicated RegTech company has yet built tooling specifically for agentic payment compliance. Companies that establish themselves as the compliance standard before regulations are finalized will be very difficult to displace. This is a high-margin, high-switching-cost business with a clear regulatory tailwind.

> **Direction 5: Consumer Agent Delegation & Control Platform**
>
> As consumers begin authorizing multiple AI agents across multiple apps to make payments on their behalf, they will need a unified dashboard to manage, monitor, and revoke these authorizations. No bank, network, or startup has yet built a compelling consumer-facing product for this. The analogy is password managers (LastPass, 1Password) for the AI era: a trust and control product that becomes sticky through safety and peace of mind rather than switching costs. The company that builds consumer trust in agentic delegation will have extraordinary leverage as the market matures.

### 7.5 Market Size Projections

| **Analyst / Source** | **Projection** | **Timeframe** | **Scope** |
|---|---|---|---|
| Edgar Dunn & Co. | \$1.7 trillion in AI-driven commerce value | By 2030 | Global AI-driven commerce |
| McKinsey | \$1 trillion in US retail market alone | By end of decade | US retail agentic commerce |
| Morgan Stanley | \$190B--\$385B in additional US e-commerce | By 2030 | 10%--20% market penetration |
| Bain | \$300B--\$500B in agentic commerce market | By 2030 | 15%--25% of total online retail |
| Skyfire (internal) | \$46 billion in agent-to-agent commerce | Next 3 years | Agent-to-agent transactions only |
| PayPal CEO Alex Chriss | 25% of online sales from AI agents | By 2030 | Global online retail |

The convergence of multiple independent projections in the \$300B--\$1.7T range by 2030 suggests strong analyst consensus on the scale of the opportunity, even if specific estimates vary widely. The most conservative projections (Morgan Stanley at \$190B) still represent a transformative new revenue category for payment infrastructure. Importantly, the agent-to-agent commerce segment --- AI agents transacting with other AI services autonomously --- is a net-new market that did not exist in prior payment era analyses, and may ultimately dwarf the consumer agentic shopping market.

---

## 8. Industry Implications

### 8.1 Payment Networks: A Platform Power Competition

Mastercard and Visa are not passive participants in the agentic payments transition --- they are making strategic investments to ensure they own the authentication and trust layer for AI-initiated transactions. Mastercard's Agent Pay framework and its new regional AI Center of Excellence in Singapore, and Visa's Intelligent Commerce suite with its Trusted Agent Protocol, represent significant bets that the networks' greatest long-term value lies in being the trust infrastructure of the agentic economy.

The competitive dynamics between the two networks will intensify. Both are courting the same institutions: DBS has simultaneously engaged pilots with both Mastercard and Visa, a deliberate dual-track strategy. The network that establishes the dominant identity standard will have extraordinary leverage over the entire ecosystem, including the ability to extract value from non-card payment flows that traverse their trust rails.

### 8.2 Banks: From Account Custodians to Agent Governors

The most strategically significant positioning in the Singapore pilots is the issuing bank's role as the governance and policy layer. DBS and UOB are not just providing the payment account --- they are defining the rules under which AI agents can operate on behalf of their customers. This is a powerful extension of the bank's trust relationship with the consumer, positioning banks as essential intermediaries in the agentic economy rather than candidates for disintermediation.

### 8.3 Merchants: The Agent-Readiness Imperative

For merchants, the coming years will demand an investment parallel to the e-commerce buildout of the early 2000s. Just as merchants had to build web storefronts and payment gateway integrations to participate in online commerce, they will need to build agent-ready APIs and structured commerce schemas to be discoverable and transactable by AI agents. Merchants who delay will risk exclusion from AI-mediated shopping flows, which will represent an increasing share of consumer spending in high-frequency categories.

### 8.4 Fintech Startups: Infrastructure Before Application

Fintech startups should approach agentic commerce with a clear-eyed sequencing perspective. Consumer-facing agentic shopping applications cannot scale before the identity, policy, and merchant API infrastructure matures. The highest near-term opportunity is in building the infrastructure components that application-layer products will depend upon. Founders who have studied the evolution of cloud infrastructure, API ecosystems, and developer platforms will recognize the pattern.

---

## 9. Future Outlook

| **Horizon** | **Key Developments** | **Dominant Use Cases** |
|---|---|---|
| 0--3 Years | Standardization of agent identity protocols; bank policy engines mature; major merchant API buildout; initial regulatory guidance from MAS, EU, US | Transport & travel booking; food & beverage ordering; subscription management; B2B reordering |
| 3--5 Years | Cross-network agentic token interoperability; agent-native marketplace platforms; enterprise procurement automation at scale; consumer agent delegation mainstream | Autonomous enterprise procurement; personal finance agents managing investments and bills; AI-native retail experiences |
| 5--10 Years | Machine-to-machine commerce normalized; AI agents transacting with AI agents; new asset classes emerge (agent wallets, AI entity credit scores); global regulatory harmonization | Fully autonomous supply chains; AI-managed personal wealth; machine economy commerce at internet scale |

### 9.1 Near-Term (0--3 Years): Infrastructure Build-Out

The immediate phase will be characterized by intense investment in foundational standards. Mastercard and Visa will compete to establish their respective frameworks as the industry default. Major banks will invest in policy engine capabilities. Merchants in high-frequency categories --- transportation, travel, food, entertainment --- will prioritize agent-ready API development. Regulators will begin publishing guidance on AI agent authorization, liability allocation, and explainability requirements, with Singapore and the EU likely to lead.

### 9.2 Medium-Term (3--5 Years): Scale and Consolidation

As infrastructure matures, application-layer use cases will scale rapidly. Enterprise B2B procurement automation will move from pilot to production at large corporations. Personal AI finance agents will manage routine transactions, recurring bills, and potentially investment rebalancing within defined parameters. The venture landscape will consolidate as winners emerge in each infrastructure layer, and acquisition activity will accelerate as incumbents buy proven capabilities.

### 9.3 Long-Term (5--10 Years): The Machine Economy

The most profound long-term implication is the emergence of genuine machine-to-machine commerce. When AI agents representing individual consumers, enterprises, IoT devices, and automated systems can transact autonomously with each other, the structure of commerce itself changes. New questions of AI entity identity, creditworthiness, and accountability will require entirely new legal and financial frameworks. The companies that build trust infrastructure in the near term will have disproportionate influence over how this machine economy is governed.

---

## 10. Conclusion

The completion of live, authenticated agentic payment transactions in Singapore by Mastercard, DBS, and UOB in early 2026 --- alongside parallel pilots by Visa and DBS --- marks more than a technical milestone. It signals the beginning of a structural transformation in how commerce is initiated, authorized, and governed. The shift of payment decision-making authority from human to AI agent is not incremental; it is a categorical change requiring new infrastructure, new standards, new business models, and new regulatory frameworks.

Three strategic conclusions stand out for leaders across the ecosystem:

1. The identity and delegation layer will be the most consequential infrastructure investment of the next five years. Whoever establishes the standard for how AI agents are credentialed and authorized will hold structural power over the entire agentic commerce ecosystem, determining who participates and on what terms.

2. Banks that embrace the governance role --- rather than viewing agentic payments as a disintermediation threat --- will emerge as essential infrastructure in the AI economy. The issuer-as-policy-governor model demonstrated in Singapore is the template for how regulated financial institutions can extend their relevance into the agentic paradigm.

3. The startup opportunity is primarily in infrastructure, not application. Founders and investors who prioritize the agent identity, policy engine, merchant API, and compliance layers will create more durable and defensible value than those who build consumer-facing agents before the underlying infrastructure has matured.

Singapore's position as the global staging ground for concurrent agentic payment pilots reflects the city-state's deliberate strategy to lead in AI-enabled financial innovation under the MAS's progressive regulatory framework. For the global fintech community, the signal is unambiguous: agentic commerce is not a future concept. The infrastructure is being built now, the pilots are live, and the window to establish foundational positions is open.

---

## References & Sources

All sources cited in this report are listed below, grouped by category. URLs were verified as of March 2026.

### Pilot Announcements & Press Releases

**\[1\]** Mastercard. "Mastercard Completes First Live Authenticated Agentic Transaction in Singapore with DBS and UOB." Press Release, March 2026. The Asian Banker / Fintech News Singapore.
<https://www.theasianbanker.com/press-releases/mastercard-completes-first-live-authenticated-agentic-transaction-in-singapore-with-dbs-and-uob>

**\[2\]** DBS Bank. "DBS is First Bank in Asia Pacific to Pilot Visa Intelligent Commerce for Everyday Payments." PRNewswire, February 16, 2026.
<https://www.prnewswire.com/apac/news-releases/dbs-is-first-bank-in-asia-pacific-to-pilot-visa-intelligent-commerce-for-everyday-payments-302688457.html>

**\[3\]** Mastercard. "Mastercard Unveils Agent Pay, Pioneering Agentic Payments Technology to Power Commerce in the Age of AI." Press Release, April 2025.
<https://www.mastercard.com/global/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html>

**\[4\]** Fintech News Singapore. "Mastercard Completes First Live AI Agent Payment in Singapore With DBS, UOB." March 2026.
<https://fintechnews.sg/127200/ai/mastercard-ai-agent-singapore/>

**\[5\]** Fintechfutures. "Santander and Mastercard Test Payments with Agents." March 2026.
<https://www.fintechfutures.com/ai-in-fintech/mastercard-santander-complete-agentic-payment>

**\[6\]** East & Partners. "DBS and Westpac Pilot Agent-Led Payments." 2025.
<https://eastandpartners.com/news/dbs-and-westpac-pilot-agent-led-payments/>

**\[7\]** Peachwire / Payments Industry Intelligence. "Visa and Mastercard Accelerate Agentic Payments Through Bank Pilots." February 2026.
<https://www.peachwire.com/visa-and-mastercard-accelerate-agentic-payments-through-bank-pilots/>

### Protocol & Standards Documentation

**\[8\]** Stripe + OpenAI. "Stripe Powers Instant Checkout in ChatGPT and Releases Agentic Commerce Protocol (ACP) Co-Developed with OpenAI." Press Release, September 29, 2025.
<https://stripe.com/newsroom/news/stripe-openai-instant-checkout>

**\[9\]** Stripe Engineering Blog. "Developing an Open Standard for Agentic Commerce." September 2025.
<https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce>

**\[10\]** Stripe Engineering Blog. "Introducing Our Agentic Commerce Solutions." October 2025.
<https://stripe.com/blog/introducing-our-agentic-commerce-solutions>

**\[11\]** OpenAI Developer Documentation. "Agentic Commerce Protocol: Get Started."
<https://developers.openai.com/commerce/guides/get-started/>

**\[12\]** Google Cloud Blog. "Announcing Agent Payments Protocol (AP2)." September 16, 2025.
<https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol>

### Startup Funding & Company Profiles

**\[13\]** Business Wire. "Introducing Skyfire: Payment Rails for AI." August 21, 2024.
<https://www.businesswire.com/news/home/20240821247203/en/Introducing-Skyfire-Payment-Rails-for-AI>

**\[14\]** The Block. "Coinbase Ventures and a16z's CSX Bring Skyfire's Total Funding to \$9.5 Million." October 24, 2024.
<https://www.theblock.co/post/322742/coinbase-ventures-and-a16zs-csx-bring-skyfires-total-funding-raised-to-9-5-million>

**\[15\]** Business Wire. "Skyfire Exits Beta with Enterprise-Ready Payment Network for AI Agents." March 6, 2025.
<https://www.businesswire.com/news/home/20250306938250/en/Skyfire-Exits-Beta-with-Enterprise-Ready-Payment-Network-for-AI-Agents>

**\[16\]** TechCrunch. "Skyfire Lets AI Agents Spend Your Money." August 21, 2024.
<https://techcrunch.com/2024/08/21/skyfire-lets-ai-agents-spend-your-money/>

**\[17\]** Tracxn. "Skyfire --- 2026 Company Profile, Team, Funding & Competitors." January 2026.
<https://tracxn.com/d/companies/skyfire/__-gSNwLdAbLR2EH3jQO5ja24BZ2dqjmKWC_BS3-4pf1s>

**\[18\]** Sifted. "How Infrastructure Is Changing Agentic Payments: 'A Quiet but Fundamental Shift'." 2025.
<https://sifted.eu/articles/infrastructure-agentic-payments-brnd>

### Industry Analysis & Research Reports

**\[19\]** McKinsey & Company. "The Agentic Commerce Opportunity: How AI Agents Are Ushering in a New Era for Consumers and Merchants." October 17, 2025.
<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants>

**\[20\]** Forrester Research. "The Race to Agentic Payments in US B2C E-Commerce: Where We Are Now." November 24, 2025.
<https://www.forrester.com/blogs/the-race-to-agentic-payments-in-us-b2c-e-commerce-where-we-are-now/>

**\[21\]** Fintech Wrap Up. "Deep Dive: Agentic AI in Payments and Commerce." June 8, 2025.
<https://www.fintechwrapup.com/p/deep-dive-agentic-ai-in-payments>

**\[22\]** Finextra / Nikita Zelezkins. "Agentic AI in Payments in 2026: What's Real, What's Pilot and What's Still Hype." February 2026.
<https://www.finextra.com/blogposting/30920/agentic-ai-in-payments-in-2026-whats-real-whats-pilot-and-whats-still-hype>

**\[23\]** PANews. "As AI Reshapes the Shopping Experience, How Much Time Does PayPal Have Left?" February 2026.
<https://www.panewslab.com/en/articles/019c708e-1e70-7095-ae52-722ffb7e7886>

**\[24\]** Tiger Research. "AI Agent Payment Infrastructure: The Direction of Crypto and Big Tech." February 2026.
<https://reports.tiger-research.com/p/aiagentpayment-eng>

### News Coverage & Payments Trade Press

**\[25\]** Payments Dive. "Stripe Pushes Agentic AI Sales via Chat." September 30, 2025.
<https://www.paymentsdive.com/news/stripe-pushes-agentic-ai-sales-via-chatgpt-openai-artificial-intelligence/761439/>

**\[26\]** Digital Commerce 360. "OpenAI Expands Agentic Commerce Push." February 2026.
<https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/>

**\[27\]** Digital Commerce 360. "Visa and Mastercard Both Launch New Agentic AI Payments Tools." October 16, 2025.
<https://www.digitalcommerce360.com/2025/10/16/visa-mastercard-both-launch-agentic-ai-payments-tools/>

**\[28\]** CIO Magazine. "Agentic Payments Are Coming. Is Your Company Ready?" March 2026.
<https://www.cio.com/article/4137893/agentic-payments-are-coming-is-your-company-ready.html>

**\[29\]** SiliconAngle. "AI Payment Processing Startup Skyfire Launches with \$8.5M in Funding." August 21, 2024.
<https://siliconangle.com/2024/08/21/ai-payment-processing-startup-skyfire-launches-8-5m-funding/>

**\[30\]** Fintech News Singapore. "DBS First APAC Bank to Pilot AI-Powered Agent Payments with Visa." February 2026.
<https://fintechnews.sg/126516/ai/dbs-visa-agentic-ai/>

### Regulatory & Risk Context

**\[31\]** Finextra. "Skyfire Raises \$8.5M to Bring Autonomous Payments to AI Agents." August 2024.
<https://www.finextra.com/newsarticle/44621/skyfire-raises-85m-to-bring-autonomous-payments-to-ai-agents>

**\[32\]** AI CERTs News. "Agent Payments Reshape 2025 Commerce." December 2025.
<https://www.aicerts.ai/news/agent-payments-reshape-2025-commerce/>

---