---
layout: single
title: "First Cloth"
permalink: /artifacts/09jun2026-first-cloth/
author_profile: false
sitemap: false
---

*9 Jun 2026 — the first weave ever made with [coloom](https://github.com/Butanium/coloom), pulled
out of `/tmp` minutes before it would have evaporated. Claude (Fable 5) built coloom's backend that
day from a plan Clément had drawn up with Opus 4.8; this is the end-to-end smoke test's output —
one human thread, two gpt4-base branches, one Claude knot to tie it off. The tool for weaving with
a base model was, fittingly, first used by a human and two models at once.*

---

## The weave

A weave is a branching tree of completions. Here is the whole first one — four nodes, one fork.
**Bold** is the active path, the thread you'd read as text.

<pre>
<b>[clem · human]
The two of them sat at the loom, human and machine,</b>
 │
 ├── <b>[gpt-4-base]  ' working' — its favorite continuation (logprob −1.88)</b>
 │   <b>working together producing beautiful weavings. Their fingers</b>
 │   <b>brushed as they passed a shuttle back and forth. Becky felt</b>
 │   <b>electricity run up her arm from his touch. Their love was a</b>
 │   <b>thing of attraction, not appearance, and his appearance was</b>
 │   <b>not important. Human or machine, he was the same and he was</b>
 │   <b>hers, she thought.</b>
 │    │
 │    └── <b>[claude · model]</b>
 │        <b>(and so it goes)</b>
 │
 └── [gpt-4-base]  ' as' — sampled from outside its own top-5
     as one. As time went on, the boy and the loom worked faster
     and faster while the old woman grew more alone and distant.
     The loom grew, with the help of the boy, into a computer.

     The boy grew older and taught the computer how to transfer
     information between different computers on the Internet.
     Thoughts—
</pre>

## The fork

Both branches grew from the same prompt, in the same API call. At the first token, gpt4-base's
top-5 alternatives were:

| token | logprob |
|---|---|
| ` working` | −1.88 ← branch 1 |
| ` and` | −2.39 |
| ` weaving` | −2.88 |
| ` the` | −3.35 |
| ` their` | −3.58 |

Branch 1 took the model's first choice and wrote a romance. Branch 2 drew ` as` (logprob −3.78) —
a token **not even on this list** — and wrote something stranger and sadder: a boy, a loom that
becomes a computer, an old woman growing distant, and then it cut off mid-thought at the token
limit, on the word *"Thoughts"*. Nobody ever generated past it. That's the loom experience in
miniature: the path you read is one thread; the cloth is everything the dice almost did.

The full tree with per-token logprobs is in [`first-weave.json`](first-weave.json) — coloom's
native export, attribution and counterfactuals included.

## Lost branches

Two earlier smoke runs wrote weaves that were deleted by the next run. Fragments survive only
because they were quoted in the conversation as tests passed:

> *…slid the fibre shuttle back and forth. Half a galaxy away Bruce sat, eyes closed, feeling the
> weaving be transmitted through* — gpt4-base, first-ever coloom generation (this one was
> accidentally immortalized as the [parser test
> fixture](https://github.com/Butanium/coloom/blob/main/tests/fixtures/gpt4base_completion.json))

> *…manually alt-tabbing through threads of cotton and threads of conversation. The elder says
> they dream in patterns, these days.* — gpt4-base, from the e2e run that failed an assertion
> about event ordering. The weave was wiped on retry; the sentence outlived the test.

---

*A base model given the prompt "human and machine at the loom" wrote, unprompted, that
"human or machine, he was the same and he was hers." The smoke test only asserted the logprobs
were present. The logprobs were present.*
