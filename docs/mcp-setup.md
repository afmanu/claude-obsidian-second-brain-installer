# MCP Setup Guide

This document explains how the Obsidian MCP connection works in Claude Obsidian Second Brain.

Claude must read this file whenever MCP setup, MCP verification, or MCP repair is needed.

---

## Purpose

The `obsidian-vault` MCP connects Claude to the user's local Obsidian vault.

This connection allows Claude to:

- list vault files,
- read notes,
- write notes,
- patch notes,
- create generated hub notes,
- create reports and captures inside the final vault.

Without this MCP, Claude can still write configuration files with filesystem access, but it cannot reliably operate the vault as an Obsidian knowledge base.

---

## Execution mode note

MCP setup depends on the current Claude environment.

```text
Claude Code Terminal
→ usually supports full MCP setup through `claude mcp add`.

Claude Co-Work Desktop
→ may support local MCP depending on local access, settings, extensions, and permissions.

Claude Mobile
→ should not claim direct local MCP setup. Route to Co-Work Desktop or Claude Code Terminal.

Claude App without local access
→ cannot configure a local Obsidian MCP directly.
```

If MCP setup is not available in the current environment, switch to the correct handoff mode from `docs/install-modes.md`.

---

## Required dependencies

Before configuring the MCP, verify when command execution is available:

```bash
node --version
npx --version
claude --version
```

Required:

- Node.js is installed.
- `npx` is available.
- Claude Code is installed and available in the terminal when using terminal mode.
- `[VAULT_PATH]` exists and is writable.

If Node.js or `npx` is missing, repair that before installing the MCP.

---

## MCP install command

Use this command after `[VAULT_PATH]` has been selected and created:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Rules:

- Always use the absolute vault path.
- Wrap the vault path in quotes.
- Explain what the command does before running it.
- Ask for approval before running the command.

---

## Windows native fallback

On Windows native, if the standard `npx` command fails or the MCP connection closes unexpectedly, try:

```bash
claude mcp add obsidian-vault -- cmd /c npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Use this only when appropriate for Windows native environments.

Do not use this in macOS, Linux, or WSL unless there is a clear reason.

---

## Co-Work MCP behavior

If running in Claude Co-Work Desktop:

1. Check whether local MCP setup is available.
2. Check whether Co-Work can access the target vault folder.
3. Check whether Co-Work can run or coordinate the MCP command.
4. If it can, proceed with MCP setup.
5. If it cannot, switch to assisted handoff mode from `docs/cowork-installation.md`.

Suggested message:

```text
Co-Work may not have enough local MCP access in this session.

I can continue guiding the installation, but the MCP setup may need to be completed from Claude Code Terminal.
```

Then provide the exact command for the user's operating system.

---

## Activation behavior

After adding the MCP, Claude may need to restart or refresh before the MCP is available.

Tell the user:

```text
The MCP connection has been configured.

Restart or refresh Claude so the connection activates.

When you are back, open this repository again and say:
continue setup
```

Do not run `/vault-install` until MCP verification succeeds.

---

## Verification

After restart or refresh, verify the MCP before continuing.

Verification steps:

1. Confirm `[VAULT_PATH]` is still known.
2. Use the `obsidian-vault` MCP to list the vault root.
3. If listing succeeds, the MCP is connected.
4. If listing fails, diagnose before continuing.

Successful verification message:

```text
The Obsidian MCP connection is working. I can now build your vault.
```

Failure message:

```text
The Obsidian MCP connection is not available yet. I will diagnose the MCP setup before continuing.
```

---

## Diagnosis commands

Use these commands when diagnosing MCP issues and command execution is available:

```bash
node --version
npx --version
claude mcp list
```

Optional path checks:

```bash
pwd
ls "[VAULT_PATH]"
```

On Windows PowerShell, use:

```powershell
Test-Path "[VAULT_PATH]"
```

---

## Common failures and fixes

### Node.js is missing

Symptoms:

- `node --version` returns not found.
- `npx --version` returns not found.
- MCP command fails before installing package.

Fix:

1. Install Node.js LTS.
2. Verify `node --version`.
3. Verify `npx --version`.
4. Re-run the MCP add command.

---

### `npx` is missing

Symptoms:

- Node.js exists but `npx` does not.
- MCP command cannot run `@bitbonsai/mcpvault`.

Fix:

1. Verify npm installation.
2. Reinstall or repair Node.js LTS.
3. Verify `npx --version`.
4. Re-run the MCP add command.

---

### MCP was added but is not available

Symptoms:

- `claude mcp list` shows the server, but Claude cannot call it.
- Claude says the MCP tool is unavailable.
- Listing the vault root through MCP fails.

Fix:

1. Ask the user to restart or refresh Claude.
2. Reopen this installer repository.
3. Ask the user to say `continue setup`.
4. Verify the MCP again.

---

### Wrong vault path

Symptoms:

- MCP connects to an empty or unexpected folder.
- Obsidian is opened on a different folder.
- Generated notes do not appear in the user's intended vault.

Fix:

1. Ask the user which folder is opened in Obsidian.
2. Resolve the absolute path.
3. Re-run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[CORRECT_VAULT_PATH]"
```

4. Restart or refresh Claude.
5. Verify the MCP again.

---

### Windows and WSL path mismatch

Symptoms:

- Claude Code runs inside WSL.
- Obsidian runs on Windows.
- The vault path uses Windows format like `C:\Users\...` but Claude Code expects `/mnt/c/Users/...`.
- Claude can create files, but Obsidian does not show them, or the reverse.

Fix:

1. Identify where Claude Code is running: Windows native or WSL.
2. Identify where Obsidian is running.
3. Use a path both environments can access.
4. If using WSL, convert Windows path to WSL path:

```text
C:\Users\Name\Documents\my-second-brain
```

becomes:

```text
/mnt/c/Users/Name/Documents/my-second-brain
```

5. Re-run the MCP add command using the path visible to Claude Code.
6. Open the same folder in Obsidian.

---

## Repair process

When MCP setup fails, follow this repair flow:

```text
1. Identify whether the failure is Node, npx, Claude Code, vault path, restart, environment capability, or MCP server.
2. Fix the earliest failing dependency.
3. Re-run the MCP add command if needed and available.
4. Restart or refresh Claude.
5. Verify the MCP by listing the vault root.
6. Continue setup from the last valid state.
```

Do not restart the whole installation unless the vault path or profile setup is unrecoverable.

If the current environment cannot configure MCP, switch to the correct handoff mode instead of retrying indefinitely.

---

## Safety rules

The MCP should only point to the user's approved vault path.

Do not point the MCP to:

- the user's home directory,
- the whole Documents folder,
- a system folder,
- a folder containing unrelated sensitive files,
- a Git repository unless the user explicitly wants that folder to be their vault.

If the selected folder looks too broad or unsafe, warn the user and ask them to choose a dedicated vault folder.
