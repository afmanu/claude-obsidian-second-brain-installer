# /vault-install

You are running the vault installation wizard.

This command runs only after the `obsidian-vault` MCP connection has been configured and verified.

Follow these 5 phases exactly, in order.

---

## Reference Specs

Before doing anything else, read these repository specs:

```text
specs/vault-output-contract.md
specs/frontmatter-schema.md
specs/command-contracts.md
```

Use them as source of truth:

- `specs/vault-output-contract.md` defines the final vault output contract.
- `specs/frontmatter-schema.md` defines generated note metadata and note structure.
- `specs/command-contracts.md` defines required command behavior.

If anything in this command conflicts with the specs, follow the specs unless the user explicitly requests a different behavior.

---

## Preconditions

Before starting, confirm that:

1. `[VAULT_PATH]` is known.
2. `[VAULT_PATH]` exists.
3. The `obsidian-vault` MCP can list the vault root.
4. The repository files are available to read from the installer repository.
5. The repository specs can be read:
   - `specs/vault-output-contract.md`
   - `specs/frontmatter-schema.md`
   - `specs/command-contracts.md`

If any precondition fails, stop and repair setup before continuing.

---

## PHASE 1 — DIAGNOSIS

Ask the user these 3 questions, one at a time. Wait for each answer before asking the next question.

**Question 1:** "What is the main reason you want a second brain? What problem are you trying to solve?"

**Question 2:** "Describe your daily work or life in 2-3 sentences. What do you mostly do?"

**Question 3:** "What kind of information do you capture most? Examples: meetings, ideas, code, notes from books, personal goals, tasks, decisions, client notes."

After receiving all 3 answers, run the internal profile matching below silently. Do not show this scoring logic to the user.

---

### INTERNAL PROFILE MATCHING — silent

Read all 6 profiles from `profiles/` in this repository.

Profile files to read:

- `profiles/consultant.md`
- `profiles/developer.md`
- `profiles/researcher.md`
- `profiles/entrepreneur.md`
- `profiles/student.md`
- `profiles/personal.md`

Match the user's answers against the "Diagnostic Questions" section in each profile file.

Score each profile from 0 to 100:

- Exact keyword match: +25 points
- Intent or concept match: +15 points
- Contradicting signal: -20 points

Select the top-scoring profile and store it as `[PROFILE]`.

Also extract:

- `[PROJECTS]`: projects, clients, courses, products, or major initiatives the user mentioned.
- `[AREAS]`: life or work areas the user mentioned.
- `[PROFILE_REASON]`: 2-4 plain-language reasons why this profile fits.
- `[PROFILE_CONFIDENCE]`: High, Medium, or Low.

If confidence is low, explicitly show the top 2 possible profiles and ask the user to choose.

---

## PHASE 2 — STRUCTURE PROPOSAL

Present the recommended structure.

Say:

```text
Based on what you told me, I recommend the [PROFILE] profile.

Why:
- [reason 1]
- [reason 2]
- [reason 3]

Confidence: [PROFILE_CONFIDENCE]

Recommended structure:

[Show the folder tree from the selected profile file, personalized with the user's actual projects, clients, products, courses, or areas when possible.]

For example, since you mentioned [specific project/client/product/course/area], I would create:
[concrete example folder path]

Does this structure work, or would you like to adjust anything?
```

If the user wants to adjust, accept changes and update the proposed structure.

Store the final structure as `[STRUCTURE]`.

Also show:

```text
Other available profiles:
- Consultant: clients, projects, proposals, meetings, operations
- Developer: codebase, bugs, patterns, architecture, learning
- Researcher: literature notes, permanent notes, arguments, sources
- Entrepreneur: strategy, products, customers, marketing, finance
- Student: courses, concepts, exercises, exams, resources
- Personal: journal, goals, habits, life areas, reflections
```

---

## PHASE 3 — CONFIRM LANGUAGE

Ask:

```text
What language would you like for your vault?

A) English — all folders and notes in English
B) Spanish — todas las carpetas y notas en español
C) Mixed — English structure, Spanish note content
```

