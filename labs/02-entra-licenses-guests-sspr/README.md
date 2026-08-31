
<!-- BEGIN GENERATED AZ104 V2 -->
# Lab 02: Manage Entra licenses, guests, and self-service password reset

[Previous: Lab 01](../01-entra-users-groups/README.md) · [Catalog](../README.md) · [Next: Lab 03](../03-azure-rbac-scopes/README.md)

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: An identity administrator preparing a controlled external-collaboration and SSPR pilot is responding to an operational request: Build a reversible guest and licensing pilot, assess supported SSPR readiness, and preserve every tenant setting required for recovery.

Learner role: An identity administrator preparing a controlled external-collaboration and SSPR pilot.

Outcome: Build a reversible guest and licensing pilot, assess supported SSPR readiness, and preserve every tenant setting required for recovery.

| Item | Value |
|---|---|
| Duration | 105 minutes |
| Difficulty | foundational |
| Cost class | `none` |
| Command surface | Azure CLI (`az`, `az rest`, Bicep, AzCopy, or KQL where required) hosted in PowerShell |
| Live state | Not executed during this offline rebuild |

Completion criteria:

- All required checkpoints report pass.
- The deterministic break/fix is injected, diagnosed, and repaired.
- cleanup.json reports no active run-owned resources, with any retained item explicitly documented.

## Objectives and checkpoints

| Objective | Skill | Checkpoints |
|---|---|---|
| `IG-USERS-03` | Manage licenses in Microsoft Entra ID | `LAB02-CP01`, `LAB02-CP05` |
| `IG-USERS-04` | Manage external users | `LAB02-CP02`, `LAB02-CP03`, `LAB02-CP05` |
| `IG-USERS-05` | Configure self-service password reset (SSPR) | `LAB02-CP04`, `LAB02-CP05` |

The authoritative objective wording comes from the [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of 2026-04-17.

## Architecture and service topology

![Lab 02 service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). Microsoft Graph creates the pilot group and optional guest, links membership, and assigns an approved SKU. Authorization policy and registration reports are queried independently so administrator SSPR is never misrepresented as the unsupported selected-group scope.

## Concept primer and design decisions

Guest invitation, license assignment, and password-reset policy are separate control planes with different permissions and prerequisites. A user needs usageLocation before most license assignments. Microsoft Graph does not expose the Entra selected-group SSPR scope setting, so this lab never calls an undocumented endpoint. It builds the pilot group, queries supported registration reports, and gates a reversible administrator-SSPR authorizationPolicy exercise separately.

Design decisions:

- Invitation, license assignment, and the administrator SSPR policy change are independent optional gates.
- Validate SKU capacity and usageLocation before calling assignLicense.
- Persist the original allowedToUseSSPR value before PATCH and restore it before deleting pilot objects.

## Required and optional inputs

| Input | Required | Source | Safe example | Gate behavior |
|---|:---:|---|---|---|
| `run-id` — Unique lowercase run ownership identifier | Yes | parameter | `az104l02-01` | `block` |
| `subscription-id` — Expected disposable subscription ID | Yes | parameter-or-environment (`AZ104_SUBSCRIPTION_ID`) | `00000000-0000-0000-0000-000000000000` | `block` |
| `location` — Approved primary Azure region | Yes | parameter-or-environment (`AZ104_LOCATION`) | `westeurope` | `block` |
| `guest-email` — Disposable external invitation address | No | environment (`AZ104_GUEST_EMAIL`) | `learner@example.test` | `skip-checkpoint` |
| `license-sku-id` — Approved subscribed license SKU ID | No | environment (`AZ104_LICENSE_SKU_ID`) | `00000000-0000-0000-0000-000000000000` | `skip-checkpoint` |
| `usage-location` — Two-letter usage location required for the optional license assignment | No | environment (`AZ104_USAGE_LOCATION`) | `DE` | `skip-checkpoint` |
| `allow-sspr-policy-change` — Explicit YES gate for the authorized SSPR change | No | environment (`AZ104_ALLOW_SSPR_POLICY_CHANGE`) | `YES` | `skip-checkpoint` |

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l02-01' -Location 'westeurope'
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

## Task 1 — Inventory invitation policy, license capacity, and SSPR reporting access {#task-1}

Checkpoint: `LAB02-CP01`

Purpose and operational relevance: Read the three independent service surfaces before deciding which optional gates can execute. A tenant role that can invite guests might not be able to assign licenses, read reports, or update authorization policy.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
$skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,skuPartNumber,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json).value
$registrationAccess = $true
try { $null = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output none } catch { $registrationAccess = $false }
[pscustomobject]@{ invitePolicy = $policy.allowInvitesFrom; subscribedSkus = $skus.Count; registrationReportAccess = $registrationAccess }
```

Expected state: Invitation policy and subscribed SKUs are readable; registration-report access is explicitly true or recorded as an optional unavailable gate.

Representative redacted output:

```text
invitePolicy=adminsAndGuestInvitersAndAllMembers; subscribedSkus=3; registrationReportAccess=True
```

Positive validation:

```powershell
$skuResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,skuPartNumber,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json
if ($null -eq $skuResult.value) { throw 'subscribedSkus did not return a value collection.' }
$skuResult.value | Select-Object id,skuPartNumber,consumedUnits,prepaidUnits
```

Expected positive result: A value collection is returned; it may be empty in an unlicensed tenant but every item exposes capacity fields.

Negative validation:

```powershell
$policyResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
if ($policyResult.allowInvitesFrom -notin @('none','adminsAndGuestInviters','adminsGuestInvitersAndAllMembers','everyone')) { throw 'Invitation policy returned an unknown state.' }
$policyResult | Select-Object allowInvitesFrom,allowedToUseSSPR
```

Expected negative result: A known invitation-policy state is observed without changing it.

Evidence to retain:

- `LAB02-CP01` UTC result for inventory invitation policy, license capacity, and SSPR reporting access.
- Exact run-owned ID and asserted service properties from: A value collection is returned; it may be empty in an unlicensed tenant but every item exposes capacity fields.
- Negative-boundary outcome from: A known invitation-policy state is observed without changing it.
- Cleanup dependency recorded for the objects created or configured by LAB02-CP01.

Common failure and safe retry: The signed-in identity lacks directory, organization, or reports read permission for a selected gate. Treat unavailable optional permissions as skipped, obtain authorization outside the lab, and rerun only the affected read-only query.

Cleanup dependency: This checkpoint is read-only.

## Task 2 — Create and persist the required pilot group {#task-2}

Checkpoint: `LAB02-CP02`

Purpose and operational relevance: Create the security group independently of every optional gate and persist its concrete Graph collection and ID immediately. The group is the stable pilot boundary; an unavailable guest, license, or policy gate must not make its ownership ambiguous.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$group = az ad group create --display-name "AZ104-L02-$RunId-SSPR-Pilot" --mail-nickname "az104l02$suffix" --output json | ConvertFrom-Json
$external['groupId'] = [string]$group.id
Add-ManagedObject -CheckpointId 'LAB02-CP02' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
```

