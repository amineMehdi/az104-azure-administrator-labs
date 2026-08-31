
<!-- BEGIN GENERATED AZ104 V2 -->
# Lab 26: Capstone — Build a governed, secure, observable Azure workload

[Previous: Lab 25](../25-site-recovery-failover/README.md) · [Catalog](../README.md) · [Next: Lab 27](../27-capstone-operate-recover/README.md)

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: You are a platform engineer building a governed, secure, observable workload. Build and prove this disposable service path: Bicep creates the governed network, data, and telemetry foundation; two private VMs join the load-balancer pool, Blob access follows private endpoint/DNS, and Policy, diagnostics, and optional RBAC remain bounded to recorded IDs.

Learner role: A platform engineer building a governed, secure, observable workload.

Outcome: Use Azure CLI in PowerShell to deploy the governed network, compute, and data foundation, build the private load-balanced application path, and reconcile the end-to-end governed workload, with recoverable state and deterministic cleanup.

| Item | Value |
|---|---|
| Duration | 180 minutes |
| Difficulty | advanced |
| Cost class | `elevated` |
| Command surface | Azure CLI (`az`, `az rest`, Bicep, AzCopy, or KQL where required) hosted in PowerShell |
| Live state | Not executed during this offline rebuild |

Completion criteria:

- All required checkpoints report pass.
- The deterministic break/fix is injected, diagnosed, and repaired.
- cleanup.json reports no active run-owned resources, with any retained item explicitly documented.

## Objectives and checkpoints

| Objective | Skill | Checkpoints |
|---|---|---|
| `IG-ACCESS-01` | Manage built-in Azure roles | `LAB26-CP01`, `LAB26-CP05` |
| `IG-ACCESS-02` | Assign roles at different scopes | `LAB26-CP02`, `LAB26-CP05` |
| `IG-GOVERN-01` | Implement and manage Azure Policy | `LAB26-CP03`, `LAB26-CP05` |
| `IG-GOVERN-03` | Apply and manage tags on resources | `LAB26-CP04`, `LAB26-CP05` |
| `IG-GOVERN-04` | Manage resource groups | `LAB26-CP05` |
| `ST-ACCOUNTS-01` | Create and configure storage accounts | `LAB26-CP05` |
| `CP-IAC-04` | Deploy resources by using an Azure Resource Manager template or a Bicep file | `LAB26-CP05` |
| `CP-VM-01` | Create a virtual machine | `LAB26-CP05` |
| `CP-VM-06` | Deploy virtual machines to availability zones and availability sets | `LAB26-CP05` |
| `CP-VM-07` | Deploy and configure an Azure Virtual Machine Scale Sets | `LAB26-CP05` |
| `NW-VNET-01` | Create and configure virtual networks and subnets | `LAB26-CP05` |
| `NW-SECURE-01` | Create and configure network security groups (NSGs) and application security groups | `LAB26-CP05` |
| `NW-SECURE-05` | Configure private endpoints for Azure PaaS | `LAB26-CP05` |
| `NW-DNSLB-02` | Configure an internal or public load balancer | `LAB26-CP05` |
| `MR-MONITOR-02` | Configure log settings in Azure Monitor | `LAB26-CP05` |
| `MR-MONITOR-04` | Set up alert rules, action groups, and alert processing rules in Azure Monitor | `LAB26-CP05` |

