# Troubleshooting

## Start with context

Confirm the tenant, subscription, account, region, run ID, and current lab state before changing anything. Many Azure failures are valid authorization, quota, policy, or regional-availability outcomes rather than command defects.

## Safe diagnosis order

1. Read the full error and correlation/request ID.
2. Run the lab preflight again.
3. Inspect provider registration, feature state, quota, SKU availability, and policy assignments.
4. Query the resource using the lab's canonical command surface.
5. Compare `.state/<run-id>/` with the live resource IDs.
6. Use the lab's read-only Azure CLI queries to corroborate state; do not bypass the documented command path with a browser workflow.

Never paste secrets, tokens, or unredacted account output into an issue.

## Common failure map

| Symptom | What it usually means | Safe diagnostic | Do not do |
|---|---|---|---|
| `AuthorizationFailed` or Graph `403` | The signed-in identity lacks the declared action at the required scope | Compare the failed operation with `lab.yml` roles/scopes and inspect assignments read-only | Grant Owner, Global Administrator, or broad Graph consent merely to continue |
| Provider is not registered | The subscription is not prepared for that resource type | Read `az provider show --namespace <namespace>` and request registration through the approved process | Let a lab register a provider implicitly |
| SKU or feature is unavailable | Region, subscription type, quota, or feature registration blocks the choice | Rerun the lab's exact region/SKU query and select only a documented approved fallback | Retry creation repeatedly or choose an expensive SKU without approval |
| `Conflict`, `AnotherOperationInProgress`, or HTTP `429` | Azure is converging or throttling requests | Inspect the operation state and retry the same read-only query with bounded backoff | Submit duplicate creates or start unbounded polling |
| Name is already in use | A global name collided or a run ID was reused | Preserve existing state and choose a fresh run ID | Delete a similarly named resource that is not in the manifest |
| DNS resolves publicly instead of privately | Private zone, link, endpoint, or client DNS context is incomplete | Compare the private endpoint IP, zone record, VNet link, and query origin | Disable the service firewall to hide the DNS problem |
| A health probe is down | The backend listener, guest firewall, route, NSG, or probe path is wrong | Test each layer independently, beginning with backend service state | Open all inbound ports or replace a Standard load balancer with a public shortcut |
| Cleanup refuses to run | Context, run ID, live ID, or ownership tags do not match `run.json` | Stop and reconcile the exact mismatch with read-only queries | Remove the ownership check or delete by name prefix |

## Resume after an interrupted setup

1. Do not rerun `Setup.ps1` with the same run ID; it intentionally refuses
   existing state.
2. Open `.state/<run-id>/run.json` and identify the last `pass`, `in-progress`,
   or `pending` checkpoint.
3. Query every recorded managed-object ID. A failed create may still have
   returned or provisioned an object.
4. Finish or repair only the documented checkpoint commands, then run
   `Validate.ps1 -Mode Deployment`.
5. If you abandon the run, preview cleanup from the recorded manifest. Never
   invent missing targets from a name prefix.

## Resume after interrupted cleanup

Cleanup is designed to be idempotent. Rerun its preview first, verify that the
active context still matches the manifest, and then rerun `-Execute`. An absent
recorded target is an acceptable end state; an ownership mismatch is not. Finish
with `Validate.ps1 -Mode PostCleanup` and inspect both `cleanup.json` and
`validation.json`.

## Tool and extension drift

Run `tools/Test-LabEnvironment.ps1 -OfflineOnly` after upgrading Azure CLI,
PowerShell, Bicep, AzCopy, Python, Node, or an Azure CLI extension. If generated
content changes, use the repository `--check` commands before rerendering so the
authoritative source of the drift is clear.
