# Skill: /decision-tracker

Audit past decisions, track outcomes, and identify patterns of success and failure.

---

## When user runs `/decision-tracker`

### Step 1 — Find all decisions
Search vault for notes with `type: decision` in frontmatter.

### Step 2 — Find outcomes
For each decision, search future notes for outcome annotations:
- Look for: `outcome: good | bad | mixed | pending`
- Or infer from text mentions of the decision topic

### Step 3 — Calculate stats
```
DECISION OUTCOMES:

Recent decisions:
  ✓ GOOD    — Retainer pricing (3 mo ago) → +40% revenue
  ✓ GOOD    — REST vs GraphQL (2 mo ago) → smooth migration
  ⚠ MIXED   — Hire freelancer (1 mo ago) → 50% success
  ⏳ PENDING — New tool adoption (2 wk ago)

SUCCESS RATE BY CATEGORY:
  Technical:  85%  (6/7 good)
  Business:   60%  (3/5 good)
  Hiring:     50%  (1/2 good)
  Personal:   75%  (3/4 good)

PATTERNS OF ERROR:
  - No trial period defined → 100% failure rate
  - Decisions made under time pressure → 2x reversal rate
  - Missing written reasoning → harder to evaluate outcome
```

### Step 4 — Recommendations
```
SUGGESTIONS:
  1. Add trial period to any new hiring decision
  2. Write explicit success criteria before deciding
  3. Review these 3 pending decisions: [list]
```
