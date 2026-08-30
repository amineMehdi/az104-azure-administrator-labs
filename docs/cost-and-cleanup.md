# Cost and cleanup safety

Azure budgets and cost alerts notify you; they do not stop consumption. Treat cleanup as part of the lab, not an optional final note.

## Cost classes

- `none`: no Azure resource is created.
- `low`: short-lived, inexpensive resources under normal lab usage.
- `moderate`: compute, networking, monitoring ingestion, or backup can become material if left running.
- `elevated`: Bastion, mobility, custom-domain prerequisites, Backup, or Site Recovery; separate approval is required.

Do not publish fixed prices. Each lab lists billable resources and links to current official pricing.

## Resource identity

Tag taggable resources with:

- `purpose=az104-lab`
- `labId`
- `runId`
- `expiresOn`

Tags are plain text. Never put secrets or personal information in them.

## Cleanup contract

Cleanup must:

1. Read exact IDs from `.state/<run-id>/`.
2. Print the planned deletion.
3. Remove only the recorded run and matching tags.
4. Restore shared settings from the pre-change snapshot.
5. Wait for asynchronous deletion when necessary.
6. Report anything that remains.

A repository-wide janitor is report-only unless a separate destructive mode is explicitly approved.
