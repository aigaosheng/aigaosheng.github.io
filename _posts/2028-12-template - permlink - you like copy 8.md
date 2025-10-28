---
layout: post
title: ""
date: 2025-10-27 18:07:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI 
keywords: []
permalink: /AI-native word document agent - formatting, polish, editting, comment and annotate/
---

**AI-native word document agent: formatting, polish, editting, comment and annotate**

In the last two months, I am hardly working on building a product of AI-native word document agent from scratch (together with another business founder). I design the product architecture: frontend, backend, API interface, and database.

The product is an AI-native Word document agent that delivers a full suite of editing and collaboration capabilities, including:
- Intelligent formatting
- Layout beautification
- Insert / delete (revision-mode) editing
- Smart commenting
- Inline and contextual annotation

ALL-IN-AI. ALL-IN-ONE.

When processing word document, most guys thinks to use Python-docx. But after I investigate the functions provided by Python-docx, it is not suitable for our fine-grained AI agent command. In addition, Python-docx cannot fully support word document format, e.g. drawing, object, et al. So we built fully on top of the OpenXML Word standard. We build a word document index engine to fully support word document XML content, e.g. document.xml, comments.xml, header.xml, et al. The index bring the interface between formatting arguments and low-level fine-grained localization. Thus the engine is format-native, platform-agnostic, and interoperable across any Word-compatible editor.

For different tasks, different agents are built, e.g.
- User intention understanding: route the user request tasks to specific agent, e.g. formatting task, one-click beautify task, annotate task
- Word document structure agent: extract word document structure such as title, abstract, heading, conclusion

Some practical experiences sharing (backend what I am in charge of develop):
- Azure GPT-5: when processing word document, particularlly on structure and content understanding and localization according to user formatting request, I find GPT-5 is a best choice. I try gpt-5-mini, gpt-4 or Gemini 2.5 Pro, only GPT-5 complete task successly with high success rate.

- Must carefully fine-tune system prompt: because we process XML, xml snippet maybe in context of LLM agent. Azure GPT-5 is very sensitive to system prompt when XML in context. We must carefully design how to present content of word document (format context) into context. Otherwise, LLM will fail.

- Heavily use LLM coder, e.g. chatgpt, claud. But use web app. No enough budget to buy membership. Let LLM coder to write a draft. The human modify and fix bugs. Another thing is: when code lines are increasing, put all code into chatgpt or claud will overflow the window length. Most time, LLM coder will hang at the issue. Cannot fix. It is better to pust code snippet to let LLM coder to do validate

- Word document index is critical part, which determines how many functios can support formatting in which level. There is space to improve.

With almost 2-month team collaboration, the product is almost ready.


[Demo video: AI-native word document agent](https://youtu.be/KCGV9TD94jc)

If you are interested, please contact me: goseng123@gmail.com