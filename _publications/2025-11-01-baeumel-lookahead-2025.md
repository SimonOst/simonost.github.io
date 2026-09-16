---
title: "The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs"
collection: publications
category: conferences
permalink: /publication/2025-11-01-baeumel-lookahead-2025
date: 2025-11-01
venue: 'Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP'
authors: 'Tanja Baeumel, Josef van Genabith, and Simon Ostermann'
keywords: 'BlackBoxNLP'
paperurl: 'https://aclanthology.org/2025.blackboxnlp-1.15/'
citation: 'Tanja Baeumel, Josef van Genabith, and Simon Ostermann. (2025). "The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs." Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP.'
header:
  teaser: publications/lookahead.jpg
  image: /images/publications/lookahead.jpg
---

Autoregressive large language models (LLMs) exhibit impressive performance across various tasks but struggle with simple arithmetic, such as addition of two or more operands. We show that this struggle arises from LLMs' use of a simple one-digit lookahead heuristic, which works fairly well (but not perfect) for two-operand addition but fails in multi-operand cases, where the carry-over logic is more complex. Our probing experiments and digit-wise accuracy evaluation show that LLMs fail precisely where a one-digit lookahead is insufficient to account for cascading carries. We analyze the impact of tokenization strategies on arithmetic performance and show that all investigated models, regardless of tokenization, are inherently limited in the addition of multiple operands due to their reliance on a one-digit lookahead heuristic. Our findings reveal fundamental limitations that prevent LLMs from generalizing to more complex numerical reasoning.

[Access paper here](https://aclanthology.org/2025.blackboxnlp-1.15/){:target="_blank"}
