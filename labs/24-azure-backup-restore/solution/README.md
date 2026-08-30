# Lab 24 solution and diagnostic notes

Use this only after completing the lab and knowledge check. The solution is evidence-led: it does not replace the independent validator or silently repair live state.

## Intended checkpoint sequence

1. **Checkpoint 1:** Create a Recovery Services vault and a separate modern Backup vault and compare their supported workloads.
2. **Checkpoint 2:** Create a bounded-retention VM backup policy and enable protection for the test VM.
3. **Checkpoint 3:** Trigger an on-demand backup, monitor its asynchronous job, and preserve evidence before restore testing.
4. **Checkpoint 4:** Run a restore workflow, inspect Backup reports/alerts prerequisites, then stop protection and delete backup data before vault cleanup.

## Diagnostic order

1. Confirm that the active tenant and subscription match `.state/<run-id>/run.json`.
2. Confirm the exact resource group or tenant object ID; do not select by a name prefix.
3. Inspect provider registration, service quota, region support, and asynchronous provisioning state.
4. Compare the live configuration with the checkpoint statement in [the lab guide](../README.md).
5. Read `.state/<run-id>/validation.json` and reproduce the failing read-only query directly.
6. Repair only the smallest identified mismatch, then rerun validation.
7. If a prerequisite is absent, record `skipped` or `warning`; never convert a gate into a false pass.

## Expected reasoning

Vault type must match the workload, protection creates retained recovery points, and vault deletion requires ordered removal of protected items, soft-delete state, and dependencies.

The permission boundary is: Backup Contributor and Virtual Machine Contributor on the lab resource group

The live gate is: None beyond the declared role and a disposable subscription.

## Common failure classes

- **Context mismatch:** select the intended context yourself and rerun preflight. The scripts intentionally do not sign in or switch it.
- **Authorization failure:** inspect the failed action and required scope. Do not broaden to subscription or tenant scope without a justified objective.
- **Provider, quota, SKU, or region failure:** use the preflight evidence and choose an approved supported region/SKU; document any fallback.
- **Eventual consistency:** poll the documented operation state and retain timestamps. Do not interpret a transient empty query as final success.
- **Network or DNS failure:** inspect effective routes/rules, name resolution, private DNS links, listener/probe state, and the guest firewall/application separately.
- **Cleanup dependency:** remove recorded locks, role/policy assignments, protection or replication state, private links, and retained data in the service's required order.

## Completion evidence

A defensible result includes a run manifest, independent validation report, redacted CLI or PowerShell evidence, and a cleanup/residual audit. Offline repository tests alone do not establish live verification.
