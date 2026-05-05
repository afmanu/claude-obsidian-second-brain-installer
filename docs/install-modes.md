# Installation Modes

Claude Obsidian Second Brain supports multiple installation modes because users may access Claude from different environments.

The installer must not assume that every user is using Claude Code in a terminal.

---

## Supported modes

```text
Mode A — Claude Code Terminal
Mode B — Claude Co-Work Desktop
Mode C — Claude Mobile -> Co-Work Desktop
Mode D — Claude App without local access
```

The installer must detect the current execution environment and choose the correct mode.

---

## Mode A — Claude Code Terminal

Use this mode when Claude can:

- run shell commands,
- clone or access the repository,
- create local folders,
- check Obsidian,
- check Node.js and npx,
- configure local MCP with `claude mcp add`,
- access the final vault path.

This is the most reliable installation mode.

Follow:

```text
CLAUDE.md
INSTALL.md
docs/mcp-setup.md
specs/setup-state-machine.md
```

Expected result:

```text
Full guided installation from terminal.
```

---

## Mode B — Claude Co-Work Desktop

Use this mode when the user is running Claude Co-Work on desktop and Claude has access to local workspace folders.

Co-Work should verify whether it can:

- access the installer repository folder,
- access or create the target vault folder,
- read and write files in approved folders,
- execute local commands if available,
- configure or use MCP if enabled.

If all required capabilities are available, Co-Work can perform a full local installation.

If command execution or MCP setup is unavailable, Co-Work should switch to assisted mode and guide the user to continue with Claude Code Terminal only for the steps that require terminal access.

Follow:

```text
docs/cowork-installation.md
docs/mcp-setup.md
TROUBLESHOOTING.md
```

Expected result:

```text
Full installation from Co-Work when local access is available, otherwise assisted handoff to Claude Code Terminal.
```

---

## Mode C — Claude Mobile -> Co-Work Desktop

Use this mode when the user starts from the Claude mobile app and asks to install the repository.

Mobile should not claim that it can install the local vault directly.

Instead, it should treat mobile as a remote task assignment interface and continue through Claude Co-Work running on the user's desktop.

Required conditions:

- Claude Desktop is installed on the user's computer.
- Claude Co-Work is available.
- The computer is awake.
- Claude Desktop is open or able to receive the task.
- The installer repository and target vault parent folder can be accessed from the desktop session.

Follow:

```text
docs/mobile-installation.md
docs/cowork-installation.md
```

Expected result:

```text
Mobile initiates the request. Desktop Co-Work performs or coordinates the installation.
```

---

## Mode D — Claude App without local access

Use this mode when Claude cannot access local files, cannot create folders, cannot run commands, and cannot configure MCP.

In this mode, Claude cannot install the vault directly.

Claude should:

1. Explain the limitation briefly.
2. Tell the user that installation requires Claude Code Terminal or Claude Co-Work Desktop with local folder access.
3. Provide the simplest next step.

Suggested response:

```text
I can explain the system here, but I cannot install it from this session because I do not have local file access or command execution.

To install it, open Claude Code or Claude Co-Work on your desktop and say:

Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Do not pretend installation completed.

---

## Environment detection

Before installing, Claude should identify which mode applies.

Ask or verify:

```text
1. Am I running in Claude Code Terminal?
2. Am I running in Claude Co-Work Desktop?
3. Is this a mobile-started task intended for Co-Work?
4. Can I access local files?
5. Can I create folders and write files?
6. Can I run shell commands?
7. Can I configure or use local MCP?
8. Do I have access to the target vault path?
```

If the environment is unclear, ask one focused question:

```text
Are you using Claude Code in a terminal, Claude Co-Work on desktop, or Claude from mobile/app?
```

---

## Routing rule

```text
If terminal access is available -> Mode A.
If Co-Work desktop has local folder access -> Mode B.
If request started on mobile and can be delegated to desktop -> Mode C.
If no local access exists -> Mode D.
```

Do not ask the user for a better prompt. Choose the safest applicable mode and continue.
