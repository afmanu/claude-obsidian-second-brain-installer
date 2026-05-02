# Troubleshooting

This document defines recovery paths for Claude Obsidian Second Brain installation failures.

Claude must read this file whenever setup fails, verification fails, or the user returns after an interrupted installation.

---

## Recovery principle

Do not restart the full setup unless necessary.

When something fails:

1. Identify the current setup state.
2. Identify the failed component.
3. Fix the earliest failing dependency.
4. Continue from the last valid state.
5. Verify before moving forward.

Use:

```text
specs/setup-state-machine.md
```

if the installation state is unclear.

Use:

```text
docs/mcp-setup.md
```

for MCP-specific diagnosis and repair.

---

## 1. Claude cannot access or clone the repository

### Symptoms

- Repository cannot be cloned.
- GitHub URL fails.
- Claude cannot read `README.md` or `CLAUDE.md`.
- `git clone` returns an error.

### Diagnosis

Check:

```bash
git --version
```

Confirm the repository URL:

```text
https://github.com/afmanu/obsidian-sppf-vault
```

### Fix

If Git is installed, run:

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
claude .
```

If Git is missing, ask the user to install Git or download the repository as a ZIP from GitHub.

Do not continue until `README.md` and `CLAUDE.md` can be read.

---

## 2. Git is not installed

### Symptoms

- `git --version` returns not found.
- `git clone` fails because Git is unavailable.

### Fix

Guide the user to install Git for their operating system.

After installation, verify:

```bash
git --version
```

Then clone the repository again.

---

## 3. Obsidian is not installed

### Symptoms

- Obsidian app is not found.
- The user cannot open the vault folder in Obsidian.

### Diagnosis

Mac:

```bash
ls /Applications/Obsidian.app 2>/dev/null && echo "found" || echo "not found"
```

Windows:

```bash
ls "$LOCALAPPDATA/Obsidian" 2>/dev/null && echo "found" || echo "not found"
```

Linux:

```bash
which obsidian 2>/dev/null && echo "found" || echo "not found"
```

### Fix

If Homebrew is available on macOS:

```bash
brew install --cask obsidian
```

Otherwise, guide the user to install Obsidian manually from:

```text
https://obsidian.md
```

After installation, ask the user to open the selected vault folder in Obsidian.

---

## 4. Node.js is not installed

### Symptoms

- `node --version` returns not found.
- `npx --version` returns not found.
- MCP installation command fails.

### Diagnosis

```bash
node --version
npx --version
```

### Fix

Install Node.js LTS.

If Homebrew is available:

```bash
brew install node
```

Otherwise, guide the user to:

```text
https://nodejs.org
```

After installation, verify:

```bash
node --version
npx --version
```

Then continue with MCP setup.

---

## 5. `npx` is not available

### Symptoms

- Node.js is installed but `npx` is missing.
- MCP package cannot be launched.

### Diagnosis

```bash
node --version
npm --version
npx --version
```

### Fix

Repair or reinstall Node.js LTS.

Then verify:

```bash
npx --version
```

Do not run the MCP command until `npx` works.

---

## 6. MCP setup fails

### Symptoms

- `claude mcp add` fails.
- MCP server does not appear.
- Claude cannot read or write notes in the vault.
- The MCP tool is unavailable after setup.

### Fix

Read and follow:

```text
docs/mcp-setup.md
```

Common checks:

```bash
node --version
npx --version
claude mcp list
ls "[VAULT_PATH]"
```

Then re-run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Restart or refresh Claude Code before verification.

---

## 7. Claude Code was restarted and setup context was lost

### Symptoms

- The user returns after restart.
- Claude does not know the last completed step.
- The user says `continue setup`, but state is unclear.

### Fix

Read:

```text
specs/setup-state-machine.md
```

Then inspect:

```text
- Does [VAULT_PATH] exist?
- Is Obsidian installed?
- Is Node.js installed?
- Is npx available?
- Does claude mcp list show obsidian-vault?
- Can the MCP list the vault root?
- Does [VAULT_PATH]/.claude/vault-profile.md exist?
- Does [VAULT_PATH]/Home.md exist?
```

Continue from the latest valid state.

Do not start over unless the user requests it or the setup is unrecoverable.

---

## 8. Wrong vault path

### Symptoms

- Files are created but not visible in Obsidian.
- Obsidian shows a different vault than Claude is modifying.
- MCP connects to an empty folder.

### Diagnosis

Ask the user to confirm the folder currently opened in Obsidian.

Check the path Claude is using:

```bash
ls "[VAULT_PATH]"
```

### Fix

If the path is wrong:

1. Resolve the correct absolute path.
2. Re-run the MCP add command with the correct path.
3. Restart or refresh Claude Code.
4. Verify the MCP.
5. Continue setup.

---

## 9. Windows or WSL path mismatch

### Symptoms

- Claude Code runs in WSL.
- Obsidian runs on Windows.
- Paths differ between `C:\Users\...` and `/mnt/c/Users/...`.
- Files are created in one environment but not visible in the other.

### Fix

Read:

```text
docs/mcp-setup.md
```

Use a path visible to the environment running Claude Code.

Example conversion:

```text
C:\Users\Name\Documents\my-second-brain
```

becomes:

```text
/mnt/c/Users/Name/Documents/my-second-brain
```

Make sure Obsidian opens the same physical folder.

---

## 10. Final vault is missing files

### Symptoms

- Installation completes but expected files are missing.
- `/explore-skills` cannot find `docs/skills-catalog.md`.
- Claude does not follow vault-specific behavior after handoff.
- Commands are missing from `.claude/commands/`.

### Diagnosis

Read:

```text
specs/vault-output-contract.md
```

Verify required files:

```text
[VAULT_PATH]/CLAUDE.md
[VAULT_PATH]/Home.md
[VAULT_PATH]/00_START_HERE.md
[VAULT_PATH]/docs/skills-catalog.md
[VAULT_PATH]/.claude/vault-profile.md
[VAULT_PATH]/.claude/commands/second-brain-capture.md
[VAULT_PATH]/.claude/commands/link-finder.md
[VAULT_PATH]/.claude/commands/vault-synthesis.md
[VAULT_PATH]/.claude/commands/next-steps-ai.md
[VAULT_PATH]/.claude/commands/explore-skills.md
```

### Fix

Recreate missing generated files from the installer repository.

Do not overwrite user-modified files without confirmation.

If a file exists but may be modified, ask:

```text
This file already exists and may contain changes. Do you want me to overwrite it, keep it, or create a backup copy first?
```

---

## 11. `/vault-install` was run before MCP verification

### Symptoms

- Notes cannot be created through MCP.
- Home or onboarding notes fail to create.
- Claude writes config files but cannot write Obsidian notes.

### Fix

1. Stop `/vault-install`.
2. Read `docs/mcp-setup.md`.
3. Verify the MCP.
4. Resume `/vault-install` from the failed build step.

Do not restart from diagnosis unless needed.

---

## 12. User wants to start over

### Rule

Starting over may delete or overwrite useful setup files.

Before starting over, ask:

```text
Do you want to start over in a new empty vault folder, or repair the current one?
```

Recommended approach:

- Use a new vault folder for a clean reinstall.
- Do not delete the old vault unless the user explicitly requests deletion.

---

## Standard recovery prompt

If the user is stuck, they can paste:

```text
I was installing Claude Obsidian Second Brain and something failed. Please read TROUBLESHOOTING.md, inspect the current setup state, identify the last completed step, and continue from there without starting over unless necessary.
```
