---
layout: post
title: "Effective context engineering for AI agents"
date: 2025-10-01 21:16:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Context engineering
- AI agents
- Prompt optimization
- Anthropic
---
---

> 
What if your AI forgot the first line of your story?

Imagine telling a friend a long tale, then halfway through realizing they no longer remember the beginning. That’s what happens when AI “runs out of attention” — it loses track of earlier context. In building smarter AI agents, knowing *what to keep in memory* is just as vital as knowing *what to ask*. Welcome to the era of **context engineering**.

---

## The rise of context engineering

For years, prompt engineering was the hero of AI development: figuring out exactly how to phrase instructions so a model responds optimally. But as models grow more powerful and agents operate over longer interactions, we reach a turning point. Now the challenge shifts: **What configuration of context yields consistent, desired behavior?** That’s the domain of context engineering. ([Anthropic][1])

Prompt engineering focuses on crafting one strong prompt (or set of prompts). Context engineering looks at the bigger picture: how system instructions, tool outputs, memory, message history, and real-time retrieval interplay within the limited context window. ([Anthropic][1])

---

## Why context matters (and dies)

Even the smartest LLMs have finite “attention budgets.” As we stuff more tokens into the prompt window, the model’s ability to recall earlier parts decays. Researchers call this **context rot**: when distant or subtle bits of information fade as the window grows. ([Anthropic][1])

This happens because transformers compute pairwise attention across all tokens. As token count grows, the pairwise relationships become diluted, and positional encoding becomes less precise. ([Anthropic][1]) Thus, more context ≠ better performance. We must treat context as a **scarce, precious resource**.

---

## Anatomy of a well-curated context

The core principle? **Maximize signal, minimize noise**. You want the smallest set of high-information tokens that still guide the model toward the behavior you want.

Here’s how each part of context fits in:

* **System prompts**: Write at the “right altitude.” Avoid brittle, overly detailed logic; avoid vague, underspecified instructions. Use structure (sections, markdown/XML tags) to separate background, instructions, tool guidance, and output format. ([Anthropic][1])
* **Tools**: Agents often interact with external tools (APIs, code, search). Good tools must be clear, minimal, and efficient in token usage. Avoid overlapping functionality or ambiguity about when to use which tool. ([Anthropic][1])
* **Examples (few-shot prompts)**: Include a handful of canonical examples, not a laundry list of edge cases. Quality trumps quantity. ([Anthropic][1])
* **Message history & dynamic context**: You don’t need to feed the entire conversation every turn. Instead, retrieve or inject only what’s relevant at each step. “Just in time” context loading works well, especially for agentic workflows. ([Anthropic][1])

---

## Context retrieval & “just-in-time” strategies

Many systems pre-load all potentially relevant data before execution. But that approach can quickly bloat context windows. A smarter path is **lazy-loading**: agents maintain lightweight references (file paths, URLs, indexed pointers) and load content dynamically when needed via tools. ([Anthropic][1])

For instance, Anthropic’s **Claude Code** uses a hybrid scheme: drop some file primitives upfront, but let the model issue targeted queries (e.g. using `grep`, `head`) to fetch large content only when needed. ([Anthropic][1]) This mirrors how humans don’t memorize everything but fetch from external storage (files, bookmarks) on demand.

This “progressive disclosure” allows agents to explore context layer by layer, keeping working memory focused and minimal. ([Anthropic][1]) But note: runtime exploration is slower than eager loading. Choosing between pre-retrieval, lazy loading, or a hybrid depends on your task’s characteristics. ([Anthropic][1])

---

## Scaling to long-horizon tasks

Some tasks span hours or require many steps — far beyond a single context window. To tackle this, Anthropic describes three key techniques:

1. **Compaction**
   When context nears its limit, summarize (compress) the history — preserving architectural decisions, unresolved bugs, state — then begin a fresh window. Example: cleaning out redundant tool call logs. ([Anthropic][1])

2. **Structured note-taking (agentic memory)**
   Persist notes outside the context window, to be recalled later. For example, agents can maintain a `NOTES.md` or to-do list tracking state over time. ([Anthropic][1]) Claude’s memory tool supports this approach. ([Anthropic][1])

3. **Multi-agent / subagent architectures**
   Spin off specialized subagents for focused tasks (e.g. deep research), each with its own context. The main agent orchestrates and synthesizes results. Subagents return distilled summaries to the parent agent. This separation of concerns limits context pollution. ([Anthropic][1])

Your usage depends on task type: compaction works well in dialogue-driven flows, notes are great for iterative projects, and subagents shine for complex research.

---

## Final thoughts: the new frontier of AI engineering

Context engineering isn’t a fad — it represents a paradigm shift in designing AI systems. As models grow smarter and more autonomous, the goal isn’t just writing beautiful prompts, but **orchestrating which pieces of context ever see the light of day**.

Techniques like compaction, structured memory, and dynamic retrieval will stay central even as future models reduce the need for manual curation. Because attention budgets don’t vanish — they just scale differently.

If you’re building with Claude or any other agent-enabled LLM, start by treating context as a scarce resource, not an infinite canvas. Optimize for signal, prune for clarity, and let your agents fetch what they need only when they need it.

---

## Glossary

| Term                                        | Definition                                                                                                                      |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Context window / context**                | The set of tokens (text, instructions, history) passed to an LLM at a given inference step.                                     |
| **Prompt engineering**                      | The practice of designing and refining prompts (instructions or examples) to guide LLM output.                                  |
| **Context engineering**                     | The art/science of selecting, structuring, and managing the tokens and external data that feed into an LLM’s context over time. |
| **Context rot**                             | The degradation of a model’s ability to recall or use earlier context when the context window becomes very long.                |
| **Compaction**                              | Summarizing or compressing prior messages or context to make room for new context while preserving essential content.           |
| **Structured note-taking / agentic memory** | Persisting intermediate state or notes outside the context window, to be recalled and reintegrated later.                       |
| **Subagent / multi-agent architecture**     | System design where specialized agents handle sub-tasks and the main agent coordinates and synthesizes outputs.                 |

---

**Source**: *“Effective context engineering for AI agents”*, Anthropic ([Anthropic][1])

[1]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents "Effective context engineering for AI agents \ Anthropic"
