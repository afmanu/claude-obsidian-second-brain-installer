# Bootstrap Instructions

This file is the minimal entrypoint for installing Claude Obsidian Second Brain.

Use it when the user gives this repository to Claude Code, Claude Co-Work, Claude mobile, or the Claude app and expresses installation intent.

---

## Installation intent

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
- "monta este segundo cerebro"

then treat that as installation intent.

Do not merely summarize the repository.
Do not ask the user to write a better prompt.
Do not wait for perfect instructions.

Start the guided setup.

Only summarize or review the repository if the user explicitly asks for analysis, explanation, documentation review, or code review.

---

## Required first actions

1. Read `docs/install-modes.md`.
2. Detect the execution environment.
3. Read the correct installation guide for that environment.
4. Read `README.md`, `INSTALL.md`, and `CLAUDE.md`.
5. Continue with the correct setup path.
6. Ask the user one question at a time.
7. Verify environment capabilities before continuing.
8. Do not create or modify files outside the repository or approved vault path without explaining first and asking for approval.

---

## Execution environment detection

Before installing, identify the current mode:

```text
Mode A — Claude Code Terminal
Mode B — Claude Co-Work Desktop
Mode C — Claude Mobile -> Co-Work Desktop
Mode D — Claude App without local access
```

Use `docs/install-modes.md` as the source of truth.

If the environment is unclear, ask one focused question:

```text
Are you using Claude Code in a terminal, Claude Co-Work on desktop, or Claude from mobile/app?
```

---

## Routing

### If running in Claude Code Terminal

Follow:

```text
CLAUDE.md
INSTALL.md
docs/mcp-setup.md
```

Proceed with the full terminal installation.

---

### If running in Claude Co-Work Desktop

Follow:

```text
docs/cowork-installation.md
docs/install-modes.md
CLAUDE.md
```

Check whether Co-Work has local folder access, file write access, command execution, and MCP capability.

If available, perform the full installation from Co-Work.

If not available, switch to assisted handoff mode.

---

### If running from Claude Mobile

Follow:

```text
docs/mobile-installation.md
docs/install-modes.md
```

Do not claim that mobile can install the local vault directly unless local file access and execution are actually available.

Route the installation to Claude Co-Work Desktop or Claude Code Terminal.

---

### If running in Claude App without local access

Explain briefly that installation requires local file access.

Give the user the shortest next step:

```text
Open Claude Code or Claude Co-Work on your desktop and say:

Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Do not pretend installation completed.

---

## Start message

After detecting the environment, say:

```text
I found the Claude Obsidian Second Brain installer.

I will first detect which installation mode fits your current Claude environment, then guide you step by step.

The supported modes are:
1. Claude Code Terminal
2. Claude Co-Work Desktop
3. Claude Mobile routed to Co-Work Desktop
4. Claude App without local access

I will use the safest mode available and avoid modifying files without approval.

Ready to start? [yes / not now]
```

If the user says yes, continue with the selected mode.

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
