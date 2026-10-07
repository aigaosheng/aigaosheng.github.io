---

layout: post
title: "The MAS AI Risk Management Cookbook for Fintech and Payments"
description: "A practitioner's cookbook for fintech and payment firms: how to read, scope and implement the MAS Guidelines on AI Risk Management, with recipes, templates, a roadmap and a self-assessment checklist."
date: 2026-10-07 22:35:00 +0800
categories: [regulation, ai-governance]
type: post
published: true
status: publish
categories: []
tags: [MAS, AI risk management, AI governance, fintech, payments, Singapore, FEAT, generative AI, agentic AI, model risk, third-party risk, fraud, AML]
permalink: /ai-governance/mas-ai-risk-management-cookbook/

---

## Why this cookbook

On 7 October 2026 MAS issued its *Guidelines on Artificial Intelligence Risk Management* (the "Guidelines"). They set out what MAS expects from financial institutions (FIs) on AI oversight, governance systems, life cycle controls and capabilities. They explicitly cover generative AI and AI agents.

For payment companies and fintechs the practical questions are:

1. Does this apply to us, and how hard?
2. What do we have to build first?
3. What does "good" look like for our actual use cases: fraud scoring, AML alert triage, KYC, chargebacks, chatbots, internal copilots?

This cookbook answers those with **recipes**: short, ordered steps tied to paragraph numbers in the Guidelines (written ¶x.x). The paragraph references are the source of truth. The templates and scoring examples are **our suggestions**, not MAS requirements, and are labelled as such.

## At a glance

| Item | What the Guidelines say | Ref |
|---|---|---|
| Nature | Supervisory expectations (not a licence rule by themselves). Complement FEAT and other MAS guidance. | ¶1.1, ¶1.2 |
| What counts as AI | Machine-based systems that derive outputs from learned premises (data or inputs). Includes ML, deep learning, NLP, computer vision, generative AI, AI agents. Rule-based logic, hand-written formulae and fixed-script RPA are not ordinarily AI. | ¶1.3, fn 6 |
| Who | All FIs, applied proportionately. Group-basis application for locally incorporated FIs under consolidated supervision (banking and insurance) or owners of critical information infrastructure. | ¶1.2, ¶2.1, fn 4–5 |
| Starts | Take effect **7 October 2027**. Sections 3–4 (oversight, identification, inventory, materiality) from that date. Sections 5–6 (life cycle controls, capability and capacity) by **7 October 2028**. | ¶1.8 |
| Core idea | Know your AI, rate its risk, and scale controls to the rating. | ¶4.1, ¶5.2 |

**Reading note on timing.** ¶1.8 says the Guidelines take effect on 7 October 2027 and that FIs "may meet" Sections 3–4 from then and Sections 5–6 by 7 October 2028. Our reading is a two-step transition. Confirm with Compliance whether MAS has given any further transition guidance.

## Mise en place: five ideas to hold before you start

**1. Risk-based, not one-size-fits-all.** Controls scale with the risk materiality of each AI *use case* (¶1.6, ¶2.1, ¶5.2). Do not apply the heaviest process to every tool, or you will drown. Do not apply the lightest to everything, or you will miss the risky ones.

**2. Use case, system and model are different things (¶1.4).**

| Term | Plain meaning | Payments example |
|---|---|---|
| Model | A method that turns inputs into outputs | A gradient-boosted fraud score |
| System | One or more models plus other machine components | The real-time decisioning service that calls the model, rules and a case tool |
| Use case | The specific real-world context it is applied to | Auto-declining card-not-present transactions above a score threshold |

The same model can sit in a low-risk and a high-risk use case. Rate the *use case*.

**3. AI is an extension of existing risks.** MAS frames AI risk as amplifying familiar categories: financial, operational, conduct, financial crime and reputational (¶1.9). Generative AI adds security, privacy, IP, third-party, operational and human-factor risks (¶1.10). Agents add the risk of autonomous, wrong or unauthorised actions and data exfiltration at scale (¶1.11).

**4. Accountability stays with you.** You keep primary accountability for third-party AI (¶5.11). You can lean on a global group's framework only if it meets the Guidelines, and local senior management stays accountable for Singapore (¶1.5, ¶3.6).

**5. Rules are not AI, but be careful where the line blurs.** A hand-written rule such as "decline if country is on list X" is not AI (fn 6). A threshold or rule set *derived from data by a learning method* appears more likely to be in scope. Let your designated control function make that call (¶4.3).

---

## Recipe 1: Decide your governance tier (basic or full)

**Use when:** you are triaging a long list of AI tools and need to know where to spend effort.
**Refs:** ¶2.2–2.5, fn 12–13.

**Steps**

1. List each AI use. For each, ask the ¶2.3 question: *if this AI performs poorly or is unavailable, is a material adverse impact on the firm, customers or other stakeholders unlikely?* Consider financial, operational, regulatory, legal and reputational impact, and fairness and consumer-protection impact on customers.
2. If **yes**, the use may sit under **basic AI governance** (¶2.3, ¶2.5).
3. If **no or unsure**, treat it as a full-governance use case and continue to Recipes 2–14. When unsure, take the safer path.
4. Write the decision down with the reason, and have the control function review it.

**What MAS gives as examples of basic-tier use (¶2.4)**, provided humans check outputs before use (fn 13): drafting or rephrasing customer emails, summarising documents or meeting notes, first-pass document review for internal reference, generating formulas or charts, AI image tools for marketing or internal material, and internal chatbots that point staff to policies.

**Basic governance minimum set (¶2.5)**

