# /vault-synthesis

Generate a profile-aware synthesis report from the vault.

This command must follow the global command contract:

- read `.claude/vault-profile.md` first,
- respect the user's selected language,
- use the `obsidian-vault` MCP for Obsidian notes,
- use profile structure instead of hardcoded folders,
- generate a report only when the user asks for synthesis or review.

---

## STEP 1 — Read vault profile

Read this file from the current vault using the filesystem Read tool:

```text
.claude/vault-profile.md
```

Extract:

- `[PROFILE]`
- `[LANG]`
- `[VAULT_PATH]`
- `[STRUCTURE]`
- `[ROUTING_RULES]`
- `[LINK_RULES]`

If `.claude/vault-profile.md` does not exist, stop and say:

```text
I do not see a vault profile yet. Run /vault-install first to set up your second brain.
```

---

## STEP 2 — Determine synthesis scope

If the user specified a period, use it.

If no period is specified, ask:

```text
What period should I synthesize?

A) Last 7 days
B) Last 30 days
C) This month
D) Custom period
```

If the user gives no preference, default to the last 30 days.

Optional scopes:

- entire vault,
- specific project,
- specific client,
- specific product,
- specific course,
- specific area,
- specific folder.

---

## STEP 3 — Collect notes

Use the `obsidian-vault` MCP to collect notes in scope.

Ignore system folders unless explicitly requested:

```text
.claude/
docs/
```

For each note, extract:

- title,
- path,
- type,
- profile,
- created date,
- updated date if available,
- status,
- outcome,
- project/client/product/course/area,
- tags,
- wikilinks,
- key content.

---

## STEP 4 — Analyze

Analyze:

- recurring themes and keywords,
- key insights,
- decisions and outcomes,
- active projects or areas,
- stalled projects or areas,
- blockers,
- orphan or weakly connected notes,
- knowledge gaps,
- repeated references without a dedicated note,
- useful next actions.

Use profile context:

- Consultant: clients, meetings, proposals, services, operations.
- Developer: bugs, patterns, architecture, codebase, learning.
- Researcher: literature, permanent notes, arguments, questions, contradictions.
- Entrepreneur: strategy, products, customers, marketing, team, finance.
- Student: courses, concepts, exercises, resources, exams.
- Personal: journal, goals, habits, areas, reflections.

---

## STEP 5 — Choose report destination

Use the selected profile structure.

Preferred destinations by profile:

| Profile | Preferred destination |
|---|---|
| consultant | `04_Knowledge/Learnings/` or closest mapped knowledge/reports folder |
| developer | `04_Learning/` or closest mapped learning/reports folder |
| researcher | `02_Permanent/` or `03_Projects/[project]/` if project-scoped |
| entrepreneur | `01_Strategy/` or closest strategy/reports folder |
| student | `01_Courses/[course]/Summaries/` if course-scoped, otherwise `02_Concepts/` or closest learning folder |
| personal | `01_Journal/Monthly/` or closest journal/review folder |

If no suitable folder exists, create or use:

```text
[VAULT_PATH]/Reports/
```

with the filesystem Write tool for the folder and `.gitkeep`, then create the report note through the `obsidian-vault` MCP.

Report file name:

```text
[YYYY-MM-DD]-synthesis-[scope-slug].md
```

---

## STEP 6 — Create synthesis report

Use the `obsidian-vault` MCP to create the report.

Use frontmatter:

```yaml
type: synthesis
profile: [PROFILE]
created: [YYYY-MM-DD]
period: [period]
scope: [scope]
tags: [synthesis, review]
```

Use headings in `[LANG]`.

Report structure:

```markdown
# Synthesis — [Period / Scope]

## Patterns detected
- [Pattern]: [description] — found in [N] notes

## Key insights
- [Insight extracted from notes]

## Decisions and outcomes
- [Decision]: [good / bad / mixed / pending] — [reason]

## Project / area health
| Project / Area | Notes this period | Status | Comment |
|---|---:|---|---|

## Knowledge gaps
- [Gap] — why it matters

## Weak links or orphan notes
- [[note]] — suggested next link/action

## Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]
3. [Actionable recommendation]
```

If there is not enough information, create a lighter report and explicitly say what was missing.

---

## STEP 7 — Confirm

Say:

```text
Synthesis ready.
Path: [REPORT_PATH]
Notes analyzed: [N]
Patterns found: [N]
Recommendations: [N]
```

If the report used a fallback `Reports/` folder, mention it:

```text
I used a fallback Reports folder because this profile did not define a dedicated synthesis folder.
```
