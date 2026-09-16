---
title: "On Multilingual Encoder Language Model Compression for Low-Resource Languages"
collection: publications
category: conferences
permalink: /publication/2025-11-01-gurgurov-multilingual-2025-1
date: 2025-11-01
venue: 'The 14th International Joint Conference on Natural Language Processing and The 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Student Research Workshop)'
authors: 'Daniil Gurgurov, Michal Gregor, Josef van Genabith, and Simon Ostermann'
keywords: 'IJCNLP-SRW'
paperurl: 'https://aclanthology.org/2025.ijcnlp-srw.5/'
citation: 'Daniil Gurgurov, Michal Gregor, Josef van Genabith, and Simon Ostermann. (2025). "On Multilingual Encoder Language Model Compression for Low-Resource Languages." The 14th International Joint Conference on Natural Language Processing and The 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Student Research Workshop).'
header:
  teaser: publications/compression.jpg
  image: /images/publications/compression.jpg
---

In this paper, we combine two-step knowledge distillation, structured pruning, truncation, and vocabulary trimming for extremely compressing multilingual encoder-only language models for low-resource languages. Our novel approach systematically combines existing techniques and takes them to the extreme, reducing layer depth, feed-forward hidden size, and intermediate layer embedding size to create significantly smaller monolingual models while retaining essential language-specific knowledge. We achieve compression rates of up to 92\% with only a marginal performance drop of 2-10\% in four downstream tasks, including sentiment analysis, topic classification, named entity recognition, and part-of-speech tagging, across three low-resource languages. Notably, the performance degradation correlates with the amount of language-specific data in the teacher model, with larger datasets resulting in smaller performance losses. Additionally, we conduct extensive ablation studies to identify best practices for multilingual model compression using these techniques.

[Access paper here](https://aclanthology.org/2025.ijcnlp-srw.5/){:target="_blank"}
