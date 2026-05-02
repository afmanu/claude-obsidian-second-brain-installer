Find orphan notes in the vault and suggest connections with confidence scores.

---

## Steps

**1. Scan** — use `obsidian-vault` MCP to get the last 20 modified notes.

**2. Find orphans** — notes with no wikilinks in or out.

**3. Score connections** for each orphan (0–100%):
- Keyword overlap with other notes → up to 80%
- Same project in frontmatter → +10%
- Same area → +5%

**4. Show top suggestions:**
```
🔗 Found [N] orphan notes. Top connections:

orphan-note-1.md
  ├─ 92% → [[related-note-a]]
  ├─ 87% → [[related-note-b]]
  └─ 71% → [[related-note-c]]

orphan-note-2.md
  └─ 88% → [[related-note-d]]

Auto-link all? [yes] [review one by one] [skip]
```

**5. Execute** via `obsidian-vault` MCP patch_note:
- "yes" → add all wikilinks at once
- "review" → walk through each pair
- "skip" → exit

**6. Confirm:**
```
✓ [N] notes linked. [N] orphans remain (below 60% confidence).
```
