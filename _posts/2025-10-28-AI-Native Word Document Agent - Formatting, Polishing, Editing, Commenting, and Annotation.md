---
layout: post
title: "AI-Native Word Document Agent - Formatting, Polishing, Editing, Commenting, and Annotation"
date: 2025-10-28 18:39:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI-Native
- OpenXML
- Document Automation
keywords: [AI-Native, Document Automation, AI Agent]
permalink: /AI-Native Word Document Agent - Formatting, Polishing, Editing, Commenting, and Annotation/
---

## AI-Native Word Document Agent: Formatting, Polishing, Editing, Commenting, and Annotation

Over the past two months, I’ve been working intensively on building an **AI-native word document agent from scratch**, together with another co-founder. I designed the full product architecture — frontend, backend, API interface, and database — to deliver a next-generation Word editing and collaboration experience.

### What the Product Does

This AI-native Word agent provides a full suite of professional-grade editing and collaboration capabilities, including:

* Intelligent formatting
* Layout beautification
* Revision-mode (insert/delete) editing
* Smart commenting
* Inline and contextual annotation

**ALL-IN-AI. ALL-IN-ONE.**

### Why Standard Libraries Were Not Enough

Most developers immediately think of **Python-docx** when processing Word documents. However, after a deep technical investigation, it became clear that Python-docx is insufficient for our needs:

* It does **not** support fine-grained editing or structural localization for AI agent-style commands.
* It lacks support for complex Word features such as **drawing objects**, embedded structures, and other rich document components.

Instead of relying on Python-docx, we built the agent **directly on top of the OpenXML Word standard**, with a custom indexing engine that maps all key Word XML components — `document.xml`, `comments.xml`, `header.xml`, etc. This indexing layer creates a bridge between high-level AI formatting instructions and low-level XML localization, making the system:

✅ Format-native
✅ Platform-agnostic
✅ Interoperable across all Word-compatible editors

### Multi-Agent Architecture

We adopt a multi-agent architecture, where specialized agents handle different document understanding and editing tasks:

| Agent Type           | Responsibility                                                       |
| -------------------- | -------------------------------------------------------------------- |
| User Intention Agent | Understands prompts; routes formatting / beautify / annotation tasks |
| Structure Agent      | Extracts titles, headers, sections, summaries, etc.                  |
| Beautify Agent      | spelling & syntax check, minor modification (del/ins) |
| Annotate Agent      | add AI comments on the content |

This modular architecture allows the system to scale across more complex editing tasks.

### Backend Lessons (My Development Work)

Some practical learnings from the backend development:

* **Azure GPT-5 performs the best** for Word document interpretation — especially for structural understanding and location-based formatting. We tested GPT-5-mini, GPT-4, and Gemini 2.5 Pro; only GPT-5 consistently delivered accurate results.

* **System prompt design is critical** when working with XML. GPT-5 is extremely sensitive to how XML is included in context. A poorly structured format context will make the LLM fail. Prompt engineering here is not optional — it’s essential.

* **LLM-as-coder is helpful, with limits.**
  We use free ChatGPT / Claude web apps heavily for coding drafts. But once code grows large, they cannot handle full-context refactoring. The best approach is to give **targeted snippets**, not full codebases.

* **The Word index engine is the core.**
  The richer and more precise the indexing layer, the more powerful formatting and annotation features we can support. There is still room for optimization here.

---

After nearly two months of focused development and teamwork, the product is now almost ready for release.

🎥 **Demo video:**
[https://youtu.be/KCGV9TD94jc](https://youtu.be/KCGV9TD94jc)

If you’re interested in exploring collaboration, investment, or early adoption, feel free to contact me:
📩 **[goseng123@gmail.com](mailto:goseng123@gmail.com)**

---