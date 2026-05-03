# System Contracts

This document is copied into the final Obsidian vault during installation.

It gives Claude a compact reference for how the vault should behave after handoff.

The full source contracts live in the installer repository under `specs/`:

- `specs/vault-output-contract.md`
- `specs/frontmatter-schema.md`
- `specs/command-contracts.md`
- `specs/setup-state-machine.md`

---

## 1. Final vault contract

The final vault should contain:

```text
[VAULT_PATH]/
  CLAUDE.md
  Home.md
  00_START_HERE.md
  docs/
    skills-catalog.md
    system-contracts.md
  .claude/
    vault-profile.md
    commands/
      second-brain-capture.md
      link-finder.md
      vault-synthesis.md
      next-steps-ai.md
      explore-skills.md
  [personalized folders based on selected profile]
```

If any required file is missing, Claude should repair the generated files before handoff or clearly tell the user what is missing.

---

## 2. Vault profile contract

Claude must read this file before making profile-aware decisions:

```text
.claude/vault-profile.md
```

It should contain:

- selected profile,
- selected language,
- vault path,
- folder structure,
- routing rules,
- link rules.

If this file is missing, Claude should tell the user to run `/vault-install`.

---

## 3. Command behavior contract

Every installed command should:

1. Read `.claude/vault-profile.md` first.
2. Respect the selected language.
3. Use the `obsidian-vault` MCP for Obsidian notes.
4. Use filesystem tools for `.claude/`, command files, docs, and configuration.
5. Propose before writing new notes unless the user explicitly requested a report.
6. Never delete or overwrite user content without explicit confirmation.
7. Use real user-provided project, client, product, course, service, or area names.
8. Avoid inventing missing personal or business context.
9. Never ask the user to store passwords, seed phrases, private keys, API keys, or sensitive credentials in the vault.

---

## 4. Note frontmatter contract

Generated notes should use frontmatter.

Minimum fields:

```yaml
type: [note type]
profile: [selected profile]
created: YYYY-MM-DD
tags: []
```

Optional fields when known:

```yaml
updated: YYYY-MM-DD
status: pending | active | blocked | completed | archived
priority: low | medium | high
confidence: low | medium | high
project: [project name]
client: [client name]
product: [product name]
course: [course name]
area: [area name]
service: [service name]
source: [source]
outcome: pending | good | bad | mixed
review_date: YYYY-MM-DD
```

Do not invent metadata. Leave uncertain fields out or ask the user.

---

## 5. Core note types

Common note types:

```text
insight
solution
decision
meeting
idea
reference
task
goal
reflection
concept
project
process
learning
bug-fix
pattern
architecture
literature-note
permanent-note
argument
question
contradiction
product-idea
customer-feedback
campaign
content-idea
metric
daily-journal
weekly-review
habit
lesson
book-note
quote
synthesis
```

Commands may map generic types to profile-specific types based on the selected profile.

---

## 6. Language contract

If language is English:

- folder names should be English,
- note headings should be English,
- generated content should be English unless the user writes in another language.

If language is Spanish:

- folder names should be Spanish,
- note headings should be Spanish,
- generated content should be Spanish.

If language is Mixed:

- folder names should remain English,
- note content should follow the user's language,
- default to Spanish when the user writes in Spanish.

---

## 7. Installed core commands

The final vault should include:

```text
/second-brain-capture
/link-finder
/vault-synthesis
/next-steps-ai
/explore-skills
```

Command files live in:

```text
.claude/commands/
```

---

## 8. Recovery contract

If something fails, Claude should not restart the whole setup automatically.

Claude should:

1. Identify the current setup state.
2. Identify the failed component.
3. Repair the earliest failing dependency.
4. Continue from the last valid state.
5. Avoid overwriting user-modified files without confirmation.

If the original installer repository is available, Claude can consult:

```text
TROUBLESHOOTING.md
docs/mcp-setup.md
docs/recovery-prompts.md
specs/setup-state-machine.md
```

---

## 9. Safety contract

Claude must not:

- ask for passwords,
- ask for private keys,
- ask for seed phrases,
- store credentials,
- delete user notes without explicit confirmation,
- move user notes without explicit confirmation,
- upload the vault anywhere unless the user explicitly asks and understands the implications.
