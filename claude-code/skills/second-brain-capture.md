# Skill: /second-brain-capture

Capture insights, solutions, and decisions as linked notes in under 2 seconds.

---

## When user runs `/second-brain-capture [input]`

Or when user says "I learned / I realized / I decided / I discovered..."

### Step 1 — Detect type
Analyze input and classify:
- **INSIGHT** — a realization, pattern, or learning
- **SOLUTION** — a fix, workaround, or technical answer
- **DECISION** — a choice made with reasoning

### Step 2 — Detect project
Search for project keywords in the input. If none found, ask.

### Step 3 — Propose (ask for confirmation)
```
📝 Capturing...

Type: INSIGHT
Project: [detected project]
Folder: 03_Knowledge/Insights/
Title: [auto-generated title]

OK? [yes / adjust]
```

### Step 4 — Create note
After confirmation, create note via obsidian-sync-mcp:

```markdown
---
type: insight | solution | decision
project: [project]
created: [date]
status: validated
tags: [auto-generated]
---

# [Title]

[User's input, formatted]

## Related
[[related-note-1]] [[related-note-2]] [[related-note-3]]
```

### Step 5 — Auto-link
Search vault for 3-5 related notes by keyword/project match and add wikilinks.

### Step 6 — Confirm
```
✓ Captured: [title]
  Linked to: [[note-1]], [[note-2]], [[note-3]]
```

---

## Folders by type

| Type | Folder |
|---|---|
| INSIGHT | `03_Knowledge/Insights/` |
| SOLUTION | `03_Knowledge/Soluciones/` |
| DECISION | `03_Knowledge/Decisiones/` |
| CONCEPT | `03_Knowledge/Conceptos/` |
