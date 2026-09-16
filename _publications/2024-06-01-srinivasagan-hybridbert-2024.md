---
title: "HybridBERT - Making BERT Pretraining More Efficient Through Hybrid Mixture of Attention Mechanisms"
collection: publications
category: conferences
permalink: /publication/2024-06-01-srinivasagan-hybridbert-2024
date: 2024-06-01
venue: 'Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 4: Student Research Workshop)'
authors: 'Gokul Srinivasagan and Simon Ostermann'
keywords: 'NAACL-SRW'
paperurl: 'https://aclanthology.org/2024.naacl-srw.30/'
citation: 'Gokul Srinivasagan and Simon Ostermann. (2024). "HybridBERT - Making BERT Pretraining More Efficient Through Hybrid Mixture of Attention Mechanisms." Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 4: Student Research Workshop).'
header:
  teaser: publications/hybridbert.jpg
  image: /images/publications/hybridbert.jpg
---

Pretrained transformer-based language models have produced state-of-the-art performance in most natural language understanding tasks. These models undergo two stages of training: pretraining on a huge corpus of data and fine-tuning on a specific downstream task. The pretraining phase is extremely compute-intensive and requires several high-performance computing devices like GPUs and several days or even months of training, but it is crucial for the model to capture global knowledge and also has a significant impact on the fine-tuning task. This is a major roadblock for researchers without access to sophisticated computing resources. To overcome this challenge, we propose two novel hybrid architectures called HybridBERT (HBERT), which combine self-attention and additive attention mechanisms together with sub-layer normalization. We introduce a computing budget to the pretraining phase, limiting the training time and usage to a single GPU. We show that HBERT attains twice the pretraining accuracy of a vanilla-BERT baseline. We also evaluate our proposed models on two downstream tasks, where we outperform BERT-base while accelerating inference. Moreover, we study the effect of weight initialization with a limited pretraining budget. The code and models are publicly available at: www.github.com/gokulsg/HBERT/.

[Access paper here](https://aclanthology.org/2024.naacl-srw.30/){:target="_blank"}