Expected state: Exactly one run-specific security group exists and its ID is manifest-recorded as Microsoft.Graph/group before any optional task.

Representative redacted output:

```text
pilotGroups=1; securityEnabled=True; manifestType=Microsoft.Graph/group
```

Positive validation:

```powershell
$groupResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?`$select=id,displayName,securityEnabled" --output json | ConvertFrom-Json
if ($groupResult.id -ne $external.groupId -or -not $groupResult.securityEnabled) { throw 'Pilot group does not match the manifest.' }
$groupResult
```

Expected positive result: The exact manifest-recorded group exists and is security-enabled.

Negative validation:

```powershell
$groupResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups?`$filter=startswith(displayName,'AZ104-L02-$RunId-')&`$select=id" --output json | ConvertFrom-Json
if (@($groupResult.value).Count -ne 1) { throw 'Expected exactly one run-specific pilot group.' }
$groupResult.value
```

Expected negative result: Exactly one run-specific pilot group exists; no retry-created duplicate is present.

Evidence to retain:

- `LAB02-CP02` UTC result for create and persist the required pilot group.
- Exact run-owned ID and asserted service properties from: The exact manifest-recorded group exists and is security-enabled.
- Negative-boundary outcome from: Exactly one run-specific pilot group exists; no retry-created duplicate is present.
- Cleanup dependency recorded for the objects created or configured by LAB02-CP02.

Common failure and safe retry: A prior partial run created the deterministic group but its ID was not reconciled before retry. Search by the run-specific display-name prefix, record the one exact ID, and never create a second pilot group.

Cleanup dependency: Delete the exact group after restoring tenant policy and removing any guest license; then verify its ID is not found.

## Task 3 — Invite and directly link the optional guest {#task-3}

Checkpoint: `LAB02-CP03`

Purpose and operational relevance: Invite one supplied address without sending mail, persist the returned concrete user ID immediately, and add that exact object to the pilot group. Invitation can succeed while a later relationship call fails, so cleanup and retry must not depend on an email lookup.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$inviteBody = @{ invitedUserEmailAddress = $env:AZ104_GUEST_EMAIL; inviteRedirectUrl = 'https://myapps.microsoft.com'; sendInvitationMessage = $false } | ConvertTo-Json -Compress
$invitation = az rest --method post --url 'https://graph.microsoft.com/v1.0/invitations' --body $inviteBody --output json | ConvertFrom-Json
$external['guestUserId'] = [string]$invitation.invitedUser.id
if (-not $external.guestUserId) { throw 'Invitation returned no guest user ID.' }
Add-ManagedObject -CheckpointId 'LAB02-CP03' -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'invited-guest' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
$state.inputs['guest-email'] = [string]$env:AZ104_GUEST_EMAIL
Save-RunState
$memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.guestUserId)" } | ConvertTo-Json -Compress
az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
```

Expected state: One manifest-recorded userType Guest exists and is a direct member of the exact pilot group.

Representative redacted output:

```text
guestGate=pass; userType=Guest; guestId=<redacted>; directMember=True
```

Positive validation:

