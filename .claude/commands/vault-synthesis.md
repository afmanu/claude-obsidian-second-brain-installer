Generate a synthesis report of your vault with patterns, insights, and actionable recommendations.

Run on-demand whenever you want a review of your knowledge base.

---

## Steps

**1. Collect** — use `obsidian-vault` MCP to get all notes from the last 30 days (or a period the user specifies).

**2. Analyze:**
- Recurring keywords and themes → patterns
- Notes with `type: insight` → key learnings
- Notes with `type: decision` → outcomes (if annotated)
- Projects with most activity vs. stalled ones

**3. Create report** via MCP at `05_Monthly/[YYYY-MM]-synthesis.md`:

```markdown
---
type: synthesis
period: [YYYY-MM]
created: [date]
tags: [monthly, synthesis]
---

# Synthesis — [Month YYYY]

## PATTERNS DETECTED
- **[Pattern]:** [description] — found in [N] notes

## KEY INSIGHTS
- [Insight extracted from notes]

## DECISIONS + OUTCOMES
- **[Decision]:** ✓ GOOD / ❌ BAD / ⏳ PENDING

## PROJECT HEALTH
| Project | Notes this period | Status |
|---|---|---|

## RECOMMENDATIONS
1. [Actionable based on patterns]
2. [Actionable based on decisions]
3. [Actionable based on gaps]
```

**4. Notify:**
```
✓ Synthesis ready: [[05_Monthly/[YYYY-MM]-synthesis]]
  [N] notes analyzed · [N] patterns · [N] recommendations
```
