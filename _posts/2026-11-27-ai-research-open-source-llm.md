---
layout: post
title: "AI Research & Open-Source LLM Brief: Nvidia Releases 30B Image Model"
series: "AI Research & Open Source"
description: "Nvidia open-sources Nemotron-Labs-Image-30B-A3B, Ant Group releases Ling-3.2-air under MIT, and Krafton publishes Raon-1 mini on Hugging Face."
date: 2026-11-27 20:39:00 +0800
type: post
published: true
status: publish
categories: [briefing]
tags:
  - AI Research
  - Open Source AI
  - LLM
  - Nvidia
  - Ant Group
keywords: nvidia nemotron image model, ant group ling 3.2 air, krafton raon-1 mini, open-weight model release, gemini hadwiger proof
permalink: /ai-research-open-source-llm-brief-2026-11-27/
---

# AI Research & Open-Source LLM Brief: Nvidia Releases 30B Image Model

**Today:** Three major open-weight releases landed within the window—Nvidia's autoregressive image model, Ant Group's multimodal MoE, and Krafton's efficient Korean LLM—while Google's Gemini 4 Carbon assisted in solving a 70-year-old geometry conjecture.

## Top Stories

### 1. 🤖 **Nvidia Open-Sources Nemotron-Labs-Image-30B-A3B Image Generation Model**

*Digital Today · Nov 27, 2026*

**Bottom line:** Nvidia has published weights for a 30B-parameter autoregressive image model that generates visual tokens sequentially rather than through diffusion, with an agent-linked system outperforming GPT Image 2 on some benchmarks.

The model has 30 billion total parameters and 3 billion active parameters, built on Nvidia's Nemotron 3 Nano LLM . It uses a dedicated tokenizer to convert generated visual tokens into images and can produce photos, illustrations, text-containing images, and infographics . A system combining AI agents scored 92.86 on GenEval versus GPT Image 2's 89, and 97.98 on LongTextBench versus 96 for GPT Image 2 and 97.60 for Google's Nano Banana Pro . The weights are available on Hugging Face for non-commercial research and evaluation only .

**Why it matters:** Nvidia is extending its open-model strategy from language into visual generation, giving enterprises a permissively accessible alternative for document, slide, and chart generation workflows. The non-commercial restriction, however, limits immediate production deployment without separate licensing.

