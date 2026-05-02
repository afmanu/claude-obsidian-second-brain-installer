# Recovery Prompts

This document provides copy-paste prompts for recovering an interrupted Claude Obsidian Second Brain installation.

Use these prompts when Claude Code has restarted, the MCP failed, setup context was lost, or final vault verification failed.

---

## General recovery prompt

```text
I was installing Claude Obsidian Second Brain and something failed.

Please read:
- TROUBLESHOOTING.md
- specs/setup-state-machine.md
- docs/mcp-setup.md
- specs/vault-output-contract.md

Then inspect the current setup state, identify the last completed step, and continue from there without starting over unless necessary.
```

---

## Continue after Claude Code restart

```text
continue setup

Before continuing, please read specs/setup-state-machine.md, identify the latest valid setup state, verify the MCP connection, and continue from the next required step without starting over.
```

---

## MCP failed

```text
The Obsidian MCP connection failed or is not available.

Please read docs/mcp-setup.md and TROUBLESHOOTING.md, then diagnose:
- Node.js
- npx
- claude mcp list
- the selected vault path
- whether Claude Code needs to restart or refresh

Repair the MCP connection, verify it by listing the vault root, and continue setup from the last valid state.
```

---

## Wrong vault path

```text
The files seem to be created in the wrong vault folder.

Please read docs/mcp-setup.md and TROUBLESHOOTING.md, compare the folder opened in Obsidian with the path used by Claude Code, repair the vault path or MCP configuration, and continue without deleting existing files.
```

---

## Windows or WSL path issue

```text
I may have a Windows/WSL path mismatch.

Please read docs/mcp-setup.md, identify whether Claude Code is running in Windows or WSL, convert the vault path if needed, make sure Obsidian and Claude point to the same physical folder, repair the MCP configuration, and verify the vault root before continuing.
```

---

## Final vault verification failed

```text
The final vault verification failed.

Please read specs/vault-output-contract.md and TROUBLESHOOTING.md, list which required files or folders are missing, recreate only the missing generated files, avoid overwriting user-modified files without confirmation, and verify the vault again before handoff.
```

---

## Missing skills catalog

```text
/explore-skills cannot find docs/skills-catalog.md.

Please read specs/vault-output-contract.md and copy docs/skills-catalog.md from the installer repository into the final vault at [VAULT_PATH]/docs/skills-catalog.md. Then verify that /explore-skills can read it.
```

---

## Missing command files

```text
Some core command files are missing from .claude/commands/.

Please read specs/vault-output-contract.md and copy the missing command files from the installer repository into [VAULT_PATH]/.claude/commands/. Do not overwrite existing modified command files without asking first.
```

---

## Start over safely

```text
I want to start over safely.

Please do not delete the existing vault. Create or ask me for a new empty vault folder, then restart the installation flow from the beginning using README.md, CLAUDE.md, TROUBLESHOOTING.md, and specs/setup-state-machine.md.
```

---

## Repair instead of reinstall

```text
I do not want to start over. Please repair the current installation.

Read TROUBLESHOOTING.md, specs/setup-state-machine.md, and specs/vault-output-contract.md. Identify missing or incomplete generated files, repair them, and continue from the last valid setup state.
```
