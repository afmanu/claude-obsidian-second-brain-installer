# Skill: /forgotten-notes

Resurface old notes ranked by relevance to your current context.

---

## When user runs `/forgotten-notes`

### Step 1 — Find old notes
Get all notes not modified in the last 30 days.

### Step 2 — Score relevance
For each old note, calculate relevance score (0-100%):
- Linked by other notes (importance) → up to 40%
- Keyword similarity to recent notes → up to 35%
- Keyword similarity to active projects → up to 25%

### Step 3 — Show top 5
```
📚 Notes you haven't seen in 30+ days:

HIGH RELEVANCE:
  92% — [[decision-remote-vs-office]] (47 days ago)
  87% — [[concept-rapid-prototyping]] (62 days ago)

MEDIUM RELEVANCE:
  71% — [[insight-rust-patterns]] (38 days ago)
  65% — [[solution-memoization]] (55 days ago)
  58% — [[concept-api-design]] (91 days ago)

Open any of these? [note name / skip]
```

### Step 4 — Open
If user names a note: provide direct content or Obsidian URI to open it.