```powershell
$guestResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?`$select=id,userType,mail" --output json | ConvertFrom-Json
$memberResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id" --output json | ConvertFrom-Json
if ($guestResult.userType -ne 'Guest' -or $guestResult.id -notin @($memberResult.value.id)) { throw 'Guest type or direct membership mismatch.' }
[pscustomobject]@{ guestId = $guestResult.id; userType = $guestResult.userType; directMember = $true }
```

Expected positive result: The exact recorded object is userType Guest and appears in the group's direct members collection.

Negative validation:

```powershell
$guestObjectId = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?%24select=id" --query id --output tsv
$guestRecords = @($state.managedObjects | Where-Object {
  $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active'
})
if ($guestObjectId -ne $external.guestUserId -or $guestRecords.Count -ne 1 -or $guestRecords[0].id -ne $external.guestUserId) {
  throw 'The live guest and manifest guest inventory do not identify one exact object.'
}
'Active live and manifest-recorded guest objects: 1'
```

Expected negative result: The manifest contains exactly one active concrete Graph user ID for the optional guest lane.

Evidence to retain:

- `LAB02-CP03` UTC result for invite and directly link the optional guest.
- Exact run-owned ID and asserted service properties from: The exact recorded object is userType Guest and appears in the group's direct members collection.
- Negative-boundary outcome from: The manifest contains exactly one active concrete Graph user ID for the optional guest lane.
- Cleanup dependency recorded for the objects created or configured by LAB02-CP03.

Common failure and safe retry: Invitation succeeds but membership fails, or the email already maps to an existing external object. Reconcile the returned or existing user ID into run.json, then retry only the missing membership reference.

Cleanup dependency: Remove any recorded license, then delete the exact manifest-recorded user after the pilot group.

## Task 4 — Inject a license denial, then set usage location and assign the approved SKU {#task-4}

Checkpoint: `LAB02-CP04`

Purpose and operational relevance: Prove an invalid SKU is denied without mutation, normalize the guest's two-letter usage location, validate exact capacity, and assign only the approved SKU. License calls fail without usageLocation and friendly-name matching can consume the wrong subscribed product.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
if ($env:AZ104_USAGE_LOCATION -notmatch '^[A-Za-z]{2}$') { throw 'AZ104_USAGE_LOCATION must be a two-letter ISO country code.' }
if (-not $external.guestUserId) { throw 'The guest checkpoint must complete before licensing.' }
$PSNativeCommandUseErrorActionPreference = $false
$denied = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body '{"addLicenses":[{"skuId":"00000000-0000-0000-0000-000000000000"}],"removeLicenses":[]}' --output none 2>&1
$deniedExit = $LASTEXITCODE
$PSNativeCommandUseErrorActionPreference = $true
if ($deniedExit -eq 0) { throw 'The invalid-SKU break/fix request unexpectedly succeeded.' }
$locationBody = @{ usageLocation = $env:AZ104_USAGE_LOCATION.ToUpperInvariant() } | ConvertTo-Json -Compress
az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)" --body $locationBody --output none
$state.inputs['usage-location'] = $env:AZ104_USAGE_LOCATION.ToUpperInvariant()
Save-RunState
$skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus' --output json | ConvertFrom-Json).value
$sku = @($skus | Where-Object id -eq $env:AZ104_LICENSE_SKU_ID)
if ($sku.Count -ne 1) { throw 'AZ104_LICENSE_SKU_ID is not a subscribed tenant SKU.' }
if (($sku[0].prepaidUnits.enabled - $sku[0].consumedUnits) -lt 1) { throw 'The selected SKU has no enabled unit available.' }
$licenseBody = @{ addLicenses = @(@{ skuId = $env:AZ104_LICENSE_SKU_ID }); removeLicenses = @() } | ConvertTo-Json -Depth 6 -Compress
$assignmentResult = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body $licenseBody --output json | ConvertFrom-Json
$state.inputs['license-sku-id'] = [string]$env:AZ104_LICENSE_SKU_ID
Save-RunState
if ($state.inputs['license-sku-id'] -notin @($assignmentResult.assignedLicenses.skuId)) { throw 'assignLicense did not return the approved SKU.' }
```

Expected state: The impossible SKU is denied, usageLocation is uppercase and persisted, and exactly the approved subscribed SKU is assigned.

Representative redacted output:

```text
invalidSkuDenied=True; usageLocation=DE; approvedSku=<redacted>; assigned=True
```

Positive validation:

```powershell
$licenseResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/licenseDetails?`$select=skuId,skuPartNumber" --output json | ConvertFrom-Json
if (@($licenseResult.value | Where-Object skuId -eq $state.inputs['license-sku-id']).Count -ne 1) { throw 'The approved SKU is not assigned exactly once.' }
$licenseResult.value
```

Expected positive result: licenseDetails contains the exact recorded SKU once.

Negative validation:

```powershell
$guestResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?`$select=usageLocation,assignedLicenses" --output json | ConvertFrom-Json
if ($guestResult.usageLocation -ne $state.inputs['usage-location']) { throw 'Guest usageLocation does not match the recorded value.' }
$unexpected = @($guestResult.assignedLicenses | Where-Object skuId -ne $state.inputs['license-sku-id'])
if ($unexpected.Count -ne 0) { throw 'An unapproved SKU is assigned to the lab-created guest.' }
[pscustomobject]@{ usageLocation = $guestResult.usageLocation; unexpectedSkus = $unexpected.Count }
```

Expected negative result: The guest has a usageLocation and no unapproved license SKU.

Evidence to retain:

- `LAB02-CP04` UTC result for inject a license denial, then set usage location and assign the approved SKU.
- Exact run-owned ID and asserted service properties from: licenseDetails contains the exact recorded SKU once.
- Negative-boundary outcome from: The guest has a usageLocation and no unapproved license SKU.
- Cleanup dependency recorded for the objects created or configured by LAB02-CP04.

Common failure and safe retry: Capacity changed after preflight, the location is not an ISO code, or the operator supplied a product name instead of the SKU GUID. Query the exact guest licenseDetails and subscribedSkus, then add only the missing approved SKU without removing unrelated tenant data.

Cleanup dependency: Remove only state.inputs license-sku-id from the exact guest before deleting the guest object.

