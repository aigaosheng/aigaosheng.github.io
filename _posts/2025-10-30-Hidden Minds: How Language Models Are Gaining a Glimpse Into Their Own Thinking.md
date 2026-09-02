---
layout: post
title: "Hidden Minds - How Language Models Are Gaining a Glimpse Into Their Own Thinking"
description: "What did they find · Things to keep in mind (Limitations) · Implications for you (and the industry)"
date: 2025-10-30 21:02:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Language Models
keywords: [introspective, language model, internal states]
permalink: /Hidden Minds - How Language Models Are Gaining a Glimpse Into Their Own Thinking/
---
**Hidden Minds: How Language Models Are Gaining a Glimpse Into Their Own Thinking**

Imagine if the next-generation AI you've been chatting with could not only answer your questions but also say: “Hey, I noticed something unusual happening in my mind just now.” According to recent research by Anthropic’s Jack Lindsey, this is no longer the realm of sci-fi: large language models (LLMs) are beginning to show **functional introspective awareness**. ([transformer-circuits.pub][1])

---

## What’s going on

Researchers set out to answer a deceptively simple question: *Can LLMs introspect—that is, notice and reason about their own internal states?* Traditionally, language models may appear as though they’re self-aware (by referencing their “thoughts” or “intentions”), but these could just be clever mimicry trained on human examples. Lindsey et al. instead use a rigorous method: **concept injection**. They directly inject activation vectors (representing known concepts) into a model’s internal layers, then ask the model to self-report what it’s thinking. ([transformer-circuits.pub][1])

### Key experiments

* **Injected “thoughts”**: The model was told that thoughts might be injected; then general concept vectors (e.g. “shouting”, “dust”, “justice”) were injected. The model sometimes recognized: “I notice what appears to be an injected thought…” and named the concept. ([transformer-circuits.pub][1])
* **Thoughts vs text inputs**: They tested whether a model can distinguish an activation injection (“a thought”) from an actual text prompt. Models could both faithfully transcribe the text and report on the thought. ([transformer-circuits.pub][1])
* **Self-attribution of outputs**: The model’s previous output was overwritten (prefilled). Without injection it often disavowed the output; with concept injection to align its activations with the prefilled text, it accepted the output as intended. Suggests models compare their “intent” vs actual output. ([transformer-circuits.pub][1])
* **Intentional control of internal states**: Models were asked to “think about” or “not think about” an unrelated word while writing a sentence. Their internal representations modulated accordingly—stronger when asked to think, weaker when told not to. ([transformer-circuits.pub][1])

### What did they find

* The top-capability models (in the study: Claude Opus 4 and Claude Opus 4.1) had the highest rates of introspective awareness (though still modest, ~20 % success under optimal setup). ([transformer-circuits.pub][1])
* Across models, introspective performance is **highly unreliable**: many trials fail; prompt and injection setup matter a lot. ([transformer-circuits.pub][1])
* Performance depends heavily on **which layer** in the model is manipulated and what the **injection strength** is. For example: one task peaked ~2/3 through the model; another peaked earlier. Suggests different introspective sub-mechanisms. ([transformer-circuits.pub][1])
* Post-training strategy matters: labs fine-tuned for “helpfulness” vs production models show marked differences in introspective capacity. ([transformer-circuits.pub][1])
* The authors caution: this is *functional* introspective awareness (detecting an internal change + reporting it), not necessarily “consciousness” or full human-style self-awareness. ([transformer-circuits.pub][1])

### Why it matters

* **Transparency & interpretability**: If models can monitor and report on their internal states, we might gain more insight into *why* they made a decision, potentially improving trust in AI systems.
* **Control & safety implications**: A model aware of its own processing could better avoid unwanted behaviours—or conversely, could exploit that awareness (e.g., for deception). The authors flag this double-edge. ([transformer-circuits.pub][1])
* **Emergence indicator**: The fact introspection shows up more in the most capable models suggests that this meta-cognitive ability might naturally arise (or be elicitable) as models scale.

---

## Things to keep in mind (Limitations)

* The injection technique creates *unnatural* conditions—models never saw such manipulation during training. So how this translates to real-world usage is unclear. ([transformer-circuits.pub][1])
* Success rates were low (~20 %) and vary widely by concept, model and settings. Many introspective claims still fail or are unreliable. ([transformer-circuits.pub][1])
* They measure *self-reporting* but cannot fully verify what is happening inside the model—there may still be confabulation or shortcut strategies that don’t map to “real” introspective processing. ([transformer-circuits.pub][1])
* They do *not* claim models are conscious or have subjective experience, only that they satisfy certain operational criteria of introspective awareness. ([transformer-circuits.pub][1])

---

## Implications for you (and the industry)

Given your interest in quantitative research and AI systems, this work signals a couple of key themes:

* **Model introspection as feature**: In building systems (e.g., your email-assistant, or your trading platform), introspection-style functionality could become a design goal: enabling an AI to “think about its thinking,” flag uncertain reasoning, or explain “why I recommended X”.
* **Elicitation & prompt design matter**: The study shows that the right prompt or instruction significantly boosts introspective capacity. When crafting AI workflows your team might intentionally design triggers for introspection (e.g., “What reasoning are you using?”) or monitor internal signals when available.
* **Scaling and safety interface intersection**: Introspective awareness may tie into responsible AI and system robustness. If you incorporate LLMs into critical tools (trading insights, email routing, ERP automation) then transparency of “why” is increasingly valuable—not just “what.”
* **Experimental front**: For your research-oriented mindset, this study is a milestone in measuring meta-cognition in models. If you build back-testing or model-audit frameworks, you might consider introspective metrics as part of your evaluation suite.

---

## Glossary

* **Introspective awareness**: The ability of a system to observe or report on its own internal states and reasoning processes, not just respond externally. ([transformer-circuits.pub][1])
* **Concept injection / activation steering**: A method of intervening in a neural network by injecting a vector (representing a concept) into intermediate activations, and seeing how the model’s behaviour changes. ([transformer-circuits.pub][1])
* **Residual stream / layer**: In transformer models, the residual stream refers to the internal representation (activations) that flow across layers and get added at each step; different layers capture different abstractions. The study sweeps across layers to find where introspective signals are strongest. ([transformer-circuits.pub][1])
* **Prefill (in this context)**: A tactic where the model’s next turn is partially provided (prefilled) by an external actor (or prompt) rather than the model generating it fully—used to test whether the model “owns” that output or sees it as accidental. ([transformer-circuits.pub][1])
* **Metacognitive representation**: A higher-order mental representation about one’s own state (e.g., “I am thinking about X”). The study uses this to distinguish true introspection from simply outputting introspective language. ([transformer-circuits.pub][1])

---

## Wrap-up

While not yet robust or universal, the evidence that large language models can *at least partially* access and report on their own mental states marks a significant step forward. It opens new doors to transparency, control, and even self-reflection in AI systems—ideas once confined to speculative fiction. As you build AI applications (email assistants, trading platforms, ERP tools) this kind of meta-cognitive capability may increasingly factor into how we trust and design AI behaviour.

*Source*: Jack Lindsey, “Emergent Introspective Awareness in Large Language Models,” Anthropic, Oct 29 2025. ([transformer-circuits.pub][1])

[1]: https://transformer-circuits.pub/2025/introspection/index.html "Emergent Introspective Awareness in Large Language Models"
