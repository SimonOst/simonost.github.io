---
title: "Compositional Multilingual and Behavioral Attribute Steering"
collection: publications
category: conferences
permalink: /publication/2026-09-01-kang-compositional-2026
date: 2026-09-01
venue: 'Accepted at the 9th BlackboxNLP Workshop'
authors: 'Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, and Simon Ostermann'
keywords: 'BlackBoxNLP'
citation: 'Hyun Gu Kang, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, and Simon Ostermann. (2026). "Compositional Multilingual and Behavioral Attribute Steering." Accepted at the 9th BlackboxNLP Workshop.'
header:
  teaser: publications/compositional.jpg
  image: /images/publications/compositional.jpg
---

This study examines the compositionality of steering vectors for language and behavioral control in large language models. Focusing on language, jailbreak, and conciseness, we investigate whether additive, training-free composition of attribute steering vectors can preserve the intended steering effect of each attribute, across four instruction-tuned models from two model families and two size scales. We find that single-attribute steering is reliable for all three attributes, but only within an appropriate combination of intervention layer and steering strength, with abstract behaviors (jailbreak, conciseness) favoring middle layers and language favoring earlier layers. We show that additive composition of two attribute vectors succeeds in steering both attributes simultaneously when each is injected at its own best-performing layer, and that this partially extends to three simultaneously composed attributes, addressing an inconsistency left open by prior work on training-free composition. We further analyze the geometric properties of these steering vectors, finding that they are approximately orthogonal in the residual stream, consistent with their compositional behavior.

Use [Google Scholar](https://scholar.google.com/scholar?q=Compositional+Multilingual+and+Behavioral+Attribute+Steering){:target="_blank"} for full citation