## Task 5 — Record, exercise, and reconcile the supported administrator SSPR gate {#task-5}

Checkpoint: `LAB02-CP05`

Purpose and operational relevance: Persist allowedToUseSSPR before an exact-authorized PATCH, then reconcile policy, group, guest, license, and registration evidence without claiming selected-group SSPR configuration. Cleanup cannot restore a tenant policy from memory, and pilot-group membership is not evidence that a user is SSPR-capable.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -cne 'YES') { throw 'Administrator SSPR mutation requires the exact YES authorization value.' }
$policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
if (-not @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')) {
    $state.originalSettings += @{
        checkpointId = 'LAB02-CP05'; targetId = 'authorizationPolicy'; property = 'allowedToUseSSPR'
        value = [bool]$policy.allowedToUseSSPR; recordedAt = (Get-Date).ToUniversalTime().ToString('o')
    }
    Save-RunState
}
az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body '{"allowedToUseSSPR":true}' --output none
$members = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id,userType,usageLocation,assignedLicenses" --output json | ConvertFrom-Json
$baseline = @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')
if ($baseline.Count -ne 1) { throw 'Exactly one recoverable allowedToUseSSPR baseline is required.' }
$registrationAccess = $true
try { $registration = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output json | ConvertFrom-Json } catch { $registrationAccess = $false }
[pscustomobject]@{ memberCount = $members.value.Count; adminSspr = $true; recoverableBaselines = $baseline.Count; registrationReportAccess = $registrationAccess; selectedGroupScopeMutation = $false }
```

Expected state: The supported administrator property is true, exactly one prior Boolean is durable, and reconciliation explicitly reports that no selected-group scope endpoint was mutated.

Representative redacted output:

```text
adminSspr=True; recoverableBaselines=1; registrationReportAccess=True|False; selectedGroupScopeMutation=False
```

Positive validation:

```powershell
$ssprResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
$baseline = @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')
if (-not $ssprResult.allowedToUseSSPR -or $baseline.Count -ne 1) { throw 'Administrator SSPR or its recovery baseline is incomplete.' }
[pscustomobject]@{ allowedToUseSSPR = $ssprResult.allowedToUseSSPR; recoverableBaselines = $baseline.Count }
```

Expected positive result: allowedToUseSSPR is true and exactly one original Boolean remains available for cleanup.

Negative validation:

```powershell
$pilot = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?`$select=id,securityEnabled" --output json | ConvertFrom-Json
if ($pilot.id -ne $external.groupId -or -not $pilot.securityEnabled) { throw 'Pilot group no longer matches the manifest.' }
$guestObjects = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active' })
if ($guestObjects.Count -gt 1) { throw 'More than one guest object is owned by the run.' }
[pscustomobject]@{ selectedGroupScopeMutation = $false; activeGuestObjects = $guestObjects.Count }
```

Expected negative result: No unsupported selected-group mutation is claimed and at most the one intended guest is manifest-owned.

Evidence to retain:

- `LAB02-CP05` UTC result for record, exercise, and reconcile the supported administrator SSPR gate.
- Exact run-owned ID and asserted service properties from: allowedToUseSSPR is true and exactly one original Boolean remains available for cleanup.
- Negative-boundary outcome from: No unsupported selected-group mutation is claimed and at most the one intended guest is manifest-owned.
- Cleanup dependency recorded for the objects created or configured by LAB02-CP05.

Common failure and safe retry: Policy write permission is unavailable, registration reports require extra licensing, or a retry occurs without a durable original Boolean. Confirm originalSettings contains exactly one baseline before retrying; never PATCH when the prior setting cannot be recovered.

Cleanup dependency: Restore policy, remove the recorded SKU, delete the exact group, then delete the exact guest and query all IDs again.

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l02-01' -Mode Deployment
az resource list --resource-group 'rg-az104-l02-az104l02-01' --query '[].{name:name,type:type}' --output table
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: Supply a SKU ID that is not subscribed in the tenant.

Expected symptom: The license call fails without changing the guest's existing assignments.

Diagnose with a read-only service query:

```powershell
$policyResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
if ($policyResult.allowInvitesFrom -notin @('none','adminsAndGuestInviters','adminsGuestInvitersAndAllMembers','everyone')) { throw 'Invitation policy returned an unknown state.' }
$policyResult | Select-Object allowInvitesFrom,allowedToUseSSPR
```

Diagnosis: Compare the requested ID with subscribedSkus and available units.

Repair: Set the exact approved SKU ID, confirm usageLocation and capacity, then call assignLicense without removing existing assignments.

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

