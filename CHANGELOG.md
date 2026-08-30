# Changelog

All notable changes to this curriculum are documented here.

## Unreleased

### Added

- Local Git repository foundation.
- Current AZ-104 blueprint baseline dated April 17, 2026.
- Planned 28-lab curriculum and 280-question assessment contract.
- Offline-validated golden Lab 00 for safe tooling and Azure context, with CLI and PowerShell lanes, contract tests, assessment, and diagram.
- Offline-validated Lab 01 for Microsoft Entra users and groups, with an Azure CLI/Graph lane, partial-run recovery, ten-question assessment, and diagram.
- Labs 02–27 as separate, self-contained Azure CLI or PowerShell lab folders with lifecycle scripts, validation contracts, diagrams, solution notes, and ten questions with answers per lab.
- Full assessment coverage for all 82 official objectives in the April 17, 2026 AZ-104 blueprint.
- A command-evidence policy based on redacted Azure CLI and PowerShell validation output.
- A portal screenshot contract: per-lab `images/portal/manifest.yml` manifests (2–5 planned captures mapped to checkpoints), a screenshot-manifest schema, `screenshots` status metadata in every lab, validator enforcement, and a sanitization workflow in the evidence-handling guide.

### Changed

- Reinstated Azure Portal screenshots as manifest-tracked supporting evidence captured during authorized live batches; the earlier removal of the portal capture requirement is reversed. Architecture Mermaid/SVG files remain the visual learning aids, and command output remains the canonical evidence.

### Fixed

- Generated lab READMEs now render each checkpoint as a separate section; previously the checkpoint headings and evidence lists were collapsed onto a single line.
