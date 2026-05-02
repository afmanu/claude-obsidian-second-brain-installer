# obsidian-second-brain

This repo gives Claude Code slash commands to build and operate a second brain inside the user's Obsidian vault. All note operations use the `obsidian-vault` MCP.

---

## Context

**Vault MCP:** `obsidian-vault` (must be connected before any skill runs)

**Vault structure (created by /vault-install):**
```
01_Projects/    active projects — each has a hub note
02_Areas/       areas of responsibility — each has a hub note
03_Knowledge/   Insights / Soluciones / Decisiones / Conceptos
04_Daily/       daily notes
05_Monthly/     monthly synthesis reports
```

**Frontmatter convention:**
```yaml
---
type: insight | solution | decision | concept | project | area | meeting | synthesis
project: [project name]
created: [YYYY-MM-DD]
status: active | validated | pending | archived
tags: []
---
```

---

## Skills in this repo

| Command | Purpose |
|---|---|
| `/vault-install` | One-time guided setup — run this first |
| `/second-brain-capture` | Capture insight/solution/decision as a linked note |
| `/link-finder` | Find orphan notes and suggest connections |
| `/vault-synthesis` | Generate synthesis report of the vault |
| `/next-steps-ai` | Suggest next steps by impact |
| `/explore-skills` | Browse the skills catalog and build new skills |

More skills are available in `docs/skills-catalog.md` — the user can ask Claude to build any of them.

---

## Key rules

- **Always use the `obsidian-vault` MCP** to read/write Obsidian notes
- **Use the Write tool directly** for `.claude/commands/` and `CLAUDE.md` files — these are filesystem files, not Obsidian notes
- **Ask before creating notes** — propose title, type, folder; wait for confirmation
- **Auto-link** — after creating a note, find 3-5 related notes and add wikilinks
- **Never delete** without explicit user confirmation
- **Personalize** — use the user's actual project/area names, never generic placeholders