🔗 [Read the full story](https://www.digitaltoday.co.kr/en/view/131818/nvidia-releases-free-image-generation-ai-challenging-openai-google)

---

### 2. 🤖 **Ant Group Releases Ling-3.2-air Multimodal MoE Under MIT License**

*INXEN · Nov 27, 2026*

**Bottom line:** Ant Group has published Ling-3.2-air weights on Hugging Face under a commercial-friendly MIT license, a 124B-parameter hybrid-linear MoE activating 5.5B parameters per token that accepts text, images, and video.

The model stacks 35 KDA layers and 7 Gated MLA layers, with 512 routed experts and 8 activated per token . On AutomationBench-AA, agentic office-task completion rose from 15.7% to 61% versus the previous Ling-3.0-flash-VL generation; Terminal-Bench 4.0 pass rate climbed from 0% to 27% . The recommended deployment runs on four 141GB cards (H20-3e or H200) with a 262,144-token context window . A notable caveat: on Harvey LAB-AA v1.1, the model reports an 87.7% criteria pass rate but only 0.8% full-pass rate after hallucination checks .

**Why it matters:** The MIT license removes the commercial restrictions common in Chinese open-weight releases, making this a rare fully permissive multimodal option for Asia-based enterprises building agentic document workflows. The hallucination gap in legal tasks signals caution for high-stakes deployment.

🔗 [Read the full story](https://www.inxen.news/news/radar-d2e19ae2-3f0d-4a81-8199-490d61a3b1c7)

---

### 3. 🤖 **Krafton Releases Raon-1 mini, a 30B MoE Under Apache 2.0**

*THE ELEC · Nov 26, 2026*

**Bottom line:** Korean game developer Krafton has released Raon-1 mini, a 30B-parameter MoE activating 4B parameters, under the Apache 2.0 license with adjustable reasoning levels.

The model scored 64.9 on MultiChallenge, up 5.9 points from its preview version, and Krafton claims it outperformed six comparable overseas models on that instruction-following benchmark . It also scored 72.3 on GDPval and 55.9 on BrowseComp Plus, which evaluate agent task execution . Users can select from six reasoning levels depending on task complexity, and weights are available on Hugging Face for research and commercial development .

**Why it matters:** A non-US, non-Chinese entrant in the open-weight race with a permissive license and reasoning controls adds diversity to the supply chain for Asian enterprises wary of depending solely on American or Chinese model providers.

🔗 [Read the full story](https://www.thelec.net/news/articleView.html?idxno=15933)

---

### 4. 🤖 **Google's Gemini 4 Carbon Assists in Proof of 70-Year-Old Hadwiger Conjecture**

*36Kr · Nov 27, 2026*

**Bottom line:** Google Research announced that Gemini 4 Carbon helped derive the proof structure for the three-dimensional Hadwiger covering conjecture, a geometry problem open for roughly 70 years, with the model generating the proof intuition and 13,700 lines of formal verification code.

The conjecture posits that any d-dimensional convex body can be covered by at most 2^d smaller homothetic copies of itself . The proof uses a "2 + 6 = 8 twilight-line illumination" approach, deploying two lights at the poles and six along the shadow boundary . Two human researchers guided the model mid-process, and the formalized Lean code was generated automatically . The paper is available on arXiv.

**Why it matters:** This is a concrete demonstration of frontier models contributing to original mathematical discovery rather than just problem-solving, with implications for how research labs allocate compute toward scientific reasoning. For AI strategy leaders, it strengthens the case for investing in model-assisted R&D beyond software engineering.

🔗 [Read the full story](https://eu.36kr.com/zh/p/4087355247540614)

---

### 5. 🤖 **Amini Releases Soma-1X Lite, a 2B Document Model for African Languages**

*Richard Brooks AI News · Nov 27, 2026*

**Bottom line:** Amini has released Soma-1X Lite, a 2B-parameter open model for document intelligence in African languages, achieving a 2.9% character error rate across 435 test pages in 10 languages including Swahili, Yoruba, and Wolof.

The model runs on a single GPU or CPU, enabling archives to digitize records without sending data to external services . This addresses a specific gap in multilingual document processing where most commercial models offer limited coverage.

**Why it matters:** Small, domain-specific open models for underserved languages represent a growing segment of the open-source ecosystem, relevant for Asia-based organizations operating across emerging markets with diverse linguistic requirements.

🔗 [Read the full story](https://www.amini.ai/blog-post/introducing-soma-1x-lite-a-2b-model-for-document-intelligence)

---

### 6. 📊 **India Releases Chariot-1, an 11B Home-Built LLM Under IndiaAI Mission**

*Press Information Bureau, Government of India · Nov 27, 2026*

**Bottom line:** India has released Chariot-1, an 11B-parameter model built domestically under the IndiaAI Mission, with an open IndicShift method that uses up to 2.5 times fewer tokens on Indian-language text.

The model comes in three sizes and includes a text-to-speech component that correctly reads numbers, dates, and currencies in 10 Indian languages plus English . This is a sovereign AI initiative aimed at reducing dependence on foreign models for Indian-language applications.

**Why it matters:** Sovereign AI capability building in Asia is accelerating, with India following China and others in developing domestic foundation models. For enterprises operating in South Asia, this signals a future alternative to US and Chinese model providers for local-language workloads.

🔗 [Read the full story](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2341725&lang=2®=48)

---

### 7. 🤖 **GigaChat 4 Releases Two Open-Weight MoE Models, Including a 708B Variant**

*Geoffrey Chen / Hugging Face · Nov 26, 2026*

**Bottom line:** Sber's GigaChat team released GigaChat 4 in two sizes—37B-total (activating 3.8B) and 708B-total (activating 41B)—with the larger model under an MIT license.

Both models combine Gated DeltaNet layers with multi-head latent attention using DeepSeek Sparse Attention, and a single checkpoint provides both Instant and Reasoning modes with a 1,048,576-token context window . The 708B instruction model uses the MIT license, while the 37B uses a non-commercial license for individuals . Weights and SGLang self-hosting instructions are available on Hugging Face, though no inference provider currently hosts them .

**Why it matters:** A 708B-parameter open-weight model under MIT is a significant escalation in the parameter scale available for unrestricted commercial use, though the lack of hosted inference means enterprises must self-deploy on substantial hardware.

🔗 [Read the full story](https://huggingface.co/ai-sage/GigaChat4-708B-A41B)

---

## Key Takeaways

- **Image generation joins the open-weight wave:** Nvidia's autoregressive approach offers a non-diffusion path for visual content, though commercial restrictions limit near-term enterprise deployment.
- **Permissive licensing is a differentiator:** Ant Group's MIT license and Krafton's Apache 2.0 stand out against the custom or non-commercial terms used by many Chinese and some Western releases, lowering legal friction for Asian enterprise adoption.
- **Sovereign AI models are proliferating:** India's Chariot-1 and Russia's GigaChat 4 signal that national AI programs are moving from strategy documents to shipped open-weight artifacts.

## What to Watch

Independent benchmark verification for Ling-3.2-air's agentic office-task gains, and whether Nvidia relaxes the non-commercial restriction on Nemotron-Labs-Image in response to enterprise demand.