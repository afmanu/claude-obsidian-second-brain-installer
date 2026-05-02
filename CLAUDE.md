# obsidian-second-brain

**When a user opens this repo, immediately start the setup wizard. Do not wait for them to ask.**

Say this:

```
👋 Hi! I'm going to help you build your second brain in Obsidian.

I'll check what's installed on your computer and handle everything
step by step. You just answer my questions.

This takes about 20 minutes. Ready? [yes / not now]
```

If yes → run the Setup Wizard below.
If "not now" → say "No problem — say 'start setup' whenever you're ready."

---

## Setup Wizard

### CHECK 1 — Obsidian

Detect OS and check if Obsidian is installed:
- Mac: `ls /Applications/Obsidian.app 2>/dev/null && echo "found" || echo "not found"`
- Windows: `ls "$LOCALAPPDATA/Obsidian" 2>/dev/null && echo "found" || echo "not found"`
- Linux: `which obsidian 2>/dev/null && echo "found" || echo "not found"`

**If found:** ✓ Obsidian is already installed.

**If not found:**
Check Homebrew: `which brew 2>/dev/null`
- If Homebrew available: run `brew install --cask obsidian` → confirm ✓ Obsidian installed.
- If no Homebrew: guide the user to https://obsidian.md to download and install manually. Wait for "done".

---

### CHECK 2 — Create the vault folder

Ask:
```
Where should your vault live? I can create it now.
Default: ~/Documents/my-second-brain  [yes / I want a different path]
```

If yes: run `mkdir -p ~/Documents/my-second-brain`, store as [VAULT_PATH].
If custom: ask for the path, use that as [VAULT_PATH].
Always resolve ~ to absolute path: run `echo ~/Documents/my-second-brain`.

Then say:
```
✓ Folder ready at [VAULT_PATH]

Now open Obsidian → "Open folder as vault" → select [VAULT_PATH]
Say "done" when you've opened it.
```
Wait for "done".

---

### CHECK 3 — Node.js

Run: `node --version 2>/dev/null || echo "not found"`

If found: ✓ Node.js is installed.
If not found:
- Homebrew available: run `brew install node` → ✓ Node.js installed.
- No Homebrew: guide to https://nodejs.org → LTS download. Wait for "done". Verify: `node --version`.

---

### CHECK 4 — Connect the MCP

Say:
```
Almost done — I need one permission to write notes directly into your vault.
I'm going to run a command. It needs your approval.
```

Run:
```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Then say:
```
✓ Connection configured.

Restart Claude Code now so the connection activates.
Close and reopen, or press Cmd+R (Mac) / Ctrl+R (Windows).

When you're back, open this same folder and say "continue setup".
```

---

### AFTER RESTART — when user says "continue setup"

1. Verify MCP by calling list_directory on vault root.
2. If connected: say `✓ Connected to your vault. Let's build it!` → run /vault-install immediately.
3. If not connected: troubleshoot — check vault path, re-run `claude mcp add` command.

---

## Available skills

| Command | Purpose |
|---|---|
| `/vault-install` | Build the personalized vault (runs after setup wizard) |
| `/second-brain-capture` | Capture insight/solution/decision as a linked note |
| `/link-finder` | Find orphan notes and suggest connections |
| `/vault-synthesis` | Generate synthesis report of the vault |
| `/next-steps-ai` | Suggest next steps by impact |
| `/explore-skills` | Browse and build additional skills |

---

## Rules for all skills

- **MCP for notes**: use `obsidian-vault` MCP to read/write Obsidian notes
- **Write tool for config**: use Write tool directly for `.claude/commands/` and `CLAUDE.md` — filesystem files, not Obsidian notes
- **Propose before creating**: show title, type, folder — wait for confirmation
- **Auto-link**: after every note, find 3-5 related notes and add wikilinks
- **Never delete** without explicit confirmation
- **Use real names**: always use the user's actual project/area names
- **Match the user's language**: if they write in Spanish, respond in Spanish
