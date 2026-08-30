# Lab 00 — Safe Azure lab bootstrap

> **Status:** Offline-validated; live Azure queries and Portal screenshots are pending authorization.
> **Blueprint:** AZ-104 skills measured as of 2026-04-17.
> **Azure changes:** None. The scripts observe Azure and prepare lab-local state only.

You have inherited access to an Azure sandbox, but you do not yet know which tenant and subscription your terminal targets, whether the intended regions are available, which resource providers are registered, or whether regional compute quota can be read. Your first administrator task is to establish those facts and create a safe run record before any lab is allowed to deploy.

## Outcome

By the end of this lab, you will be able to:

- verify the exact cloud, tenant, subscription, and subscription state before running commands;
- distinguish read-only discovery from configuration changes;
- inspect region availability, provider registration, and compute usage/quota;
- produce a reusable run ID, naming stem, and mandatory tag set without creating a resource;
- generate a machine-readable validation report; and
- preview and remove only the selected run's local state.

This is a foundation lab, not direct scored-objective coverage. Its IDs support every later lab:

| Foundation objective | What you prove |
|---|---|
| `FD-TOOLS-01` | Required tools and maintained command surfaces are available. |
| `FD-CONTEXT-01` | The active tenant and subscription are explicit and correct. |
| `FD-COST-01` | Cost class, billable resources, and safe-stop behavior are understood. |
| `FD-SAFETY-01` | Naming and tags are prepared without leaking sensitive data. |
| `FD-CLEANUP-01` | Validation and cleanup remain scoped to a recorded run. |

## Architecture

![A learner uses Azure CLI or Az PowerShell for read-only Azure discovery while setup and validation write only lab-local run state.](diagrams/architecture.svg)

The Azure control plane is queried but never changed. `setup` writes `run.json`; `validate` reads Azure and writes `validation.json`; `cleanup` previews or removes exactly one `.state/<run-id>/` directory.

## Choose a command lane

Both lanes are complete. Use one for the exercise, then compare the other if you want practice translating administrator intent between tools.

| Lane | Requirements | Offline-tested versions |
|---|---|---|
| Azure CLI | Bash, Azure CLI, jq 1.6+ | Azure CLI 2.88.0 |
| Az PowerShell | PowerShell 7, `Az.Accounts`, `Az.Resources`, `Az.Compute` | PowerShell 7.6.5; Az.Accounts 2.12.1; Az.Resources 6.5.3; Az.Compute 5.5.0 |

Commands target public Azure by default. Sovereign-cloud learners must confirm that the selected regions and documentation apply to their cloud.

## Time, difficulty, cost, and permissions

- **Time:** 45–60 minutes
- **Difficulty:** Foundational
- **Cost class:** None
- **Billable resources:** None
- **Safe-stop point:** Every point in this lab; no Azure resource is created
- **Recommended access:** Reader at the target sandbox subscription
- **Entra roles / Graph scopes / licenses:** None
- **Default regions:** `westeurope` and `northeurope`, both configurable
- **Quota changes:** None; the scripts only read regional compute usage/quota
- **Provider changes:** None; an unregistered provider produces a warning

Do not use a production or employer subscription. Later labs can incur charges. Estimate them with the [Azure pricing calculator](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator), obtain authorization, and tear them down promptly. A Cost Management budget is an alerting mechanism: exceeding a budget does not stop resources or consumption.

## Resources and local state

No Azure resources, RBAC assignments, provider registrations, tenant settings, or CLI/PowerShell contexts are changed.

Setup creates only:

```text
.state/<run-id>/
└── run.json
```

Validation adds `validation.json`. The lab-local `.gitignore` excludes `.state/`. State includes tenant and subscription IDs so the scripts can prevent context drift; it never includes user names, tokens, keys, passwords, connection strings, or SAS values.

Prepared tags for later labs are:

```text
purpose=az104-lab
labId=00-safe-bootstrap
runId=<run-id>
expiresOn=<UTC date>
```

Tags are plain text and can appear in cost reports and logs. Never put sensitive data in them.

## Before you begin

1. Use a dedicated non-production sandbox.
2. Sign in interactively. The lab never signs in for you and never stores credentials.
3. Review the active context yourself.

Azure CLI:

```bash
az login
az account show --output table
# If necessary, make a deliberate local context choice:
az account set --subscription '<sandbox-subscription-id>'
```

Az PowerShell:

```powershell
Connect-AzAccount
Get-AzContext
# If necessary, make a deliberate local context choice:
Set-AzContext -Subscription '<sandbox-subscription-id>'
```

