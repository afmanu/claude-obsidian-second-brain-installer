# 🧠 obsidian-second-brain

> Build your second brain in Obsidian, guided step by step by Claude Code.

Clone this repo, follow 3 setup steps, and run `/vault-install`. Claude will ask you about your projects and areas, then build your personalized vault structure automatically — folders, hub notes, knowledge base, and all. Skills are installed directly in your vault so you never need this repo again.

---

## What you get

### Core skills (installed automatically)

| Skill | What it does |
|---|---|
| `/second-brain-capture` | Capture an insight, decision, or solution → linked note in seconds |
| `/link-finder` | Find orphan notes and suggest connections with confidence scores |
| `/vault-synthesis` | Generate a synthesis report: patterns, insights, recommendations |
| `/next-steps-ai` | Suggest your next 3-5 actions ordered by impact |
| `/explore-skills` | Browse the skills catalog and build new skills on demand |

### Skills catalog

`/explore-skills` opens a catalog of additional skills you can build at any time:

- `/forgotten-notes` — resurface old notes by relevance
- `/decision-tracker` — audit past decisions and success rates
- `/daily-note` — create today's note from a template
- `/project-health` — flag stalled projects
- `/weekly-review` — guided weekly review
- `/capture-from-url` — turn any URL into a vault note
- `/meeting-recap` — structure raw meeting notes
- *...and any skill you design yourself*

---

## Setup — 3 steps

### Step 1 — Install Obsidian

Download [Obsidian](https://obsidian.md) (free, Mac / Windows / Linux).

Open Obsidian → **Create new vault** → choose a folder → note the full path to that folder.

---

### Step 2 — Connect the Obsidian MCP

The MCP lets Claude Code read and write notes directly in your vault.

Requires [Node.js](https://nodejs.org) v18+. Then run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/path/to/your/vault"
```

**Mac example:**
```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/Users/yourname/Documents/my-second-brain"
```

**Windows example:**
```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "C:\Users\yourname\Documents\my-second-brain"
```

Restart Claude Code. Verify with `claude mcp list` — you should see `obsidian-vault` as Connected.

---

### Step 3 — Clone and open in Claude Code

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
```

Open the `obsidian-sppf-vault` folder in Claude Code.

---

## Run the installer

```
/vault-install
```

Claude will guide you through 5 steps:
1. **Discovery** — your role, projects, areas, capture style
2. **Structure design** — review and adjust your vault layout
3. **Personalize** — language, extras
4. **Build** — automatic: creates all folders, hub notes, knowledge base
5. **Handoff** — skills installed in your vault, first note captured live

**After installation:** open your vault folder in Claude Code. This repo can be deleted — everything is in your vault.

---

## How it works

```
Clone repo → connect MCP → run /vault-install
         ↓
Claude asks about your projects and areas
         ↓
Claude builds your vault structure via MCP:
  · personalized folders and hub notes
  · knowledge base (Insights, Decisions, Solutions, Concepts)
  · VAULT-INDEX.md linking everything
  · Claude_Improves reference guide
         ↓
Claude installs all skills in your vault/.claude/commands/
         ↓
Open your vault in Claude Code. Done forever.
```

---

## Requirements

- [Obsidian](https://obsidian.md) (free)
- [Claude Code](https://claude.ai/code)
- [Node.js](https://nodejs.org) v18+
