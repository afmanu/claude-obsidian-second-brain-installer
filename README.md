# 🧠 obsidian-second-brain

> Build your second brain in Obsidian, guided step by step by Claude Code.

## How to start

**1. Clone this repo and open it in Claude Code:**

```bash
git clone https://github.com/afmanu/obsidian-sppf-vault.git
cd obsidian-sppf-vault
claude .
```

**2. That's it.** Claude will take over immediately — checking what's installed, guiding you through setup, and building your vault automatically.

---

## What Claude does for you

Claude checks your environment step by step and handles everything:

- **Obsidian** — detects if it's installed, installs it automatically if needed
- **Vault folder** — creates it for you at `~/Documents/my-second-brain` (or wherever you choose)
- **Node.js** — detects and installs if missing
- **MCP connection** — connects Claude Code to your vault so it can read and write notes
- **Vault structure** — asks about your projects and areas, then builds everything

---

## What you get

### 5 core skills (installed automatically into your vault)

| Skill | What it does |
|---|---|
| `/second-brain-capture` | Capture an insight, decision, or solution → linked note in seconds |
| `/link-finder` | Find orphan notes and suggest connections with confidence scores |
| `/vault-synthesis` | Generate a synthesis report: patterns, insights, recommendations |
| `/next-steps-ai` | Suggest your next 3-5 actions ordered by impact |
| `/explore-skills` | Browse a catalog of additional skills and build any of them on demand |

### Skills catalog — build what you need

`/explore-skills` gives you a catalog of additional skills you can ask Claude to build:

- `/forgotten-notes` — resurface old notes by relevance
- `/decision-tracker` — audit past decisions and success rates
- `/daily-note` — create today's note from a template
- `/project-health` — flag stalled projects
- `/weekly-review` — guided weekly review
- `/capture-from-url` — turn any URL into a vault note
- `/meeting-recap` — structure raw meeting notes
- *...and any skill you design yourself*

### Vault structure (personalized to you)

```
01_Projects/    your active projects
02_Areas/       your areas of responsibility
03_Knowledge/
  Insights/     realizations and patterns
  Soluciones/   fixes and workarounds
  Decisiones/   decisions with reasoning
  Conceptos/    frameworks and definitions
04_Daily/       daily notes
05_Monthly/     monthly synthesis reports
```

---

## After setup

Once installed, **open your vault folder in Claude Code** — not this repo.
All 5 skills will be there permanently.

```bash
claude /path/to/your/vault
```

---

## Requirements

- [Claude Code](https://claude.ai/code)
- Internet connection (for first run — Claude installs everything else)
