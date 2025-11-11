---
layout: post
title: "AI’s Time‑Sense Fault - Why Large Language Models Still Can’t Read an Analog Clock"
date: 2025-11-11 22:14:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- analog clock reading
- AI model generalisation
- multimodal large language model
keywords: [AI limitations, clock reading AI, multimodal AI]
permalink: /AI’s Time‑Sense Fault - Why Large Language Models Still Can’t Read an Analog Clock/
---
**AI’s Time‑Sense Fault: Why Large Language Models Still Can’t Read an Analog Clock**

If you thought modern AI systems were nearly foolproof, think again. In an illuminating twist, a recent study reveals that even the most advanced multimodal large language models (MLLMs) struggle with what seems like one of the simplest tasks: reading an analog clock.

## A surprising failure in full view

The research team led by Javier Conde (Universidad Politécnica de Madrid) and collaborators at the Politecnico di Milano and Universidad de Valladolid assembled a **synthetic dataset of more than 43,000 images** of analog clocks showing different times. ([IEEE Spectrum][1])

They then tested four different MLLMs on a subset of the clock images. The models **initially failed badly** at reading the times correctly. With extra training on about 5,000 of the images, performance improved—but when tested on completely new clock‑styles, the models’ accuracy dropped again dramatically. ([IEEE Spectrum][1])

The core issue: these models are **terrible at generalising** when the input deviates even slightly from their training examples.

## What’s really going wrong?

The study dug deeper: What makes reading a clock so tricky for AI?

* First, models had difficulty distinguishing the **clock hands** (short vs. long) and their **orientation** relative to the dial. ([IEEE Spectrum][1])
* Second, variations such as “warped” clocks (shapes altered) or hands with added arrows on the tips—which humans easily interpret—completely throw off the models. ([IEEE Spectrum][1])
* The researchers found a cascading effect: failing to identify the hand correctly leads to greater spatial‑orientation errors. In short: the models’ hand‑detection errors exacerbate the time‑reading errors. ([IEEE Spectrum][1])

Conde explains: *“It appears that reading the time is not as simple a task as it may seem, since the model must identify the clock hands, determine their orientations, and combine these observations to infer the correct time.”* ([IEEE Spectrum][1])

## Why this matters beyond clocks

On first glance this may look like an academic curiosity (“AI can’t read clocks!”), but it actually shines a revealing light on broader limitations of current AI models.

* These MLLMs may perform well on familiar inputs (those similar to their training data) but falter in out‑of‑distribution scenarios. That lack of **robust generalisation** is a recurring concern. ([IEEE Spectrum][1])
* In high‑stakes applications — such as medical imaging, autonomous driving perception, or robotics — small errors in spatial interpretation or pattern generalisation *could* lead to serious consequences. The clock‑reading problem is a miniature metaphor for more critical failures. ([IEEE Spectrum][1])
* The results suggest that, despite the hype around large pretrained models and multimodal AI, **we cannot take model performance for granted**. Testing needs to cover diverse, unexpected, and distorted inputs. ([IEEE Spectrum][1])

## Take‑aways & implications

* Even state‑of‑the‑art multimodal models struggle at tasks humans find trivial—like reading analog clocks.
* Training on more data helps, but if the model hasn’t encountered a particular distortion (shape‑warp, arrow‑tip hands, etc.), performance collapses.
* For developers and researchers building AI systems: you must test for *edge‑cases*, distortions, unfamiliar styles—not just the “happy path”.
* For investors, users, or stakeholders: don’t assume “AI” equals “universal intelligence”. The gaps persist.
* For the future: bridging this gap may demand new architectures or training regimes that emphasise *spatial reasoning*, *invariance to distortions*, and *deeper disentangling* of perceptual factors.

## Glossary

* **Multimodal Large Language Model (MLLM)**: An AI system that can process more than one type of input (for example text, images, video) and generate outputs accordingly.
* **Generalisation (in AI)**: The ability of a model to perform well on new, previously unseen data—especially data that differs from its training set.
* **Out‑of‑distribution (OOD) input**: An input that differs significantly in style, format or other properties from the data the model saw during training.
* **Synthetic dataset**: A data collection created artificially (e.g., via simulation or generative methods) rather than gathered from real‑world examples.
* **Spatial orientation (in vision models)**: The model’s capacity to identify how parts of an image are arranged in space (e.g., direction/angle of clock‑hands) and infer meaning from that arrangement.

## Conclusion

In short: if you can glance at an analog clock and instantly tell the time, you’re outperforming many of today’s cutting‑edge AI models in that narrow task. And perhaps more importantly, this little task exposes serious questions about how robust, reliable or flexible our current AI systems really are when faced with the unexpected. The next time someone praises “AI” as near‑human intelligence, remember: it struggles to tell time too.

**Source**: [IEEE Spectrum: “AI Models Fail Miserably at This One Easy Task: Telling Time”](https://spectrum.ieee.org/large-language-models-reading-clocks)

[1]: https://spectrum.ieee.org/large-language-models-reading-clocks "Large Language Models Struggle With Reading Clocks - IEEE Spectrum"
