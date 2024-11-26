---
title: "Using Crosscoders for Diffing Base and Instruction-Tuned Language Models"
collection: research
authors: "Clément Dumas, Julian Minder"
permalink: /research/2024-11-crosscoders
excerpt: 'We investigate the differences between base and instruction-tuned language models using Crosscoders'
date: 2024-11-15
venue: "MATS Program Project"
# paperurl: https://colab.research.google.com/drive/1S2QL82BZlNOFvm5i9t3juw4rgjCWNDaI?usp=sharing
# codeurl: https://github.com/Butanium/tiny-activation-dashboard/
---

This research was conducted during Neel Nanda's MATS training phase, we used [Crosscoders](transformer-circuits.pub/drafts/crosscoders/index.html#model-diffing) to analyze the differences in the latent space of base and instruction-tuned language models. We replicated the Anthropic blog post on `Gemma 2 2B` and `Gemma 2 2B IT` by training a crosscoder on their 13th layer activations on chat data from [LMSYS Chat 1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) and a subset of [FineWeb](https://huggingface.co/datasets/huggingfacefw/fineweb).

We created a [demo notebook](https://colab.research.google.com/drive/1S2QL82BZlNOFvm5i9t3juw4rgjCWNDaI?usp=sharing) to analyze the feature of our crosscoder using:
- Offline analysis: Examining pre-computed maximum activations across a dataset
- Online analysis: Interactive testing with custom prompts

A key finding was the identification of highly interpretable IT-specific features. We developed a "base uselessness" metric to quantify how much a crosscoder latent can contribute to reconstructing base model activations. This score is calculated as the -log of a scalar trained for base activation reconstruction. If the scalar is greater than 0, it means that using this latent to reconstruct the base model activation reduces the L2 loss of the reconstruction. Therefore, a crosscoder latent with a high base uselessness score represents a feature that is not present in the base model activations.

Notably, features with a base uselessness score greater than 4 seemed to be very interpretable.