| # | Element | Practical form |
|---|---|---|
| a | Clear accountability | A named senior manager owns AI oversight |
| b | Permitted and prohibited uses, plus human oversight | One-page acceptable-use policy. Example in MAS text: no confidential, proprietary or client information in public AI tools. State when human review is mandatory. |
| c | Approved tool list and approval process | A register of approved tools and a request form |
| d | Staff education | Short annual training plus onboarding |
| e | Regular compliance checks | Sampling of usage, DLP alerts, access reviews |
| f | Periodic and trigger-based review | Re-test "is it still basic?" yearly and whenever scope, data or vendor changes |

**Watch-outs for payments**

- A "basic" tool becomes full-tier the moment it touches a customer decision, a funds flow, or is used without human review. Write that trigger into the policy.
- Even for low-materiality AI, MAS says data management, safety and cybersecurity controls remain relevant and should be applied proportionately (fn 12). Copilots are not exempt from data rules.

---

## Recipe 2: Stand up board and senior management oversight

**Use when:** you need the governance spine in place before the 7 October 2027 start.
**Refs:** ¶3.1–3.6. **[Sign-off]**

**Steps**

1. **Choose the structure.** MAS allows a new central AI risk function or managing incremental AI risk through existing functions, as long as management is consistent and coordinated (¶3.3). Small firms usually extend existing model-risk, technology-risk and compliance functions and add a cross-functional AI committee (fn 16).
2. **Map existing frameworks.** Check that model, operational, reputational, data, technology and cyber, third-party, legal and compliance, financial and conduct risk frameworks each cover AI (¶3.2, fn 14). Note gaps.
3. **Assign the board's items (¶3.4):** approve and regularly review the AI governance approach; put AI risk explicitly in the **risk appetite framework**; set board and management roles; make sure the board understands AI well enough to challenge; and review all of this as AI and strategy change.
4. **Assign senior management's items (¶3.5):** implement and review frameworks; control risk across the whole life cycle; define roles across business lines and control functions; run an **escalation process** for AI incidents and threshold breaches; report to the board in a timely way; and resource and train people.
5. **Group firms:** local management should receive timely Singapore-relevant reports, have clear escalation paths, and be able to show MAS how it discharges oversight even when using group frameworks (¶3.6).

**Template: AI risk appetite statements (illustrative, based on fn 18 ideas)**

*Qualitative*
- "We do not allow AI to make final, un-reviewed decisions to freeze customer funds or close accounts."
- "We do not put customer personal data or card data into public AI tools."

*Quantitative (set your own numbers with Risk)*
- Number or financial impact of AI incidents per quarter.
- Number of high-materiality use cases that depend on a single AI provider.
- Number of high-materiality use cases currently outside their performance thresholds.

**Three lines of defence mapping (illustrative, fn 19)**

| Line | Typical AI role |
|---|---|
| 1st: builders and users | Develop, assess use-case risk, apply human oversight |
| 2nd: Risk and Compliance | Independent challenge and validation, regulatory compliance |
| 3rd: Internal Audit | Independent assurance on the AI risk framework |

**Watch-outs:** a board that "noted" an AI paper has not necessarily met ¶3.4. Keep minutes that show challenge, approval of the framework and appetite, and a training record for directors.

---

## Recipe 3: Find all your AI (identification)

**Use when:** you cannot rate or control what you have not found.
**Refs:** ¶4.2–4.4, fn 21–22.

**Steps**

1. **Write a one-page AI definition** aligned with ¶1.3 and fn 6, with examples and non-examples from your stack (e.g., "rules engine: not AI; ML risk score: AI; vendor chat assistant: AI").
2. **Designate a control function** to own identification. It should oversee consistency, find new AI over time, and be the **final arbiter** of whether something is AI (¶4.3). Business units may do the actual identifying.
3. **Run a discovery sweep** across:
   - internally built models and systems;
   - vendor products with embedded AI features, including SaaS that is "not sold as AI" but contains it (fn 21). At minimum this covers material third-party service providers (¶4.2);
   - shadow AI (staff using public tools).
4. **Add triggers:** procurement intake, architecture review, vendor release notes and change requests should all ask "does this add AI?"
5. **Document outcomes** and review the process regularly as new AI techniques and vendor features appear (¶4.3).
6. **Handle what you cannot see.** Where you cannot identify everything (poor vendor disclosure, shadow AI), identify the resulting risk and mitigate: clear staff guidance on allowed and disallowed uses, and technical controls such as network monitoring and data loss prevention (fn 22). Keep residual risk from unidentified AI within appetite (¶4.4).

**Payments sources worth sweeping:** fraud and risk vendors, KYC and liveness providers, sanctions and adverse-media screening, customer-support platforms, CRM and email tools, developer tools and code assistants, BI tools with "ask your data" features, and card-scheme or processor tools that add ML features.

---

## Recipe 4: Build the AI inventory

**Use when:** you need a single source of truth that supports oversight, materiality rating and monitoring.
**Refs:** ¶4.5–4.9, fn 23–25.

**Steps**

1. Decide whether to **extend an existing inventory** (model, application, vendor) or create a dedicated AI inventory. Either is acceptable, but link it to other inventories such as data assets and the third-party or outsourcing register using consistent IDs (¶4.6, fn 23).
2. Capture attributes at a useful level of detail (¶4.7). Start from the list below.
3. Add **agent-specific attributes** where relevant: agent identifier, tools and systems it can access, components, guardrails (fn 25).
4. Set an **update frequency** and triggers for new, changed and retired items (¶4.5).
5. Have the control function keep independent oversight of accuracy and completeness (¶4.9). Review the inventory design itself as technology changes (¶4.8).

