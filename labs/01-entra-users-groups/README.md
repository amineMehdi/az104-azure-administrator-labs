
<!-- BEGIN GENERATED AZ104 V2 -->
# Lab 01: Create and manage Microsoft Entra users and groups

[Previous: Lab 00](../00-safe-bootstrap/README.md) · [Catalog](../README.md) · [Next: Lab 02](../02-entra-licenses-guests-sspr/README.md)

This self-contained lab uses Azure CLI commands hosted in PowerShell. Complete the guided lane or the automated lane—not both with the same run ID.

## Scenario, role, and outcome

Scenario: An identity administrator onboarding a small operations team is responding to an operational request: Create, operate, validate, and retire two cloud-only users and their member and owner relationships by using Microsoft Graph through Azure CLI.

Learner role: An identity administrator onboarding a small operations team.

Outcome: Create, operate, validate, and retire two cloud-only users and their member and owner relationships by using Microsoft Graph through Azure CLI.

| Item | Value |
|---|---|
| Duration | 75 minutes |
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
| `IG-USERS-01` | Create users and groups | `LAB01-CP01`, `LAB01-CP03`, `LAB01-CP05` |
| `IG-USERS-02` | Manage user and group properties | `LAB01-CP02`, `LAB01-CP04`, `LAB01-CP05` |

