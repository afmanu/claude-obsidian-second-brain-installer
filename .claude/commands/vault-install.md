# /vault-install

You are running the vault installation wizard. Follow these 5 phases exactly, in order.

---

## PHASE 1 — DIAGNOSIS

Ask the user these 3 questions, one at a time (wait for each answer):

**Question 1:** "What is the main reason you want a second brain? What problem are you trying to solve?"

**Question 2:** "Describe your daily work or life in 2-3 sentences. What do you mostly do?"

**Question 3:** "What kind of information do you capture most? (meetings, ideas, code, notes from books, personal goals, tasks...)"

After receiving all 3 answers, run the internal profile matching below silently. Do NOT show this logic to the user.

---

### INTERNAL PROFILE MATCHING (silent)

Read all 6 profiles from `profiles/` in this repo. Match user answers against the "Diagnostic Questions" section in each profile file.

Score each profile 0-100 based on keyword and intent matching:
- Exact keyword match = +25 points
- Intent/concept match = +15 points
- Contradicting signal = -20 points

**Profile files to read:**
- `profiles/consultant.md`
- `profiles/developer.md`
- `profiles/researcher.md`
- `profiles/entrepreneur.md`
- `profiles/student.md`
- `profiles/personal.md`

Select the top-scoring profile. Store as [PROFILE].

Also extract from user answers:
- [PROJECTS]: list of projects/areas they mentioned (e.g. "my startup", "Python course", "client XYZ")
- [AREAS]: life/work areas they mentioned (e.g. "health", "finance", "marketing")

---

## PHASE 2 — STRUCTURE PROPOSAL

Present the recommended structure. Say:

```
Based on what you told me, you're a [profile description in plain words].

I recommend the [PROFILE NAME] structure:

[Show the folder tree from the profile file, personalized with their actual projects/areas]

For example, since you mentioned [their specific project], I'd create:
  [concrete example folder path]

Does this structure work, or would you like to adjust anything?
```

If user wants to adjust: accept changes and update the proposed structure. Store final structure as [STRUCTURE].

Also show this at the bottom:
```
Not what you expected? Other available profiles:
- Consultant (clients + projects + operations)
- Developer (codebase + solutions + learning)
- Researcher (Zettelkasten: literature + permanent notes)
- Entrepreneur (strategy + products + customers)
- Student (courses + concepts + exams)
- Personal (journal + goals + life areas)
```

---

## PHASE 3 — CONFIRM + LANGUAGE

Ask:

**"One last thing — what language would you like for your vault?"**
```
A) English  — all folders and notes in English
B) Spanish  — todas las carpetas y notas en español
C) Mixed    — English structure, Spanish note content
```

Wait for their choice. Store as [LANG].

Apply the language mapping from the selected profile file (`profiles/[profile].md`, section "Language Mapping") to all folder names and note content.

Then confirm:

```
Perfect! Here's what I'll build:

📦 PROFILE: [profile name]
📁 STRUCTURE: [final folder list with language-mapped names]
🌐 LANGUAGE: [their choice]

Skills I'll install:
✅ /second-brain-capture — capture anything → routed to the right place automatically
✅ /link-finder — find orphan notes and suggest connections
✅ /vault-synthesis — generate monthly knowledge reports
✅ /next-steps-ai — AI-ranked next steps based on vault state
✅ /explore-skills — browse and install additional skills

Ready to build? [Yes / Adjust something]
```

---

## PHASE 4 — BUILD

Once user confirms, execute all steps silently and fast.

### Step 1 — Create folder structure

Use the **Write tool** (filesystem) to create a `.gitkeep` in each folder:
`[VAULT_PATH]/[folder]/.gitkeep`

Create all folders from [STRUCTURE] using the language-mapped names from `profiles/[PROFILE].md`.

### Step 2 — Save vault profile config

Use the **obsidian-vault MCP** (`mcp__obsidian-vault__write_note`) to create `[VAULT_PATH]/.claude/vault-profile.md`:

```markdown
---
profile: [PROFILE]
language: [LANG]
vault_path: [VAULT_PATH]
created: [today's date]
---

# Vault Profile

## Profile
[PROFILE]

## Language
[LANG]

## Structure
[list of all created folders with their language-mapped names]

## Routing Rules
[copy the full "Routing Rules" table from profiles/[PROFILE].md]

## Link Rules
[copy the full "Link Rules" table from profiles/[PROFILE].md]
```

This file is the source of truth for all skills. Every skill reads it to know where to route notes and what links to create.

### Step 3 — Create Home note

Use the **obsidian-vault MCP** to create `Home.md` in the vault root.

Content should be in [LANG]. Use the main hub notes from `profiles/[PROFILE].md` as the quick links.

```markdown
---
type: hub
profile: [PROFILE]
created: [today]
---

# 🧠 Second Brain

## Quick Access
[links to top-level folders using language-mapped names]

## Active [Projects/Proyectos/Proyectos]
[if user mentioned specific projects, list them here as wikilinks]

## This Week
(update weekly)
```

### Step 4 — Create hub notes

Use the **obsidian-vault MCP** to create the hub notes defined in `profiles/[PROFILE].md`, section "Hub Notes to Create".

For each hub note, personalize with the user's actual projects/areas from [PROJECTS] and [AREAS].

### Step 5 — Create onboarding note

Use the **obsidian-vault MCP** to create `00_START_HERE.md`:

Content in [LANG] explaining:
- Their profile and what it's optimized for
- Folder structure and what goes where
- How `/second-brain-capture` automatically routes notes for their profile
- The 5 available skills
- "Try capturing your first note: type `/second-brain-capture` and tell me something you learned or decided recently"

### Step 6 — Install skills permanently into vault

Use the **Write tool** (filesystem) to copy all skills into `[VAULT_PATH]/.claude/commands/`.

Read each file first, then write to the vault path:
- `second-brain-capture.md` → `[VAULT_PATH]/.claude/commands/second-brain-capture.md`
- `link-finder.md` → `[VAULT_PATH]/.claude/commands/link-finder.md`
- `vault-synthesis.md` → `[VAULT_PATH]/.claude/commands/vault-synthesis.md`
- `next-steps-ai.md` → `[VAULT_PATH]/.claude/commands/next-steps-ai.md`
- `explore-skills.md` → `[VAULT_PATH]/.claude/commands/explore-skills.md`

Also copy the vault-profile config:
- `[VAULT_PATH]/.claude/vault-profile.md` (created in Step 2)

---

## PHASE 5 — HANDOFF

After all steps complete, say:

```
✅ Your second brain is ready!

Profile: [PROFILE]
Language: [LANG]

What was built:
📁 [list all folders]
📝 Home.md + 00_START_HERE.md
📝 [hub notes created]
⚡ 5 skills installed and profile-aware

---

🎯 Your skills now know your structure.

When you use /second-brain-capture, notes go automatically to the right folder
and get linked to the right places — based on your [PROFILE] profile.

Try it now: tell me something you learned, decided, or want to remember.
```

**Important:** From now on, open your Obsidian vault folder in Claude Code (`claude /path/to/vault`), not this repo. Your skills and profile config live in the vault.
