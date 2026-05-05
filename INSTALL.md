# Installation Guide

This guide explains how to install Claude Obsidian Second Brain from Claude Code Terminal, Claude Co-Work Desktop, or Claude Mobile routed to Co-Work.

Claude Obsidian Second Brain is a Claude-guided installer for building a personalized Obsidian second brain.

---

## Recommended installation

The shortest request is enough:

```text
Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Claude should read `BOOTSTRAP.md`, detect the execution environment, and choose the correct installation mode.

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

## Installation modes

Claude should read:

```text
docs/install-modes.md
```

and choose one of these modes:

```text
Mode A — Claude Code Terminal
Mode B — Claude Co-Work Desktop
Mode C — Claude Mobile -> Co-Work Desktop
Mode D — Claude App without local access
```

Mode A is the most reliable full-installation mode.

Mode B can install directly when Co-Work has local folder access, file write access, command execution, and MCP capability. If not, it should use assisted handoff.

Mode C starts from mobile but routes the actual local installation to desktop Co-Work or Claude Code Terminal.

Mode D cannot install locally and should route the user to Claude Code or Co-Work.

---

## What happens next

Claude should:

1. Clone or access the repository.
2. Read `BOOTSTRAP.md`.
3. Read `docs/install-modes.md`.
4. Read `README.md`.
5. Read `CLAUDE.md`.
6. Read the repository specs and recovery docs.
7. Detect execution mode.
8. Start the matching setup workflow.
9. Check whether Obsidian is installed when local access is available.
10. Create or confirm your vault folder.
11. Check whether Node.js and `npx` are installed when command execution is available.
12. Configure the Obsidian MCP connection when possible.
13. Ask you to restart or refresh Claude if needed.
14. Continue setup after restart.
15. Run `/vault-install` once MCP is verified.
16. Ask diagnostic questions about your work, projects, and capture needs.
17. Recommend a personalized vault profile.
18. Ask which language you want for your vault.
19. Build your personalized vault structure.
20. Install the core vault skills.
21. Verify the final vault.
22. Hand you off to the final vault folder.

---

## Important repository files

Claude should use these files during installation:

```text
BOOTSTRAP.md
README.md
CLAUDE.md
INSTALL.md
TROUBLESHOOTING.md
docs/install-modes.md
docs/cowork-installation.md
docs/mobile-installation.md
docs/mcp-setup.md
docs/recovery-prompts.md
specs/vault-output-contract.md
specs/frontmatter-schema.md
specs/command-contracts.md
specs/setup-state-machine.md
```

---

## Requirements by mode

### Claude Code Terminal

Required:

- Claude Code installed and working.
- Internet connection.
- Git installed, or the ability for Claude Code to access GitHub.
- Terminal access.
- Permission to create local folders.

### Claude Co-Work Desktop

Required:

- Claude Co-Work available.
- Access to the installer repository folder.
- Access to the target parent folder for the vault.
- Permission to create and modify files in approved folders.

For full local installation, Co-Work also needs command execution and MCP setup capability. If unavailable, it should use assisted handoff.

### Claude Mobile

Mobile can start or coordinate installation, but the actual local vault installation requires Claude Co-Work Desktop or Claude Code Terminal.

---

## Manual terminal fallback

If Claude cannot clone or access the repository automatically, run this manually:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

Claude should then read `BOOTSTRAP.md`, `CLAUDE.md`, and start the setup workflow.

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
  system-contracts.md
[personalized folders based on your selected profile]
```

The exact folder structure depends on your selected profile and language.

The full final vault contract is defined in:

```text
specs/vault-output-contract.md
```

---

## After installation

After setup, stop opening this repository as the active workspace unless you want to update or reinstall the system.

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

Claude should read:

```text
TROUBLESHOOTING.md
specs/setup-state-machine.md
docs/mcp-setup.md
docs/cowork-installation.md
docs/mobile-installation.md
docs/recovery-prompts.md
```

Common failure points are:

- Git cannot clone the repository.
- Obsidian is not installed and cannot be installed automatically.
- Node.js or `npx` is missing.
- The MCP connection does not activate until Claude restarts or refreshes.
- Co-Work does not have access to the target folder.
- Co-Work cannot configure local MCP.
- Mobile cannot install locally and needs desktop handoff.
- Windows/WSL paths do not match the Obsidian vault location.
- The final vault is missing expected files.

If you need a copy-paste recovery prompt, see:

```text
docs/recovery-prompts.md
```