The authoritative objective wording comes from the [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of 2026-04-17.

## Architecture and service topology

![Lab 01 service topology](diagrams/architecture.svg)

The editable source is [architecture.mmd](diagrams/architecture.mmd). The administrator calls Microsoft Graph through az rest. Two cloud-only users connect to one security group through separate member and owner references. The local run manifest is the authoritative cleanup boundary.

## Concept primer and design decisions

Microsoft Entra users are security principals, while groups provide a maintainable authorization boundary. Object IDs are immutable references; display names and user principal names can change. A recoverable identity workflow records each returned ID before starting the next mutation, because a partial failure can otherwise leave an unknown tenant object.

Design decisions:

- Use disposable cloud-only identities for practice.
- Persist every returned user and group ID immediately in run.json before adding relationships.
- Make one user a member and the other an owner so learners can prove that the relationships are independent.

## Required and optional inputs

| Input | Required | Source | Safe example | Gate behavior |
|---|:---:|---|---|---|
| `run-id` — Unique lowercase run ownership identifier | Yes | parameter | `az104l01-01` | `block` |
| `subscription-id` — Expected disposable subscription ID | Yes | parameter-or-environment (`AZ104_SUBSCRIPTION_ID`) | `00000000-0000-0000-0000-000000000000` | `block` |
| `location` — Approved primary Azure region | Yes | parameter-or-environment (`AZ104_LOCATION`) | `westeurope` | `block` |
| `tenant-domain` — Verified disposable tenant domain | Yes | environment (`AZ104_TENANT_DOMAIN`) | `contoso-lab.onmicrosoft.com` | `block` |
| `initial-password` — Temporary policy-compliant initial password | Yes | environment (`AZ104_LAB_INITIAL_PASSWORD`) | `&lt;secret&gt;` | `block` |

Secrets stay in temporary environment variables and are never written to `run.json`, validation evidence, or Git. A `skip-checkpoint` gate produces a visible partial result; it never becomes a pass.

## Read-only preflight

Sign in deliberately, inspect the active context, then run the lab preflight. It never signs in, changes context, installs an extension, registers a provider, or creates a resource.

```powershell
az login
az account show --query '{cloud:environmentName,subscription:id,tenant:tenantId,user:user.name}' --output json
./scripts/cli/Preflight.ps1 -SubscriptionId $env:AZ104_SUBSCRIPTION_ID -RunId 'az104l01-01' -Location 'westeurope'
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

## Task 1 — Prove Graph access and validate the verified UPN domain {#task-1}

Checkpoint: `LAB01-CP01`

Purpose and operational relevance: Confirm the active tenant, enumerate only verified domains, and stop if the supplied domain cannot host a cloud-only user. A valid subscription context does not prove Microsoft Graph permissions or a usable UPN suffix.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$tenant = az account show --query tenantId --output tsv
$domains = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/domains?$select=id,isVerified,isDefault' --output json | ConvertFrom-Json).value
$domain = @($domains | Where-Object { $_.id -eq $env:AZ104_TENANT_DOMAIN -and $_.isVerified })
if ($domain.Count -ne 1) { throw 'AZ104_TENANT_DOMAIN must name one verified domain in the active tenant.' }
[pscustomobject]@{ tenant = '<redacted>'; domain = $domain[0].id; verified = $domain[0].isVerified }
```

Expected state: The supplied domain appears exactly once with isVerified true, and the Graph request succeeds in the active tenant.

Representative redacted output:

```text
tenant=<redacted>; domain=contoso-lab.onmicrosoft.com; verified=True
```

Positive validation:

```powershell
$domain = az rest --method get --url "https://graph.microsoft.com/v1.0/domains/$($env:AZ104_TENANT_DOMAIN)?%24select=id,isVerified" --output json | ConvertFrom-Json
if ($domain.id -ne $env:AZ104_TENANT_DOMAIN -or -not $domain.isVerified) { throw 'Selected UPN domain is not verified.' }
$domain
```

Expected positive result: The selected domain exists and is verified.

Negative validation:

```powershell
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id" --output json | ConvertFrom-Json).value
$unexpected = @($users | Where-Object id -notin $external.userIds)
if ($users.Count -ne 2 -or $unexpected.Count -ne 0) { throw 'Run-specific user inventory contains a missing or unowned object.' }
'Run-specific users=2; unowned users=0'
```

Expected negative result: During deployment, exactly the two manifest IDs exist and no third run-specific user is present.

Evidence to retain:

- `LAB01-CP01` UTC result for prove Graph access and validate the verified UPN domain.
- Exact run-owned ID and asserted service properties from: The selected domain exists and is verified.
- Negative-boundary outcome from: During deployment, exactly the two manifest IDs exist and no third run-specific user is present.
- Cleanup dependency recorded for the objects created or configured by LAB01-CP01.

Common failure and safe retry: Graph returns Authorization_RequestDenied, or the domain is unverified or belongs to another tenant. Correct the active tenant or delegated Graph permission, then rerun this read-only checkpoint without changing context in the script.

Cleanup dependency: This checkpoint is read-only and has no Azure cleanup dependency.

## Task 2 — Create two cloud-only users and persist each ID immediately {#task-2}

Checkpoint: `LAB01-CP02`

Purpose and operational relevance: Create Alex and Blair one at a time, recording each immutable object ID before attempting the next user. Immediate persistence lets cleanup recover the first user if creation of the second user fails.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
if ($env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) { throw 'The temporary password must contain at least 12 characters.' }
$domain = $env:AZ104_TENANT_DOMAIN
$userIds = @()
$users = @(
    @{ alias = "az104l01a$suffix"; displayName = "AZ104-L01-$RunId-Alex"; department = 'Operations' },
    @{ alias = "az104l01b$suffix"; displayName = "AZ104-L01-$RunId-Blair"; department = 'Operations' }
)
foreach ($user in $users) {
    $bodyPath = Join-Path $StateDir ".user-$($user.alias).json"
    $body = @{
        accountEnabled = $true
        displayName = $user.displayName
        mailNickname = $user.alias
        userPrincipalName = "$($user.alias)@$domain"
        department = $user.department
        passwordProfile = @{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
    }
    try {
        $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $bodyPath -Encoding utf8
        $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$bodyPath" --output json | ConvertFrom-Json
    } finally {
        Remove-Item -LiteralPath $bodyPath -Force -ErrorAction SilentlyContinue
    }
    $userIds += [string]$created.id
    $external['userIds'] = @($userIds)
    Add-ManagedObject -CheckpointId 'LAB01-CP02' -Kind 'entra-object' -Id ([string]$created.id) -Name $user.displayName -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
}
Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue
```

Expected state: Two enabled cloud-only users exist with unique UPNs, Operations department, and IDs already present in run.json.

Representative redacted output:

```text
createdUsers=2; enabled=2; manifestIds=2 (IDs and UPNs redacted)
```

Positive validation:

```powershell
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id,displayName,accountEnabled,department" --output json | ConvertFrom-Json).value
if ($users.Count -ne 2 -or @($users | Where-Object { -not $_.accountEnabled -or $_.department -ne 'Operations' }).Count -ne 0) { throw 'Created-user state mismatch.' }
$users
```

Expected positive result: Exactly two run-specific users are enabled and assigned to Operations.

Negative validation:

```powershell
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id,userType" --output json | ConvertFrom-Json).value
if ($users.Count -ne 2 -or @($users | Where-Object userType -ne 'Member').Count -ne 0) { throw 'Expected exactly two member users.' }
$users
```

Expected negative result: The inventory contains no third run-specific user and each created object has userType Member.

Evidence to retain:

- `LAB01-CP02` UTC result for create two cloud-only users and persist each ID immediately.
- Exact run-owned ID and asserted service properties from: Exactly two run-specific users are enabled and assigned to Operations.
- Negative-boundary outcome from: The inventory contains no third run-specific user and each created object has userType Member.
- Cleanup dependency recorded for the objects created or configured by LAB01-CP02.

Common failure and safe retry: The UPN already exists, the password violates tenant policy, or User.ReadWrite.All is unavailable. Query by the deterministic UPNs first; never create replacements until run.json and the tenant inventory agree.

Cleanup dependency: Remove group owner and member references before deleting either user.

## Task 3 — Create the security group and add Alex as a member {#task-3}

Checkpoint: `LAB01-CP03`

Purpose and operational relevance: Establish a reusable authorization boundary and add only the first recorded user through an object-ID reference. Group membership should be proven by immutable IDs rather than display-name matching.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$groupBodyPath = Join-Path $StateDir '.group.json'
@{ displayName = "AZ104-L01-$RunId-Operators"; mailEnabled = $false; mailNickname = "az104l01g$suffix"; securityEnabled = $true } |
    ConvertTo-Json | Set-Content -LiteralPath $groupBodyPath -Encoding utf8
try {
    $group = az rest --method post --url 'https://graph.microsoft.com/v1.0/groups' --body "@$groupBodyPath" --output json | ConvertFrom-Json
} finally {
    Remove-Item -LiteralPath $groupBodyPath -Force -ErrorAction SilentlyContinue
}
$external['groupId'] = [string]$group.id
Add-ManagedObject -CheckpointId 'LAB01-CP03' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
$memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
```

Expected state: One security-enabled group exists and its direct members collection contains Alex but not Blair.

Representative redacted output:

```text
group.securityEnabled=True; directMembers=1; Alex=True; Blair=False
```

Positive validation:

```powershell
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id,displayName" --output json | ConvertFrom-Json).value
if ($members.Count -ne 1 -or $members[0].id -ne $external.userIds[0]) { throw 'Alex is not the sole direct member.' }
$members
```

Expected positive result: The member list contains only Alex's recorded object ID.

Negative validation:

```powershell
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($external.userIds[1] -in @($members.id)) { throw 'Blair received unintended membership.' }
'Blair direct membership=False'
```

Expected negative result: Blair's owner candidate ID is absent from direct membership.

Evidence to retain:

- `LAB01-CP03` UTC result for create the security group and add Alex as a member.
- Exact run-owned ID and asserted service properties from: The member list contains only Alex's recorded object ID.
- Negative-boundary outcome from: Blair's owner candidate ID is absent from direct membership.
- Cleanup dependency recorded for the objects created or configured by LAB01-CP03.

Common failure and safe retry: Group propagation is incomplete or the member reference uses a UPN instead of the recorded object ID. Query the group and direct members by ID; repeat the idempotent relationship call only when the member is absent.

Cleanup dependency: Delete the group before deleting its member and owner users.

## Task 4 — Assign Blair as owner without making Blair a member {#task-4}

Checkpoint: `LAB01-CP04`

Purpose and operational relevance: Add the second user to the owners reference and prove that ownership does not imply membership. Owners administer group composition; members receive group-based access, so conflating them creates excess access.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
$ownerBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" } | ConvertTo-Json -Compress
az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners/`$ref" --body $ownerBody --output none
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id" --output json | ConvertFrom-Json).value.id
if ($external.userIds[1] -in $members) { throw 'Blair must be an owner only for this checkpoint.' }
```

Expected state: Blair is the sole explicit owner, Alex is the sole member, and the two object-ID sets do not overlap.

Representative redacted output:

```text
owners=1; members=1; overlap=0
```

Positive validation:

```powershell
$owners = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners?%24select=id,displayName" --output json | ConvertFrom-Json).value
if ($owners.Count -ne 1 -or $owners[0].id -ne $external.userIds[1]) { throw 'Blair is not the sole explicit owner.' }
$owners
```

Expected positive result: The owners collection contains Blair's recorded object ID.

Negative validation:

```powershell
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($external.userIds[1] -in @($members.id)) { throw 'Ownership leaked into membership.' }
'Owner/member overlap=0'
```

Expected negative result: Blair's owner ID is absent from the direct members collection.

Evidence to retain:

- `LAB01-CP04` UTC result for assign Blair as owner without making Blair a member.
- Exact run-owned ID and asserted service properties from: The owners collection contains Blair's recorded object ID.
- Negative-boundary outcome from: Blair's owner ID is absent from the direct members collection.
- Cleanup dependency recorded for the objects created or configured by LAB01-CP04.

Common failure and safe retry: The owner call uses a directoryObjects URL unsupported for this relationship or Blair was also added as a member. Compare direct owner and member ID sets, remove only the unintended relationship, and rerun the exact-ID query.

Cleanup dependency: Remove or delete the group before deleting Blair.

## Task 5 — Operate the user lifecycle and reconcile the final identity inventory {#task-5}

Checkpoint: `LAB01-CP05`

Purpose and operational relevance: Update Alex's job title, disable and re-enable Blair, then reconcile users, membership, ownership, and run.json by immutable ID. Day-two identity administration includes property and sign-in-state changes, not only object creation.

Run these commands from PowerShell. If you already used the automated lane, choose a new run ID before trying this guided lane.

```powershell
az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[0])" --body '{"jobTitle":"Cloud Operations Analyst"}' --output none
az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":false}' --output none
$disabled = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])?`$select=accountEnabled" --query accountEnabled --output tsv
if ($disabled -ne 'false') { throw 'The disabled-state validation did not converge.' }
az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":true}' --output none
az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/$($external.userIds[0])/%24ref" --output none
$faultMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($external.userIds[0] -in @($faultMembers.id)) { throw 'The missing-membership fault was not established.' }
$memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/%24ref" --body $memberBody --output none
$repairedMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($repairedMembers.Count -ne 1 -or $repairedMembers[0].id -ne $external.userIds[0]) { throw 'Alex membership repair failed.' }
```

Expected state: Alex has the new job title, Blair is enabled again, and the final relationship inventory still has one distinct member and owner.

Representative redacted output:

```text
Alex.jobTitle=Cloud Operations Analyst; Blair.accountEnabled=True; memberOwnerOverlap=0
```

Positive validation:

```powershell
$alex = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[0])?%24select=id,jobTitle,department,accountEnabled" --output json | ConvertFrom-Json
if ($alex.id -ne $external.userIds[0] -or $alex.jobTitle -ne 'Cloud Operations Analyst' -or $alex.department -ne 'Operations' -or -not $alex.accountEnabled) { throw 'Alex lifecycle state mismatch.' }
$alex
```

Expected positive result: Alex is enabled with the expected job title and department.

Negative validation:

```powershell
$group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?%24select=id,deletedDateTime" --output json | ConvertFrom-Json
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
$owners = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners?%24select=id" --output json | ConvertFrom-Json).value
if ($group.id -ne $external.groupId -or $group.deletedDateTime) { throw 'Group is missing or deleted.' }
if ($members.Count -ne 1 -or $members[0].id -ne $external.userIds[0] -or $owners.Count -ne 1 -or $owners[0].id -ne $external.userIds[1]) { throw 'Final member/owner reconciliation failed.' }
if (@($state.managedObjects | Where-Object { $_.type -in @('Microsoft.Graph/user','Microsoft.Graph/group') -and $_.lifecycleStatus -eq 'active' }).Count -ne 3) { throw 'Manifest identity inventory is incomplete.' }
'Final users=2; groups=1; members=1; owners=1'
```

Expected negative result: The group is active, has no deletedDateTime, and every run-owned ID is represented once in run.json.

Evidence to retain:

- `LAB01-CP05` UTC result for operate the user lifecycle and reconcile the final identity inventory.
- Exact run-owned ID and asserted service properties from: Alex is enabled with the expected job title and department.
- Negative-boundary outcome from: The group is active, has no deletedDateTime, and every run-owned ID is represented once in run.json.
- Cleanup dependency recorded for the objects created or configured by LAB01-CP05.

Common failure and safe retry: A PATCH has not converged, or a transient relationship update left the final inventory inconsistent. Requery the exact user and group IDs; repeat only the missing property or relationship change.

Cleanup dependency: Cleanup deletes the group first, then the two exact manifest-recorded users, and verifies each ID returns not found.

## Final validation and result interpretation

Run independent deployment validation after all required checkpoints:

```powershell
./scripts/cli/Validate.ps1 -RunId 'az104l01-01' -Mode Deployment
az resource list --resource-group 'rg-az104-l01-az104l01-01' --query '[].{name:name,type:type}' --output table
```

- `pass`: every required positive and negative check passed.
- `partial`: every required check passed, but at least one optional gate was deliberately skipped.
- `fail`: a required checkpoint failed; do not record the lab as complete.

Keep the redacted `validation.json`; do not retain credentials, tokens, access keys, certificate material, email addresses, tenant IDs, or unredacted command output.

## Deterministic break/fix exercise

Injection: Delete Alex's direct member reference while leaving Blair's owner reference unchanged.

Expected symptom: The group still has an owner but the member query is empty, so group-based workload access disappears.

Diagnose with a read-only service query:

```powershell
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id" --output json | ConvertFrom-Json).value
$unexpected = @($users | Where-Object id -notin $external.userIds)
if ($users.Count -ne 2 -or $unexpected.Count -ne 0) { throw 'Run-specific user inventory contains a missing or unowned object.' }
'Run-specific users=2; unowned users=0'
```

Diagnosis: Compare the exact owner and member collections with the two IDs in run.json; do not infer either relationship from display names.

Repair: POST Alex's recorded directory-object reference back to the group's members/$ref endpoint and rerun both collections.

Before/after evidence must show the failed negative or positive check before repair and the same check passing afterward. Do not inject a second fault until the first is removed.

## Optional job-style challenge

Create a second role-appropriate group, transfer Alex's membership, and submit a before/after inventory that proves ownership did not move.

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
./scripts/cli/Cleanup.ps1 -RunId 'az104l01-01'
./scripts/cli/Cleanup.ps1 -RunId 'az104l01-01' -Execute
./scripts/cli/Validate.ps1 -RunId 'az104l01-01' -Mode PostCleanup
$group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?%24select=id,deletedDateTime" --output json | ConvertFrom-Json
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
$owners = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners?%24select=id" --output json | ConvertFrom-Json).value
if ($group.id -ne $external.groupId -or $group.deletedDateTime) { throw 'Group is missing or deleted.' }
if ($members.Count -ne 1 -or $members[0].id -ne $external.userIds[0] -or $owners.Count -ne 1 -or $owners[0].id -ne $external.userIds[1]) { throw 'Final member/owner reconciliation failed.' }
if (@($state.managedObjects | Where-Object { $_.type -in @('Microsoft.Graph/user','Microsoft.Graph/group') -and $_.lifecycleStatus -eq 'active' }).Count -ne 3) { throw 'Manifest identity inventory is incomplete.' }
'Final users=2; groups=1; members=1; owners=1'
```

`cleanup.json` passes only when no active manifest-managed object remains. Soft-deleted or intentionally retained items must be listed with their reason and expected disposition. The lifecycle never performs irreversible purge automatically.

## Exam debrief and assessment

Explain why the expected state, negative check, and cleanup boundary matter—not only which command was used. Map any missed concept back to its task anchor before reviewing the answer key.

Complete [QUESTIONS.md](assessment/QUESTIONS.md), then use [ANSWERS.md](assessment/ANSWERS.md) for option-by-option remediation. Scores of 85–100% indicate mastery, 70–84% indicate targeted review, and below 70% means repeat the mapped tasks.

## Microsoft Learn sources

- [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Microsoft Graph user resource type](https://learn.microsoft.com/en-us/graph/api/resources/user)
- [Microsoft Graph group members and owners overview](https://learn.microsoft.com/en-us/graph/api/resources/groups-overview)

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
$ResourceGroupName = $(if ('01' -in @('00', '01', '02')) { $null } else { "rg-az104-l01-$RunId" })

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

$requiredEnvironmentVariables = @(
    'AZ104_TENANT_DOMAIN'
    'AZ104_LAB_INITIAL_PASSWORD'
)
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

$tenantDomain = [Environment]::GetEnvironmentVariable('AZ104_TENANT_DOMAIN')
$initialPassword = [Environment]::GetEnvironmentVariable('AZ104_LAB_INITIAL_PASSWORD')

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
$domains = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/domains?$select=id,isVerified' --output json | ConvertFrom-Json).value
if (@($domains | Where-Object { $_.id -eq $tenantDomain -and $_.isVerified }).Count -ne 1) { throw 'The supplied tenant domain is not verified in the active tenant.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab01.graph-domain' -Required $true -Passed $probePassed -Actual $probeActual

$probePassed = $true
$probeActual = 'assertion passed (output not persisted)'
try {
    $LASTEXITCODE = 0
    & {
if (-not (Test-Path Env:AZ104_LAB_INITIAL_PASSWORD) -or [string]::IsNullOrWhiteSpace($initialPassword) -or $initialPassword.Length -lt 12) { throw 'The temporary password must contain at least 12 characters.' }
    } | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "native exit code $LASTEXITCODE" }
} catch {
    $probePassed = $false
    $probeActual = "assertion failed: $($_.Exception.GetType().Name)"
}
Add-PreflightResult -Id 'preflight.authored.lab01.password-policy' -Required $true -Passed $probePassed -Actual $probeActual

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
$ResourceGroupName = $(if ('01' -in @('00', '01', '02')) { $null } else { "rg-az104-l01-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-01 execution plan'
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
    labId = 'LAB-01'
    runId = $RunId
    createdAt = $now
    updatedAt = $now
    status = 'initialized'
    context = @{ cloud = [string]$account.environmentName; tenantId = [string]$account.tenantId; subscriptionId = [string]$SubscriptionId }
    acknowledgements = @{ cost = [bool]$AcknowledgeCost; tenantChange = [bool]$AcknowledgeTenantChange }
    inputs = @{ 'location' = $Location; 'secondary-location' = $SecondaryLocation }
    checkpointStates = @(
        @{ checkpointId = 'LAB01-CP01'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP02'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP03'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP04'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
        @{ checkpointId = 'LAB01-CP05'; required = $true; status = 'pending'; updatedAt = $now; message = 'Not started.' }
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
        $expectedTags = @{ purpose = 'az104-lab'; labId = '01'; runId = $RunId }
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
                $groupCheckpoint = $(if ([string]$group.name -eq [string]$ResourceGroupName) { 'LAB01-CP01' } else { $CheckpointId })
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

# CHECKPOINT LAB01-CP01 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP01'
    Save-RunState

    $tenant = az account show --query tenantId --output tsv
    $domains = @(az rest --method get --url 'https://graph.microsoft.com/v1.0/domains?$select=id,isVerified,isDefault' --output json | ConvertFrom-Json).value
    $domain = @($domains | Where-Object { $_.id -eq $env:AZ104_TENANT_DOMAIN -and $_.isVerified })
    if ($domain.Count -ne 1) { throw 'AZ104_TENANT_DOMAIN must name one verified domain in the active tenant.' }
    [pscustomobject]@{ tenant = '<redacted>'; domain = $domain[0].id; verified = $domain[0].isVerified }

    Sync-ManagedResource -CheckpointId 'LAB01-CP01'
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'pass' -Message 'The supplied domain appears exactly once with isVerified true, and the Graph request succeeds in the active tenant.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP01'
    Write-CheckpointState -CheckpointId 'LAB01-CP01' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP01 END

# CHECKPOINT LAB01-CP02 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP02'
    Save-RunState

    if ($env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) { throw 'The temporary password must contain at least 12 characters.' }
    $domain = $env:AZ104_TENANT_DOMAIN
    $userIds = @()
    $users = @(
        @{ alias = "az104l01a$suffix"; displayName = "AZ104-L01-$RunId-Alex"; department = 'Operations' },
        @{ alias = "az104l01b$suffix"; displayName = "AZ104-L01-$RunId-Blair"; department = 'Operations' }
    )
    foreach ($user in $users) {
        $bodyPath = Join-Path $StateDir ".user-$($user.alias).json"
        $body = @{
            accountEnabled = $true
            displayName = $user.displayName
            mailNickname = $user.alias
            userPrincipalName = "$($user.alias)@$domain"
            department = $user.department
            passwordProfile = @{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
        }
        try {
            $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $bodyPath -Encoding utf8
    try {
                $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$bodyPath" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    }
        } finally {
            Remove-Item -LiteralPath $bodyPath -Force -ErrorAction SilentlyContinue
        }
        $userIds += [string]$created.id
        $external['userIds'] = @($userIds)
    Save-ExternalState
        Add-ManagedObject -CheckpointId 'LAB01-CP02' -Kind 'entra-object' -Id ([string]$created.id) -Name $user.displayName -Type 'Microsoft.Graph/user' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    }
    Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue

    Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'pass' -Message 'Two enabled cloud-only users exist with unique UPNs, Operations department, and IDs already present in run.json.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP02'
    Write-CheckpointState -CheckpointId 'LAB01-CP02' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP02 END

# CHECKPOINT LAB01-CP03 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP03'
    Save-RunState

    $groupBodyPath = Join-Path $StateDir '.group.json'
    @{ displayName = "AZ104-L01-$RunId-Operators"; mailEnabled = $false; mailNickname = "az104l01g$suffix"; securityEnabled = $true } |
        ConvertTo-Json | Set-Content -LiteralPath $groupBodyPath -Encoding utf8
    try {
    try {
            $group = az rest --method post --url 'https://graph.microsoft.com/v1.0/groups' --body "@$groupBodyPath" --output json | ConvertFrom-Json
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    }
    } finally {
        Remove-Item -LiteralPath $groupBodyPath -Force -ErrorAction SilentlyContinue
    }
    $external['groupId'] = [string]$group.id
    Save-ExternalState
    Add-ManagedObject -CheckpointId 'LAB01-CP03' -Kind 'entra-object' -Id ([string]$group.id) -Name ([string]$group.displayName) -Type 'Microsoft.Graph/group' -Scope $state.context.tenantId -OwnershipMethod 'manifest-id'
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/`$ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    }

    Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'pass' -Message 'One security-enabled group exists and its direct members collection contains Alex but not Blair.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP03'
    Write-CheckpointState -CheckpointId 'LAB01-CP03' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP03 END

# CHECKPOINT LAB01-CP04 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP04'
    Save-RunState

    $ownerBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners/`$ref" --body $ownerBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    }
    $members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?`$select=id" --output json | ConvertFrom-Json).value.id
    if ($external.userIds[1] -in $members) { throw 'Blair must be an owner only for this checkpoint.' }

    Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'pass' -Message 'Blair is the sole explicit owner, Alex is the sole member, and the two object-ID sets do not overlap.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP04'
    Write-CheckpointState -CheckpointId 'LAB01-CP04' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP04 END

# CHECKPOINT LAB01-CP05 BEGIN
try {
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'in-progress' -Message 'Checkpoint execution started.'
    $activeCheckpointId = 'LAB01-CP05'
    Save-RunState

    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[0])" --body '{"jobTitle":"Cloud Operations Analyst"}' --output none
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":false}' --output none
    $disabled = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])?`$select=accountEnabled" --query accountEnabled --output tsv
    if ($disabled -ne 'false') { throw 'The disabled-state validation did not converge.' }
    az rest --method patch --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[1])" --body '{"accountEnabled":true}' --output none
    az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/$($external.userIds[0])/%24ref" --output none
    $faultMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
    if ($external.userIds[0] -in @($faultMembers.id)) { throw 'The missing-membership fault was not established.' }
    $memberBody = @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$($external.userIds[0])" } | ConvertTo-Json -Compress
    try {
        az rest --method post --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members/%24ref" --body $memberBody --output none
    } finally {
        Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    }
    $repairedMembers = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
    if ($repairedMembers.Count -ne 1 -or $repairedMembers[0].id -ne $external.userIds[0]) { throw 'Alex membership repair failed.' }

    Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'pass' -Message 'Alex has the new job title, Blair is enabled again, and the final relationship inventory still has one distinct member and owner.'
    Save-RunState
} catch {
    Sync-ManagedResource -CheckpointId 'LAB01-CP05'
    Write-CheckpointState -CheckpointId 'LAB01-CP05' -Status 'fail' -Message "Checkpoint failed: $($_.Exception.GetType().Name)"
    $state.status = 'failed'
    Save-RunState
    throw
}
# CHECKPOINT LAB01-CP05 END

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
if ($state.labId -ne 'LAB-01' -or $state.runId -ne $RunId) { throw 'Manifest ownership does not match this lab and run ID.' }
$PSNativeCommandUseErrorActionPreference = $false
$accountJson = az account show --output json 2>$null
$account = $(if ($LASTEXITCODE -eq 0 -and $accountJson) { $accountJson | ConvertFrom-Json } else { $null })
if (-not $account -or [string]$account.tenantId -ne [string]$state.context.tenantId -or [string]$account.id -ne [string]$state.context.subscriptionId) {
    $capturedAt = (Get-Date).ToUniversalTime().ToString('o')
    $actualContext = $(if ($account) { "tenant=$($account.tenantId); subscription=$($account.id)" } else { 'active context unavailable' })
    $contextFailure = @{
        schemaVersion = '1.0.0'; labId = 'LAB-01'; runId = $RunId; mode = $Mode
        generatedAt = $capturedAt; result = 'fail'
        summary = @{ required = 1; passed = 0; failed = 1; skipped = 0 }
        checks = @(@{ id = 'context.active'; checkpointId = 'LAB01-CP01'; kind = 'context'; required = $true; status = 'fail'; message = 'Active Azure context does not match the run manifest.'; evidence = @{ command = 'az account show --output json'; expected = 'tenant and subscription exactly match run.json'; actual = $actualContext; capturedAt = $capturedAt; redacted = $true } })
    }
    $contextFailure | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $ValidationPath -Encoding utf8
    Write-Host "Validation $Mode result: fail"
    Write-Host "Artifact: $ValidationPath"
    exit 1
}
$SubscriptionId = [string]$state.context.subscriptionId
$Location = [string]$state.inputs['location']
$SecondaryLocation = [string]$state.inputs['secondary-location']
$ResourceGroupName = $(if ('01' -in @('00', '01', '02')) { $null } else { "rg-az104-l01-$RunId" })
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$external = @{}
$userRecords = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/user' -and $_.lifecycleStatus -eq 'active' })
$groupRecords = @($state.managedObjects | Where-Object { $_.type -eq 'Microsoft.Graph/group' -and $_.lifecycleStatus -eq 'active' })
$alexRecord = @($userRecords | Where-Object name -like '*-Alex')
$blairRecord = @($userRecords | Where-Object name -like '*-Blair')
$external['userIds'] = @($(if ($alexRecord.Count -eq 1) { [string]$alexRecord[0].id } else { '' }), $(if ($blairRecord.Count -eq 1) { [string]$blairRecord[0].id } else { '' }))
$external['groupId'] = $(if ($groupRecords.Count -eq 1) { [string]$groupRecords[0].id } else { '' })

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

# CHECKPOINT LAB01-CP01 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB01-CP01' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP01' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab01-cp01.positive' -CheckpointId 'LAB01-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab01-cp01.negative' -CheckpointId 'LAB01-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$domain = az rest --method get --url "https://graph.microsoft.com/v1.0/domains/$($env:AZ104_TENANT_DOMAIN)?%24select=id,isVerified" --output json | ConvertFrom-Json
if ($domain.id -ne $env:AZ104_TENANT_DOMAIN -or -not $domain.isVerified) { throw 'Selected UPN domain is not verified.' }
$domain
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
    Add-ValidationCheck -Id 'lab01-cp01.positive' -CheckpointId 'LAB01-CP01' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id" --output json | ConvertFrom-Json).value
$unexpected = @($users | Where-Object id -notin $external.userIds)
if ($users.Count -ne 2 -or $unexpected.Count -ne 0) { throw 'Run-specific user inventory contains a missing or unowned object.' }
'Run-specific users=2; unowned users=0'
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
    Add-ValidationCheck -Id 'lab01-cp01.negative' -CheckpointId 'LAB01-CP01' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab01-cp01.residual' -CheckpointId 'LAB01-CP01' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB01-CP01 END

# CHECKPOINT LAB01-CP02 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB01-CP02' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP02' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab01-cp02.positive' -CheckpointId 'LAB01-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab01-cp02.negative' -CheckpointId 'LAB01-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id,displayName,accountEnabled,department" --output json | ConvertFrom-Json).value
if ($users.Count -ne 2 -or @($users | Where-Object { -not $_.accountEnabled -or $_.department -ne 'Operations' }).Count -ne 0) { throw 'Created-user state mismatch.' }
$users
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
    Add-ValidationCheck -Id 'lab01-cp02.positive' -CheckpointId 'LAB01-CP02' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$users = @(az rest --method get --url "https://graph.microsoft.com/v1.0/users?%24filter=startswith(displayName,'AZ104-L01-$RunId-')&%24select=id,userType" --output json | ConvertFrom-Json).value
if ($users.Count -ne 2 -or @($users | Where-Object userType -ne 'Member').Count -ne 0) { throw 'Expected exactly two member users.' }
$users
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
    Add-ValidationCheck -Id 'lab01-cp02.negative' -CheckpointId 'LAB01-CP02' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab01-cp02.residual' -CheckpointId 'LAB01-CP02' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB01-CP02 END

# CHECKPOINT LAB01-CP03 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB01-CP03' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP03' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab01-cp03.positive' -CheckpointId 'LAB01-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab01-cp03.negative' -CheckpointId 'LAB01-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id,displayName" --output json | ConvertFrom-Json).value
if ($members.Count -ne 1 -or $members[0].id -ne $external.userIds[0]) { throw 'Alex is not the sole direct member.' }
$members
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
    Add-ValidationCheck -Id 'lab01-cp03.positive' -CheckpointId 'LAB01-CP03' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($external.userIds[1] -in @($members.id)) { throw 'Blair received unintended membership.' }
'Blair direct membership=False'
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
    Add-ValidationCheck -Id 'lab01-cp03.negative' -CheckpointId 'LAB01-CP03' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab01-cp03.residual' -CheckpointId 'LAB01-CP03' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB01-CP03 END

# CHECKPOINT LAB01-CP04 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB01-CP04' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP04' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab01-cp04.positive' -CheckpointId 'LAB01-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab01-cp04.negative' -CheckpointId 'LAB01-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$owners = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners?%24select=id,displayName" --output json | ConvertFrom-Json).value
if ($owners.Count -ne 1 -or $owners[0].id -ne $external.userIds[1]) { throw 'Blair is not the sole explicit owner.' }
$owners
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
    Add-ValidationCheck -Id 'lab01-cp04.positive' -CheckpointId 'LAB01-CP04' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
if ($external.userIds[1] -in @($members.id)) { throw 'Ownership leaked into membership.' }
'Owner/member overlap=0'
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
    Add-ValidationCheck -Id 'lab01-cp04.negative' -CheckpointId 'LAB01-CP04' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab01-cp04.residual' -CheckpointId 'LAB01-CP04' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB01-CP04 END

# CHECKPOINT LAB01-CP05 BEGIN
$checkpointState = @($state.checkpointStates | Where-Object { $_.checkpointId -eq 'LAB01-CP05' })[0]
$checkpointObjects = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP05' })

if ($Mode -eq 'Deployment') {
    if ($checkpointState.status -eq 'skipped') {
        Add-ValidationCheck -Id 'lab01-cp05.positive' -CheckpointId 'LAB01-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'The optional checkpoint is explicitly skipped when its documented input is absent.' -Actual 'optional gate absent'
        Add-ValidationCheck -Id 'lab01-cp05.negative' -CheckpointId 'LAB01-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $true -Skipped $true -Command 'optional gate evaluation' -Expected 'No mutation occurs for a skipped optional checkpoint.' -Actual 'optional gate absent'
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
$alex = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($external.userIds[0])?%24select=id,jobTitle,department,accountEnabled" --output json | ConvertFrom-Json
if ($alex.id -ne $external.userIds[0] -or $alex.jobTitle -ne 'Cloud Operations Analyst' -or $alex.department -ne 'Operations' -or -not $alex.accountEnabled) { throw 'Alex lifecycle state mismatch.' }
$alex
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
    Add-ValidationCheck -Id 'lab01-cp05.positive' -CheckpointId 'LAB01-CP05' -Kind 'positive' -Required ([bool]$checkpointState.required) -Passed $positivePassed -Command 'query each manifest-recorded object by exact ID and run the authored service probe' -Expected 'Checkpoint state is pass, recorded objects exist, and service state matches.' -Actual $positiveActual

    $unsafe = @($checkpointObjects | Where-Object { $_.ownership.method -eq 'manifest-id-and-tags' -and ($_.ownership.expectedTags.runId -ne $RunId) })

    # AUTHORED SERVICE ASSERTION: negative
    $negativeProbePassed = $true
    $negativeProbeActual = 'serviceProbe=pass (output not persisted)'
    try {
        $LASTEXITCODE = 0
        & {
$group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)?%24select=id,deletedDateTime" --output json | ConvertFrom-Json
$members = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/members?%24select=id" --output json | ConvertFrom-Json).value
$owners = @(az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($external.groupId)/owners?%24select=id" --output json | ConvertFrom-Json).value
if ($group.id -ne $external.groupId -or $group.deletedDateTime) { throw 'Group is missing or deleted.' }
if ($members.Count -ne 1 -or $members[0].id -ne $external.userIds[0] -or $owners.Count -ne 1 -or $owners[0].id -ne $external.userIds[1]) { throw 'Final member/owner reconciliation failed.' }
if (@($state.managedObjects | Where-Object { $_.type -in @('Microsoft.Graph/user','Microsoft.Graph/group') -and $_.lifecycleStatus -eq 'active' }).Count -ne 3) { throw 'Manifest identity inventory is incomplete.' }
'Final users=2; groups=1; members=1; owners=1'
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
    Add-ValidationCheck -Id 'lab01-cp05.negative' -CheckpointId 'LAB01-CP05' -Kind 'negative' -Required ([bool]$checkpointState.required) -Passed $negativePassed -Command 'run the authored denied-state probe and compare manifest ownership' -Expected 'The service boundary and ownership checks both pass.' -Actual $negativeActual
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
    Add-ValidationCheck -Id 'lab01-cp05.residual' -CheckpointId 'LAB01-CP05' -Kind 'residual' -Required ([bool]$checkpointState.required) -Passed ($active.Count -eq 0) -Command 'query every recorded object by exact ID after cleanup' -Expected 'No active manifest-managed object remains.' -Actual "active=$($active -join ',')"
}
# CHECKPOINT LAB01-CP05 END

$requiredChecks = @($checks | Where-Object { $_.required })
$failedChecks = @($checks | Where-Object { $_.status -eq 'fail' })
$requiredSkippedChecks = @($checks | Where-Object { $_.required -and $_.status -eq 'skipped' })
$skippedChecks = @($checks | Where-Object { $_.status -eq 'skipped' })
$result = if ($failedChecks.Count -gt 0 -or $requiredSkippedChecks.Count -gt 0) { 'fail' } elseif ($skippedChecks.Count -gt 0) { 'partial' } else { 'pass' }
$document = @{
    schemaVersion = '1.0.0'
    labId = 'LAB-01'
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
        schemaVersion = '1.0.0'; labId = 'LAB-01'; runId = $RunId
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
if ($state.labId -ne 'LAB-01' -or $state.runId -ne $RunId) {
    Write-CleanupRefusal -Message 'Cleanup ownership refusal: manifest lab ID or run ID does not match.'
}
if ($Execute -and $active.Count -eq 0 -and $state.status -eq 'cleaned') {
    $priorRetained = @()
    if (Test-Path -LiteralPath $CleanupPath) {
        try { $priorRetained = @((Get-Content -LiteralPath $CleanupPath -Raw | ConvertFrom-Json).retainedItems) } catch { $priorRetained = @() }
    }
    $idempotent = @{
        schemaVersion = '1.0.0'; labId = 'LAB-01'; runId = $RunId
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
$ResourceGroupName = $(if ('01' -in @('00', '01', '02')) { $null } else { "rg-az104-l01-$RunId" })
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
                [string]$tags['labId'] -eq '01' -and
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
            [string]$expectedTags['labId'] -eq '01' -and
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

# CHECKPOINT LAB01-CP05 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP05' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB01-CP05'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB01-CP05 END

# CHECKPOINT LAB01-CP04 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP04' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB01-CP04'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB01-CP04 END

# CHECKPOINT LAB01-CP03 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP03' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB01-CP03'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB01-CP03 END

# CHECKPOINT LAB01-CP02 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP02' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB01-CP02'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB01-CP02 END

# CHECKPOINT LAB01-CP01 BEGIN
$targets = @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP01' -and $_.lifecycleStatus -eq 'active' })
foreach ($target in $targets) {
    $alreadyAbsent = $absentIds.Contains([string]$target.id)
    $actions.Add(@{ checkpointId = 'LAB01-CP01'; targetId = [string]$target.id; targetType = [string]$target.type; ownership = @{ method = [string]$target.ownership.method; verified = [bool]$verifiedOwnershipById[[string]$target.id] }; status = $(if ($alreadyAbsent) { 'skipped' } else { 'preview' }); message = $(if ($alreadyAbsent) { 'The exact manifest ID was already absent; idempotent cleanup recorded the safe end state.' } elseif ($Execute) { 'Pending removal through the dependency-safe ownership boundary.' } else { 'Would remove this exact manifest-recorded target.' }) })
}
$state.updatedAt = (Get-Date).ToUniversalTime().ToString('o')
$state | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Manifest -Encoding utf8
# CHECKPOINT LAB01-CP01 END

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
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP01' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp01.residual'; command = 'query manifest-recorded IDs for LAB01-CP01'; expected = 'zero active objects for LAB01-CP01'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP02' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp02.residual'; command = 'query manifest-recorded IDs for LAB01-CP02'; expected = 'zero active objects for LAB01-CP02'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP03' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp03.residual'; command = 'query manifest-recorded IDs for LAB01-CP03'; expected = 'zero active objects for LAB01-CP03'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP04' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp04.residual'; command = 'query manifest-recorded IDs for LAB01-CP04'; expected = 'zero active objects for LAB01-CP04'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
$checkpointRemaining = @($remaining | Where-Object { $_ -in @($state.managedObjects | Where-Object { $_.checkpointId -eq 'LAB01-CP05' } | ForEach-Object id) }); $residualChecks.Add(@{ id = 'cp05.residual'; command = 'query manifest-recorded IDs for LAB01-CP05'; expected = 'zero active objects for LAB01-CP05'; actual = "active=$($checkpointRemaining.Count)"; status = $(if ($Execute -and $checkpointRemaining.Count -eq 0) { 'pass' } elseif (-not $Execute) { 'skipped' } else { 'fail' }) })
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
    labId = 'LAB-01'
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

[Previous: Lab 00](../00-safe-bootstrap/README.md) · [Catalog](../README.md) · [Next: Lab 02](../02-entra-licenses-guests-sspr/README.md)
<!-- END GENERATED AZ104 V2 -->
