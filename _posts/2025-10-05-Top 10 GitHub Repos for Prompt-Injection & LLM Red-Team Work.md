---
layout: post
title: "Top 10 GitHub Repos for Prompt-Injection & LLM Red-Team Work"
description: "Short intro (one line) · Ranked table — top 10 (prompt-injection topic) · Quick summary & recommended first steps · Caveats & safety note"
date: 2025-10-05 17:05:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Prompt Injection
- LLM Security
- Red Teaming

---
---

**Top 10 GitHub Repos for Prompt-Injection & LLM Red-Team Work, October 4 2025**

## Short intro (one line)

A snapshot of the most useful GitHub projects for prompt-injection, jailbreaks, detection and red-team automation — stars, recency, and practical notes included. ([GitHub][1])

---

## Ranked table — top 10 (prompt-injection topic)

| Rank | Repo (link)                                                                                                 | Stars | Last updated         | Short notes                                                                                                                                    |
| ---: | ----------------------------------------------------------------------------------------------------------- | ----: | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|    1 | [asgeirtj / system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)                         | 21.8k | Updated Oct 4, 2025  | Large collection of extracted system prompts from ChatGPT, Claude, Gemini — high-value payloads for red-team tests and analysis. ([GitHub][1]) |
|    2 | [CyberAlbSecOP / Awesome_GPT_Super_Prompting](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting) |  3.1k | Updated Sep 25, 2025 | Curated jailbreaks, prompt leaks, templates and attack examples — great “attack library.” ([GitHub][1])                                        |
|    3 | [protectai / llm-guard](https://github.com/protectai/llm-guard)                                             |  2.1k | Updated Sep 29, 2025 | Runtime toolkit for detecting/sanitizing malicious prompts — useful as a runtime guard layer. ([GitHub][1])                                    |
|    4 | [microsoft / AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)   |  1.7k | Updated Aug 14, 2025 | Hands-on labs and scenarios from Microsoft for building red-team skills and infrastructure. Good for structured training. ([GitHub][1])        |
|    5 | [abilzerian / LLM-Prompt-Library](https://github.com/abilzerian/LLM-Prompt-Library)                         |  1.5k | Updated Jul 12, 2025 | Playgrounds and templating for experimental prompts — useful for building reproducible payloads. ([GitHub][1])                                 |
|    6 | [protectai / rebuff](https://github.com/protectai/rebuff)                                                   |  1.4k | Updated Aug 7, 2024  | Prompt injection detector (prompt scanner) — complementary to llm-guard for detection pipelines. ([GitHub][1])                                 |
|    7 | [utkusen / promptmap](https://github.com/utkusen/promptmap)                                                 |   986 | Updated Sep 30, 2025 | Security scanner for custom LLM apps; helpful for assessing deployed prompt flows. ([GitHub][1])                                               |
|    8 | [whylabs / langkit](https://github.com/whylabs/langkit)                                                     |   948 | Updated Nov 22, 2024 | LLM observability toolkit — extracts signals from prompts/responses for monitoring and safety checks. ([GitHub][1])                            |
|    9 | [tldrsec / prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses)                 |   556 | Updated Feb 22, 2025 | Consolidated list of practical and proposed defenses — excellent starting point for countermeasure design. ([GitHub][1])                       |
|   10 | [deadbits / vigil-llm](https://github.com/deadbits/vigil-llm)                                               |   416 | Updated Jan 31, 2024 | Detector for prompt injections, jailbreaks and risky inputs — useful lightweight scanner for pipelines. ([GitHub][1])                          |

*(Source: GitHub `prompt-injection` topic listing — validated metadata: stars & last-updated shown on each repo card.)* ([GitHub][1])

---

## Quick summary & recommended first steps

1. **Mirror the top repos locally** (system_prompts_leaks, Awesome_GPT_Super_Prompting) to assemble attack payloads. ([GitHub][1])
2. **Run detection tools** (llm-guard, rebuff, vigil-llm) in a sandboxed environment against your prompt flows. ([GitHub][1])
3. **Automate via CI**: add prompt-fuzzing and observability (use prompt datasets + langkit) and baseline with curated defenses (tldrsec). ([GitHub][1])

---

## Caveats & safety note

* Many repos contain dual-use payloads and extracted system prompts. **Do not** run untrusted code or use extracted prompts against production systems. Sandbox, vet, and isolate all tests. ([GitHub][1])

---

[1]: https://github.com/topics/prompt-injection "prompt-injection · GitHub Topics · GitHub"