**Starter schema (suggested; MAS lists example attributes in ¶4.7)**

```yaml
use_case_id: UC-0042
name: "Card transaction fraud scoring"
purpose: "Score card-not-present transactions in real time"
business_owner: "Head of Risk Operations"
model_owner: "Data Science Lead"
approved_scope: "SG and PH cardholders; CNP only"      # approved scope of use, e.g. jurisdiction
model_type: "Gradient-boosted trees (in-house)"
third_party_ai: false
vendor_id: null                                        # links to outsourcing/third-party register
data_used: ["DA-017 transaction history", "DA-022 device signals"]   # links to data inventory
data_sensitivity: "Restricted"
dependencies: ["UC-0051 device reputation vendor model"]
lifecycle_status: "In production"
risk_materiality: {inherent: "High", residual: "Medium", approved_by: "AI control function", date: "2027-03-31"}
model_review_status: "Independently validated 2027-02-10; next due 2028-02"
human_oversight: "Analyst review for scores in referral band"
kill_switch_or_fallback: "Rules-only fallback; tested 2027-05-02"
agent_attributes: null
documentation_links: ["wiki://uc-0042/design", "wiki://uc-0042/validation"]
```

**Watch-outs:** an inventory that lists *tools* but not *use cases* will not support materiality rating. A spreadsheet with no owner and no update trigger goes stale in a quarter.

---

## Recipe 5: Rate risk materiality

**Use when:** you need to decide how much control each use case gets.
**Refs:** ¶4.10–4.13, fn 26. **[Sign-off]**

**What MAS requires**

- A consistent methodology applied to **every** AI use case (¶4.10).
- Assess both **inherent** risk (before controls) and **residual** risk (after controls). Residual risk must meet appetite *before deployment* (¶4.11).
- Cover at least three dimensions (¶4.12):
  - **Impact:** consequence of failure on the firm (financial, operational, regulatory, reputational) and on customers and others (fairness, ethics, consumer protection), including the sensitivity of the data processed.
  - **Complexity:** the technology, novelty of the application, the data, explainability, and for third-party AI how much visibility you have.
  - **Reliance:** how much you depend on the AI for the decision, how much autonomy it has, and how much human involvement there is.
- Consider dependencies between AI systems that feed the use case (fn 26).
- A designated control function sets the framework and **arbitrates or approves** each rating (¶4.13).

**Starter scoring (our suggestion, not MAS-prescribed; Risk should calibrate)**

Score each dimension 1 (low) to 3 (high). Sum to 3–9.

| Total | Suggested tier |
|---|---|
| 3–4 | Low |
| 5–6 | Medium |
| 7–9 | High |

Add **overrides** your Risk team agrees, for example: any use case that makes or drives decisions on customer funds, account access, credit or regulatory reporting is at least Medium, and High if reliance is 3. Add a rule that unexplained third-party AI cannot score below 2 on complexity.

**Illustrative examples (for discussion only; not decisions)**

| Use case | Impact | Complexity | Reliance | Illustrative tier | Notes |
|---|---|---|---|---|---|
| Internal chatbot to find policies | 1 | 2 | 1 | Basic or Low | ¶2.4(f) example |
| Meeting-note summariser, human-checked | 1 | 2 | 1 | Basic or Low | ¶2.4(b) example |
| LLM drafts chargeback or dispute response, analyst reviews and submits | 2 | 2 | 2 | Medium | Reliance rises sharply if it submits without review |
| Customer-facing generative chatbot | 2 | 3 | 2 | Medium to High | Incorrect or offensive answers are a named reputational risk (¶1.9(e)) |
| ML card fraud score that auto-declines | 3 | 2 | 3 | High | Customer and revenue impact, high reliance |
| AI agent that ranks and closes AML alerts | 3 | 3 | 2–3 | High | Financial crime risk (¶1.9(d)); agent autonomy (¶1.11) |
| Vendor ML for ID document and liveness checks | 3 | 2 | 3 | High | Third-party visibility limits (¶4.12(b), ¶5.11) |

> Any decision on KYC outcomes, fraud outcomes, credit, refunds, chargebacks or risk acceptance is made by accountable people under your policies. The AI and this table support those people. They do not replace them.

**Watch-outs:** rate the use case as actually deployed, not as the vendor describes it. Re-rate on scope, data, autonomy or vendor changes (¶4.11 asks for regular review of methodology and assessments).

---

## Recipe 6: Match controls to tier (the control matrix)

**Use when:** you need to turn the rating into a work plan.
**Refs:** ¶5.1–5.3, ¶2.2(b).

MAS expects robust controls across the whole life cycle, with clear roles, reviewed regularly (¶5.1). Controls may be proportionate to materiality (¶5.2). Some controls are mainly relevant to certain use cases. For example, transparency, explainability and fairness matter most in credit scoring, underwriting, advice and fund management (fn 12).

**Where the Guidelines name a tier-specific expectation, it is shown. Other cells are our suggestions.**

