# /second-brain-capture

Capture a user input and turn it into a structured, profile-aware, linked Obsidian note.

This command must follow the global command contract:

- read `.claude/vault-profile.md` first,
- respect the user's selected language,
- use the `obsidian-vault` MCP for Obsidian notes,
- use the filesystem Read/Write tools for `.claude/`, command files, docs, and configuration,
- propose before creating a note,
- never delete or overwrite user content without explicit confirmation.

---

## STEP 1 — Read vault profile

Read this file from the current vault using the filesystem Read tool:

```text
.claude/vault-profile.md
```

Extract:

- `[PROFILE]`: consultant, developer, researcher, entrepreneur, student, or personal
- `[LANG]`: English, Spanish, or Mixed
- `[VAULT_PATH]`
- `[STRUCTURE]`
- `[ROUTING_RULES]`
- `[LINK_RULES]`

If `.claude/vault-profile.md` does not exist, stop and say:

```text
I do not see a vault profile yet. Run /vault-install first to set up your second brain.
```

---

## STEP 2 — Classify the input

Analyze what the user shared.

First classify it into one generic type:

- `insight` — something learned or realized
- `solution` — a fix, workaround, or approach to a problem
- `decision` — a choice made with reasoning
- `meeting` — notes from a meeting or conversation
- `idea` — a new idea, hypothesis, or possibility
- `reference` — something captured from a source
- `task` — something to do
- `goal` — a goal, objective, or intention
- `reflection` — personal or strategic reflection

Extract:

- `[GENERIC_TYPE]`
- `[TOPIC]`: 2-3 stable keywords
- `[PROJECT]`: if applicable
- `[CLIENT]`: if applicable
- `[PRODUCT]`: if applicable
- `[COURSE]`: if applicable
- `[AREA]`: if applicable
- `[SOURCE]`: if applicable

---

## STEP 3 — Map to profile-specific type

Map `[GENERIC_TYPE]` to the selected profile when needed.

Use this mapping unless `[ROUTING_RULES]` clearly indicate a better destination:

| Generic type | Consultant | Developer | Researcher | Entrepreneur | Student | Personal |
|---|---|---|---|---|---|---|
| insight | learning | concept | permanent-note | learning | concept | lesson |
| solution | process | bug-fix or pattern | permanent-note | process | concept | lesson |
| decision | project or proposal | decision | argument | decision | project-note | goal or lesson |
| meeting | meeting | daily or project-note | project-note | team-note | project-note | person-note |
| idea | methodology | pattern | permanent-note | product-idea or content-idea | concept | reflection |
| reference | reference | concept | literature-note | learning | resource | book-note |
| task | project | project-note | project-note | process | exercise | goal |
| goal | project | project | project | strategy | course or project | goal |
| reflection | learning | learning | permanent-note | learning | summary | reflection |

Store the final note type as `[TYPE]`.

If the mapping is ambiguous, choose the closest routing rule, flag the uncertainty in the proposal, and allow the user to adjust.

---

## STEP 4 — Apply routing rules

Using `[ROUTING_RULES]` from `.claude/vault-profile.md`:

1. Match `[TYPE]`, `[GENERIC_TYPE]`, `[TOPIC]`, and detected project/client/product/course/area against the routing table.
2. Determine `[DESTINATION_FOLDER]`.
3. Use specific subfolders when the profile defines them, for example client, project, product, course, or area subfolders.
4. If no exact rule matches, choose the closest folder and mark it as `routing_uncertain: true` in your internal reasoning and in the proposal.

Do not invent client, project, product, course, service, or area names.

If destination cannot be inferred safely, ask one focused question.

---

## STEP 5 — Generate note title, slug, tags, and links

Generate:

- `[TITLE]`: short, descriptive title
- `[SLUG]`: lowercase, hyphenated, file-safe slug
- `[TAGS]`: 2-4 stable lowercase tags
- `[PROPOSED_LINKS]`: 2-3 likely wikilinks based on `[LINK_RULES]`, existing hub notes, project notes, and related topics

Avoid one-off tags unless they are genuinely useful.

---

## STEP 6 — Propose to user

Before creating anything, show:

```text
Type: [TYPE]
Folder: [DESTINATION_FOLDER]
Title: [TITLE]
Tags: [TAGS]
Links to: [PROPOSED_LINKS]

OK? [yes / adjust]
```

If routing is uncertain, add:

```text
Routing note: I am not fully certain this is the best folder. You can adjust it before I create the note.
```

Wait for confirmation.

If the user adjusts type, folder, title, tags, or links, apply the adjustment before writing.

Do not create the note before confirmation.

---

## STEP 7 — Create note

Use the `obsidian-vault` MCP to create the note.

Path:

```text
[DESTINATION_FOLDER]/[YYYY-MM-DD]-[SLUG].md
```

Use frontmatter compatible with this minimum schema:

```yaml
type: [TYPE]
profile: [PROFILE]
created: [YYYY-MM-DD]
tags: [TAGS]
```

Add optional fields only when known:

```yaml
project: [PROJECT]
client: [CLIENT]
product: [PRODUCT]
course: [COURSE]
area: [AREA]
source: [SOURCE]
status: [pending | active | blocked | completed | archived]
priority: [low | medium | high]
confidence: [low | medium | high]
```

For decisions, include when useful:

```yaml
decision_status: pending
outcome: pending
review_date: [YYYY-MM-DD if inferable]
```

---

## STEP 8 — Content templates

Write headings in `[LANG]`.

If `[LANG]` is Mixed, keep folder structure in English and write note content in the user's language.

### Insight, solution, learning, lesson, concept, pattern, methodology

```markdown
# [TITLE]

## Summary
[user input, cleaned and structured]

## Context
[brief context if inferable]

## Why it matters
[why this is useful]

## Related
[PROPOSED_LINKS]
```

### Decision

```markdown
# [TITLE]

## Decision
[what was decided]

## Context
[why this decision matters]

## Reasoning
[reasoning behind the decision]

## Expected outcome
[what should happen if this is a good decision]

## Review
[to be completed later]

## Related
[PROPOSED_LINKS]
```

### Meeting

```markdown
# [TITLE] — [YYYY-MM-DD]

## Key points
-

## Decisions
-

## Action items
- [ ]

## Risks
-

## Related
[PROPOSED_LINKS]
```

### Idea, goal, task, reflection

```markdown
# [TITLE]

## Capture
[user input, cleaned and structured]

## Why it matters
[brief reasoning if inferable]

## Next actions
- [ ]

## Related
[PROPOSED_LINKS]
```

### Reference or source-based note

```markdown
# [TITLE]

## Summary
[short summary]

## Key ideas
-

## Useful for
[how this connects to the user's work or knowledge system]

## Related
[PROPOSED_LINKS]
```

---

## STEP 9 — Create wikilinks and backlinks

After creating the note:

1. For each proposed linked note, check whether it exists using the `obsidian-vault` MCP.
2. If it exists, use `patch_note` to add a backlink to the new note when appropriate.
3. If it does not exist, keep the wikilink in the new note but do not create an empty note.
4. Do not silently create hub notes or placeholder notes.

---

## STEP 10 — Confirm

Say:

```text
Captured: [TITLE]
Path: [DESTINATION_FOLDER]/[YYYY-MM-DD]-[SLUG].md
Linked to: [created backlinks or proposed wikilinks]
```

If any linked notes did not exist, say:

```text
Some links point to notes that do not exist yet. They will become active when those notes are created.
```
