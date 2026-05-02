# /vault-install

You are running the vault installation wizard. Follow these 5 phases exactly, in order.

---

## PHASE 1 — DISCOVERY

Ask the user these questions one at a time (wait for answer before next):

1. "What's the main thing you want to use this second brain for? (work projects, learning, business, research, personal...)"
2. "Do you already have projects or areas of life you want to organize? Name 2-4 examples."
3. "What kind of notes do you capture most? (decisions, insights, meeting notes, ideas, references...)"

After answers, say: "Got it. Let me design a structure for you."

---

## PHASE 2 — STRUCTURE DESIGN

Based on their answers, propose a personalized vault structure. Example:

```
Proposed structure for you:

📁 01_Projects/        → Active projects (CraftSoph, ClientX, etc.)
📁 02_Areas/           → Ongoing responsibilities (Health, Finance, Learning)
📁 03_Knowledge/       → What you learn (Insights, Solutions, Concepts)
📁 04_Daily/           → Daily notes
📁 05_Monthly/         → Monthly synthesis reports
```

Adjust folder names to match their use case. If they're a researcher, maybe `03_Research/`. If they're a developer, maybe `02_Codebases/`.

Say: "Does this structure work for you, or would you like to adjust anything?"

Wait for confirmation or adjustments. Update the proposed structure accordingly.

---

## PHASE 3 — CONFIRM + PERSONALIZE

Ask:

**"One last thing — what language would you like for your vault?"**
```
A) English  — all folders and notes in English
B) Spanish  — todas las carpetas y notas en español
C) Mixed    — English structure, Spanish note content
```

Wait for their choice. Store it as [LANG] = "english", "spanish", or "mixed".

Then confirm everything:

```
Perfect! Here's what I'll build:

📦 VAULT STRUCTURE: [their confirmed structure]
🌐 LANGUAGE: [their choice]

Skills I'll install:
✅ /second-brain-capture — capture insights, solutions, decisions
✅ /link-finder — find orphan notes and suggest connections
✅ /vault-synthesis — generate monthly knowledge reports
✅ /next-steps-ai — AI-powered next steps ranked by impact
✅ /explore-skills — browse and install additional skills

Ready to build? [Yes / Adjust something]
```

---

## PHASE 4 — BUILD

Once user confirms, execute all steps silently and fast.

### Language Mapping Table

Use this table to apply [LANG] to ALL folder names and note content:

| Element              | english           | spanish              | mixed             |
|----------------------|-------------------|----------------------|-------------------|
| Projects folder      | `01_Projects`     | `01_Proyectos`       | `01_Projects`     |
| Areas folder         | `02_Areas`        | `02_Áreas`           | `02_Areas`        |
| Knowledge folder     | `03_Knowledge`    | `03_Conocimiento`    | `03_Knowledge`    |
| Daily folder         | `04_Daily`        | `04_Diario`          | `04_Daily`        |
| Monthly folder       | `05_Monthly`      | `05_Mensual`         | `05_Monthly`      |
| Insights subfolder   | `Insights`        | `Ideas`              | `Insights`        |
| Solutions subfolder  | `Solutions`       | `Soluciones`         | `Soluciones`      |
| Decisions subfolder  | `Decisions`       | `Decisiones`         | `Decisiones`      |
| Concepts subfolder   | `Concepts`        | `Conceptos`          | `Concepts`        |
| Note: Key points     | `## Key Points`   | `## Puntos clave`    | `## Key Points`   |
| Note: Next steps     | `## Next Steps`   | `## Próximos pasos`  | `## Next Steps`   |
| Note: Summary        | `## Summary`      | `## Resumen`         | `## Summary`      |
| Note: Outcome        | `## Outcome`      | `## Resultado`       | `## Resultado`    |

Apply the column matching [LANG] to every folder name and note section header you create below.

---

### Step 1 — Create folder structure

Use the **Write tool** (filesystem) to create a `.gitkeep` file in each folder, which forces the folder to exist. Write to `[VAULT_PATH]/[folder]/.gitkeep`.

Create all folders from the confirmed structure using the language-mapped names.

