---
title: "Separating Tongue from Thought: Activation Patching Reveals Language-Agnostic Concept Representations in Transformers"
collection: research
authors: "Clément Dumas*, Chris Wendler*, Veniamin Veselovsky, Giovanni Monea, Robert West"
permalink: /research/2024-07-llm-english
excerpt: 'We provide causal evidence for the existence of language-agnostic concept representations within LLMs'
date: 2024-07-15
venue: "ACL 2025, main"
paperurl: https://arxiv.org/abs/2411.08745
codeurl: https://github.com/Butanium/llm-lang-agnostic
---
This work was conducted during my first year master's internship at EPFL (École Polytechnique Fédérale de Lausanne) under the supervision of [Chris Wendler](https://ch.linkedin.com/in/wendlerc) and [Robert West](https://dlab.epfl.ch/people/west/).

This work was previously a spotlight at the [ICML 2024 mechanistic interpretability workshop](https://openreview.net/forum?id=0ku2hIm4BS).

## Abstract

A central question in multilingual language modeling is whether large language models (LLMs) develop a universal concept representation, disentangled from specific languages. In this paper, we address this question by analyzing latent representations (latents) during a word-translation task in transformer-based LLMs. We strategically extract latents from a source translation prompt and insert them into the forward pass on a target translation prompt. By doing so, we find that the output language is encoded in the latent at an earlier layer than the concept to be translated. Building on this insight, we conduct two key experiments. First, we demonstrate that we can change the concept without changing the language and vice versa through activation patching alone. Second, we show that patching with the mean representation of a concept across different languages does not affect the models' ability to translate it, but instead improves it. Finally, we generalize to multi-token generation and demonstrate that the model can generate natural language description of those mean representations. Our results provide evidence for the existence of language-agnostic concept representations within the investigated models.