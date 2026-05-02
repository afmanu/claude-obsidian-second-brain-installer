# 🧠 obsidian-second-brain

> A second brain template for Obsidian — powered by Claude Code AI skills.

Clone this repo, follow 3 setup steps, run `/vault-install`, and Claude builds your personalized vault automatically — then installs all skills directly into your vault so you never need this repo again.

---

## What you get

**6 AI skills** that run inside Claude Code and write directly into your Obsidian vault:

| Skill | What it does |
|---|---|
| `/vault-install` | One-time guided setup — builds your vault in ~20 min |
| `/second-brain-capture` | Capture insights/decisions → linked note in <2s |
| `/link-finder` | Find orphan notes + suggest connections with % score |
| `/vault-synthesis` | Monthly report: patterns, insights, recommendations |
| `/forgotten-notes` | Resurface old notes ranked by relevance |
| `/decision-tracker` | Audit past decisions + success rate by category |
| `/next-steps-ai` | Suggest 3-5 next steps ordered by impact |

---

## Setup — 3 steps before running the installer

### Step 1 — Install Obsidian

Download and install [Obsidian](https://obsidian.md) (free, available for Mac, Windows, Linux).

Open Obsidian → **Create new vault** → choose a folder on your computer → name it whatever you want (e.g. `my-second-brain`).

Note the full path to that folder — you'll need it in Step 2.

---

### Step 2 — Connect the Obsidian MCP

The MCP lets Claude Code read and write notes directly in your vault.

Make sure you have [Node.js](https://nodejs.org) installed, then run:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/path/to/your/vault"
```

Replace `/path/to/your/vault` with the actual path to the vault folder you created in Step 1.

**Example (Mac):**
```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/Users/yourname/Documents/my-second-brain"
```

**Example (Windows):**
```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "C:\Users\yourname\Documents\my-second-brain"
```

Restart Claude Code. You should see `obsidian-vault` in your MCP list (`claude mcp list`).

---

### Step 3 — Clone this repo and open in Claude Code

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
```

Open the `obsidian-sppf-vault` folder in Claude Code.

---

## Run the installer

Type in Claude Code:

```
/vault-install
```

Claude will ask you about your projects and areas, build your vault structure in Obsidian, and install all 6 skills directly into your vault.

**After installation:** open your vault folder (not this repo) in Claude Code. All skills will be available there permanently.

---

## How it works

```
You clone this repo → run /vault-install in Claude Code
         ↓
Claude asks: your projects, areas, capture style
         ↓
Claude writes everything into your Obsidian vault via MCP:
  · folder structure personalized to you
  · hub notes for each project and area
  · Claude_Improves reference guide
  · all 6 skills installed in your vault
         ↓
You close this repo. Open your vault in Claude Code.
All skills work from there forever.
```

---

## Requirements

- [Obsidian](https://obsidian.md) (free)
- [Claude Code](https://claude.ai/code)
- [Node.js](https://nodejs.org) v18+

---

## After installation — vault structure

```
01_Projects/    your active projects (personalized to you)
02_Areas/       your areas of responsibility (personalized)
03_Knowledge/
  Insights/     realizations and patterns
  Soluciones/   fixes and workarounds
  Decisiones/   decisions with reasoning
  Conceptos/    frameworks and definitions
04_Daily/       daily notes
05_Monthly/     monthly synthesis reports
```

Plus `Claude_Improves/` — a reference guide that explains every skill and how to use it.
