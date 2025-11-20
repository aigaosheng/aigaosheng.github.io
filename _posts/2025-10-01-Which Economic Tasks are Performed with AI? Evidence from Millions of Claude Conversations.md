---
layout: post
title: “Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations”
date: 2025-10-01 21:23:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- AI in the workplace**
- Task automation and augmentation
- Economic impact of AI
---
---

## 1. Research topic and objective

**Topic**
The study examines how people are actually using AI—specifically through Anthropic’s Claude model—in real economic tasks, mapped to occupations and work functions. It seeks to move beyond speculation and expert forecasts, instead providing empirical evidence of AI adoption in real-world usage.

**Objective**

* To develop a method to map anonymized AI interactions to specific tasks and occupations (via U.S. Department of Labor’s O*NET database)
* To quantify how many tasks and which occupations are affected by AI
* To distinguish **augmentation** (AI assisting a human) versus **automation** (AI autonomously doing a task)
* To provide a baseline / “index” that can be tracked over time to understand AI’s evolving role in the labor market

---

## 2. Key findings and conclusions

Here are the main outcomes and insights:

* **Concentration in coding + writing tasks**
  AI usage is heavily concentrated in software development (coding) and writing tasks. Together, these two categories account for nearly half of total usage observed. ([arXiv][1])

* **Broad but uneven usage across occupations**
  While AI use is concentrated, it is not limited to only a few fields: about **36% of occupations** use AI for at least 25% of their associated tasks. ([arXiv][1])

* **Augmentation > Automation**
  Of all the AI‐human interactions studied:

  > 57% of usage suggests *augmentation* (i.e. the AI helps, iterates, or is used interactively with human oversight)
  > 43% suggests *automation* (i.e. the AI performs a task with minimal human involvement) ([arXiv][1])

* **Variation by task and occupation**
  Some tasks show more automation (e.g. translation) and others show more human-AI co-writing or iteration (e.g. editing or creative writing). ([Anthropic][2])

* **New “extended thinking” mode usage**
  In later updates (particularly after the release of Claude 3.7), the model’s “extended thinking” mode (which allows the model to reason more deeply or hold longer chains of thought) is used more in technical, scientific, and creative tasks (e.g. by software developers, multimedia artists). ([Anthropic][2])

* **Limitations acknowledged**
  The authors are careful to note limitations:

  * The data is only from interactions with Claude (not all AI systems).
  * Mapping a conversation to a task/occupation is imperfect.
  * It is not always clear whether outputs are used, modified, or discarded by users.
  * The dataset is U.S.-focused and may not generalize globally. ([arXiv][1])

* **Conclusion**
  The authors argue that AI is currently acting more as a *complement* to human labor than as a wholesale replacement. Their framework also provides a baseline for monitoring AI’s economic impact over time.

---

## 3. Critical data and facts

Here are some of the important data points and facts:

| Metric / Fact                                 | Value / Description                                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Number of conversations analyzed              | Over 4 million anonymized Claude conversations ([arXiv][1])                                              |
| Share of occupations with ≥25% tasks using AI | ~ 36% of occupations ([arXiv][1])                                                                        |
| Augmentation vs Automation ratio              | 57% augmentation, 43% automation ([arXiv][1])                                                            |
| Proportion of usage in coding + writing       | Nearly half of total usage ([arXiv][1])                                                                  |
| Use of “extended thinking” mode               | More frequent in technical, creative tasks (e.g. software developers, multimedia roles) ([Anthropic][2]) |

Additionally, the project has published associated datasets (for tasks, occupation mappings, wage data, etc.) under open licenses. ([Hugging Face][3])

---

## 4. Potential applications or implications

Based on the findings, here are several implications and possible applications:

1. **Policy & workforce planning**
   Governments and institutions can use this empirical view to guide training programs, education updates, and labor policies. For instance, they might prioritize helping workers in tasks or fields likely to be impacted by automation.

2. **Tracking AI’s economic impact over time**
   Because Anthropic intends this “index” to be updated periodically, researchers can observe trends: which occupations adopt AI most, shift in augmentation vs automation, etc.

3. **Business strategy & productivity tools**
   Companies can better understand which parts of workflows are most amenable to AI assistance (e.g. coding, writing, editing) and build tooling accordingly.

4. **Bridging inequality risks**
   The concentration of AI effects in high-skilled tasks suggests a risk of widening inequality between workers and regions with high knowledge-work density vs others. Policy interventions may be needed to ensure broader access. (Some media coverage already flags this concern.) ([Axios][4])

5. **Benchmarking for future studies**
   Academics and industry researchers can use the data and methodology as a baseline or comparison for studies across models, geographies, or over time.

6. **Caution in generalization**
   As the authors note, their results apply to Claude users (Free & Pro) and U.S.-based occupational mapping. Other platforms, sectors, or countries may show different patterns.

---

[1]: https://arxiv.org/abs/2503.04761 "Which Economic Tasks are Performed with AI? Evidence ... - arXiv"
[2]: https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7 "Anthropic Economic Index: Insights from Claude 3.7 Sonnet"
[3]: https://huggingface.co/datasets/Anthropic/EconomicIndex/blame/218b35116baa43c55beffe61f243bd81f5f84cf8/README.md "README.md · Anthropic/EconomicIndex at ... - Hugging Face"
[4]: https://www.axios.com/2025/09/15/anthropic-economic-index-2025 "Anthropic data shows uneven AI adoption"
