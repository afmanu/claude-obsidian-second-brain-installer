# /second-brain-capture

You are running the second-brain capture skill. Follow these steps exactly.

---

## STEP 1 — READ VAULT PROFILE

Read `.claude/vault-profile.md` in the current vault using the **obsidian-vault MCP** (`mcp__obsidian-vault__read_note`).

Extract:
- [PROFILE]: the user's profile (consultant, developer, researcher, entrepreneur, student, personal)
- [LANG]: the language setting
- [ROUTING_RULES]: the routing rules table
- [LINK_RULES]: the link rules table
- [STRUCTURE]: the folder structure

If vault-profile.md doesn't exist, say: "I don't see a vault profile yet. Run `/vault-install` first to set up your second brain."

---

## STEP 2 — CLASSIFY THE INPUT

Analyze what the user shared. Determine:

**Type** — pick one:
- `insight` — something they learned or realized
- `solution` — a fix or approach to a problem
- `decision` — a choice they made
- `meeting` — notes from a meeting or conversation
- `idea` — a new idea or hypothesis
- `reference` — something to remember from a source (book, article, etc.)
- `task` — something to do
- `goal` — a goal or intention
- `reflection` — a personal reflection

**Topic** — what is it about? Extract 2-3 keywords.

**Project or area** — does it belong to a specific project or life area they've mentioned?

---

## STEP 3 — APPLY ROUTING RULES

Using [ROUTING_RULES] from the vault profile:

1. Match the note type and topic against the routing table
2. Determine the destination folder
3. If a client/project/course is mentioned, use the specific subfolder (e.g. `01_Clients/ClientName/Meetings/`)
4. If no rule matches exactly, pick the closest folder and flag it

---

## STEP 4 — PROPOSE TO USER

Say:

```
Type: [TYPE]
Folder: [DESTINATION_FOLDER]
Title: [suggested-note-title]
Links to: [2-3 notes this should link to, based on LINK_RULES]

OK? [Yes / Adjust]
```

Wait for confirmation. If user adjusts, update accordingly.

---

## STEP 5 — CREATE NOTE

Use the **obsidian-vault MCP** (`mcp__obsidian-vault__write_note`) to create the note.

**Path:** `[DESTINATION_FOLDER]/[YYYY-MM-DD]-[slug].md`

**Frontmatter:**
```yaml
type: [TYPE]
profile: [PROFILE]
project: [project if applicable]
created: [today's date]
tags: [2-3 relevant tags based on topic]
```

**Content structure** (write in [LANG]):

For `insight` / `solution` / `decision`:
```markdown
# [Title]

## [Summary / Resumen]
[user's input, formatted clearly]

## [Context / Contexto]
[brief context if inferable]

## [Related / Relacionado]
[wikilinks from LINK_RULES]
```

For `meeting`:
```markdown
# [Meeting Title] — [Date]

## [Key Points / Puntos clave]
[extracted from user input]

## [Commitments / Compromisos]
-

## [Next Steps / Próximos pasos]
- [ ]

## [Related / Relacionado]
[wikilinks from LINK_RULES]
```

For `idea` / `goal` / `reflection`:
```markdown
# [Title]

[user's input]

## [Why it matters / Por qué importa]
[brief reasoning if inferable]

## [Related / Relacionado]
[wikilinks from LINK_RULES]
```

---

## STEP 6 — CREATE WIKILINKS

After creating the note, apply the [LINK_RULES] from the vault profile:

1. For each linked note in [LINK_RULES], check if it exists using `mcp__obsidian-vault__read_note`
2. If it exists: use `mcp__obsidian-vault__patch_note` to add a backlink to the new note
3. If it doesn't exist: skip silently (don't create empty hub notes)

---

## STEP 7 — CONFIRM

Say:

```
✓ Captured: [note title]
  → [destination folder]
  → Linked to: [list of wikilinks created]
```

If any linked notes didn't exist yet, mention: "Note: [X] doesn't exist yet — link will activate when you create it."
