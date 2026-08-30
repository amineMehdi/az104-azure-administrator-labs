# Project implementation plan

## Locked decisions

- 28 standalone lab folders: 26 instructional labs and 2 capstones.
- One complete best-fit Azure CLI or PowerShell lane per lab; Lab 00 demonstrates both.
- Exactly ten original four-option, single-answer questions per lab, with a separate answer key.
- All 82 official objectives receive instruction, exercise, validation, question, and official-source coverage.
- Offline authoring and validation precede live Azure testing.
- Live work uses an approved disposable sandbox in small batches capped at €10.
- The agent captures and sanitizes real Azure Portal screenshots after successful validation.
- Local Git first; no GitHub remote, Pages, OIDC, or publication until separately approved.

## Milestones

1. Freeze the current official blueprint and establish schemas, tooling, CI, and documentation.
2. Complete `00-safe-bootstrap` as the golden folder contract.
3. Implement identity/governance, storage, compute, networking, and monitoring/recovery in domain waves.
4. Implement both capstones, requiring the learner to switch command surface.
5. Live-test authorized batches, capture Portal evidence, clean up, and audit residual state.
6. Verify all 82 objectives, 28 portable folders, and 280 questions; create a local blueprint-version tag.

## Completion rule

A planned catalog entry is not a completed lab. A lab becomes `offline-validated` only after its content, scripts, metadata, diagram, assessment, and portability checks pass. It becomes `live-verified` only after an authorized Azure run, sanitized Portal evidence, cleanup, and residual-resource audit succeed.

See [AZ-104-GITHUB-LABS-MEGA-PROMPT.md](AZ-104-GITHUB-LABS-MEGA-PROMPT.md) for the original detailed project charter.
