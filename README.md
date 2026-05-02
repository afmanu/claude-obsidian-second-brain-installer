# 🧠 obsidian-second-brain

> A second brain template for Obsidian — powered by Claude Code AI skills.

Clone this repo, follow 3 setup steps, then run `/vault-install` and Claude builds your personalized vault automatically.

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

## Before you start — 3 setup steps

### Step 1 — Install Obsidian

Download and install [Obsidian](https://obsidian.md) (free).

Open Obsidian → **Create new vault** → choose a folder on your computer → name it whatever you want (e.g. `my-vault`).

Leave it open. You'll point the MCP to this folder in Step 2.

---

### Step 2 — Connect the Obsidian MCP

The MCP is what allows Claude Code to read and write notes in your vault.

**Install the MCP package:**
```bash
npm install -g mcp-obsidian
```

**Add it to your Claude Code MCP settings.**

Open Claude Code → Settings → MCP Servers → add:

```json
{
  "obsidian-vault": {
    "command": "npx",
    "args": ["-y", "mcp-obsidian"],
    "env": {
      "VAULT_PATH": "/absolute/path/to/your/vault"
    }
  }
}
```

Replace `/absolute/path/to/your/vault` with the actual path to the vault folder you created in Step 1.

Restart Claude Code. You should see `obsidian-vault` in your MCP list.

---

### Step 3 — Clone this repo and open in Claude Code

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
```

Open the folder in Claude Code. The 7 skills will be available immediately as slash commands.

---

## Run the installer

Type in Claude Code:

```
/vault-install
```

Claude will ask you about your projects and areas, then build your personalized vault structure directly in Obsidian. Takes ~20 minutes, mostly automated.

---

## Requirements

- [Obsidian](https://obsidian.md) (free)
- [Claude Code](https://claude.ai/code)
- Node.js (for the MCP)

---

## How it works

```
You → /vault-install in Claude Code
         ↓
Claude asks: your projects, areas, capture style
         ↓
Claude writes structure into your Obsidian vault via MCP
         ↓
Your vault is ready with folders, hubs, and all 6 skills active
```

No Python. No scripts. No manual file creation. Claude does it all through the Obsidian MCP.

---

## After installation

The vault structure Claude creates:

```
01_Projects/    your active projects (personalized)
02_Areas/       areas of responsibility (personalized)
03_Knowledge/
  Insights/
  Soluciones/
  Decisiones/
  Conceptos/
04_Daily/       daily notes
05_Monthly/     monthly synthesis reports
```

Plus a `Claude_Improves/` project inside `01_Projects/` that documents every skill and how it works — your personal reference guide.
