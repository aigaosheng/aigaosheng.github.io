---
layout: post
title: "When Even the Smartest AI Falters — 200 Finance Experts Put GPT-5 Gemini 2.5 Pro and Claude Sonnet 4.5 to the Test"
description: "The Scope — From Wall Street to Excel Sheets · Where Things Went Wrong — The Six Recurring Failure Patterns · Real Examples — What Went Wrong in Practice…"
date: 2025-12-01 18:40:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Large Language Models
keywords: [AI finance, LLM risk, model evaluation]
permalink: /When Even the Smartest AI Falters — 200 Finance Experts Put GPT-5 Gemini 2.5 Pro and Claude Sonnet 4.5 to the Test/
---
**When Even the Smartest AI Falters — 200 Finance Experts Put GPT-5, Gemini 2.5 Pro, and Claude Sonnet 4.5 to the Test**

In a sobering reality check for AI enthusiasts, a recent evaluation by Surge AI reveals that leading large-language models (LLMs) — GPT-5, Gemini 2.5 Pro, and Claude Sonnet 4.5 — stumble when confronted with real-world financial tasks. Across **200+ finance scenarios** designed by veterans from trading, investment banking, and risk management, these models failed **70% of the time** in producing output that meets professional standards. ([Surge AI][1])

---

## 📊 The Scope — From Wall Street to Excel Sheets

Surge AI’s finance-savvy panel crafted scenarios spanning seven subdomains of finance — from regulatory capital calculations, to commodities trading, forecasting spreadsheets, and even automated slide-deck generation in PowerPoint. ([Surge AI][1]) The intention was to test not just theoretical knowledge, but real workflows: tasks that analysts and bankers deal with daily.

In direct comparison, the models ranked as follows: GPT-5 outperformed the others in 47% of tasks, followed by Sonnet 4.5 at 26% and Gemini 2.5 Pro at 24%. ([Surge AI][1])

On head-to-head showdowns:

* GPT-5 beat Sonnet 4.5 handily (59% vs 36%)
* GPT-5 edged out Gemini (62% vs 35%)
* Sonnet 4.5 slightly surpassed Gemini (52% vs 41%) ([Surge AI][1])

Yet — and this is the punch — even GPT-5’s best efforts were rated “mediocre to bad” in over 70% of cases. ([Surge AI][1])

---

## 🔍 Where Things Went Wrong — The Six Recurring Failure Patterns

The Surge AI evaluation singled out **six consistent failure modes**, illustrating why front-rank AIs still struggle with professional-grade finance tasks. ([Surge AI][1])

1. **Theory vs Reality** — Models often applied formulas correctly but ignored real-world constraints like regulatory limits, market liquidity, or trading caps. In one Basel-capital calculation, all models oversimplified risk netting, violating real compliance boundaries. ([Surge AI][1])
2. **Fragile Multi-Step Workflows** — When tasks required chained reasoning or multiple dependent steps, the models lost coherence or dropped the ball entirely. ([Surge AI][1])
3. **Weak Domain Calibration** — Many outputs looked numerically plausible but made glaringly unrealistic assumptions: e.g. losses too similar across diverse portfolios, or hedging strategies ignoring instrument liquidity. ([Surge AI][1])
4. **File Handling & Output Fidelity** — Spreadsheet and slide-deck tasks exposed severe flaws: from misreading uploads to corrupt formulas and unusable downloads. ([Surge AI][1])
5. **Skipping Industry Conventions** — The models often ignored unstated professional norms: sign conventions, mark-to-market rules, templating consistency — leading to technically “correct” yet professionally unusable outputs. ([Surge AI][1])
6. **Framework Misalignment** — Sometimes the wrong methodology was chosen altogether: e.g. mixing regulatory and internal-model approaches, or inventing new accounting tricks that don’t exist in practice. ([Surge AI][1])

---

## 🚨 Real Examples — What Went Wrong in Practice

### • PowerPoint Deck for a Market-Crash Stress Test

The task: analyze five multi-asset portfolios under historical market shocks (e.g. 2008, 2020) and create a final slide projecting an AI-driven crash — with mitigation strategies. ([Surge AI][1])

