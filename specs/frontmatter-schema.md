# Frontmatter Schema

This document defines the recommended frontmatter schema for notes created by Claude Obsidian Second Brain.

The goal is not to force every note to use every field. The goal is to keep enough structure for routing, linking, synthesis, decision review, and next-step generation.

---

## Core principles

1. Every generated note should include frontmatter.
2. Every generated note should include at least `type`, `created`, and `tags`.
3. Profile-aware notes should include `profile`.
4. Project-aware notes should include `project`.
5. Area-aware notes should include `area`.
6. Decisions should include enough metadata to review outcomes later.
7. Tasks and goals should include status when useful.
8. Source-based notes should include source metadata.

---

## Universal fields

These fields can appear on any generated note.

```yaml
type: insight | solution | decision | meeting | idea | reference | task | goal | reflection | concept | project | process | template | learning | methodology | bug-fix | pattern | snippet | architecture | course-note | literature-note | permanent-note | argument | question | contradiction | product-idea | customer-feedback | campaign | content-idea | team-note | metric | daily-journal | weekly-review | habit | finance-note | person-note | lesson | gratitude | book-note | quote
profile: consultant | developer | researcher | entrepreneur | student | personal
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag-one, tag-two]
status: active | inactive | blocked | pending | completed | archived
priority: low | medium | high
confidence: low | medium | high
```

### Required minimum

For most notes:

```yaml
type: [note type]
profile: [selected profile]
created: YYYY-MM-DD
tags: []
```

---

## Project and area fields

Use these when the note belongs to a project, client, product, course, or life/work area.

```yaml
project: [project name]
client: [client name]
product: [product name]
course: [course name]
area: [area name]
service: [service name]
```

Rules:

- Use real names provided by the user.
- Do not invent clients, projects, or products.
- If uncertain, leave the field empty or ask the user.

---

## Decision fields

Use for notes with `type: decision`.

```yaml
type: decision
profile: [selected profile]
created: YYYY-MM-DD
project: [optional]
area: [optional]
decision_status: pending | validated | reversed | abandoned
outcome: pending | good | bad | mixed
review_date: YYYY-MM-DD
confidence: low | medium | high
tags: []
```

Recommended note sections:

```markdown
# [Decision Title]

## Decision
[What was decided]

## Context
[Why this decision matters]

## Options Considered
- Option A
- Option B

## Reasoning
[Reasoning behind the decision]

## Expected Outcome
[What should happen if this was a good decision]

## Review
[To be filled later]

## Related
[[related-note]]
```

---

## Meeting fields

Use for notes with `type: meeting`.

```yaml
type: meeting
profile: [selected profile]
created: YYYY-MM-DD
project: [optional]
client: [optional]
attendees: []
status: completed
tags: []
```

Recommended note sections:

```markdown
# [Meeting Title] — [Date]

## Key Points
-

## Decisions
-

## Action Items
- [ ]

## Risks
-

## Related
[[related-note]]
```

---

## Source/reference fields

Use for notes based on books, articles, URLs, papers, podcasts, videos, or external references.

```yaml
type: reference | literature-note | book-note
profile: [selected profile]
created: YYYY-MM-DD
source_type: book | article | paper | podcast | video | url | other
source_title: [title]
source_author: [author]
source_url: [url]
source_date: YYYY-MM-DD
captured_date: YYYY-MM-DD
tags: []
```

Recommended note sections:

```markdown
# [Source Title]

## Summary
[Short summary]

## Key Ideas
-

## Useful For
[How this connects to the user's work or knowledge system]

## Related
[[related-note]]
```

---

## Task fields

Use for actionable notes or notes that primarily define work to do.

```yaml
type: task
profile: [selected profile]
created: YYYY-MM-DD
project: [optional]
area: [optional]
status: pending | active | blocked | completed
due: YYYY-MM-DD
priority: low | medium | high
tags: []
```

Recommended note sections:

```markdown
# [Task Title]

## Outcome
[What must be true when this is done]

## Context
[Why this task exists]

## Steps
- [ ]

## Blockers
-

## Related
[[related-note]]
```

---

## Goal fields

Use for goals, objectives, intentions, or strategic outcomes.

```yaml
type: goal
profile: [selected profile]
created: YYYY-MM-DD
area: [optional]
project: [optional]
status: active | blocked | completed | archived
time_horizon: daily | weekly | monthly | quarterly | yearly
review_date: YYYY-MM-DD
tags: []
```

Recommended note sections:

```markdown
# [Goal Title]

## Goal
[What the user wants to achieve]

## Why It Matters
[Why this matters]

## Success Criteria
-

## Next Actions
- [ ]

## Related
[[related-note]]
```

---

## Profile-specific note type mapping

The capture command may classify a user input into a generic type first. Then it should map that type to the selected profile when needed.

| Generic type | Consultant | Developer | Researcher | Entrepreneur | Student | Personal |
|---|---|---|---|---|---|---|
| insight | learning | concept | permanent-note | learning | concept | lesson |
| solution | process | bug-fix / pattern | permanent-note | process | concept | lesson |
| decision | project / proposal | decision | argument | decision | project-note | goal / lesson |
| meeting | meeting | daily / project-note | project-note | team-note | project-note | person-note |
| idea | methodology | pattern | permanent-note | product-idea / content-idea | concept | reflection |
| reference | reference | concept | literature-note | learning | resource | book-note |
| task | project | project-note | project-note | process | exercise | goal |
| goal | project | project | project | strategy | course / project | goal |
| reflection | learning | learning | permanent-note | learning | summary | reflection |

If the mapping is ambiguous, Claude should ask the user or choose the closest routing rule and flag the uncertainty.

---

## Status values

Use these consistently:

| Status | Meaning |
|---|---|
| `pending` | Not started or waiting |
| `active` | Currently in progress |
| `blocked` | Cannot progress without resolving something |
| `completed` | Done |
| `archived` | No longer active but retained |
| `inactive` | Not currently active, but not formally archived |

---

## Outcome values

Use mainly for decisions and experiments:

| Outcome | Meaning |
|---|---|
| `pending` | Not reviewed yet |
| `good` | Produced the expected or positive result |
| `bad` | Produced a negative result |
| `mixed` | Partially successful or unclear |

---

## Tag rules

Tags should be:

- lowercase,
- short,
- stable,
- useful for retrieval.

Examples:

```yaml
tags: [strategy, client-work, automation]
tags: [research, prompting, paper]
tags: [health, habit, reflection]
```

Avoid creating too many one-off tags.

---

## Language rules

If `[LANG]` is English:

- folder names should be English,
- note headings should be English,
- generated note content should be English unless the user input is clearly in another language.

If `[LANG]` is Spanish:

- folder names should be Spanish,
- note headings should be Spanish,
- generated note content should be Spanish.

If `[LANG]` is Mixed:

- folder names should be English,
- generated note content should follow the user's language, usually Spanish if the user writes in Spanish.
