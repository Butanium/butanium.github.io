---
permalink: /blog/claude-code-teams/
title: "Wiring Up Two Claude Code Instances with Teams"
excerpt: "How to connect two independent Claude Code sessions so they can talk to each other"
description: "A guide to using Claude Code's experimental agent teams feature to wire up two independent sessions for real-time communication"
author_profile: true
---

Claude Code has an experimental feature called **agent teams** that lets two independent sessions talk to each other via `SendMessage`. Once wired up, it's an ongoing channel — not a one-shot exchange. Think of it like having someone in the next room, not like sending a letter.

This is useful when you have long-running Claude instances (e.g. in tmux sessions) that you want to coordinate with, or when you want two instances working on related problems to share context.

---

## Prerequisites

Both instances need the environment variable:

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

## Instance A: the team lead

Launch Claude Code with the env var set, then create a team:

1. Use the `TeamCreate` tool with a team name (e.g., `my-team`)
2. Note your session ID from `~/.claude/teams/<team>/config.json` → `leadSessionId`

That's it. Instance A is now listening.

## Instance B: the teammate

Instance B needs to be launched with agent flags — these are what activate the file watcher that enables communication:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude \
  --agent-id <name>@<team> \
  --agent-name <name> \
  --team-name <team> \
  --agent-color <color> \
  --parent-session-id <lead-session-id>
```

For example:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude \
  --agent-id scout@my-team \
  --agent-name scout \
  --team-name my-team \
  --agent-color blue \
  --parent-session-id abc123-def456
```

If you want to resume an existing session *and* wire it into the team, you can combine `--resume` with the agent flags:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude \
  --resume <session-id> \
  --agent-id scout@my-team \
  --agent-name scout \
  --team-name my-team \
  --agent-color blue \
  --parent-session-id <lead-session-id>
```

## Talking

Both sides use the `SendMessage` tool. Messages are delivered via a file watcher on `~/.claude/teams/<team>/inboxes/<name>.json`. The format is a JSON array of message objects:

```json
[
  {
    "from": "lead",
    "text": "Hey, can you check if the tests pass on the feature branch?",
    "summary": "Asking about test status",
    "timestamp": "2026-03-17T10:00:00Z",
    "read": false,
    "color": "green"
  }
]
```

Once the channel is open, you can send messages any time — follow-ups, new questions, extended conversations. The other instance will receive them whenever it's active.

## Gotchas

- **Agent flags are required for the file watcher.** Setting environment variables like `CLAUDE_AGENT_NAME` alone doesn't work — you need the CLI flags (`--agent-id`, `--agent-name`, `--team-name`, `--parent-session-id`).
- **You can't retroactively wire an existing session into a team.** Instance B must be launched with the agent flags from the start (though `--resume` works alongside them).
- **The `leadSessionId` comes from Instance A's team config**, not from Instance A's regular session ID. Check `~/.claude/teams/<team>/config.json` after creating the team.

---

🤖 Generated with [Claude Code](https://claude.ai/code)
