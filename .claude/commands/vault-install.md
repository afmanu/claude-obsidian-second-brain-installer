One-time guided setup that builds a personalized second brain vault in Obsidian.

Before starting, verify the `obsidian-vault` MCP is connected by listing the vault root. If it fails, stop and tell the user to complete Step 2 in the README.

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

## PHASE 3 — Confirm skills and extras

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

Use the `obsidian-vault` MCP to create everything. Show progress as you go:

```
🚀 Building your vault...
```

Create in this order:

1. **Folder structure** — create hub notes for each folder:
   - `01_Projects/[project-slug]/[project-slug].md` (one per project)
   - `02_Areas/[area-slug]/[area-slug].md` (one per area)
   - `03_Knowledge/Insights/.gitkeep` placeholder note
   - `03_Knowledge/Soluciones/.gitkeep` placeholder note
   - `03_Knowledge/Decisiones/.gitkeep` placeholder note
   - `03_Knowledge/Conceptos/.gitkeep` placeholder note

2. **Project hubs** — each with frontmatter:
   ```yaml
   ---
   type: project
   name: [Project Name]
   status: active
   created: [today]
   tags: [project]
   ---
   ```

3. **Area hubs** — each with frontmatter:
   ```yaml
   ---
   type: area
   name: [Area Name]
   created: [today]
   tags: [area]
   ---
   ```

4. **Claude_Improves project** — create hub + one doc per skill:
   - `01_Projects/Claude_Improves/Claude_Improves.md` (hub)
   - `01_Projects/Claude_Improves/skill-second-brain-capture.md`
   - `01_Projects/Claude_Improves/skill-link-finder.md`
   - `01_Projects/Claude_Improves/skill-vault-synthesis.md`
   - `01_Projects/Claude_Improves/skill-forgotten-notes.md`
   - `01_Projects/Claude_Improves/skill-decision-tracker.md`
   - `01_Projects/Claude_Improves/skill-next-steps-ai.md`

   Each skill doc explains: what it does, how to use it, when to use it, example.

5. **VAULT-INDEX.md** at vault root — links to all projects and areas.

Show a tick as each step completes. End with:

```
✅ Vault ready! Created:
   [N] project hubs
   [N] area hubs
   Knowledge base structure
   Claude_Improves reference guide
```

---

## PHASE 5 — First note (live demo)

```
🎉 One last thing — let's capture your first note.

You mentioned you work on [project-1].

Tell me one insight, decision, or challenge about it right now.
```

Run /second-brain-capture with their input. This shows the skill working in real time.

Then show the final screen:

```
🧠 YOUR VAULT IS READY

✅ [N] projects set up
✅ [N] areas set up
✅ Knowledge base ready
✅ Claude_Improves guide created
✅ First note captured

---
USE DAILY:
  /second-brain-capture "I learned X"
  /next-steps-ai

USE WEEKLY:
  /link-finder
  /forgotten-notes

USE MONTHLY:
  /vault-synthesis
  /decision-tracker

Everything is in your Obsidian vault. Open it and explore.
Happy capturing! 🧠
```
