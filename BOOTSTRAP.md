# Bootstrap Instructions for Claude Code / Claude Co-Work

This file is the minimal entrypoint for installing Claude Obsidian Second Brain.

If a user gives you this repository and says anything like:

- "install this repo"
- "set this up"
- "run this system"
- "I want to use this Obsidian second brain"
- "read this repository and start"
- "install Claude Obsidian Second Brain"
- "quiero instalar este repositorio"
- "lee este repo y ejecútalo"
- "quiero usar este sistema"

then treat that as installation intent.

Do not merely summarize the repository.
Do not ask the user to write a better prompt.
Do not wait for perfect instructions.

Start the guided setup.

---

## Required first actions

1. Read `README.md`.
2. Read `INSTALL.md`.
3. Read `CLAUDE.md`.
4. Follow the setup wizard in `CLAUDE.md`.
5. Ask the user one question at a time.
6. Verify the environment before continuing.
7. Do not create or modify files outside the repository or approved vault path without explaining first and asking for approval.

---

## Start message

Say:

```text
I found the Claude Obsidian Second Brain installer.

I will guide you step by step to create your personalized Obsidian second brain.

I will check Obsidian, create or confirm your vault folder, check Node.js and npx, configure the Obsidian MCP, then run the vault installer.

Ready to start? [yes / not now]
```

If the user says yes, continue with `CLAUDE.md`.

---

## Recovery

If setup fails, read:

```text
TROUBLESHOOTING.md
docs/mcp-setup.md
docs/recovery-prompts.md
specs/setup-state-machine.md
```

Then continue from the last valid state. Do not restart from zero unless necessary.
