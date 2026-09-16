---
title: "Modular Arithmetic: Language Models Solve Math Digit by Digit"
collection: publications
category: conferences
permalink: /publication/2025-12-02-baeumel-modular-2025
date: 2025-12-02
venue: 'Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Findings)'
authors: 'Tanja Baeumel, Daniil Gurgurov, Yusser al Ghussin, Josef van Genabith, and Simon Ostermann'
keywords: 'IJCNLP'
paperurl: 'https://aclanthology.org/2025.findings-ijcnlp.86/'
citation: 'Tanja Baeumel, Daniil Gurgurov, Yusser al Ghussin, Josef van Genabith, and Simon Ostermann. (2025). "Modular Arithmetic: Language Models Solve Math Digit by Digit." Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Findings).'
header:
  teaser: publications/modulararithmetics.jpg
  image: /images/publications/modulararithmetics.jpg
---

While recent work has begun to uncover the internal strategies that Large Language Models (LLMs) employ for simple arithmetic tasks, a unified understanding of their underlying mechanisms is still lacking. We extend recent findings showing that LLMs represent numbers in a digit-wise manner and present evidence for the existence of digit-position-specific circuits that LLMs use to perform simple arithmetic tasks, i.e. modular subgroups of MLP neurons that operate independently on different digit positions (units, tens, hundreds). Notably, such circuits exist independently of model size and of tokenization strategy, i.e. both for models that encode longer numbers digit-by-digit and as one token. Using Feature Importance and Causal Interventions, we identify and validate the digit-position-specific circuits, revealing a compositional and interpretable structure underlying the solving of arithmetic problems in LLMs. Our interventions selectively alter the model's prediction at targeted digit positions, demonstrating the causal role of digit-position circuits in solving arithmetic tasks.

[Access paper here](https://aclanthology.org/2025.findings-ijcnlp.86/){:target="_blank"}
