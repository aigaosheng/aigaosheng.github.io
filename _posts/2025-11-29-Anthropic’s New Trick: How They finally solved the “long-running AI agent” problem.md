---
layout: post
title: "Anthropic’s New Trick - How They finally solved the “long-running AI agent” problem"
date: 2025-11-29 20:35:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Anthropic
- long-running AI agents
- Claude Agent SDK
keywords: [Anthropic, AI agents, multi-session]
permalink: /Anthropic’s New Trick - How They finally solved the “long-running AI agent” problem/
---
**Anthropic’s New Trick: How They finally solved the “long-running AI agent” problem**

When you ask an AI to build a web application, refactor a big codebase, or run a multi-step task over hours or even days — the AI often “loses its mind.” It forgets what it was doing. It gets confused. It abandons important context. That’s been one of the biggest obstacles slowing down real-world adoption of autonomous AI agents.

Now, according to Anthropic, that’s changed. Their new “multi-session Claude Agent SDK” offers a clever, practical fix to the long-running agent problem — and the implications could reshape how people build production-ready AI tools. ([Venturebeat][1])

---

## 🧠 The Problem: Why AI Agents Lose Steam

AI agents built on foundation models (like those behind Claude) operate within a **context window** — a limit on how much recent conversation, instructions, or code they can “remember” at any one time. For short bursts, that’s fine. But for tasks spanning many hours or sessions, context runs out.

That limitation manifests in two common failure patterns:

* The agent tries to do too much at once, runs out of context mid-task, and ends up “guessing” what to do next — often skipping critical steps. ([Venturebeat][1])
* Or, toward the end of what it *thinks* is progress, the agent prematurely declares the job done — even if core functionality is unfinished or buggy. ([Venturebeat][1])

In short: without a way to persist memory across sessions, long-running tasks become unreliable, brittle or opaque. That’s why many AI-agent experiments stall in early phases.

---

## 🔧 The Solution: A Two-Part “Harness” That Mirrors Real Software Engineering

Anthropic’s innovation is not just a smarter model — it’s a smarter workflow. The multi-session Claude Agent SDK uses a two-agent structure that borrows from practices real engineering teams use: ([Venturebeat][1])

* **Initializer Agent**: At the very first run, it sets up the project environment — scaffolding folders, initializing versioning (e.g. git), and creating a baseline log of what needs to be done. This ensures every later session has a clear starting point. ([Venturebeat][1])
* **Coding Agent**: In each subsequent session, the coding agent picks up exactly one unfinished task from the log, implements it, tests it (the system now includes automated test tools), commits changes, and logs what was done — leaving a “clean slate” for the next session. ([Venturebeat][1])

This structured, incremental progress mirrors how human developers actually work: small, manageable steps; consistent version control; and clear logs for continuity. As Anthropic puts it, they drew these practices directly from what “effective software engineers do every day.” ([Anthropic][2])

---

## 🌐 Why This Could Matter (Especially for Developers, Enterprises & Advanced Workflows)

* **Durable, multi-day agent workflows**: What used to decay over time — build drift, forgotten context, half-baked features — can now maintain coherence across sessions. That means entire complex projects (web apps, data pipelines, automation scripts, even financial or research workflows) could be handed off to an AI agent and trusted to run incrementally.
* **Better reliability, auditability, and debugging**: Because every step is logged, versioned, and subject to testing — unlike “all-in-one prompts” — it becomes easier to track progress, diagnose failures, and maintain code quality.
* **Scalable for enterprise / production use**: For businesses wanting to deploy AI agents in mission-critical workflows (engineering, data science, content pipelines, financial modeling), this makes the difference between a cute demo and a production-ready tool. Anthropic itself suggests these lessons could apply beyond web apps — to scientific research, financial modeling, and other “long-horizon” tasks. ([Venturebeat][1])

---

## ⚠️ But It’s Just a First Step — Not a Magic Bullet

Anthropic acknowledges this is “one possible set of solutions in a long-running agent harness,” not necessarily *the* definitive fix. ([Venturebeat][1])

Open questions remain:

* Is a *single* coding agent enough across all types of tasks — or will some tasks need specialized multi-agent structures? ([Venturebeat][1])
* So far, the demo focused on full-stack web development. It remains to be seen how the approach translates to other domains (e.g. scientific research, financial modeling, large-scale data pipelines) where task types and dependencies vary widely. ([Venturebeat][1])

---

## 📘 Glossary

* **Context window**: The span of recent tokens (text, instructions, code) that a language model can “remember.” Once exceeded, earlier tokens are dropped — leading to loss of context.
* **Agent**: An AI system (often based on a large language model) that performs tasks automatically, often including tool use, code generation, file management, etc.
* **SDK (Software Development Kit)**: A collection of tools, libraries, and guidelines that allow developers to build applications using a particular platform or service — in this case, the Claude Agent SDK.
* **Multi-session / long-running agent**: An agent that can operate over multiple separate sessions (like multiple developer work sessions) — not just a single burst. Crucial for multi-day or multi-step tasks.
* **Initializer / Coding Agent (in this context)**: The two-part design principle introduced by Anthropic — the initializer sets up the environment once; the coding agent executes incremental work in each session.

---

## 📰 Conclusion

With its multi-session Claude Agent SDK, Anthropic is not just showing off a fancy new LLM — it’s rethinking **how** we integrate AI into long-term, real-world workflows. By applying human-inspired software engineering practices (version control, incremental progress, structured logging), they’re turning AI agents from fragile prototypes into potentially reliable, enterprise-ready collaborators.

Whether this becomes the new norm for AI-driven development — in web apps, data engineering, research, or financial modeling — remains to be seen. But given how fundamental the “agent memory problem” has been, this marks a meaningful milestone.

Source: [https://venturebeat.com/ai/anthropic-says-it-solved-the-long-running-ai-agent-problem-with-a-new-multi](https://venturebeat.com/ai/anthropic-says-it-solved-the-long-running-ai-agent-problem-with-a-new-multi)

[1]: https://venturebeat.com/ai/anthropic-says-it-solved-the-long-running-ai-agent-problem-with-a-new-multi "Anthropic says it solved the long-running AI agent problem with a new multi-session Claude SDK | VentureBeat"
[2]: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents "Effective harnesses for long-running agents \ Anthropic"
