# AZ-104 complete learning environment charter

> Blueprint baseline: skills measured as of April 17, 2026
> Authoring mode: offline first
> Learner command surface: Azure CLI hosted in PowerShell

This is the durable implementation charter for the repository. The authoritative
objective inventory is in
[`docs/research/az-104-blueprint.md`](docs/research/az-104-blueprint.md), and the
machine-readable lab source is
[`curriculum/lab-content.yml`](curriculum/lab-content.yml).

## Outcome

Build a beginner-to-job-ready Azure Administrator environment with:

- exactly 28 numbered, portable lab folders;
- complete guided Azure CLI commands in every lab README;
- synchronized, preview-first lifecycle scripts for automation and testing;
- architecture Mermaid sources and accessible SVGs as the only instructional
  visuals;
- exactly 50 fully authored questions in each of Labs 01–25;
- hands-on-only Lab 00 and Capstones 26–27;
- traceability across all 82 objectives in the April 17, 2026 blueprint;
- a searchable static documentation site and private browser-local progress;
- deterministic offline validation before any authorized Azure pilot.

PowerShell is the command host and scripting language. Learner Azure operations
use `az`, `az rest`, Bicep through `az bicep`, AzCopy, or KQL where appropriate.
There are no Bash lanes, Azure PowerShell cmdlets, browser UI procedures, or
image-based evidence requirements.

## Lab contract

Every README follows this learner-first order:

1. Previous, catalog, and next navigation.
2. Scenario, role, outcome, time, difficulty, cost, and completion criteria.
3. Objective-to-checkpoint mapping.
4. Service topology and architecture walkthrough.
5. Concept primer and design decisions.
6. Required and optional inputs with safe examples and gate behavior.
7. Read-only preflight with representative redacted output.
8. Guided checkpoints with direct commands, expected state, positive and
   negative checks, evidence, retry guidance, and cleanup dependencies.
9. Service-specific final validation and result interpretation.
10. Deterministic break/fix injection, diagnosis, repair, and before/after proof.
11. Optional job-style challenge.
12. Troubleshooting guidance.
13. Dependency-aware cleanup and residual queries.
14. Exam debrief, assessment link, named Microsoft sources, and navigation.
15. Full synchronized lifecycle scripts in an appendix.

No required checkpoint may exist only in a script. The optional automated lane
must use a different run ID if a learner already completed the guided lane.

## Lifecycle contract

- `Preflight.ps1` is read-only and checks context, tools, providers, region,
  quota, SKU availability, inputs, and authorization gates.
- `Setup.ps1` previews by default. `-Execute` is required for mutation.
- Moderate or elevated cost requires `-AcknowledgeCost`; tenant-wide change
  requires `-AcknowledgeTenantChange`.
- Every returned managed-object ID is written to ignored local run state
  immediately after creation. Original shared settings are captured before a
  change.
- `Validate.ps1 -Mode Deployment` proves the service state independently.
- Required checkpoint failure prevents an overall pass. An intentionally
  skipped optional gate makes the overall result partial.
- `Cleanup.ps1` previews by default, checks recorded ownership before each
  mutation, never performs an irreversible purge automatically, and follows
  declared dependencies.
- `Validate.ps1 -Mode PostCleanup` passes only when no active managed resource
  remains. Expected retained or soft-deleted objects are explicit in
  `cleanup.json`.

State may contain identifiers and original settings needed for recovery, but it
must never contain credentials, tokens, passwords, keys, connection strings, or
SAS values.

## Assessment contract

Labs 01–25 each contain `Q01` through `Q50` with a 15 foundational, 25 applied,
and 10 advanced mix. Every record has:

- one checkpoint and remediation anchor;
- four distinct options and exactly one answer;
- an explanation for every option;
- domain-consistent objective mappings;
- descriptive Microsoft Learn source titles and URLs;
- an individual verification date.

The checker rejects incomplete banks, exact and near duplicates, repeated option
sets, generic rationales, predictable answer-key periods, invalid anchors, and
procedural sources that do not support the command-first workflow. Learner files
do not expose answers. Answer files repeat the stem and options, label each
option, link to the mapped task, and show named sources.

Assessment scores are learning signals: 85–100% is mastery, 70–84% calls for
targeted review, and below 70% means repeating the mapped tasks.

## Offline release gate

Release validation requires all 28 labs and checks schemas, objective coverage,
checkpoint depth, inline/script synchronization, PowerShell syntax and analysis,
mocked lifecycle safety tests, Bicep lint/build, Markdown, spelling, links,
secrets, generator drift, assessment originality, diagram synchronization, a
strict site build, and representative desktop/mobile accessibility signals.

The repository must not claim live verification during this rebuild. Live work
is a later, separately authorized pilot for Labs 00, 01, 06, 14, 17, and 22 in a
disposable environment. Each pilot includes the inline path, break/fix,
validation, cleanup, and residual audit with redacted command evidence.

## Authority boundary

Local authoring and non-mutating offline checks are authorized. Azure sign-in,
provider registration, resource deployment, elevated cost, tenant-wide changes,
publishing settings, and live evidence collection require separate approval.

The implementation plan and acceptance state are maintained in
[`PROJECT-PLAN.md`](PROJECT-PLAN.md) and
[`docs/implementation-status.md`](docs/implementation-status.md).
