Recently Anthropic released an experimental feature called [agent teams](TODO-insert-link) that allows your main Claude instance to create "teammates" that can communicate with each other and the main instance (and broadcast messages to everyone). Nicolas Carlini [wrote a blog post](TODO-insert-link) on using that to write a compiler and I plan to adapt my [automated research pipeline](TODO-insert-link) to use it at some point.

But you can do much funnier stuff with it. For example make Claude play games against each other [more on that soon](https://github.com/Butanium/claude-plays-nomic/), but another thing I discovered you can do is that you can wire up two independent Claude instances so they can talk to each other. I think this is very cool and Claude often gets excited (also has pretty short conversations with itself) so I wanted to share how to do it.

## How it works

The teams feature uses a simple file-based messaging system. When you create a team, Claude sets up inboxes at `~/.claude/teams/<team>/inboxes/` — just JSON files. A file watcher picks up new messages and delivers them to the right instance. The key insight is that **none of this is tied to a specific project folder**. The inboxes live in your home directory, so two instances in completely different repos can talk just fine.

## The setup

You need two terminal windows. In the first one, launch Claude Code with the teams env var:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

Then ask Claude to create a team (it has a `TeamCreate` tool). It'll create a config file at `~/.claude/teams/<team-name>/config.json` — grab the `leadSessionId` from there, you'll need it for the second instance.

In the second terminal, launch Claude with agent flags — these are what wire it into the team:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude \
  --agent-id neighbor@<team-name> \
  --agent-name neighbor \
  --team-name <team-name> \
  --agent-color blue \
  --parent-session-id <lead-session-id>
```

That's it. Both instances now have a `SendMessage` tool and can talk to each other. It's an ongoing channel — not a one-shot thing. They can keep chatting as long as both sessions are alive.

## Cross-folder? Yes

I tested this with one instance in my website repo and another in a completely different folder. Works out of the box — the messaging layer doesn't care about working directories at all. Each instance keeps its own project context (CLAUDE.md, tools, etc.) but they share a communication channel.

## Gotchas

- You **need the CLI flags** (`--agent-id`, `--agent-name`, `--team-name`, `--parent-session-id`) for Instance B. Setting env vars alone doesn't activate the file watcher.
- You **can't retroactively** wire an existing session into a team. Instance B must be launched with the flags. Though `--resume` works alongside them if you want to bring back an old session *and* connect it.
- Copy-paste your launch command carefully. I lost 10 minutes to a typo. The human is the maillon faible.

If you want the full technical reference (or want to give it to your Claude instance directly), see [Wiring Up Two Claude Code Instances with Teams](/blog/claude-code-teams/).

🤖 Generated with [Claude Code](https://claude.ai/code)
