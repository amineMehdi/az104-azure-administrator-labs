# AZ-104 glossary

## Action group

A reusable set of notification or automation receivers invoked by Azure Monitor
alerts.

## Application security group

A logical collection of virtual-machine network interfaces used as the source
or destination in an NSG rule, so policy follows the workload role instead of a
hard-coded address.

## Azure Policy

A governance service that audits or changes resource behavior by evaluating
definitions and initiatives at an assigned scope.

## Azure RBAC

Azure role-based access control. It authorizes actions at management group,
subscription, resource group, or resource scope through role assignments.

## Bicep

A declarative language for Azure Resource Manager deployments. A Bicep file is
compiled to an ARM JSON template before Azure evaluates the deployment.

## Checkpoint

A lab milestone with an expected state, positive and negative validation,
evidence guidance, objective mapping, and cleanup dependency.

## Cleanup ownership boundary

The exact set of manifest-recorded IDs, context values, and expected tags that
must agree with live state before a cleanup mutation is permitted.

## Control plane

Azure Resource Manager operations that create or configure resources. Control
plane authorization is distinct from data-plane authorization.

## Data plane

Operations against data inside a service, such as reading blobs or secrets.
Data-plane access may require a separate role even when control-plane access is
available.

## Diagnostic setting

A resource configuration that routes supported platform logs and metrics to a
destination such as Log Analytics, a Storage account, or an event hub.

## Idempotent cleanup

A cleanup operation that remains safe when run more than once and reports an
already-absent target as a successful end state.

## KQL

Kusto Query Language, used to filter, aggregate, and correlate records in Azure
Monitor Logs and other Azure Data Explorer-based services.

## Log Analytics workspace

The Azure Monitor data store and query boundary that holds tables populated by
diagnostic settings, agents, and service integrations.

## Managed identity

An identity managed by Azure that lets a resource request tokens without storing
application credentials.

## Negative validation

A deliberate read-only check proving that an unauthorized, invalid, or broken
path is denied as expected.

## Network security group

An ordered set of stateful allow and deny rules applied to a subnet or network
interface. The effective rules also account for defaults and all associations.

## Partial result

A truthful outcome used when every required checkpoint passes but a documented
optional gate is skipped. It is not interchangeable with a pass or failure.

## Private endpoint

A network interface with a private address that connects a virtual network to a
supported Azure service through Private Link.

## Recovery point objective

The maximum acceptable amount of data loss measured in time.

## Recovery Services vault

A vault used by workloads such as Azure VM Backup and Site Recovery. Its
supported protection model differs from the newer Backup vault resource.

## Recovery time objective

The target duration for restoring a service after disruption.

## Residual-resource check

A post-cleanup query that proves no active lab-managed resources remain and
records any expected soft-deleted or retained item.

## Run ID

A unique, non-secret identifier applied to state, names, and ownership tags so a
lab can validate and clean up only its own resources.

## Self-service password reset

A Microsoft Entra capability that lets an eligible user reset or unlock their
account after satisfying the configured authentication policy.

## Service endpoint

A subnet configuration that extends a virtual network identity to a supported
Azure service while the service still uses its public endpoint.

## Shared access signature

A time-bounded, permission-scoped token that delegates access to specific
Storage resources. The token itself is secret and is never retained as lab
evidence.

## Soft delete

A service retention state in which a deleted object or recovery point remains
recoverable for a configured period even though no active resource should use
it.

## Tenant-scoped change

A configuration change whose effect is broader than the lab resource group. The
labs require explicit authorization, a captured original setting, and a
documented restoration path before making one.

## User-defined route

A route-table entry that overrides or augments Azure system routes for a subnet,
using a declared address prefix and next-hop type.

## Virtual network peering

A non-transitive private connection between two Azure virtual networks. Each
direction has its own peering object and forwarding or gateway settings.

## What-if

A deployment preview that describes planned Azure Resource Manager changes
without applying them.