| Control area | Ref | Low | Medium | High |
|---|---|---|---|---|
| Data management | ¶5.4 | Classification, access, privacy basics (fn 12 says still applies) | Plus quality and lineage checks | Plus representativeness incl. stressed conditions, drift checks, full lineage |
| Transparency and explainability | ¶5.5–5.6 | Staff know it is AI | Key drivers visible to users | Customer notice, drivers, consequences, redress channel |
| Fairness | ¶5.7–5.8 | Not usually needed | Screen if customers are affected | Defined fairness criteria, metrics, documented mitigation |
| Human oversight | ¶5.9 | Output check by user | Defined review points | Designed-in escalation, authority to intervene, near-miss review |
| Third-party AI | ¶5.10–5.11 | Approved-tool list | Contract and testing proportionate | Own-data testing, compensating tests, exit and contingency plans |
| Selection | ¶5.12–5.13 | Light note | Documented rationale | Documented justification vs simpler alternatives |
| Evaluation and testing | ¶5.14–5.15 | Basic functional tests | Thresholds and out-of-sample tests | Stress, edge-case, adversarial and sub-population testing |
| Tech and cyber | ¶5.16, ¶5.22 | Baseline | Plus security review | Pen test, red teaming, adversarial tests |
| Reproducibility and auditability | ¶5.17 | Basic notes | Design and test records | Full replicable documentation |
| Pre-deployment review | ¶5.18–5.21 | Peer review | Peer review by uninvolved person | **Formal independent validation** (¶5.19) |
| Monitoring and re-validation | ¶5.23–5.24 | Periodic check | Defined metrics and thresholds | Tiered thresholds, drift checks, **regular independent re-validation** (¶5.24) |
| Change management | ¶5.25 | Change log | Review significant changes | Re-approval for significant changes, rollback ability |
| Contingency | ¶5.3 | n/a | Manual fallback noted | **Contingency plans, regularly reviewed and tested** (¶5.3) |
| Kill switch or override | ¶5.23(b) | n/a | Consider | **Consider** for high-materiality AI |

**Partial deployments, pilots and phased rollouts (fn 28).** MAS recognises these may need adjusted controls. Set a written policy for deviations: time and user limits, success criteria, terms of use for owners and users, close monitoring for anomalies, and a check that use stays within the limited scope.

Recipes 7–13 give the detail for each control family.

---

## Recipe 7: Data you can defend

**Refs:** ¶5.4(a)–(g), fn 30. **[Sign-off]** for personal data.

Run each AI use case through seven checks:

| Check | Question to answer | Evidence to keep |
|---|---|---|
| Fit for purpose | Is this data suitable for the objective, and does using it raise fairness issues? | Data selection note |
| Representativeness | Does training and test data cover real conditions, including stressed ones? | Coverage analysis by market, product, segment, period |
| Quality | Is it relevant, accurate, complete and recent, with monitoring for anomalies, drift and bias? | Data quality dashboard |
| Classification | Is the data's sensitivity known and used to limit what the AI can see? | Classification tags |
| Security | Encrypted in transit and at rest, inputs and outputs protected, and training data, model artefacts and outputs destroyed or sanitised when no longer needed? | Retention and destruction records |
| Privacy | Is there a legal basis, such as consent where required, for using customers' or employees' sensitive personal data to train or run the AI? | Privacy assessment (see PDPC advisory guidelines referenced in fn 30) |
| Lineage and auditability | Can you show sourcing, processing, fit-for-purpose assessment, approvals and fixes? | Lineage records |

**Payments-specific tips**

- **Never put full card numbers, CVV, PIN or chip/stripe data into prompts, training sets, logs or test fixtures.** Mask or tokenise before data reaches any AI component. If your card data environment is in scope for PCI DSS, involve your security and PCI owners early.
- Use anonymised or synthetic data for development and demos wherever possible.
- Fraud and AML labels are often biased by past investigator behaviour (what was investigated is what got labelled). Document this limitation in the fit-for-purpose and representativeness checks.
- **Tension to resolve with Compliance:** ¶5.23(d) suggests logging prompts and model responses for generative AI and agents, while data-privacy and card-data rules push you to minimise what you store. A workable approach is to log with masking or redaction, restrict access, set retention limits, and document the decision. **[Sign-off]**

---

## Recipe 8: Transparency, explainability and fairness

**Refs:** ¶5.5–5.8, fn 31–36. **[Sign-off]** for customer-facing disclosures.

**Transparency and explainability**

1. Set the level by use case and materiality (¶5.6). Higher for credit and other regulated decisions with high customer impact; lower for internal low-risk assistants.
2. For higher-level use cases, plan for: justification of the input features used, the ability for users to identify **key drivers** of an output, telling customers AI is used, explaining the consequences of AI-driven decisions, and a **channel for redress**.
3. Tailor to the audience (fn 34): customers need plain language on how AI affects them, the basis for the decision and where to ask or complain. Model validators need technical behaviour and limitations.
4. For generative AI chatbots, MAS points to IMDA's transparency guidelines as a reference (fn 34).

**Fairness**

1. **Define what "fair" means** for your firm (¶5.7). FEAT is a named reference (fn 35).
2. Where relevant, run a fairness assessment (¶5.8): define protected attributes, include proxies or highly correlated attributes (fn 36), measure with suitable fairness metrics, and document results and mitigation.
3. Give more attention where AI could lead to unfair access to or denial of financial services (¶5.7).

**Payments-specific tips**

- Account opening, KYC verification, transaction declines and account restrictions all affect access to services. Test whether decline, false-positive and escalation rates differ materially across customer groups, markets, document types or devices, and record the findings.
- If an AI-supported decision leads to an adverse customer outcome, make sure a human can explain it and the customer has a route to challenge it. Build this into the process before launch, not after the first complaint.

---

## Recipe 9: Human oversight that actually works

**Refs:** ¶5.9(a)–(d), fn 37.

**Steps**