The authoritative objective wording comes from the [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of 2026-04-17.

## Architecture and service topology

![Lab 26 service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). Bicep creates the governed network, data, and telemetry foundation; two private VMs join the load-balancer pool, Blob access follows private endpoint/DNS, and Policy, diagnostics, and optional RBAC remain bounded to recorded IDs.

## Concept primer and design decisions

The build capstone integrates infrastructure as code, segmentation, resilient compute, private data access, RBAC, Policy, diagnostics, and alerts. Success means the components work together and can be removed from the recorded ownership boundary.

Design decisions:

- Use Bicep build and what-if as release gates.
- Keep data private and compute resilient.
- Validate governance and observability before handoff.

## Required and optional inputs

| Input | Required | Source | Safe example | Gate behavior |
|---|:---:|---|---|---|
| `run-id` — Unique lowercase run ownership identifier | Yes | parameter | `az104l26-01` | `block` |
| `subscription-id` — Expected disposable subscription ID | Yes | parameter-or-environment (`AZ104_SUBSCRIPTION_ID`) | `00000000-0000-0000-0000-000000000000` | `block` |
| `location` — Approved primary Azure region | Yes | parameter-or-environment (`AZ104_LOCATION`) | `westeurope` | `block` |
| `principal-object-id` — Optional disposable principal for capstone RBAC | No | environment (`AZ104_PRINCIPAL_OBJECT_ID`) | `00000000-0000-0000-0000-000000000000` | `skip-checkpoint` |

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l26-01' -Location 'westeurope'
```

Representative redacted output:

```text
context                 True  cloud=AzureCloud; tenant=<redacted>; subscription=<redacted>
azure-cli               True  2.88.x
provider:<namespace>    True  Registered
region                  True  westeurope
Preflight passed. It performed no Azure mutation.
```

If a required row fails, stop. Correct the local tool, context, provider, quota, SKU, region, permission, or input outside the lab, then rerun preflight.

## Task 1 — Verify governed workload deployment prerequisites {#task-1}

Checkpoint: `LAB26-CP01`

Purpose and operational relevance: Read the provider, region, SKU, feature, quota, and companion-tool signals needed for verify governed workload deployment prerequisites, without changing Azure state. The change is unsafe when one missing provider or role can allow early resources to deploy but block governance or observability later. This checkpoint therefore proves: Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az bicep build --file "$LabRoot/artifacts/main.bicep" --outfile "$StateDir/main.json"
az provider show --namespace Microsoft.Compute --query registrationState --output tsv
az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the backend keys.' }
```

Expected state: Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.

Representative redacted output:

```text
Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.
```

Positive validation:

```powershell
$compute = az provider show --namespace Microsoft.Compute --query registrationState --output tsv
if ($compute -ne 'Registered') { throw 'Microsoft.Compute is not registered.' }
```

Expected positive result: Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.

Negative validation:

```powershell
$sku = az vm list-skus --location $Location --size Standard_B1s --all --query '[?name==`Standard_B1s` && (restrictions==null || length(restrictions)==`0`)] | length(@)' --output tsv
if ([int]$sku -lt 1) { throw 'Standard_B1s is restricted in this region.' }
```

Expected negative result: LAB26-CP01 negative boundary: The undesired state is absent; the negative assertion must not report: Standard_B1s is restricted in this region.

Evidence to retain:

- LAB26-CP01 UTC result for verify governed workload deployment prerequisites.
- Exact run-owned resource/object ID returned by the commands in LAB26-CP01.
- Positive assertion proving: Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.
- Negative assertion proving absence of: Standard_B1s is restricted in this region.

Common failure and safe retry: One missing provider or role can allow early resources to deploy but block governance or observability later. Retry LAB26-CP01 for verify governed workload deployment prerequisites only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB26-CP02, LAB26-CP03, LAB26-CP04, LAB26-CP05, remove the exact manifest IDs created or configured by LAB26-CP01 for verify governed workload deployment prerequisites; its residual probe must then return zero active IDs.

## Task 2 — Deploy the governed network, compute, and data foundation {#task-2}

Checkpoint: `LAB26-CP02`

Purpose and operational relevance: Provision and immediately inventory the exact run-owned resources needed to deploy the governed network, compute, and data foundation, so partial completion remains recoverable. The change is unsafe when a storage-name collision or Bicep what-if discrepancy must be resolved before continuing to dependent resources. This checkpoint therefore proves: The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$storage = "st26$suffix"; $vnet = "vnet-$suffix"; $workspace = "law-$suffix"; $loadBalancer = "lb-$suffix"; $nsg = "nsg-$suffix"; $vm1 = "vm-1-$suffix"; $vm2 = "vm-2-$suffix"; $privateEndpoint = "pe-$suffix"
az deployment group what-if --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --result-format ResourceIdOnly --no-pretty-print | Set-Content -LiteralPath "$StateDir/what-if.txt"
az deployment group create --resource-group $ResourceGroupName --name "capstone-$RunId" --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --output none
az network nsg create --resource-group $ResourceGroupName --name $nsg --location $Location --output none
az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowLoadBalancerSsh --priority 200 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes AzureLoadBalancer --destination-port-ranges 22 --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name web --network-security-group $nsg --output none
az network lb address-pool create --resource-group $ResourceGroupName --lb-name $loadBalancer --name backends --output none
az network lb probe create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --port 22 --interval 5 --threshold 2 --output none
az network lb rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --frontend-port 2222 --backend-port 22 --frontend-ip-name frontend --backend-pool-name backends --probe-name ssh --disable-outbound-snat true --output none
```

Expected state: The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.

Representative redacted output:

```text
The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.
```

Positive validation:

```powershell
$deployment = az deployment group show --resource-group $ResourceGroupName --name "capstone-$RunId" --query properties.provisioningState --output tsv
if ($deployment -ne 'Succeeded') { throw "Capstone Bicep deployment state is $deployment." }
```

Expected positive result: The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.

Negative validation:

```powershell
$publicAccess = az storage account show --resource-group $ResourceGroupName --name $storage --query publicNetworkAccess --output tsv
if ($publicAccess -ne 'Disabled') { throw 'Capstone storage public network access is enabled.' }
```

Expected negative result: LAB26-CP02 negative boundary: The undesired state is absent; the negative assertion must not report: Capstone storage public network access is enabled.

Evidence to retain:

- LAB26-CP02 UTC result for deploy the governed network, compute, and data foundation.
- Exact run-owned resource/object ID returned by the commands in LAB26-CP02.
- Positive assertion proving: The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.
- Negative assertion proving absence of: Capstone storage public network access is enabled.

Common failure and safe retry: A storage-name collision or Bicep what-if discrepancy must be resolved before continuing to dependent resources. Retry LAB26-CP02 for deploy the governed network, compute, and data foundation only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB26-CP03, LAB26-CP04, LAB26-CP05, remove the exact manifest IDs created or configured by LAB26-CP02 for deploy the governed network, compute, and data foundation; its residual probe must then return zero active IDs.

## Task 3 — Build the private load-balanced application path {#task-3}

Checkpoint: `LAB26-CP03`

Purpose and operational relevance: Configure and independently inspect the control-plane and data-path properties needed to build the private load-balanced application path. The change is unsafe when disabling public storage access before private endpoint/DNS convergence can make validation appear to lose the data service. This checkpoint therefore proves: Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
foreach ($index in 1..2) {
    $nic = "nic-$index-$suffix"; $vm = "vm-$index-$suffix"
    az network nic create --resource-group $ResourceGroupName --name $nic --vnet-name $vnet --subnet web --network-security-group $nsg --output none
    az network nic ip-config address-pool add --resource-group $ResourceGroupName --nic-name $nic --ip-config-name ipconfig1 --lb-name $loadBalancer --address-pool backends --output none
    az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics $nic --output none
}
$storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
az network private-endpoint create --resource-group $ResourceGroupName --name $privateEndpoint --location $Location --vnet-name $vnet --subnet private-endpoints --private-connection-resource-id $storageId --group-id blob --connection-name "storage-$suffix" --output none
az network private-dns zone create --resource-group $ResourceGroupName --name privatelink.blob.core.windows.net --output none
az network private-dns link vnet create --resource-group $ResourceGroupName --zone-name privatelink.blob.core.windows.net --name "link-$suffix" --virtual-network $vnet --registration-enabled false --output none
az network private-endpoint dns-zone-group create --resource-group $ResourceGroupName --endpoint-name $privateEndpoint --name default --private-dns-zone privatelink.blob.core.windows.net --zone-name blob --output none
$workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
$metricCategories = az monitor diagnostic-settings categories list --resource $storageId --query "value[?categoryType=='Metrics'].name" --output tsv
$metricArgs = @($metricCategories | ForEach-Object { @{ category = $_; enabled = $true } }) | ConvertTo-Json -Compress
az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics $metricArgs --output none
$policyName = az policy definition list --query "[?displayName=='Audit VMs that do not use managed disks'].name | [0]" --output tsv
if (-not $policyName) { throw 'The built-in managed-disk audit policy definition was not found.' }
az policy assignment create --name "managed-disks-$suffix" --display-name 'AZ-104 managed disk audit' --policy $policyName --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output none
```

Expected state: Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.

Representative redacted output:

```text
Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.
```

Positive validation:

```powershell
$poolMembers = az network lb address-pool show --resource-group $ResourceGroupName --lb-name $loadBalancer --name backends --query "backendIPConfigurations | length(@)" --output tsv
if ([int]$poolMembers -ne 2) { throw "Load Balancer backend count is $poolMembers." }
```

Expected positive result: Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.

Negative validation:

```powershell
$connection = az network private-endpoint show --resource-group $ResourceGroupName --name $privateEndpoint --query "privateLinkServiceConnections[0].privateLinkServiceConnectionState.status" --output tsv
if ($connection -ne 'Approved') { throw "Private endpoint state is $connection." }
```

Expected negative result: LAB26-CP03 negative boundary: The undesired state is absent; the negative assertion must not report: Private endpoint state is reported connection.

Evidence to retain:

- LAB26-CP03 UTC result for build the private load-balanced application path.
- Exact run-owned resource/object ID returned by the commands in LAB26-CP03.
- Positive assertion proving: Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.
- Negative assertion proving absence of: Private endpoint state is reported connection.

Common failure and safe retry: Disabling public storage access before private endpoint/DNS convergence can make validation appear to lose the data service. Retry LAB26-CP03 for build the private load-balanced application path only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB26-CP04, LAB26-CP05, remove the exact manifest IDs created or configured by LAB26-CP03 for build the private load-balanced application path; its residual probe must then return zero active IDs.

## Task 4 — Apply governance, observability, and least-privilege access {#task-4}

Checkpoint: `LAB26-CP04`

Purpose and operational relevance: Exercise the deterministic operational or denied path needed to apply governance, observability, and least-privilege access, then retain comparable before-and-after results. The change is unsafe when an empty or incorrect principal ID must skip the optional RBAC checkpoint rather than create a broader assignment. This checkpoint therefore proves: Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
$external['capstoneRoleAssignmentId'] = az role assignment create --assignee-object-id $env:AZ104_PRINCIPAL_OBJECT_ID --assignee-principal-type User --role Reader --scope $scope --query id --output tsv
```

Expected state: Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.

Representative redacted output:

```text
Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.
```

Positive validation:

```powershell
$assignments = az role assignment list --assignee $env:AZ104_PRINCIPAL_OBJECT_ID --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --query "[?roleDefinitionName=='Reader'] | length(@)" --output tsv
if ([int]$assignments -ne 1) { throw 'The optional capstone Reader assignment is absent or duplicated.' }
```

Expected positive result: Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.

Negative validation:

```powershell
$owner = az role assignment list --assignee $env:AZ104_PRINCIPAL_OBJECT_ID --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --query "[?roleDefinitionName=='Owner'] | length(@)" --output tsv
if ([int]$owner -ne 0) { throw 'The optional principal has an overbroad Owner assignment.' }
```

Expected negative result: LAB26-CP04 negative boundary: The undesired state is absent; the negative assertion must not report: The optional principal has an overbroad Owner assignment.

Evidence to retain:

- LAB26-CP04 UTC result for apply governance, observability, and least-privilege access.
- Exact run-owned resource/object ID returned by the commands in LAB26-CP04.
- Positive assertion proving: Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.
- Negative assertion proving absence of: The optional principal has an overbroad Owner assignment.

Common failure and safe retry: An empty or incorrect principal ID must skip the optional RBAC checkpoint rather than create a broader assignment. Retry LAB26-CP04 for apply governance, observability, and least-privilege access only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After LAB26-CP05, remove the exact manifest IDs created or configured by LAB26-CP04 for apply governance, observability, and least-privilege access; its residual probe must then return zero active IDs.

## Task 5 — Reconcile the end-to-end governed workload {#task-5}

Checkpoint: `LAB26-CP05`

Purpose and operational relevance: Reconcile live service properties, returned IDs, and dependency-aware removal needed to reconcile the end-to-end governed workload before handoff. The change is unsafe when validating each service separately can miss a broken cross-service ID, DNS link, or scope boundary. This checkpoint therefore proves: Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az network lb show --resource-group $ResourceGroupName --name $loadBalancer --query "{sku:sku.name,frontend:frontendIPConfigurations[0].name,pool:backendAddressPools[0].name,probe:probes[0].port,rule:loadBalancingRules[0].frontendPort}" --output json
az vm list --resource-group $ResourceGroupName --show-details --query "[].{name:name,power:powerState,publicIp:publicIps}" --output table
az policy assignment show --name "managed-disks-$suffix" --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output json
```

Expected state: Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.

Representative redacted output:

```text
Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.
```

Positive validation:

```powershell
$running = az vm list --resource-group $ResourceGroupName --show-details --query "[?powerState=='VM running'] | length(@)" --output tsv
if ([int]$running -ne 2) { throw "Expected two running capstone backends; found $running." }
```

Expected positive result: Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.

Negative validation:

```powershell
$publicBackends = az vm list --resource-group $ResourceGroupName --show-details --query "[?publicIps!=null && publicIps!=''] | length(@)" --output tsv
if ([int]$publicBackends -ne 0) { throw 'A backend VM has a public IP.' }
```

Expected negative result: LAB26-CP05 negative boundary: The undesired state is absent; the negative assertion must not report: A backend VM has a public IP.

Evidence to retain:

- LAB26-CP05 UTC result for reconcile the end-to-end governed workload.
- Exact run-owned resource/object ID returned by the commands in LAB26-CP05.
- Positive assertion proving: Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.
- Negative assertion proving absence of: A backend VM has a public IP.

Common failure and safe retry: Validating each service separately can miss a broken cross-service ID, DNS link, or scope boundary. Retry LAB26-CP05 for reconcile the end-to-end governed workload only after its exact recorded ID and current property are read. If the ID exists, reissue only the idempotent update; if it is absent, repeat only the owning create command, then rerun both assertions.

Cleanup dependency: After all service validation and evidence capture, remove the exact manifest IDs created or configured by LAB26-CP05 for reconcile the end-to-end governed workload; its residual probe must then return zero active IDs.

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l26-01' -Mode Deployment
az resource list --resource-group 'rg-az104-l26-az104l26-01' --query '[].{name:name,type:type}' --output table
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: Add a higher-priority inbound deny for the backend probe and SSH service.

Inject the bounded fault:

```powershell
az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name DenyInjectedProbe --priority 100 --direction Inbound --access Deny --protocol Tcp --source-address-prefixes AzureLoadBalancer --destination-port-ranges 22 --output none
```

Capture the failed state with a read-only query:

```powershell
az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-1-$suffix" --output json
```

Repair only the injected setting, then repeat the same query:

```powershell
az network nsg rule delete --resource-group $ResourceGroupName --nsg-name $nsg --name DenyInjectedProbe
az network nsg rule list --resource-group $ResourceGroupName --nsg-name $nsg --query "[?destinationPortRange=='22'].{name:name,priority:priority,access:access}" --output table
```

Expected symptom: The Load Balancer probe cannot reach either backend although ARM provisioning remains successful.

Diagnose with a read-only service query:

```powershell
az network nic list-effective-nsg --resource-group $ResourceGroupName --name "nic-1-$suffix" --output json
```

Diagnosis: Compare the custom NSG rule priority with the AzureLoadBalancer allow and inspect effective rules on a backend NIC.

Repair: Delete only the injected rule and retain the run-owned probe allow.

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

Prepare a job-style handoff containing architecture, risks, validation, cost controls, operations, and rollback.

Deliver a short change record containing assumptions, exact commands, redacted evidence, cost and risk notes, rollback, and residual results. The challenge is optional and never changes required checkpoint status.

## Troubleshooting

| Symptom | Likely cause | Safe next step |
|---|---|---|
| Context mismatch | Active CLI context differs from `run.json` | Stop, inspect `az account show`, and select the intended disposable context yourself. |
| Provider or feature unavailable | Registration, region, feature, or SKU gate is unmet | Read the preflight result; do not register or enable tenant features implicitly. |
| Name already exists | The run ID is reused or a globally unique name collided | Keep existing state intact and choose a new run ID. |
| Expected state is delayed | The service is converging asynchronously | Repeat only the read-only query with bounded retries; do not duplicate creation. |
| Permission denied | Role, Graph scope, or data-plane authorization is insufficient | Confirm the declared least-privilege boundary; do not broaden access automatically. |
| Cleanup refuses ownership | ID, context, or tags differ from the manifest | Investigate the mismatch; never bypass ownership verification. |

## Cleanup and residual verification

Preview exact targets first, execute only after ownership review, then validate post-cleanup:

```powershell
./scripts/cli/Cleanup.ps1 -RunId 'az104l26-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l26-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l26-01' -Mode PostCleanup
$publicBackends = az vm list --resource-group $ResourceGroupName --show-details --query "[?publicIps!=null && publicIps!=''] | length(@)" --output tsv
if ([int]$publicBackends -ne 0) { throw 'A backend VM has a public IP.' }
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

This hands-on lab has no separate question set. Use the [domain assessment dashboard](../../docs/question-bank-index.md) to choose review questions.

## Microsoft Learn sources

- [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Deploy Bicep files with Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)
- [Create a public Standard Load Balancer with Azure CLI](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-cli)
- [Use private endpoints for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
- [Assign Azure Policy with Azure CLI](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-azurecli)

## Lifecycle script appendix

The guided task blocks above and these executable scripts are generated from the same checkpoint data. The scripts are an optional automated lane; use a different run ID if you already completed the guided lane.

### `Preflight.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and [string]$account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. Preflight will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
# The account read above is the mandatory context gate. All remaining Azure
# probes are collected as results instead of allowing one unavailable SKU or
# provider query to abort the readiness report before it can explain the gap.
$PSNativeCommandUseErrorActionPreference = $false
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$ResourceGroupName = $(if ('26' -in @('00', '01', '02')) { $null } else { "rg-az104-l26-$RunId" })

$checks = [System.Collections.Generic.List[object]]::new()
function Add-PreflightResult {
    param([string]$Id, [bool]$Required, [bool]$Passed, [string]$Actual)
    $checks.Add([pscustomobject]@{ id = $Id; required = $Required; passed = $Passed; actual = $Actual })
}

Add-PreflightResult -Id 'context' -Required $true -Passed $true -Actual "cloud=$($account.environmentName); tenant=<redacted>; subscription=<redacted>"
$azVersion = (az version --query '"azure-cli"' --output tsv)
$bicepVersion = (az bicep version 2>&1 | Out-String).Trim()
Add-PreflightResult -Id 'azure-cli' -Required $true -Passed ([bool]$azVersion) -Actual $azVersion
Add-PreflightResult -Id 'powershell' -Required $true -Passed ($PSVersionTable.PSVersion -ge [version]'7.4') -Actual $PSVersionTable.PSVersion.ToString()
Add-PreflightResult -Id 'bicep' -Required $true -Passed ([bool]$bicepVersion) -Actual $bicepVersion

$requiredEnvironmentVariables = @()
foreach ($variableName in $requiredEnvironmentVariables) {
    $present = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($variableName))
    Add-PreflightResult -Id "input:$variableName" -Required $true -Passed $present -Actual $(if ($present) { 'present (value redacted)' } else { 'missing' })
}

