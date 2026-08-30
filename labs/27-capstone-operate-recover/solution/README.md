# Lab 27 solution and diagnostic notes

Use this only after completing the lab and knowledge check. The solution is evidence-led: it does not replace the independent validator or silently repair live state.

## Intended checkpoint sequence

1. **Checkpoint 1:** Inventory the workload, interpret direct/inherited access, policy compliance, tags, locks, and current health before changing anything.
2. **Checkpoint 2:** Inject one bounded NSG or load-balancer fault, use effective rules and Network Watcher evidence to diagnose it, then repair only the identified cause.
3. **Checkpoint 3:** Query metrics/logs, process an alert, and record the operational timeline and validation output.
4. **Checkpoint 4:** Protect the test workload, run a restore or isolated recovery drill, verify recovered state, and remove protection/resources in dependency order.

## Diagnostic order

1. Confirm that the active tenant and subscription match `.state/<run-id>/run.json`.
2. Confirm the exact resource group or tenant object ID; do not select by a name prefix.
3. Inspect provider registration, service quota, region support, and asynchronous provisioning state.
4. Compare the live configuration with the checkpoint statement in [the lab guide](../README.md).
5. Read `.state/<run-id>/validation.json` and reproduce the failing read-only query directly.
6. Repair only the smallest identified mismatch, then rerun validation.
7. If a prerequisite is absent, record `skipped` or `warning`; never convert a gate into a false pass.

## Expected reasoning

Operations should follow evidence: establish baseline, detect and scope the fault, repair the smallest cause, validate service state, then prove backup or recovery objectives before cleanup.

The permission boundary is: Contributor, Monitoring Contributor, Backup Contributor, and Network Contributor on the capstone resource group

The live gate is: The live recovery drill requires cost review and an isolated workload; production failover or irreversible deletion is never inferred from this capstone.

## Common failure classes

- **Context mismatch:** select the intended context yourself and rerun preflight. The scripts intentionally do not sign in or switch it.
- **Authorization failure:** inspect the failed action and required scope. Do not broaden to subscription or tenant scope without a justified objective.
- **Provider, quota, SKU, or region failure:** use the preflight evidence and choose an approved supported region/SKU; document any fallback.
- **Eventual consistency:** poll the documented operation state and retain timestamps. Do not interpret a transient empty query as final success.
- **Network or DNS failure:** inspect effective routes/rules, name resolution, private DNS links, listener/probe state, and the guest firewall/application separately.
- **Cleanup dependency:** remove recorded locks, role/policy assignments, protection or replication state, private links, and retained data in the service's required order.

## Completion evidence

A defensible result includes a run manifest, independent validation report, redacted CLI or PowerShell evidence, and a cleanup/residual audit. Offline repository tests alone do not establish live verification.