Produce a pilot matrix that separates invitation, redemption, usageLocation, license, group membership, registration capability, and administrator SSPR policy.

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
./scripts/cli/Cleanup.ps1 -RunId 'az104l02-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l02-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l02-01' -Mode PostCleanup
$pilot = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?`$select=id,securityEnabled" --output json | ConvertFrom-Json
if ($pilot.id -ne $external.groupId -or -not $pilot.securityEnabled) { throw 'Pilot group no longer matches the manifest.' }
$guestObjects = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active' })
if ($guestObjects.Count -gt 1) { throw 'More than one guest object is owned by the run.' }
[pscustomobject]@{ selectedGroupScopeMutation = $false; activeGuestObjects = $guestObjects.Count }
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

Complete [QUESTIONS.md](assessment/QUESTIONS.md), then use [ANSWERS.md](assessment/ANSWERS.md) for option-by-option remediation. Scores of 85–100% indicate mastery, 70–84% indicate targeted review, and below 70% means repeat the mapped tasks.

## Microsoft Learn sources

- [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Add or update a user's profile information in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info)
- [Microsoft Graph invitation API](https://learn.microsoft.com/en-us/graph/api/invitation-post)
- [Microsoft Graph assignLicense API](https://learn.microsoft.com/en-us/graph/api/user-assignlicense)
- [Microsoft Graph authorizationPolicy resource](https://learn.microsoft.com/en-us/graph/api/resources/authorizationpolicy)
- [Deploy Microsoft Entra self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-deploy)

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
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })

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

$providers = @()
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    Add-PreflightResult -Id "provider:$provider" -Required $true -Passed ($registrationState -eq 'Registered') -Actual $(if ($registrationState) { $registrationState } else { 'Unavailable' })
}

$knownLocation = az account list-locations --query "[?name=='$Location'].name | [0]" --output tsv
Add-PreflightResult -Id 'region' -Required $true -Passed ($knownLocation -eq $Location) -Actual $(if ($knownLocation) { $knownLocation } else { 'not available' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))
Add-PreflightResult -Id 'optional-gate:AZ104_GUEST_EMAIL' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID'))
Add-PreflightResult -Id 'optional-gate:AZ104_LICENSE_SKU_ID' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gatePresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION'))
Add-PreflightResult -Id 'optional-gate:AZ104_USAGE_LOCATION' -Required $false -Passed $gatePresent -Actual $(if ($gatePresent) { 'present (value redacted)' } else { 'absent; checkpoint will be skipped' })

$gateMatches = [string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE'), 'YES', [StringComparison]::Ordinal)
Add-PreflightResult -Id 'optional-gate:AZ104_ALLOW_SSPR_POLICY_CHANGE' -Required $false -Passed $gateMatches -Actual $(if ($gateMatches) { 'exact affirmative value supplied (value redacted)' } else { 'absent or not exact; checkpoint will be skipped' })

$guestEmail = [Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL')
$usageLocation = [Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION')
$licenseSkuId = [Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID')
$ssprAuthorization = [Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE')

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
$skus = az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json
if (-not $policy.id -or $null -eq $skus.value) { throw 'Required Graph policy or SKU inventory is unavailable.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.graph-surfaces' -Required $true -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($guestEmail) {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom' --output json | ConvertFrom-Json
    if ($policy.allowInvitesFrom -eq 'none') { throw 'Tenant invitation policy disables the requested guest lane.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.guest-gate' -Required $false -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($guestEmail -or $usageLocation -or $licenseSkuId) {
    if (-not $guestEmail -or -not $licenseSkuId -or $usageLocation -notmatch '^[A-Za-z]{2}$') { throw 'Guest email, exact SKU ID, and two-letter usage location must be supplied together for licensing.' }
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus' --output json | ConvertFrom-Json).value
    $selected = @($skus | Where-Object id -eq $licenseSkuId)
    if ($selected.Count -ne 1 -or ($selected[0].prepaidUnits.enabled - $selected[0].consumedUnits) -lt 1) { throw 'The exact license SKU is absent or has no enabled unit available.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.license-gate' -Required $false -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if ($ssprAuthorization -eq 'YES') {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
    if (-not $policy.id -or $null -eq $policy.allowedToUseSSPR) { throw 'allowedToUseSSPR cannot be read for recovery.' }
}
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab02.sspr-gate' -Required $false -Passed $probePassed -Actual $probeActual

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
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-02 execution plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  command surface: Azure CLI hosted in PowerShell'
Write-Host '  state: run.json, validation.json, cleanup.json'
if (-not $Execute) {
    Write-Host 'Preview only. Review context, inputs, cost, tenant scope, and cleanup before using -Execute.'
    return
}
if ($false -and -not $AcknowledgeCost) { throw 'This lab requires -AcknowledgeCost before execution.' }
if ($true -and -not $AcknowledgeTenantChange) { throw 'This lab requires -AcknowledgeTenantChange before execution.' }

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -RunId $RunId -Location $Location -SecondaryLocation $SecondaryLocation
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest. Choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$now = (Get-Date).ToUniversalTime().ToString('o')
$state = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-02'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB02-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP03'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP04'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB02-CP05'; required = $false; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '02'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB02-CP01' } else { $CheckpointId })
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

# CHECKPOINT LAB02-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP01'
    Save-RunState

    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,skuPartNumber,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json).value
    $registrationAccess = $true
    try { $null = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output none } catch { $registrationAccess = $false }
    [pscustomobject]@{ invitePolicy = $policy.allowInvitesFrom; subscribedSkus = $skus.Count; registrationReportAccess = $registrationAccess }

    Sync-ManagedResource -CheckpointId 'LAB02-CP01'
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'pass' -Message 'Invitation policy and subscribed SKUs are readable; registration-report access is explicitly true or recorded as an optional unavailable gate.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP01'
    Write-CheckpointState -CheckpointId 'LAB02-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB02-CP01 END

# CHECKPOINT LAB02-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP02'
    Save-RunState

    try {
        $group = az ad group create --display-name "AZ104-L02-$RunId-SSPR-Pilot" --mail-nickname "az104l02$suffix" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    }
    $external['groupId'] = [string]$group.id
    Save-ExternalState
    Add-ManagedObject -CheckpointId 'LAB02-CP02' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'

    Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'pass' -Message 'Exactly one run-specific security group exists and its ID is manifest-recorded as Microsoft.Graph/group before any optional task.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP02'
    Write-CheckpointState -CheckpointId 'LAB02-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB02-CP02 END

# CHECKPOINT LAB02-CP03 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP03'
    Save-RunState

    $inviteBody = @{ invitedUserEmailAddress = $env:AZ104_GUEST_EMAIL; inviteRedirectUrl = 'https://myapps.microsoft.com'; sendInvitationMessage = $false } | ConvertTo-Json -Compress
    try {
        $invitation = az rest --method post --url 'https://graph.microsoft.com/v1.0/invitations' --body $inviteBody --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    }
    $external['guestUserId'] = [string]$invitation.invitedUser.id
    Save-ExternalState
    if (-not $external.guestUserId) { throw 'Invitation returned no guest user ID.' }
    Add-ManagedObject -CheckpointId 'LAB02-CP03' -Kind 'entra-object' -Id ([string]$external.guestUserId) -Name 'invited-guest' -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    $state.inputs['guest-email'] = [string]$env:AZ104_GUEST_EMAIL
    Save-RunState
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.guestUserId)" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'pass' -Message 'One manifest-recorded userType Guest exists and is a direct member of the exact pilot group.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP03'
    Write-CheckpointState -CheckpointId 'LAB02-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP03 END

# CHECKPOINT LAB02-CP04 BEGIN
if (-not ((-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_GUEST_EMAIL'))) -and (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_LICENSE_SKU_ID'))) -and (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('AZ104_USAGE_LOCATION'))))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP04'
    Save-RunState

    if ($env:AZ104_USAGE_LOCATION -notmatch '^[A-Za-z]{2}$') { throw 'AZ104_USAGE_LOCATION must be a two-letter ISO country code.' }
    if (-not $external.guestUserId) { throw 'The guest checkpoint must complete before licensing.' }
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        $denied = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body '{"addLicenses":[{"skuId":"00000000-0000-0000-0000-000000000000"}],"removeLicenses":[]}' --output none 2>&1
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    }
    $deniedExit = $LASTEXITCODE
    $PSNativeCommandUseErrorActionPreference = $true
    if ($deniedExit -eq 0) { throw 'The invalid-SKU break/fix request unexpectedly succeeded.' }
    $locationBody = @{ usageLocation = $env:AZ104_USAGE_LOCATION.ToUpperInvariant() } | ConvertTo-Json -Compress
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)" --body $locationBody --output none
    $state.inputs['usage-location'] = $env:AZ104_USAGE_LOCATION.ToUpperInvariant()
    Save-RunState
    $skus = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus' --output json | ConvertFrom-Json).value
    $sku = @($skus | Where-Object id -eq $env:AZ104_LICENSE_SKU_ID)
    if ($sku.Count -ne 1) { throw 'AZ104_LICENSE_SKU_ID is not a subscribed tenant SKU.' }
    if (($sku[0].prepaidUnits.enabled - $sku[0].consumedUnits) -lt 1) { throw 'The selected SKU has no enabled unit available.' }
    $licenseBody = @{ addLicenses = @(@{ skuId = $env:AZ104_LICENSE_SKU_ID }); removeLicenses = @() } | ConvertTo-Json -Depth 6 -Compress
    try {
        $assignmentResult = az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/assignLicense" --body $licenseBody --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    }
    $state.inputs['license-sku-id'] = [string]$env:AZ104_LICENSE_SKU_ID
    Save-RunState
    if ($state.inputs['license-sku-id'] -notin @($assignmentResult.assignedLicenses.skuId)) { throw 'assignLicense did not return the approved SKU.' }

    Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'pass' -Message 'The impossible SKU is denied, usageLocation is uppercase and persisted, and exactly the approved subscribed SKU is assigned.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP04'
    Write-CheckpointState -CheckpointId 'LAB02-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP04 END

# CHECKPOINT LAB02-CP05 BEGIN
if (-not ([string]::Equals([Environment]::GetEnvironmentVariable('AZ104_ALLOW_SSPR_POLICY_CHANGE'), 'YES', [StringComparison]::Ordinal))) {
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'skipped' -Message 'Optional input or exact authorization gate was not satisfied.'
    Save-RunState
} else {
try {
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB02-CP05'
    Save-RunState

    if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -cne 'YES') { throw 'Administrator SSPR mutation requires the exact YES authorization value.' }
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
    if (-not @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')) {
        $state.originalSettings += @{
            checkpointId = 'LAB02-CP05'; targetId = 'authorizationPolicy'; property = 'allowedToUseSSPR'
            value = [bool]$policy.allowedToUseSSPR; recordedAt = (Get-Date).ToUniversalTime().ToString('o')
        }
        Save-RunState
    }
    az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body '{"allowedToUseSSPR":true}' --output none
    $members = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id,userType,usageLocation,assignedLicenses" --output json | ConvertFrom-Json
    $baseline = @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')
    if ($baseline.Count -ne 1) { throw 'Exactly one recoverable allowedToUseSSPR baseline is required.' }
    $registrationAccess = $true
    try { $registration = az rest --method get --url 'https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails?$top=1' --output json | ConvertFrom-Json } catch { $registrationAccess = $false }
    [pscustomobject]@{ memberCount = $members.value.Count; adminSspr = $true; recoverableBaselines = $baseline.Count; registrationReportAccess = $registrationAccess; selectedGroupScopeMutation = $false }

    Sync-ManagedResource -CheckpointId 'LAB02-CP05'
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'pass' -Message 'The supported administrator property is true, exactly one prior Boolean is durable, and reconciliation explicitly reports that no selected-group scope endpoint was mutated.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB02-CP05'
    Write-CheckpointState -CheckpointId 'LAB02-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
}
# CHECKPOINT LAB02-CP05 END

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
if ($state.labId -ne 'LAB-02' -or $state.runId -ne $RunId) { throw 'Manifest ownership does not match this lab and run ID.' }
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) { $accountJson | ConvertFrom-Json } else { $null })
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) { "tenant=$($account.tenantId); subscription=$($account.id)" } else { 'active context unavailable' })
    $contextFailure = @{
        schemaVersion = '1.0.0'; labId = 'LAB-02'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{ required = 1; passed = 0; failed = 1; skipped = 0 }
        checks = @(@{ id = 'context.active'; checkpointId = 'LAB02-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true } })
    }
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$external = @{}
$groupRecord = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/group' } | Select-Object -First 1)
$guestRecord = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' } | Select-Object -First 1)
$external['groupId'] = $(if ($groupRecord.Count -eq 1) { [string]$groupRecord[0].id } else { '' })
$external['guestUserId'] = $(if ($guestRecord.Count -eq 1) { [string]$guestRecord[0].id } else { '' })

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

# CHECKPOINT LAB02-CP01 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB02-CP01' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP01' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab02-cp01.positive' -CheckpointId 'LAB02-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab02-cp01.negative' -CheckpointId 'LAB02-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$skuResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/subscribedSkus?$select=id,skuPartNumber,consumedUnits,prepaidUnits' --output json | ConvertFrom-Json
if ($null -eq $skuResult.value) { throw 'subscribedSkus did not return a value collection.' }
$skuResult.value | Select-Object id,skuPartNumber,consumedUnits,prepaidUnits
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
    Add-ValidationCheck -Id 'lab02-cp01.positive' -CheckpointId 'LAB02-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$policyResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=allowInvitesFrom,allowedToUseSSPR' --output json | ConvertFrom-Json
if ($policyResult.allowInvitesFrom -notin @('none','adminsAndGuestInviters','adminsGuestInvitersAndAllMembers','everyone')) { throw 'Invitation policy returned an unknown state.' }
$policyResult | Select-Object allowInvitesFrom,allowedToUseSSPR
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
    Add-ValidationCheck -Id 'lab02-cp01.negative' -CheckpointId 'LAB02-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab02-cp01.residual' -CheckpointId 'LAB02-CP01' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB02-CP01 END

# CHECKPOINT LAB02-CP02 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB02-CP02' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP02' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab02-cp02.positive' -CheckpointId 'LAB02-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab02-cp02.negative' -CheckpointId 'LAB02-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$groupResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?`$select=id,displayName,securityEnabled" --output json | ConvertFrom-Json
if ($groupResult.id -ne $external.groupId -or -not $groupResult.securityEnabled) { throw 'Pilot group does not match the manifest.' }
$groupResult
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
    Add-ValidationCheck -Id 'lab02-cp02.positive' -CheckpointId 'LAB02-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$groupResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups?`$filter=startswith(displayName,'AZ104-L02-$RunId-')&`$select=id" --output json | ConvertFrom-Json
