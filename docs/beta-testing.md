# Beta Testing

Use this checklist to test a clean installation before describing a mode as verified.

## External blind validation

| Date | Prompt | Outcome | Runtime details |
|---|---|---|---|
| 2026-11-05 | Repository link only | Installation reported complete with no issues | Not recorded |

This confirms that an external user can trigger and complete the installation from the repository link alone. It does not verify a specific environment row below because the operating system, Claude runtime and installation mode were not recorded.

## Test environments

Record at least one real run for each supported path:

| Environment | New vault | Existing vault | Interrupted recovery | Result |
|---|---:|---:|---:|---|
| Windows + Claude Code | Pending | Pending | Pending | Pending |
| macOS + Claude Code | Pending | Pending | Pending | Pending |
| Claude Co-Work Desktop | Pending | Pending | Pending | Pending |
| Mobile to desktop handoff | Pending | Not applicable | Pending | Pending |
| Windows + WSL | Pending | Pending | Pending | Pending |

Do not replace Pending with Pass without completing the scenario.

## Required checks

For every run, confirm:

1. The environment was detected correctly.
2. No files were created outside the approved repository and vault paths.
3. Existing user files were preserved.
4. The user saw the proposed profile, language, and structure before creation.
5. MCP access was verified before running the vault wizard.
6. The final vault satisfied specs/vault-output-contract.md.
7. The vault reopened successfully as an independent workspace.
8. At least one capture and one recovery flow were tested.

## Evidence to retain

Keep evidence free of personal vault content:

- operating system and execution mode;
- fresh or existing vault;
- installation stage reached;
- pass, fail, or partial result;
- sanitized error text;
- recovery action;
- final verification result.

Never retain credentials, private notes, complete local paths, or MCP secrets.

## Release claim rule

Describe a mode as supported when its instructions exist. Describe it as verified only after a clean test has passed and the result has been recorded.
