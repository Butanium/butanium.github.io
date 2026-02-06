---
title: "Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences"
collection: research
authors: "Julian Minder*, Clément Dumas, Stewart Slocum, Helena Casademunt, Cameron Holmes, Robert West, Neel Nanda"
permalink: /research/2025-10-narrow-finetuning
excerpt: ''
date: 2025-10-14
venue: "ICLR 2026"
paperurl: https://arxiv.org/abs/2510.13900
posturl: https://www.alignmentforum.org/posts/sBSjEBykQkmSfqrwt/narrow-finetuning-leaves-clearly-readable-traces-in
codeurl: https://github.com/science-of-finetuning/diffing-toolkit
---

## Abstract
We show that narrow finetuning creates strong biases in LLM activations that can be interpreted to understand the finetuning domain, and these biases can be discovered using simple tools from model diffing—the study of differences between models before and after finetuning. Analyzing activation differences on the first few tokens of random text and steering by adding this difference to the model activations produces text similar to the format and general content of the finetuning data. We also created an LLM-based interpretability agent to understand the finetuning domain that performs significantly better with access to the bias. Our analysis spans synthetic document finetuning for false facts, emergent misalignment, subliminal learning, and taboo word guessing game models across different architectures (Gemma, LLaMA, Qwen) and scales (1B to 32B parameters).
