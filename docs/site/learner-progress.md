# Learner progress

Use the controls below to review lab completion, export a backup, or import an
existing progress file. The controls appear when JavaScript is enabled.

<noscript>
This dashboard needs JavaScript for browser-local progress. The lab content and
assessments remain readable without it; use the command-line tracker below if
you prefer not to enable JavaScript.
</noscript>

Progress is private and local:

- the browser stores data under `az104LearnerProgress.v1` in `localStorage`;
- no data is sent to Azure, GitHub, analytics, or any other service;
- exports contain lab status, validation and cleanup outcomes, optional scores,
  and update times only;
- tenant IDs, subscription IDs, usernames, and resource IDs are rejected.

Browser progress is scoped to this site, browser profile, and storage partition.
Private-browsing cleanup or clearing site data may remove it, so export a JSON
backup if you want portability. The browser and `.state/progress.json` do not
silently synchronize; transfer a validated export explicitly.

Imports and exports must satisfy the closed
[learner progress schema](../../curriculum/progress-schema.json).

## Command-line progress

The same record shape is supported in `.state/progress.json`:

```powershell
pwsh -File tools/Update-LearnerProgress.ps1 `
  -LabId LAB-06 `
  -Status complete `
  -ValidationPassed true `
  -CleanupPassed true `
  -AssessmentScore 88
```

Display, import, or export the local record:

```powershell
pwsh -File tools/Update-LearnerProgress.ps1 -Show
pwsh -File tools/Update-LearnerProgress.ps1 -ImportPath progress-backup.json
pwsh -File tools/Update-LearnerProgress.ps1 -ExportPath progress-backup.json
```

Importing replaces the current local record only after the complete JSON file
passes structural and privacy checks. Browser imports are limited to 256 KiB,
well above the expected closed 28-lab record size.

## Completion rules

A lab is complete only when both deployment validation and cleanup validation
are recorded as passed. Lab 00 and Capstones 26–27 are hands-on only and do not
store a score; Labs 01–25 use the score to show mastery guidance.
