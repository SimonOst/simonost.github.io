---
title: "A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages"
collection: publications
category: conferences
permalink: /publication/2025-10-01-anikina-rigorous-2025
date: 2025-10-01
venue: 'Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (Long Papers)'
authors: 'Tatiana Anikina, Jan Cegin, Jakub Simko, and Simon Ostermann'
keywords: 'EMNLP'
paperurl: 'https://aclanthology.org/2025.emnlp-main.418/'
citation: 'Tatiana Anikina, Jan Cegin, Jakub Simko, and Simon Ostermann. (2025). "A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages." Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (Long Papers).'
header:
  teaser: publications/synthetic.jpg
  image: /images/publications/synthetic.jpg
---

Large Language Models (LLMs) are increasingly used to generate synthetic textual data for training smaller specialized models. However, a comparison of various generation strategies for low-resource language settings is lacking. While various prompting strategies have been proposed, such as demonstrations, label-based summaries, and self-revision, their comparative effectiveness remains unclear, especially for low-resource languages. In this paper, we systematically evaluate the performance of these generation strategies and their combinations across 11 typologically diverse languages, including several extremely low-resource ones. Using three NLP tasks and four open-source LLMs, we assess downstream model performance on generated versus gold-standard data. Our results show that strategic combinations of generation methods, particularly target-language demonstrations with LLM-based revisions, yield strong performance, narrowing the gap with real data to as little as 5\% in some settings. We also find that smart prompting techniques can reduce the advantage of larger LLMs, highlighting efficient generation strategies for synthetic data generation in low-resource scenarios with smaller models.

[Access paper here](https://aclanthology.org/2025.emnlp-main.418/){:target="_blank"}
