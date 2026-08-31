# Changelog

All notable changes to this curriculum are documented here.

## Unreleased

### Added

- Current AZ-104 blueprint baseline dated April 17, 2026.
- Twenty-eight self-contained learning environments with Azure CLI commands hosted in PowerShell, lifecycle contracts, diagrams, and solution notes.
- Preview-first `Preflight.ps1`, `Setup.ps1`, `Validate.ps1`, and `Cleanup.ps1` interfaces, including cost and tenant-change gates.
- Strict schemas for lab metadata, the lab catalog, run state, deployment validation, cleanup results, assessments, and private learner progress.
- A marked-section, data-driven lab renderer with drift checking.
- Full assessment coverage for all 82 official objectives in the April 17, 2026 AZ-104 blueprint.
- Exactly 50 questions in every assessment-enabled lab, with separate learner and answer files in Labs 01–25.
- A searchable Material for MkDocs site, private browser-local progress, JSON import/export, learning pathways, and generated domain dashboards.
- A cross-platform initializer, blocking readiness report, pinned development container, VS Code tasks, and GitHub Pages workflow.
- Deterministic accessible SVG rendering from each lab's Mermaid architecture source.

### Changed

- Every core checkpoint now includes the direct learner command, expected state, positive and negative checks, retained evidence, retry guidance, and cleanup dependency.
- Architecture Mermaid/SVG files are the only instructional visuals.
- Learner evidence is redacted command output and structured lifecycle results; no browser procedure or screenshot evidence is required.
- Complete lifecycle script implementations are synchronized into every lab README after the guided tasks.
- The assessment expander now renders authored records and refuses incomplete or duplicated banks.
- The master question index is a compact per-lab and objective-coverage dashboard.

### Fixed

- Setup persists every returned managed-object ID immediately so cleanup can recover after a partial failure.
- Cleanup verifies run ownership before mutation, follows declared dependencies, is idempotent, and reports expected retained or soft-deleted objects explicitly.
- Validation reports `pass` only when every required checkpoint passes and uses `partial` when an optional gate is skipped.
- Generated lab READMEs render each checkpoint as a distinct learner-first section.
