# Claude Co-Work Installation Guide

This guide defines how Claude Obsidian Second Brain should be installed from Claude Co-Work Desktop.

Co-Work installation is supported, but it depends on local folder access and available execution permissions.

---

## Goal

When a user says something like:

```text
Quiero instalar este sistema de segundo cerebro:

https://github.com/afmanu/claude-obsidian-second-brain-installer
```

from Claude Co-Work, Claude should not merely summarize the repository.

Claude should:

1. Detect installation intent.
2. Confirm that it is running in Co-Work Desktop.
3. Check whether the required folders are accessible.
4. Check whether local command execution and MCP setup are available.
5. Install directly if possible.
6. If not possible, switch to assisted handoff mode.

---

## Co-Work requirements

For a full Co-Work installation, Claude needs access to:

```text
1. The installer repository folder.
2. A target parent folder where the Obsidian vault will be created.
3. Permission to create and modify files in the target vault folder.
4. Ability to check or guide Obsidian installation.
5. Ability to check or guide Node.js and npx installation.
6. Ability to configure or guide MCP setup.
```

If any required capability is unavailable, do not fail silently. Explain the missing capability and switch to the safest fallback.

---

## Automatic Co-Work start

The user has already requested installation. Do not ask whether they want to continue.

Proceed in this order:

1. Try to access the repository from the supplied GitHub URL.
2. Read BOOTSTRAP.md and docs/install-modes.md.
3. Confirm from the current session that the runtime is Co-Work Desktop.
4. Inspect available folder, command, and MCP capabilities without writing files.
5. If the repository cannot be accessed from the URL, ask the user to download or attach the repository folder. This is a capability fallback, not a request for a better prompt.
6. If the target vault parent folder is unknown, ask the user to select one dedicated folder.
7. Request approval immediately before the first write, package installation, configuration change, or test-file creation.

Use this concise first message:

~~~text
I found the installer and I am checking the Co-Work environment now. I will ask you only for the destination folder, personalization choices, or approval before making changes.
~~~

Do not repeat the repository instructions to the user unless a capability is missing.

---

## Capability check

Before installation, inspect these capabilities directly when possible. Ask only about an item that cannot be determined from the current session:

```text
1. Can I read README.md, INSTALL.md, CLAUDE.md, and BOOTSTRAP.md?
2. Can I create a test file in the target parent folder?
3. Can I delete or clean up that test file after confirmation?
4. Can I run shell commands?
5. Can I check Node.js and npx?
6. Can I configure local MCP?
```

If a test file is used, ask for approval before creating it.

Do not create test files in sensitive or broad folders such as the user's home directory.

---

## Installation paths

### Path 1 — Full Co-Work installation

Use this path if Co-Work can:

- read/write local files,
- create folders,
- run required checks,
- configure MCP or access the configured MCP.

Proceed with the same installation logic as `CLAUDE.md`:

1. Check Obsidian.
2. Select/create vault folder.
3. Check Node.js and npx.
4. Configure MCP.
5. Verify MCP.
6. Run `/vault-install`.
7. Verify final vault.
8. Handoff to the final vault.

---

### Path 2 — Co-Work assisted installation

Use this path if Co-Work can read/write files but cannot execute some commands or configure MCP directly.

Claude should still help by:

1. Preparing the target vault folder if file access exists.
2. Creating or copying non-MCP files where possible.
3. Giving the user exact terminal commands for unavailable steps.
4. Waiting for the user to confirm completion.
5. Continuing from the next setup state.

For MCP setup, provide this command:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

On Windows native, if the standard command fails, provide this command:

```bash
claude mcp add obsidian-vault -- cmd /c npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

---

### Path 3 — Handoff to Claude Code Terminal

Use this path if Co-Work cannot access local folders or cannot perform enough of the installation safely.

Say:

```text
I can guide this setup from Co-Work, but I do not currently have enough local access to install the vault directly from this session.

Please open Claude Code in your terminal and run the commands below.

When Claude opens the repository, it will read BOOTSTRAP.md and CLAUDE.md and start the setup wizard.
```

Then provide:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

Do not present this as a failure. Present it as the correct execution mode for the user's environment.

---

## Folder access rules

Co-Work should only operate inside approved folders.

Allowed:

```text
- installer repository folder
- selected vault folder
- selected parent folder for the vault
```

Avoid:

```text
- entire home directory
- entire Documents folder unless the user explicitly approves it
- system folders
- folders containing unrelated sensitive files
```

If the user selects a broad folder, recommend creating a dedicated vault folder.

---

## MCP rules in Co-Work

If MCP setup is available in Co-Work, follow `docs/mcp-setup.md`.

If MCP setup is unavailable:

1. Explain that local MCP setup may require Claude Code Terminal or local developer settings.
2. Provide the exact command.
3. Ask the user to run it in Claude Code Terminal.
4. Ask them to return and say `continue setup`.
5. Use `specs/setup-state-machine.md` to resume.

Do not run `/vault-install` until MCP is verified.

---

## Co-Work recovery

If Co-Work loses context, ask the user to say:

```text
continue setup
```

Then read:

```text
specs/setup-state-machine.md
TROUBLESHOOTING.md
docs/mcp-setup.md
```

Identify the latest valid state and continue from there.

---

## Success criteria

A Co-Work installation is successful when the final vault contains:

```text
CLAUDE.md
Home.md
00_START_HERE.md
docs/skills-catalog.md
docs/system-contracts.md
.claude/vault-profile.md
.claude/commands/second-brain-capture.md
.claude/commands/link-finder.md
.claude/commands/vault-synthesis.md
.claude/commands/next-steps-ai.md
.claude/commands/explore-skills.md
[personalized folders]
```

Then tell the user how to continue using the vault from Claude Code or Co-Work.
