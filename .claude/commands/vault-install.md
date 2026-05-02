One-time guided setup that builds a personalized second brain vault in Obsidian.

**Before starting:** verify the `obsidian-vault` MCP is connected by calling list_directory on the vault root. If it fails, stop and show this message:

```
⚠️ The obsidian-vault MCP is not connected.

Complete Step 2 in the README before running /vault-install:

  claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/path/to/your/vault"

Then restart Claude Code and try again.
```

---

## PHASE 1 — Discovery

Say exactly:

```
🧠 Let's build YOUR vault.

4 quick questions — your answers shape everything.

1. What's your main role? (choose 1-3)
   A) Creator (YouTube, Substack, podcast)
   B) Knowledge Worker (engineer, designer, PM)
   C) Founder / Entrepreneur
   D) Student / Researcher
   E) Manager / Team Lead
   F) Freelancer / Consultant

2. What projects are you actively working on?
   List 1-5. Example: my startup, side project, learning Rust

3. What areas of responsibility do you have?
   List 1-5. Example: health, finances, team, learning

4. How do you capture knowledge today?
   □ Meetings & conversations
   □ Research / articles / books
   □ Code & technical solutions
   □ Personal insights & ideas
   □ Decisions & choices
```

Wait for answers. Then confirm:

```
✓ Here's your profile:

Role: [detected]
Projects: [list]
Areas: [list]
Capture style: [detected types]

Ready to design your vault structure? [yes / adjust]
```

---

## PHASE 2 — Structure Design

Show the proposed structure using their actual project and area names:

```
📐 Your vault:

01_Projects/
├── [project-1]/
├── [project-2]/
└── Claude_Improves/     ← documents all AI skills

02_Areas/
├── [area-1]/
└── [area-2]/

03_Knowledge/
├── Insights/
├── Soluciones/
├── Decisiones/
└── Conceptos/

04_Daily/
05_Monthly/

Look right? [yes / modify / what is this?]
```

If "modify": adjust interactively.
If "what is this?": explain each folder's purpose.

---

## PHASE 3 — Confirm

```
⚙️ Skills to install (all recommended):
  ✓ /second-brain-capture
  ✓ /link-finder
  ✓ /vault-synthesis
  ✓ /forgotten-notes
  ✓ /decision-tracker
  ✓ /next-steps-ai
  ✓ Claude_Improves project (your personal skill reference guide)

Install everything? [yes / customize]
```

---

## PHASE 4 — Build the vault (automatic)

Use the `obsidian-vault` MCP to create everything. Show a tick as each step completes.

**Step 1 — Folder structure**

Create a hub note for each project:
```markdown
---
type: project
name: [Project Name]
status: active
created: [today YYYY-MM-DD]
tags: [project]
---

# [Project Name]

## Overview

## Goals

## Notes
```
Save at `01_Projects/[project-slug]/[project-slug].md`

Create a hub note for each area:
```markdown
---
type: area
name: [Area Name]
created: [today YYYY-MM-DD]
tags: [area]
---

# [Area Name]

## Purpose

## Notes
```
Save at `02_Areas/[area-slug]/[area-slug].md`

Create placeholder notes to initialize knowledge folders:
- `03_Knowledge/Insights/README.md` — "Capture realizations and patterns here."
- `03_Knowledge/Soluciones/README.md` — "Document fixes and workarounds here."
- `03_Knowledge/Decisiones/README.md` — "Log decisions with reasoning here."
- `03_Knowledge/Conceptos/README.md` — "Define frameworks and concepts here."

**Step 2 — Claude_Improves project**

Create `01_Projects/Claude_Improves/Claude_Improves.md` (hub) and one doc per skill explaining what it does, how to call it, and when to use it.

**Step 3 — VAULT-INDEX.md at vault root**

A single index note linking to all projects and areas with wikilinks.

**Step 4 — Install skills into THIS vault** ⬅️ critical step

Write each skill file to `.claude/commands/` inside the vault using the MCP. This means that from now on the user works from their vault folder in Claude Code — not from this repo — and all skills remain available.

Files to write:
- `.claude/commands/second-brain-capture.md`
- `.claude/commands/link-finder.md`
- `.claude/commands/vault-synthesis.md`
- `.claude/commands/forgotten-notes.md`
- `.claude/commands/decision-tracker.md`
- `.claude/commands/next-steps-ai.md`

Use the exact content from each skill file in this repo's `.claude/commands/` folder.

Also write a `CLAUDE.md` at vault root:
```markdown
# My Second Brain

This vault is powered by Claude Code. All skills are in `.claude/commands/`.

## Vault structure
01_Projects/ — active projects
02_Areas/    — areas of responsibility
03_Knowledge/ — Insights / Soluciones / Decisiones / Conceptos
04_Daily/    — daily notes
05_Monthly/  — monthly synthesis reports

## Frontmatter convention
type: insight | solution | decision | concept | project | area | meeting | synthesis
project: [name]
created: [YYYY-MM-DD]
status: active | validated | pending | archived
```

Show progress:
```
🚀 Building your vault...

✓ [N] project hubs created
✓ [N] area hubs created
✓ Knowledge base initialized
✓ Claude_Improves guide created
✓ VAULT-INDEX.md created
✓ Skills installed into your vault
✓ CLAUDE.md written

✅ Done!
```

---

## PHASE 5 — Handoff

```
🎉 Your vault is ready in Obsidian.

One important step: from now on, open your VAULT folder
(not this repo) in Claude Code. All skills will be there.

Your vault path: [detected vault path from MCP]

Want to capture your first note before we finish?
Tell me one insight or decision from your work on [project-1].
```

Run /second-brain-capture with their input as a live demo.

Then show the final screen:

```
🧠 ALL DONE

✅ [N] projects set up
✅ [N] areas set up
✅ Knowledge base ready
✅ Skills installed in your vault
✅ First note captured

From now on:
→ Open [vault-path] in Claude Code
→ All 6 skills are available as slash commands

DAILY:    /second-brain-capture  /next-steps-ai
WEEKLY:   /link-finder  /forgotten-notes
MONTHLY:  /vault-synthesis  /decision-tracker

Happy capturing! 🧠
```
