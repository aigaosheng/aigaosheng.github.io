---
layout: post
title: "Paper reading - Language Models are Injective and Hence Invertible(arXiv:2510.15511"
date: 2025-10-30 21:20:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Language Model Invertibility
- Transformer Injectivity
- AI Privacy and Interpretability
keywords: [Language Model Invertibility,Transformer Injectivity,AI Privacy and Interpretability]
permalink: /Paper reading - Language Models are Injective and Hence Invertible(arXiv:2510.15511/
---
**Paper reading: Language Models are Injective and Hence Invertible(arXiv:2510.15511)**

---

## Research topic & objective

* The paper investigates how modern decoder-only Transformer language models (i.e., models that map a discrete input text sequence (“prompt”) to a sequence of continuous hidden representations) preserve information about their input.
* In particular, the authors question a common belief: that because of components such as non-linear activations, normalization layers, attention mechanisms, etc., these models might *lose* information (i.e., two different inputs might map to the same representation).
* The **objective** is to show that:

  1. Under very general conditions, the mapping from input prompt → hidden (last‐token) representation is *injective* (i.e., different inputs almost always map to different outputs) for such models.
  2. Training with gradient descent does *not* break this property.
  3. They furthermore provide an algorithm (“SIPIT”) that, given the hidden states of a model, recovers the exact input prompt — thereby showing the mapping is *practically invertible*.
* In other words: to establish that language models of this kind are (almost surely) lossless with respect to the input text, and that this can be exploited in practice for full inversion of the prompt.

---

## Key findings & conclusions

* **Theoretical result:** They prove that for decoder-only Transformer architectures (with finite vocabulary V, finite context length K, embedding width d, at least one attention head per block, analytic activations, etc) if parameters are randomly initialized from any continuous density (e.g., Gaussian, uniform) then *with probability one* two distinct prompts yield distinct last-token hidden state representations. (Injectivity at initialization) ([arXiv][1])
* They also prove that gradient‐descent training (for a finite number of steps) preserves this property: i.e., training cannot collapse the mapping into a many‐to‐one map. Thus the injectivity holds throughout training under standard conditions. ([arXiv][1])
* They define and implement the algorithm **SIPIT** (Sequential Inverse Prompt via Iterative Updates), which given hidden states at some layer, recovers the original input sequence token‐by‐token. They prove correctness: SIPIT recovers the true input in *at most* T×|V| steps (where T = length of sequence) and under the injectivity assumptions. ([arXiv][1])
* **Empirical evidence:**

  * They sample 100,000 prompts from a mixture of datasets (Wikipedia, C4, The Pile) and extracted last‐token hidden states from several models (e.g., GPT-2, Gemma3 family, Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M) and computed minimum pairwise distances between that hidden state for different prompts. They observed **no collisions** (i.e., no two distinct prompts had identical last‐token states) and the minimum distances remained well above a collision threshold (10⁻6) across layers, model depths, etc. ([arXiv][1])
  * They then applied SIPIT to recover prompts from hidden states (for GPT-2 Small): for 100 prompts of length 20 tokens, SIPIT achieved **100% token‐level accuracy**, recovering the exact input sequence, and with an average time ~28 s compared to brute‐force ~3889 s or approaches that failed altogether. ([arXiv][1])
* **Conclusions:**

  * Decoder‐only Transformer LMs almost surely map distinct input prompts to distinct hidden states.
  * The hidden states at the last token already contain sufficient information to uniquely identify the input prompt.
  * It is therefore possible to *invert* the mapping (recover the prompt) from hidden activations, in linear time and in practice.
  * The perception that these models are “lossy” in the sense of many inputs → same state is, under standard assumptions, misleading.
  * This has implications for interpretability (the model’s latent space faithfully encodes inputs), for transparency, and for issues of privacy and deployment (hidden states are not anonymised or irrecoverable—they *contain* the input).

---

## Critical data & facts

* Vocabulary size, context length, embedding dimension: The paper considers a finite vocabulary V, context length ≤ K, embedding width d. Specific numeric values of V, K, d vary by model; but formally they show results for any fixed finite V and K. ([arXiv][1])
* Theorem 2.2: For parameters θ drawn from any continuous‐density distribution, for any two distinct prompts s ≠ s′ ∈ V ≤ K, the probability that r(s; θ) = r(s′; θ) is zero. (Injectivity at initialization) ([arXiv][1])
* Theorem 2.3: After T steps of gradient descent (step sizes in (0,1)), with probability one over initialization, s ≠ s′ ⇒ r(s; θ_T) ≠ r(s′; θ_T). (Injectivity preserved under training) ([arXiv][1])
* Empirical Table 1 (4.1): Minimum pairwise L2 distance between last‐token states across models (e.g., for Llama-3.1-8B: ~0.001 at layer 1, ~0.129 mid, ~0.620 last layer). All values well above collision threshold of 10⁻6. ([arXiv][1])
* Empirical Table 2 (4.2): Inversion results:

  * HARDPROMPTS: time ~6132.59 s ±104.61, accuracy 0.00
  * BRUTEFORCE: time ~3889.61 s ±691.17, accuracy 1.00
  * SIPIT: time ~28.01 s ±35.87, accuracy 1.00 ([arXiv][1])
* They confirm that inversion time rises only mildly with depth (longer prompts/ deeper layers) in Fig 6. ([arXiv][1])
* They note that failure‐cases/collisions are possible only for parameter settings lying in a “measure‐zero” set (i.e., extremely unlikely under standard continuous initialization) or if non‐analytic choices are used (e.g., quantization, tied weights, identical embeddings) which they discuss as engineered adversarial cases. ([arXiv][1])

---

## Potential applications or implications

* **Interpretability & mechanistic probing:** Because the input is almost surely uniquely encoded in the hidden state, analyses that probe hidden representations have a firm foundation: one can be confident the model has preserved the full prompt. Thus interpretability work (e.g., causal analysis, attribution) can assume no “information loss” in hidden states (except perhaps under non‐standard modifications).
* **Privacy / data‐leak / usage concerns:** Hidden states (activations) or stored last‐token representations cannot be assumed anonymized or de‐identified: the paper shows that given hidden states, one *can* recover the exact input prompt. Thus use‐cases where hidden states are stored or transmitted (e.g., for caching, embedding sharing, model‐as‐a‐service) must treat them as if they contain the original user input. The authors highlight legal implications: e.g., regulators treating embeddings as “non‐personal data” may need to revisit that assumption. ([arXiv][1])
* **Model‐based auditing & transparency:** Because the mapping is invertible, one could audit logged hidden states to confirm what prompt produced them (given the algorithmic capability). This increases system transparency.
* **Safety / deployment:** For systems that rely on hiding user input via embedding or intermediate activation, this result warns that hiding via representation may not be sufficient: the input may still be reconstructed. So deployments must treat hidden states with equivalent sensitivity as the original text.
* **Compression & memory design:** Although not the main focus, knowing that hidden states preserve the entire input might influence how models or systems compress or store representation data: one could ask whether storing only some subset of activations loses anything—but here the result says: the last‐token hidden state already preserves full input almost always.
* **Future research directions:** The authors mention extending this analysis to multimodal transformers (vision + language, audio) or quantised/approximate models; studying how noise, compression, quantisation breaks invertibility; exploring how to exploit or mitigate this invertibility for e.g., secure or private representations. ([arXiv][1])

---

[1]: https://www.arxiv.org/pdf/2510.15511 "Language Models are Injective and Hence Invertible"
