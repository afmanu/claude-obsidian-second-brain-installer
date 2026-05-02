# obsidian-second-brain

This repo gives Claude Code 7 slash commands that build and operate a second brain inside the user's Obsidian vault. All commands use the `obsidian-vault` MCP to read and write notes directly in Obsidian.

---

## Context

**Vault MCP:** `obsidian-vault` (must be connected before any skill runs)
**Vault structure (after install):**
```
01_Projects/    active projects
02_Areas/       areas of responsibility  
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

## Available skills

All skills are in `.claude/commands/`. They are invoked as slash commands:

- `/vault-install` — one-time guided setup
- `/second-brain-capture` — capture insight/solution/decision
- `/link-finder` — find orphans and suggest links
- `/vault-synthesis` — generate monthly report
- `/forgotten-notes` — resurface old relevant notes
- `/decision-tracker` — audit decisions and outcomes
- `/next-steps-ai` — suggest next steps by impact

---

## Important behavior

- **Always use the `obsidian-vault` MCP** to read/write notes — never create local files
- **Ask before creating** — propose title, type and folder, wait for confirmation
- **Auto-link** — after creating a note, search for 3-5 related notes and add wikilinks
- **Respect the structure** — always place notes in the correct folder by type
- **Never delete** without explicit user confirmation
- **Personalize** — use the user's actual project and area names, not generic placeholders
