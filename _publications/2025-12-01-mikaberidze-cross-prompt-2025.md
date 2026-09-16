---
title: "Cross-Prompt Encoder for Low-Performing Languages"
collection: publications
category: conferences
permalink: /publication/2025-12-01-mikaberidze-cross-prompt-2025
date: 2025-12-01
venue: 'Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Findings)'
authors: 'Beso Mikaberidze, Teimuraz Saghinadze, Simon Ostermann, and Philipp Muller'
keywords: 'IJCNLP'
paperurl: 'https://aclanthology.org/2025.findings-ijcnlp.144/'
citation: 'Beso Mikaberidze, Teimuraz Saghinadze, Simon Ostermann, and Philipp Muller. (2025). "Cross-Prompt Encoder for Low-Performing Languages." Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Findings).'
header:
  teaser: publications/crossprompt.jpg
  image: /images/publications/crossprompt.jpg
---

Soft prompts have emerged as a powerful alternative to adapters in parameter-efficient fine-tuning (PEFT), enabling large language models (LLMs) to adapt to downstream tasks without architectural changes or parameter updates. While prior work has focused on stabilizing training via parameter interaction in small neural prompt encoders, their broader potential for transfer across languages remains unexplored. In this paper, we demonstrate that a prompt encoder can play a central role in improving performance on low-performing languages-those that achieve poor accuracy even under full-model fine-tuning. We introduce the Cross-Prompt Encoder (XPE), which combines a lightweight encoding architecture with multi-source training on typologically diverse languages - a design that enables the model to capture abstract and transferable patterns across languages. To complement XPE, we propose a Dual Soft Prompt mechanism that combines an encoder-based prompt with a directly trained standard soft prompt. This hybrid design proves especially effective for target languages that benefit from both broadly shared structure and language-specific alignment. Experiments on the SIB-200 benchmark reveal a consistent trade-off: XPE is most effective for low-performing languages, while hybrid variants offer broader adaptability across multilingual settings.

[Access paper here](https://aclanthology.org/2025.findings-ijcnlp.144/){:target="_blank"}
