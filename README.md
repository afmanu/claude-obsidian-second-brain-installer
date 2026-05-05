# Claude Obsidian Second Brain

> A Claude-guided installer for building a personalized Obsidian second brain.

Claude Obsidian Second Brain is not just an Obsidian template. It is a guided installation system for Claude Code, Claude Co-Work, and mobile-started Co-Work tasks.

You give Claude this repository, Claude detects the current environment, chooses the safest installation mode, checks your local setup, creates your Obsidian vault when local access is available, connects it through MCP when possible, asks a few diagnostic questions, builds a personalized structure, and installs reusable AI skills inside the vault.

---

## Quick start

You do not need a perfect prompt.

Open Claude Code, Claude Co-Work, or Claude mobile and say something simple like:

```text
Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

or:

```text
I want to install this Obsidian second brain system:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Claude should treat that as installation intent, read the repository instructions, detect your environment, and start the guided setup or the correct handoff flow.

If Claude only summarizes the repository instead of installing it, say:

```text
Do not summarize it. Read BOOTSTRAP.md, docs/install-modes.md, README.md, INSTALL.md, and CLAUDE.md, then start the installation workflow.
```

---

## Installation modes

This installer supports four modes:

| Mode | Best for | Behavior |
|---|---|---|
| Claude Code Terminal | Users comfortable with terminal | Full direct installation |
| Claude Co-Work Desktop | Users working from Claude Desktop / Co-Work | Installs if local folder and MCP access are available; otherwise uses assisted handoff |
| Claude Mobile -> Co-Work Desktop | Users starting from mobile | Mobile starts the task, desktop Co-Work executes or coordinates installation |
| Claude App without local access | Users without local file access | Claude explains the limitation and routes the user to Code or Co-Work |

See [`docs/install-modes.md`](docs/install-modes.md) for the full routing logic.

---

## What this is

This repository is a Claude-guided installer.

It helps you create a personalized Obsidian second brain by:

- detecting the Claude environment,
- checking local capabilities,
- checking your local setup,
- creating your vault folder when local access is available,
- connecting Claude to your vault through MCP when possible,
- asking diagnostic questions,
- building a personalized folder structure,
- installing reusable Claude skills,
- handing you off to the final vault.

## What this is not

This is not:

- an Obsidian plugin,
- a SaaS app,
- a pre-filled knowledge vault,
- a replacement for Obsidian Sync,
- a fully autonomous background agent.

Claude guides and executes the setup with your approval. If your current Claude environment does not have local file access, Claude will route you to the correct environment instead of pretending the installation is complete.

---

## Who this is for

This is for people who want to use Obsidian as a second brain but do not want to manually design:

- folder structures,
- capture workflows,
- note routing rules,
- linking habits,
- review systems,
- Claude commands.

It is especially useful for:

- consultants,
- developers,
- researchers,
- entrepreneurs,
- students,
- knowledge workers,
- people building a personal operating system.

This may not be ideal if you do not want to use Obsidian, prefer a mobile-only setup without desktop access, or want to design every part of your vault manually.

---

## Install with Claude

The short version is enough:

```text
Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

For a stricter installation request, paste this:

```text
I want to install this Obsidian second brain system:

https://github.com/afmanu/claude-obsidian-second-brain-installer

Please do the following:

1. Clone or access the repository.
2. Read BOOTSTRAP.md, docs/install-modes.md, README.md, INSTALL.md, and CLAUDE.md.
3. Detect whether I am using Claude Code Terminal, Claude Co-Work Desktop, Claude Mobile, or Claude App without local access.
4. Follow the correct installation mode.
5. Guide me step by step through the full setup or handoff.
6. Ask me one question at a time.
7. Do not skip environment checks.
8. Do not create or modify files outside the intended repository or vault path unless you explain it first and ask for my approval.
9. After setup, verify that the final vault contains all required files, folders, commands, and configuration.
```

Spanish version:

```text
Quiero instalar este sistema de segundo cerebro para Obsidian:

https://github.com/afmanu/claude-obsidian-second-brain-installer

Haz lo siguiente:

