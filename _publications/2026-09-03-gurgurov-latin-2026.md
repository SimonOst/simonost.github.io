---
title: "The Latin Substrate: How Language Models Represent and Mediate Script Choice"
collection: publications
category: conferences
permalink: /publication/2026-09-03-gurgurov-latin-2026
date: 2026-09-03
venue: 'Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP'
authors: 'Daniil Gurgurov, Alan Saji, Katharina Trinley, Josef van Genabith, and Simon Ostermann'
keywords: 'BlackBoxNLP'
paperurl: 'https://aclanthology.org/2026.blackboxnlp-1.49/'
citation: 'Daniil Gurgurov, Alan Saji, Katharina Trinley, Josef van Genabith, and Simon Ostermann. (2026). "The Latin Substrate: How Language Models Represent and Mediate Script Choice." Proceedings of the 9th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP.'
header:
  teaser: publications/latinsubstrate.jpg
  image: /images/publications/latinsubstrate.jpg
---

Many languages are written in multiple scripts, requiring large language models (LLMs) to generate equivalent linguistic content in distinct orthographic forms. While prior work suggests that LLMs route information through shared latent representations, how they internally mediate script variation remains poorly understood. We study this question by first examining per-layer output distributions with the logit lens, which reveals consistent latent romanization during transliteration, and then through representational and mechanistic analyses of script generation. At the \$\textbackslashtextit\representational\\$ level, we show that scripts of the same language become increasingly separable across layers and that a simple linear steering direction can flip a model's output script while largely maintaining semantic content. The vector generalizes asymmetrically to writing systems unseen during construction, flipping non-Latin output to Latin reliably, but mapping Latin output into varied non-Latin scripts. At the \$\textbackslashtextit\mechanistic\\$ level, we localize a small set of late-layer attention heads that causally mediate script choice. These heads transfer across unrelated languages and writing systems, suggesting that script routing is implemented by language-agnostic components. Across both analyses, we observe a consistent directional asymmetry: non-Latin output is produced by a compact, identifiable gate, while Latin-script output emerges from diffuse contributions across the network. Collectively, our findings hint that LLMs organize script variation around shared latent representations while exhibiting a privileged substrate toward Latin script.

[Access paper here](https://aclanthology.org/2026.blackboxnlp-1.49/){:target="_blank"}