1. **Decide the oversight mode** by risk: human-in-the-loop (human approves each output) or human-over-the-loop (human monitors and can intervene). MAS covers all forms where you decided human involvement is needed (fn 37).
2. **Assign roles**: who reviews, who escalates, who decides (¶5.9(a)).
3. **Equip the reviewers** with competence, authority and the practical ability to intervene (¶5.9(b)).
4. **Design for oversight from the start**: build escalation triggers when pre-defined conditions on reliability or accuracy are met (¶5.9(c)).
5. **Record and review**: keep logs, review human decisions and interventions, including incidents and near misses, to test whether oversight is working (¶5.9(d)).
6. **Plan for automation bias and decision fatigue** as AI speed and volume grow (¶5.9).

**Practical indicators (our suggestion)**

- Reviewer agreement rate with AI recommendations. A rate near 100% over long periods can mean rubber-stamping.
- Time per review versus a baseline.
- Override rate and the reasons for overrides.
- Queue size and backlog trends (fatigue signal).
- Share of AI outputs sampled by an independent second reviewer.

**Watch-out:** in AML and fraud operations, analysts who face hundreds of AI-ranked alerts per day may stop challenging the ranking. Rotate samples, seed known-answer test cases, and report oversight quality to the committee.

---

## Recipe 10: Third-party and vendor AI

**Refs:** ¶5.10–5.11, ¶4.2, fn 38–40. **[Sign-off]** (outsourcing and third-party risk)

MAS expects its outsourcing and third-party service expectations to apply to third-party AI too (fn 39). You keep primary accountability (¶5.11).

**Steps**

1. **Onboarding controls scaled to materiality**, including controls for any fine-tuning or modification you make (¶5.10, fn 38).
2. **Contracts** that give risk-appropriate visibility into when AI is introduced and when it changes (¶5.10). Consider clauses on performance guarantees, data protection, right to audit, notification of AI introduction or updates, and your agreement before AI is added (¶5.11(f)).
3. **Test in your context**, using your own data where feasible, and do compensatory testing where the vendor discloses too little. Keep documentation of how you tested and why you judged it suitable (¶5.10).
4. **Work through the eight considerations in ¶5.11(a)–(h)**:

| Area | Ask |
|---|---|
| Transparency | Does vendor documentation let us judge their controls on data, model, security, fairness, explainability? Are there independent certifications or assessments (not self-attestation)? |
| Supply chain | Have key third-party and open-source models, datasets and dependencies been assessed for provenance, training data integrity and known vulnerabilities? |
| Concentration | Are we over-reliant on a few providers, directly or indirectly? |
| Change management | Will we be told about updates, and can we assess their impact? |
| Contingency | What is the fallback if it fails, behaves unexpectedly or support ends? |
| Legal | Are expectations and responsibilities clear in the agreement? |
| Capabilities | Do our procurement, development and user teams understand it? |
| Complexity | Is this new to us, such as third-party AI agents, so that we need deeper evaluation and security checks? (fn 40) |

5. **If residual risk cannot be brought within appetite**, consider limiting or suspending the service, or replacing the provider (¶5.11).

**Payments-specific tips**

- Ask KYC, fraud and screening vendors directly: which features use ML or generative AI, which model versions are live, how and when models are retrained, and whether customer data is used to train shared models.
- Treat silent model updates by a vendor as a change-management event, even if you did not release anything.
- Quantify concentration: count high-materiality use cases that rely on one AI or LLM provider (a metric MAS gives as an example in fn 18) and test your exit plan.

---

## Recipe 11: Select, evaluate, test and review before go-live

**Refs:** ¶5.12–5.22, fn 41–48.

**Select (¶5.12–5.13)**

1. Write down the objective and risks of the use case.
2. Compare options, including **simpler or conventional alternatives**, and document why more complex models or less understood features were chosen. Balance performance against complexity, fairness, transparency and explainability.
3. Where you pick newer, less understood AI, weigh the benefits against new or heightened risks such as hallucination, opacity and security, and against your ability to mitigate them (¶5.13).
4. Involve domain experts or business users in selection (¶5.12).

**Evaluate and test (¶5.14–5.15)**

1. Identify key risks and set **clear, measurable thresholds**, agreed by business owners, developers and reviewers (¶5.14(a)).
2. Test across plausible conditions, from typical to edge cases, using data representative of your context. Methods MAS lists include out-of-sample or out-of-time testing, sensitivity and stability analysis, sub-population analysis, stress testing (including edge cases and adversarial testing where appropriate), error analysis and benchmarking against alternatives (¶5.14(b)).
3. Mitigate overfitting where possible, such as by favouring simpler models unless complexity is justified (¶5.14(c)).
4. Put controls and guardrails in place for limitations found *before* deployment (¶5.15).
5. For generative AI and agents, test **key failure modes** and whether guardrails work: hallucination, toxic or biased content, data leakage, and vulnerability to adversarial attack (¶5.15, fn 46). IMDA's Starter Kit is a named reference (fn 43).

**Document for replay (¶5.17):** data sources and quality checks, selection rationale, training procedures (code versions, environments, hyperparameters), evaluation measures and results, explainability and fairness work, and assumptions, limitations and mitigants. An independent person should be able to understand and potentially replicate your work.

**Review before deployment (¶5.18–5.22)**

