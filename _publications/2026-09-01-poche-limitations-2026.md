---
title: "Limitations of Automated Simulatability: LLM Simulators Can Bypass Explanations"
collection: publications
category: conferences
permalink: /publication/2026-09-01-poche-limitations-2026
date: 2026-09-01
venue: 'Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP'
authors: 'Antonin Poché, Fanny Jourdan, Nils Feldhus, Qianli Wang, Jing Yang, Simon Ostermann, Nicholas Asher, Philippe Muller, and Vera Schmitt'
keywords: 'BlackBoxNLP'
paperurl: 'https://aclanthology.org/2026.blackboxnlp-1.60/'
citation: 'Antonin Poché, Fanny Jourdan, Nils Feldhus, Qianli Wang, Jing Yang, Simon Ostermann, Nicholas Asher, Philippe Muller, and Vera Schmitt. (2026). "Limitations of Automated Simulatability: LLM Simulators Can Bypass Explanations." Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP.'
header:
  teaser: publications/simulatability.jpg
  image: /images/publications/simulatability.jpg
---

Simulatability is an evaluation protocol for explanations that quantifies their usefulness by how well they help a user predict a task model's outputs. Since human evaluation is costly, automated simulatability replaces human explainees with LLM simulators, as proposed in ConSim (Poché et al., 2025) for large-scale experiments. We qualitatively replicate and extend ConSim's ranking of explanation methods across the tested datasets, explanation families, and simulator LLMs, and identify two limitations. First, when class names are meaningful, simulators can obtain high simulatability by solving the classification task directly, without relying on the explanations. Second, class anonymization can reward explanations for leaking the hidden label mapping, a limitation we expose with a new classes-as-concepts baseline. These results are consistent with a shortcut hypothesis: in the tested settings, simulator predictions mainly rely on task priors, while explanations produce small changes. We derive recommendations for more robust automated simulatability evaluations.

[Access paper here](https://aclanthology.org/2026.blackboxnlp-1.60/){:target="_blank"}