Wait for the user's choice.

Store it as `[LANG]`.

Apply the language mapping from the selected profile file, section "Language Mapping", to all folder names and note content.

Then confirm:

```text
Here is what I will build:

Profile: [PROFILE]
Language: [LANG]
Structure:
[final folder list with language-mapped names]

Core vault skills to install:
- /second-brain-capture
- /link-finder
- /vault-synthesis
- /next-steps-ai
- /explore-skills

I will also install:
- CLAUDE.md inside the final vault
- .claude/vault-profile.md
- docs/skills-catalog.md

I will verify the final vault against:
- specs/vault-output-contract.md

Ready to build? [yes / adjust]
```

If the user chooses adjust, apply the requested changes and confirm again.

Do not build until the user confirms.

---

## PHASE 4 — BUILD

Once the user confirms, execute all steps in order.

Use the filesystem Write tool for configuration files and command files.
Use the `obsidian-vault` MCP for Obsidian notes.
Use `specs/frontmatter-schema.md` when creating generated notes.
Use `specs/command-contracts.md` when installing or describing commands.
Use `specs/vault-output-contract.md` when validating the final vault.

---

### Step 1 — Create required system folders

Use the filesystem Write tool to create `.gitkeep` files in these folders:

```text
[VAULT_PATH]/.claude/.gitkeep
[VAULT_PATH]/.claude/commands/.gitkeep
[VAULT_PATH]/docs/.gitkeep
```

---

### Step 2 — Create personalized folder structure

Create all folders from `[STRUCTURE]` using the language-mapped names from the selected profile.

Use the filesystem Write tool to create a `.gitkeep` in each folder:

```text
[VAULT_PATH]/[folder]/.gitkeep
```

If a folder includes user-specific names, use the actual names provided by the user.

---

### Step 3 — Create `.claude/vault-profile.md`

Use the filesystem Write tool, not the MCP, to create:

```text
[VAULT_PATH]/.claude/vault-profile.md
```

Content:

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

## Profile Reason
[PROFILE_REASON]

## Language
[LANG]

## Structure
[list of all created folders with language-mapped names]

## Routing Rules
[copy the full "Routing Rules" table from profiles/[PROFILE].md]

## Link Rules
[copy the full "Link Rules" table from profiles/[PROFILE].md]

## Reference Specs
- specs/vault-output-contract.md
- specs/frontmatter-schema.md
- specs/command-contracts.md
```

This file is the source of truth for all skills inside the final vault.

Every skill must read it before routing notes, suggesting links, or creating reports.

---

### Step 4 — Create final vault `CLAUDE.md`

Use the filesystem Write tool to create:

```text
[VAULT_PATH]/CLAUDE.md
```

Content:

```markdown
# Claude Obsidian Second Brain Vault

You are operating inside the user's Obsidian vault.

Before making profile-aware decisions, always read:

`.claude/vault-profile.md`

## Operating Rules

- Use the `obsidian-vault` MCP to read and write Obsidian notes.
- Use the filesystem Write tool for `.claude/`, command files, docs, and configuration files.
- Respect the user's selected language.
- Propose before creating notes: show title, type, folder, and likely links.
- Use the note metadata patterns defined during installation.
- Follow the installed command contracts.
- Never delete notes or configuration without explicit confirmation.
- Never ask the user to store passwords, seed phrases, private keys, API keys, or sensitive credentials in the vault.

## Installed Commands

