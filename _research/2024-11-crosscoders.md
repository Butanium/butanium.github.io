---
title: "Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning"
collection: research
authors: "Clément Dumas*, Julian Minder*, Caden Juang, Bilal Chugtai, Neel Nanda"
permalink: /research/2024-11-crosscoders
excerpt: ''
date: 2024-11-15
venue: "MATS Program Project"
paperurl: https://arxiv.org/pdf/2504.02922
posturl: https://www.notion.so/What-We-Learned-Trying-to-Diff-Base-and-Chat-Models-And-Why-It-Matters-215cdfe65ca380e0a6c1f444d25a585c
codeurl: https://github.com/science-of-finetuning/sparsity-artifacts-crosscoders
---

## Abstract
Model diffing is the study of how fine-tuning changes a model's representations and internal algorithms. 
Many behaviors of interest are introduced during fine-tuning, and model diffing offers a promising lens to interpret such behaviors. 
Crosscoders are a recent model diffing method that learns a shared dictionary of interpretable concepts represented as latent directions in both the base and fine-tuned models, allowing us to track how concepts shift or emerge during fine-tuning. 
Notably, prior work has observed concepts with no direction in the base model, and it was hypothesized that these model-specific latents were concepts introduced during fine-tuning.
However, we identify two issues which stem from the crosscoders L1 training loss that can misattribute concepts as unique to the fine-tuned model, when they really exist in both models. 
We develop Latent Scaling to flag these issues by more accurately measuring each latent's presence across models.
In experiments comparing Gemma 2 2B base and chat models, we observe that the standard crosscoder suffers heavily from these issues. 
Building on these insights, we train a crosscoder with BatchTopK loss and show that it substantially mitigates these issues, finding more genuinely chat-specific and highly interpretable concepts. We recommend practitioners adopt similar techniques.
Using the BatchTopK crosscoder, we successfully identify a set of chat-specific latents that are both interpretable and causally effective, representing concepts such as *false information* and *personal question*, along with multiple refusal-related latents that show nuanced preferences for different refusal triggers. 
Overall, our work advances best practices for the crosscoder-based methodology for model diffing and demonstrates that it can provide concrete insights into how chat-tuning modifies model behavior.

We open-source our [code](https://github.com/science-of-finetuning/sparsity-artifacts-crosscoders), [crosscoder training library](https://github.com/jkminder/dictionary_learning), [models](https://huggingface.co/science-of-finetuning), [wandb runs](https://wandb.ai/jkminder/chat-crosscoders) and a [demo notebook to explore latents](https://dub.sh/ccdm).