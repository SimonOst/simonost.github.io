---
title: "Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection"
collection: publications
category: conferences
permalink: /publication/2026-03-02-ghussin-multilingual-2026
date: 2026-03-02
venue: 'Proceedings of the 6th Workshop on Trustworthy NLP (TrustNLP 2026)'
authors: 'Yusser Al Ghussin, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, Patrick Schramowski, and Simon Ostermann'
keywords: 'TrustNLP'
paperurl: 'https://aclanthology.org/2026.trustnlp-main.24/'
citation: 'Yusser Al Ghussin, Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, Patrick Schramowski, and Simon Ostermann. (2026). "Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection." Proceedings of the 6th Workshop on Trustworthy NLP (TrustNLP 2026).'
header:
  teaser: publications/saes.jpg
  image: /images/publications/saes.jpg
---

Sparse autoencoders (SAEs) enable feature-level mechanistic interpretability and activation steering in large language models (LLMs), but SAE-based language control remains unreliable in multilingual settings: most SAEs are trained on English-only data, and steering layers are chosen heuristically. We address these limitations by advancing a principled, mechanistic account of multilingual language steering with SAEs. First, we show that training SAEs on multilingual data consistently strengthens cross-lingual representations and yields more reliable, quality-preserving language control across layers and model families. Second, we introduce an \textbackslashemph\a priori\ steering layer-selection rule based on the intersection of multilingual alignment and language separability, which predicts effective intervention depths without exhaustive layerwise search. We evaluate our approach on LLaMA-3.1-8B and Gemma-2-9B across machine translation and cross-lingual summarization (CrossSumm), using SpBLEU, ROUGE-L, COMET, and LaSE. Our results show that multilingual SAEs combined with intersection-selected layers stabilize the trade-off between language identification accuracy and generation quality, providing a principled, predictive, representation-level account of multilingual SAE steering.

[Access paper here](https://aclanthology.org/2026.trustnlp-main.24/){:target="_blank"}