1. Accede o clona el repositorio.
2. Lee BOOTSTRAP.md, docs/install-modes.md, README.md, INSTALL.md y CLAUDE.md.
3. Detecta si estoy usando Claude Code Terminal, Claude Co-Work Desktop, Claude Mobile o Claude App sin acceso local.
4. Sigue el modo de instalación correcto.
5. Guíame paso por paso durante la instalación o el handoff.
6. Hazme una sola pregunta cada vez.
7. No saltes ninguna comprobación del entorno.
8. No crees ni modifiques archivos fuera del repositorio o del vault previsto sin explicarme antes qué vas a hacer y pedirme aprobación.
9. Al terminar, verifica que el vault final contiene todos los archivos, carpetas, comandos y configuración necesarios.
```

---

## What Claude will do

Claude will guide you through the setup, automate the parts it can, ask for approval when needed, and verify that your final vault is ready to use.

The setup flow is:

1. Detect installation intent.
2. Read `BOOTSTRAP.md`, `docs/install-modes.md`, `README.md`, `INSTALL.md`, and `CLAUDE.md`.
3. Detect the execution environment.
4. Choose the safest installation mode.
5. Check whether Obsidian is installed when local access is available.
6. Create or confirm your vault folder.
7. Check whether Node.js and `npx` are installed when command execution is available.
8. Configure the Obsidian MCP connection when possible.
9. Ask you to restart or refresh Claude if needed.
10. Continue the setup after restart.
11. Run `/vault-install` once MCP is verified.
12. Ask diagnostic questions about your work and knowledge needs.
13. Recommend a personalized vault profile.
14. Create the vault structure.
15. Install the core skills.
16. Hand you off to the final vault folder.

---

## What you get

### Core vault skills

| Skill | What it does |
|---|---|
| `/second-brain-capture` | Capture an insight, decision, solution, meeting note, idea, goal, or reference as a linked note |
| `/link-finder` | Find orphan notes and suggest connections with confidence scores |
| `/vault-synthesis` | Generate a synthesis report with patterns, insights, decisions, project health, and recommendations |
| `/next-steps-ai` | Suggest your next 3-5 actions ordered by impact |
| `/explore-skills` | Browse a catalog of additional skills and build any of them on demand |

### Skills catalog

`/explore-skills` gives you a catalog of additional skills you can ask Claude to build:

- `/forgotten-notes` — resurface old notes by relevance
- `/decision-tracker` — audit past decisions and success rates
- `/daily-note` — create today's note from a template
- `/project-health` — flag stalled projects
- `/weekly-review` — guided weekly review
- `/capture-from-url` — turn any URL into a vault note
- `/meeting-recap` — structure raw meeting notes
- any skill you design yourself

---

## Repository vs. final vault

This repository is only the installer.

After setup, Claude will create your actual Obsidian vault in the location you choose.

From that point on, you should open the vault folder in Claude Code or Claude Co-Work, not this repository:

```bash
claude /path/to/your/vault
```

The final vault is where your notes, commands, profile configuration, and workflows will live.

---

## Manual installation fallback

If Claude cannot clone or access the repository automatically, run this manually:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

Claude should then read `BOOTSTRAP.md`, `CLAUDE.md`, and start the setup workflow.

---

## Requirements

Required:

- Claude Code Terminal or Claude Co-Work Desktop for full local installation.
- Internet connection.
- Git installed, or the ability for Claude to access GitHub.
- Permission to create local folders.

Installed automatically or guided by Claude when possible:

- Obsidian.
- Node.js.
- MCP connection to the vault.

Mobile users:

- Mobile can start or coordinate installation.
- The actual vault installation requires Claude Co-Work Desktop or Claude Code Terminal with local file access.

Recommended:

- Basic comfort approving file and command actions.
- A clean folder where your vault can be created.

Windows and WSL users may need additional path configuration if Obsidian runs on Windows but Claude Code runs inside WSL.

---

## Privacy

This system creates files locally in your Obsidian vault.

Do not store passwords, API keys, seed phrases, private keys, or sensitive credentials in your notes.

Review any command before approving it.

This system does not require uploading your vault to GitHub.

---

## Installation guide

For the full installation flow, see [`INSTALL.md`](INSTALL.md).
