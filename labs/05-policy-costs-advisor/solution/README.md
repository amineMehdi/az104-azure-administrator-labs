# Lab 05 solution and diagnostic notes

Use this only after completing the guided lab. In Labs 01–25, complete the knowledge check before reading these notes. The solution is evidence-led: it does not replace the independent validator or silently repair live state.

## Intended checkpoint sequence

1. **Checkpoint 1:** Create the tagged policy-test resource group.
2. **Checkpoint 2:** Assign the built-in Require a tag and its value on resources policy at resource-group scope.
3. **Checkpoint 3:** Trigger and interpret a policy compliance scan without claiming immediate convergence.
4. **Checkpoint 4:** Read Advisor cost recommendations and create an optional low-threshold budget with AZ104_BUDGET_EMAIL.
5. **Checkpoint 5:** Correlate service state with the run manifest, retain redacted validation evidence, and prove cleanup readiness.

## Diagnostic order

1. Confirm that the active tenant and subscription match `.state/<run-id>/run.json`.
2. Confirm the exact resource group or tenant object ID; do not select by a name prefix.
3. Inspect provider registration, service quota, region support, and asynchronous provisioning state.
4. Compare the live configuration with the checkpoint statement in [the lab guide](../README.md).
5. Read `.state/<run-id>/validation.json` and reproduce the failing read-only query directly.
6. Repair only the smallest identified mismatch, then rerun validation.
7. If a prerequisite is absent, record `skipped` or `warning`; never convert a gate into a false pass.

## Expected reasoning

Policy compliance is eventually evaluated, budgets notify rather than stop spending, and Advisor recommendations remain advisory until an administrator acts.

The permission boundary is: Resource Policy Contributor at the lab scope; Cost Management Contributor for the optional budget path

The live gate is: Budget creation requires AZ104_BUDGET_EMAIL and Cost Management authorization; otherwise the lab inventories cost controls without creating one.

## Common failure classes

- **Context mismatch:** select the intended context yourself and rerun preflight. The scripts intentionally do not sign in or switch it.
- **Authorization failure:** inspect the failed action and required scope. Do not broaden to subscription or tenant scope without a justified objective.
- **Provider, quota, SKU, or region failure:** use the preflight evidence and choose an approved supported region/SKU; document any fallback.
- **Eventual consistency:** poll the documented operation state and retain timestamps. Do not interpret a transient empty query as final success.
- **Network or DNS failure:** inspect effective routes/rules, name resolution, private DNS links, listener/probe state, and the guest firewall/application separately.
- **Cleanup dependency:** remove recorded locks, role/policy assignments, protection or replication state, private links, and retained data in the service's required order.

## Completion evidence

A defensible result includes a run manifest, independent validation report, redacted Azure CLI evidence captured from PowerShell, and a cleanup/residual audit. Offline repository tests alone do not establish live verification.
