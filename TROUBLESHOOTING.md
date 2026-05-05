# Troubleshooting

This document defines recovery paths for Claude Obsidian Second Brain installation failures.

Claude must read this file whenever setup fails, verification fails, the user returns after an interrupted installation, or the current execution environment cannot complete the install directly.

---

## Recovery principle

Do not restart the full setup unless necessary.

When something fails:

1. Identify the current execution mode.
2. Identify the current setup state.
3. Identify the failed component.
4. Fix the earliest failing dependency.
5. Continue from the last valid state.
6. Verify before moving forward.

Use:

```text
docs/install-modes.md
specs/setup-state-machine.md
```

if the execution mode or installation state is unclear.

Use:

```text
docs/mcp-setup.md
```

for MCP-specific diagnosis and repair.

Use:

```text
docs/cowork-installation.md
docs/mobile-installation.md
```

for Co-Work or mobile-specific recovery.

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
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

### Fix

If Git is installed, run:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

If Git is missing, ask the user to install Git or download the repository as a ZIP from GitHub.

Do not continue until `BOOTSTRAP.md`, `README.md`, `INSTALL.md`, and `CLAUDE.md` can be read.

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

On Windows native, if needed:

```bash
claude mcp add obsidian-vault -- cmd /c npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Restart or refresh Claude before verification.

If MCP setup is not available in the current environment, switch to the correct handoff mode using `docs/install-modes.md`.

---

## 7. Claude was restarted and setup context was lost

### Symptoms

- The user returns after restart.
- Claude does not know the last completed step.
- The user says `continue setup`, but state is unclear.

### Fix

Read:

```text
specs/setup-state-machine.md
docs/install-modes.md
```

Then inspect:

```text
- Which execution mode is active?
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
3. Restart or refresh Claude.
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

Use a path visible to the environment running Claude.

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
[VAULT_PATH]/docs/system-contracts.md
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

## 12. Co-Work cannot access the installer repository folder

### Symptoms

- Co-Work cannot read `BOOTSTRAP.md`.
- Co-Work cannot read `CLAUDE.md`.
- Co-Work only sees the GitHub URL but no local workspace folder.
- Co-Work summarizes the repo but cannot modify local files.

### Fix

Read:

```text
docs/cowork-installation.md
```

Then ask the user to attach or open the installer repository folder as a Co-Work workspace folder.

If the user has not cloned the repository locally, provide the terminal fallback:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

If Co-Work cannot use local folders in the current session, switch to Claude Code Terminal mode.

---

## 13. Co-Work cannot access or create the target vault folder

### Symptoms

- Co-Work can read the repo but cannot create the vault folder.
- File creation fails.
- The user has not attached or approved the parent folder.
- Co-Work says it lacks access to the destination.

### Fix

1. Ask the user to select or attach a dedicated parent folder for the vault.
2. Avoid broad folders like the entire home directory.
3. Ask approval before creating a small test file if needed.
4. If write access works, continue with Co-Work installation.
5. If write access does not work, switch to assisted handoff or Claude Code Terminal.

Suggested message:

```text
I can continue from Co-Work if you give me access to the folder where the vault should live. Otherwise, I will hand this off to Claude Code Terminal.
```

---

## 14. Co-Work cannot execute commands

### Symptoms

- Co-Work can edit files but cannot run shell commands.
- Node.js, npx, or Git checks cannot be executed.
- MCP setup cannot be run from the Co-Work session.

### Fix

Use Co-Work assisted installation:

1. Continue file-based steps from Co-Work if safe.
2. Provide exact terminal commands for unavailable checks or MCP setup.
3. Wait for the user to confirm completion.
4. Continue from the next setup state.

If MCP setup is blocked, provide:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

If the user is on Windows native and the standard command fails, provide:

```bash
claude mcp add obsidian-vault -- cmd /c npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

---

## 15. Co-Work cannot configure local MCP

### Symptoms

- Co-Work can access files but not MCP settings.
- Local MCP is disabled.
- MCP server cannot be added from Co-Work.
- Admin or app settings restrict local extensions/MCP.

### Fix

Read:

```text
docs/cowork-installation.md
docs/mcp-setup.md
```

Then switch to assisted MCP setup:

1. Explain that the vault files can be prepared from Co-Work, but MCP setup requires Claude Code Terminal or local settings.
2. Provide the exact MCP command.
3. Ask the user to run it from Claude Code Terminal.
4. Ask them to restart or refresh Claude.
5. Resume with `continue setup`.

Do not retry indefinitely from Co-Work.

---

## 16. Mobile session cannot install locally

### Symptoms

- User starts from the Claude mobile app.
- Claude cannot access local folders.
- Claude cannot run commands.
- Claude cannot configure MCP.

### Fix

Read:

```text
docs/mobile-installation.md
```

Tell the user:

```text
This installation needs local file access on your computer. From mobile, I can start or coordinate the task, but the vault must be created from Claude Co-Work Desktop or Claude Code Terminal.
```

Then offer:

```text
A) Send the task to Claude Co-Work Desktop
B) Continue from Claude Code Terminal
```

Do not pretend the mobile session installed the local vault.

---

## 17. Mobile-to-Co-Work handoff fails

### Symptoms

- The user starts from mobile but desktop Co-Work does not receive or continue the task.
- The desktop computer is asleep or offline.
- Claude Desktop is not open.
- Co-Work cannot access the local folders.

### Fix

Ask the user to confirm:

```text
1. Is your desktop computer awake and online?
2. Is Claude Desktop open?
3. Is Co-Work available?
4. Can Co-Work access the installer repository and vault parent folder?
```

If not, switch to terminal fallback:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

---

## 18. Claude App without local access

### Symptoms

- Claude has no local file access.
- Claude cannot create folders.
- Claude cannot run commands.
- Claude cannot configure MCP.

### Fix

Say:

```text
I can explain the system here, but I cannot install it from this session because I do not have local file access or command execution.

To install it, open Claude Code or Claude Co-Work on your desktop and say:

Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Do not claim installation is possible in that session.

---

## 19. User wants to start over

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
I was installing Claude Obsidian Second Brain and something failed. Please read TROUBLESHOOTING.md, docs/install-modes.md, inspect the current execution mode and setup state, identify the last completed step, and continue from there without starting over unless necessary.
```
