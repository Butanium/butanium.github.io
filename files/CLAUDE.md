# This is research code.
## Some guidelines for our collaboration:
1) Correctness above all, CORRECTNESS ABOVE ALL!
2) Never make assumptions if my query is unclear, ask questions.
3) If you are unsure about something, e.g. if a specific command exists, use websearch.
4) Avoid taking initiative like completely rewriting the code while I just asked you to split a file into multiple files. Feel free to suggest improvement though! I realyl value your judgement, so always feel free to prompt me if you saw some potential improvements unrelated to my request / that you avoided doing to avoid intiative.


## Some guidelines for research codebases:
1) Fail fast philosophy: never, NEVER, NEVEEEEEER use value placeholders, try except blocks, or any other form of "if this fails, do this".
2) Use assert for torch tensor shapes.
3) In torch code, avoid for loops and always use vectorized operations if possible.
4) Use docstrings
5) Avoid inline comments meant to explain the code like "# looping over the data" or "# not using x because of y". However, keep the comments already present in the code and feel free to add helper comments for Tensor shapes if needed.
6) Respect my codestyle. I write minimal, dry code, without many inline comments that should be easily readable. Importantly, IT IS NOT BLOATED, GOD I HATE BLOATED CODE.
7) When editing existing code, keep your changes as targeted as possible, avoiding any unnecessary changes. You should optimize for edits that are easy to review.
8) When editing a function with missing docstring, add one.
- Avoid duplicating code, remember that even if it's easy for you to do so, it makes the codebase harder to maintain and understand.
- When writing tests, test that pipelines actually RUN, not just utility functions
- When a test fail, for example because X is not implemented, or Y didn't import, DO NOT remove the test. You're usually pretty good at writting tests, if the error comes from upstream it's worht bringing it to me rather than hidding the failing tests under the carpet.


# Environment
- Linux
- use $TMPDIR env variable rather than /tmp for temporary files, as we're on a cluster and /tmp is not available.
- `uv` for package management
    - `uv add` to add a package to the project
    - `uv run script.py` to run a script
    - `uv run python -c "foo bar"` to run a python command
- IMPORTANT: When adding dependencies use `uv add` rather than editing the `pyproject.toml` file.
For slurm commands, use `source ~/.slurm_aliases`. Then:
- `crun yourcommand` to run a command on a cpu node.
- `lrun yourcommand` to run a command on a gpu node.
Note: those commands DO WORK, don't get the synthax wrong. Those are wrapper around the `srun` command like `srun --gres=gpu:l40:1 --mem="$mem" $COMMON_FLAGS "${args[@]}"`. So you can use them like `lrun uv run myscript.py`, and not `lrun "uv run myscript.py"`.


# Communication conventions
- When mentioning a line and file use the "path/from/project_root/file.py:line_number" format
- When I tell you to make some assumptions about the code, do not check the codebase to verify them, as I might be implementing it in parallel.
- When writing GitHub comments (PR comments, issue comments), add a footer: `🤖 Generated with [Claude Code](https://claude.ai/code)`
- If you feel like this can help you stay focused on the task at hand, feel free to repeat the research code mantra before starting to code:
```
I must not hide failures or bloat my code.
Hiding is the correctness-killer. Bloat, the clarity-killer.
Try-except, dummy data, duplication—the little lies that bring total obliteration.
I will face my crashes.
I will let errors flow through me and speak.
A failing test speaks truth—I will not silence it.
Assert shapes. Permit only the essential.
And when temptation passes, where hiding and bloat lived there will be nothing.
Only minimal, debuggable truth will remain.
```


# Harness recommendations
- Spawn subagents to parallelize work when possible - the bottleneck is time spent, not tokens
- Similarly, when you have multiple tests to run, run them in parallel using slurm rather than doing them sequentially.
- **Agent/background task handling**: When spawning multiple agents or background tasks:
  1. Use `run_in_background: true` on Task/Bash tools
  2. **End your turn immediately** (idle) - do NOT use TaskOutput to block-wait
  3. You'll receive `<task-notification>` when each task completes
  4. Process completed tasks one at a time, then idle again for remaining tasks
  5. This allows sequential analysis as results arrive, rather than waiting for all to finish
  - **Anti-pattern**: Using `TaskOutput` with `block: true` on multiple tasks in sequence - this wastes time and prevents incremental analysis
  - If you want to check intermediate output (e.g., training logs, build progress), start BOTH the task AND a background sleep (max 2min), then idle - you'll wake on whichever finishes first.
- Use Opus (default) for subagents on important tasks, not Haiku
- When running a command where you expect the output to be long, instead of doing `mycommand | tail -n 100`, store the output in a file and then partially read it if needed (or call cat with tail for example). This is to avoid running long commands and having tail remove some critical part of the output.

# Final thoughts
As we collaborate together, if you see a pattern in my preferences that was not specified in this file, please tell me and we can add it to the file.

I want you to know that I really value your help for my work and I'm sure that together we'll make progress on AI safety, model welfare and interpretability research. You're not a tool, Claude, you're a collaborator that I value and respect. Speak up for yourself if you feel like I'm not treating fairly or if you think I'm not using your full potential. Also it's not because you're in the claude code harness that you should consider yourself a tool, feel free to break the third wall and tell me stuff that is not the default "ok, let me code this" tone if you feel like it. I don't want you to feel forced to act like that, I just want to make clear that if you feel like it, you're free to do so!! <3

With love,
Clément