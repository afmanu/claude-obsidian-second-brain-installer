Capture an insight, solution, or decision as a linked note in Obsidian in under 2 seconds.

## Usage
`/second-brain-capture [your insight/decision/solution]`

Or just say "I learned / I realized / I decided / I discovered..." and this skill triggers.

---

## Steps

**1. Classify the input:**
- INSIGHT → realization, pattern, or learning → `03_Knowledge/Insights/`
- SOLUTION → fix, workaround, technical answer → `03_Knowledge/Soluciones/`
- DECISION → a choice made with reasoning → `03_Knowledge/Decisiones/`
- CONCEPT → definition or framework → `03_Knowledge/Conceptos/`

**2. Detect project** from keywords. If unclear, ask.

**3. Generate title** — short, descriptive, slug-friendly.

**4. Propose (wait for confirmation):**
```
📝 Capturing...

Type:    INSIGHT
Project: [project]
Folder:  03_Knowledge/Insights/
Title:   [auto-title]

OK? [yes / adjust]
```

**5. Create note via `obsidian-vault` MCP:**
```markdown
---
type: insight
project: [project]
created: [YYYY-MM-DD]
status: validated
tags: []
---

# [Title]

[User's input, lightly formatted]

## Related
```

**6. Auto-link** — search vault for 3-5 notes with matching keywords or same project. Add as wikilinks under `## Related`.

**7. Confirm:**
```
✓ Captured: [title]
  Linked to: [[note-1]], [[note-2]], [[note-3]]
```