Context-changing commands above affect only your local Azure tool session, but they are intentionally not hidden inside the lab scripts. Stop if the tenant or subscription is not the sandbox you intend to use.

## Checkpoint 1 — Observe and predict your context

Before running preflight, predict:

- which tenant and subscription are active;
- whether the subscription state is `Enabled`; and
- whether your requested tenant/subscription IDs will match.

Run the read-only preflight with explicit IDs. Supplying both IDs makes an accidental-context error visible.

Azure CLI:

```bash
./scripts/cli/preflight.sh \
  --subscription-id '<sandbox-subscription-id>' \
  --tenant-id '<sandbox-tenant-id>' \
  --location westeurope \
  --secondary-location northeurope
```

Az PowerShell:

```powershell
./scripts/powershell/Preflight.ps1 `
  -SubscriptionId '<sandbox-subscription-id>' `
  -TenantId '<sandbox-tenant-id>' `
  -Location westeurope `
  -SecondaryLocation northeurope
```

Expected state:

- the exact context is printed locally;
- matching context and enabled subscription checks pass;
- unavailable regions fail;
- unregistered or unreadable providers and quota produce warnings, never automatic fixes.

Exit code `0` means all checks passed, `1` means a required check failed, and `2` means required checks passed with an optional warning. In PowerShell, inspect `$LASTEXITCODE`; in Bash, inspect `$?` immediately after the command.

Portal evidence is pending. After a separately authorized live run, `images/portal/01-subscription-overview.png` will show the sanitized subscription overview. Do not add a placeholder image.

## Checkpoint 2 — Prepare a run record

Predict which values must be unique and which should stay stable across resources. A run ID should be unique per attempt; `purpose` and `labId` stay stable; resource-type prefixes vary.

Choose a run ID and initialize local state.

Azure CLI:

```bash
RUN_ID="az10400-$(date -u +%Y%m%d%H%M%S)"
./scripts/cli/setup.sh \
  --subscription-id '<sandbox-subscription-id>' \
  --tenant-id '<sandbox-tenant-id>' \
  --location westeurope \
  --secondary-location northeurope \
  --run-id "$RUN_ID"

jq '{runId, regions, naming, tags, resources, liveAzureMutations}' \
  ".state/$RUN_ID/run.json"
```

Az PowerShell:

```powershell
$runId = 'az10400-{0}' -f [DateTime]::UtcNow.ToString('yyyyMMddHHmmss')
./scripts/powershell/Setup.ps1 `
  -SubscriptionId '<sandbox-subscription-id>' `
  -TenantId '<sandbox-tenant-id>' `
  -Location westeurope `
  -SecondaryLocation northeurope `
  -RunId $runId

Get-Content ".state/$runId/run.json" -Raw |
  ConvertFrom-Json |
  Select-Object runId, regions, naming, tags, resources, liveAzureMutations
```

Expected state: `resources` and `tenantScopedChanges` are empty and `liveAzureMutations` is `false`. Rerunning setup with the same valid run ID is idempotent and leaves the existing manifest unchanged.

## Checkpoint 3 — Inspect provider readiness

Predict which result means “ready for a later deployment”: `Registered`. `NotRegistered` is not an invitation to register everything. Least privilege and smaller attack surface favor registering only providers that an authorized workload needs.

The scripts observe these namespaces:

- `Microsoft.Authorization`
- `Microsoft.Compute`
- `Microsoft.Insights`
- `Microsoft.Network`
- `Microsoft.RecoveryServices`
- `Microsoft.Storage`

Optional focused query:

Azure CLI:

```bash
az provider show \
  --namespace Microsoft.Compute \
  --subscription '<sandbox-subscription-id>' \
  --query '{namespace:namespace,state:registrationState}' \
  --output table
```

Az PowerShell:

```powershell
Get-AzResourceProvider -ProviderNamespace Microsoft.Compute |
  Select-Object ProviderNamespace, RegistrationState -Unique
```

These are read-only commands. Do not run `az provider register` or `Register-AzResourceProvider` in this lab. Portal evidence `02-resource-providers.png` remains pending until authorized capture and sanitization.

## Checkpoint 4 — Inspect regional quota and cost risk

Quota is regional and service-specific. A successful read does not guarantee that every VM SKU is available or that a future request fits within the remaining quota.

Azure CLI:

```bash
az vm list-usage \
  --location westeurope \
  --subscription '<sandbox-subscription-id>' \
  --output table
