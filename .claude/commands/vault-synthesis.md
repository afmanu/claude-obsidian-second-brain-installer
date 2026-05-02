Generate a monthly synthesis report with patterns, insights, and actionable recommendations.

Runs automatically on the 1st of each month, or on-demand when called.

---

## Steps

**1. Collect** — use `obsidian-vault` MCP to get all notes from the previous month (or current month if on-demand).

**2. Analyze:**
- Recurring keywords and themes → patterns
- Notes with `type: insight` → key learnings
- Notes with `type: decision` → outcomes (if annotated)
- Projects with most activity

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
| Project | Notes this month | Status |
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
