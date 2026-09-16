---
title: "Language Arithmetics: Towards Systematic Language Neuron Identification and Manipulation"
collection: publications
category: conferences
permalink: /publication/2025-12-03-gurgurov-language-2025
date: 2025-12-03
venue: 'Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Main)'
authors: 'Daniil Gurgurov, Katharina Trinley, Yusser Al Ghussin, Tanja Baeumel, Josef van Genabith, and Simon Ostermann'
keywords: 'IJCNLP'
paperurl: 'https://aclanthology.org/2025.ijcnlp-long.156/'
citation: 'Daniil Gurgurov, Katharina Trinley, Yusser Al Ghussin, Tanja Baeumel, Josef van Genabith, and Simon Ostermann. (2025). "Language Arithmetics: Towards Systematic Language Neuron Identification and Manipulation." Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Main).'
header:
  teaser: publications/langarithmetics.jpg
  image: /images/publications/langarithmetics.jpg
---

Large language models (LLMs) exhibit strong multilingual abilities, yet the neural mechanisms behind language-specific processing remain unclear. We analyze language-specific neurons in Llama-3.1-8B, Mistral-Nemo-12B, and Aya-Expanse-8B \& 32B across 21 typologically diverse languages, identifying neurons that control language behavior. Using the Language Activation Probability Entropy (LAPE) method, we show that these neurons cluster in deeper layers, with non-Latin scripts showing greater specialization. Related languages share overlapping neurons, reflecting internal representations of linguistic proximity. Through language arithmetics, i.e. systematic activation addition and multiplication, we steer models to deactivate unwanted languages and activate desired ones, outperforming simpler replacement approaches. These interventions effectively guide behavior across five multilingual tasks: language forcing, translation, QA, comprehension, and NLI. Manipulation is more successful for high-resource languages, while typological similarity improves effectiveness. We also demonstrate that cross-lingual neuron steering enhances downstream performance and reveal internal "fallback" mechanisms for language selection when neurons are progressively deactivated. Our code is made publicly available at https://github.com/d-gurgurov/Language-Neurons-Manipulation.

[Access paper here](https://aclanthology.org/2025.ijcnlp-long.156/){:target="_blank"}
