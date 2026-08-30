# AZ-104 source register

Research date: **2026-08-30**

Only first-party Microsoft sources are authoritative for the exam blueprint and technical lab claims. The current English study guide is the sole source used to count official objectives; supporting sources add role context, learning paths, and tool guidance.

## Blueprint and credential authorities

| Source ID | Source | Purpose | Verified | Notes |
|---|---|---|---|---|
| `SRC-EXAM-GUIDE` | [Study guide for Exam AZ-104: Microsoft Azure Administrator](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) | Canonical domain weights, skill groups, and objective text | 2026-08-30 | Skills measured as of 2026-04-17; page reports last update 2026-03-19 |
| `SRC-CERTIFICATION` | [Microsoft Certified: Azure Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) | Audience, role, exam, renewal, and credential context | 2026-08-30 | Credential page reports last update 2026-04-17 |
| `SRC-COURSE` | [Course AZ-104T00-A: Microsoft Azure Administrator](https://learn.microsoft.com/en-us/training/courses/az-104t00) | Instructor-led course context and related training | 2026-08-30 | Supporting source only; does not control objective counts |

## Microsoft Learn paths

| Source ID | Source | Curriculum use | Verified |
|---|---|---|---|
| `SRC-LP-PREREQ` | [AZ-104: Prerequisites for Azure administrators](https://learn.microsoft.com/en-us/training/paths/az-104-administrator-prerequisites/) | Lab 00 foundation and learner prerequisites | 2026-08-30 |
| `SRC-LP-IDENTITY` | [AZ-104: Manage identities and governance in Azure](https://learn.microsoft.com/en-us/training/paths/az-104-manage-identities-governance/) | Identity and governance domain | 2026-08-30 |
| `SRC-LP-STORAGE` | [AZ-104: Implement and manage storage in Azure](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/) | Storage domain | 2026-08-30 |
| `SRC-LP-COMPUTE` | [AZ-104: Deploy and manage Azure compute resources](https://learn.microsoft.com/en-us/training/paths/az-104-manage-compute-resources/) | Compute domain | 2026-08-30 |
| `SRC-LP-NETWORK` | [AZ-104: Configure and manage virtual networks for Azure administrators](https://learn.microsoft.com/en-us/training/paths/az-104-manage-virtual-networks/) | Networking domain | 2026-08-30 |
| `SRC-LP-MONITOR` | [AZ-104: Monitor and back up Azure resources](https://learn.microsoft.com/en-us/training/paths/az-104-monitor-backup-resources/) | Monitoring and recovery domain | 2026-08-30 |

## Command and automation authorities

| Source ID | Source | Curriculum use | Verified |
|---|---|---|---|
| `SRC-AZ-CLI` | [Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/) | Azure CLI command syntax and reference | 2026-08-30 |
| `SRC-AZ-PS` | [Azure PowerShell documentation](https://learn.microsoft.com/en-us/powershell/azure/) | Az PowerShell command syntax and module guidance | 2026-08-30 |
| `SRC-GRAPH-PS` | [Microsoft Graph PowerShell documentation](https://learn.microsoft.com/en-us/powershell/microsoftgraph/) | Microsoft Entra user, group, guest, and license operations | 2026-08-30 |
| `SRC-BICEP` | [Bicep documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) | Infrastructure-as-code interpretation, deployment, export, and decompilation | 2026-08-30 |
| `SRC-AZCOPY` | [Get started with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) | Storage data movement exercises | 2026-08-30 |
| `SRC-KQL` | [Kusto Query Language overview](https://learn.microsoft.com/en-us/kusto/query/) | Azure Monitor log queries and troubleshooting | 2026-08-30 |

## Domain documentation hubs

| Source ID | Source | Curriculum use | Verified |
|---|---|---|---|
| `SRC-ENTRA` | [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/) | Identity and tenant configuration | 2026-08-30 |
| `SRC-POLICY` | [Azure Policy documentation](https://learn.microsoft.com/en-us/azure/governance/policy/) | Governance, compliance, and remediation | 2026-08-30 |
| `SRC-STORAGE` | [Azure Storage documentation](https://learn.microsoft.com/en-us/azure/storage/) | Storage accounts, Blob Storage, and Azure Files | 2026-08-30 |
| `SRC-COMPUTE` | [Azure compute documentation](https://learn.microsoft.com/en-us/azure/?product=compute) | Virtual machines, containers, and App Service routing to service docs | 2026-08-30 |
| `SRC-NETWORK` | [Azure networking documentation](https://learn.microsoft.com/en-us/azure/networking/) | Virtual networks, security, DNS, load balancing, and diagnostics | 2026-08-30 |
| `SRC-MONITOR` | [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/) | Metrics, logs, Insights, alerts, and diagnostic settings | 2026-08-30 |
| `SRC-BACKUP` | [Azure Backup documentation](https://learn.microsoft.com/en-us/azure/backup/) | Vaults, policies, backup, restore, reports, and alerts | 2026-08-30 |
| `SRC-ASR` | [Azure Site Recovery documentation](https://learn.microsoft.com/en-us/azure/site-recovery/) | Replication, test failover, failover, and cleanup | 2026-08-30 |

## Source policy

- Recheck `SRC-EXAM-GUIDE` before authoring a release; Microsoft updates exams periodically and updates English first.
- Cite the most specific current Microsoft article in each lab and each answer explanation rather than citing only a documentation hub.
- Record a `lastVerified` date beside time-sensitive command or service behavior.
- Treat Microsoft Learn training as helpful sequencing, not as a replacement for the official objective list.
- Do not use exam dumps, leaked items, copied practice-assessment wording, or third-party question banks.
- When a source and a live tool disagree, pause the affected lab, record the discrepancy, and verify against the current service reference before changing instructions.
