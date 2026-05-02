# Skill: /next-steps-ai

Suggest 3-5 next steps ordered by impact based on your current vault state.

---

## When user runs `/next-steps-ai`

### Step 1 — Analyze current state
Gather context from vault:
- Projects: count recent notes → estimate % completion
- Blockers: notes tagged `status: blocked`
- Knowledge gaps: topics referenced but no note exists
- Recent focus: last 5-10 notes created

### Step 2 — Score possible next steps
For each candidate action, calculate impact score:
- Unblocks other work → HIGH (80-100)
- Aligns with current focus → MEDIUM-HIGH (60-80)
- Fills a knowledge gap → MEDIUM (40-60)
- Routine maintenance → LOW (20-40)

### Step 3 — Show ranked suggestions
```
🎯 NEXT STEPS (by impact):

1. [HIGH]   Complete [task] → unblocks [project]
2. [HIGH]   Review outcome of [decision] → overdue 3 weeks
3. [MEDIUM] Link [[orphan-note]] → 92% relevant to current work
4. [MEDIUM] Document [concept] → referenced 4x but no note
5. [LOW]    Run /link-finder → 8 orphans detected

Pick 1-2 to work on now.
```

### Step 4 — Optional drill-down
If user picks a suggestion: provide more detail or start the work.