- `/second-brain-capture` — capture and route notes
- `/link-finder` — find orphan notes and suggest links
- `/vault-synthesis` — generate synthesis reports
- `/next-steps-ai` — suggest next actions by impact
- `/explore-skills` — browse and build additional skills
```

---

### Step 5 — Copy core skills into the final vault

Read each command file from this installer repository and write it to the final vault:

```text
.claude/commands/second-brain-capture.md -> [VAULT_PATH]/.claude/commands/second-brain-capture.md
.claude/commands/link-finder.md -> [VAULT_PATH]/.claude/commands/link-finder.md
.claude/commands/vault-synthesis.md -> [VAULT_PATH]/.claude/commands/vault-synthesis.md
.claude/commands/next-steps-ai.md -> [VAULT_PATH]/.claude/commands/next-steps-ai.md
.claude/commands/explore-skills.md -> [VAULT_PATH]/.claude/commands/explore-skills.md
```

Do not summarize or rewrite these files unless the user explicitly asks. Copy their full contents.

The installed commands must follow `specs/command-contracts.md`.

---

### Step 6 — Copy the skills catalog into the final vault

Read from this installer repository:

```text
docs/skills-catalog.md
```

Write the full content to:

```text
[VAULT_PATH]/docs/skills-catalog.md
```

This is required because `/explore-skills` depends on this file after handoff.

---

### Step 7 — Create `Home.md`

Use the `obsidian-vault` MCP to create `Home.md` in the vault root.

Content should be in `[LANG]`.

Use the selected profile's hub notes and top-level folders as quick links.

Use frontmatter compatible with `specs/frontmatter-schema.md`.

Suggested structure:

```markdown
---
type: hub
profile: [PROFILE]
created: [today]
tags: [hub, home]
---

# Second Brain

## Quick Access
[links to top-level folders using language-mapped names]

## Active Projects / Areas
[if user mentioned specific projects, clients, products, courses, or areas, list them as wikilinks]

## This Week
(update weekly)
```

---

### Step 8 — Create hub notes

Use the `obsidian-vault` MCP to create the hub notes defined in the selected profile file, section "Hub Notes to Create".

For each hub note:

1. Use frontmatter compatible with `specs/frontmatter-schema.md`.
2. Use the mapped language when needed.
3. Personalize with the user's actual projects, clients, products, courses, or areas.
4. Include useful backlinks to top-level folders.

---

### Step 9 — Create onboarding note

Use the `obsidian-vault` MCP to create:

```text
00_START_HERE.md
```

Use frontmatter compatible with `specs/frontmatter-schema.md`.

Content in `[LANG]` explaining:

- what this vault is for,
- which profile was selected,
- what the folder structure means,
- how `/second-brain-capture` routes notes,
- what the 5 core vault skills do,
- how to open the vault in Claude Code,
- how to capture the first note.

---

### Step 10 — Verify final vault output contract

Read and apply:

```text
specs/vault-output-contract.md
```

Before handoff, verify that the final vault contains all required files, command files, docs, and personalized folders defined there.

At minimum, verify:

```text
[VAULT_PATH]/CLAUDE.md
[VAULT_PATH]/Home.md
[VAULT_PATH]/00_START_HERE.md
[VAULT_PATH]/docs/skills-catalog.md
[VAULT_PATH]/.claude/vault-profile.md
[VAULT_PATH]/.claude/commands/second-brain-capture.md
[VAULT_PATH]/.claude/commands/link-finder.md
[VAULT_PATH]/.claude/commands/vault-synthesis.md
[VAULT_PATH]/.claude/commands/next-steps-ai.md
[VAULT_PATH]/.claude/commands/explore-skills.md
[all folders from STRUCTURE]
```

If any required file or folder is missing, repair it before handoff.

If repair fails, clearly tell the user what is missing.

---

## PHASE 5 — HANDOFF

After verification succeeds, say:

```text
Your second brain is ready.

Profile: [PROFILE]
Language: [LANG]
Vault path: [VAULT_PATH]

What was built:
- Personalized folder structure
- Home.md
- 00_START_HERE.md
- Profile-aware CLAUDE.md
- .claude/vault-profile.md
- Core vault skills
- Skills catalog
- Hub notes for your selected profile

From now on, open your vault directly in Claude Code:

claude "[VAULT_PATH]"

Do not keep working from this installer repository unless you want to update or reinstall the system.

Try your first capture now:
Use /second-brain-capture and tell me something you learned, decided, or want to remember.
```