$providers = @(
    'Microsoft.Authorization'
    'Microsoft.Compute'
    'Microsoft.Insights'
    'Microsoft.Network'
    'Microsoft.OperationalInsights'
    'Microsoft.Storage'
)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) { $registrationState } else { 'Unavailable' })
}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) { $knownLocation } else { 'not available' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_PRINCIPAL_OBJECT_ID'))
Add-PreflightResult -Id 'optional-gate:AZ104_PRINCIPAL_OBJECT_ID' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$usage = az vm list-usage --location $Location --output json 2>$null | ConvertFrom-Json
Add-PreflightResult -Id 'regional-compute-quota' -Required $false -Passed ($LASTEXITCODE -eq 0) -Actual "entries=$(@($usage).Count)"

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$compute = az provider show --namespace Microsoft.Compute --query registrationState --output tsv
if ($compute -ne 'Registered') { throw 'Microsoft.Compute is not registered.' }
$sku = az vm list-skus --location $Location --size Standard_B1s --all --query '[?name==`Standard_B1s` && (restrictions==null || length(restrictions)==`0`)] | length(@)' --output tsv
if ([int]$sku -lt 1) { throw 'Standard_B1s is restricted in this region.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.service' -Required $true -Passed $probePassed -Actual $probeActual

$checks | Format-Table -AutoSize
$failedRequired = @($checks | Where-Object { $_.required -and -not $_.passed })
if ($failedRequired.Count -gt 0) {
    throw "Preflight blocked: $($failedRequired.id -join ', ')"
}
Write-Host 'Preflight passed. It performed no sign-in, context switch, provider registration, or Azure mutation.'
# END GENERATED AZ104 V2
```

### `Setup.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZ104_SECONDARY_LOCATION,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange,
    [switch]$Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ResourceGroupName = $(if ('26' -in @('00', '01', '02')) { $null } else { "rg-az104-l26-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-26 execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}
if ($true -and -not $AcknowledgeCost) { throw 'This lab requires -AcknowledgeCost before execution.' }
if ($false -and -not $AcknowledgeTenantChange) { throw 'This lab requires -AcknowledgeTenantChange before execution.' }

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest. Choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-26'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB26-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB26-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
    )
    managedObjects = @()
    originalSettings = @()
}
$external = @{}

function Save-RunState {
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

function Save-ExternalState {
    foreach ($key in @($external.Keys)) {
        $value = $external[$key]
        if ($null -eq $value -or $value -is [string] -or $value -is [ValueType]) {
            $inputKey = 'external-' + (([string]$key -creplace '([a-z0-9])([A-Z])', '$1-$2') -replace '[^a-zA-Z0-9-]', '-').ToLowerInvariant()
            $state.inputs[$inputKey] = $value
        }
    }
    Save-RunState
}

function Write-CheckpointState {
    param([string]$CheckpointId, [string]$Status, [string]$Message)
    $entry = @($state.checkpointStates | Where-Object { $_.checkpointId -eq $CheckpointId })[0]
    $entry.status = $Status
    $entry.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $entry.message = $Message
}

function Add-ManagedObject {
    param([string]$CheckpointId, [string]$Kind, [string]$Id, [string]$Name, [string]$Type, [string]$Scope, [string]$OwnershipMethod)
    if ([string]::IsNullOrWhiteSpace($Id)) { return }
    $existing = @($state.managedObjects | Where-Object { $_.id -eq $Id })
    if ($existing.Count -gt 0) { return }
    $expectedTags = @{}
    if ($OwnershipMethod -eq 'manifest-id-and-tags') {
        $expectedTags = @{ purpose = 'az104-lab'; labId = '26'; runId = $RunId }
    }
    $state.managedObjects += @{
        checkpointId = $CheckpointId
        kind = $Kind
        id = $Id
        name = $Name
        type = $Type
        scope = $Scope
        ownership = @{ method = $OwnershipMethod; expectedTags = $expectedTags }
        recordedAt = (Get-Date).ToUniversalTime().ToString('o')
        lifecycleStatus = 'active'
    }
    Save-RunState
}

function Sync-ManagedResource {
    param([string]$CheckpointId)
    # The entire recovery inventory is best effort so a state-helper or Azure
    # query failure cannot mask the original mutation error. Every object that
    # can be recovered is still persisted immediately as it is discovered.
    $nativePreference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        Save-ExternalState
        $resourceGroupNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
        if ($ResourceGroupName) { $null = $resourceGroupNames.Add([string]$ResourceGroupName) }
        foreach ($key in @($external.Keys | Where-Object { [string]$_ -match '(?i)ResourceGroupName$' })) {
            if ($external[$key]) { $null = $resourceGroupNames.Add([string]$external[$key]) }
        }
        foreach ($groupName in $resourceGroupNames) {
            $groupJson = az group show --subscription $SubscriptionId --name $groupName --output json 2>$null
            $group = $(if ($LASTEXITCODE -eq 0 -and $groupJson) { $groupJson | ConvertFrom-Json } else { $null })
            if ($group) {
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB26-CP01' } else { $CheckpointId })
                Add-ManagedObject -CheckpointId $groupCheckpoint -Kind 'azure-resource' -Id ([string]$group.id) -Name ([string]$group.name) -Type 'Microsoft.Resources/resourceGroups' -Scope "/subscriptions/$SubscriptionId" -OwnershipMethod 'manifest-id-and-tags'
                $resourcesJson = az resource list --subscription $SubscriptionId --resource-group $groupName --output json 2>$null
                $resources = @($(if ($LASTEXITCODE -eq 0 -and $resourcesJson) { $resourcesJson | ConvertFrom-Json } else { @() }))
                foreach ($resource in $resources) {
                    Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$resource.id) -Name ([string]$resource.name) -Type ([string]$resource.type) -Scope ([string]$group.id) -OwnershipMethod 'manifest-id-and-tags'
                }
            }
        }
        if ($external.ContainsKey('groupId') -and $external.groupId) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.groupId) -Name 'lab-group' -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        if ($external.ContainsKey('guestUserId') -and $external.guestUserId) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'guest-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        if ($external.ContainsKey('userIds')) {
            foreach ($userId in @($external.userIds)) { Add-ManagedObject -CheckpointId $CheckpointId -Kind 'entra-object' -Id ([string]$userId) -Name 'lab-user' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id' }
        }
        if ($external.ContainsKey('delegationRecordId') -and $external.delegationRecordId) {
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.delegationRecordId) -Name ([string]$external.delegationRecordName) -Type 'Microsoft.Network/dnsZones/NS' -Scope ([string]$external.parentZoneId) -OwnershipMethod 'manifest-id'
        }
        if ($external.ContainsKey('connectionMonitorId') -and $external.connectionMonitorId) {
            Add-ManagedObject -CheckpointId $CheckpointId -Kind 'azure-resource' -Id ([string]$external.connectionMonitorId) -Name ([string]$external.connectionMonitorName) -Type 'Microsoft.Network/networkWatchers/connectionMonitors' -Scope ([string]$external.networkWatcherId) -OwnershipMethod 'manifest-id'
        }
    } catch {
        Write-Warning "Recovery inventory for $CheckpointId was incomplete: $($_.Exception.Message)"
    } finally {
        $PSNativeCommandUseErrorActionPreference = $nativePreference
    }
}