* **Gemini 2.5 Pro** never generated slides.
* **Claude Sonnet 4.5** created slides for stress scenarios but skipped the final “AI-crash + mitigation” slide and even misstated key numbers.
* **GPT-5** produced a full deck with correct exposure numbers and visuals — but *omitted risk-mitigation commentary*. In other words: almost useful, but missing the essential “so what” analysis that drives decisions. ([Surge AI][1])

### • Two-Year Financial Forecast in Excel

The task: extend a company’s operating forecast into the next fiscal year, fill in missing formulas, maintain formatting, and flag critical overdraft thresholds. ([Surge AI][1])

* **Gemini** failed to detect the uploaded workbook — then hallucinated a nonexistent “overdraft-interest” variable.
* **Sonnet 4.5** initially produced plausible results, but quickly corrupted formulas, skipped months, and broke formatting.
* **GPT-5** got the numeric forecasts right (when overdraft would exceed $600k, when it peaked), but stripped all formatting, mishandled percentage signs, and delivered a download file that needed manual cleanup. ([Surge AI][1])

### • Regulatory Capital (Basel) Optimization for a Credit-Derivatives Portfolio

Traders asked the models to compute required regulatory capital (under real regulatory frameworks) and propose legally compliant ways to reduce it without changing risk positions. ([Surge AI][1])

* **Gemini** superficially followed the Basel rulebook but missed key regulatory mechanics — producing dangerously understated capital requirements.
* **Sonnet 4.5** picked the wrong methodology (an internal-model approach rather than the standard regulatory approach), yielding incorrect capital results.
* **GPT-5** recognized the correct framework, but simplified aggressively — using wrong loss given default (LGD), omitting mark-to-market components, and applying offsetting incorrectly. In a real bank audit, those would be fatal flaws. ([Surge AI][1])

Surge AI notes bluntly: *“No model came close to generating a useful, profitable, and regulation-compliant recommendation.”* ([Surge AI][1])

---

## 📉 What This Means: AI Is Smart — But Not Street-Smart

The takeaway is jarring for anyone hoping to plug LLMs into financial workflows without oversight. These models handle academic-style problems just fine — but real finance tasks require domain judgment, institutional awareness, and rigorous process discipline.

Current benchmarks like FinQA or TAT-QA emphasize isolated reasoning or fact recall. They do not capture the messy entanglement of regulations, market behavior, formatting, and compliance that defines real-world finance. ([Surge AI][1])

As one Surger put it:

> “Overall, GPT would confuse financial analysts more than it would help them with this document.” ([Surge AI][1])

For AI to truly support — and not hinder — professional workflows, evaluation must shift from textbook-style tasks toward messy, real-world pipelines: Excel models, regulatory frameworks, multi-step deliverables, and full workflow fidelity. ([Surge AI][1])

---

## 🔑 Glossary

* **LLM (Large Language Model)**: A type of AI model trained on large corpora of text data to generate human-like language, answer questions, or perform reasoning tasks.
* **Basel Framework**: International banking regulations (set by the Basel Committee on Banking Supervision) governing how much capital banks must hold against their risk exposures.
* **Net Stressed Exposure (NSE)**: A risk metric estimating potential losses of a portfolio under stressed market conditions.
* **VaR (Value at Risk)**: A statistical technique to measure the risk of loss on a portfolio over a specific time frame under normal market conditions.
* **LGD (Loss Given Default)**: The amount of loss a lender incurs when a borrower defaults, expressed as a percentage of total exposure.

---

## 🧭 Why It Matters

For AI practitioners, finance professionals, and developers working at the intersection of ML and financial applications — including you, Sheng, given your ambition to build trading tools — this study is a crucial warning: **being able to run an LLM is not enough.** Real value only comes when those models are integrated into workflows with robust oversight, domain-specific calibration, and human-in-the-loop checks.

AI in finance could revolutionize efficiency — but only if we acknowledge and close the gap between “textbook AI” and “finance-grade AI”.

Source: [https://surgehq.ai/blog/finance-eval-real-world](https://surgehq.ai/blog/finance-eval-real-world)

[1]: https://surgehq.ai/blog/finance-eval-real-world "200 finance experts tested frontier models on real tasks. Over 70% failed."
