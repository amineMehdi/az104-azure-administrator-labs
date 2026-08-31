# Project implementation plan

## Locked decisions

- Keep 28 standalone lab folders: 26 instructional labs and 2 capstones.
- Embed every lifecycle command implementation in its lab README and retain the synchronized scripts for automation and testing.
- Use accessible Mermaid/SVG architecture diagrams as the only instructional visuals.
- Maintain exactly 1,250 original four-option, single-answer questions: 50 in every assessment-enabled lab.
- Store assessments in Labs 01–25; Lab 00 and Capstones 26–27 remain hands-on only.
- Ensure all 82 official objectives receive instruction, exercise, validation, question, and official-source coverage.
- Complete offline authoring and validation before any authorized live Azure work.
- Pilot live work only in an approved disposable environment, after explicit cost and tenant-change authorization.
- Build the documentation site on pull requests. Publish from `main` only after the repository owner enables GitHub Pages for Actions.

## Milestones

1. Maintain schemas, generators, CI, and documentation as the source of truth for the repository contract.
2. Keep lifecycle commands synchronized between every README and its retained scripts.
3. Maintain 50 questions in each assessment-enabled lab, with domain-consistent objective mappings.
4. Validate all 82 objective mappings, 28 portable folders, 1,250 questions, diagrams, scripts, and cleanup contracts offline.
5. Live-test only authorized batches, retain redacted command evidence, clean up, and audit residual state.

The first authorized pilot is limited to Labs 00, 01, 06, 14, 17, and 22 in a disposable environment. Expansion occurs only after the complete inline, break/fix, validation, cleanup, and residual workflow exposes no systemic contract problem.

## Completion rule

A repository release passes offline acceptance only after its content, inline commands, scripts, metadata, diagrams, applicable assessments, site, and portability checks all pass. No lab is labeled `live-verified` until a separately authorized Azure run completes its learner lane, break/fix exercise, redacted Azure CLI evidence, deterministic cleanup, and residual-resource audit.

See [AZ-104-GITHUB-LABS-MEGA-PROMPT.md](AZ-104-GITHUB-LABS-MEGA-PROMPT.md) for the detailed project charter.
