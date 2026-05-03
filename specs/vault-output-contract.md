# Vault Output Contract

This document defines the required final state of a vault created by Claude Obsidian Second Brain.

Claude must use this contract to verify the installation before handing the vault off to the user.

---

## Purpose

The installer repository is only the bootstrap system.

The final Obsidian vault is the user's working environment. It must contain all files, folders, commands, documentation, and configuration needed to keep working without opening the installer repository again.

---

## Required final vault structure

At the end of setup, the final vault must contain:

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

The exact personalized folders depend on the selected profile and language mapping.

---

## Required root files

### `CLAUDE.md`

Required.

Purpose:

- tells Claude how to operate inside the final vault,
- instructs Claude to read `.claude/vault-profile.md`,
- defines safety and writing rules,
- lists installed commands.

Validation:

- file exists at `[VAULT_PATH]/CLAUDE.md`,
- mentions `.claude/vault-profile.md`,
- lists the five core vault skills.

---

### `Home.md`

Required.

Purpose:

- main Obsidian hub note,
- links to top-level folders,
- links to active projects, clients, courses, products, or areas when available.

Validation:

- file exists at `[VAULT_PATH]/Home.md`,
- has frontmatter with `type: hub`,
- includes quick access links.

---

### `00_START_HERE.md`

Required.

Purpose:

- explains how to use the vault,
- explains the selected profile,
- explains the folder structure,
- explains the five core vault skills,
- tells the user how to capture the first note.

Validation:

- file exists at `[VAULT_PATH]/00_START_HERE.md`,
- includes the selected profile,
- includes the selected language or note language behavior,
- includes usage instructions for `/second-brain-capture`.

---

## Required `.claude/` files

### `.claude/vault-profile.md`

Required.

Purpose:

- source of truth for profile-aware behavior,
- stores selected profile,
- stores language,
- stores vault path,
- stores final folder structure,
- stores routing rules,
- stores link rules.

Validation:

- file exists at `[VAULT_PATH]/.claude/vault-profile.md`,
- contains frontmatter,
- contains `profile`, `language`, `vault_path`, and `created`,
- contains sections for `Structure`, `Routing Rules`, and `Link Rules`.

---

### `.claude/commands/`

Required.

Purpose:

- stores the Claude Code slash commands that operate inside the final vault.

Required command files:

```text
[VAULT_PATH]/.claude/commands/second-brain-capture.md
[VAULT_PATH]/.claude/commands/link-finder.md
[VAULT_PATH]/.claude/commands/vault-synthesis.md
[VAULT_PATH]/.claude/commands/next-steps-ai.md
[VAULT_PATH]/.claude/commands/explore-skills.md
```

Validation:

- all five command files exist,
- each command file is non-empty,
- each command file is copied from the installer repository unless the user explicitly requested modification.

---

## Required `docs/` files

### `docs/skills-catalog.md`

Required.

Purpose:

- source catalog used by `/explore-skills`,
- contains optional skills that can be built after setup.

Validation:

- file exists at `[VAULT_PATH]/docs/skills-catalog.md`,
- includes available buildable skills,
- includes `/forgotten-notes`, `/decision-tracker`, `/daily-note`, `/project-health`, `/weekly-review`, `/capture-from-url`, and `/meeting-recap` unless the catalog has been intentionally updated.

---

### `docs/system-contracts.md`

Required.

Purpose:

- compact reference for how the final vault should behave after handoff,
- summarizes final vault contract, command behavior, frontmatter rules, language behavior, recovery behavior, and safety rules,
- allows Claude to operate inside the final vault without needing to reopen the installer repository.

Validation:

- file exists at `[VAULT_PATH]/docs/system-contracts.md`,
- includes final vault contract summary,
- includes command behavior rules,
- includes frontmatter minimum fields,
- includes safety rules.

---

## Required personalized folders

The installer must create all folders from the selected profile's final structure.

Each created folder must contain a `.gitkeep` file if needed to force folder creation.

Validation:

- every folder in `[STRUCTURE]` exists,
- user-specific folders use the user's real names where available,
- language mapping has been applied correctly.

---

## Verification process

Before handoff, Claude must verify:

1. Root files exist.
2. `.claude/vault-profile.md` exists and is complete.
3. All five core command files exist.
4. `docs/skills-catalog.md` exists.
5. `docs/system-contracts.md` exists.
6. All selected profile folders exist.
7. `Home.md` and `00_START_HERE.md` were created through the vault note system.
8. The final vault can be opened directly with `claude "[VAULT_PATH]"`.

---

## Repair rules

If a required file or folder is missing:

1. Recreate it if enough information is available.
2. Do not delete existing user files.
3. Do not overwrite user-modified files without explicit confirmation.
4. If repair is not possible, tell the user exactly what is missing and how to fix it.

---

## Handoff condition

The user should only be handed off after the contract is satisfied or after Claude clearly reports any unresolved missing items.

The final handoff must include:

```text
Vault path: [VAULT_PATH]
Open this vault with:
claude "[VAULT_PATH]"
```