```

Az PowerShell:

```powershell
Get-AzVMUsage -Location westeurope |
  Sort-Object CurrentValue -Descending |
  Select-Object -First 10 Name, CurrentValue, Limit
```

Expected state: usage and limit rows are returned, or the scripts record a warning explaining that permissions/provider readiness must be reviewed. This lab never requests quota. Portal evidence `03-usage-quotas.png` is pending.

## Checkpoint 5 — Positive and negative tests

### Positive test: validate the recorded run

Azure CLI:

```bash
./scripts/cli/validate.sh --run-id "$RUN_ID"
jq '{result, toolLane, checks}' ".state/$RUN_ID/validation.json"
```

Az PowerShell:

```powershell
./scripts/powershell/Validate.ps1 -RunId $runId
Get-Content ".state/$runId/validation.json" -Raw | ConvertFrom-Json
```

Validation reads Azure and writes only the local report. A provider or quota warning produces overall result `partial` and exit code `2`; it is never disguised as full verification.

### Negative safety test: detect a risky region choice

Use the same primary and secondary region. This changes nothing and should return exit code `2` with a resilience warning, provided required checks pass.

Azure CLI:

```bash
./scripts/cli/preflight.sh \
  --location westeurope \
  --secondary-location westeurope
```

Az PowerShell:

```powershell
./scripts/powershell/Preflight.ps1 `
  -Location westeurope `
  -SecondaryLocation westeurope
```

## Break/fix challenge — Configuration drift

Create a backup of `run.json`, change only `regions.primary` in the working copy to the nonexistent value `moonbase-1`, and run validation. You should get a failed `azure.primary-region` check and exit code `1`.

Your task is to restore the original value without rerunning setup or weakening validation.

Hints:

1. The backup is authoritative because setup refuses to overwrite an initialized run.
2. Compare the two JSON files before restoring.
3. Do not edit tenant/subscription IDs to make validation pass.

The exact recovery commands are in [solution/README.md](solution/README.md). Do not open the solution until you have diagnosed the failed check.

## Cleanup and residual-state audit

Cleanup is report-only by default. It refuses to proceed if the manifest records an Azure resource, a tenant-scoped change, or a live Azure mutation.

Azure CLI:

```bash
./scripts/cli/cleanup.sh --run-id "$RUN_ID"
./scripts/cli/cleanup.sh --run-id "$RUN_ID" --execute
test ! -e ".state/$RUN_ID" && echo 'PASS: no local run state remains'
```

Az PowerShell:

```powershell
./scripts/powershell/Cleanup.ps1 -RunId $runId
./scripts/powershell/Cleanup.ps1 -RunId $runId -Execute
if (-not (Test-Path ".state/$runId")) { 'PASS: no local run state remains' }
```

Deletion scope is exactly `.state/<run-id>/`. No Azure deletion, provider unregistration, context change, or tenant restoration occurs. Cleanup is idempotent: rerunning it after removal reports that nothing remains.

## Exam and administrator takeaways

- A tenant is the Microsoft Entra identity boundary; a subscription is an Azure resource, governance, and billing scope.
- Most CLI/cmdlet operations use the active context unless a subscription is explicitly supplied.
- Provider registration is subscription-scoped and should be intentional.
- Quota and service/SKU availability are different checks and often vary by region.
- Azure resource naming rules differ by resource type and uniqueness scope.
- Tags do not automatically inherit from a resource group to its resources.
- Budgets notify; they are not universal hard spending caps.
- Cleanup should use recorded IDs plus identifying tags, never a broad name-only or subscription-wide delete.

## Knowledge check

Complete the ten original questions in [assessment/QUESTIONS.md](assessment/QUESTIONS.md), then review explanations in [assessment/ANSWERS.md](assessment/ANSWERS.md). The foundation question bank is educational and is not copied from the certification exam.

## Official references

Last verified: **2026-08-30**.

- [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Manage Azure subscriptions with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli?view=azure-cli-latest)
- [Manage Azure subscriptions with Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/manage-subscriptions-azureps)
- [Azure resource providers and types](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types)
- [Azure CLI VM usage command](https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-list-usage)
- [Get-AzVMUsage](https://learn.microsoft.com/en-us/powershell/module/az.compute/get-azvmusage)
- [Define an Azure naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- [Use tags to organize Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)
- [Create and manage Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

Portal UI and command output can change. Replace screenshots and update their manifest when the interface changes; do not patch instructions around stale evidence.
