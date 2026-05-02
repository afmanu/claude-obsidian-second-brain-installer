# Skill: /link-finder

Find orphan notes and suggest connections with confidence scores.

---

## When user runs `/link-finder`

### Step 1 — Scan recent notes
Get last 20 notes from vault via obsidian-sync-mcp.

### Step 2 — Find orphans
Identify notes with 0 incoming or outgoing wikilinks.

### Step 3 — Score connections
For each orphan, calculate connection score (0-100%):
- Keywords match with other notes → up to 80%
- Same project → +10%
- Same area → +5%

### Step 4 — Show suggestions
```
🔗 Found [N] orphan notes. Top suggestions:

orphan-note-1.md
  ├─ 92% → [[related-note-a]]
  ├─ 87% → [[related-note-b]]
  └─ 71% → [[related-note-c]]

orphan-note-2.md
  ├─ 88% → [[related-note-d]]
  └─ 65% → [[related-note-e]]

Auto-link all? [yes] [review first] [skip]
```

### Step 5 — Execute
If "yes": add wikilinks to all suggested pairs via obsidian-sync-mcp.
If "review first": walk through each one by one.
If "skip": exit.

### Step 6 — Confirm
```
✓ 8 notes linked. 4 orphans remain (below 60% confidence).
```
