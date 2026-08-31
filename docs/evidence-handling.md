# Azure CLI evidence handling

The canonical evidence for a live-tested lab is the machine-readable result produced by its Azure CLI validation stage hosted in PowerShell. Architecture diagrams explain relationships; they are not proof of a live deployment.

## Evidence workflow

1. Run preflight and confirm the exact tenant, subscription, location, role boundary, provider state, and cost class.
2. Execute setup only with its explicit execution switch.
3. Run the independent validator and review every `pass`, `fail`, and `skipped` check; review preflight warnings separately.
4. Keep the complete result under the ignored `.state/<run-id>/` directory.
5. If durable evidence is needed, retain only a minimal redacted excerpt with the date, tool versions, region, result, cleanup result, and residual-state audit.
6. Never edit a failing result into a pass or reuse output from a different tenant or run.

## Redaction rules

Remove tenant and subscription IDs, user and object IDs, personal email addresses, tokens, passwords, access keys, connection strings, SAS values, notification destinations, billing information, and unrelated resources. Public IPs, hostnames, and custom domains should also be removed when they identify a real environment.

Do not commit `.state/`, shell history, transcripts containing secrets, or complete raw cloud inventories. Redaction does not make a secret safe if the underlying value remains recoverable.
