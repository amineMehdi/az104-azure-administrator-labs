# Lab catalog

The curriculum contains 28 numbered, self-contained labs. Azure CLI is hosted in PowerShell throughout; there are no Bash lanes, browser procedures, screenshots, or screenshot-evidence steps.

## How to use a lab

Start with [Lab 00](00-safe-bootstrap/README.md), then open the domain that matches your pathway. Each README contains the complete guided command lane. Its lifecycle scripts are an optional synchronized automation lane, so use a different run ID if you try both.

Labs 01–25 each include exactly 50 original questions with task-level remediation. Lab 00 and Capstones 26–27 are hands-on only and link to the compact [assessment dashboard](../docs/question-bank-index.md).

## Domains

- Foundation: [Lab 00 — Safe bootstrap](00-safe-bootstrap/README.md)
- Identity and governance: [Labs 01–05](01-entra-users-groups/README.md)
- Storage: [Labs 06–09](06-storage-accounts-security/README.md)
- Compute: [Labs 10–16](10-arm-bicep-lifecycle/README.md)
- Networking: [Labs 17–21](17-vnet-subnets-peering-public-ip/README.md)
- Monitoring and recovery: [Labs 22–25](22-azure-monitor-logs-insights/README.md)
- End-to-end practice: [Lab 26 — Build](26-capstone-build/README.md) and [Lab 27 — Operate and recover](27-capstone-operate-recover/README.md)

The machine-readable [catalog.yml](catalog.yml) powers the documentation navigation and validator. Repository checks are offline; live Azure verification requires separate access and cost approval.