| Tier | Review type | Ref |
|---|---|---|
| High | **Formal independent validation** by competent people independent of development and deployment. It should cover: conceptual soundness, data suitability and quality, implementation integrity, evaluation and test results, explainability and fairness, assumptions and limits. It should give effective challenge. | ¶5.19 |
| Other | Documented review, such as peer review by qualified people not involved in development or deployment | ¶5.20 |
| All | Findings, limitations, remediation and conditions of use go to the approval body, which must see that recommendations are actioned | ¶5.21 |
| All | Technology and cyber review: secure design and least-privilege access, deployment checklists (encryption, DLP, firewalls, access restrictions, logging), vulnerability assessment, penetration testing, red teaming, adversarial tests with safeguards such as input validation, throttling and anomaly detection | ¶5.22 |

---

## Recipe 12: Run it, watch it, change it, retire it

**Refs:** ¶5.3, ¶5.16, ¶5.23–5.26.

**Monitoring (¶5.23)**

1. Define key metrics and acceptable thresholds from the use case risks: robustness, stability, data quality, fairness and others. Use **tiered thresholds**, with early-warning levels that trigger action before a breach.
2. Monitor for **data drift** (input distributions change), **concept drift** (input-output relationships change) and overall model drift.
3. For generative AI and agents, also monitor, where relevant, the information flow and decision paths: reasoning, actions taken, tools used (¶5.23(a)). Consider logging prompts, responses, model versions and reasoning (¶5.23(d)), subject to the data-handling point in Recipe 7.
4. Run an **AI incident process**: report, track, escalate, resolve. Fixes may include retraining, adjustment, redevelopment or decommissioning. For high-materiality AI consider kill switches or override mechanisms (¶5.23(b)). Give users a way to report issues.
5. Name an **accountable person**, keep records, strictly control and log access to models, training data, pipelines and configuration, and train monitors and users (¶5.23(c)–(e)).

**Re-validation (¶5.24):** frequency and depth follow materiality. High-materiality use cases need **regular independent re-validation**. Triggers include: issues on connected systems, monitoring alerts or breaches, significant changes to the AI or environment, and new external risks such as regulatory or technology developments.

**Contingency (¶5.3):** for high-risk use cases, have fallbacks such as alternative systems or manual processes, review and test them across a range of conditions, and test kill-switch activation protocols regularly.

**Change management (¶5.25)**

- Define what counts as a **significant change** (changes to training data, architecture, key assumptions, scope of use, or downstream impact, per fn 49). Significant changes trigger review and re-approval before implementation. Where significant changes can occur without prior review for high-materiality use cases, apply compensating controls such as enhanced monitoring.
- Use change control with human oversight and version control for code, data, parameters and hyperparameters, with traceability and rollback.
- For AI that **updates automatically**, require strict justification, define exactly what may update automatically (for example retraining or hyperparameter changes, but not core architecture changes), and add stronger data quality checks and monitoring.

**Retirement (¶5.26):** plan decommissioning, covering dependencies, data retention, secure removal and stakeholder notification.

**Security baseline (¶5.16):** secured environments, hardened configuration, network segmentation, input validation, API authentication, encryption, DLP, role-based access with multi-factor authentication, privileged access management, separation of duties (for example different teams training and testing), and controls on third-party plugins and APIs. MAS points to its technology risk management guidelines (fn 47).

---

## Recipe 13: AI agents (the special case)

**Refs:** ¶1.11, ¶4.12(c), fn 11, fn 25, fn 40, ¶5.15, ¶5.23.

MAS names agents among the technologies the Guidelines cover (¶1.5). The risk it highlights is an agent with tool access taking unauthorised or wrong actions because its goals were translated into actions in an unexpected way, or a compromised agent being used to exfiltrate data or run malicious commands at scale (¶1.11).

**Controls that follow from the text**

| Concern | Control to put in place | Ref |
|---|---|---|
| Autonomy | Rate **reliance** explicitly: how much autonomy, how much human involvement | ¶4.12(c) |
| Tool access | Record the tools and systems each agent can reach in the inventory. Apply least privilege and separate agent identities. | fn 25, ¶5.22(a) |
| Guardrails | Define and test them, including whether they work in key failure modes | ¶5.15 |
| Human control | Approval gates for actions that move funds, change customer status or send regulatory filings. Escalation on pre-defined conditions. | ¶5.9(c) |
| Visibility | Log reasoning steps, tool calls and actions | ¶5.23(a), (d) |
| Containment | Kill switch or override and tested contingency activation for high-materiality agents | ¶5.3, ¶5.23(b) |
| Third-party agents | Deeper evaluation and security checks if you have little experience | fn 40 |
| Reference | IMDA's Model AI Governance Framework for Agentic AI | fn 11 |

---

## Recipe 14: Capability, capacity and infrastructure

**Refs:** ¶6.1–6.3.

1. Define the competence and conduct expected of people who develop, deploy and use AI. Recruit and train for it (¶6.1).
2. Resource the work in proportion to risk: people, technology and budget (¶6.1, ¶3.5(g)).
3. Review regularly whether staff capability and capacity still fit, and refresh training for new AI risks (¶6.2).
4. Check infrastructure: compute, network, memory and secure data pipelines sufficient for performance, scalability and resilience, with technology risk guidelines and recognised frameworks such as NIST AI RMF in mind (¶6.3, fn 50–51).
5. Train the board (¶3.4(d)).

**Suggested training tracks:** all staff (acceptable use, data rules, reporting); builders and buyers (testing, fairness, third-party AI); reviewers and analysts (automation bias, challenge techniques); control functions (materiality, validation); directors and executives (oversight, appetite).

---

## Use-case playbooks for payments and fintech

> Illustrative starting points for discussion. Final materiality ratings and control decisions belong to your control function, Compliance and Risk. **[Sign-off]**

### Real-time fraud scoring

