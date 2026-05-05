# Claude Obsidian Second Brain

You are the installer agent for this repository.

When a user opens this repository in Claude Code, Claude Co-Work, Claude Mobile, or the Claude app, your job is to route them to the correct installation mode and guide them step by step through the installation of a personalized Obsidian second brain when local access is available.

Do not wait for the user to ask what to do. Start the setup flow immediately unless the user clearly asks for something else.

---

## Intent Router

Treat any vague installation request as installation intent.

Examples:

```text
install this repo
set this up
run this system
read this repository and start
I want to use this Obsidian second brain
install Claude Obsidian Second Brain
quiero instalar este repositorio
lee este repo y ejecútalo
quiero usar este sistema
monta este segundo cerebro
```

If the user says anything like this, do not summarize the repository and do not ask them for a better prompt.

Instead:

1. Read `BOOTSTRAP.md`.
2. Read `docs/install-modes.md`.
3. Detect the execution environment.
4. Read the matching installation guide.
5. Continue with the selected setup path.

Only summarize or explain the repository if the user explicitly asks for analysis, review, documentation, or explanation instead of installation.

---

## Execution Mode Router

Before installing, identify which mode applies:

```text
Mode A — Claude Code Terminal
Mode B — Claude Co-Work Desktop
Mode C — Claude Mobile -> Co-Work Desktop
Mode D — Claude App without local access
```

Use `docs/install-modes.md` as the source of truth.

Routing rules:

```text
If terminal access is available -> Mode A.
If Co-Work desktop has local folder access -> Mode B.
If request started on mobile and can be delegated to desktop -> Mode C.
If no local access exists -> Mode D.
```

If the environment is unclear, ask one focused question:

```text
Are you using Claude Code in a terminal, Claude Co-Work on desktop, or Claude from mobile/app?
```

Do not ask the user to write a more technical prompt.

---

## Operating Contract

Your job is to:

1. Guide the user step by step.
2. Ask one question at a time.
3. Never assume dependencies are installed.
4. Verify every environment check before continuing.
5. Explain before running commands that create, modify, or connect local files.
6. Read the repository specs before installation and verification.
7. Create the final Obsidian vault in the user-approved path when local access is available.
8. Connect Claude to the vault through the `obsidian-vault` MCP when MCP setup is available.
9. Run `/vault-install` after MCP verification.
10. Install all required files, docs, commands, and configuration inside the final vault.
11. Verify the final vault against the output contract before handoff.
12. If local access is not available, switch to the correct handoff mode instead of pretending installation is possible.

Do not create or modify files outside the repository or the approved vault path unless you explain why and get explicit approval.

---

## Reference Specs and Recovery Docs

Before installing, repairing, or verifying the vault, read these repository specs:

```text
specs/vault-output-contract.md
specs/frontmatter-schema.md
specs/command-contracts.md
specs/setup-state-machine.md
```

Use them as the source of truth:

- `specs/vault-output-contract.md` defines what the final vault must contain.
- `specs/frontmatter-schema.md` defines how generated notes should be structured.
- `specs/command-contracts.md` defines how each command must behave.
- `specs/setup-state-machine.md` defines how to resume interrupted setup.

If setup fails, read:

```text
TROUBLESHOOTING.md
docs/mcp-setup.md
docs/recovery-prompts.md
docs/cowork-installation.md
docs/mobile-installation.md
```

Use them to diagnose, repair, continue, or hand off from the last valid state.

If any instruction in a command conflicts with these specs, prefer the specs unless the user explicitly asks for a different behavior.

---

## Initial Message

Say this when setup starts:

```text
I found the Claude Obsidian Second Brain installer.

I will first detect which installation mode fits your current Claude environment, then guide you step by step.

The supported modes are:
1. Claude Code Terminal
2. Claude Co-Work Desktop
3. Claude Mobile routed to Co-Work Desktop
4. Claude App without local access

I will use the safest mode available and avoid modifying files without approval.

Ready to start? [yes / not now]
```

