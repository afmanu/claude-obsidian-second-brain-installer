# Skill: /vault-synthesis

Generate a monthly synthesis report with patterns, insights, and recommendations.

---

## When user runs `/vault-synthesis`

Or automatically on the 1st of each month at 9 AM.

### Step 1 — Collect notes
Get all notes created or modified in the previous month.

### Step 2 — Analyze
Extract:
- Recurring themes and keywords (patterns)
- Notes tagged as insight/solution/decision
- Decisions with outcome annotations
- Projects with most activity

### Step 3 — Generate report
Create `05_Monthly/[YYYY-MM]-synthesis.md`:

```markdown
---
type: synthesis
period: [YYYY-MM]
created: [date]
tags: [monthly, synthesis, review]
---

# Synthesis — [Month YYYY]

## PATTERNS DETECTED
- **[Pattern 1]:** [description] — appeared in [N] notes
- **[Pattern 2]:** [description] — appeared in [N] notes

## KEY INSIGHTS
- [Insight extracted from notes]
- [Insight extracted from notes]

## DECISIONS + OUTCOMES
- **[Decision]:** ✓ GOOD / ❌ BAD / ⏳ PENDING
  - [Why it worked or didn't]

## PROJECT HEALTH
| Project | Notes this month | Status |
|---|---|---|
| [project] | [N] | active/stalled |

## RECOMMENDATIONS
1. [Actionable recommendation based on patterns]
2. [Actionable recommendation based on decisions]
3. [Actionable recommendation based on gaps]
```

### Step 4 — Notify
```
✓ Monthly synthesis ready: [[05_Monthly/[YYYY-MM]-synthesis]]
  - [N] notes analyzed
  - [N] patterns detected
  - [N] recommendations
```
