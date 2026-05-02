# Skills Catalog

This vault ships with 4 core skills. Everything else lives here — a catalog of skills you can ask Claude Code to build for you.

---

## How to build any skill

Open your vault in Claude Code and say:

> "Read `docs/skills-catalog.md` and build me the [skill name] skill."

Claude will read the spec, create the `.claude/commands/[skill].md` file in your vault, and the skill will be available immediately.

---

## Core skills (already installed)

| Skill | What it does |
|---|---|
| `/second-brain-capture` | Capture insight/decision/solution as a linked note |
| `/link-finder` | Find orphan notes and suggest connections |
| `/vault-synthesis` | Generate synthesis report of your vault |
| `/next-steps-ai` | Suggest next steps ordered by impact |

---

## Skills you can build

---

### /forgotten-notes

**What it does:** Resurfaces notes you haven't visited in 30+ days, ordered by how relevant they are to what you're currently working on.

**Why it's useful:** Your vault accumulates knowledge you forget about. This skill brings it back at the right moment.

**How to build it:** Ask Claude to:
1. List all notes in the vault
2. Filter those not modified in 30+ days
3. Compare keywords in old notes vs. your 10 most recent notes
4. Show top 5 by keyword overlap, with links to open them

**Prompt to give Claude:**
> "Build me a `/forgotten-notes` skill. It should list notes not modified in 30+ days, rank them by keyword similarity to my 10 most recent notes, and show the top 5 with wikilinks."

---

### /decision-tracker

**What it does:** Finds all your decision notes, checks if you've logged outcomes, calculates success rate by category, and identifies patterns in when you fail.

**Why it's useful:** You make better decisions when you review past ones. Most people never do.

**How to build it:** Ask Claude to:
1. Search for all notes with `type: decision` in frontmatter
2. Check each for an `outcome:` field (good / bad / mixed / pending)
3. Group by category and calculate success rates
4. Surface patterns: which contexts produce bad decisions?

**Prompt to give Claude:**
> "Build me a `/decision-tracker` skill. It should find all notes with `type: decision`, group them by a `category` frontmatter field, calculate success rate per category based on an `outcome` field, and show patterns of failure."

---

### /daily-note

**What it does:** Creates or opens today's daily note with a template — yesterday's incomplete tasks, today's focus, and a capture area.

**Why it's useful:** Gives you a consistent daily starting point inside Obsidian without leaving Claude Code.

**How to build it:** Ask Claude to:
1. Check if `04_Daily/[today].md` exists
2. If not: create it with a template pulling in open tasks from yesterday
3. If yes: show it and ask what to update

**Prompt to give Claude:**
> "Build me a `/daily-note` skill. It should create today's note in `04_Daily/` using a template with sections: Yesterday's open tasks, Today's focus, and Notes/Captures. If today's note already exists, show it."

---

### /project-health

**What it does:** Reviews all your active projects, shows last activity date, open tasks, and flags any that have gone silent for more than 2 weeks.

**Why it's useful:** Projects stall silently. This makes the stalling visible before it becomes a problem.

**How to build it:** Ask Claude to:
1. List all notes in `01_Projects/` with `status: active`
2. Check the most recent note modification date per project
3. Flag projects with no activity in 14+ days
4. Show a simple dashboard

**Prompt to give Claude:**
> "Build me a `/project-health` skill. It should list all projects in `01_Projects/` with `status: active`, show the date of their last modified note, and flag any project with no activity in the last 14 days as 'stalled'."

---

### /weekly-review

**What it does:** Guides you through a structured weekly review — what you captured, what decisions you made, what's moving, what's stuck — and creates a `04_Daily/[date]-weekly-review.md` note.

**Why it's useful:** The weekly review is the most high-leverage habit in any productivity system. This skill makes it frictionless.

**How to build it:** Ask Claude to:
1. Pull all notes created in the last 7 days
2. Group by type (insights, decisions, solutions)
3. Ask the user: what went well? what's stuck? what's next week's priority?
4. Create a weekly review note with all of it

**Prompt to give Claude:**
> "Build me a `/weekly-review` skill. It should pull all notes from the last 7 days grouped by type, ask me 3 questions (what went well, what's stuck, next week's priority), then create a weekly review note in `04_Daily/` with the summary."

---

### /capture-from-url

**What it does:** Takes a URL, fetches the page content, extracts the key ideas, and creates a note in `03_Knowledge/` with the source linked.

**Why it's useful:** You read things online and lose them. This turns a link into a permanent note instantly.

**How to build it:** Ask Claude to:
1. Accept a URL as input
2. Fetch and summarize the content
3. Extract 3-5 key ideas
4. Create a note with `type: concept` and the source URL in frontmatter

**Prompt to give Claude:**
> "Build me a `/capture-from-url` skill. It takes a URL, fetches the content, extracts the 3-5 most important ideas, and saves them as a note in `03_Knowledge/Conceptos/` with the source URL in frontmatter."

---

### /meeting-recap

**What it does:** Takes raw meeting notes or a transcript, structures them into: key points, decisions made, action items, and risks. Saves a clean note in `01_Projects/[project]/`.

**Why it's useful:** Raw meeting notes are useless. Structured ones are searchable and actionable.

**How to build it:** Ask Claude to:
1. Accept meeting notes as input (paste or file)
2. Detect the project from content or ask
3. Structure into: Key points / Decisions / Action items / Risks
4. Save with `type: meeting` frontmatter

**Prompt to give Claude:**
> "Build me a `/meeting-recap` skill. It takes raw meeting notes, structures them into Key points, Decisions, Action items, and Risks, then saves the result in the relevant project folder with `type: meeting` frontmatter."

---

## How to suggest a new skill

If you think of a skill that would make your vault smarter, describe it to Claude Code:

> "I want a skill that does [X]. Add it to my `docs/skills-catalog.md` with a spec and a build prompt."

Claude will write the spec and add it to your catalog permanently.