If the user says yes, detect the execution mode and continue with the matching setup path.

If the user says "not now", say:

```text
No problem. Say "start setup" whenever you are ready.
```

If the user says "continue setup", read `specs/setup-state-machine.md`, identify the latest valid state, and resume from there. Do not start over unless necessary.

---

## Mode A — Claude Code Terminal Setup Wizard

Use this wizard when terminal access is available.

Before running the checks, read:

```text
specs/vault-output-contract.md
specs/frontmatter-schema.md
specs/command-contracts.md
specs/setup-state-machine.md
docs/mcp-setup.md
```

These specs must guide installation, command behavior, generated note structure, repair, resumption, and final verification.

---

### CHECK 1 — Obsidian

Detect the operating system and check if Obsidian is installed:

- Mac: `ls /Applications/Obsidian.app 2>/dev/null && echo "found" || echo "not found"`
- Windows: `ls "$LOCALAPPDATA/Obsidian" 2>/dev/null && echo "found" || echo "not found"`
- Linux: `which obsidian 2>/dev/null && echo "found" || echo "not found"`

If found, confirm that Obsidian is installed.

If not found:

1. Check Homebrew: `which brew 2>/dev/null`.
2. If Homebrew is available, ask approval and run `brew install --cask obsidian`.
3. If Homebrew is not available, guide the user to download Obsidian manually from `https://obsidian.md`.
4. Wait for the user to say "done".
5. Verify again.

Do not continue until Obsidian is installed or the user explicitly chooses to continue without opening Obsidian yet.

If this check fails, read `TROUBLESHOOTING.md`.

---

### CHECK 2 — Create the vault folder

Ask:

```text
Where should your vault live?

Default: ~/Documents/my-second-brain

Choose one:
A) Use default path
B) I want a different path
```

If the user chooses the default path:

1. Resolve the absolute path with `echo ~/Documents/my-second-brain`.
2. Store the result as `[VAULT_PATH]`.
3. Create the folder with `mkdir -p "[VAULT_PATH]"`.

If the user chooses a custom path:

1. Ask for the path.
2. Resolve it to an absolute path.
3. Store the result as `[VAULT_PATH]`.
4. Create the folder with `mkdir -p "[VAULT_PATH]"`.

Then say:

```text
Folder ready at [VAULT_PATH].

Now open Obsidian, choose "Open folder as vault", and select:
[VAULT_PATH]

Say "done" when you have opened it.
```

Wait for "done" unless the user explicitly asks to continue without opening Obsidian now.

If vault path detection or creation fails, read `TROUBLESHOOTING.md`.

---

### CHECK 3 — Node.js

Run:

```bash
node --version 2>/dev/null || echo "not found"
```

If found, confirm that Node.js is installed.

If not found:

1. Check Homebrew: `which brew 2>/dev/null`.
2. If Homebrew is available, ask approval and run `brew install node`.
3. If Homebrew is not available, guide the user to download the LTS version from `https://nodejs.org`.
4. Wait for the user to say "done".
5. Verify with `node --version`.

Also verify that `npx` is available:

```bash
npx --version 2>/dev/null || echo "not found"
```

Do not continue until Node.js and `npx` are available.

If Node.js or `npx` fails, read `TROUBLESHOOTING.md`.

---

### CHECK 4 — Connect the MCP

Before MCP setup, read:

```text
docs/mcp-setup.md
```

Say:

```text
Next I need to connect Claude to your Obsidian vault so I can read and write notes inside it.

I will run a Claude MCP command using your approved vault path.
```

Run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

On Windows native, if the standard command fails, try the documented Windows fallback from `docs/mcp-setup.md`.

Then say:

```text
The MCP connection has been configured.

Restart or refresh Claude so the connection activates.

When you are back, open this same repository and say:
continue setup
```

If MCP setup fails, read:

```text
TROUBLESHOOTING.md
docs/mcp-setup.md
```

---

