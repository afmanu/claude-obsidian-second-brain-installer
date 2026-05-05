# Mobile Installation Guide

This guide defines how Claude Obsidian Second Brain should behave when the user starts installation from the Claude mobile app or a Claude session without direct local file access.

Mobile can start or coordinate the installation, but it usually cannot install a local Obsidian vault directly.

---

## Core principle

Mobile is a remote starting point, not the local installer.

If the user starts from mobile, Claude should route the installation to:

```text
Claude Co-Work Desktop
```

or, if Co-Work is not available:

```text
Claude Code Terminal
```

Do not claim that the mobile session installed the local vault unless local file access and execution are actually available.

---

## Mobile installation intent

Treat these as installation intent:

```text
install this repo
install this second brain
set this up on my computer
use this repository
instala este repositorio
quiero montar este segundo cerebro
quiero instalarlo desde el móvil
```

Do not ask the user for a better prompt.

---

## Initial mobile response

Say:

```text
I can help you install Claude Obsidian Second Brain, but the actual local vault needs to be created on your computer.

From mobile, I can start the process and route it to Claude Co-Work on desktop.

To continue, your computer should have:

1. Claude Desktop available.
2. Co-Work available.
3. The computer awake and online.
4. Access to the folder where you want the Obsidian vault to live.

Do you want to continue by sending this setup to Co-Work on desktop? [yes / use terminal instead]
```

If the user chooses terminal, provide the Claude Code Terminal flow.

---

## Mobile -> Co-Work handoff

If the user confirms Co-Work handoff, provide this task instruction:

```text
Install Claude Obsidian Second Brain from this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer

Read BOOTSTRAP.md, README.md, INSTALL.md, CLAUDE.md, docs/install-modes.md, and docs/cowork-installation.md.

Use the Co-Work installation mode.

Detect whether you have local folder access, command execution, and MCP setup capability.

If you can install directly from Co-Work, proceed step by step.

If not, switch to assisted mode and give me the exact Claude Code Terminal commands required.

Do not summarize the repository. Start the installation workflow.
```

---

## Mobile -> Terminal fallback

If Co-Work is unavailable or cannot access local files, tell the user:

```text
This installation needs local file access. Please continue from Claude Code on your computer.

Open your terminal and run:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

Claude Code will read the repository and start the guided installation.
```

---

## What mobile can do safely

From mobile, Claude can:

- explain the installation modes,
- prepare the task for Co-Work,
- provide the correct repository URL,
- provide handoff instructions,
- help troubleshoot conceptually,
- continue planning the installation.

From mobile, Claude usually should not claim it can:

- create the local Obsidian vault directly,
- configure local MCP directly,
- run local shell commands directly,
- verify local file creation directly.

---

## If the user insists on mobile-only installation

Say:

```text
A mobile-only Claude session usually cannot install a local Obsidian vault because it needs access to your computer's filesystem and local MCP configuration.

The correct path is to start from mobile and delegate the work to Co-Work Desktop or Claude Code Terminal.
```

Then offer the shortest handoff path.

---

## Resume after mobile handoff

If the user returns and says the desktop task started, continue based on the environment:

- If Co-Work has local access, follow `docs/cowork-installation.md`.
- If terminal is being used, follow `CLAUDE.md`.
- If context is unclear, read `docs/install-modes.md` and ask one focused question.

Focused question:

```text
Are you continuing from Claude Co-Work Desktop, Claude Code Terminal, or mobile only?
```
