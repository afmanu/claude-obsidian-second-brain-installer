Show the skills catalog and offer to build any skill the user chooses.

---

## Steps

**1.** Read `docs/skills-catalog.md` from the vault via the `obsidian-vault` MCP.

**2.** Show a summary of what's available:

```
🧩 SKILLS CATALOG

Already installed:
  ✓ /second-brain-capture
  ✓ /link-finder
  ✓ /vault-synthesis
  ✓ /next-steps-ai
  ✓ /explore-skills

Available to build:
  · /forgotten-notes     — resurface old relevant notes
  · /decision-tracker    — audit past decisions + success rate
  · /daily-note          — create today's note from a template
  · /project-health      — flag stalled projects
  · /weekly-review       — guided weekly review
  · /capture-from-url    — turn any URL into a vault note
  · /meeting-recap       — structure raw meeting notes

Which one do you want to build? (or "show me [skill]" for details)
```

**3.** If user picks a skill:
- Read its full spec from `docs/skills-catalog.md`
- Show the spec clearly
- Ask: "Build it now? [yes / show me first]"

**4.** If user says yes:
- Write the skill file to `.claude/commands/[skill-name].md` in the vault directory (use the Write tool directly, not the MCP — this is a filesystem file, not an Obsidian note)
- Content: the spec from the catalog, formatted as a proper skill instruction
- Confirm: "✓ /[skill-name] is ready. Try it now."

**5.** If user wants to add a new skill idea:
- Ask them to describe what it should do
- Write a spec in the catalog format
- Append it to `docs/skills-catalog.md` via MCP
- Confirm: "✓ Added to your catalog. Say 'build it' when you're ready."
