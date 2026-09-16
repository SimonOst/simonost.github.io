---
title: "Reverse Probing: Evaluating Knowledge Transfer via Finetuned Task Embeddings for Coreference Resolution"
collection: publications
category: conferences
permalink: /publication/2025-05-01-anikina-reverse-2025
date: 2025-05-01
venue: 'Proceedings of the 10th Workshop on Representation Learning for NLP (RepL4NLP-2025)'
authors: 'Tatiana Anikina, Arne Binder, David Harbecke, Stalin Varanasi, Leonhard Hennig, Simon Ostermann, Sebastian Möller, and Josef Van Genabith'
keywords: 'Rep4NLP'
paperurl: 'https://aclanthology.org/2025.repl4nlp-1.9/'
citation: 'Tatiana Anikina, Arne Binder, David Harbecke, Stalin Varanasi, Leonhard Hennig, Simon Ostermann, Sebastian Möller, and Josef Van Genabith. (2025). "Reverse Probing: Evaluating Knowledge Transfer via Finetuned Task Embeddings for Coreference Resolution." Proceedings of the 10th Workshop on Representation Learning for NLP (RepL4NLP-2025).'
header:
  teaser: publications/reverseprobing.jpg
  image: /images/publications/reverseprobing.jpg
---

In this work, we reimagine classical probing to evaluate knowledge transfer from simple source to more complex target tasks. Instead of probing frozen representations from a complex source task on diverse simple target probing tasks (as usually done in probing), we explore the effectiveness of embeddings from multiple simple source tasks on a single target task. We select coreference resolution, a linguistically complex problem requiring contextual understanding, as focus target task, and test the usefulness of embeddings from comparably simpler tasks tasks such as paraphrase detection, named entity recognition, and relation extraction. Through systematic experiments, we evaluate the impact of individual and combined task embeddings. Our findings reveal that task embeddings vary significantly in utility for coreference resolution, with semantic similarity tasks (e.g., paraphrase detection) proving most beneficial. Additionally, representations from intermediate layers of fine-tuned models often outperform those from final layers. Combining embeddings from multiple tasks consistently improves performance, with attention-based aggregation yielding substantial gains. These insights shed light on relationships between task-specific representations and their adaptability to complex downstream tasks, encouraging further exploration of embedding-level task transfer. Our source code is publicly available under https://github.com/Cora4NLP/multi-task-knowledge-transfer.

[Access paper here](https://aclanthology.org/2025.repl4nlp-1.9/){:target="_blank"}