if (@($groupResult.value).Count -ne 1) { throw 'Expected exactly one run-specific pilot group.' }
$groupResult.value
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
    Add-ValidationCheck -Id 'lab02-cp02.negative' -CheckpointId 'LAB02-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab02-cp02.residual' -CheckpointId 'LAB02-CP02' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB02-CP02 END

# CHECKPOINT LAB02-CP03 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB02-CP03' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP03' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab02-cp03.positive' -CheckpointId 'LAB02-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab02-cp03.negative' -CheckpointId 'LAB02-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$guestResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?`$select=id,userType,mail" --output json | ConvertFrom-Json
$memberResult = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id" --output json | ConvertFrom-Json
if ($guestResult.userType -ne 'Guest' -or $guestResult.id -notin @($memberResult.value.id)) { throw 'Guest type or direct membership mismatch.' }
[pscustomobject]@{ guestId = $guestResult.id; userType = $guestResult.userType; directMember = $true }
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
    Add-ValidationCheck -Id 'lab02-cp03.positive' -CheckpointId 'LAB02-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$guestObjectId = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?%24select=id" --query id --output tsv
$guestRecords = @($state.managedObjects | Where-Object {
  $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active'
})
if ($guestObjectId -ne $external.guestUserId -or $guestRecords.Count -ne 1 -or $guestRecords[0].id -ne $external.guestUserId) {
  throw 'The live guest and manifest guest inventory do not identify one exact object.'
}
'Active live and manifest-recorded guest objects: 1'
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
    Add-ValidationCheck -Id 'lab02-cp03.negative' -CheckpointId 'LAB02-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab02-cp03.residual' -CheckpointId 'LAB02-CP03' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB02-CP03 END

