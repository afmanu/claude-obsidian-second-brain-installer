# /link-finder

Find orphan or weakly connected notes and suggest profile-aware wikilinks.

This command must follow the global command contract:

- read `.claude/vault-profile.md` first,
- respect the user's selected language,
- use the `obsidian-vault` MCP for Obsidian notes,
- never modify notes without confirmation,
- never delete notes.

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

## STEP 2 — Define scan scope

If the user specified a scope, use it.

Supported scopes:

- a folder,
- a project,
- a client,
- a product,
- a course,
- an area,
- a date range,
- recent notes.

If no scope is specified, default to the last 20 modified notes.

Use the `obsidian-vault` MCP to list and read notes in scope.

Do not scan unrelated system folders such as `.claude/` or `docs/` unless the user explicitly asks.

---

## STEP 3 — Find weakly connected notes

For each note in scope, identify:

- outgoing wikilinks,
- likely incoming wikilinks if available,
- frontmatter fields,
- note type,
- project/client/product/course/area,
- tags,
- keywords.

Classify notes as:

- `orphan`: no obvious incoming or outgoing wikilinks,
- `weak`: only one weak or generic link,
- `healthy`: at least two useful contextual links.

Only propose links for orphan or weak notes.

---

## STEP 4 — Score candidate connections

Score each candidate connection from 0 to 100.

Use these signals:

| Signal | Score |
|---|---:|
| Keyword overlap | up to 40 |
| Same project/client/product/course/area | up to 20 |
| Same or related note type | up to 10 |
| Matches `[LINK_RULES]` | up to 20 |
| Same tags | up to 10 |

Only show suggestions with confidence of 60 or above unless the user asks to see weaker suggestions.

---

## STEP 5 — Show suggestions

Show a concise list:

```text
Found [N] orphan or weakly connected notes.

Top link suggestions:

[orphan-note-1.md]
- 92% -> [[related-note-a]] — same project and overlapping topic
- 84% -> [[related-note-b]] — matches link rules

[weak-note-2.md]
- 78% -> [[related-note-c]] — same area and tags

Choose:
A) Apply all suggestions above 80%
B) Review one by one
C) Skip
```

Do not apply links automatically.

---

## STEP 6 — Apply links after confirmation

If the user chooses `A`:

- apply only suggestions with confidence 80 or above,
- patch the orphan or weak note to include wikilinks in a `Related` section,
- when appropriate, patch the linked note with a backlink.

If the user chooses `B`:

- walk through suggestions one by one,
- ask for confirmation on each link.

If the user chooses `C`:

- make no changes.

Use the `obsidian-vault` MCP `patch_note` operation for note edits.

Do not create empty placeholder notes.

---

## STEP 7 — Confirm result

After applying confirmed links, say:

```text
Linking complete.
Notes updated: [N]
Links added: [N]
Remaining orphan or weak notes: [N]
Skipped suggestions below confidence threshold: [N]
```

If no useful links were found, say:

```text
No high-confidence link suggestions found. The notes may need more context or tags before they can be linked reliably.
```
