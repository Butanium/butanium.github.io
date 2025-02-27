---
title: "Robustly identifying concepts introduced during chat fine-tuning using crosscoders"
collection: research
authors: "Clément Dumas*, Julian Minder*, Caden Juang, Bilal Chugtai, Neel Nanda"
permalink: /research/2024-11-crosscoders
excerpt: ''
date: 2024-11-15
venue: "MATS Program Project"
# paperurl: https://colab.research.google.com/drive/1S2QL82BZlNOFvm5i9t3juw4rgjCWNDaI?usp=sharing
# codeurl: https://github.com/Butanium/tiny-activation-dashboard/
---
Arxiv paper coming soon! Feel free to reach out if you'd like a copy.
## Abstract
Model diffing studies the *change* in a model's representations or internal algorithms as a result of fine-tuning. Focusing on such differences may offer a promising lens into a range of model behaviors of interest, and might be significantly easier than attempts to reverse engineer and interpret the entire model. The recently introduced crosscoder [(Lindsey et al., 2024)](https://transformer-circuits.pub/2024/crosscoders/index.html) enables such analysis by learning a shared dictionary of interpretable concepts represented as latent directions in both models, allowing us to track how concepts shift or emerge during fine-tuning. In this work, we identify two issues with the crosscoder training objective, which we term Complete Shrinkage and Latent Decoupling - that can misattribute concepts as unique to the fine-tuned model via prior naive specificity metrics, when they really exist in both models. We develop a technique we call Latent Scaling to address these issues - which more accurately measures each latent's presence across both base and chat models, allowing us to identify which concepts are more genuinely specific to the fine-tuned model. The concepts we identify are both more causally effective in controlling chat-model specific behavior and have higher qualitative latent interpretability. Latents with high "specificity" represent concepts such as *knowledge gap identifier* or *self-identity* and primarily activate on tokens that structure model conversations. Overall, our work improves the crosscoder-based methodology for model diffing and provides concrete insights into how chat tuning modifies the behavior of language models.

## Context

This research was conducted during Neel Nanda's MATS training phase, we used [Crosscoders](transformer-circuits.pub/drafts/crosscoders/index.html#model-diffing) to analyze the differences in the latent space of base and instruction-tuned language models. We replicated the Anthropic blog post on `Gemma 2 2B` and `Gemma 2 2B IT` by training a crosscoder on their 13th layer activations on chat data from [LMSYS Chat 1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) and a subset of [FineWeb](https://huggingface.co/datasets/huggingfacefw/fineweb).


## Demo

We created a [demo notebook](https://colab.research.google.com/drive/1S2QL82BZlNOFvm5i9t3juw4rgjCWNDaI?usp=sharing) to analyze the feature of our crosscoder using:
- Offline analysis: Examining pre-computed maximum activations across a dataset
- Online analysis: Interactive testing with custom prompts

