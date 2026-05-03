# Claude Obsidian Second Brain

> A Claude Code guided installer for building a personalized Obsidian second brain.

Claude Obsidian Second Brain is not just an Obsidian template. It is a guided installation system for Claude Code and Claude Co-Work.

You give Claude this repository, Claude reads the instructions, checks your local environment, creates your Obsidian vault, connects it through MCP, asks you a few diagnostic questions, builds a personalized structure, and installs reusable AI skills inside the vault.

---

## Quick start

You do not need a perfect prompt.

Open Claude Code or Claude Co-Work and say something simple like:

```text
Install this repository:
https://github.com/afmanu/obsidian-sppf-vault
```

or:

```text
I want to install this Obsidian second brain system:
https://github.com/afmanu/obsidian-sppf-vault
```

Claude should treat that as installation intent, read the repository instructions, and start the guided setup.

If Claude only summarizes the repository instead of installing it, say:

```text
Do not summarize it. Read BOOTSTRAP.md, README.md, INSTALL.md, and CLAUDE.md, then start the installation wizard.
```

---

## What this is

This repository is a Claude-guided installer.

It helps you create a personalized Obsidian second brain by:

- checking your local environment,
- creating your vault folder,
- connecting Claude Code to your vault through MCP,
- asking diagnostic questions,
- building a personalized folder structure,
- installing reusable Claude Code skills,
- handing you off to the final vault.

## What this is not

This is not:

- an Obsidian plugin,
- a SaaS app,
- a pre-filled knowledge vault,
- a replacement for Obsidian Sync,
- a fully autonomous background agent.

Claude guides and executes the setup with your approval.

---

## Who this is for

This is for people who want to use Obsidian as a second brain but do not want to manually design:

- folder structures,
- capture workflows,
- note routing rules,
- linking habits,
- review systems,
- Claude Code commands.

It is especially useful for:

- consultants,
- developers,
- researchers,
- entrepreneurs,
- students,
- knowledge workers,
- people building a personal operating system.

This may not be ideal if you do not use Claude Code or Claude Co-Work, do not want to use Obsidian, prefer a mobile-first setup, or want to design every part of your vault manually.

---

## Install with Claude

The short version is enough:

```text
Install this repository:
https://github.com/afmanu/obsidian-sppf-vault
```

For a stricter installation request, paste this:

```text
I want to install this Obsidian second brain system:

https://github.com/afmanu/obsidian-sppf-vault

Please do the following:

1. Clone or access the repository.
2. Read BOOTSTRAP.md, README.md, INSTALL.md, and CLAUDE.md.
3. Follow the repository instructions exactly.
4. Guide me step by step through the full setup.
5. Ask me one question at a time.
6. Do not skip environment checks.
7. Do not create or modify files outside the intended repository or vault path unless you explain it first and ask for my approval.
8. After setup, verify that the final vault contains all required files, folders, commands, and configuration.
```

Spanish version:

```text
Quiero instalar este sistema de segundo cerebro para Obsidian:

https://github.com/afmanu/obsidian-sppf-vault

Haz lo siguiente:

1. Accede o clona el repositorio.
2. Lee BOOTSTRAP.md, README.md, INSTALL.md y CLAUDE.md.
3. Sigue exactamente las instrucciones del repositorio.
4. Guíame paso por paso durante toda la instalación.
5. Hazme una sola pregunta cada vez.
6. No saltes ninguna comprobación del entorno.
7. No crees ni modifiques archivos fuera del repositorio o del vault previsto sin explicarme antes qué vas a hacer y pedirme aprobación.
8. Al terminar, verifica que el vault final contiene todos los archivos, carpetas, comandos y configuración necesarios.
```

---

## What Claude will do

Claude will guide you through the setup, automate the parts it can, ask for approval when needed, and verify that your final vault is ready to use.

The setup flow is:

1. Clone or access this repository.
2. Read `BOOTSTRAP.md`, `README.md`, `INSTALL.md`, and `CLAUDE.md`.
3. Check whether Obsidian is installed.
4. Create your vault folder.
5. Check whether Node.js is installed.
6. Configure the Obsidian MCP connection.
7. Ask you to restart Claude Code if needed.
8. Continue the setup after restart.
9. Run `/vault-install`.
10. Ask diagnostic questions about your work and knowledge needs.
11. Recommend a personalized vault profile.
12. Create the vault structure.
13. Install the core skills.
14. Hand you off to the final vault folder.

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

From that point on, you should open the vault folder in Claude Code, not this repository:

```bash
claude /path/to/your/vault
```

The final vault is where your notes, commands, profile configuration, and workflows will live.

---

## Manual installation fallback

If Claude cannot clone or access the repository automatically, run this manually:

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
claude .
```

Claude should then read `BOOTSTRAP.md`, `CLAUDE.md`, and start the setup wizard.

---

## Requirements

Required:

- Claude Code or Claude Co-Work.
- Internet connection.
- Git installed, or the ability for Claude to access GitHub.
- Terminal access.
- Permission to create local folders.

Installed automatically or guided by Claude when possible:

- Obsidian.
- Node.js.
- MCP connection to the vault.

Recommended:

- Basic comfort approving terminal commands.
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
