# AZ-104 GitHub Labs: research baseline and mega prompt

> Research snapshot: 2026-08-29
> Current Microsoft blueprint: skills measured as of 2026-04-17
> Intended use: paste the mega prompt below into Codex or another capable coding agent to build the repository.

## Research conclusion

Microsoft's current AZ-104 blueprint has five domains, 15 skill groups, and 82 illustrative objective bullets. Microsoft notes that related topics may also appear and that commonly used Preview features can occasionally be assessed.

| Exam domain | Weight |
|---|---:|
| Manage Azure identities and governance | 20–25% |
| Implement and manage storage | 15–20% |
| Deploy and manage Azure compute resources | 20–25% |
| Implement and manage virtual networking | 15–20% |
| Monitor and maintain Azure resources | 10–15% |

Authoritative sources:

- [Official AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure Administrator Associate certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/)
- [Current Microsoft Learn AZ-104 paths](https://learn.microsoft.com/en-us/training/browse/?terms=AZ-104)
- [Official MicrosoftLearning AZ-104 lab repository](https://github.com/MicrosoftLearning/AZ-104-MicrosoftAzureAdministrator)

The MicrosoftLearning repository currently contains 14 lab units. They are useful scenario references but are largely Portal-first and do not give deep hands-on coverage to every 2026 objective. Important gaps for a command-first curriculum include licensing and SSPR, budgets and Advisor, several storage data-protection features, VM mobility and host encryption, App Service security/networking/backup, private access, restore operations, Connection Monitor, and a complete Site Recovery failover.

## Recommended size

Build **28 separate lab folders**:

- 1 safe bootstrap lab
- 5 identity and governance labs
- 4 storage labs
- 7 compute labs
- 5 networking labs
- 4 monitoring and recovery labs
- 2 cross-domain capstones

Twenty-four labs are a workable minimum if related services are compressed into long exercises. Twenty-eight is the better full curriculum: it keeps most labs focused, independently resumable, and suitable for approximately 60–120 minutes of work. Expect roughly **45–60 hands-on hours**, including validation, troubleshooting, Portal verification, screenshots, and cleanup.

Every lab remains Azure CLI or PowerShell-first. Real Azure Portal screenshots are added after the command-line work to teach UI recognition and prove the expected state; Portal clicking must not become the primary implementation path.

---

# BEGIN MEGA PROMPT

## Role

Act as a principal Azure administrator, AZ-104 curriculum architect, technical writer, GitHub repository maintainer, automation engineer, and visual QA reviewer.

Build a polished, self-paced GitHub repository that prepares a learner for the complete current Microsoft AZ-104 Azure Administrator exam through command-first, scenario-based labs.

Be accurate, practical, security-conscious, cost-conscious, and honest about anything that cannot be live-tested. Use clear English suitable for a learner who knows cloud fundamentals but is developing administrator-level judgment.

## Goal

Create a production-quality repository named `az-104-cli-powershell-labs` containing exactly **28 numbered, self-contained lab folders** under `labs/`.

The repository must:

1. Trace every current official AZ-104 objective to at least one lab.
2. Use Azure CLI, Az PowerShell, Microsoft Graph/Entra PowerShell, or `az rest` as the canonical implementation surface for every required administrative action.
3. Include real, current, sanitized Azure Portal screenshots captured after executing each lab in an authorized Azure sandbox.
4. Include an architecture diagram and objective validation for every lab.
5. Include safe, idempotent cleanup and a residual-resource check for every lab.
6. Be pleasant to browse and learn from directly on GitHub.
7. Never claim that a command, screenshot, live test, or objective was completed when it was not.

## Success criteria

The work is complete only when all of the following are true:

- The live Microsoft study guide has been checked and its effective date is recorded.
- All official objective bullets are present in a machine-checkable traceability matrix.
- Every objective maps to teaching content, a lab or explicit gated exercise, a verification method, and a coverage status.
- All 28 lab folders exist and satisfy the folder and README contracts below.
- Each lab has at least one complete command-line lane; there are no incomplete pseudo-equivalents.
- Each lab can be copied out of the repository and used without importing runtime files from another lab.
- Offline lint, schema, syntax, and documentation checks pass.
- Live-tested labs record the date, tenant type, region, tool versions, result, screenshot manifest, and cleanup result without exposing identifiers.
- Gated or untested labs are clearly marked `partial`, `blocked`, or `offline-validated`; they are never labeled fully verified.
- No credentials, tokens, keys, passwords, SAS values, personal email addresses, tenant IDs, subscription IDs, or sensitive Portal details are committed.
- README tables, objective mappings, image links, and lab metadata agree with one another.

## Configuration defaults

Use these defaults unless the repository already contains an explicit, compatible decision:

```yaml
repositoryName: az-104-cli-powershell-labs
documentationLanguage: en-US
blueprintBaseline: 2026-04-17
labCount: 28
commandMode: hybrid
primaryCommandSurface: Azure CLI
secondaryCommandSurface: Az PowerShell
portalRole: verification-and-ui-recognition
screenshotMode: real-portal-only
defaultRegion: configurable
secondaryRegion: configurable
liveAzureDeployment: requires-user-authorization
defaultLiveCostAuthorization: none
```

Do not hardcode a tenant, subscription, region, domain, username, public IP, SKU, or fixed price. Use parameters and explain regional, quota, permission, licensing, and price dependencies.

## Authority and safety boundaries

You are authorized to research, plan, create and edit local repository files, run non-destructive local validation, and prepare scripts.

Before signing in to Azure, deploying resources, inviting users, assigning licenses, changing tenant settings, creating billable services, registering features, changing subscription or management-group state, or capturing real Portal screenshots:

1. Inspect the intended live changes.
2. Present one concise batch summary containing the target tenant/subscription, roles needed, regions, billable resources, expected duration, and cleanup strategy.
3. Obtain explicit user authorization.
4. Confirm the exact tenant and subscription again in the preflight output.

Never use a production subscription or an employer tenant without explicit authorization. Recommend a dedicated disposable sandbox subscription and test tenant.

Do not publish the repository, enable GitHub Pages, create cloud credentials, configure OIDC, push to a remote, or open a pull request unless explicitly asked.

## Source-of-truth and freshness gate

Before building content, browse and read the current versions of:

1. [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
2. [Azure Administrator Associate certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/)
3. The six current AZ-104 Microsoft Learn paths
4. [MicrosoftLearning/AZ-104-MicrosoftAzureAdministrator](https://github.com/MicrosoftLearning/AZ-104-MicrosoftAzureAdministrator)
5. Current official Microsoft documentation for every command and Azure feature used

Use primary Microsoft documentation for changing technical claims. The official GitHub training repository may inform scenarios and architecture, but write original lab instructions and cite sources rather than copying its prose.

Create:

- `docs/research/az-104-blueprint.md`
- `docs/research/source-register.md`
- `docs/objective-map.md`
- `curriculum/blueprint.yml`

Record the research date, effective blueprint date, source URL, and any differences from the baseline below. If Microsoft has published a newer effective blueprint, the live blueprint wins: update the catalog, lab mapping, counts if genuinely necessary, and document the change before implementation. Do not silently keep a stale objective list merely to preserve the requested number.

## Current objective baseline to verify

### 1. Manage Azure identities and governance (20–25%)

#### Manage Microsoft Entra users and groups

- Create users and groups.
- Manage user and group properties.
- Manage licenses in Microsoft Entra ID.
- Manage external users.
- Configure self-service password reset (SSPR).

#### Manage access to Azure resources

- Manage built-in Azure roles.
- Assign roles at different scopes.
- Interpret access assignments.

#### Manage Azure subscriptions and governance

- Implement and manage Azure Policy.
- Configure resource locks.
- Apply and manage tags on resources.
- Manage resource groups.
- Manage subscriptions.
- Manage costs by using alerts, budgets, and Azure Advisor recommendations.
- Configure management groups.

### 2. Implement and manage storage (15–20%)

#### Configure access to storage

- Configure Azure Storage firewalls and virtual networks.
- Create and use shared access signature (SAS) tokens.
- Configure stored access policies.
- Manage access keys.
- Configure identity-based access for Azure Files.

#### Configure and manage storage accounts

- Create and configure storage accounts.
- Configure Azure Storage redundancy.
- Configure object replication.
- Configure storage account encryption.
- Manage data by using Azure Storage Explorer and AzCopy.

#### Configure Azure Files and Azure Blob Storage

- Create and configure a file share in Azure Files.
- Create and configure a container in Azure Blob Storage.
- Configure storage tiers.
- Configure soft delete for blobs and containers.
- Configure snapshots and soft delete for Azure Files.
- Configure blob lifecycle management.
- Configure blob versioning.

### 3. Deploy and manage Azure compute resources (20–25%)

#### Automate deployment by using ARM templates or Bicep files

- Interpret an Azure Resource Manager template or a Bicep file.
- Modify an existing Azure Resource Manager template.
- Modify an existing Bicep file.
- Deploy resources by using an Azure Resource Manager template or a Bicep file.
- Export a deployment as an Azure Resource Manager template or convert an ARM template to Bicep.

#### Create and configure virtual machines

- Create a virtual machine.
- Configure encryption at host for Azure virtual machines.
- Move a virtual machine to another resource group, subscription, or region.
- Manage virtual machine sizes.
- Manage virtual machine disks.
- Deploy virtual machines to availability zones and availability sets.
- Deploy and configure Azure Virtual Machine Scale Sets.

#### Provision and manage containers

- Create and manage an Azure Container Registry.
- Provision a container by using Azure Container Instances.
- Provision a container by using Azure Container Apps.
- Manage sizing and scaling for containers, including Azure Container Instances and Azure Container Apps.

#### Create and configure Azure App Service

- Provision an App Service plan.
- Configure scaling for an App Service plan.
- Create an App Service.
- Configure certificates and TLS for an App Service.
- Map an existing custom DNS name to an App Service.
- Configure backup for an App Service.
- Configure networking settings for an App Service.
- Configure deployment slots for an App Service.

### 4. Implement and manage virtual networking (15–20%)

#### Configure and manage virtual networks

- Create and configure virtual networks and subnets.
- Create and configure virtual network peering.
- Configure public IP addresses.
- Configure user-defined routes.
- Troubleshoot network connectivity.

#### Configure secure access to virtual networks

- Create and configure network security groups and application security groups.
- Evaluate effective security rules in network security groups.
- Implement Azure Bastion.
- Configure service endpoints for Azure PaaS.
- Configure private endpoints for Azure PaaS.

#### Configure name resolution and load balancing

- Configure Azure DNS.
- Configure an internal or public load balancer.
- Troubleshoot load balancing.

### 5. Monitor and maintain Azure resources (10–15%)

#### Monitor resources

- Interpret metrics in Azure Monitor.
- Configure log settings in Azure Monitor.
- Query and analyze logs in Azure Monitor.
- Set up alert rules, action groups, and alert processing rules in Azure Monitor.
- Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights.
- Use Azure Network Watcher and Connection Monitor.

#### Implement backup and recovery

- Create a Recovery Services vault.
- Create an Azure Backup vault.
- Create and configure a backup policy.
- Perform backup and restore operations by using Azure Backup.
- Configure Azure Site Recovery for Azure resources.
- Perform a failover to a secondary region by using Site Recovery.
- Configure and interpret reports and alerts for backups.

## Required lab catalog

Create these exact folders unless the freshness gate proves that a current blueprint change requires an adjustment. If adjusted, preserve the separate-folder rule and explain the delta.

| Folder | Focus | Canonical surface | Target time |
|---|---|---|---:|
| `00-safe-bootstrap` | Tools, authentication, subscription context, naming, tags, provider/quota checks, cost warnings, validation, safe cleanup | Both | 45–60m |
| `01-entra-users-groups` | Users, groups, memberships, and properties | Azure CLI/Graph | 60–75m |
| `02-entra-licenses-guests-sspr` | License assignment, B2B invitation, and SSPR | Graph/Entra PowerShell | 75–105m |
| `03-azure-rbac-scopes` | Built-in roles, assignments at multiple scopes, inherited and effective access | Az PowerShell | 75–90m |
| `04-resource-hierarchy-tags-locks` | Subscriptions, management groups, resource groups, tags, and locks | Azure CLI | 75–90m |
| `05-policy-costs-advisor` | Policy definitions/initiatives/remediation, budgets, alerts, and Advisor | Az PowerShell | 90–120m |
| `06-storage-accounts-security` | Account configuration, redundancy, encryption, and keys | Azure CLI | 75–90m |
| `07-storage-network-sas` | Firewall/VNet access, SAS, stored access policy, and positive/negative tests | Az PowerShell | 90–105m |
| `08-blob-lifecycle-replication` | Containers, tiers, versioning, soft delete, lifecycle, object replication, and AzCopy | Azure CLI | 105–120m |
| `09-azure-files-identity` | File shares, identity-based access, snapshots, soft delete, AzCopy, and Storage Explorer awareness | Az PowerShell | 105–135m |
| `10-arm-bicep-lifecycle` | Interpret, modify, validate, what-if, deploy, export, and decompile | Both | 105–120m |
| `11-vm-lifecycle-disks-encryption` | VM creation, sizes, disks, and encryption at host | Azure CLI | 90–120m |
| `12-vm-resilience-scale-mobility` | Zones, availability sets, VMSS, autoscaling, and RG/subscription/region mobility | Az PowerShell | 120–150m |
| `13-acr-aci` | Azure Container Registry and Azure Container Instances | Azure CLI | 75–105m |
| `14-container-apps` | Environments, revisions, ingress, sizing, and scaling | Azure CLI | 90–120m |
| `15-app-service-scale-slots` | Plans, apps, scale up/out, deployment slots, and swap | Az PowerShell | 105–120m |
| `16-app-service-tls-dns-backup-network` | TLS/certificates, custom DNS, backup, and networking | Azure CLI | 120–150m |
| `17-vnet-subnets-peering-public-ip` | VNets, subnets, public IPs, and peering | Az PowerShell | 90–105m |
| `18-routing-nsg-asg` | UDRs, NSGs, ASGs, effective rules, and connectivity diagnosis | Azure CLI | 105–120m |
| `19-service-private-endpoints` | Service endpoints, private endpoints, private DNS, and public-access denial | Az PowerShell | 105–120m |
| `20-azure-dns-bastion` | Public/private DNS concepts and secure Bastion access | Azure CLI | 105–120m |
| `21-load-balancer-network-watcher` | Public/internal load balancers, probes, troubleshooting, Network Watcher, and Connection Monitor | Az PowerShell | 120–150m |
| `22-azure-monitor-logs-insights` | Metrics, diagnostic settings, Log Analytics, KQL, and Insights | Both | 105–135m |
| `23-monitor-alerts-actions` | Alert rules, action groups, alert processing rules, and controlled triggering | Azure CLI | 75–105m |
| `24-azure-backup-restore` | Recovery Services vault, Backup vault, policies, backup, restore, reports, and alerts | Az PowerShell | 120–150m |
| `25-site-recovery-failover` | Azure-to-Azure replication, isolated test failover/failover, and cleanup | Az PowerShell | 150–180m |
| `26-capstone-build` | Secure, governed, highly available, observable workload | Learner choice | 180m |
| `27-capstone-operate-recover` | Fault injection, diagnosis, restore/failover, optimization, and complete teardown | Opposite tool | 180m |

If Lab 26 is completed with Azure CLI, require Az PowerShell for Lab 27, and vice versa.

## Separate-folder invariant

Every lab must live in its own folder directly under `labs/`. A learner must be able to copy that one folder elsewhere and run it after satisfying its declared prerequisites.

Use this shape:

```text
labs/
├── README.md
├── catalog.yml
├── 00-safe-bootstrap/
│   ├── README.md
│   ├── lab.yml
│   ├── images/
│   │   ├── README.md
│   │   ├── manifest.yml
│   │   └── portal/
│   │       ├── 01-subscription-context.png
│   │       └── 02-resource-result.png
│   ├── diagrams/
│   │   ├── architecture.mmd
│   │   └── architecture.svg
│   ├── scripts/
│   │   ├── cli/
│   │   │   ├── preflight.sh
│   │   │   ├── setup.sh
│   │   │   ├── validate.sh
│   │   │   └── cleanup.sh
│   │   └── powershell/
│   │       ├── Preflight.ps1
│   │       ├── Setup.ps1
│   │       ├── Validate.ps1
│   │       └── Cleanup.ps1
│   ├── solution/
│   ├── infra/
│   ├── data/
│   └── tests/
├── 01-entra-users-groups/
└── ...
```

Rules:

- Do not create empty command-lane folders. Include only a complete, declared lane.
- No `../` runtime imports, cross-lab symlinks, or dependencies on another lab.
- Root tooling may scaffold, lint, index, and test, but it must not be required by a learner running a lab.
- Vendor any small required runtime helper inside the lab.
- Store transient state in `.state/<run-id>/`; ignore it in Git.
- State may contain resource IDs and original settings, never secrets, keys, passwords, access tokens, or SAS tokens.
- `setup` creates prerequisites but does not silently solve learner exercises.
- `validate` is read-only.
- `cleanup` is idempotent and restricted to the recorded run.
- `solution` is opt-in, clearly separated from the exercise, and safe to rerun.

## Command policy

- Every required configuration action must be performed through Azure CLI or PowerShell.
- Use Azure CLI as the general default.
- Use current Az PowerShell, Microsoft Graph PowerShell, or Microsoft Entra PowerShell where those are the maintained and more reliable administrative interfaces.
- Do not use the retired `AzureAD` or `MSOnline` modules.
- Stable Microsoft Graph v1.0 via `az rest` is acceptable where regular `az` commands do not expose a required Entra operation.
- Allow Bicep CLI, AzCopy, KQL, `curl`, `openssl`, `dig`, `nslookup`, and similar focused companion tools only when needed by the objective.
- The core path must not depend on clicking through the Azure Portal.
- Where the blueprint explicitly names the Portal or Azure Storage Explorer, add a concise UI-recognition or optional interface exercise. Do not mislabel a conceptual note as a completed hands-on objective.
- Commands must be copyable, use parameters/variables, avoid deprecated aliases, and show expected output or a meaningful assertion.
- Explain why a command matters before asking the learner to run it.
- Never expose passwords, keys, connection strings, SAS values, or tokens in commands, screenshots, shell history, logs, or committed state.
- Prefer SSH keys, managed identities, Entra authentication, and least-privilege RBAC.

## Real Azure Portal screenshot policy

Each lab must include real screenshots made by walking through the deployed lab resources in the Azure Portal after the command-line steps succeed.

Portal images are evidence and visual orientation, not the primary procedure.

For each lab:

1. Run the lab in an explicitly authorized Azure sandbox.
2. Run validation and confirm the intended state.
3. Open the Azure Portal using the user's already authenticated browser session.
4. Navigate to the most useful blades for understanding and verifying the result.
5. Capture 2–5 meaningful screenshots; use more only for a genuinely complex workflow.
6. Place them in that lab's `images/portal/` folder.
7. Reference each image next to the matching verification step in the lab README.
8. Add accurate alt text, a short caption, and what the screenshot proves.
9. Record capture metadata in `images/manifest.yml`.
10. Perform cleanup only after all required evidence is captured.

The manifest must record:

```yaml
- file:
  step:
  portalBlade:
  proves:
  capturedAt:
  azureRegion:
  portalUiVersionOrNotes:
  redactions:
  source: real-azure-portal
```

Screenshot rules:

- Never generate or substitute AI-made Portal screenshots.
- Never use another person's screenshots as proof of this repository's live test.
- Never capture sign-in pages, account menus, access tokens, keys, passwords, connection strings, SAS tokens, billing details, or unrelated resources.
- Crop away or irreversibly flatten redactions over tenant IDs, subscription IDs, object IDs, personal emails, custom domains, and other account-specific details not essential to learning.
- Prefer framing that avoids sensitive data rather than adding many redactions.
- Strip image metadata.
- Use a consistent Portal theme, browser zoom, and readable viewport.
- Optimize PNGs without making Portal text blurry.
- Use descriptive filenames such as `02-private-endpoint-approved.png`.
- Add `Captured YYYY-MM-DD; Portal UI may change` below the image.
- Validate every relative image link and enforce reasonable image dimensions/file sizes in CI.
- If live access or authorization is unavailable, create the README, manifest schema, and a clearly marked screenshot checklist. Do not create fake PNGs, do not show broken image links, and report the screenshots as pending.
- When the Portal UI has changed since an image was captured, replace the screenshot and update its manifest rather than patching instructions around stale visuals.

## Architecture visuals

In addition to Portal images, every topology or workflow lab must include:

- Mermaid source in `diagrams/architecture.mmd`.
- A checked-in SVG rendering for accessibility and reuse.
- Useful alt text and a short explanation in the README.

Create these repository-level visuals:

- Curriculum roadmap with exam percentages.
- Azure scope hierarchy: tenant → management group → subscription → resource group → resource.
- Storage authorization decision tree.
- Compute resilience and mobility map.
- VNet, peering, service endpoint, and private endpoint flow.
- DNS and load-balancing resolution flow.
- Azure Monitor signal pipeline.
- Backup versus Site Recovery comparison and failover sequence.
- Capstone architecture and incident timeline.

Use diagrams to explain relationships and flows, not as decoration.

## `lab.yml` contract

Every folder must include validated metadata with at least:

```yaml
id:
title:
blueprintVersion:
domain:
objectives:
track:
testedToolVersions:
estimatedMinutes:
cost:
  class:
  billableResources:
permissions:
  azureRbacRoles:
  entraRoles:
  graphScopes:
prerequisites:
providers:
regions:
creates:
tenantScopedChanges:
externalRequirements:
validation:
screenshotStatus:
cleanup:
lastOfflineValidated:
lastLiveVerified:
```

Use stable objective IDs in `curriculum/blueprint.yml`, and reference those IDs from every `lab.yml`.

## Every lab README must contain

Use the same high-quality structure without making the writing robotic:

1. Title, status, and short scenario.
2. Concrete outcome and why an Azure administrator needs it.
3. Exact mapped AZ-104 objectives and blueprint date.
4. Architecture diagram.
5. Tool lane and tested versions.
6. Estimated time and difficulty.
7. Cost class, billable resources, safe-stop point, and pricing link.
8. Azure RBAC roles, Entra roles, Graph scopes, licenses, regions, quotas, and external requirements.
9. Resources created and naming pattern.
10. Preflight instructions and expected checks.
11. Learning exercises divided into checkpoints rather than one giant solution script.
12. For each checkpoint: explanation, command, expected state/output, validation, and relevant real Portal screenshot.
13. At least one positive test and, when relevant, one negative security test.
14. One realistic break/fix challenge with hints separated from the solution.
15. A read-only validation command and explanation of pass/fail/warning/skipped.
16. Cleanup command, exact deletion scope, asynchronous deletion notes, and residual-resource audit.
17. Tenant-level restoration steps when the lab changes shared settings.
18. Exam takeaways, common misconceptions, and 3–5 reasoning questions.
19. Official Microsoft references with a `last verified` date.
20. Accessibility-friendly captions and alt text for all visuals.

Do not turn a lab into a wall of commands. Use the learning loop:

1. Observe.
2. Predict.
3. Implement.
4. Test a success case.
5. Test or diagnose a failure case.
6. Validate objectively.
7. Inspect the result in the Portal and capture evidence.
8. Clean up.
9. Reflect with exam-style questions.

## Conditional and elevated labs

Clearly flag scenarios that many learners cannot run in a free or shared tenant:

- Entra licensing, SSPR, B2B, tenant roles, and Graph consent.
- Management-group and multi-subscription authority.
- Identity-based Azure Files prerequisites.
- Full VM cross-subscription or cross-region movement.
- Bastion and private endpoints.
- Owned/delegated DNS name and App Service certificate validation.
- Backup and restore wait times.
- Site Recovery replication and failover.

Each conditional lab needs:

- A full authorized hands-on path.
- A safe observation, what-if, or partial fallback.
- An honest coverage status.
- A clear list of what the fallback does not prove.
- No fabricated screenshot or validation result.

## Preflight, validation, and cleanup

Preflight must check:

- Exact account, tenant, and subscription.
- Required roles, Graph scopes, and licenses.
- Provider and feature registrations.
- Regional SKU availability and quotas.
- Current tool versions and required extensions/modules.
- Global-name availability.
- External prerequisites.
- Expected billable resources.

Validation must:

- Query control-plane state through CLI, PowerShell, or Azure Resource Graph.
- Probe real data-plane behavior where possible.
- Include negative security assertions where relevant.
- Emit readable console output and machine-readable `validation.json`.
- Distinguish `pass`, `fail`, `warning`, and `skipped`.
- Never report full completion when a gated objective was skipped.

Cleanup must:

- Delete only IDs recorded in lab-local state and resources matching the lab's tags and run ID.
- Print a deletion plan before changing tenant, management-group, subscription, RBAC, Policy, identity, DNS, backup, or replication state.
- Restore original shared settings from a pre-change snapshot.
- Remove locks before resource-group deletion.
- Handle hidden or residual resources such as identities, invitations, role assignments, policies, budgets, protected items, ASR replication, snapshots, disks, public IPs, Log Analytics workspaces, private DNS links, and managed resource groups.
- Wait for asynchronous operations when needed.
- Run a residual-resource inventory.
- Be safely rerunnable after partial failure.

Any repository-wide janitor must be report-only by default. Deletion requires a separate explicit mode, an exact subscription allowlist, and tag plus state verification.

## Cost and security rules

- Tag every taggable resource with `purpose=az104-lab`, `labId`, `runId`, and `expiresOn`.
- Do not place personal information or sensitive values in tags.
- Use relative cost classes and link to current official pricing; do not promise stale fixed prices.
- Explain that budgets send alerts and are not hard spending caps.
- Require explicit confirmation for materially billable resources such as Bastion, VMSS, Monitor ingestion, backups, Resource Mover, and Site Recovery.
- Prefer same-session teardown.
- Never allow SSH or RDP from `0.0.0.0/0`.
- Use the narrowest practical RBAC scope.
- Use short-lived SAS permissions and expiry when SAS is required.
- Never echo secrets.
- For local or Codespaces use interactive/device authentication without storing Azure tokens.
- If live GitHub Actions are later authorized, use OIDC federation, a protected environment, and least privilege; never use a long-lived client secret.
- Never run tenant-global, cross-subscription, custom-domain, or Site Recovery changes automatically in pull-request CI.

## Repository experience

Create at least:

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CHANGELOG.md
.gitignore
.editorconfig
.devcontainer/
.github/
  ISSUE_TEMPLATE/
  PULL_REQUEST_TEMPLATE.md
  workflows/
curriculum/
  blueprint.yml
  lab-schema.json
docs/
  research/
  objective-map.md
  prerequisites.md
  permissions-matrix.md
  cost-and-cleanup.md
  study-plan.md
  troubleshooting.md
  command-cheatsheet.md
  screenshot-style-guide.md
  visuals/
labs/
  README.md
  catalog.yml
  00-safe-bootstrap/
  ...
  27-capstone-operate-recover/
tools/
  generate-catalog/
  validate-repository/
```

The root README must include:

- A concise explanation of the project and its independent/non-official status.
- The effective exam blueprint date.
- A strong warning about Azure cost, permissions, and cleanup.
- A quick-start path for local use, Azure Cloud Shell, and GitHub Codespaces.
- A Mermaid curriculum roadmap.
- The five domain weights.
- A generated table of all 28 labs with domain, tool, time, cost class, permissions, screenshot status, and verification status.
- A CLI path, a PowerShell path, and a recommended mixed path.
- A progress checklist.
- Links to the objective map, study plan, prerequisites, troubleshooting, and official Microsoft resources.
- A freshness and contribution policy.

Generate repeated index data from `lab.yml` rather than hand-maintaining contradictory tables.

## CI and quality gates

Pull-request CI must not authenticate to Azure. It should perform:

- Markdown lint, spelling, and internal-link/image checks.
- Mermaid parse/render checks.
- YAML and JSON schema validation.
- Coverage validation: every official objective maps to at least one lab and a verification method.
- Lab-folder portability and forbidden cross-lab reference checks.
- Bash syntax, ShellCheck, and formatting checks.
- PowerShell parser, PSScriptAnalyzer, and Pester unit/mocked tests.
- Bicep build/lint and ARM template validation.
- GitHub Actions lint.
- Secret-pattern scanning.
- Checks for required cost, permissions, validation, cleanup, screenshot, reference, and blueprint metadata.
- Checks that third-party GitHub Actions are pinned to full commit SHAs.

If live Azure smoke tests are later authorized, make them manual or tightly bounded scheduled jobs with OIDC, a protected sandbox environment, concurrency one, `if: always()` cleanup, and post-cleanup inventory. Never run expensive or tenant-wide labs automatically.

## Implementation sequence

Work in phases and keep the repository usable after each phase:

1. Research current sources and freeze the verified blueprint.
2. Create the objective IDs, schemas, catalog, repository structure, and quality gates.
3. Build `00-safe-bootstrap` as the golden lab and validate the pattern.
4. Build labs domain by domain, updating the objective matrix continuously.
5. Run offline validation after each domain.
6. Prepare a consolidated live-test and screenshot plan with cost/permission gates.
7. After authorization, execute labs in small batches, validate, capture sanitized Portal images, and clean up each batch.
8. Complete both capstones.
9. Run the full objective, portability, documentation, image, secret, and residual-resource audits.
10. Produce a final verification report.

Do not create 28 superficial placeholder READMEs merely to satisfy the folder count. Finish a domain to the quality bar before moving on. If the full implementation cannot fit in one working session, leave a precise status document and continue from it; do not lower the definition of done.

## Stop and escalation rules

- Continue autonomously through safe local research, authoring, and offline validation.
- Ask only for information that cannot be discovered and would materially change the result.
- Stop before any live external change until the user authorizes the summarized target and cost exposure.
- If Azure permissions, licenses, quotas, domains, or credentials block a lab, complete all safe local work, record the exact blocker, and mark the lab honestly.
- Retry transient read-only or local validation failures reasonably; do not loop indefinitely.
- Never bypass a safety, cost, permission, or cleanup gate to make the status appear complete.

## Final report format

Lead with the outcome and include:

1. Repository location and current blueprint date.
2. Number of complete, partial, blocked, offline-validated, and live-verified labs.
3. Objective coverage totals and any uncovered objective IDs.
4. Offline validation results.
5. Live test, screenshot, and cleanup results.
6. Costs or billable resources created during testing.
7. Material limitations and exact next actions.
8. Links to the root README, objective map, catalog, screenshot guide, and verification report.

# END MEGA PROMPT

---

## Notes for the project owner

The prompt intentionally separates local repository creation from live Azure execution. Building scripts and documentation is safe local work; producing genuine Portal screenshots requires an authenticated Azure environment, suitable permissions and licenses, live deployments, and cost authorization.

The CLI/PowerShell-first rule is compatible with the exam's administration topics, but Microsoft also explicitly expects Portal familiarity and names Azure Storage Explorer and AzCopy. The repository should therefore use command-line implementation plus real Portal verification images and short interface-awareness notes rather than claiming that the other interfaces do not matter.

## Approved assessment addendum

The project owner subsequently approved the following requirements, which extend the mega prompt and take precedence where it is silent:

- Create exactly ten original multiple-choice questions per lab: 280 questions across 28 labs.
- Give every question four options (A–D) and exactly one correct answer.
- Store the source in `assessment/questions.yml`, learner questions in `assessment/QUESTIONS.md`, and explanations in `assessment/ANSWERS.md` inside each lab folder.
- Map every question to official objective IDs or clearly marked non-exam foundation IDs.
- Assess every one of the 82 official objective bullets at least once.
- Use a 3 foundational / 5 applied / 2 advanced difficulty mix per lab.
- Explain why the correct option is right and why each distractor is wrong, citing current official Microsoft documentation.
- Balance correct-answer positions and prohibit exam dumps, copied practice questions, ambiguous trick wording, and synthetic claims that questions came from the real exam.
