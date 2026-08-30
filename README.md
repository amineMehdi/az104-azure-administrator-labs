# AZ-104 Azure Administrator Labs

A command-first, self-paced lab curriculum for the Microsoft Certified: Azure Administrator Associate exam. The repository follows the official skills measured as of **April 17, 2026** and is designed around Azure CLI, Az PowerShell, real validation, safe cleanup, architecture diagrams, and sanitized Azure Portal evidence.

> [!IMPORTANT]
> This is an independent learning project, not an official Microsoft course. Azure resources can incur charges. Use a disposable sandbox subscription, read each cost notice, and complete cleanup before leaving a lab.

## Current milestone

Repository foundation, `00-safe-bootstrap`, and `01-entra-users-groups` are offline-validated. Lab 01 live tenant execution and real Portal capture remain pending authorization.

## Exam coverage

| Domain | Exam weight | Planned labs |
|---|---:|---:|
| Manage Azure identities and governance | 20–25% | 5 |
| Implement and manage storage | 15–20% | 4 |
| Deploy and manage Azure compute resources | 20–25% | 7 |
| Implement and manage virtual networking | 15–20% | 5 |
| Monitor and maintain Azure resources | 10–15% | 4 |
| Foundation and capstones | — | 3 |

```mermaid
flowchart LR
    F[00 Safe bootstrap] --> I[01–05 Identity and governance]
    I --> S[06–09 Storage]
    S --> C[10–16 Compute]
    C --> N[17–21 Networking]
    N --> M[22–25 Monitor and recovery]
    M --> X[26–27 Capstones]
```

The verified blueprint contains **82 official objective bullets**. The curriculum adds five clearly marked foundation objectives for tooling, context, cost control, safe state, and cleanup.

## Learning model

Each lab follows the same loop:

1. Observe the starting state and predict the outcome.
2. Implement with one complete Azure CLI or PowerShell lane.
3. Test both expected and denied/failure behavior where relevant.
4. Validate using read-only commands and machine-readable results.
5. Inspect the result in the Azure Portal and capture sanitized evidence.
6. Clean up and audit for residual resources.
7. Complete ten original multiple-choice questions using the separate answer key.

Every lab is self-contained under `labs/<number>-<slug>/`. It does not import runtime files from another lab.

## Planned curriculum

| Lab | Topic | Primary surface | Status |
|---:|---|---|---|
| 00 | Safe bootstrap | CLI + PowerShell | Offline-validated |
| 01 | Entra users and groups | Azure CLI/Graph | Offline-validated |
| 02 | Entra licenses, guests, and SSPR | Graph/Entra PowerShell | Planned |
| 03 | Azure RBAC scopes | Az PowerShell | Planned |
| 04 | Resource hierarchy, tags, and locks | Azure CLI | Planned |
| 05 | Policy, costs, and Advisor | Az PowerShell | Planned |
| 06 | Storage accounts and security | Azure CLI | Planned |
| 07 | Storage networking and SAS | Az PowerShell | Planned |
| 08 | Blob lifecycle and replication | Azure CLI | Planned |
| 09 | Azure Files identity | Az PowerShell | Planned |
| 10 | ARM and Bicep lifecycle | CLI + PowerShell | Planned |
| 11 | VM lifecycle, disks, and host encryption | Azure CLI | Planned |
| 12 | VM resilience, scale, and mobility | Az PowerShell | Planned |
| 13 | ACR and ACI | Azure CLI | Planned |
| 14 | Azure Container Apps | Azure CLI | Planned |
| 15 | App Service scaling and slots | Az PowerShell | Planned |
| 16 | App Service TLS, DNS, backup, and networking | Azure CLI | Planned |
| 17 | VNets, subnets, peering, and public IPs | Az PowerShell | Planned |
| 18 | Routing, NSGs, and ASGs | Azure CLI | Planned |
| 19 | Service and private endpoints | Az PowerShell | Planned |
| 20 | Azure DNS and Bastion | Azure CLI | Planned |
| 21 | Load Balancer and Network Watcher | Az PowerShell | Planned |
| 22 | Azure Monitor logs and Insights | CLI + PowerShell | Planned |
| 23 | Monitor alerts and actions | Azure CLI | Planned |
| 24 | Azure Backup and restore | Az PowerShell | Planned |
| 25 | Site Recovery and failover | Az PowerShell | Planned |
| 26 | Capstone: build | Learner choice | Planned |
| 27 | Capstone: operate and recover | Opposite surface | Planned |

## Start here

1. Read [prerequisites](docs/prerequisites.md).
2. Read [cost and cleanup safety](docs/cost-and-cleanup.md).
3. Complete [Lab 00: Safe bootstrap](labs/00-safe-bootstrap/README.md).
4. In an authorized disposable tenant, complete [Lab 01: Entra users and groups](labs/01-entra-users-groups/README.md).
5. Follow the generated [lab catalog](labs/catalog.yml) and [objective map](docs/objective-map.md).

Labs can be run locally, in GitHub Codespaces, or in Azure Cloud Shell. Tool versions and permissions are checked by each lab rather than assumed.

## Important documentation

- [Official blueprint research](docs/research/az-104-blueprint.md)
- [Objective map](docs/objective-map.md)
- [Permissions matrix](docs/permissions-matrix.md)
- [Study plan](docs/study-plan.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Command cheat sheet](docs/command-cheatsheet.md)
- [Screenshot style guide](docs/screenshot-style-guide.md)
- [Assessment authoring guide](docs/assessment-guide.md)
- [Question bank index](docs/question-bank-index.md)
- [Implementation status](docs/implementation-status.md)
- [Project mega prompt](AZ-104-GITHUB-LABS-MEGA-PROMPT.md)

## Safety defaults

- Default primary region: `westeurope`; secondary: `northeurope`, subject to availability.
- Default live-test budget: no spending without approval; authorized batches are capped at €10.
- Preflight and validation are read-only.
- Cleanup is idempotent and limited to the recorded run ID.
- Pull-request CI never authenticates to Azure.
- Real Portal screenshots are required for live-verified labs; synthetic Portal images are forbidden.

## License

Code and documentation are available under the [MIT License](LICENSE).
