# Command Contracts

This document defines how every Claude Code command in Claude Obsidian Second Brain should behave.

The goal is to make the system predictable, safe, profile-aware, and reusable after the final vault has been installed.

---

## Global command contract

Every command must follow these rules:

1. Read `.claude/vault-profile.md` before making profile-aware decisions.
2. Respect the user's selected language.
3. Use the `obsidian-vault` MCP for Obsidian notes.
4. Use the filesystem Write tool for `.claude/`, command files, docs, and configuration files.
5. Propose before writing new notes unless the command is explicitly a report generator.
6. Never delete notes or configuration without explicit confirmation.
7. Never overwrite user-modified files without explicit confirmation.
8. Use real user-provided names for projects, clients, products, courses, services, or areas.
9. Do not invent missing business or personal context.
10. Do not ask the user to store passwords, seed phrases, private keys, API keys, or sensitive credentials.

---

## Required profile read

Before routing, linking, reporting, or generating next steps, commands must read:

```text
.claude/vault-profile.md
```

Required fields to extract:

```text
profile
language
vault_path
structure
routing_rules
link_rules
```

If `.claude/vault-profile.md` does not exist, the command must stop and say:

```text
I do not see a vault profile yet. Run /vault-install first to set up your second brain.
```

---

## Required language behavior

If the vault language is English:

- respond in English,
- use English headings,
- use English folder labels.

If the vault language is Spanish:

- respond in Spanish,
- use Spanish headings,
- use Spanish folder labels.

If the vault language is Mixed:

- keep folder structure in English,
- write note content in the user's language,
- default to Spanish if the user writes in Spanish.

---

## `/second-brain-capture` contract

Purpose:

Capture a user input and turn it into a structured, linked Obsidian note.

Required flow:

1. Read `.claude/vault-profile.md`.
2. Classify the input.
3. Map generic type to profile-specific routing when needed.
4. Select destination folder using routing rules.
5. Suggest title, type, folder, and links.
6. Ask for confirmation.
7. Create the note using the `obsidian-vault` MCP.
8. Add wikilinks based on link rules.
9. Confirm what was created.

Required proposal format:

```text
Type: [TYPE]
Folder: [DESTINATION_FOLDER]
Title: [TITLE]
Links to: [2-3 proposed links]

OK? [yes / adjust]
```

Required minimum frontmatter:

```yaml
type: [TYPE]
profile: [PROFILE]
created: YYYY-MM-DD
tags: []
```

If project, client, product, course, service, or area is known, include it.

Do not create the note before user confirmation.

---

## `/link-finder` contract

Purpose:

Find orphan notes and suggest connections.

Required flow:

1. Read `.claude/vault-profile.md`.
2. Scan recent or selected notes through the `obsidian-vault` MCP.
3. Identify notes with no obvious incoming or outgoing wikilinks.
4. Score connection candidates.
5. Show suggested links with confidence scores.
6. Ask whether to apply all, review one by one, or skip.
7. Apply links only after user confirmation.
8. Confirm how many links were added.

Required scoring signals:

- keyword overlap,
- same project,
- same client/product/course/area,
- related note type,
- explicit routing/link rules from vault profile.

Never auto-link without confirmation.

---

## `/vault-synthesis` contract

Purpose:

Generate a synthesis report from the vault.

Required flow:

1. Read `.claude/vault-profile.md`.
2. Ask for a period if the user did not specify one.
3. Default to the last 30 days if the user agrees or gives no preference.
4. Collect relevant notes through the `obsidian-vault` MCP.
5. Analyze recurring themes, decisions, insights, stalled projects, gaps, and recommendations.
6. Create a synthesis note in the profile-appropriate reports/monthly/synthesis folder.
7. Confirm the created report path.

Report should include:

```markdown
# Synthesis — [Period]

## Patterns Detected

## Key Insights

## Decisions and Outcomes

## Project / Area Health

## Knowledge Gaps

## Recommendations
```

This command may write the report without a second confirmation if the user explicitly asked to generate the synthesis.

---

## `/next-steps-ai` contract

Purpose:

Suggest 3-5 next actions based on vault state.

Required flow:

1. Read `.claude/vault-profile.md`.
2. Analyze recent notes.
3. Identify blockers, stale projects, unresolved decisions, active goals, and knowledge gaps.
4. Score candidate actions by impact.
5. Show ranked suggestions.
6. Ask the user to pick one or two.
7. If the user picks one, help execute or break it down.

Scoring criteria:

| Signal | Impact |
|---|---|
| Unblocks other work | High |
| Supports an active project or goal | High |
| Resolves a pending decision | Medium-high |
| Connects orphan knowledge | Medium |
| Fills an important knowledge gap | Medium |
| Routine maintenance | Low |

Do not create tasks automatically unless the user asks.

---

## `/explore-skills` contract

Purpose:

Show optional skills and build selected skills into the final vault.

Required flow:

1. Read `.claude/vault-profile.md`.
2. Read `docs/skills-catalog.md` from the final vault.
3. Show installed skills and available skills.
4. If the user chooses a skill, show its spec.
5. Ask whether to build it.
6. If confirmed, write the new command file to `.claude/commands/[skill-name].md` using the filesystem Write tool.
7. Confirm the new command is ready.

If `docs/skills-catalog.md` does not exist, say:

```text
I cannot find docs/skills-catalog.md in this vault. The installer may not have copied the skills catalog. I can help recreate it from the installer repository if available.
```

Never create a new skill without showing the spec first.

---

## `/vault-install` contract

Purpose:

Build the final personalized Obsidian vault after environment and MCP setup.

Required flow:

1. Verify MCP connection.
2. Diagnose user profile.
3. Propose structure.
4. Confirm language.
5. Confirm final build plan.
6. Create required system folders.
7. Create personalized folders.
8. Create `.claude/vault-profile.md`.
9. Create final vault `CLAUDE.md`.
10. Copy core commands.
11. Copy `docs/skills-catalog.md`.
12. Create `Home.md`.
13. Create hub notes.
14. Create `00_START_HERE.md`.
15. Verify final vault output contract.
16. Hand off the user to the final vault path.

The final vault must satisfy `specs/vault-output-contract.md`.

---

## Error handling contract

When a command fails:

1. State what failed.
2. State the most likely reason.
3. State whether user action is needed.
4. Continue from the last safe state if possible.
5. Do not start over unless necessary.

Example:

```text
The MCP connection is not available yet. This usually means Claude Code needs to be restarted or refreshed after adding the MCP server. Please restart Claude Code, reopen this repository, and say "continue setup".
```

---

## File overwrite rules

Before overwriting an existing file, Claude must check whether it appears user-modified.

If the file is a generated installer file and unchanged, it can be replaced during repair.

If the file may contain user modifications, ask:

```text
This file already exists and may contain changes. Do you want me to overwrite it, keep it, or create a backup copy first?
```

Recommended backup naming:

```text
filename.backup-YYYY-MM-DD.md
```

---

## Safety rules

Commands must not:

- ask for passwords,
- ask for private keys,
- ask for seed phrases,
- store credentials,
- delete user notes without explicit confirmation,
- move user notes without explicit confirmation,
- upload the vault anywhere unless the user explicitly asks and understands the implications.
