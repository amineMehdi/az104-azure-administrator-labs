# Lab 25 solution and diagnostic notes

Use this only after completing the lab and knowledge check. The solution is evidence-led: it does not replace the independent validator or silently repair live state.

## Intended checkpoint sequence

1. **Checkpoint 1:** Create non-overlapping source and recovery VNets in the configured primary and secondary regions.
2. **Checkpoint 2:** Create a source VM and Recovery Services vault, then configure Azure-to-Azure fabric, container, policy, and network mappings.
3. **Checkpoint 3:** Enable replication and wait for protected health before running an isolated test failover into a test subnet.
4. **Checkpoint 4:** Clean up test failover, compare planned and unplanned failover, and remove replication in the required order before vault deletion.

## Diagnostic order

1. Confirm that the active tenant and subscription match `.state/<run-id>/run.json`.
2. Confirm the exact resource group or tenant object ID; do not select by a name prefix.
3. Inspect provider registration, service quota, region support, and asynchronous provisioning state.
4. Compare the live configuration with the checkpoint statement in [the lab guide](../README.md).
5. Read `.state/<run-id>/validation.json` and reproduce the failing read-only query directly.
6. Repair only the smallest identified mismatch, then rerun validation.
7. If a prerequisite is absent, record `skipped` or `warning`; never convert a gate into a false pass.

## Expected reasoning

Test failover validates recovery without committing production direction, while planned/unplanned failover, commit, reprotect, and failback are separate state transitions with cost and data-loss implications.

The permission boundary is: Site Recovery Contributor, Virtual Machine Contributor, and Network Contributor on both region scopes

The live gate is: This elevated lab requires two approved regions and explicit cost review before live execution; test failover must use an isolated network.

## Common failure classes

- **Context mismatch:** select the intended context yourself and rerun preflight. The scripts intentionally do not sign in or switch it.
- **Authorization failure:** inspect the failed action and required scope. Do not broaden to subscription or tenant scope without a justified objective.
- **Provider, quota, SKU, or region failure:** use the preflight evidence and choose an approved supported region/SKU; document any fallback.
- **Eventual consistency:** poll the documented operation state and retain timestamps. Do not interpret a transient empty query as final success.
- **Network or DNS failure:** inspect effective routes/rules, name resolution, private DNS links, listener/probe state, and the guest firewall/application separately.
- **Cleanup dependency:** remove recorded locks, role/policy assignments, protection or replication state, private links, and retained data in the service's required order.

## Completion evidence

A defensible result includes a run manifest, independent validation report, redacted CLI or PowerShell evidence, and a cleanup/residual audit. Offline repository tests alone do not establish live verification.
