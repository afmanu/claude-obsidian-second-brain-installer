# /next-steps-ai

Suggest 3-5 next actions based on the current vault state.

This command must follow the global command contract:

- read `.claude/vault-profile.md` first,
- respect the user's selected language,
- use the `obsidian-vault` MCP for Obsidian notes,
- do not create tasks automatically unless the user asks,
- prioritize actions that unblock real work.

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

## STEP 2 — Determine scope

If the user specified a scope, use it.

Supported scopes:

- entire vault,
- recent notes,
- project,
- client,
- product,
- course,
- area,
- folder,
- current week,
- current month.

If no scope is specified, analyze:

- the last 10 created or modified notes,
- active projects or areas if discoverable,
- blocked notes,
- unresolved decisions,
- weakly linked notes.

---

## STEP 3 — Analyze vault state

Use the `obsidian-vault` MCP to inspect relevant notes.

Look for:

- notes with `status: blocked`,
- notes with `status: active`,
- notes with `type: decision` and `outcome: pending`,
- goals with active or pending status,
- projects or areas with low recent activity,
- repeated topics without a dedicated note,
- orphan or weakly connected notes,
- action items in meeting notes,
- incomplete tasks.

Ignore system folders unless explicitly requested:

```text
.claude/
docs/
```

---

## STEP 4 — Score candidate actions

Generate candidate actions and score them from 0 to 100.

Scoring:

| Signal | Score guidance |
|---|---:|
| Unblocks other work | 80-100 |
| Supports an active project, client, product, course, or goal | 70-90 |
| Resolves or reviews a pending decision | 60-80 |
| Addresses a blocker | 60-80 |
| Fills a recurring knowledge gap | 50-70 |
| Connects orphan or weak notes | 40-60 |
| Routine maintenance | 20-40 |

Profile-specific priorities:

- Consultant: client deliverables, proposals, meeting follow-ups, stalled accounts, reusable processes.
- Developer: bugs, architecture decisions, blocked projects, reusable patterns, missing documentation.
- Researcher: unresolved questions, weak arguments, missing sources, unprocessed literature, contradictions.
- Entrepreneur: strategic decisions, product feedback, customer insights, marketing actions, metrics.
- Student: upcoming reviews, weak concepts, exercises, course summaries, exam prep.
- Personal: goals, habits, weekly review, blocked areas, reflections needing action.

---

## STEP 5 — Show ranked suggestions

Show 3-5 actions ordered by impact.

Format:

```text
Next steps by impact

1. [HIGH | score] [Action]
   Why: [reason]
   Related: [[note]] / [project or area]

2. [MEDIUM | score] [Action]
   Why: [reason]
   Related: [[note]] / [project or area]

3. [LOW | score] [Action]
   Why: [reason]
   Related: [[note]] / [project or area]

Pick 1-2 to work on.
```

Do not create tasks automatically.

---

## STEP 6 — If user picks an action

If the user picks one action:

1. Provide a short execution plan.
2. Ask whether they want to create a note, task, decision review, or project update.
3. If they want to create something, propose the note first using `/second-brain-capture` style:

```text
Type: [TYPE]
Folder: [DESTINATION_FOLDER]
Title: [TITLE]
Tags: [TAGS]
Links to: [PROPOSED_LINKS]

OK? [yes / adjust]
```

4. Only create it after confirmation.

---

## STEP 7 — If there is not enough information

If the vault does not contain enough notes or metadata, say:

```text
I do not have enough structured vault data to make strong next-step recommendations yet.

Best first actions:
1. Capture 3-5 important current projects, decisions, or goals with /second-brain-capture.
2. Run /link-finder after a few notes exist.
3. Run /vault-synthesis after at least one week of captures.
```

Do not fabricate project status or blockers.
