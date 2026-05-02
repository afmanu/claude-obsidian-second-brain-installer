# Setup State Machine

This document defines the installation states for Claude Obsidian Second Brain.

Claude must use this file when setup is interrupted, the user says `continue setup`, or the current installation state is unclear.

---

## Core rule

Continue from the latest valid state.

Do not start over unless:

- the user explicitly requests a clean reinstall,
- the vault path is wrong and unrecoverable,
- required setup information is missing,
- continuing would overwrite user data without consent.

---

## State overview

```text
STATE 0: Repository opened
STATE 1: User confirmed setup
STATE 2: Obsidian checked
STATE 3: Vault path selected
STATE 4: Vault folder created
STATE 5: Node.js checked
STATE 6: npx checked
STATE 7: MCP command configured
STATE 8: Claude Code restarted or refreshed
STATE 9: MCP verified
STATE 10: /vault-install started
STATE 11: Profile selected
STATE 12: Structure confirmed
STATE 13: Language confirmed
STATE 14: Final build confirmed
STATE 15: System folders created
STATE 16: Personalized folders created
STATE 17: Vault profile created
STATE 18: Final vault CLAUDE.md created
STATE 19: Core commands copied
STATE 20: Skills catalog copied
STATE 21: Home note created
STATE 22: Hub notes created
STATE 23: Onboarding note created
STATE 24: Final vault verified
STATE 25: Handoff complete
```

---

## State details

### STATE 0: Repository opened

Evidence:

- `README.md` exists.
- `CLAUDE.md` exists.
- `.claude/commands/vault-install.md` exists.

Next:

- Start setup wizard.

---

### STATE 1: User confirmed setup

Evidence:

- User answered yes to setup.

Next:

- Check Obsidian.

---

### STATE 2: Obsidian checked

Evidence:

- Obsidian is found, or user explicitly chooses to continue before opening Obsidian.

Checks:

```bash
ls /Applications/Obsidian.app 2>/dev/null && echo "found" || echo "not found"
which obsidian 2>/dev/null && echo "found" || echo "not found"
```

Next:

- Select vault path.

---

### STATE 3: Vault path selected

Evidence:

- `[VAULT_PATH]` is known.
- Path is absolute.
- User approved the path.

Next:

- Create vault folder.

---

### STATE 4: Vault folder created

Evidence:

```bash
ls "[VAULT_PATH]"
```

or on Windows PowerShell:

```powershell
Test-Path "[VAULT_PATH]"
```

Next:

- Check Node.js.

---

### STATE 5: Node.js checked

Evidence:

```bash
node --version
```

Next:

- Check `npx`.

---

### STATE 6: npx checked

Evidence:

```bash
npx --version
```

Next:

- Configure MCP.

---

### STATE 7: MCP command configured

Evidence:

```bash
claude mcp list
```

shows `obsidian-vault`, or the MCP add command completed without error:

```bash
claude mcp add obsidian-vault -- npx -y @bitbonsai/mcpvault@latest "[VAULT_PATH]"
```

Next:

- Restart or refresh Claude Code.

---

### STATE 8: Claude Code restarted or refreshed

Evidence:

- User returned and said `continue setup`.
- Claude Code session has reloaded.

Next:

- Verify MCP.

---

### STATE 9: MCP verified

Evidence:

- `obsidian-vault` MCP can list the vault root.

Next:

- Run `/vault-install`.

If verification fails:

- Read `docs/mcp-setup.md`.
- Repair MCP.

---

### STATE 10: /vault-install started

Evidence:

- Preconditions checked.
- Specs read:
  - `specs/vault-output-contract.md`
  - `specs/frontmatter-schema.md`
  - `specs/command-contracts.md`

Next:

- Diagnose profile.

---

### STATE 11: Profile selected

Evidence:

- `[PROFILE]` is known.
- `[PROFILE_REASON]` is known.
- `[PROFILE_CONFIDENCE]` is known.

Next:

- Confirm structure.

---

### STATE 12: Structure confirmed

Evidence:

- `[STRUCTURE]` is known.
- User approved or adjusted the proposed structure.

Next:

- Confirm language.

---

### STATE 13: Language confirmed

Evidence:

- `[LANG]` is known.
- Value is English, Spanish, or Mixed.

Next:

- Confirm final build plan.

---

### STATE 14: Final build confirmed

Evidence:

- User confirmed the build.

Next:

- Create system folders.

---

### STATE 15: System folders created

Evidence:

```text
[VAULT_PATH]/.claude/
[VAULT_PATH]/.claude/commands/
[VAULT_PATH]/docs/
```

exist.

Next:

- Create personalized folders.

---

### STATE 16: Personalized folders created

Evidence:

- All folders from `[STRUCTURE]` exist.

Next:

- Create `.claude/vault-profile.md`.

---

### STATE 17: Vault profile created

Evidence:

```text
[VAULT_PATH]/.claude/vault-profile.md
```

exists and contains:

```text
profile
language
vault_path
Structure
Routing Rules
Link Rules
```

Next:

- Create final vault `CLAUDE.md`.

---

### STATE 18: Final vault CLAUDE.md created

Evidence:

```text
[VAULT_PATH]/CLAUDE.md
```

exists and mentions:

```text
.claude/vault-profile.md
```

Next:

- Copy core commands.

---

### STATE 19: Core commands copied

Evidence:

All files exist:

```text
[VAULT_PATH]/.claude/commands/second-brain-capture.md
[VAULT_PATH]/.claude/commands/link-finder.md
[VAULT_PATH]/.claude/commands/vault-synthesis.md
[VAULT_PATH]/.claude/commands/next-steps-ai.md
[VAULT_PATH]/.claude/commands/explore-skills.md
```

Next:

- Copy skills catalog.

---

### STATE 20: Skills catalog copied

Evidence:

```text
[VAULT_PATH]/docs/skills-catalog.md
```

exists.

Next:

- Create Home note.

---

### STATE 21: Home note created

Evidence:

```text
[VAULT_PATH]/Home.md
```

exists and has `type: hub` frontmatter.

Next:

- Create hub notes.

---

### STATE 22: Hub notes created

Evidence:

- Hub notes from the selected profile exist.
- User-specific hub notes exist where applicable.

Next:

- Create onboarding note.

---

### STATE 23: Onboarding note created

Evidence:

```text
[VAULT_PATH]/00_START_HERE.md
```

exists.

Next:

- Verify final vault.

---

### STATE 24: Final vault verified

Evidence:

- `specs/vault-output-contract.md` is satisfied.

Next:

- Handoff.

---

### STATE 25: Handoff complete

Evidence:

- User has been told:

```bash
claude "[VAULT_PATH]"
```

- User has been told not to keep working from installer repository unless updating or reinstalling.

---

## Resume algorithm

When the user says `continue setup`:

1. Read this state machine.
2. Identify `[VAULT_PATH]` if possible.
3. Check evidence from the latest states backward.
4. Select the highest state with valid evidence.
5. Continue from the next state.
6. If evidence is ambiguous, ask one focused question.

Example:

```text
I found the vault folder and the MCP is configured, but I cannot verify the MCP yet. Please restart or refresh Claude Code, then say "continue setup" again.
```

---

## Repair behavior

If a state partially completed:

- repair missing generated files,
- do not delete existing files,
- do not overwrite user-modified files without confirmation,
- continue from the repaired state.

If the user wants a clean reinstall:

- recommend creating a new empty vault folder,
- do not delete the old vault unless explicitly asked.