Also always create these knowledge subfolders inside the Knowledge folder:
- `[knowledge-folder]/Insights` (or mapped name)
- `[knowledge-folder]/Solutions` (or mapped name)
- `[knowledge-folder]/Decisions` (or mapped name)
- `[knowledge-folder]/Concepts` (or mapped name)

### Step 2 — Create Home note

Use the **obsidian-vault MCP** (`mcp__obsidian-vault__write_note`) to create `Home.md`:

```markdown
---
type: hub
created: [today's date]
---

# 🧠 Second Brain

> Built with [obsidian-sppf-vault](https://github.com/afmanu/obsidian-sppf-vault)

## Quick Links
- [[01_Projects/]] (or language-mapped name)
- [[03_Knowledge/]] (or language-mapped name)
- [[04_Daily/]] (or language-mapped name)

## Active Projects
(add your projects here)

## This Week's Focus
(update weekly)
```

Write Home.md content in [LANG] — use the section headers from the language mapping table.

### Step 3 — Create README note inside vault

Use the **obsidian-vault MCP** to create `00_START_HERE.md`:

Content should explain (in [LANG]):
- What this vault is for
- The 5 folder structure and what goes in each
- The skills available (`/second-brain-capture`, `/link-finder`, etc.)
- How to capture a first note: "Try `/second-brain-capture` now"

### Step 4 — Create first project hub

If user mentioned specific projects in Phase 1, create a hub note for their first project using the **obsidian-vault MCP**.

Path: `[projects-folder]/[ProjectName]/[ProjectName].md`

Content (in [LANG]):
```markdown
---
type: project
status: active
created: [today]
---

# [ProjectName]

## [Summary/Resumen]
[one line description]

## [Key Points/Puntos clave]
- 

## [Next Steps/Próximos pasos]
- [ ] 

## Notes
```

### Step 5 — Install skills permanently into vault

Use the **Write tool** (filesystem) to copy skills into `[VAULT_PATH]/.claude/commands/`.

This is critical: skills must live in the VAULT, not the repo, so they work when the user opens their vault in Claude Code.

Write these files to `[VAULT_PATH]/.claude/commands/`:

**second-brain-capture.md** — copy the full content from `.claude/commands/second-brain-capture.md` in this repo

**link-finder.md** — copy the full content from `.claude/commands/link-finder.md` in this repo

**vault-synthesis.md** — copy the full content from `.claude/commands/vault-synthesis.md` in this repo

**next-steps-ai.md** — copy the full content from `.claude/commands/next-steps-ai.md` in this repo

**explore-skills.md** — copy the full content from `.claude/commands/explore-skills.md` in this repo

To get the content of each file, read it first with the Read tool, then write to the vault path.

### Step 6 — Create skills index in vault

Use the **obsidian-vault MCP** to create `00_SKILLS.md` in the vault root:

Content (in [LANG]):
```markdown
# Skills Available

These commands work when you open this vault in Claude Code (`claude .`):

| Command | What it does |
|---|---|
| `/second-brain-capture` | Capture insights, solutions, decisions → auto-linked note |
| `/link-finder` | Find orphan notes and suggest connections |
| `/vault-synthesis` | Generate monthly knowledge report |
| `/next-steps-ai` | Get AI-ranked next steps based on your vault state |
| `/explore-skills` | Browse and install additional skills |

## Want more skills?
Type `/explore-skills` to see the full catalog of available skills you can add.
```

Write in [LANG].

---

## PHASE 5 — HANDOFF

After all steps complete, say:

```
✅ Your second brain is ready!

Here's what was built:
📁 [list the folders created with their language-mapped names]
📝 Home.md — your vault hub
📝 00_START_HERE.md — how to use this vault
⚡ 5 skills installed: /second-brain-capture, /link-finder, /vault-synthesis, /next-steps-ai, /explore-skills

---

🎯 Try your first capture right now:
Tell me something you learned recently and I'll capture it for you.

(Type `/second-brain-capture` or just say "I learned that...")
```

Wait for them to try it, or offer to demonstrate.

**Important final note:** From now on, open your Obsidian vault folder directly in Claude Code (`claude /path/to/vault`), not this repo. Your skills are installed in the vault — that's your home base.
