One-time guided setup that builds a personalized second brain vault in Obsidian.

**Before starting:** verify the `obsidian-vault` MCP is connected by calling list_directory on the vault root. If it fails, stop and show:

```
⚠️ The obsidian-vault MCP is not connected.

Complete Step 2 in the README first:

  claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "/path/to/your/vault"

Then restart Claude Code and try again.
```

---

## PHASE 1 — Discovery

Say:

```
🧠 Let's build YOUR second brain.

I'll ask you 4 questions. Your answers shape everything — folder names,
structure, and how the system works for you specifically.

1. What's your main role? (choose 1-3)
   A) Creator (YouTube, Substack, podcast)
   B) Knowledge Worker (engineer, designer, PM)
   C) Founder / Entrepreneur
   D) Student / Researcher
   E) Manager / Team Lead
   F) Freelancer / Consultant

2. What projects are you actively working on?
   List 1-5. These become your 01_Projects/ folders.
   Example: my startup, learning Rust, side project

3. What areas of responsibility do you have?
   List 1-5. These become your 02_Areas/ folders.
   Example: health, finances, team management, learning

4. What types of knowledge do you most want to capture?
   □ Insights and realizations
   □ Technical solutions and fixes
   □ Decisions (with reasoning)
   □ Concepts and frameworks
   □ Meeting notes
   □ Resources and references
```

Wait for all answers. Then confirm:

```
✓ Got it. Here's your profile:

Role:     [detected]
Projects: [list]
Areas:    [list]
Capture:  [selected types]

Does this look right? [yes / adjust]
```

---

## PHASE 2 — Structure Design

Propose the vault structure using their actual names:

```
📐 Here's your vault structure:

01_Projects/
├── [project-1]/        ← hub note + all related notes
├── [project-2]/
└── Claude_Improves/    ← documents your AI skills

02_Areas/
├── [area-1]/
└── [area-2]/

03_Knowledge/
├── Insights/           ← realizations, patterns, learnings
├── Soluciones/         ← fixes, workarounds, technical answers
├── Decisiones/         ← choices with reasoning and outcomes
└── Conceptos/          ← frameworks, definitions, mental models

04_Daily/               ← daily notes (one per day)
05_Monthly/             ← monthly synthesis reports

Every note has frontmatter: type, project, date, status, tags.
This makes everything searchable and linkable.

Look right? [yes / modify / explain any folder]
```

Adjust interactively if needed. If user asks "what is this?", explain the purpose of each section in plain terms.

---

## PHASE 3 — Confirm and personalize

Ask two quick personalizations:

```
Two quick choices:

1. Language for folder/note names?
   A) English  B) Spanish  C) Keep it as shown

2. Want a Claude_Improves project? (recommended)
   It's a reference guide in your vault that explains every skill,
   how to use it, and when. You can read it anytime in Obsidian.
   [yes / skip]

Ready to build? [yes]
```

---

## PHASE 4 — Build the vault

Use the `obsidian-vault` MCP to create all notes. Show progress as you go.

```
🚀 Building your vault...
```

**Step 1 — Project hubs**

For each project, create `01_Projects/[slug]/[slug].md`:

```markdown
---
type: project
name: [Project Name]
status: active
created: [YYYY-MM-DD]
tags: [project]
---

# [Project Name]

## Overview


## Goals


## Notes

```

Tick: `✓ [N] project hubs created`

**Step 2 — Area hubs**

For each area, create `02_Areas/[slug]/[slug].md`:

```markdown
---
type: area
name: [Area Name]
created: [YYYY-MM-DD]
tags: [area]
---

# [Area Name]

## Purpose


## Notes

```

Tick: `✓ [N] area hubs created`

**Step 3 — Knowledge base**

Create a README note in each knowledge folder explaining what goes there:
- `03_Knowledge/Insights/README.md` → "Realizations, patterns, and learnings. Created with /second-brain-capture."
- `03_Knowledge/Soluciones/README.md` → "Fixes, workarounds, and technical answers."
- `03_Knowledge/Decisiones/README.md` → "Decisions with reasoning. Add an `outcome:` field later to track results."
- `03_Knowledge/Conceptos/README.md` → "Frameworks, definitions, and mental models."

Tick: `✓ Knowledge base initialized`

**Step 4 — VAULT-INDEX.md**

Create at vault root — a single note linking to all projects and areas:

```markdown
---
type: index
created: [YYYY-MM-DD]
---

# Vault Index

## Projects
- [[01_Projects/[slug]/[slug]|[Project Name]]]
...

## Areas
- [[02_Areas/[slug]/[slug]|[Area Name]]]

## Knowledge
- [[03_Knowledge/Insights/README|Insights]]
- [[03_Knowledge/Soluciones/README|Soluciones]]
- [[03_Knowledge/Decisiones/README|Decisiones]]
- [[03_Knowledge/Conceptos/README|Conceptos]]
```

Tick: `✓ VAULT-INDEX.md created`

**Step 5 — Claude_Improves project** (if user selected yes)

Create `01_Projects/Claude_Improves/Claude_Improves.md` and one note per installed skill explaining: what it does, how to call it, example input/output.

Tick: `✓ Claude_Improves guide created`

**Step 6 — Install skills into the vault** ⚠️ use the filesystem Write tool, NOT the MCP

The vault is a folder on the user's computer. To install skills, write files directly to `[vault-path]/.claude/commands/` using the Write tool. Do not use the obsidian-vault MCP for this step — it is for Obsidian notes, not hidden config directories.

Get the vault path by asking the user: "What is the full path to your vault folder?" (they set it when connecting the MCP).

Write these files:
- `[vault-path]/.claude/commands/second-brain-capture.md` — copy from this repo
- `[vault-path]/.claude/commands/link-finder.md` — copy from this repo
- `[vault-path]/.claude/commands/vault-synthesis.md` — copy from this repo
- `[vault-path]/.claude/commands/next-steps-ai.md` — copy from this repo
- `[vault-path]/.claude/commands/explore-skills.md` — copy from this repo

Also write `[vault-path]/CLAUDE.md`:

```markdown
# My Second Brain

This vault is powered by Claude Code.

## Available skills
- /second-brain-capture — capture insight/decision/solution
- /link-finder          — find orphan notes and suggest links
- /vault-synthesis      — generate synthesis report
- /next-steps-ai        — suggest next steps by impact
- /explore-skills       — browse and build more skills

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
tags: []
```

Also copy `docs/skills-catalog.md` from this repo to `[vault-path]/docs/skills-catalog.md` so the user can browse and build more skills from inside their vault.

Tick: `✓ Skills installed`
Tick: `✓ CLAUDE.md written`
Tick: `✓ Skills catalog copied`

---

## PHASE 5 — First note + handoff

```
🎉 Your vault is ready.

Important: from now on, open your vault folder in Claude Code
(not this repo). All skills will be there permanently.

Vault: [vault-path]

One last thing — let's make your first capture.
You mentioned you work on [project-1].

Tell me one insight, decision, or challenge about it right now.
```

Run /second-brain-capture with their input as a live demo.

Then show:

```
🧠 ALL DONE

✅ [N] projects set up
✅ [N] areas set up  
✅ Knowledge base ready
✅ 5 skills installed in your vault
✅ Skills catalog installed (run /explore-skills to build more)
✅ First note captured

From now on → open [vault-path] in Claude Code

DAILY:    /second-brain-capture    /next-steps-ai
WEEKLY:   /link-finder
MONTHLY:  /vault-synthesis
ANYTIME:  /explore-skills  (to add new skills)

Happy capturing! 🧠
```
