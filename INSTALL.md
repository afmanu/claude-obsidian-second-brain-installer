# Installation Guide

This guide explains how to install Claude Obsidian Second Brain.

Claude Obsidian Second Brain is a Claude Code guided installer for building a personalized Obsidian second brain.

---

## Recommended installation

Open Claude Code and paste this prompt:

```text
I want to install this Obsidian second brain system:

https://github.com/afmanu/obsidian-sppf-vault

Please do the following:

1. Clone or access the repository.
2. Read its README.md and CLAUDE.md files.
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
2. Lee sus archivos README.md y CLAUDE.md.
3. Sigue exactamente las instrucciones del repositorio.
4. Guíame paso por paso durante toda la instalación.
5. Hazme una sola pregunta cada vez.
6. No saltes ninguna comprobación del entorno.
7. No crees ni modifiques archivos fuera del repositorio o del vault previsto sin explicarme antes qué vas a hacer y pedirme aprobación.
8. Al terminar, verifica que el vault final contiene todos los archivos, carpetas, comandos y configuración necesarios.
```

---

## What happens next

Claude should:

1. Clone or access the repository.
2. Read `README.md`.
3. Read `CLAUDE.md`.
4. Start the setup wizard.
5. Check whether Obsidian is installed.
6. Create or confirm your vault folder.
7. Check whether Node.js is installed.
8. Configure the Obsidian MCP connection.
9. Ask you to restart Claude Code if needed.
10. Continue setup after restart.
11. Run `/vault-install`.
12. Ask diagnostic questions about your work, projects, and capture needs.
13. Recommend a personalized vault profile.
14. Ask which language you want for your vault.
15. Build your personalized vault structure.
16. Install the core vault skills.
17. Hand you off to the final vault folder.

---

## Requirements

Required:

- Claude Code installed and working.
- Internet connection.
- Git installed, or the ability for Claude Code to access GitHub.
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

## Manual fallback

If Claude cannot clone the repository automatically, run this manually:

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
claude .
```

Claude should then read `CLAUDE.md` and start the setup wizard.

---

## Expected result

At the end of the setup, your final vault should contain:

```text
Home.md
00_START_HERE.md
CLAUDE.md
.claude/
  vault-profile.md
  commands/
    second-brain-capture.md
    link-finder.md
    vault-synthesis.md
    next-steps-ai.md
    explore-skills.md
docs/
  skills-catalog.md
[personalized folders based on your selected profile]
```

The exact folder structure depends on your selected profile and language.

---

## After installation

After setup, stop opening this repository in Claude Code.

Open your final Obsidian vault instead:

```bash
claude /path/to/your/vault
```

Your installed skills and vault profile configuration will live inside that vault.

---

## If something fails

If setup fails, ask Claude to:

```text
Review the installation state, identify the failed step, and continue from the last successful setup stage without starting over unless necessary.
```

Common failure points are:

- Git cannot clone the repository.
- Obsidian is not installed and cannot be installed automatically.
- Node.js or `npx` is missing.
- The MCP connection does not activate until Claude Code restarts.
- Windows/WSL paths do not match the Obsidian vault location.
- The final vault is missing expected files.

A dedicated `TROUBLESHOOTING.md` file should be added in a future version.