# CHECKPOINT LAB02-CP04 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB02-CP04' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP04' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab02-cp04.positive' -CheckpointId 'LAB02-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab02-cp04.negative' -CheckpointId 'LAB02-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$licenseResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)/licenseDetails?`$select=skuId,skuPartNumber" --output json | ConvertFrom-Json
if (@($licenseResult.value | Where-Object skuId -eq $state.inputs['license-sku-id']).Count -ne 1) { throw 'The approved SKU is not assigned exactly once.' }
$licenseResult.value
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
    Add-ValidationCheck -Id 'lab02-cp04.positive' -CheckpointId 'LAB02-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$guestResult = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.guestUserId)?`$select=usageLocation,assignedLicenses" --output json | ConvertFrom-Json
if ($guestResult.usageLocation -ne $state.inputs['usage-location']) { throw 'Guest usageLocation does not match the recorded value.' }
$unexpected = @($guestResult.assignedLicenses | Where-Object skuId -ne $state.inputs['license-sku-id'])
if ($unexpected.Count -ne 0) { throw 'An unapproved SKU is assigned to the lab-created guest.' }
[pscustomobject]@{ usageLocation = $guestResult.usageLocation; unexpectedSkus = $unexpected.Count }
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
    Add-ValidationCheck -Id 'lab02-cp04.negative' -CheckpointId 'LAB02-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab02-cp04.residual' -CheckpointId 'LAB02-CP04' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB02-CP04 END