# The manifest exists before the first Azure mutation.
Save-RunState
$state.status = 'setup-in-progress'
Save-RunState

$expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
try {
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=26 runId=$RunId expiresOn=$expiresOn --output none
} catch {
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'fail' -Message "Resource-group boundary creation failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
} finally {
    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
}

# CHECKPOINT LAB26-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP01'
    Save-RunState

    az bicep build --file "$LabRoot/artifacts/main.bicep" --outfile "$StateDir/main.json"
    az provider show --namespace Microsoft.Compute --query registrationState --output tsv
    az vm list-skus --location $Location --size Standard_B1s --all --query "[?name=='Standard_B1s'].name" --output tsv
    if (-not (Get-Command ssh-keygen -ErrorAction SilentlyContinue)) { throw 'ssh-keygen is required for the backend keys.' }

    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'pass' -Message 'Bicep, VM SKU, private-link, load-balancer, Policy, RBAC, and diagnostic APIs are available before the capstone mutates Azure.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP01'
    Write-CheckpointState -CheckpointId 'LAB26-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP01 END

# CHECKPOINT LAB26-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP02'
    Save-RunState

    $storage = "st26$suffix"; $vnet = "vnet-$suffix"; $workspace = "law-$suffix"; $loadBalancer = "lb-$suffix"; $nsg = "nsg-$suffix"; $vm1 = "vm-1-$suffix"; $vm2 = "vm-2-$suffix"; $privateEndpoint = "pe-$suffix"
    az deployment group what-if --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --result-format ResourceIdOnly --no-pretty-print | Set-Content -LiteralPath "$StateDir/what-if.txt"
    try {
        az deployment group create --resource-group $ResourceGroupName --name "capstone-$RunId" --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network nsg create --resource-group $ResourceGroupName --name $nsg --location $Location --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowLoadBalancerSsh --priority 200 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes AzureLoadBalancer --destination-port-ranges 22 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name web --network-security-group $nsg --output none
    try {
        az network lb address-pool create --resource-group $ResourceGroupName --lb-name $loadBalancer --name backends --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network lb probe create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --port 22 --interval 5 --threshold 2 --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }
    try {
        az network lb rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name ssh --protocol Tcp --frontend-port 2222 --backend-port 22 --frontend-ip-name frontend --backend-pool-name backends --probe-name ssh --disable-outbound-snat true --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'pass' -Message 'The Bicep deployment creates tagged network, storage, workspace, and security boundaries whose returned IDs are recorded.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP02'
    Write-CheckpointState -CheckpointId 'LAB26-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP02 END

# CHECKPOINT LAB26-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP03'
    Save-RunState

    $keyPath = Join-Path $StateDir 'id_ed25519'; ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
    foreach ($index in 1..2) {
        $nic = "nic-$index-$suffix"; $vm = "vm-$index-$suffix"
    try {
            az network nic create --resource-group $ResourceGroupName --name $nic --vnet-name $vnet --subnet web --network-security-group $nsg --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
        az network nic ip-config address-pool add --resource-group $ResourceGroupName --nic-name $nic --ip-config-name ipconfig1 --lb-name $loadBalancer --address-pool backends --output none
    try {
            az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --nics $nic --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    }
    $storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
    try {
        az network private-endpoint create --resource-group $ResourceGroupName --name $privateEndpoint --location $Location --vnet-name $vnet --subnet private-endpoints --private-connection-resource-id $storageId --group-id blob --connection-name "storage-$suffix" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-dns zone create --resource-group $ResourceGroupName --name privatelink.blob.core.windows.net --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-dns link vnet create --resource-group $ResourceGroupName --zone-name privatelink.blob.core.windows.net --name "link-$suffix" --virtual-network $vnet --registration-enabled false --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    try {
        az network private-endpoint dns-zone-group create --resource-group $ResourceGroupName --endpoint-name $privateEndpoint --name default --private-dns-zone privatelink.blob.core.windows.net --zone-name blob --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    $workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
    $metricCategories = az monitor diagnostic-settings categories list --resource $storageId --query "value[?categoryType=='Metrics'].name" --output tsv
    $metricArgs = @($metricCategories | ForEach-Object { @{ category = $_; enabled = $true } }) | ConvertTo-Json -Compress
    try {
        az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics $metricArgs --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }
    $policyName = az policy definition list --query "[?displayName=='Audit VMs that do not use managed disks'].name | [0]" --output tsv
    if (-not $policyName) { throw 'The built-in managed-disk audit policy definition was not found.' }
    try {
        az policy assignment create --name "managed-disks-$suffix" --display-name 'AZ-104 managed disk audit' --policy $policyName --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'pass' -Message 'Two private VM NICs join the backend pool, the health probe/rule are consistent, and storage uses a private endpoint plus linked DNS.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP03'
    Write-CheckpointState -CheckpointId 'LAB26-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP03 END

# CHECKPOINT LAB26-CP04 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_PRINCIPAL_OBJECT_ID'))))) {
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP04'
    Save-RunState

    $scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
    try {
        $external['capstoneRoleAssignmentId'] = az role assignment create --assignee-object-id $env:AZ104_PRINCIPAL_OBJECT_ID --assignee-principal-type User --role Reader --scope $scope --query id --output tsv
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    }

    Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'pass' -Message 'Diagnostic settings target the run-owned workspace, Policy scope is bounded, and optional RBAC targets only the supplied principal and resource scope.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP04'
    Write-CheckpointState -CheckpointId 'LAB26-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB26-CP04 END

# CHECKPOINT LAB26-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB26-CP05'
    Save-RunState

    az network lb show --resource-group $ResourceGroupName --name $loadBalancer --query "{sku:sku.name,frontend:frontendIPConfigurations[0].name,pool:backendAddressPools[0].name,probe:probes[0].port,rule:loadBalancingRules[0].frontendPort}" --output json
    az vm list --resource-group $ResourceGroupName --show-details --query "[].{name:name,power:powerState,publicIp:publicIps}" --output table
    az policy assignment show --name "managed-disks-$suffix" --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --output json

    Sync-ManagedResource -CheckpointId 'LAB26-CP05'
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'pass' -Message 'Traffic, private data access, diagnostics, Policy, tags, optional RBAC, and cleanup dependencies all resolve to one manifest-owned environment.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB26-CP05'
    Write-CheckpointState -CheckpointId 'LAB26-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB26-CP05 END

$skippedRequired = @($state.checkpointStates | Where-Object { $_.required -and $_.status -eq 'skipped' })
if ($skippedRequired.Count -gt 0) {
    $state.status = 'failed'
    Save-RunState
    throw "Required checkpoints were skipped: $($skippedRequired.checkpointId -join ', ')"
}
$skippedOptional = @($state.checkpointStates | Where-Object { -not $_.required -and $_.status -eq 'skipped' })
$state.status = $(if ($skippedOptional.Count -gt 0) { 'partial' } else { 'setup-complete' })
Save-RunState
Write-Host "Setup result: $($state.status). State: $Manifest"
Write-Host "Next: ./Validate.ps1 -RunId $RunId -Mode Deployment"
# END GENERATED AZ104 V2
```

### `Validate.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ValidationPath = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Run manifest not found: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
if ($state.labId -ne 'LAB-26' -or $state.runId -ne $RunId) { throw 'Manifest ownership does not match this lab and run ID.' }
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) { $accountJson | ConvertFrom-Json } else { $null })
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) { "tenant=$($account.tenantId); subscription=$($account.id)" } else { 'active context unavailable' })
    $contextFailure = @{
        schemaVersion = '1.0.0'; labId = 'LAB-26'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{ required = 1; passed = 0; failed = 1; skipped = 0 }
        checks = @(@{ id = 'context.active'; checkpointId = 'LAB26-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true } })
    }
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('26' -in @('00', '01', '02')) { $null } else { "rg-az104-l26-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$storage = "st26$suffix"; $vnet = "vnet-$suffix"; $workspace = "law-$suffix"; $loadBalancer = "lb-$suffix"; $nsg = "nsg-$suffix"; $vm1 = "vm-1-$suffix"; $vm2 = "vm-2-$suffix"; $privateEndpoint = "pe-$suffix"

$checks = [System.Collections.Generic.List[object]]::new()
function Add-ValidationCheck {
    param([string]$Id, [string]$CheckpointId, [string]$Kind, [bool]$Required, [bool]$Passed, [string]$Command, [string]$Expected, [string]$Actual, [bool]$Skipped = $false)
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $checks.Add(@{
        id = $Id
        checkpointId = $CheckpointId
        kind = $Kind
        required = $Required
        status = $(if ($Skipped) { 'skipped' } elseif ($Passed) { 'pass' } else { 'fail' })
        message = $(if ($Skipped) { 'Optional gate was deliberately skipped.' } elseif ($Passed) { 'Expected state observed.' } else { 'Expected state was not observed.' })
        evidence = @{ command = $Command; expected = $Expected; actual = $Actual; capturedAt = $capturedAt; redacted = $true }
    })
}

# CHECKPOINT LAB26-CP01 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB26-CP01' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP01' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab26-cp01.positive' -CheckpointId 'LAB26-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab26-cp01.negative' -CheckpointId 'LAB26-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$compute = az provider show --namespace Microsoft.Compute --query registrationState --output tsv
if ($compute -ne 'Registered') { throw 'Microsoft.Compute is not registered.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab26-cp01.positive' -CheckpointId 'LAB26-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$sku = az vm list-skus --location $Location --size Standard_B1s --all --query '[?name==`Standard_B1s` && (restrictions==null || length(restrictions)==`0`)] | length(@)' --output tsv
if ([int]$sku -lt 1) { throw 'Standard_B1s is restricted in this region.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab26-cp01.negative' -CheckpointId 'LAB26-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab26-cp01.residual' -CheckpointId 'LAB26-CP01' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB26-CP01 END

# CHECKPOINT LAB26-CP02 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB26-CP02' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP02' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab26-cp02.positive' -CheckpointId 'LAB26-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab26-cp02.negative' -CheckpointId 'LAB26-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$deployment = az deployment group show --resource-group $ResourceGroupName --name "capstone-$RunId" --query properties.provisioningState --output tsv
if ($deployment -ne 'Succeeded') { throw "Capstone Bicep deployment state is $deployment." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab26-cp02.positive' -CheckpointId 'LAB26-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$publicAccess = az storage account show --resource-group $ResourceGroupName --name $storage --query publicNetworkAccess --output tsv
if ($publicAccess -ne 'Disabled') { throw 'Capstone storage public network access is enabled.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab26-cp02.negative' -CheckpointId 'LAB26-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab26-cp02.residual' -CheckpointId 'LAB26-CP02' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB26-CP02 END

# CHECKPOINT LAB26-CP03 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB26-CP03' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP03' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab26-cp03.positive' -CheckpointId 'LAB26-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab26-cp03.negative' -CheckpointId 'LAB26-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$poolMembers = az network lb address-pool show --resource-group $ResourceGroupName --lb-name $loadBalancer --name backends --query "backendIPConfigurations | length(@)" --output tsv
if ([int]$poolMembers -ne 2) { throw "Load Balancer backend count is $poolMembers." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab26-cp03.positive' -CheckpointId 'LAB26-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$connection = az network private-endpoint show --resource-group $ResourceGroupName --name $privateEndpoint --query "privateLinkServiceConnections[0].privateLinkServiceConnectionState.status" --output tsv
if ($connection -ne 'Approved') { throw "Private endpoint state is $connection." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab26-cp03.negative' -CheckpointId 'LAB26-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab26-cp03.residual' -CheckpointId 'LAB26-CP03' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB26-CP03 END

# CHECKPOINT LAB26-CP04 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB26-CP04' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP04' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab26-cp04.positive' -CheckpointId 'LAB26-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab26-cp04.negative' -CheckpointId 'LAB26-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$assignments = az role assignment list --assignee $env:AZ104_PRINCIPAL_OBJECT_ID --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --query "[?roleDefinitionName=='Reader'] | length(@)" --output tsv
if ([int]$assignments -ne 1) { throw 'The optional capstone Reader assignment is absent or duplicated.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab26-cp04.positive' -CheckpointId 'LAB26-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$owner = az role assignment list --assignee $env:AZ104_PRINCIPAL_OBJECT_ID --scope "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName" --query "[?roleDefinitionName=='Owner'] | length(@)" --output tsv
if ([int]$owner -ne 0) { throw 'The optional principal has an overbroad Owner assignment.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab26-cp04.negative' -CheckpointId 'LAB26-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab26-cp04.residual' -CheckpointId 'LAB26-CP04' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB26-CP04 END

# CHECKPOINT LAB26-CP05 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB26-CP05' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP05' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab26-cp05.positive' -CheckpointId 'LAB26-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab26-cp05.negative' -CheckpointId 'LAB26-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
    } else {
    $positivePassed = $checkpointState.status -eq 'pass'
    $positiveActual = "checkpoint=$($checkpointState.status); managedObjects=$($checkpointObjects.Count)"
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -ne 0) { $positivePassed = $false; $positiveActual += "; missing=$($managedObject.id)" }
        }
    }

    # AUTHORED SERVICE ASSERTION: positive
    try {
        $LASTEXITCODE = 0
        & {
$running = az vm list --resource-group $ResourceGroupName --show-details --query "[?powerState=='VM running'] | length(@)" --output tsv
if ([int]$running -ne 2) { throw "Expected two running capstone backends; found $running." }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $positivePassed = $false
            $positiveActual += "; serviceProbeExit=$LASTEXITCODE"
        } else {
            $positiveActual += '; serviceProbe=pass (output not persisted)'
        }
    } catch {
        $positivePassed = $false
        $positiveActual += "; serviceProbeError=$($_.Exception.GetType().Name)"
    }
    Add-ValidationCheck -Id 'lab26-cp05.positive' -CheckpointId 'LAB26-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$publicBackends = az vm list --resource-group $ResourceGroupName --show-details --query "[?publicIps!=null && publicIps!=''] | length(@)" --output tsv
if ([int]$publicBackends -ne 0) { throw 'A backend VM has a public IP.' }
        } | Out-Null
        if ($LASTEXITCODE -ne 0) {
            $negativeProbePassed = $false
            $negativeProbeActual = "serviceProbeExit=$LASTEXITCODE"
        }
    } catch {
        $negativeProbePassed = $false
        $negativeProbeActual = "serviceProbeError=$($_.Exception.GetType().Name)"
    }
    $negativePassed = $unsafe.Count -eq 0 -and $negativeProbePassed
    $negativeActual = "unsafeObjects=$($unsafe.Count)" + "; $negativeProbeActual"
    Add-ValidationCheck -Id 'lab26-cp05.negative' -CheckpointId 'LAB26-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
    }
} else {
    $active = [System.Collections.Generic.List[string]]::new()
    foreach ($managedObject in $checkpointObjects) {
        if ($managedObject.type -eq 'Microsoft.Management/managementGroups') {
            $null = az account management-group show --name $managedObject.name --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'azure-resource') {
            $null = az resource show --ids $managedObject.id --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        } elseif ($managedObject.kind -eq 'entra-object') {
            $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($managedObject.id)" --output none 2>$null
            if ($LASTEXITCODE -eq 0) { $active.Add([string]$managedObject.id) }
        }
    }
    Add-ValidationCheck -Id 'lab26-cp05.residual' -CheckpointId 'LAB26-CP05' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB26-CP05 END

$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-26'
    runId = $RunId
    mode = $Mode
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    result = $result
    summary = @{
        required = $requiredChecks.Count
        passed = @($checks | Where-Object { $_.status -eq 'pass' }).Count
        failed = $failedChecks.Count
        skipped = $skippedChecks.Count
    }
    checks = @($checks)
}
$document | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
Write-Host "Validation $Mode result: $result"
Write-Host "Artifact: $ValidationPath"
if ($result -eq 'fail') { exit 1 }
# END GENERATED AZ104 V2
```

### `Cleanup.ps1`

```powershell
# BEGIN GENERATED AZ104 V2
#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lifecycle scripts expose a stable cross-lab interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Generated task variables are intentionally shared across checkpoint blocks.')]
param(
    [string]$SubscriptionId = $env:AZ104_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$')][string]$RunId,
    [switch]$Execute
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Run the repository readiness initializer, then retry.'
}

$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$CleanupPath = Join-Path $StateDir 'cleanup.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Run manifest not found: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -AsHashtable
$active = @($state.managedObjects | Where-Object { $_.lifecycleStatus -eq 'active' })
function Write-CleanupRefusal {
    param([string]$Message)
    $refusalActions = @($active | ForEach-Object {
        @{ checkpointId = [string]$_.checkpointId; targetId = [string]$_.id; targetType = [string]$_.type; ownership = @{ method = [string]$_.ownership.method; verified = $false }; status = 'failed'; message = $Message }
    })
    $refusal = @{
        schemaVersion = '1.0.0'; labId = 'LAB-26'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o')
        executionMode = $(if ($Execute) { 'execute' } else { 'preview' })
        result = $(if ($Execute) { 'fail' } else { 'preview' })
        ownershipVerified = $false; actions = $refusalActions
        residualChecks = @(@{ id = 'ownership.refusal'; command = 'compare manifest, active context, exact IDs, and ownership proof'; expected = 'all ownership checks pass before mutation'; actual = $Message; status = $(if ($Execute) { 'fail' } else { 'skipped' }) })
        activeManagedObjects = @($active | ForEach-Object id); retainedItems = @()
    }
    $refusal | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    throw $Message
}
if ($state.labId -ne 'LAB-26' -or $state.runId -ne $RunId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {
        try { $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) } catch { $priorRetained = @() }
    }
    $idempotent = @{
        schemaVersion = '1.0.0'; labId = 'LAB-26'; runId = $RunId
        generatedAt = (Get-Date).ToUniversalTime().ToString('o'); executionMode = 'execute'; result = 'pass'
        ownershipVerified = $true; actions = @(); activeManagedObjects = @(); retainedItems = $priorRetained
        residualChecks = @(@{ id = 'cleanup.idempotent'; command = 'read run.json active managed-object inventory'; expected = 'zero active manifest-managed objects'; actual = 'active=0; prior cleanup already completed'; status = 'pass' })
    }
    $idempotent | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
    Write-Host 'Cleanup result: pass (already cleaned)'
    Write-Host "Artifact: $CleanupPath"
    return
}
try {
    $account = az account show --output json | ConvertFrom-Json
} catch {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active Azure context could not be read.'
}
if ([string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: active context does not match the manifest.'
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('26' -in @('00', '01', '02')) { $null } else { "rg-az104-l26-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)


$ownershipVerified = $true
$verifiedOwnershipById = @{}
$absentIds = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$verifiedResourceGroupIds = [System.Collections.Generic.List[string]]::new()
$resourceGroupObjects = @($active | Where-Object { $_.type -eq 'Microsoft.Resources/resourceGroups' })
$resourceGroupObject = $resourceGroupObjects | Select-Object -First 1
$nativeProbePreference = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false

# A manifest entry is necessary but is not, by itself, proof of ownership. Verify
# each manifest-id-and-tags boundary against the live Azure tags before mutation.
foreach ($groupObject in $resourceGroupObjects) {
    $groupVerified = $false
    try {
        $tagJson = az group show --ids $groupObject.id --query tags --output json 2>$null
        if ($LASTEXITCODE -eq 0 -and $tagJson) {
            $tags = $tagJson | ConvertFrom-Json -AsHashtable
            $expectedTags = $groupObject.ownership.expectedTags
            $groupVerified =
                $groupObject.ownership.method -eq 'manifest-id-and-tags' -and
                [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                [string]$tags['runId'] -eq [string]$expectedTags['runId'] -and
                [string]$tags['purpose'] -eq 'az104-lab' -and
                [string]$tags['labId'] -eq '26' -and
                [string]$tags['runId'] -eq $RunId
        } else {
            $groupExists = az group exists --subscription $state.context.subscriptionId --name $groupObject.name --output tsv 2>$null
            if ($LASTEXITCODE -eq 0 -and $groupExists -eq 'false') {
                $null = $absentIds.Add([string]$groupObject.id)
                $groupVerified = $true
            }
        }
    } catch {
        $groupVerified = $false
    }
    $verifiedOwnershipById[[string]$groupObject.id] = $groupVerified
    if ($groupVerified) { $verifiedResourceGroupIds.Add([string]$groupObject.id) }
    if (-not $groupVerified) { $ownershipVerified = $false }
}

foreach ($object in $active) {
    $objectId = [string]$object.id
    if ($verifiedOwnershipById.ContainsKey($objectId)) { continue }
    $method = [string]$object.ownership.method
    $objectVerified = $false

    $absentGroupBoundary = @($resourceGroupObjects | Where-Object {
        $absentIds.Contains([string]$_.id) -and $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase)
    }).Count -gt 0
    if ($absentGroupBoundary) {
        $null = $absentIds.Add($objectId)
        $verifiedOwnershipById[$objectId] = $true
        continue
    }

    if ($method -eq 'manifest-id-and-tags' -and $object.kind -eq 'azure-resource') {
        $expectedTags = $object.ownership.expectedTags
        $manifestTagsMatch =
            [string]$expectedTags['purpose'] -eq 'az104-lab' -and
            [string]$expectedTags['labId'] -eq '26' -and
            [string]$expectedTags['runId'] -eq $RunId
        $verifiedByGroupBoundary = @($verifiedResourceGroupIds | Where-Object {
            $objectId.StartsWith("$_/", [System.StringComparison]::OrdinalIgnoreCase)
        }).Count -gt 0
        $verifiedByOwnTags = $false
        try {
            $tagJson = az resource show --ids $objectId --query tags --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $tagJson) {
                $tags = $tagJson | ConvertFrom-Json -AsHashtable
                $verifiedByOwnTags =
                    [string]$tags['purpose'] -eq [string]$expectedTags['purpose'] -and
                    [string]$tags['labId'] -eq [string]$expectedTags['labId'] -and
                    [string]$tags['runId'] -eq [string]$expectedTags['runId']
            } elseif ($verifiedByGroupBoundary) {
                $parentGroupObject = $resourceGroupObjects | Where-Object { $objectId.StartsWith("$($_.id)/", [System.StringComparison]::OrdinalIgnoreCase) } | Select-Object -First 1
                $exactCount = az resource list --resource-group $parentGroupObject.name --query "[?id=='$objectId'] | length(@)" --output tsv 2>$null
                if ($LASTEXITCODE -eq 0 -and [int]$exactCount -eq 0) {
                    $null = $absentIds.Add($objectId)
                    $verifiedByOwnTags = $true
                }
            }
        } catch {
            $verifiedByOwnTags = $false
        }
        $objectVerified = $manifestTagsMatch -and ($verifiedByOwnTags -or $verifiedByGroupBoundary)
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource' -and $object.type -eq 'Microsoft.Management/managementGroups') {
        try {
            $managementGroupJson = az account management-group show --name $object.name --expand --recurse --output json 2>&1
            if ($LASTEXITCODE -eq 0) {
                $managementGroup = $managementGroupJson | ConvertFrom-Json
                $objectVerified = [string]$managementGroup.id -eq $objectId -and @($managementGroup.children).Count -eq 0
            } elseif ([string]$managementGroupJson -match '(?i)404|not.?found') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'entra-object') {
        try {
            $graphResult = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$objectId" --output none 2>&1
            if ($LASTEXITCODE -eq 0) {
                $objectVerified = $true
            } elseif ([string]$graphResult -match '(?i)404|Request_ResourceNotFound') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'manifest-id' -and $object.kind -eq 'azure-resource') {
        try {
            $resourceResult = az resource show --ids $objectId --output none 2>&1
            if ($LASTEXITCODE -eq 0) {
                $objectVerified = $true
            } elseif ([string]$resourceResult -match '(?i)404|ResourceNotFound|could not be found') {
                $null = $absentIds.Add($objectId)
                $objectVerified = $true
            }
        } catch {
            $objectVerified = $false
        }
    } elseif ($method -eq 'local-path') {
        try {
            $candidate = if ([System.IO.Path]::IsPathRooted($objectId)) { $objectId } else { Join-Path $LabRoot $objectId }
            $fullPath = [System.IO.Path]::GetFullPath($candidate)
            $statePrefix = [System.IO.Path]::GetFullPath($StateDir).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
            $inStateBoundary = $fullPath.StartsWith($statePrefix, [System.StringComparison]::OrdinalIgnoreCase)
            $objectVerified = $inStateBoundary
            if ($inStateBoundary -and -not (Test-Path -LiteralPath $fullPath)) { $null = $absentIds.Add($objectId) }
        } catch {
            $objectVerified = $false
        }
    }

    $verifiedOwnershipById[$objectId] = $objectVerified
    if (-not $objectVerified) { $ownershipVerified = $false }
}
$PSNativeCommandUseErrorActionPreference = $nativeProbePreference

if (-not $ownershipVerified) {
    $failedOwnershipIds = @($active | Where-Object { -not $verifiedOwnershipById[[string]$_.id] } | ForEach-Object id)
    Write-CleanupRefusal -Message "Cleanup ownership refusal: live ID and ownership proof failed for $($failedOwnershipIds -join ', ')."
}

$actions = [System.Collections.Generic.List[object]]::new()
$residualChecks = [System.Collections.Generic.List[object]]::new()
if (-not $Execute) {
    Write-Host 'Preview only. The exact manifest-owned targets below will not be changed.'
}

# CHECKPOINT LAB26-CP05 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP05' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB26-CP05'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB26-CP05 END

# CHECKPOINT LAB26-CP04 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP04' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB26-CP04'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB26-CP04 END

# CHECKPOINT LAB26-CP03 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP03' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB26-CP03'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB26-CP03 END

# CHECKPOINT LAB26-CP02 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP02' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB26-CP02'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB26-CP02 END

# CHECKPOINT LAB26-CP01 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP01' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB26-CP01'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB26-CP01 END

$cleanupFailure = $null
if ($Execute) {
    $PSNativeCommandUseErrorActionPreference = $true
    $state.status = 'cleanup-in-progress'
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8

    try {
        # Restore shared or tenant-wide settings before removing the disposable
        # objects that were used to exercise them.
        foreach ($setting in @($state.originalSettings)) {
            if ($setting.targetId -eq 'authorizationPolicy' -and $setting.property -eq 'allowedToUseSSPR') {
                $restoreBody = @{ allowedToUseSSPR = [bool]$setting.value } | ConvertTo-Json -Compress
                az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --headers 'Content-Type=application/json' --body $restoreBody --output none
                $restored = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowedToUseSSPR' --query allowedToUseSSPR --output tsv
                if ([bool]::Parse([string]$restored) -ne [bool]$setting.value) {
                    throw 'Cleanup stopped because authorizationPolicy.allowedToUseSSPR was not restored.'
                }
            }
        }
        foreach ($object in @($active | Where-Object { $_.type -eq 'Microsoft.Management/managementGroups' -and -not $absentIds.Contains([string]$_.id) })) {
            az account management-group delete --name $object.name --output none
        }
        $hasLiveManagedTarget = @($active | Where-Object { -not $absentIds.Contains([string]$_.id) }).Count -gt 0
        if ($hasLiveManagedTarget) {

        }
        foreach ($groupToDelete in @($resourceGroupObjects | Where-Object { -not $absentIds.Contains([string]$_.id) })) {
            az group delete --ids $groupToDelete.id --yes
        }
        foreach ($object in @($active | Where-Object { $_.kind -eq 'entra-object' -and -not $absentIds.Contains([string]$_.id) })) {
            $collection = switch ([string]$object.type) {
                'Microsoft.Graph/user' { 'users' }
                'Microsoft.Graph/group' { 'groups' }
                default { 'directoryObjects' }
            }
            az rest --method delete --url "https://graph.microsoft.com/v1.0/$collection/$($object.id)" --output none 2>$null
        }
        foreach ($object in $state.managedObjects) {
            $object.lifecycleStatus = 'deleted'
        }
        foreach ($action in $actions) {
            if ($action.status -eq 'skipped') { continue }
            $action.status = 'deleted'
            $action.message = 'The exact manifest-recorded target was removed through its ownership boundary.'
        }
    } catch {
        $cleanupFailure = "Cleanup mutation failed: $($_.Exception.GetType().Name)"
        foreach ($action in $actions) {
            if ($action.status -eq 'preview') {
                $action.status = 'failed'
                $action.message = $cleanupFailure
            }
        }
    }
}

$PSNativeCommandUseErrorActionPreference = $false
$remaining = [System.Collections.Generic.List[string]]::new()
foreach ($object in $state.managedObjects) {
    if (-not $Execute -and $object.lifecycleStatus -eq 'active') { $remaining.Add([string]$object.id); continue }
    if ($Execute -and $object.type -eq 'Microsoft.Management/managementGroups') {
        $null = az account management-group show --name $object.name --output none 2>$null
        if ($LASTEXITCODE -eq 0) { $remaining.Add([string]$object.id) }
    } elseif ($Execute -and $object.type -eq 'Microsoft.Resources/resourceGroups') {
        $groupExists = az group exists --subscription $SubscriptionId --name $object.name --output tsv 2>$null
        if ($LASTEXITCODE -ne 0 -or $groupExists -ne 'false') { $remaining.Add([string]$object.id) }
    } elseif ($Execute -and $object.kind -eq 'azure-resource') {
        $null = az resource show --ids $object.id --output none 2>$null
        if ($LASTEXITCODE -eq 0) {
            $remaining.Add([string]$object.id)
        } elseif ($object.type -eq 'Microsoft.RecoveryServices/vaults' -and $false) {
            $deletedVault = az backup deleted-vault get --location $Location --name $object.name --output json 2>$null
            if ($LASTEXITCODE -eq 0 -and $deletedVault) {
                $object.lifecycleStatus = 'soft-deleted'
                foreach ($action in @($actions | Where-Object { [string]$_.targetId -eq [string]$object.id -and $_.status -ne 'skipped' })) {
                    $action.status = 'soft-deleted'
                    $action.message = 'The active ARM vault is absent and the exact recoverable deleted-vault record was confirmed; no purge was performed.'
                }
            } else {
                $remaining.Add([string]$object.id)
            }
        }
    } elseif ($Execute -and $object.kind -eq 'entra-object') {
        $null = az rest --method get --url "https://graph.microsoft.com/v1.0/directoryObjects/$($object.id)" --output none 2>$null
        if ($LASTEXITCODE -eq 0) { $remaining.Add([string]$object.id) }
    }
}
$residualChecks.Clear()
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP01' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp01.residual'; command = 'query manifest-recorded IDs for LAB26-CP01'; expected = 'zero active objects for LAB26-CP01'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP02' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp02.residual'; command = 'query manifest-recorded IDs for LAB26-CP02'; expected = 'zero active objects for LAB26-CP02'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP03' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp03.residual'; command = 'query manifest-recorded IDs for LAB26-CP03'; expected = 'zero active objects for LAB26-CP03'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP04' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp04.residual'; command = 'query manifest-recorded IDs for LAB26-CP04'; expected = 'zero active objects for LAB26-CP04'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB26-CP05' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp05.residual'; command = 'query manifest-recorded IDs for LAB26-CP05'; expected = 'zero active objects for LAB26-CP05'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
if ($Execute -and $remaining.Count -gt 0) {
    foreach ($object in $state.managedObjects) {
        if ([string]$object.id -in @($remaining)) { $object.lifecycleStatus = 'active' }
    }
    foreach ($action in $actions) {
        if ([string]$action.targetId -in @($remaining) -and $action.status -ne 'skipped') {
            $action.status = 'failed'
            $action.message = 'Residual query found the target still active after cleanup.'
        }
    }
}
$result = if (-not $Execute) { 'preview' } elseif ($cleanupFailure -or $remaining.Count -gt 0) { 'fail' } else { 'pass' }
$cleanup = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-26'
    runId = $RunId
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    executionMode = $(if ($Execute) { 'execute' } else { 'preview' })
    result = $result
    ownershipVerified = $ownershipVerified
    actions = @($actions)
    residualChecks = @($residualChecks)
    activeManagedObjects = @($remaining)
    retainedItems = @(

    )
}
$cleanup | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $CleanupPath -Encoding utf8
if ($Execute) {
    if ($result -eq 'pass') { $state.status = 'cleaned' }
    $state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
    $state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
}
Write-Host "Cleanup result: $result"
Write-Host "Artifact: $CleanupPath"
Write-Host 'Irreversible purge is never automated; retained or soft-deleted items must be documented explicitly.'
if ($result -eq 'fail') { exit 1 }
# END GENERATED AZ104 V2
```

[Previous: Lab 25](../25-site-recovery-failover/README.md) · [Catalog](../README.md) · [Next: Lab 27](../27-capstone-operate-recover/README.md)
<!-- END GENERATED AZ104 V2 -->
