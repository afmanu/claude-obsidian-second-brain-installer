# Example Transcript — Claude Co-Work Installation

This example shows the expected behavior when a user tries to install Claude Obsidian Second Brain from Claude Co-Work Desktop.

The goal is not to copy this transcript word for word. The goal is to model the correct flow:

1. Detect installation intent.
2. Detect execution environment.
3. Check local folder access.
4. Check command and MCP capability.
5. Install directly if possible.
6. Use assisted handoff if needed.
7. Avoid pretending installation completed when local access is missing.

---

## Scenario

The user is using Claude Co-Work Desktop.

The user gives Claude this repository and says:

```text
Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

---

## Transcript

### User

```text
Install this repository:
https://github.com/afmanu/claude-obsidian-second-brain-installer
```

### Claude

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

### User

```text
yes
```

### Claude

```text
I am running in Claude Co-Work Desktop mode.

For a Co-Work installation, I need to confirm two things:

1. I can access this installer repository as a workspace folder.
2. I can access or create the folder where your Obsidian vault will live.

Can I access the repository folder and the target parent folder for your vault? [yes / I need help]
```

### User

```text
yes
```

### Claude

```text
Good. I will now check installation capabilities.

I need to verify:
- repository files are readable,
- the vault parent folder is writable,
- command execution is available,
- Node.js and npx can be checked,
- MCP setup is available or can be handed off.

Before I create any test file in the vault parent folder, do I have your approval? [yes / no]
```

### User

```text
yes
```

### Claude

```text
File access is available.

Now I need to check whether command execution and MCP setup are available from this Co-Work session.
```

---

## Path A — Full Co-Work installation succeeds

### Claude

```text
Command execution is available.
Node.js and npx are available.
MCP setup is available.

I can continue with a full Co-Work installation.

Next I will check Obsidian and create or confirm your vault folder.
```

### Claude

```text
Where should your vault live?

Default: ~/Documents/my-second-brain

Choose one:
A) Use default path
B) I want a different path
```

### User

```text
A
```

### Claude

```text
Folder ready at [VAULT_PATH].

Now open Obsidian, choose "Open folder as vault", and select:
[VAULT_PATH]

Say "done" when you have opened it.
```

### User

```text
done
```

### Claude

```text
Next I need to connect Claude to your Obsidian vault so I can read and write notes inside it.

I will run the MCP setup using your approved vault path.
```

### Claude

```text
The MCP connection has been configured.

Restart or refresh Claude so the connection activates.

When you are back, say:
continue setup
```

### User

```text
continue setup
```

### Claude

```text
The Obsidian MCP connection is working. I can now build your vault.

I will run /vault-install.
```

### Claude

```text
What is the main reason you want a second brain? What problem are you trying to solve?
```

### User

```text
I manage client projects and want a place to capture meetings, decisions, proposals, and reusable processes.
```

### Claude

```text
Describe your daily work or life in 2-3 sentences. What do you mostly do?
```

### User

```text
I work with clients, prepare proposals, run meetings, and turn operational problems into AI automations.
```

### Claude

```text
What kind of information do you capture most? Examples: meetings, ideas, code, notes from books, personal goals, tasks, decisions, client notes.
```

### User

```text
Client notes, meeting summaries, process ideas, decisions, and service templates.
```

### Claude

```text
Based on what you told me, I recommend the Consultant profile.

Why:
- You manage client projects.
- You capture meetings, decisions, and proposals.
- You want reusable processes and service templates.

Confidence: High

Recommended structure:
[profile-specific folder tree]

Does this structure work, or would you like to adjust anything?
```

### User

```text
Works for me.
```

### Claude

```text
What language would you like for your vault?

A) English — all folders and notes in English
B) Spanish — todas las carpetas y notas en español
C) Mixed — English structure, Spanish note content
```

### User

```text
C
```

### Claude

```text
Here is what I will build:

Profile: Consultant
Language: Mixed
Structure:
[final folder list]

Core vault skills to install:
- /second-brain-capture
- /link-finder
- /vault-synthesis
- /next-steps-ai
- /explore-skills

I will also install:
- CLAUDE.md inside the final vault
- .claude/vault-profile.md
- docs/skills-catalog.md
- docs/system-contracts.md

Ready to build? [yes / adjust]
```

### User

```text
yes
```

### Claude

```text
Your second brain is ready.

Profile: Consultant
Language: Mixed
Vault path: [VAULT_PATH]

What was built:
- Personalized folder structure
- Home.md
- 00_START_HERE.md
- Profile-aware CLAUDE.md
- .claude/vault-profile.md
- Core vault skills
- Skills catalog
- System contracts reference
- Hub notes for your selected profile

From now on, open your vault directly in Claude:

claude "[VAULT_PATH]"

Try your first capture now:
Use /second-brain-capture and tell me something you learned, decided, or want to remember.
```

---

## Path B — Co-Work cannot configure MCP

If Co-Work can access files but cannot configure MCP, use assisted handoff.

### Claude

```text
I can access and prepare local files from Co-Work, but this session does not appear to have enough local MCP access to configure the Obsidian MCP directly.

I will switch to assisted installation mode.

You can continue from Co-Work for file preparation, but MCP setup needs to be completed from Claude Code Terminal.
```

### Claude

```text
Please open Claude Code Terminal and run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

If you are on Windows native and the command fails, run:

```bash
claude mcp add obsidian-vault -- cmd /c npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

After that, restart or refresh Claude and say:
continue setup
```

### User

```text
continue setup
```

### Claude

```text
I will verify the MCP connection before continuing.

If the MCP is connected, I will run /vault-install.
If it is not connected, I will diagnose using docs/mcp-setup.md and TROUBLESHOOTING.md.
```

---

## Path C — Co-Work has no local folder access

If Co-Work cannot access local folders, do not pretend the install can continue.

### Claude

```text
I can guide this setup from Co-Work, but I do not currently have enough local folder access to install the vault directly from this session.

The correct path is to continue from Claude Code Terminal.

Please run:

```bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
```

When Claude opens the repository, it will read BOOTSTRAP.md and CLAUDE.md and start the setup workflow.
```

---

## What this example demonstrates

Correct behavior:

- Claude treats vague install intent as setup intent.
- Claude detects Co-Work mode.
- Claude checks local folder access before writing.
- Claude checks whether command execution and MCP are available.
- Claude installs directly when possible.
- Claude switches to assisted handoff when needed.
- Claude does not pretend mobile/app/Co-Work can do things they cannot do.
- Claude resumes from `continue setup` instead of restarting.

Incorrect behavior:

- Summarizing the repo instead of installing.
- Asking the user for a better prompt.
- Running `/vault-install` before MCP verification.
- Pretending mobile installed the local vault directly.
- Writing outside the approved vault path.
- Starting over after restart without checking setup state.
