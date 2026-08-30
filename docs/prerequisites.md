# Prerequisites

## Knowledge

- Azure fundamentals, networking, operating systems, servers, and virtualization.
- Basic command-line and source-control familiarity.

## Azure environment

- A disposable sandbox tenant and subscription that you are authorized to modify.
- `Reader` is sufficient for many preflight checks; labs declare additional Azure RBAC and Entra roles individually.
- A €10 live-test batch ceiling by default. Elevated labs require separate approval.
- `westeurope` and `northeurope` are defaults, not guarantees; preflight checks service and SKU availability.

Never use production or an employer tenant unless the owner has explicitly approved the exact lab changes.

## Tools

- Git
- Azure CLI
- PowerShell 7 and the current Az modules
- Python 3 with the development requirements
- Bicep and AzCopy for the labs that declare them
- A browser with access to the Azure Portal for live-verification screenshots

The dev container provides a reproducible starting point. Every lab still checks its own required extensions and modules.

## Authentication

Use interactive or device authentication locally. Do not save access tokens in the repository. Future GitHub Actions that contact Azure must use OIDC and a protected environment; pull-request checks stay offline.
