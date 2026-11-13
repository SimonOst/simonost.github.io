---
title: "Compositional Multilingual and Behavioral Attribute Steering"
collection: publications
category: conferences
permalink: /publication/2026-09-01-kang-compositional-2026
date: 2026-09-01
venue: 'Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP'
authors: 'Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, and Simon Ostermann'
keywords: 'BlackBoxNLP'
paperurl: 'https://aclanthology.org/2026.blackboxnlp-1.38/'
citation: 'Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, and Simon Ostermann. (2026). "Compositional Multilingual and Behavioral Attribute Steering." Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP.'
header:
  teaser: publications/compositional.jpg
  image: /images/publications/compositional.jpg
---

This study examines the compositionality of steering vectors for language and behavioral control in large language models. Focusing on language, jailbreak, and conciseness, we investigate whether additive, training-free composition of attribute steering vectors can preserve the intended steering effect of each attribute, across four instruction-tuned models from two model families and two size scales. We find that single-attribute steering is reliable for all three attributes, but only within an appropriate combination of intervention layer and steering strength, with abstract behaviors (jailbreak, conciseness) favoring middle layers and language favoring earlier layers. We show that additive composition of two attribute vectors succeeds in steering both attributes simultaneously when each is injected at its own best-performing layer, and that this partially extends to three simultaneously composed attributes, addressing an inconsistency left open by prior work on training-free composition. We further analyze the geometric properties of these steering vectors, finding that they are approximately orthogonal in the residual stream, consistent with their compositional behavior.

[Access paper here](https://aclanthology.org/2026.blackboxnlp-1.38/){:target="_blank"}