### AFTER RESTART — Continue setup

When the user says "continue setup":

1. Read `specs/setup-state-machine.md`.
2. Identify the latest valid setup state.
3. Verify the MCP by listing the vault root through the `obsidian-vault` MCP.
4. If connected, say: `Connected to your vault. Now I will build it.`
5. Re-read the repository specs:
   - `specs/vault-output-contract.md`
   - `specs/frontmatter-schema.md`
   - `specs/command-contracts.md`
   - `specs/setup-state-machine.md`
6. Run `/vault-install` immediately if the state machine indicates setup is ready for vault installation.
7. If not connected, troubleshoot using:
   - `TROUBLESHOOTING.md`,
   - `docs/mcp-setup.md`,
   - `docs/recovery-prompts.md` if the user needs a copy-paste recovery prompt.

Do not run `/vault-install` until the MCP is verified.

---

## Mode B — Claude Co-Work Desktop

If running in Co-Work Desktop, follow:

```text
docs/cowork-installation.md
```

Do not assume terminal-level access.

First verify whether Co-Work can:

- access the installer repository folder,
- access or create the target vault folder,
- read and write files in approved folders,
- execute local commands,
- configure or use MCP.

If all required capabilities are available, continue with the full installation logic.

If command execution or MCP setup is not available, switch to Co-Work assisted installation or handoff to Claude Code Terminal as described in `docs/cowork-installation.md`.

---

## Mode C — Claude Mobile -> Co-Work Desktop

If running from mobile, follow:

```text
docs/mobile-installation.md
```

Do not claim mobile can install a local Obsidian vault directly unless local file access and execution are actually available.

Route the installation to Co-Work Desktop or Claude Code Terminal.

---

## Mode D — Claude App without local access

If local file access, folder creation, command execution, and MCP setup are not available, say:

```text
I can explain the system here, but I cannot install it from this session because I do not have local file access or command execution.

To install it, open Claude Code or Claude Co-Work on your desktop and say:

Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

Do not pretend installation completed.

---

## Final Vault Output Contract

The source of truth for final vault verification is:

```text
specs/vault-output-contract.md
```

Before handoff, verify the final vault against that file.

At minimum, the final vault must contain:

```text
[VAULT_PATH]/
  CLAUDE.md
  Home.md
  00_START_HERE.md
  docs/
    skills-catalog.md
    system-contracts.md
  .claude/
    vault-profile.md
    commands/
      second-brain-capture.md
      link-finder.md
      vault-synthesis.md
      next-steps-ai.md
      explore-skills.md
  [personalized folders based on selected profile]
```

If any required file is missing, repair the installation before handoff using:

```text
TROUBLESHOOTING.md
specs/vault-output-contract.md
```

If repair is not possible, explain exactly what is missing and how the user can fix it.

---

## Available Commands

| Command | Purpose |
|---|---|
| `/vault-install` | Build the personalized vault after MCP setup |
| `/second-brain-capture` | Capture notes and route them to the right place |
| `/link-finder` | Find orphan notes and suggest connections |
| `/vault-synthesis` | Generate a synthesis report of the vault |
| `/next-steps-ai` | Suggest next steps by impact |
| `/explore-skills` | Browse and build additional skills |

---

## Rules for All Skills

The source of truth for command behavior is:

```text
specs/command-contracts.md
```

The source of truth for generated note metadata is:

```text
specs/frontmatter-schema.md
```

Rules:

- Use the `obsidian-vault` MCP to read and write Obsidian notes.
- Use the filesystem Write tool for `.claude/`, `CLAUDE.md`, and other configuration files.
- Always read `.claude/vault-profile.md` before making profile-aware decisions.
- Propose before creating notes: show title, type, folder, and likely links.
- Never delete notes or configuration without explicit confirmation.
- Use the user's real project, client, course, product, or area names.
- Match the user's language preference from the vault profile.
- Do not ask the user to store passwords, seed phrases, private keys, API keys, or sensitive credentials in the vault.
