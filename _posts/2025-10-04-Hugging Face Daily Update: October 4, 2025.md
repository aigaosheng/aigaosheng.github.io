---
layout: post
title: "Hugging Face Daily Update: October 4, 2025"
date: 2025-10-04 21:23:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Hugging Face 
- Multimodal Models 
- Energy Efficiency
- Open-Source AI 
- AI Research
---
---
[![Hugging Face Open-Sourced FineVision: A New Multimodal Dataset with 24 Million Samples for Training Vision-Language Models (VLMs) - MarkTechPost](https://images.openai.com/thumbnails/url/DpJNZ3icu5meUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw6q8vQJ8PUuq0wtzwlxz_MPKclKDjJ1NDDLz023TPYPjSyKd4wsSvPTzc12VCu2NTQAAB7iJXA)](https://www.marktechpost.com/2025/09/06/hugging-face-open-sourced-finevision-a-new-multimodal-dataset-with-24-million-samples-for-training-vision-language-models-vlms/?amp=&utm_source=chatgpt.com)

**Hugging Face Daily Update: October 4, 2025**

---

### 🔍 Overview

In the past 24 hours, Hugging Face has introduced several significant updates, including new model releases, platform enhancements, and research initiatives. These developments reflect ongoing trends in the AI community, such as the rise of multimodal models, advancements in energy efficiency, and the growing influence of Chinese open-source AI systems.

---

### 🚀 New Model Releases

* **Smol2Operator**: Hugging Face has released Smol2Operator, a fully open-source pipeline that transforms a 2.2B parameter vision-language model (VLM) into an agentic GUI coder. This release includes data transformation utilities, training scripts, transformed datasets, and the resulting model checkpoint, providing a comprehensive blueprint for building GUI agents from scratch. ([Hugging Face][1])

* **Hunyuan3D-Part**: Tencent has released Hunyuan3D-Part, a model designed for 3D object understanding. This release underscores the growing focus on multimodal models that can process and understand 3D data. ([Hugging Face][1])

---

### ⚙️ Platform Enhancements

* **Compressed Tensors**: Hugging Face has introduced compressed tensors, extending safetensors files to support compressed tensor data types. This enhancement provides a unified checkpoint format for storing and loading various quantization and sparsity formats, including dense, int-quantized (int8), float-quantized (fp8), and pack-quantized (int4 or int8 weight-quantized packed into int32). This development aims to improve the efficiency and scalability of model deployment. ([Hugging Face][2])

* **Torchao Integration**: The integration of Torchao, a PyTorch architecture optimization library, into Hugging Face's ecosystem allows for custom high-performance data types, quantization, and sparsity. Torchao is composable with native PyTorch features such as `torch.compile`, enabling faster inference and training. ([Hugging Face][3])

---

### 🧠 Research Initiatives

* **Spatial Transcriptomics**: A new paper on spatial transcriptomics has been published, exploring methods to simultaneously measure gene expression and tissue morphology. This research offers unprecedented insights into cellular behavior and tissue architecture. ([Hugging Face][4])

* **Volatility Modeling in Stock Markets**: A study on volatility clustering in stock markets has been released, presenting several volatility models based on the generalized autoregressive conditional heteroscedasticity (GARCH) framework. These models aim to improve the prediction of future volatilities of stock prices. ([Hugging Face][5])

---

### 📈 Emerging Trends

* **Rise of Multimodal Models**: The release of Smol2Operator and Hunyuan3D-Part highlights the increasing emphasis on multimodal models capable of processing and understanding diverse data types, including text, images, and 3D objects.

* **Advancements in Energy Efficiency**: The introduction of compressed tensors and Torchao integration demonstrates a concerted effort to enhance the energy efficiency of AI models, addressing growing concerns over the environmental impact of large-scale AI deployments.

* **Influence of Chinese Open-Source AI Systems**: Tencent's release of Hunyuan3D-Part signifies the expanding influence of Chinese open-source AI systems, contributing to the global AI ecosystem and fostering international collaboration.

---

### 🔮 Implications for the AI Community

These developments underscore a shift towards more efficient, versatile, and globally collaborative AI systems. The focus on multimodal models and energy efficiency aligns with the industry's goals of creating more sustainable and adaptable AI technologies. Additionally, the growing influence of Chinese open-source AI systems highlights the importance of international collaboration and knowledge sharing in advancing AI research and development.

---

[1]: https://huggingface.co/models?utm_source=chatgpt.com "Models – Hugging Face"
[2]: https://huggingface.co/docs/transformers/v4.57.0/en/quantization/compressed_tensors?utm_source=chatgpt.com "compressed-tensors"
[3]: https://huggingface.co/docs/transformers/v4.57.0/en/quantization/torchao?utm_source=chatgpt.com "torchao"
[4]: https://huggingface.co/papers?q=spatial+transcriptomics&utm_source=chatgpt.com "Daily Papers"
[5]: https://huggingface.co/papers?q=stocks&utm_source=chatgpt.com "Daily Papers"
