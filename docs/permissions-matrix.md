# Permissions matrix

Each lab declares its exact requirements in `lab.yml`. This summary describes the permission categories used by the curriculum.

| Category | Typical requirement | Examples |
|---|---|---|
| Subscription read | Reader | Context, provider, quota, and inventory checks |
| Resource management | Contributor or service-specific role | Storage, compute, network, and monitoring labs |
| Access management | User Access Administrator or Owner | RBAC assignments |
| Governance | Resource Policy Contributor, management-group authority | Policy and hierarchy labs |
| Entra administration | Specific Entra roles and Graph scopes | Users, licenses, guests, SSPR |
| Data plane | Service-specific data roles | Blob, Files, and backup validation |

The broad `Owner` role is not a default. Preflight should fail or mark a gated path when the narrow required permission is unavailable.

## Implemented identity labs

| Lab | Microsoft Entra requirement | Azure RBAC requirement | Notes |
|---|---|---|---|
| 00 Safe bootstrap | None | Reader recommended for discovery | Read-only; creates no Azure or tenant object. |
| 01 Entra users and groups | User Administrator recommended at the intended tenant scope | None | Creates two disposable users and one security group; subscription Owner is not a substitute. |
