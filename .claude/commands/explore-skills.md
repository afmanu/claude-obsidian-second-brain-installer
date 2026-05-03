# /explore-skills

Browse the skills catalog and build optional Claude Code commands into the final vault.

This command must follow the global command contract:

- read `.claude/vault-profile.md` first,
- read `docs/skills-catalog.md` from the final vault,
- use the filesystem Write tool for `.claude/commands/`,
- show a skill spec before building it,
- never overwrite existing command files without confirmation.

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

## STEP 2 — Read skills catalog

Read this file from the current vault using the filesystem Read tool:

```text
docs/skills-catalog.md
```

Do not read it through the Obsidian MCP unless the filesystem Read tool is unavailable.

If the file does not exist, say:

```text
I cannot find docs/skills-catalog.md in this vault. The installer may not have copied the skills catalog.

If the installer repository is available, I can copy docs/skills-catalog.md from the installer into this vault. Otherwise, I can recreate a minimal catalog.
```

Ask before recreating or copying the catalog.

---

## STEP 3 — Show installed and available skills

Show:

```text
Installed core skills:
- /second-brain-capture
- /link-finder
- /vault-synthesis
- /next-steps-ai
- /explore-skills

Available skills from catalog:
- /forgotten-notes — resurface old relevant notes
- /decision-tracker — audit past decisions and outcomes
- /daily-note — create or open today's note from a template
- /project-health — flag stalled projects or areas
- /weekly-review — guided weekly review
- /capture-from-url — turn a URL into a vault note
- /meeting-recap — structure raw meeting notes

Which skill do you want to inspect or build?
```

If `[LANG]` is Spanish, present the explanation in Spanish while keeping command names unchanged.

---

## STEP 4 — Show selected skill spec

If the user chooses a skill:

1. Find the full skill spec in `docs/skills-catalog.md`.
2. Show the spec clearly.
3. Explain what the skill will create or modify.
4. Ask:

```text
Build this skill now? [yes / adjust / cancel]
```

Do not build the skill before showing the spec.

---

## STEP 5 — Build selected skill

If the user confirms, create:

```text
.claude/commands/[skill-name].md
```

Use the filesystem Write tool, not the Obsidian MCP.

The command file must include:

- command name,
- purpose,
- required profile read from `.claude/vault-profile.md`,
- expected inputs,
- step-by-step behavior,
- write/confirmation rules,
- safety rules,
- language behavior.

If the command file already exists, ask:

```text
This command already exists. Do you want to overwrite it, keep it, or create a backup first?
```

Recommended backup name:

```text
.claude/commands/[skill-name].backup-[YYYY-MM-DD].md
```

Do not overwrite without confirmation.

---

## STEP 6 — Add a custom skill idea

If the user wants to add a new skill idea:

1. Ask what the skill should do.
2. Ask what inputs it should accept.
3. Ask what it should create, update, or analyze.
4. Draft a catalog spec.
5. Show the spec to the user.
6. Ask whether to add it to `docs/skills-catalog.md`.
7. If confirmed, append it to `docs/skills-catalog.md` using the filesystem Write tool.
8. Ask whether to build it now.

Do not append new catalog entries without confirmation.

---

## STEP 7 — Confirm

After building a skill, say:

```text
Skill installed: /[skill-name]
Path: .claude/commands/[skill-name].md

You can now run /[skill-name] from this vault in Claude Code.
```

If the user only inspected a skill and did not build it, say:

```text
No changes made.
```