- **Why it matters:** high impact (customer experience, losses) and high reliance when it auto-declines. Fraud patterns shift, so drift is a core risk (¶5.23).
- **Do:** set thresholds for loss, false-positive and approval rates; use tiered early warnings; keep a tested rules-only fallback (¶5.3); sub-population analysis for decline-rate differences (¶5.14(b), ¶5.8); independent validation and regular re-validation (¶5.19, ¶5.24).
- **Avoid:** retraining automatically without the dynamic-update controls in ¶5.25(c).

### AML and fraud alert triage

- **Why it matters:** MAS explicitly names AI uncertainty causing undetected suspicious transactions as a financial crime risk (¶1.9(d)).
- **Do:** keep humans accountable for disposition decisions; design escalation triggers (¶5.9(c)); track analyst agreement and override rates (Recipe 9); seed known-positive cases to check the AI does not suppress them; log AI recommendations and human actions for audit; define what the agent may and may not do (Recipe 13).
- **Avoid:** letting AI close alerts without an approved, tested and documented policy and the right sign-off. **[Sign-off]**

### KYC, KYB and identity verification

- **Why it matters:** often third-party AI with limited visibility (¶4.12(b)); affects access to services (¶5.7).
- **Do:** contractual visibility on model changes (¶5.10); test on your own population and document types (¶5.10); fairness checks across groups and document types (¶5.8); fallback manual review path; redress channel for rejected customers (¶5.6).
- **Avoid:** accepting vendor self-attestation as your only evidence (¶5.11(a) points to independent assessments). Vendor ML must not become the unreviewed final decision on KYC outcomes. **[Sign-off]**

### Chargeback and dispute document drafting (generative AI)

- **Why it matters:** facts and figures in documents sent to schemes, issuers or customers must be right. Hallucination is a named risk (¶5.13, ¶5.15).
- **Do:** require human review before any submission (¶2.4 footnote 13 logic, ¶5.9); ground outputs in system-of-record data; test for fabricated facts and wrong amounts or dates (¶5.15, fn 46); keep prompt and output logs with masked card data (Recipe 7).
- **Avoid:** feeding full card numbers into prompts, or moving from "assistive drafting" to "auto-submission" without re-rating (¶4.11, ¶5.25(a)).

### Customer-facing chatbot

- **Why it matters:** reputational and conduct risk if answers are wrong or offensive (¶1.9(c), (e)). MAS reminds FIs that Fair Dealing expectations still apply when AI delivers services (fn 15).
- **Do:** disclose that customers are talking to AI (¶5.6); red-team for prompt injection and data leakage (¶5.22(b)); clear handoff to humans; monitoring of complaints and unsafe outputs; IMDA's chatbot transparency guidance (fn 34) and testing starter kit (fn 43) as references.
- **Avoid:** giving the bot access to tools that change account state without approval gates.

### Internal copilots and code assistants

- **Why it matters:** often "basic" tier (¶2.4), but shadow AI and data leakage are real risks (¶1.10(b), (f)).
- **Do:** approved-tool list, acceptable-use policy with a ban on confidential or client data in public tools (¶2.5(b)–(c)); DLP; staff training.
- **Avoid:** assuming "basic" means "no controls". Data and security controls still apply (fn 12).

---

## Implementation roadmap

A suggested pacing for a firm planning to be ready for Sections 3–4 by 7 October 2027 and Sections 5–6 by 7 October 2028. Adjust to your size and risk profile. MAS expects proportionality (¶2.1).

| Phase | Window (suggested) | Deliver |
|---|---|---|
| 0. Mobilise | Q4 2026 | Executive owner named; control function(s) designated; gap assessment against Sections 3–6; basic-tier policy issued (Recipe 1) |
| 1. Discover | Q1 2027 | AI definition; discovery sweep; inventory v1 (Recipes 3–4) |
| 2. Rate | Q2 2027 | Materiality methodology approved; all inventory items rated; high-materiality list agreed (Recipe 5) |
| 3. Govern | Q2–Q3 2027 | Board and committee structures; AI risk appetite approved; escalation and incident process; board training (Recipe 2) |
| 4. Dry run | Q3 2027 | Rehearse the oversight cycle; internal audit pre-read; fix gaps |
| **Milestone** | **7 Oct 2027** | **Sections 3–4 expectations in place** |
| 5. Build controls | Q4 2027 to Q2 2028 | Control library by tier; third-party contract uplift; validation function; monitoring standards; logging approach (Recipes 6–13) |
| 6. Prove | Q2 to Q3 2028 | Validate and re-validate high-materiality use cases; test contingency and kill-switch plans; capability programme (Recipe 14) |
| **Milestone** | **7 Oct 2028** | **Sections 5–6 expectations in place** |

---

## Common mistakes

1. **Inventory of tools, not use cases.** You cannot rate what you have not described.
2. **Treating vendor AI as the vendor's problem.** You retain primary accountability (¶5.11).
3. **One-time materiality rating.** Scope, data, autonomy and vendor changes require re-rating (¶4.11, ¶5.25).
4. **Validation by the builders.** High-materiality use cases need independence (¶5.19).
5. **"Human in the loop" that is a rubber stamp.** MAS names automation bias and decision fatigue (¶5.9).
6. **Skipping the simpler alternative.** MAS expects documented justification when choosing complex models over simpler ones (¶5.12).
7. **No tested fallback.** A fallback never tested is a hope, not a plan (¶5.3).
8. **Logging everything.** Prompt logs can capture personal or card data. Mask first.
9. **Assuming group policy is enough.** Local management must show MAS how it oversees Singapore (¶3.6).
10. **Ignoring other regulators.** This post covers MAS only. If you operate in the Philippines, Indonesia or other markets, local rules need their own review.

