# Skill: /vault-install

Interactive guided setup to build a personalized second brain vault.

---

## When user runs `/vault-install`

Execute the following 5 phases in order. Wait for user confirmation between phases.

---

## PHASE 1 — Discovery (5 min)

Say:

```
🧠 Let's build YOUR vault.

I'll ask you 4 quick questions. Your answers shape everything.

**1. What's your main role?** (choose 1-3)
   A) Creator (YouTube, Substack, podcast)
   B) Knowledge Worker (engineer, designer, PM)
   C) Founder / Entrepreneur
   D) Student / Researcher
   E) Manager / Team Lead
   F) Freelancer (multiple projects)

**2. What projects are you actively working on?**
   List 1-5. Example: "my startup, a side project, learning Rust"

**3. What areas of responsibility do you have?**
   List 1-5. Example: "health, finances, team management, learning"

**4. How do you currently capture knowledge?**
   □ Meetings & discussions
   □ Research / articles / books
   □ Code & technical solutions
   □ Personal insights & ideas
   □ Decisions & choices
   □ Other: ___

Ready? Answer all 4.
```

After user answers, confirm:

```
✓ Got it. Here's your profile:

- Role: [detected role]
- Projects: [list]
- Areas: [list]
- Capture style: [detected types]

Ready for Phase 2 — vault structure? [yes / adjust]
```

---

## PHASE 2 — Structure Design (5 min)

Show proposed vault structure based on their answers:

```
📐 Your vault structure:

01_Projects/
├── [project-1]/
├── [project-2]/
└── Claude_Improves/     ← tracks all AI improvements

02_Areas/
├── [area-1]/
└── [area-2]/

03_Knowledge/
├── Insights/
├── Soluciones/
├── Decisiones/
└── Conceptos/

04_Daily/                ← auto daily notes
05_Monthly/              ← monthly synthesis reports

Does this look right? [yes / modify / explain]
```

If "modify": adjust interactively.
If "explain": describe what each folder is for.

---

## PHASE 3 — Configuration (5 min)

```
⚙️ Almost ready. A few choices:

**Skills to install:** (all recommended)
  ✓ /second-brain-capture
  ✓ /link-finder
  ✓ /vault-synthesis
  ✓ /forgotten-notes
  ✓ /decision-tracker
  ✓ /next-steps-ai

**MCPs:**
  ✓ obsidian-sync-mcp (essential — real-time sync)
  ○ github-mcp (recommended — auto backup every 60 min)

**Extras:**
  ✓ Claude_Improves project (documents all skills/MCPs in your vault)

Enable github-mcp? [yes / skip]
Enable Claude_Improves? [yes / skip]

Or just say "install everything" to proceed with all defaults.
```

---

## PHASE 4 — Installation (10 min, automatic)

Run the installation:

1. Call `scripts/create-structure.py` with user's projects and areas
2. Copy templates from `templates/` to vault
3. Create hub files for each project and area
4. Install all selected skills into `.claude/` settings
5. Configure MCPs
6. If Claude_Improves selected: create all documentation notes
7. Generate `vault/VAULT-MANIFEST.md`

Show progress:

```
🚀 Installing your vault...

✓ Creating folder structure
✓ Creating project hubs
✓ Creating area hubs
✓ Installing 6 skills
✓ Configuring MCPs
✓ Creating Claude_Improves project
✓ Generating VAULT-MANIFEST.md

✅ Installation complete!
```

---

## PHASE 5 — Integration + First Note (5 min)

```
🔗 Connect to Obsidian:

1. Open Obsidian
2. "Open folder as vault"
3. Select: [path]/vault/
4. Done!

Say "obsidian-open" when ready.
```

After "obsidian-open":

```
🎉 Let's create your FIRST note.

You said you work on: [project-1]

Tell me one insight, decision, or challenge about it.
(Example: "I decided to use X instead of Y because...")
```

Run `/second-brain-capture` with their input as a live demo.

Final screen:

```
🎉 YOUR VAULT IS READY!

✅ 6 skills installed
✅ MCPs configured
✅ Claude_Improves created
✅ First note captured
✅ Connected to Obsidian

---
DAILY (on-demand):
  /second-brain-capture "I learned X"
  /next-steps-ai

WEEKLY:
  /link-finder (Monday)
  /forgotten-notes (Wednesday)

MONTHLY:
  /vault-synthesis (1st of month)
  /decision-tracker (end of month)

Happy capturing! 🧠
```