# CHECKPOINT LAB02-CP05 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB02-CP05' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP05' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab02-cp05.positive' -CheckpointId 'LAB02-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab02-cp05.negative' -CheckpointId 'LAB02-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$ssprResult = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy?$select=id,allowedToUseSSPR' --output json | ConvertFrom-Json
$baseline = @($state.originalSettings | Where-Object property -eq 'allowedToUseSSPR')
if (-not $ssprResult.allowedToUseSSPR -or $baseline.Count -ne 1) { throw 'Administrator SSPR or its recovery baseline is incomplete.' }
[pscustomobject]@{ allowedToUseSSPR = $ssprResult.allowedToUseSSPR; recoverableBaselines = $baseline.Count }
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
    Add-ValidationCheck -Id 'lab02-cp05.positive' -CheckpointId 'LAB02-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$pilot = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?`$select=id,securityEnabled" --output json | ConvertFrom-Json
if ($pilot.id -ne $external.groupId -or -not $pilot.securityEnabled) { throw 'Pilot group no longer matches the manifest.' }
$guestObjects = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active' })
if ($guestObjects.Count -gt 1) { throw 'More than one guest object is owned by the run.' }
[pscustomobject]@{ selectedGroupScopeMutation = $false; activeGuestObjects = $guestObjects.Count }
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
    Add-ValidationCheck -Id 'lab02-cp05.negative' -CheckpointId 'LAB02-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab02-cp05.residual' -CheckpointId 'LAB02-CP05' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB02-CP05 END

$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-02'
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
        schemaVersion = '1.0.0'; labId = 'LAB-02'; runId = $RunId
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
if ($state.labId -ne 'LAB-02' -or $state.runId -ne $RunId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {
        try { $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) } catch { $priorRetained = @() }
    }
    $idempotent = @{
        schemaVersion = '1.0.0'; labId = 'LAB-02'; runId = $RunId
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
$ResourceGroupName = $(if ('02' -in @('00', '01', '02')) { $null } else { "rg-az104-l02-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$guestRecord = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active' } | Select-Object -First 1)
$guestUserId = $(if ($guestRecord.Count -eq 1) { [string]$guestRecord[0].id } else { '' })
$licenseSkuId = [string]$state.inputs['license-sku-id']

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
                [string]$tags['labId'] -eq '02' -and
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
            [string]$expectedTags['labId'] -eq '02' -and
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

# CHECKPOINT LAB02-CP05 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP05' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB02-CP05'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB02-CP05 END

# CHECKPOINT LAB02-CP04 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP04' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB02-CP04'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB02-CP04 END

# CHECKPOINT LAB02-CP03 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP03' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB02-CP03'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB02-CP03 END

# CHECKPOINT LAB02-CP02 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP02' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB02-CP02'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB02-CP02 END

# CHECKPOINT LAB02-CP01 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP01' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB02-CP01'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB02-CP01 END

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
if ($guestUserId -and $licenseSkuId) {
    $removeBody = @{ addLicenses = @(); removeLicenses = @($licenseSkuId) } | ConvertTo-Json -Depth 5 -Compress
    az rest --method post --url "https://graph.microsoft.com/v1.0/users/$guestUserId/assignLicense" --body $removeBody --output none
    $remainingLicenses = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$guestUserId?%24select=assignedLicenses" --output json | ConvertFrom-Json
    if ($licenseSkuId -in @($remainingLicenses.assignedLicenses.skuId)) { throw 'Cleanup stopped because the recorded guest license was not removed.' }
}
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
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP01' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp01.residual'; command = 'query manifest-recorded IDs for LAB02-CP01'; expected = 'zero active objects for LAB02-CP01'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP02' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp02.residual'; command = 'query manifest-recorded IDs for LAB02-CP02'; expected = 'zero active objects for LAB02-CP02'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP03' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp03.residual'; command = 'query manifest-recorded IDs for LAB02-CP03'; expected = 'zero active objects for LAB02-CP03'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP04' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp04.residual'; command = 'query manifest-recorded IDs for LAB02-CP04'; expected = 'zero active objects for LAB02-CP04'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB02-CP05' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp05.residual'; command = 'query manifest-recorded IDs for LAB02-CP05'; expected = 'zero active objects for LAB02-CP05'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
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
    labId = 'LAB-02'
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

[Previous: Lab 01](../01-entra-users-groups/README.md) · [Catalog](../README.md) · [Next: Lab 03](../03-azure-rbac-scopes/README.md)
<!-- END GENERATED AZ104 V2 -->