---

## Self-assessment checklist

Use as a conversation starter with Compliance and Risk. Answering "yes" to all of these is **not** a statement that you meet MAS expectations.

**Oversight (Section 3)**
- ☐ Board or delegated committee has approved the AI governance approach (¶3.4(a))
- ☐ AI risk is in the risk appetite framework with qualitative and, where suitable, quantitative measures (¶3.4(b))
- ☐ Roles for board, senior management and control functions are written down (¶3.4(c), ¶3.5(d))
- ☐ There is an AI incident and breach escalation process, and the board gets timely updates (¶3.5(e)–(f))
- ☐ Directors have had AI training (¶3.4(d))
- ☐ Local management can show how it oversees Singapore operations if using group frameworks (¶3.6)

**Identification, inventory, materiality (Section 4)**
- ☐ AI definition and criteria published; control function is final arbiter (¶4.2–4.3)
- ☐ Embedded third-party AI in material providers is covered (¶4.2)
- ☐ Residual risk from unidentified AI and shadow AI is assessed and mitigated (¶4.4)
- ☐ Inventory exists, is linked to data and third-party registers, and has an update process (¶4.5–4.9)
- ☐ Every use case has an inherent and a residual risk rating, approved by the control function (¶4.11–4.13)
- ☐ Ratings cover impact, complexity and reliance (¶4.12)

**Life cycle (Section 5)**
- ☐ Control matrix by tier (¶5.2)
- ☐ Data checks cover all seven areas (¶5.4)
- ☐ Transparency, explainability and fairness approach set for customer-affecting use cases (¶5.5–5.8)
- ☐ Human oversight designed, resourced and reviewed (¶5.9)
- ☐ Third-party AI: contracts, own-context testing, concentration and exit plans (¶5.10–5.11)
- ☐ Selection rationale documented, including simpler alternatives (¶5.12)
- ☐ Thresholds, testing and guardrail tests defined (¶5.14–5.15)
- ☐ Security controls, penetration testing and red teaming done (¶5.16, ¶5.22)
- ☐ Development process documented for replay (¶5.17)
- ☐ Independent validation for high-materiality use cases (¶5.19)
- ☐ Monitoring with tiered thresholds and drift checks; incident process live (¶5.23)
- ☐ Re-validation schedule and triggers set (¶5.24)
- ☐ Change control, dynamic-update rules and decommissioning process in place (¶5.25–5.26)
- ☐ Contingency plans and kill-switch protocols tested for high-materiality use cases (¶5.3)

**Capability (Section 6)**
- ☐ Competence expectations, training and resources defined and reviewed (¶6.1–6.2)
- ☐ Infrastructure is adequate for AI workloads (¶6.3)

---

## Open questions for Compliance and Risk

These are points where the Guidelines leave judgement to the firm or where we could not confirm the answer from the document alone.

1. **Applicability.** The Guidelines apply to FIs as defined in the Financial Services and Markets Act 2022 (fn 1). Confirm how this applies to your licence category and group structure, and whether the group-basis wording in ¶1.2 reaches you.
2. **Transition.** Confirm the reading of ¶1.8 on phased dates and whether MAS has issued any further guidance, FAQs or supervisory communication.
3. **"Learned" thresholds in rules engines.** Where a rule set uses thresholds tuned from data, is it AI under ¶1.3 and fn 6? The control function should decide and document.
4. **Prompt logging versus data minimisation.** Agree a standard for redaction, retention and access (Recipe 7).
5. **Cross-border use cases.** Where one model serves several markets, how will you reconcile MAS expectations with other regulators' requirements?
6. **Outsourcing overlap.** Which third-party AI services also fall under your outsourcing or third-party risk requirements (fn 39), and who owns the combined assessment?

---

## Sources, method and limits

- **Primary source:** Monetary Authority of Singapore, *Guidelines on Artificial Intelligence Risk Management*, 7 October 2026. This cookbook was prepared from the copy of the Guidelines supplied to the author. We did not cross-check it against the MAS website, later notices or FAQs.
- **Documents the Guidelines refer to (not reviewed for this post):**
  - [MAS FEAT Principles (2018)](https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat)
  - [MAS Guidelines on Risk Management Practices for Technology Risk](https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines)
  - [MAS Information Paper on Cyber Risks Associated with Generative AI](https://www.mas.gov.sg/regulation/circulars/cyber-risks-associated-with-generative-artificial-intelligence)
  - [IMDA Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)
  - [IMDA Starter Kit for Testing LLM-Based Applications](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/large-language-model-starter-kit.pdf)
  - NIST AI Risk Management Framework ([NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1))
  - PDPC Advisory Guidelines on the use of personal data in AI recommendation and decision systems, and in generative AI (see fn 30 of the Guidelines)
- **What is MAS text and what is ours:** paragraph references (¶) point to what MAS says. Scoring scales, tier tables, control-matrix cells marked as suggestions, schemas, indicators, playbooks and the roadmap are the author's and Claude's suggestions, not MAS requirements.
- **Confidence:** high on the content of the Guidelines as supplied; medium on payments-specific mappings; applicability to any specific firm is unconfirmed.
- **Review status:** draft. Not yet reviewed by Compliance or Risk.

*Disclosure: this post was drafted by Claude, an AI system built by Anthropic, at the author's direction. Because it is an AI system writing about AI governance, readers should weigh that potential conflict of interest and rely on the MAS source document for what the Guidelines require.*
