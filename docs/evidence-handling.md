# CLI, PowerShell, and portal evidence handling

The canonical evidence for a live-tested lab is the machine-readable result produced by its Azure CLI or PowerShell validation stage. Sanitized Azure Portal screenshots are secondary, supporting evidence: each lab plans 2–5 captures in `images/portal/manifest.yml`, and architecture diagrams remain the repository's visual learning aids.

## Evidence workflow

1. Run preflight and confirm the exact tenant, subscription, location, role boundary, provider state, and cost class.
2. Execute setup only with its explicit execution switch.
3. Run the independent validator and review every `pass`, `fail`, `warning`, and `skipped` check.
4. Keep the complete result under the ignored `.state/<run-id>/` directory.
5. If durable evidence is needed, retain only a minimal redacted excerpt with the date, tool versions, region, result, cleanup result, and residual-state audit.
6. Never edit a failing result into a pass or reuse output from a different tenant or run.

## Portal screenshot workflow

Screenshots are captured only during an authorized live batch, after the lab's validation stage has produced its result.

1. Open the signed-in Azure Portal against the disposable lab environment and navigate to the blade named in the lab's manifest entry.
2. Capture the planned evidence as PNG; record the capture date and region and set the entry to `captured`. Raw captures stay outside the repository.
3. Sanitize: crop to the relevant blade, irreversibly redact account-specific values, strip all image metadata, and optimize the PNG (at most 1920 px wide, roughly 500 KB or less). Record the redactions performed, set `portalConfirmed: true`, move the entry to `sanitized`, and only then copy the file into `images/portal/`.
4. Embed the image beside the matching README checkpoint and update the manifest and `lab.yml` screenshot status.
5. Mark `verified` only after a second manual review confirms no identifying content remains.

Statuses progress `pending` → `captured` → `sanitized` → `verified`. A missing prerequisite produces a documented `pending` entry, never a fabricated or placeholder image. The repository validator enforces that only `sanitized` or `verified` images exist on disk and that every committed PNG has a manifest entry.

## Redaction rules

Remove tenant and subscription IDs, user and object IDs, personal email addresses, tokens, passwords, access keys, connection strings, SAS values, notification destinations, billing information, and unrelated resources. Public IPs, hostnames, and custom domains should also be removed when they identify a real environment. The same rules apply to text visible inside portal screenshots.

Do not commit `.state/`, shell history, transcripts containing secrets, raw or unsanitized screenshots, or complete raw cloud inventories. Redaction does not make a secret safe if the underlying value remains recoverable.
