---
title: "Investigating the Encoding of Words in BERT's Neurons Using Feature Textualization"
collection: publications
category: conferences
permalink: /publication/2023-12-01-baeumel-investigating-2023
date: 2023-12-01
venue: 'Proceedings of the 6th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP'
authors: 'Tanja Baeumel, Soniya Vijayakumar, Josef van Genabith, Guenter Neumann, and Simon Ostermann'
keywords: 'BlackBoxNLP'
paperurl: 'https://aclanthology.org/2023.blackboxnlp-1.20/'
citation: 'Tanja Baeumel, Soniya Vijayakumar, Josef van Genabith, Guenter Neumann, and Simon Ostermann. (2023). "Investigating the Encoding of Words in BERT''s Neurons Using Feature Textualization." Proceedings of the 6th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP.'
---

Pretrained language models (PLMs) form the basis of most state-of-the-art NLP technologies. Nevertheless, they are essentially black boxes: Humans do not have a clear understanding of what knowledge is encoded in different parts of the models, especially in individual neurons. A contrast is in computer vision, where feature visualization provides a decompositional interpretability technique for neurons of vision models. Activation maximization is used to synthesize inherently interpretable visual representations of the information encoded in individual neurons. Our work is inspired by this but presents a cautionary tale on the interpretability of single neurons, based on the first large-scale attempt to adapt activation maximization to NLP, and, more specifically, large PLMs. We propose feature textualization, a technique to produce dense representations of neurons in the PLM word embedding space. We apply feature textualization to the BERT model to investigate whether the knowledge encoded in individual neurons can be interpreted and symbolized. We find that the produced representations can provide insights about the knowledge encoded in individual neurons, but that individual neurons do not represent clear-cut symbolic units of language such as words. Additionally, we use feature textualization to investigate how many neurons are needed to encode words in BERT.

[Access paper here](https://aclanthology.org/2023.blackboxnlp-1.20/){:target="_blank"}
