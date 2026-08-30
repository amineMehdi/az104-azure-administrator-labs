#!/usr/bin/env python3
"""Build the offline-authored Lab 02-27 folders from reviewed curriculum specifications.

The generated labs are intentionally marked offline-validated only after the repository
validator and local safety tests pass. This tool never invokes Azure or Microsoft Graph.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from textwrap import dedent

import yaml


ROOT = Path(__file__).resolve().parents[1]
LABS_ROOT = ROOT / "labs"
BLUEPRINT_DATE = "2026-04-17"
REVIEW_DATE = "2026-08-30"


def s(
    number: str,
    title: str,
    surface: str,
    cost: str,
    minutes: int,
    role: str,
    summary: str,
    resources: list[str],
    providers: list[str],
    modules: list[str],
    actions: list[str],
    expected_types: list[str],
    portal: list[tuple[str, str]],
    sources: list[str],
    fact: str,
    gate: str = "None beyond the declared role and a disposable subscription.",
    scope: str = "resource-group",
    setup: str = "",
    validate: str = "",
    cleanup: str = "",
) -> dict:
    return locals()


SPECS: dict[str, dict] = {
    "02": s(
        "02",
        "Manage Entra licenses, guests, and self-service password reset",
        "Microsoft Graph PowerShell",
        "none",
        105,
        "User Administrator and License Administrator; Authentication Policy Administrator for the SSPR policy path",
        "Build a disposable identity cohort, inventory available licenses, invite an external user, and scope self-service password reset without assigning a license or changing tenant policy unless the required gates are explicitly supplied.",
        ["security group", "invited guest user", "optional license assignment", "optional SSPR scope"],
        [],
        ["Microsoft.Graph.Authentication", "Microsoft.Graph.Users", "Microsoft.Graph.Groups", "Microsoft.Graph.Identity.SignIns"],
        [
            "Create a security group that represents the SSPR pilot cohort.",
            "Invite a disposable external account only when AZ104_GUEST_EMAIL is supplied.",
            "Inventory subscribed SKUs and assign only AZ104_LICENSE_SKU_ID when explicitly supplied.",
            "Read the authorization policy and enable the gated SSPR pilot path only after AZ104_ALLOW_SSPR_POLICY_CHANGE=YES.",
        ],
        [],
        [
            ("Microsoft Entra ID > Groups > All groups", "The isolated SSPR pilot group and membership"),
            ("Microsoft Entra ID > Users > All users", "The invited guest user and external identity type"),
            ("Microsoft Entra ID > Protection > Password reset", "The selected-group SSPR scope when the gated path is authorized"),
        ],
        [
            "https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info",
            "https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-invite-powershell",
            "https://learn.microsoft.com/en-us/entra/identity/users/licensing-powershell-graph-examples",
            "https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr",
        ],
        "SSPR and group-based licensing are tenant capabilities with role and license gates; inventory and scoped pilots are safer than tenant-wide changes.",
        "Requires a real disposable guest email for invitation, an available SKU for license assignment, and an authorized tenant policy change for SSPR.",
        scope="tenant",
    ),
    "03": s(
        "03",
        "Assign and interpret Azure RBAC at multiple scopes",
        "Az PowerShell",
        "none",
        90,
        "User Access Administrator or Owner at the lab resource-group scope",
        "Create a tagged resource group, inspect built-in role definitions, assign Reader to an explicitly supplied principal, compare inherited and direct assignments, and remove only the recorded role assignment.",
        ["resource group", "resource-group-scoped role assignment"],
        ["Microsoft.Authorization", "Microsoft.Resources"],
        ["Az.Accounts", "Az.Resources"],
        [
            "Create the dedicated tagged resource group.",
            "Resolve Reader and Contributor built-in role definitions without creating custom roles.",
            "Assign Reader at resource-group scope to AZ104_PRINCIPAL_OBJECT_ID.",
            "Interpret the principal's direct and inherited access at resource-group and subscription scopes.",
        ],
        [],
        [
            ("Resource group > Access control (IAM) > Role assignments", "The direct Reader assignment and its scope"),
            ("Resource group > Access control (IAM) > Check access", "The principal's effective assignments"),
            ("Subscriptions > Access control (IAM)", "The contrast between subscription and resource-group scope"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell",
            "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles",
            "https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access",
        ],
        "A role definition describes allowed actions; a role assignment binds that definition to a principal at a scope, with inheritance flowing downward.",
        "Requires the object ID of a disposable principal in AZ104_PRINCIPAL_OBJECT_ID.",
    ),
    "04": s(
        "04",
        "Manage hierarchy, resource groups, tags, and locks",
        "Azure CLI",
        "none",
        90,
        "Contributor plus User Access Administrator for lock management; Management Group Contributor for the optional hierarchy path",
        "Create and retag a resource group, apply a CanNotDelete lock, examine subscription metadata, and optionally create an isolated management group when tenant authorization is explicit.",
        ["resource group", "resource lock", "optional management group"],
        ["Microsoft.Authorization", "Microsoft.Management", "Microsoft.Resources"],
        [],
        [
            "Create a resource group with purpose, labId, runId, owner, and expiresOn tags.",
            "Update tags using merge semantics and verify which values do not inherit automatically.",
            "Create a CanNotDelete lock and test the protected deletion path.",
            "Inventory the active subscription and run the optional management-group branch only with AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE=YES.",
        ],
        ["Microsoft.Authorization/locks"],
        [
            ("Resource groups > Overview", "The lab resource group and effective tags"),
            ("Resource group > Locks", "The CanNotDelete lock and its notes"),
            ("Management groups", "The optional isolated management group and parent relationship"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources",
            "https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal",
        ],
        "Tags are metadata rather than access controls, and resource locks protect the control plane without replacing RBAC or data-plane protection.",
        "Management-group creation is optional and requires explicit tenant hierarchy authorization.",
    ),
    "05": s(
        "05",
        "Enforce policy and manage costs with budgets and Advisor",
        "Az PowerShell",
        "none",
        120,
        "Resource Policy Contributor at the lab scope; Cost Management Contributor for the optional budget path",
        "Assign a built-in required-tag policy to a disposable resource group, evaluate compliance, inventory Advisor recommendations, and create a tightly named budget only when a notification email is explicitly provided.",
        ["resource group", "policy assignment", "optional cost budget"],
        ["Microsoft.Authorization", "Microsoft.Advisor", "Microsoft.Consumption", "Microsoft.CostManagement"],
        ["Az.Accounts", "Az.Resources", "Az.Advisor"],
        [
            "Create the tagged policy-test resource group.",
            "Assign the built-in Require a tag and its value on resources policy at resource-group scope.",
            "Trigger and interpret a policy compliance scan without claiming immediate convergence.",
            "Read Advisor cost recommendations and create an optional low-threshold budget with AZ104_BUDGET_EMAIL.",
        ],
        ["Microsoft.Authorization/policyAssignments"],
        [
            ("Resource group > Policies", "The scoped policy assignment and parameter value"),
            ("Policy > Compliance", "The evaluated compliance state and timestamp"),
            ("Cost Management > Budgets", "The optional lab budget and notifications"),
            ("Advisor > Cost", "Current cost recommendations or an empty recommendation state"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-powershell",
            "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets",
            "https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations",
        ],
        "Policy compliance is eventually evaluated, budgets notify rather than stop spending, and Advisor recommendations remain advisory until an administrator acts.",
        "Budget creation requires AZ104_BUDGET_EMAIL and Cost Management authorization; otherwise the lab inventories cost controls without creating one.",
    ),
    "06": s(
        "06",
        "Secure storage accounts, redundancy, encryption, and keys",
        "Azure CLI",
        "low",
        90,
        "Contributor on the lab resource group",
        "Create a StorageV2 account with secure transport, TLS 1.2, disabled public blob access, infrastructure encryption, and configurable redundancy; inspect and rotate one access key without persisting it.",
        ["resource group", "StorageV2 account"],
        ["Microsoft.Storage"],
        [],
        [
            "Create a globally unique StorageV2 account with Standard_ZRS when available and a documented LRS fallback.",
            "Require HTTPS, TLS 1.2, and disabled anonymous blob access.",
            "Inspect Microsoft-managed encryption and infrastructure encryption settings.",
            "Regenerate the secondary access key and prove no key enters repository state.",
        ],
        ["Microsoft.Storage/storageAccounts"],
        [
            ("Storage account > Overview", "Account kind, location, and redundancy"),
            ("Storage account > Configuration", "Secure transfer, TLS, and public access settings"),
            ("Storage account > Encryption", "Encryption services and infrastructure encryption"),
            ("Storage account > Access keys", "Key-management interface with all key values redacted"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage",
        ],
        "Redundancy protects copies of data, encryption protects data at rest, and access keys are broad secrets that must be rotated without entering state or command evidence.",
    ),
    "07": s(
        "07",
        "Restrict storage networking and issue scoped SAS access",
        "Az PowerShell",
        "low",
        105,
        "Contributor plus Storage Account Contributor on the lab resource group",
        "Create a storage account, service-endpoint subnet, network rule, private container, stored access policy, and short-lived SAS token while keeping credentials out of state.",
        ["resource group", "virtual network and subnet", "storage account", "blob container", "stored access policy"],
        ["Microsoft.Network", "Microsoft.Storage"],
        ["Az.Accounts", "Az.Resources", "Az.Network", "Az.Storage"],
        [
            "Create a virtual network subnet with the Microsoft.Storage service endpoint.",
            "Create a secure StorageV2 account and change the network default action to Deny.",
            "Add the subnet as an allowed storage network rule.",
            "Create a private container and stored access policy, then generate a short-lived service SAS only in memory.",
        ],
        ["Microsoft.Network/virtualNetworks", "Microsoft.Storage/storageAccounts"],
        [
            ("Storage account > Networking", "Default deny and the allowed virtual network rule"),
            ("Storage account > Containers", "The private container"),
            ("Container > Access policy", "The stored access policy and expiry"),
            ("Storage account > Shared access signature", "SAS controls with token values excluded"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview",
            "https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy",
            "https://learn.microsoft.com/en-us/powershell/module/az.storage/",
        ],
        "A stored access policy can revoke or change a service SAS, while account SAS and access keys have broader authority and require stricter handling.",
    ),
    "08": s(
        "08",
        "Manage Blob lifecycle, tiers, versioning, replication, and AzCopy",
        "Azure CLI",
        "low",
        120,
        "Contributor and Storage Blob Data Contributor on the lab resource group",
        "Create source and destination storage accounts, private containers, versioning, soft delete, lifecycle rules, sample tier changes, and an object-replication policy; exercise AzCopy only when the tool is available.",
        ["resource group", "two StorageV2 accounts", "blob containers", "lifecycle policy", "object replication policy"],
        ["Microsoft.Storage"],
        [],
        [
            "Create source and destination general-purpose v2 accounts with change feed and blob versioning.",
            "Enable blob and container soft delete and create private containers.",
            "Apply a lifecycle rule that moves older block blobs to cool storage and deletes old versions.",
            "Configure object replication and use AzCopy for a sample upload when AZCOPY is installed.",
        ],
        ["Microsoft.Storage/storageAccounts"],
        [
            ("Storage account > Data protection", "Versioning, change feed, and soft-delete settings"),
            ("Storage account > Lifecycle management", "The tiering and version cleanup rule"),
            ("Storage account > Object replication", "Source and destination replication policy"),
            ("Container > Blobs", "Sample blob versions and access tier"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview",
            "https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview",
            "https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview",
            "https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10",
        ],
        "Object replication depends on versioning and change feed, while lifecycle rules act asynchronously and should be validated as configuration rather than immediate data movement.",
    ),
    "09": s(
        "09",
        "Configure Azure Files, snapshots, soft delete, and identity access",
        "Az PowerShell",
        "low",
        135,
        "Contributor and Storage File Data SMB Share Contributor; directory permissions for the optional identity-source path",
        "Create a storage account and file share, enable share soft delete, create a snapshot, copy sample data, and prepare an identity-based SMB configuration through an explicitly gated Entra Kerberos or AD DS path.",
        ["resource group", "storage account", "Azure file share", "share snapshot"],
        ["Microsoft.Storage"],
        ["Az.Accounts", "Az.Resources", "Az.Storage"],
        [
            "Create a secure StorageV2 account and transaction-optimized file share with quota.",
            "Enable Azure Files share soft delete and create a point-in-time share snapshot.",
            "Upload sample content with AzCopy or Az.Storage without storing account keys.",
            "Inventory identity-based SMB options and configure only the authorized AZ104_FILES_IDENTITY_SOURCE path.",
        ],
        ["Microsoft.Storage/storageAccounts", "Microsoft.Storage/storageAccounts/fileServices/shares"],
        [
            ("Storage account > File shares", "The share, quota, and selected tier"),
            ("File share > Snapshots", "The point-in-time share snapshot"),
            ("Storage account > Data protection", "Azure Files soft-delete retention"),
            ("Storage account > File shares > Identity-based access", "The configured or gated directory source"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share",
            "https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files",
            "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion",
            "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files",
        ],
        "Share snapshots and soft delete solve different recovery problems, while identity-based SMB authentication requires an approved directory source and data-plane authorization.",
        "Identity-based SMB configuration is gated by AZ104_FILES_IDENTITY_SOURCE because Entra Kerberos, AD DS, and Entra Domain Services have different prerequisites.",
    ),
}

SPECS.update({
    "10": s(
        "10",
        "Interpret, modify, deploy, export, and decompile ARM and Bicep",
        "Azure CLI and Bicep",
        "none",
        120,
        "Contributor on the lab resource group",
        "Read equivalent ARM and Bicep definitions, change parameters and conditions, run build and what-if, deploy a tagged storage account, export the resource group template, and decompile an ARM template for comparison.",
        ["resource group", "Bicep deployment", "StorageV2 account", "exported ARM template"],
        ["Microsoft.Resources", "Microsoft.Storage"],
        [],
        [
            "Build and lint the supplied Bicep file and inspect its generated ARM JSON.",
            "Modify parameter values and run a resource-group what-if before deployment.",
            "Deploy through Azure CLI and inspect deployment operations and outputs.",
            "Export the resource group template and decompile a reviewed ARM template into a separate comparison file.",
        ],
        ["Microsoft.Resources/deployments", "Microsoft.Storage/storageAccounts"],
        [
            ("Resource group > Deployments", "Deployment inputs, outputs, and operations"),
            ("Resource group > Export template", "The generated ARM representation and limitations"),
            ("Storage account > Overview", "The resource produced from Bicep"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal",
        ],
        "Bicep compiles to ARM JSON, what-if predicts control-plane changes, and exported/decompiled templates require human review rather than being treated as pristine source.",
    ),
    "11": s(
        "11",
        "Manage VM lifecycle, size, disks, and host encryption",
        "Azure CLI",
        "moderate",
        120,
        "Virtual Machine Contributor and Network Contributor on the lab resource group",
        "Create a Linux VM with a managed OS disk, data disk, secure networking, encryption at host when the selected size supports it, then stop, resize, detach, reattach, and validate disk state.",
        ["resource group", "virtual network", "network security group", "network interface", "Linux virtual machine", "managed data disk"],
        ["Microsoft.Compute", "Microsoft.Network"],
        [],
        [
            "Create a VNet, subnet, NSG, NIC, and Linux VM without an inbound public management port.",
            "Enable encryption at host only after the subscription feature and selected VM size are confirmed.",
            "Create, attach, detach, and reattach a managed data disk using its exact resource ID.",
            "Deallocate and resize the VM to a validated alternative SKU, then return it to the intended state.",
        ],
        ["Microsoft.Compute/virtualMachines", "Microsoft.Compute/disks", "Microsoft.Network/virtualNetworks"],
        [
            ("Virtual machine > Overview", "VM size, power state, and availability metadata"),
            ("Virtual machine > Disks", "OS/data disk attachment and caching"),
            ("Virtual machine > Configuration", "Encryption at host state when supported"),
            ("Virtual machine > Size", "Available resize choices and current SKU"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli",
            "https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm",
            "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal",
            "https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-host-based-encryption-cli",
        ],
        "VM resize can require deallocation, managed disks have independent lifecycles, and encryption at host depends on subscription registration, region, and VM size support.",
    ),
    "12": s(
        "12",
        "Design VM resilience, scale sets, and mobility",
        "Az PowerShell",
        "elevated",
        150,
        "Virtual Machine Contributor, Network Contributor, and move permissions on source and destination scopes",
        "Compare availability sets and zones, deploy a small flexible VM scale set, inspect autoscale and upgrade settings, validate a resource-group move, and plan regional mobility without claiming a cross-region copy occurred.",
        ["resource group", "availability set", "zonal VM metadata", "flexible VM scale set", "autoscale setting"],
        ["Microsoft.Compute", "Microsoft.Insights", "Microsoft.Network", "Microsoft.Resources"],
        ["Az.Accounts", "Az.Resources", "Az.Network", "Az.Compute", "Az.Monitor"],
        [
            "Create an availability set and compare its fault/update-domain model with availability zones.",
            "Deploy a small flexible orchestration VM scale set with an explicit instance count and upgrade policy.",
            "Configure bounded autoscale rules and inspect instance protection and health behavior.",
            "Use move validation for a destination resource group and document the different process required for another region or subscription.",
        ],
        ["Microsoft.Compute/virtualMachineScaleSets", "Microsoft.Compute/availabilitySets"],
        [
            ("Virtual machine scale set > Overview", "Orchestration mode, instance count, and zones"),
            ("Virtual machine scale set > Scaling", "Manual capacity and autoscale bounds"),
            ("Availability set > Overview", "Fault and update domain configuration"),
            ("Resource group > Move", "Move validation results or documented dependency blockers"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets",
            "https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview",
            "https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview",
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription",
            "https://learn.microsoft.com/en-us/azure/resource-mover/tutorial-move-region-virtual-machines",
        ],
        "Availability sets, zones, scale sets, and regional moves solve different resilience or mobility problems and have distinct dependency and cost models.",
    ),
    "13": s(
        "13",
        "Publish images with ACR and run Azure Container Instances",
        "Azure CLI",
        "low",
        105,
        "Contributor on the lab resource group",
        "Create a Basic Azure Container Registry, import a Microsoft sample image without local Docker, deploy it to Azure Container Instances with bounded CPU and memory, inspect logs and restart policy, then remove the dedicated resource group.",
        ["resource group", "Basic container registry", "container group"],
        ["Microsoft.ContainerInstance", "Microsoft.ContainerRegistry"],
        [],
        [
            "Create a globally unique Basic ACR with the admin account disabled.",
            "Import a public Microsoft sample image and inspect repository and tag metadata.",
            "Create an ACI container group using a managed identity or time-bounded registry authentication path.",
            "Inspect CPU, memory, restart policy, events, logs, and current container state.",
        ],
        ["Microsoft.ContainerRegistry/registries", "Microsoft.ContainerInstance/containerGroups"],
        [
            ("Container registry > Repositories", "Imported repository, tag, and digest"),
            ("Container instance > Containers", "Image, resources, restart policy, and status"),
            ("Container instance > Logs", "Application output from the running sample"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli",
            "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images",
            "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart",
            "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups",
        ],
        "ACR stores image artifacts and ACI runs container groups; registry admin credentials are not required when managed identities or scoped tokens are available.",
    ),
    "14": s(
        "14",
        "Deploy and scale Azure Container Apps",
        "Azure CLI",
        "low",
        120,
        "Contributor on the lab resource group",
        "Create a Log Analytics-backed Container Apps environment, deploy a public sample app, configure ingress, revisions, min/max replicas, and an HTTP scale rule, then observe revision and replica behavior.",
        ["resource group", "Log Analytics workspace", "Container Apps environment", "container app"],
        ["Microsoft.App", "Microsoft.OperationalInsights"],
        [],
        [
            "Verify the containerapp Azure CLI extension and required provider registrations.",
            "Create a managed environment and deploy a sample app with external ingress.",
            "Create a new revision by changing an environment variable and split traffic deliberately.",
            "Configure bounded HTTP scaling and compare replicas, revisions, and provisioning state.",
        ],
        ["Microsoft.App/managedEnvironments", "Microsoft.App/containerApps"],
        [
            ("Container App > Overview", "Application URL, environment, and provisioning state"),
            ("Container App > Revisions and replicas", "Active revisions, traffic, and replicas"),
            ("Container App > Scale", "Minimum, maximum, and HTTP scaling rule"),
            ("Container App > Log stream", "Runtime output from a selected replica"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/container-apps/get-started",
            "https://learn.microsoft.com/en-us/azure/container-apps/revisions",
            "https://learn.microsoft.com/en-us/azure/container-apps/scale-app",
            "https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview",
        ],
        "Container Apps revisions are immutable deployment snapshots, while replicas scale within an active revision according to minimum, maximum, and event rules.",
    ),
    "15": s(
        "15",
        "Scale App Service and operate deployment slots",
        "Az PowerShell",
        "low",
        120,
        "Website Contributor and Monitoring Contributor on the lab resource group",
        "Create a Linux App Service plan and web app, configure plan capacity and autoscale, create a staging slot with slot-specific settings, warm it, swap it, and verify production and staging state.",
        ["resource group", "App Service plan", "web app", "deployment slot", "autoscale setting"],
        ["Microsoft.Insights", "Microsoft.Web"],
        ["Az.Accounts", "Az.Resources", "Az.Websites", "Az.Monitor"],
        [
            "Create a Linux App Service plan and web app with deterministic names.",
            "Scale the plan manually and configure bounded CPU-based autoscale where the SKU supports it.",
            "Create a staging slot and mark an application setting as a deployment-slot setting.",
            "Warm and swap staging into production, then verify which settings followed content and which remained sticky.",
        ],
        ["Microsoft.Web/serverfarms", "Microsoft.Web/sites", "Microsoft.Insights/autoscalesettings"],
        [
            ("App Service plan > Scale out", "Manual capacity and autoscale configuration"),
            ("App Service > Deployment slots", "Production and staging slots"),
            ("Deployment slot > Configuration", "Slot-specific application settings"),
            ("App Service > Activity log", "Slot swap operation and result"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/app-service/quickstart-powershell",
            "https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up",
            "https://learn.microsoft.com/en-us/azure/app-service/manage-scale-per-app",
            "https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots",
        ],
        "App Service plan scale affects workers shared by apps, while deployment slots isolate deployable content and selected sticky configuration before a controlled swap.",
    ),
    "16": s(
        "16",
        "Configure App Service TLS, DNS, backup, and networking",
        "Azure CLI",
        "moderate",
        150,
        "Website Contributor, Network Contributor, and Storage Account Contributor; control of the DNS zone and certificate for gated paths",
        "Create a web app, storage-backed backup target, and VNet integration subnet; inspect TLS settings, then map an owned DNS name and bind a certificate only when external DNS and certificate prerequisites are supplied.",
        ["resource group", "App Service plan", "web app", "storage account", "virtual network integration subnet", "optional custom hostname and TLS binding"],
        ["Microsoft.Network", "Microsoft.Storage", "Microsoft.Web"],
        [],
        [
            "Create an App Service plan and web app with HTTPS-only and minimum TLS 1.2.",
            "Create a delegated integration subnet and configure regional VNet integration.",
            "Create a private backup container and configure an App Service backup schedule without exposing its SAS.",
            "Validate the DNS TXT/CNAME records and bind AZ104_CUSTOM_HOSTNAME and AZ104_CERTIFICATE_PATH only when supplied.",
        ],
        ["Microsoft.Web/serverfarms", "Microsoft.Web/sites", "Microsoft.Storage/storageAccounts", "Microsoft.Network/virtualNetworks"],
        [
            ("App Service > Configuration > General settings", "HTTPS-only and minimum inbound TLS"),
            ("App Service > Networking", "Regional VNet integration"),
            ("App Service > Backups", "Backup destination and schedule with secrets hidden"),
            ("App Service > Custom domains", "Validated custom hostname and TLS binding when gated inputs exist"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings",
            "https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain",
            "https://learn.microsoft.com/en-us/azure/app-service/manage-backup",
            "https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration",
        ],
        "Custom hostnames prove DNS control, certificate bindings prove TLS identity, VNet integration governs outbound connectivity, and backups require protected storage access.",
        "Custom DNS and certificate steps require AZ104_CUSTOM_HOSTNAME plus an owned DNS zone and an authorized certificate; they remain gated otherwise.",
    ),
    "17": s(
        "17",
        "Create VNets, subnets, peerings, and public IPs",
        "Az PowerShell",
        "low",
        105,
        "Network Contributor on the lab resource group",
        "Create two non-overlapping virtual networks with application and management subnets, peer them in both directions, create a Standard static public IP, and validate address spaces, peering state, and allocation properties.",
        ["resource group", "two virtual networks", "four subnets", "bidirectional peering", "Standard public IP"],
        ["Microsoft.Network"],
        ["Az.Accounts", "Az.Resources", "Az.Network"],
        [
            "Create hub and spoke address spaces that do not overlap and subdivide them into purpose-specific subnets.",
            "Create both sides of VNet peering and interpret Connected, Initiated, and Disconnected states.",
            "Create a zone-redundant Standard static public IP where supported.",
            "Compare private address planning, public IP allocation, DNS labels, and effective peering routes.",
        ],
        ["Microsoft.Network/virtualNetworks", "Microsoft.Network/publicIPAddresses"],
        [
            ("Virtual network > Address space", "Non-overlapping hub and spoke prefixes"),
            ("Virtual network > Subnets", "Application and management subnet boundaries"),
            ("Virtual network > Peerings", "Connected bidirectional peerings"),
            ("Public IP address > Overview", "Standard SKU, static allocation, and zones"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell",
            "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering",
            "https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses",
        ],
        "VNet peering is non-transitive and requires compatible address spaces and two directional peering objects, while Standard public IPs are secure by default until an NSG permits traffic.",
    ),
    "18": s(
        "18",
        "Control traffic with routes, NSGs, ASGs, and effective rules",
        "Azure CLI",
        "low",
        120,
        "Network Contributor on the lab resource group",
        "Create an application network, NSG, application security groups, route table, and test NICs; apply narrowly scoped rules, inspect effective routes and security rules, and diagnose a deliberately blocked flow.",
        ["resource group", "virtual network", "network security group", "two application security groups", "route table", "test network interfaces"],
        ["Microsoft.Network"],
        [],
        [
            "Create frontend and backend ASGs and associate test NIC configurations.",
            "Create ordered NSG rules that allow only the intended application flow and preserve default deny behavior.",
            "Associate a route table containing a documented user-defined route with the application subnet.",
            "Use effective NSG and route queries plus Network Watcher diagnostics to explain a blocked connection.",
        ],
        ["Microsoft.Network/networkSecurityGroups", "Microsoft.Network/applicationSecurityGroups", "Microsoft.Network/routeTables", "Microsoft.Network/virtualNetworks"],
        [
            ("Network security group > Security rules", "Custom priorities, source ASG, destination ASG, and port"),
            ("Network interface > Effective security rules", "Combined subnet and NIC rule evaluation"),
            ("Network interface > Effective routes", "System and user-defined route selection"),
            ("Network Watcher > IP flow verify", "Allow or deny result and matching rule"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group",
            "https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups",
            "https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table",
            "https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview",
        ],
        "NSG evaluation uses priority and direction, ASGs replace hard-coded IP membership, and route selection uses longest-prefix matching before connectivity diagnostics explain the result.",
    ),
})


def load_blueprint() -> dict:
    return yaml.safe_load((ROOT / "curriculum" / "blueprint.yml").read_text(encoding="utf-8"))


def curriculum_index() -> tuple[dict[str, dict], dict[str, str]]:
    """Return objective records and domain names keyed by objective/domain ID."""
    blueprint = load_blueprint()
    objectives: dict[str, dict] = {}
    domains: dict[str, str] = {}
    for item in blueprint.get("foundationObjectives", []):
        objectives[item["id"]] = {**item, "domainId": "FD", "domainName": "Foundation and lab safety"}
    for domain in blueprint["domains"]:
        domains[domain["id"]] = domain["name"]
        for group in domain["groups"]:
            for item in group["objectives"]:
                objectives[item["id"]] = {
                    **item,
                    "domainId": domain["id"],
                    "domainName": domain["name"],
                    "groupName": group["name"],
                }
    return objectives, domains


def slug_and_objectives(number: str, objectives: dict[str, dict]) -> tuple[str, list[dict]]:
    slugs = sorted(
        {
            slug
            for objective in objectives.values()
            for slug in objective.get("labs", [])
            if slug.startswith(f"{number}-")
        }
    )
    if len(slugs) != 1:
        raise ValueError(f"Expected one slug for Lab {number}; found {slugs}")
    slug = slugs[0]
    records = [objective for objective in objectives.values() if slug in objective.get("labs", [])]
    if not records:
        raise ValueError(f"No objectives mapped to {slug}")
    return slug, records


def yaml_text(data: object) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = content.replace("\r\n", "\n").split("\n")
    normalized = "\n".join(line.rstrip() for line in lines).rstrip() + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(normalized)


def safe_id(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


# Checkpoint that each authored portal capture evidences, per generated lab.
PORTAL_CHECKPOINT_MAP: dict[str, list[int]] = {
    "02": [1, 2, 4],
    "03": [3, 4, 4],
    "04": [2, 3, 4],
    "05": [2, 3, 4, 4],
    "06": [1, 2, 3, 4],
    "07": [3, 4, 4, 4],
    "08": [2, 3, 4, 4],
    "09": [1, 2, 2, 4],
    "10": [3, 4, 3],
    "11": [1, 3, 2, 4],
    "12": [2, 3, 1, 4],
    "13": [2, 3, 4],
    "14": [2, 3, 4, 4],
    "15": [2, 3, 3, 4],
    "16": [1, 2, 3, 4],
    "17": [1, 1, 2, 3],
    "18": [2, 4, 4, 4],
    "19": [2, 4, 4, 1],
    "20": [2, 1, 4, 3],
    "21": [2, 3, 3, 4],
    "22": [4, 3, 2, 4],
    "23": [3, 1, 4, 4],
    "24": [2, 3, 1, 4],
    "25": [3, 3, 4, 3],
    "26": [1, 2, 3, 4],
    "27": [3, 2, 3, 4],
}


def portal_captures(number: str, spec: dict) -> list[dict]:
    checkpoints = PORTAL_CHECKPOINT_MAP[number]
    if len(checkpoints) != len(spec["portal"]):
        raise ValueError(f"Lab {number}: portal capture and checkpoint-map lengths differ")
    captures: list[dict] = []
    for index, ((blade, evidence), checkpoint) in enumerate(zip(spec["portal"], checkpoints), 1):
        segments = [safe_id(part) for part in blade.split(">")]
        name = "-".join(segments[-2:]) if len(segments) > 1 else segments[0]
        captures.append(
            {
                "file": f"{index:02d}-{name}.png",
                "checkpoint": checkpoint,
                "portalBlade": blade.strip(),
                "evidenceShown": evidence.strip(),
                "captureDate": None,
                "region": None,
                "redactions": [],
                "portalConfirmed": False,
                "status": "pending",
            }
        )
    return captures


def render_portal_manifest(number: str, spec: dict) -> dict:
    return {
        "schemaVersion": "1.0",
        "labId": f"LAB-{number}",
        "status": "pending",
        "source": (
            "Every capture must come from a signed-in session of the real Azure Portal "
            "(https://portal.azure.com) against the disposable lab environment; fabricated or "
            "placeholder images are forbidden."
        ),
        "captures": portal_captures(number, spec),
    }


def render_images_readme(number: str) -> str:
    return f"""# Lab {number} portal evidence

This folder holds sanitized Azure Portal screenshots for Lab {number} and the manifest that tracks them.

## Contract

- [portal/manifest.yml](portal/manifest.yml) lists every planned capture with its checkpoint, blade, and expected evidence.
- A PNG enters this folder only after an authorized live run and full sanitization; fabricated or placeholder images are forbidden.
- Statuses progress `pending` → `captured` → `sanitized` → `verified`; raw (`captured`) files must never be committed.
- Two to five captures per lab, PNG only, at most 1920 px wide, and roughly 500 KB or less after optimization.

## Sanitization checklist

Before a capture may be recorded as `sanitized`:

1. Crop to the relevant blade and remove browser chrome, bookmarks, other tabs, and unrelated resources.
2. Irreversibly redact tenant and subscription GUIDs, account names, email addresses and UPNs, tokens, keys, public IPs, and billing details.
3. Strip all image metadata (EXIF, XMP, and text chunks) and re-encode as an optimized PNG.
4. Update the matching manifest entry: capture date, region (or `not-applicable` for tenant-plane blades), the redactions performed, `portalConfirmed: true`, and the new status.
5. Record `verified` only after a second manual review confirms no identifying content remains.

Repository-wide rules live in [docs/evidence-handling.md](../../../docs/evidence-handling.md).
"""


def command_lane(spec: dict) -> str:
    return "cli" if "CLI" in spec["surface"] else "powershell"


def track_name(spec: dict) -> str:
    if spec["surface"] == "Microsoft Graph PowerShell":
        return "powershell-graph"
    if "CLI" in spec["surface"] and "Bicep" in spec["surface"]:
        return "azure-cli-bicep"
    if "CLI" in spec["surface"]:
        return "azure-cli"
    return "az-powershell"


def difficulty_for(number: int) -> str:
    if number <= 9:
        return "foundational"
    if number <= 23:
        return "intermediate"
    return "advanced"


def make_questions(number: str, spec: dict, objective_records: list[dict]) -> list[dict]:
    """Create ten original, source-backed checks with balanced answer positions."""
    difficulties = ["foundational"] * 3 + ["applied"] * 5 + ["advanced"] * 2
    correct_positions = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
    objective_ids = [item["id"] for item in objective_records]
    titles = [item["title"] for item in objective_records]
    resources = ", ".join(spec["resources"][:3]) or "the recorded tenant objects"
    expected = ", ".join(spec["expected_types"][:2]) or "the exact recorded object IDs"
    gate = spec["gate"]
    sources = spec["sources"]

    templates = [
        (
            f"Which statement best captures the key design principle for {spec['title'].lower()}?",
            spec["fact"],
            "Every related control is interchangeable, so choose whichever command is shortest.",
            "A command surface automatically supplies any missing authorization or configuration.",
            "Cleanup evidence is unnecessary when a resource group has a recognizable name.",
            f"The lab's central distinction is: {spec['fact']}",
        ),
        (
            f"You must begin the hands-on path for '{titles[0]}'. Which action matches the reviewed lab sequence?",
            spec["actions"][0],
            "Delete similarly named resources before recording the current subscription.",
            "Change the active tenant automatically and continue without displaying the new context.",
            "Infer configuration from resource names without querying the live control plane.",
            f"The first implementation checkpoint is: {spec['actions'][0]}",
        ),
        (
            f"Which authorization statement is appropriate before creating {resources} in this lab?",
            f"Confirm the active context and obtain only the declared role boundary: {spec['role']}",
            "Subscription Reader is sufficient for every create, update, role, policy, and recovery operation.",
            "A local administrator account automatically grants Microsoft Entra and Azure permissions.",
            "Skip authorization checks because all resources use an AZ104 naming prefix.",
            f"The documented permission boundary is {spec['role']}",
        ),
        (
            f"The setup command for Lab {number} is run without its execution switch. What should happen?",
            "It should print the intended resources, context, cost class, and gates without changing Azure.",
            "It should deploy everything and ask for confirmation only before cleanup.",
            "It should log in interactively and select the first available subscription.",
            "It should delete any older run that shares the same lab number.",
            "Preview-first behavior makes the default invocation non-mutating; execution requires an explicit switch.",
        ),
        (
            f"Which validation evidence most directly proves the baseline resource boundary for Lab {number}?",
            f"Query the exact recorded scope and verify the intended resource/object types, including {expected}.",
            "Search the whole tenant by display-name prefix and accept the first match.",
            "Treat a successful setup process exit code as proof of every data-plane and relationship requirement.",
            "Verify only that an Azure subscription exists.",
            "Validation must use the recorded scope and test the intended state independently of setup.",
        ),
        (
            f"A learner reaches the externally gated checkpoint in Lab {number}. What is the safest response?",
            f"Stop that branch unless its prerequisites are explicitly satisfied: {gate}",
            "Invent a placeholder tenant, email address, domain, or production target and continue.",
            "Broaden the assignment to subscription scope so the gate no longer applies.",
            "Mark the checkpoint as passed because the offline tests succeeded.",
            f"The live-only gate is explicit and must not be guessed: {gate}",
        ),
        (
            f"Which command-side evidence best supports the first completed checkpoint in Lab {number}?",
            f"Run the independent validator and retain redacted structured output for the exact recorded scope after: {spec['actions'][0]}",
            "Copy a successful command from an unrelated tenant and treat it as this run's evidence.",
            "Record access tokens and keys so another learner can replay the same session.",
            "Use the setup process exit code alone without querying resource state.",
            "Command evidence must come from the recorded run, exclude secrets and identifiers, and prove the intended state independently of setup.",
        ),
        (
            f"During cleanup of Lab {number}, several similarly named resources exist. Which targeting method is correct?",
            "Use the exact IDs and run metadata recorded before creation, verify the lab tags, then delete only that boundary.",
            "Delete every resource whose name contains az104.",
            "Delete the active subscription to guarantee that no lab resources remain.",
            "Use creation timestamps alone and remove the oldest matching resources.",
            "Recorded immutable IDs plus ownership tags provide the narrow, auditable cleanup boundary.",
        ),
        (
            f"Setup completed for Lab {number}, but one required state check fails. What is the best break/fix approach?",
            "Inspect the failing check and exact recorded resource, repair the smallest identified cause, then rerun validation.",
            "Rerun setup repeatedly with new names until one run reports no error.",
            "Edit validation.json so the failed status reads pass.",
            "Disable all policies, locks, NSGs, and monitoring controls in the subscription.",
            "Evidence-led repair limits drift and preserves the diagnostic value of an independent validator.",
        ),
        (
            f"Which completion claim is valid immediately after this repository's offline tests pass for Lab {number}?",
            "The documentation, schemas, script contracts, assessments, diagrams, and fixtures are offline-validated; live Azure state remains pending until executed.",
            "Every command has been proven in every Azure region and tenant type.",
            "The lab is live-verified even if no subscription was used.",
            "Any pending gated checkpoint can be treated as successfully completed.",
            "Offline validation proves artifact quality and safety contracts, not live service behavior.",
        ),
    ]

    questions: list[dict] = []
    for index, template in enumerate(templates):
        stem, correct, wrong1, wrong2, wrong3, explanation = template
        correct_position = correct_positions[index]
        wrongs = iter([wrong1, wrong2, wrong3])
        options = {letter: correct if letter == correct_position else next(wrongs) for letter in "ABCD"}
        objective_id = objective_ids[index % len(objective_ids)]
        # Include a second objective on scenario questions while retaining full primary coverage.
        mapped = [objective_id]
        if index in {7, 8, 9} and len(objective_ids) > 1:
            mapped.append(objective_ids[(index + 1) % len(objective_ids)])
        distractors = {
            letter: (
                f"Correct. {explanation}"
                if letter == correct_position
                else "This choice either exceeds the declared scope, skips required evidence, or confuses offline validation with live Azure state."
            )
            for letter in "ABCD"
        }
        questions.append(
            {
                "id": f"LAB{number}-Q{index + 1:02d}",
                "objectiveIds": mapped,
                "difficulty": difficulties[index],
                "stem": stem,
                "options": options,
                "correctOption": correct_position,
                "explanation": explanation,
                "distractorExplanations": distractors,
                "sourceUrls": [sources[index % len(sources)]],
                "lastVerified": REVIEW_DATE,
            }
        )
    return questions


def render_questions(number: str, title: str, questions: list[dict]) -> tuple[str, str]:
    question_lines = [f"# Lab {number} knowledge check", "", title, "", "Choose one answer for each question before opening the answer key.", ""]
    answer_lines = [f"# Lab {number} answer key", "", f"Return to [the questions](QUESTIONS.md).", ""]
    for index, question in enumerate(questions, 1):
        question_lines.extend([f"## {index}. {question['stem']} (`{question['id']}`)", ""])
        for letter, option in question["options"].items():
            question_lines.append(f"- {letter}. {option}")
        question_lines.append("")
        answer_lines.extend(
            [
                f"## {index}. {question['correctOption']} (`{question['id']}`)",
                "",
                question["explanation"],
                "",
                f"Objectives: {', '.join(question['objectiveIds'])}",
                "",
                "Why the other choices do not fit:",
                "",
            ]
        )
        for letter, explanation in question["distractorExplanations"].items():
            if letter != question["correctOption"]:
                answer_lines.append(f"- **{letter}:** {explanation}")
        answer_lines.extend(["", f"Source: <{question['sourceUrls'][0]}>", ""])
    return "\n".join(question_lines), "\n".join(answer_lines)


def make_lab_metadata(number: str, slug: str, spec: dict, objectives: list[dict], status: str) -> dict:
    lane = command_lane(spec)
    domain_names = list(dict.fromkeys(item["domainName"] for item in objectives))
    is_tenant = spec["scope"] == "tenant"
    billable = [] if spec["cost"] == "none" else spec["resources"]
    metadata = {
        "id": f"LAB-{number}",
        "slug": slug,
        "title": spec["title"],
        "blueprintVersion": BLUEPRINT_DATE,
        "domain": " / ".join(domain_names),
        "objectives": [item["id"] for item in objectives],
        "track": track_name(spec),
        "status": status,
        "testedToolVersions": (
            {
                "azureCli": "2.88.0",
                "bash": "5.x (Git for Windows lane)",
                "jq": ">=1.6",
            }
            if lane == "cli"
            else {
                "powershell": ">=7.4",
                "modules": spec["modules"],
            }
        ),
        "estimatedMinutes": spec["minutes"],
        "difficulty": difficulty_for(int(number)),
        "cost": {
            "class": spec["cost"],
            "billableResources": billable,
            "notes": (
                "No Azure resource charge is expected, but tenant licensing can still gate features."
                if is_tenant
                else "Pricing, free allowances, quotas, and regional availability can change. Review the Azure pricing calculator before execution and clean up immediately."
            ),
        },
        "permissions": {
            "azureRbacRoles": [] if is_tenant else [spec["role"]],
            "entraRoles": [spec["role"]] if is_tenant else [],
            "graphScopes": spec["modules"] if is_tenant else [],
        },
        "prerequisites": [
            "A disposable non-production Azure environment",
            "An active context that matches the explicitly supplied tenant and subscription",
            f"The command surface and dependencies for {spec['surface']}",
            f"Authorization boundary: {spec['role']}",
            f"External gate review: {spec['gate']}",
        ],
        "providers": {
            "observed": spec["providers"],
            "registeredByLab": [],
        },
        "regions": {
            "applicable": not is_tenant,
            "primary": "supplied at execution time" if not is_tenant else None,
            "secondary": "required only for multi-region checkpoints" if number in {"08", "12", "25", "27"} else None,
        },
        "creates": {
            "azureResources": [] if is_tenant else spec["resources"],
            "entraObjects": spec["resources"] if is_tenant else [],
            "localArtifacts": [
                ".state/<run-id>/run.json",
                ".state/<run-id>/validation.json",
            ],
        },
        "tenantScopedChanges": spec["resources"] if is_tenant else [],
        "externalRequirements": [] if spec["gate"].startswith("None beyond") else [spec["gate"]],
        "validation": {
            "commandLanes": [f"scripts/{lane}/" + ("validate.sh" if lane == "cli" else "Validate.ps1")],
            "output": ".state/<run-id>/validation.json",
            "statuses": ["pass", "fail", "warning", "skipped"],
            "liveExecutionRequiredForLiveVerified": True,
        },
        "cleanup": {
            "azureDeletion": "none" if is_tenant else "exact recorded resource-group ID after tag verification",
            "entraDeletion": "exact recorded object IDs only" if is_tenant else "none",
            "reportOnlyByDefault": True,
            "requiresExecuteFlag": True,
            "residualAuditRequired": True,
        },
        "screenshots": {
            "status": "pending",
            "manifest": "images/portal/manifest.yml",
        },
        "lastOfflineValidated": REVIEW_DATE if status == "offline-validated" else None,
        "lastLiveVerified": None,
    }
    return metadata


def render_readme(number: str, slug: str, spec: dict, objectives: list[dict]) -> str:
    lane = command_lane(spec)
    script_ext = "sh" if lane == "cli" else "ps1"
    names = {
        "preflight": "preflight.sh" if lane == "cli" else "Preflight.ps1",
        "setup": "setup.sh" if lane == "cli" else "Setup.ps1",
        "validate": "validate.sh" if lane == "cli" else "Validate.ps1",
        "cleanup": "cleanup.sh" if lane == "cli" else "Cleanup.ps1",
    }
    if lane == "cli":
        preview = f"./scripts/cli/{names['setup']} --subscription-id <subscription-id> --location <region> --run-id az104l{number}-01"
        execute = preview + " --execute"
        validate = f"./scripts/cli/{names['validate']} --subscription-id <subscription-id> --run-id az104l{number}-01"
        cleanup_preview = f"./scripts/cli/{names['cleanup']} --subscription-id <subscription-id> --run-id az104l{number}-01"
        cleanup_execute = cleanup_preview + " --execute"
    else:
        subscription = "" if spec["scope"] == "tenant" else " -SubscriptionId <subscription-id>"
        preview = f"pwsh ./scripts/powershell/{names['setup']} -RunId az104l{number}-01{subscription} -Location <region>"
        execute = preview + " -Execute"
        validate = f"pwsh ./scripts/powershell/{names['validate']} -RunId az104l{number}-01{subscription}"
        cleanup_preview = f"pwsh ./scripts/powershell/{names['cleanup']} -RunId az104l{number}-01{subscription}"
        cleanup_execute = cleanup_preview + " -Execute"

    objective_rows = "\n".join(f"| `{item['id']}` | {item['title']} |" for item in objectives)
    resource_rows = "\n".join(f"| {index} | {resource} |" for index, resource in enumerate(spec["resources"], 1))
    action_sections = []
    for index, action in enumerate(spec["actions"], 1):
        action_sections.extend(
            [
                f"### Checkpoint {index}: {action.split('.')[0]}",
                "",
                action,
                "",
                "Evidence to retain:",
                "",
                f"- The command output or exact resource/object ID for checkpoint {index}.",
                "- A positive assertion proving the intended state.",
                "- A negative assertion showing that broader or anonymous access was not introduced.",
                "- Any asynchronous operation state, timestamp, and final result.",
                "",
            ]
        )
    actions_block = "\n".join(action_sections)
    portal_rows = "\n".join(
        f"| `{item['file']}` | {item['checkpoint']} | {item['portalBlade']} | {item['evidenceShown']} |"
        for item in portal_captures(number, spec)
    )
    providers = ", ".join(f"`{provider}`" for provider in spec["providers"]) or "No Azure resource provider; tenant/Graph plane only"
    modules = ", ".join(f"`{module}`" for module in spec["modules"]) or "No extra PowerShell modules"
    return f"""# Lab {number}: {spec['title']}

> Status: **offline-authored and contract-tested; live Azure verification is pending.**

{spec['summary']}

This folder is self-contained. It does not depend on another lab's runtime state. Use a disposable environment, keep the generated run manifest, and never substitute a production scope for a missing lab prerequisite.

## Learning objectives

| ID | Microsoft AZ-104 objective |
|---|---|
{objective_rows}

Blueprint source: [Microsoft AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), effective {BLUEPRINT_DATE}.

## Architecture

![Lab {number} architecture](diagrams/architecture.svg)

The editable Mermaid source is [diagrams/architecture.mmd](diagrams/architecture.mmd). The diagram describes the learning boundary, not a production reference architecture.

## Scenario and outcome

You are the Azure administrator for a training environment. Your task is to implement the smallest isolated configuration that demonstrates the mapped exam objectives, validate it independently, capture sanitized evidence, and remove only what this run recorded.

The key design idea is: **{spec['fact']}**

## Time, cost, and permissions

| Item | Value |
|---|---|
| Estimated time | {spec['minutes']} minutes |
| Cost class | `{spec['cost']}` |
| Command surface | {spec['surface']} |
| Required boundary | {spec['role']} |
| External/live gate | {spec['gate']} |

Cost is not a fixed promise. Check current pricing, free allowances, quotas, and regional availability before using `--execute` or `-Execute`. Labs marked moderate or elevated should be cleaned up in the same study session.

## Resources and dependencies

| # | Intended resource or object |
|---:|---|
{resource_rows}

- Resource providers observed by preflight: {providers}
- PowerShell modules used when applicable: {modules}
- Repository state: `.state/<run-id>/run.json` and `.state/<run-id>/validation.json`
- Secrets, access keys, SAS tokens, generated passwords, and shared keys must remain in memory and must not enter the manifest, command evidence, or Git history.

## Safety contract

1. Preflight is read-only. It does not sign in, register providers, or switch the active context.
2. Setup is preview-only unless the explicit execution switch is supplied.
3. State is written before the first cloud mutation and updated with exact returned IDs.
4. Validation reads live state independently; it does not repair a failed configuration.
5. Cleanup previews exact targets, verifies run ownership, then requires the explicit execution switch.
6. Tenant-wide, DNS, licensing, notification, failover, and policy gates are never guessed.

## Before you begin

- Use a disposable non-production tenant/subscription and verify the displayed tenant and subscription IDs.
- Install the declared command surface and supporting dependencies.
- Confirm the role boundary above at the smallest possible scope.
- Review provider registration and quota output; preflight reports requirements but does not register providers.
- Read the external gate. An unavailable gate is a documented `skipped` checkpoint, not a pass.
- Choose a unique run ID matching `^[a-z0-9-]+$`, such as `az104l{number}-01`.

## Run the lab

Run these commands from this lab folder. The examples intentionally use placeholders rather than silently reading an arbitrary subscription.

### 1. Preview

```{script_ext}
{preview}
```

Review the context, names, tags, cost class, providers, and gated branches printed by the script.

### 2. Execute the approved baseline

```{script_ext}
{execute}
```

The script records its run before creating resources. If a cloud operation fails partway through, keep the state directory and use validation plus cleanup against that exact run.

### 3. Complete and reason through the checkpoints

{actions_block}
### 4. Validate independently

```{script_ext}
{validate}
```

Inspect `.state/az104l{number}-01/validation.json`. A `pass` applies only to checks that could be executed. A gated or asynchronous path must remain `warning` or `skipped` until its evidence exists.

Positive checks should prove the intended resources, configuration, relationships, or health. Negative checks should prove that anonymous access, excess scope, accidental inheritance, unresolved DNS, unhealthy probes, or unrecorded resources were not introduced where the scenario forbids them.

## Portal evidence

Portal screenshots are planned evidence captured only during an authorized live run. Until then every entry in [images/portal/manifest.yml](images/portal/manifest.yml) stays `pending`, and no placeholder image is committed. Capture and sanitization rules live in [images/README.md](images/README.md).

| Planned file | Checkpoint | Portal blade | Evidence |
|---|---:|---|---|
{portal_rows}

## Break/fix exercise

1. Pick one reversible configuration created inside the recorded lab boundary.
2. Record the exact ID and current value.
3. Introduce one bounded mismatch; do not weaken a tenant-wide or production control.
4. Run validation and connect the failed check to an exact CLI/PowerShell query and the machine-readable validation result.
5. Repair only the identified setting, rerun validation, and compare the evidence.

The [solution notes](solution/README.md) provide a diagnostic sequence without hiding the reasoning behind an opaque repair script.

## Cleanup

Preview cleanup first:

```{script_ext}
{cleanup_preview}
```

After verifying every printed target belongs to this run:

```{script_ext}
{cleanup_execute}
```

Run validation again after deletion. Some services use soft delete, retained recovery points, asynchronous deletion, or external DNS/tenant state; the cleanup report must distinguish active cleanup from retention and must list residual items instead of claiming success prematurely.

## Exam practice

- Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md) without opening the answer key.
- Review [assessment/ANSWERS.md](assessment/ANSWERS.md) and trace each explanation to its Microsoft Learn source.
- Revisit every mapped objective whose answer you could not justify from the resource state.

## Microsoft Learn sources

{chr(10).join(f'- [{url}]({url})' for url in spec['sources'])}

Last curriculum/source review: {REVIEW_DATE}. Azure interfaces and command modules evolve; confirm current syntax in the linked primary documentation before a live run.
"""


def render_diagram(number: str, spec: dict) -> tuple[str, str]:
    nodes = spec["resources"][:5] or ["Tenant objects"]
    mermaid_lines = [
        "flowchart LR",
        f'    A["Operator<br/>{html.escape(spec["surface"])}"] --> P["Preview and preflight"]',
        f'    P --> S["Recorded Lab {number} boundary"]',
    ]
    for index, resource in enumerate(nodes, 1):
        mermaid_lines.append(f'    S --> R{index}["{resource}"]')
    mermaid_lines.extend(
        [
            '    S --> V["Independent validation"]',
            '    V --> E["Sanitized evidence"]',
            '    V --> C["Previewed cleanup"]',
            "    classDef control fill:#e8f1ff,stroke:#2563eb,color:#102a43;",
            "    classDef resource fill:#e9f8ef,stroke:#16803a,color:#102a43;",
            "    class A,P,S,V,E,C control;",
            "    class R1,R2,R3,R4,R5 resource;" if len(nodes) >= 5 else "    class " + ",".join(f"R{i}" for i in range(1, len(nodes) + 1)) + " resource;",
        ]
    )
    width, height = 1040, max(390, 170 + 58 * len(nodes))
    boxes = []
    arrows = []
    start_y = 110
    for index, resource in enumerate(nodes):
        y = start_y + index * 58
        boxes.append(f'<rect x="500" y="{y}" width="470" height="40" rx="8" class="resource"/><text x="735" y="{y + 25}" text-anchor="middle">{html.escape(resource)}</text>')
        arrows.append(f'<path d="M 455 155 L 500 {y + 20}" class="arrow"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Lab {number} architecture</title>
<desc id="desc">Preview-first operator workflow, a recorded lab boundary, intended resources, independent validation, sanitized evidence, and scoped cleanup.</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#46647f"/></marker></defs>
<style>text{{font-family:Segoe UI,Arial,sans-serif;font-size:14px;fill:#102a43}} .control{{fill:#e8f1ff;stroke:#2563eb;stroke-width:2}} .resource{{fill:#e9f8ef;stroke:#16803a;stroke-width:2}} .arrow{{fill:none;stroke:#46647f;stroke-width:2;marker-end:url(#arrow)}}</style>
<rect width="100%" height="100%" fill="#ffffff"/>
<rect x="40" y="55" width="180" height="55" rx="8" class="control"/><text x="130" y="79" text-anchor="middle">Operator</text><text x="130" y="98" text-anchor="middle">{html.escape(spec['surface'])}</text>
<rect x="275" y="55" width="180" height="55" rx="8" class="control"/><text x="365" y="79" text-anchor="middle">Preview and preflight</text><text x="365" y="98" text-anchor="middle">read-only context check</text>
<path d="M220 82 L275 82" class="arrow"/>
<rect x="275" y="130" width="180" height="50" rx="8" class="control"/><text x="365" y="151" text-anchor="middle">Recorded Lab {number}</text><text x="365" y="170" text-anchor="middle">exact cleanup boundary</text>
<path d="M365 110 L365 130" class="arrow"/>
{''.join(boxes)}
{''.join(arrows)}
<rect x="40" y="215" width="180" height="50" rx="8" class="control"/><text x="130" y="237" text-anchor="middle">Independent validation</text><text x="130" y="256" text-anchor="middle">positive + negative</text>
<path d="M275 165 L220 230" class="arrow"/>
<rect x="40" y="290" width="180" height="50" rx="8" class="control"/><text x="130" y="312" text-anchor="middle">Evidence + cleanup</text><text x="130" y="331" text-anchor="middle">sanitized and scoped</text>
<path d="M130 265 L130 290" class="arrow"/>
</svg>'''
    return "\n".join(mermaid_lines), svg


def cli_preflight(number: str, spec: dict) -> str:
    providers = " ".join(spec["providers"])
    extra = "require_tool ssh-keygen" if number == "11" else ""
    return f'''#!/usr/bin/env bash
set -euo pipefail

SUBSCRIPTION_ID="${{AZURE_SUBSCRIPTION_ID:-}}"
LOCATION="${{AZURE_LOCATION:-}}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --location) LOCATION="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$SUBSCRIPTION_ID" ]] || {{ echo "Supply --subscription-id or AZURE_SUBSCRIPTION_ID." >&2; exit 2; }}
[[ -n "$LOCATION" ]] || {{ echo "Supply --location or AZURE_LOCATION." >&2; exit 2; }}

require_tool() {{ command -v "$1" >/dev/null 2>&1 || {{ echo "Missing required tool: $1" >&2; exit 3; }}; }}
require_tool az
require_tool jq
{extra}

ACCOUNT_JSON="$(az account show --output json)"
ACTIVE_SUBSCRIPTION="$(jq -r '.id' <<<"$ACCOUNT_JSON")"
ACTIVE_TENANT="$(jq -r '.tenantId' <<<"$ACCOUNT_JSON")"
[[ "$ACTIVE_SUBSCRIPTION" == "$SUBSCRIPTION_ID" ]] || {{
  echo "Context mismatch: active subscription is $ACTIVE_SUBSCRIPTION, expected $SUBSCRIPTION_ID." >&2
  echo "Select the intended context yourself; this script will not change it." >&2
  exit 4
}}

echo "Lab: LAB-{number}"
echo "Tenant: $ACTIVE_TENANT"
echo "Subscription: $ACTIVE_SUBSCRIPTION"
echo "Location: $LOCATION"
echo "Cost class: {spec['cost']}"
echo "Role boundary: {spec['role']}"

for provider in {providers}; do
  state="$(az provider show --namespace "$provider" --query registrationState --output tsv 2>/dev/null || true)"
  printf 'Provider %-38s %s\n' "$provider" "${{state:-Unavailable}}"
done

echo "Preflight is read-only. Register missing providers only after an explicit scope and cost review."
'''


def cli_setup(number: str, spec: dict) -> str:
    action = CLI_ACTIONS.get(number, "echo 'This lab uses guided checkpoints after the recorded baseline.'")
    secondary = "SECONDARY_LOCATION=\"${AZURE_SECONDARY_LOCATION:-}\""
    return f'''#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/../.." && pwd)"
SUBSCRIPTION_ID="${{AZURE_SUBSCRIPTION_ID:-}}"
LOCATION="${{AZURE_LOCATION:-}}"
{secondary}
RUN_ID=""
EXECUTE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --location) LOCATION="$2"; shift 2 ;;
    --secondary-location) SECONDARY_LOCATION="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    --execute) EXECUTE=true; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$SUBSCRIPTION_ID" && -n "$LOCATION" && -n "$RUN_ID" ]] || {{
  echo "Usage: $0 --subscription-id ID --location REGION --run-id RUN [--secondary-location REGION] [--execute]" >&2
  exit 2
}}
[[ "$RUN_ID" =~ ^[a-z0-9-]+$ ]] || {{ echo "Run ID must match ^[a-z0-9-]+$." >&2; exit 2; }}

RG="rg-az104-l{number}-${{RUN_ID}}"
SUFFIX="$(printf '%s' "$RUN_ID" | tr -cd 'a-z0-9' | tail -c 12)"
STATE_DIR="$LAB_ROOT/.state/$RUN_ID"
MANIFEST="$STATE_DIR/run.json"
EXPIRES_ON="$(date -u -d '+1 day' +%F 2>/dev/null || date -u +%F)"

echo "LAB-{number} plan"
echo "  subscription: $SUBSCRIPTION_ID"
echo "  location: $LOCATION"
echo "  resource group: $RG"
echo "  cost class: {spec['cost']}"
echo "  external gate: {spec['gate']}"
echo "  resources: {', '.join(spec['resources'])}"

if [[ "$EXECUTE" != true ]]; then
  echo "Preview only. Re-run with --execute after approving context, permissions, cost, and gates."
  exit 0
fi

"$LAB_ROOT/scripts/cli/preflight.sh" --subscription-id "$SUBSCRIPTION_ID" --location "$LOCATION"
[[ ! -e "$MANIFEST" ]] || {{ echo "State already exists at $MANIFEST; choose a new run ID." >&2; exit 5; }}
mkdir -p "$STATE_DIR"
TENANT_ID="$(az account show --query tenantId --output tsv)"
jq -n \
  --arg labId "LAB-{number}" --arg runId "$RUN_ID" --arg tenantId "$TENANT_ID" \
  --arg subscriptionId "$SUBSCRIPTION_ID" --arg location "$LOCATION" --arg rgName "$RG" \
  --arg createdAt "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  '{{labId:$labId,runId:$runId,tenantId:$tenantId,subscriptionId:$subscriptionId,location:$location,createdAt:$createdAt,status:"recorded-before-mutation",resourceGroup:{{name:$rgName,id:null}},resources:[],external:{{}}}}' >"$MANIFEST"

az group create --subscription "$SUBSCRIPTION_ID" --name "$RG" --location "$LOCATION" \
  --tags purpose=az104-lab labId={number} runId="$RUN_ID" expiresOn="$EXPIRES_ON" --output none
RG_ID="$(az group show --subscription "$SUBSCRIPTION_ID" --name "$RG" --query id --output tsv)"
jq --arg id "$RG_ID" '.resourceGroup.id=$id | .status="baseline-created"' "$MANIFEST" >"$MANIFEST.tmp"
mv -f "$MANIFEST.tmp" "$MANIFEST"

{action.strip()}

az resource list --subscription "$SUBSCRIPTION_ID" --resource-group "$RG" --output json >"$STATE_DIR/resources.json"
jq --slurpfile resources "$STATE_DIR/resources.json" '.resources=($resources[0] | map({{id,name,type,location}})) | .status="setup-complete"' "$MANIFEST" >"$MANIFEST.tmp"
mv -f "$MANIFEST.tmp" "$MANIFEST"
echo "Setup complete. State: $MANIFEST"
echo "Run scripts/cli/validate.sh before recording command evidence."
'''


def cli_validate(number: str, spec: dict) -> str:
    expected_lines = "\n".join(f'  "{resource_type}"' for resource_type in spec["expected_types"])
    return f'''#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/../.." && pwd)"
SUBSCRIPTION_ID="${{AZURE_SUBSCRIPTION_ID:-}}"
RUN_ID=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
[[ -n "$SUBSCRIPTION_ID" && -n "$RUN_ID" ]] || {{ echo "Supply --subscription-id and --run-id." >&2; exit 2; }}

STATE_DIR="$LAB_ROOT/.state/$RUN_ID"
MANIFEST="$STATE_DIR/run.json"
REPORT="$STATE_DIR/validation.json"
[[ -f "$MANIFEST" ]] || {{ echo "Missing state: $MANIFEST" >&2; exit 5; }}
ACTIVE_SUB="$(az account show --query id --output tsv)"
[[ "$ACTIVE_SUB" == "$SUBSCRIPTION_ID" ]] || {{ echo "Active subscription does not match the requested subscription." >&2; exit 4; }}
RECORDED_SUB="$(jq -r '.subscriptionId' "$MANIFEST")"
[[ "$RECORDED_SUB" == "$SUBSCRIPTION_ID" ]] || {{ echo "Recorded subscription mismatch." >&2; exit 4; }}
RG="$(jq -r '.resourceGroup.name' "$MANIFEST")"
RG_ID="$(jq -r '.resourceGroup.id' "$MANIFEST")"

checks='[]'
add_check() {{
  checks="$(jq -c --arg id "$1" --arg status "$2" --arg message "$3" '. + [{{id:$id,status:$status,message:$message}}]' <<<"$checks")"
}}

actual_rg_id="$(az group show --subscription "$SUBSCRIPTION_ID" --name "$RG" --query id --output tsv 2>/dev/null || true)"
if [[ -z "$actual_rg_id" ]]; then
  add_check context.resource-group fail "The recorded resource group is absent."
elif [[ "${{actual_rg_id,,}}" != "${{RG_ID,,}}" ]]; then
  add_check context.resource-group fail "The resource-group ID does not match the run manifest."
else
  add_check context.resource-group pass "The exact recorded resource group exists."
fi

purpose="$(az group show --name "$RG" --query tags.purpose --output tsv 2>/dev/null || true)"
lab_id="$(az group show --name "$RG" --query tags.labId --output tsv 2>/dev/null || true)"
run_id="$(az group show --name "$RG" --query tags.runId --output tsv 2>/dev/null || true)"
if [[ "$purpose" == "az104-lab" && "$lab_id" == "{number}" && "$run_id" == "$RUN_ID" ]]; then
  add_check ownership.tags pass "purpose, labId, and runId tags match the manifest."
else
  add_check ownership.tags fail "Ownership tags do not match; cleanup must not proceed."
fi

resources="$(az resource list --subscription "$SUBSCRIPTION_ID" --resource-group "$RG" --output json 2>/dev/null || echo '[]')"
EXPECTED_TYPES=(
{expected_lines}
)
if [[ "${{#EXPECTED_TYPES[@]}}" -eq 0 ]]; then
  add_check resources.baseline warning "This lab validates external or tenant-scoped state separately."
else
  for expected in "${{EXPECTED_TYPES[@]}}"; do
    count="$(jq --arg expected "${{expected,,}}" '[.[] | select((.type | ascii_downcase) == $expected)] | length' <<<"$resources")"
    if [[ "$count" -gt 0 ]]; then
      add_check "resource.$(tr '/.' '--' <<<"$expected")" pass "Found $count resource(s) of type $expected."
    else
      add_check "resource.$(tr '/.' '--' <<<"$expected")" warning "No top-level resource of type $expected was returned; inspect nested or gated checkpoint state."
    fi
  done
fi

failures="$(jq '[.[] | select(.status == "fail")] | length' <<<"$checks")"
warnings="$(jq '[.[] | select(.status == "warning" or .status == "skipped")] | length' <<<"$checks")"
result=pass
[[ "$warnings" -eq 0 ]] || result=partial
[[ "$failures" -eq 0 ]] || result=fail
jq -n --arg labId "LAB-{number}" --arg runId "$RUN_ID" --arg generatedAt "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --arg result "$result" --argjson checks "$checks" \
  '{{labId:$labId,runId:$runId,generatedAt:$generatedAt,result:$result,checks:$checks}}' >"$REPORT"
cat "$REPORT"
[[ "$result" != fail ]]
'''


def cli_cleanup(number: str, spec: dict) -> str:
    pre_cleanup = ""
    post_cleanup = ""
    if number == "04":
        pre_cleanup = '''
LOCK_ID="$(az lock show --name "lock-${RUN_ID}" --resource-group "$RG" --query id --output tsv 2>/dev/null || true)"
if [[ -n "$LOCK_ID" ]]; then az lock delete --ids "$LOCK_ID" --output none; fi
'''
        post_cleanup = '''
MG_NAME="$(jq -r '.external.managementGroup // empty' "$MANIFEST")"
if [[ -n "$MG_NAME" ]]; then az account management-group delete --name "$MG_NAME" --output none; fi
'''
    return f'''#!/usr/bin/env bash
set -euo pipefail

LAB_ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/../.." && pwd)"
SUBSCRIPTION_ID="${{AZURE_SUBSCRIPTION_ID:-}}"
RUN_ID=""
EXECUTE=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --subscription-id) SUBSCRIPTION_ID="$2"; shift 2 ;;
    --run-id) RUN_ID="$2"; shift 2 ;;
    --execute) EXECUTE=true; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
[[ -n "$SUBSCRIPTION_ID" && -n "$RUN_ID" ]] || {{ echo "Supply --subscription-id and --run-id." >&2; exit 2; }}

MANIFEST="$LAB_ROOT/.state/$RUN_ID/run.json"
[[ -f "$MANIFEST" ]] || {{ echo "Missing state: $MANIFEST" >&2; exit 5; }}
[[ "$(az account show --query id --output tsv)" == "$SUBSCRIPTION_ID" ]] || {{ echo "Active subscription mismatch." >&2; exit 4; }}
[[ "$(jq -r '.subscriptionId' "$MANIFEST")" == "$SUBSCRIPTION_ID" ]] || {{ echo "Recorded subscription mismatch." >&2; exit 4; }}
RG="$(jq -r '.resourceGroup.name' "$MANIFEST")"
RG_ID="$(jq -r '.resourceGroup.id' "$MANIFEST")"
echo "Cleanup preview for LAB-{number}:"
echo "  exact resource group ID: $RG_ID"
echo "  recorded child resources: $(jq '.resources | length' "$MANIFEST")"
echo "  residual/soft-delete behavior must be audited after deletion."
if [[ "$EXECUTE" != true ]]; then
  echo "Preview only. Re-run with --execute after checking every target."
  exit 0
fi

actual="$(az group show --name "$RG" --query id --output tsv 2>/dev/null || true)"
if [[ -z "$actual" ]]; then echo "Resource group is already absent; cleanup is idempotent."; exit 0; fi
purpose="$(az group show --name "$RG" --query tags.purpose --output tsv)"
lab_id="$(az group show --name "$RG" --query tags.labId --output tsv)"
run_id="$(az group show --name "$RG" --query tags.runId --output tsv)"
[[ "${{actual,,}}" == "${{RG_ID,,}}" && "$purpose" == az104-lab && "$lab_id" == {number} && "$run_id" == "$RUN_ID" ]] || {{
  echo "ID or ownership-tag verification failed; refusing cleanup." >&2; exit 6;
}}
{pre_cleanup.strip()}
az group delete --ids "$RG_ID" --yes --output none
{post_cleanup.strip()}
if az group exists --name "$RG" | grep -qi true; then
  echo "Resource group still exists; deletion may be asynchronous or blocked." >&2
  exit 7
fi
jq '.status="cleanup-complete"' "$MANIFEST" >"$MANIFEST.tmp" && mv -f "$MANIFEST.tmp" "$MANIFEST"
echo "Active resource-group cleanup complete. Audit soft-deleted or externally retained items separately."
'''


def ps_preflight(number: str, spec: dict) -> str:
    modules = ",\n    ".join(f"'{module}'" for module in spec["modules"])
    providers = ",\n    ".join(f"'{provider}'" for provider in spec["providers"])
    if spec["scope"] == "tenant":
        context_check = '''$graphContext = Get-MgContext
if (-not $graphContext) { throw 'No Microsoft Graph context is active. Sign in deliberately before running this lab.' }
Write-Host "Graph tenant: $($graphContext.TenantId)"
Write-Host "Graph account: $($graphContext.Account)"'''
        subscription_param = "[string]$SubscriptionId = '',"
        provider_check = "Write-Host 'Azure provider checks are not applicable to this tenant-scoped lab.'"
    else:
        context_check = '''if (-not $SubscriptionId) { throw 'Supply -SubscriptionId explicitly.' }
$context = Get-AzContext
if (-not $context) { throw 'No Az PowerShell context is active. Sign in deliberately before running this lab.' }
if ($context.Subscription.Id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($context.Subscription.Id), expected $SubscriptionId. This script will not switch it."
}
Write-Host "Tenant: $($context.Tenant.Id)"
Write-Host "Subscription: $($context.Subscription.Id)"'''
        subscription_param = "[Parameter(Mandatory)][string]$SubscriptionId,"
        provider_check = f'''$providers = @(
    {providers}
)
foreach ($provider in $providers) {{
    $item = Get-AzResourceProvider -ProviderNamespace $provider -ErrorAction SilentlyContinue
    $states = @($item.ResourceTypes.RegistrationState | Sort-Object -Unique) -join ','
    Write-Host ("Provider {{0,-38}} {{1}}" -f $provider, $(if ($states) {{ $states }} else {{ 'Unavailable' }}))
}}'''
    return f'''#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context interface.')]
param(
    {subscription_param}
    [Parameter(Mandatory)][string]$Location
)

$ErrorActionPreference = 'Stop'
$requiredModules = @(
    {modules}
)
foreach ($module in $requiredModules) {{
    if (-not (Get-Module -ListAvailable -Name $module)) {{ throw "Missing required module: $module" }}
}}

{context_check}
Write-Host 'Lab: LAB-{number}'
Write-Host 'Location:' $Location
Write-Host 'Cost class: {spec['cost']}'
Write-Host 'Role boundary: {spec['role']}'
{provider_check}
Write-Host 'Preflight is read-only. It does not connect, change context, register providers, or create resources.'
'''


def ps_setup(number: str, spec: dict) -> str:
    action = POWERSHELL_ACTIONS.get(number, "Write-Host 'Continue with the documented guided checkpoints after this recorded baseline.'")
    tenant = spec["scope"] == "tenant"
    subscription_param = "[string]$SubscriptionId = ''," if tenant else "[Parameter(Mandatory)][string]$SubscriptionId,"
    preflight_subscription = "" if tenant else " -SubscriptionId $SubscriptionId"
    context = (
        '''$graphContext = Get-MgContext
$TenantId = $graphContext.TenantId'''
        if tenant
        else '''$context = Get-AzContext
$TenantId = $context.Tenant.Id'''
    )
    rg_create = ""
    resource_capture = "$state.status = 'setup-complete'"
    if not tenant:
        rg_create = '''$tags = @{ purpose = 'az104-lab'; labId = 'LAB_NUMBER'; runId = $RunId; expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd') }
$resourceGroup = New-AzResourceGroup -Name $ResourceGroupName -Location $Location -Tag $tags
$state.resourceGroup.id = $resourceGroup.ResourceId
$state.status = 'baseline-created'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8'''.replace("LAB_NUMBER", number)
        resource_capture = '''$state.resources = @(Get-AzResource -ResourceGroupName $ResourceGroupName | ForEach-Object {
    [ordered]@{ id = $_.ResourceId; name = $_.Name; type = $_.ResourceType; location = $_.Location }
})
$state.status = 'setup-complete' '''
    has_rg = "$true" if not tenant else "$false"
    resources = ", ".join(spec["resources"])
    return f'''#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'All lanes keep a consistent explicit context and region interface.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Named checkpoint results improve readability even when the object is used only to enforce failure handling.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'The disposable generated VMSS credential remains in memory and is never persisted.')]
param(
    {subscription_param}
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$ResourceGroupName = 'rg-az104-l{number}-' + $RunId
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'

Write-Host 'LAB-{number} plan'
Write-Host '  subscription:' $(if ($SubscriptionId) {{ $SubscriptionId }} else {{ 'tenant-scoped / not applicable' }})
Write-Host '  location:' $Location
Write-Host '  resource group:' $(if ({has_rg}) {{ $ResourceGroupName }} else {{ 'none (tenant objects)' }})
Write-Host '  cost class: {spec['cost']}'
Write-Host '  external gate: {spec['gate']}'
Write-Host '  resources: {resources}'
if (-not $Execute) {{
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}}

& (Join-Path $PSScriptRoot 'Preflight.ps1'){preflight_subscription} -Location $Location
if (Test-Path -LiteralPath $Manifest) {{ throw "State already exists at $Manifest; choose a new run ID." }}
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
{context}
$state = [ordered]@{{
    labId = 'LAB-{number}'
    runId = $RunId
    tenantId = $TenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{{ name = $(if ({has_rg}) {{ $ResourceGroupName }} else {{ $null }}); id = $null }}
    resources = @()
    external = [ordered]@{{}}
}}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
{rg_create}

{action.strip()}

{resource_capture}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
'''


def ps_validate(number: str, spec: dict) -> str:
    tenant = spec["scope"] == "tenant"
    subscription_param = "[string]$SubscriptionId = ''," if tenant else "[Parameter(Mandatory)][string]$SubscriptionId,"
    expected = ",\n    ".join(f"'{item}'" for item in spec["expected_types"])
    if tenant:
        body = '''$graphContext = Get-MgContext
if (-not $graphContext) { throw 'No Microsoft Graph context is active.' }
if ($graphContext.TenantId -ne $state.tenantId) { throw 'Recorded tenant does not match the active Graph context.' }
$groupId = $state.external.groupId
if ($groupId) {
    $group = Get-MgGroup -GroupId $groupId -ErrorAction SilentlyContinue
    if ($group) { Add-Check 'entra.group' 'pass' 'The exact recorded pilot group exists.' }
    else { Add-Check 'entra.group' 'fail' 'The recorded pilot group is absent.' }
} else { Add-Check 'entra.group' 'warning' 'No group ID was recorded; setup did not reach the tenant mutation.' }
if ($state.external.guestUserId) {
    $guest = Get-MgUser -UserId $state.external.guestUserId -ErrorAction SilentlyContinue
    if ($guest) { Add-Check 'entra.guest' 'pass' 'The exact invited guest exists.' }
    else { Add-Check 'entra.guest' 'fail' 'A guest ID was recorded but the guest is absent.' }
} else { Add-Check 'entra.guest' 'skipped' 'Guest invitation was gated because AZ104_GUEST_EMAIL was not supplied.' }'''
    else:
        body = f'''$context = Get-AzContext
if (-not $context -or $context.Subscription.Id -ne $SubscriptionId) {{ throw 'Active Az context does not match -SubscriptionId.' }}
if ($state.subscriptionId -ne $SubscriptionId) {{ throw 'Recorded subscription mismatch.' }}
$rg = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if (-not $rg) {{ Add-Check 'context.resource-group' 'fail' 'The recorded resource group is absent.' }}
elseif ($rg.ResourceId -ne $state.resourceGroup.id) {{ Add-Check 'context.resource-group' 'fail' 'The resource-group ID differs from the manifest.' }}
else {{ Add-Check 'context.resource-group' 'pass' 'The exact recorded resource group exists.' }}
if ($rg -and $rg.Tags.purpose -eq 'az104-lab' -and $rg.Tags.labId -eq '{number}' -and $rg.Tags.runId -eq $RunId) {{
    Add-Check 'ownership.tags' 'pass' 'purpose, labId, and runId tags match.'
}} else {{ Add-Check 'ownership.tags' 'fail' 'Ownership tags do not match.' }}
$resources = @(Get-AzResource -ResourceGroupName $state.resourceGroup.name -ErrorAction SilentlyContinue)
$expectedTypes = @(
    {expected}
)
foreach ($type in $expectedTypes) {{
    $count = @($resources | Where-Object ResourceType -eq $type).Count
    if ($count -gt 0) {{ Add-Check ("resource." + ($type -replace '[/\\.]','-')) 'pass' "Found $count resource(s) of type $type." }}
    else {{ Add-Check ("resource." + ($type -replace '[/\\.]','-')) 'warning' "No top-level $type was returned; inspect nested or gated state." }}
}}'''
    return f'''#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent validation interface.')]
param(
    {subscription_param}
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$Report = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) {{ throw "Missing state: $Manifest" }}
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$checks = [System.Collections.Generic.List[object]]::new()
function Add-Check([string]$Id, [string]$Status, [string]$Message) {{
    $checks.Add([ordered]@{{ id = $Id; status = $Status; message = $Message }})
}}

{body}
$failures = @($checks | Where-Object status -eq 'fail').Count
$warnings = @($checks | Where-Object status -in @('warning','skipped')).Count
$result = if ($failures -gt 0) {{ 'fail' }} elseif ($warnings -gt 0) {{ 'partial' }} else {{ 'pass' }}
$output = [ordered]@{{ labId = 'LAB-{number}'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }}
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') {{ exit 1 }}
'''


def ps_cleanup(number: str, spec: dict) -> str:
    tenant = spec["scope"] == "tenant"
    subscription_param = "[string]$SubscriptionId = ''," if tenant else "[Parameter(Mandatory)][string]$SubscriptionId,"
    if tenant:
        body = '''$graphContext = Get-MgContext
if (-not $graphContext -or $graphContext.TenantId -ne $state.tenantId) { throw 'Active Graph tenant does not match the manifest.' }
if ($state.external.licenseSkuId -and $state.external.guestUserId) {
    Set-MgUserLicense -UserId $state.external.guestUserId -AddLicenses @() -RemoveLicenses @([Guid]$state.external.licenseSkuId)
}
if ($state.external.guestUserId) { Remove-MgUser -UserId $state.external.guestUserId -Confirm:$false -ErrorAction SilentlyContinue }
if ($state.external.groupId) { Remove-MgGroup -GroupId $state.external.groupId -Confirm:$false -ErrorAction SilentlyContinue }
if ($state.external.ssprChanged -and $null -ne $state.external.originalAllowedToUseSspr) {
    Update-MgPolicyAuthorizationPolicy -AllowedToUseSspr ([bool]$state.external.originalAllowedToUseSspr)
}
Write-Host 'Exact active tenant objects were removed. Deleted-user retention was not purged.' '''
        preview_target = "$($state.external | ConvertTo-Json -Compress)"
    else:
        pre = ""
        if number == "03":
            pre = '''if ($state.external.roleAssignmentId) {
    $assignment = Get-AzRoleAssignment | Where-Object RoleAssignmentId -eq $state.external.roleAssignmentId | Select-Object -First 1
    if ($assignment) { Remove-AzRoleAssignment -InputObject $assignment }
}'''
        body = f'''$context = Get-AzContext
if (-not $context -or $context.Subscription.Id -ne $SubscriptionId) {{ throw 'Active Az context does not match -SubscriptionId.' }}
if ($state.subscriptionId -ne $SubscriptionId) {{ throw 'Recorded subscription mismatch.' }}
$rg = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if (-not $rg) {{ Write-Host 'Resource group is already absent; cleanup is idempotent.'; return }}
if ($rg.ResourceId -ne $state.resourceGroup.id -or $rg.Tags.purpose -ne 'az104-lab' -or $rg.Tags.labId -ne '{number}' -or $rg.Tags.runId -ne $RunId) {{
    throw 'ID or ownership-tag verification failed; refusing cleanup.'
}}
{pre}
Remove-AzResourceGroup -Id $state.resourceGroup.id -Force
$remaining = Get-AzResourceGroup -Name $state.resourceGroup.name -ErrorAction SilentlyContinue
if ($remaining) {{ throw 'Resource group still exists; inspect soft-delete dependencies, locks, or asynchronous operations.' }}
Write-Host 'Active resource-group cleanup completed. Audit soft-deleted and externally retained items separately.' '''
        preview_target = "$state.resourceGroup.id"
    return f'''#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive cleanup previews are intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Tenant and subscription lanes share a consistent cleanup interface.')]
param(
    {subscription_param}
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$Manifest = Join-Path $LabRoot ".state/$RunId/run.json"
if (-not (Test-Path -LiteralPath $Manifest)) {{ throw "Missing state: $Manifest" }}
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
Write-Host 'Cleanup preview for LAB-{number}'
Write-Host '  exact target:' {preview_target}
Write-Host '  residual/soft-delete behavior must be audited after deletion.'
if (-not $Execute) {{ Write-Host 'Preview only. Re-run with -Execute after checking every target.'; return }}
{body}
$state.status = 'cleanup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
'''


CLI_ACTIONS: dict[str, str] = {
    "04": r'''
az lock create --name "lock-${RUN_ID}" --lock-type CanNotDelete --resource-group "$RG" --notes "AZ-104 Lab 04 run ${RUN_ID}" --output none
az group update --name "$RG" --set tags.stage=managed tags.costCenter=training --output none
if [[ "${AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE:-NO}" == "YES" ]]; then
  MG_NAME="mg-az104-${SUFFIX}"
  az account management-group create --name "$MG_NAME" --display-name "AZ104 ${RUN_ID}" --output none
  jq --arg mg "$MG_NAME" '.external.managementGroup=$mg' "$MANIFEST" >"$MANIFEST.tmp" && mv -f "$MANIFEST.tmp" "$MANIFEST"
fi
''',
    "06": r'''
STORAGE="st06${SUFFIX}"
az storage account create --name "$STORAGE" --resource-group "$RG" --location "$LOCATION" --kind StorageV2 --sku Standard_ZRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --require-infrastructure-encryption true --tags purpose=az104-lab labId=06 runId="$RUN_ID" --output none || \
  az storage account create --name "$STORAGE" --resource-group "$RG" --location "$LOCATION" --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --tags purpose=az104-lab labId=06 runId="$RUN_ID" --output none
az storage account keys renew --resource-group "$RG" --account-name "$STORAGE" --key secondary --output none
''',
    "08": r'''
SRC="st08s${SUFFIX}"
DST="st08d${SUFFIX}"
for ACCOUNT in "$SRC" "$DST"; do
  az storage account create --name "$ACCOUNT" --resource-group "$RG" --location "$LOCATION" --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --enable-change-feed true --enable-versioning true --output none
  az storage account blob-service-properties update --account-name "$ACCOUNT" --resource-group "$RG" --enable-delete-retention true --delete-retention-days 7 --enable-container-delete-retention true --container-delete-retention-days 7 --output none
done
az storage container create --name source --account-name "$SRC" --auth-mode login --output none
az storage container create --name destination --account-name "$DST" --auth-mode login --output none
POLICY=$(jq -nc '{rules:[{enabled:true,name:"tier-and-clean",type:"Lifecycle",definition:{actions:{baseBlob:{tierToCool:{daysAfterModificationGreaterThan:7}},version:{delete:{daysAfterCreationGreaterThan:30}}},filters:{blobTypes:["blockBlob"],prefixMatch:["source/"]}}}]}')
az storage account management-policy create --account-name "$SRC" --resource-group "$RG" --policy "$POLICY" --output none
''',
    "10": r'''
STORAGE="st10${SUFFIX}"
az bicep build --file "$LAB_ROOT/artifacts/main.bicep" --outfile "$STATE_DIR/main.json"
az deployment group what-if --resource-group "$RG" --template-file "$LAB_ROOT/artifacts/main.bicep" --parameters storageName="$STORAGE" --result-format ResourceIdOnly --no-pretty-print >"$STATE_DIR/what-if.txt"
az deployment group create --name "deploy-${RUN_ID}" --resource-group "$RG" --template-file "$LAB_ROOT/artifacts/main.bicep" --parameters storageName="$STORAGE" --output none
az group export --name "$RG" --output json >"$STATE_DIR/exported-template.json"
''',
    "11": r'''
VNET="vnet-${SUFFIX}"
VM="vm-${SUFFIX}"
DISK="disk-${SUFFIX}"
ssh-keygen -q -t ed25519 -N '' -f "$STATE_DIR/id_ed25519"
az network vnet create --resource-group "$RG" --name "$VNET" --address-prefixes 10.11.0.0/16 --subnet-name workload --subnet-prefixes 10.11.1.0/24 --output none
az vm create --resource-group "$RG" --name "$VM" --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$STATE_DIR/id_ed25519.pub" --vnet-name "$VNET" --subnet workload --public-ip-address '' --nsg-rule NONE --output none
az disk create --resource-group "$RG" --name "$DISK" --size-gb 8 --sku Standard_LRS --output none
az vm disk attach --resource-group "$RG" --vm-name "$VM" --name "$DISK" --caching ReadWrite --output none
''',
    "13": r'''
ACR="acr13${SUFFIX}"
ACI="aci-${SUFFIX}"
az acr create --resource-group "$RG" --name "$ACR" --sku Basic --admin-enabled false --output none
az acr import --name "$ACR" --source mcr.microsoft.com/azuredocs/aci-helloworld:latest --image az104/hello:v1 --output none
az container create --resource-group "$RG" --name "$ACI" --image mcr.microsoft.com/azuredocs/aci-helloworld:latest --cpu 1 --memory 1 --restart-policy OnFailure --ports 80 --ip-address Public --dns-name-label "aci-${SUFFIX}" --output none
''',
    "14": r'''
az extension add --name containerapp --upgrade --only-show-errors
WORKSPACE="law-${SUFFIX}"
ENVIRONMENT="cae-${SUFFIX}"
APP="ca-${SUFFIX}"
az monitor log-analytics workspace create --resource-group "$RG" --workspace-name "$WORKSPACE" --location "$LOCATION" --output none
CUSTOMER_ID=$(az monitor log-analytics workspace show --resource-group "$RG" --workspace-name "$WORKSPACE" --query customerId --output tsv)
SHARED_KEY=$(az monitor log-analytics workspace get-shared-keys --resource-group "$RG" --workspace-name "$WORKSPACE" --query primarySharedKey --output tsv)
az containerapp env create --resource-group "$RG" --name "$ENVIRONMENT" --location "$LOCATION" --logs-workspace-id "$CUSTOMER_ID" --logs-workspace-key "$SHARED_KEY" --output none
unset SHARED_KEY
az containerapp create --resource-group "$RG" --name "$APP" --environment "$ENVIRONMENT" --image mcr.microsoft.com/k8se/quickstart:latest --target-port 80 --ingress external --min-replicas 0 --max-replicas 3 --scale-rule-name http --scale-rule-http-concurrency 20 --env-vars LAB_RUN="$RUN_ID" --output none
''',
    "16": r'''
PLAN="plan-${SUFFIX}"
APP="app-${SUFFIX}"
STORAGE="st16${SUFFIX}"
VNET="vnet-${SUFFIX}"
az appservice plan create --resource-group "$RG" --name "$PLAN" --is-linux --sku B1 --output none
az webapp create --resource-group "$RG" --plan "$PLAN" --name "$APP" --runtime 'PYTHON:3.12' --output none
az webapp update --resource-group "$RG" --name "$APP" --https-only true --set siteConfig.minTlsVersion=1.2 --output none
az storage account create --resource-group "$RG" --name "$STORAGE" --location "$LOCATION" --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
az network vnet create --resource-group "$RG" --name "$VNET" --address-prefixes 10.16.0.0/16 --subnet-name integration --subnet-prefixes 10.16.1.0/24 --output none
az network vnet subnet update --resource-group "$RG" --vnet-name "$VNET" --name integration --delegations Microsoft.Web/serverFarms --output none
az webapp vnet-integration add --resource-group "$RG" --name "$APP" --vnet "$VNET" --subnet integration --output none
''',
    "18": r'''
VNET="vnet-${SUFFIX}"
NSG="nsg-${SUFFIX}"
ASG_FRONT="asg-front-${SUFFIX}"
ASG_BACK="asg-back-${SUFFIX}"
ROUTE="rt-${SUFFIX}"
az network vnet create --resource-group "$RG" --name "$VNET" --address-prefixes 10.18.0.0/16 --subnet-name app --subnet-prefixes 10.18.1.0/24 --output none
az network nsg create --resource-group "$RG" --name "$NSG" --output none
az network asg create --resource-group "$RG" --name "$ASG_FRONT" --location "$LOCATION" --output none
az network asg create --resource-group "$RG" --name "$ASG_BACK" --location "$LOCATION" --output none
az network nsg rule create --resource-group "$RG" --nsg-name "$NSG" --name AllowFrontendToBackend443 --priority 200 --direction Inbound --access Allow --protocol Tcp --source-asgs "$ASG_FRONT" --destination-asgs "$ASG_BACK" --destination-port-ranges 443 --output none
az network route-table create --resource-group "$RG" --name "$ROUTE" --location "$LOCATION" --output none
az network route-table route create --resource-group "$RG" --route-table-name "$ROUTE" --name DefaultToInternet --address-prefix 0.0.0.0/0 --next-hop-type Internet --output none
az network vnet subnet update --resource-group "$RG" --vnet-name "$VNET" --name app --network-security-group "$NSG" --route-table "$ROUTE" --output none
''',
    "20": r'''
VNET="vnet-${SUFFIX}"
PIP="pip-${SUFFIX}"
BASTION="bas-${SUFFIX}"
ZONE="lab${SUFFIX}.example.invalid"
az network vnet create --resource-group "$RG" --name "$VNET" --address-prefixes 10.20.0.0/16 --subnet-name AzureBastionSubnet --subnet-prefixes 10.20.0.0/26 --output none
az network public-ip create --resource-group "$RG" --name "$PIP" --sku Standard --allocation-method Static --output none
az network bastion create --resource-group "$RG" --name "$BASTION" --vnet-name "$VNET" --public-ip-address "$PIP" --location "$LOCATION" --sku Basic --output none
az network dns zone create --resource-group "$RG" --name "$ZONE" --output none
az network dns record-set a add-record --resource-group "$RG" --zone-name "$ZONE" --record-set-name app --ipv4-address 192.0.2.10 --output none
az network dns record-set txt add-record --resource-group "$RG" --zone-name "$ZONE" --record-set-name verify --value "az104-${RUN_ID}" --output none
''',
    "22": r'''
WORKSPACE="law-${SUFFIX}"
STORAGE="st22${SUFFIX}"
az monitor log-analytics workspace create --resource-group "$RG" --workspace-name "$WORKSPACE" --location "$LOCATION" --retention-time 30 --output none
az storage account create --resource-group "$RG" --name "$STORAGE" --location "$LOCATION" --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
WORKSPACE_ID=$(az monitor log-analytics workspace show --resource-group "$RG" --workspace-name "$WORKSPACE" --query id --output tsv)
STORAGE_ID=$(az storage account show --resource-group "$RG" --name "$STORAGE" --query id --output tsv)
az monitor diagnostic-settings create --name "diag-${RUN_ID}" --resource "$STORAGE_ID" --workspace "$WORKSPACE_ID" --metrics '[{"category":"Transaction","enabled":true}]' --output none
''',
    "23": r'''
STORAGE="st23${SUFFIX}"
ACTION="ag-${SUFFIX}"
ALERT="alert-${SUFFIX}"
az storage account create --resource-group "$RG" --name "$STORAGE" --location "$LOCATION" --sku Standard_LRS --kind StorageV2 --output none
if [[ -n "${AZ104_ALERT_EMAIL:-}" ]]; then
  az monitor action-group create --resource-group "$RG" --name "$ACTION" --short-name AZ104 --action email lab "$AZ104_ALERT_EMAIL" --output none
else
  az monitor action-group create --resource-group "$RG" --name "$ACTION" --short-name AZ104 --output none
fi
STORAGE_ID=$(az storage account show --resource-group "$RG" --name "$STORAGE" --query id --output tsv)
ACTION_ID=$(az monitor action-group show --resource-group "$RG" --name "$ACTION" --query id --output tsv)
az monitor metrics alert create --resource-group "$RG" --name "$ALERT" --scopes "$STORAGE_ID" --condition 'avg UsedCapacity > 1' --window-size 15m --evaluation-frequency 5m --action "$ACTION_ID" --description "AZ-104 Lab 23 capacity signal" --output none
az monitor activity-log alert create --resource-group "$RG" --name "activity-${SUFFIX}" --scope "$STORAGE_ID" --condition category=Administrative operationName=Microsoft.Storage/storageAccounts/write --action-group "$ACTION_ID" --output none
''',
    "26": r'''
STORAGE="st26${SUFFIX}"
az bicep build --file "$LAB_ROOT/artifacts/main.bicep" --outfile "$STATE_DIR/main.json"
az deployment group what-if --resource-group "$RG" --template-file "$LAB_ROOT/artifacts/main.bicep" --parameters suffix="$SUFFIX" storageName="$STORAGE" --result-format ResourceIdOnly --no-pretty-print >"$STATE_DIR/what-if.txt"
az deployment group create --name "capstone-${RUN_ID}" --resource-group "$RG" --template-file "$LAB_ROOT/artifacts/main.bicep" --parameters suffix="$SUFFIX" storageName="$STORAGE" --output none
''',
}


POWERSHELL_ACTIONS: dict[str, str] = {
    "02": r'''
$displayName = "AZ104-L02-$RunId-SSPR-Pilot"
$group = New-MgGroup -DisplayName $displayName -MailEnabled:$false -MailNickname ("az104l02" + $suffix) -SecurityEnabled
$state.external.groupId = $group.Id
if ($env:AZ104_GUEST_EMAIL) {
    $invitation = New-MgInvitation -InvitedUserEmailAddress $env:AZ104_GUEST_EMAIL -InviteRedirectUrl 'https://myapps.microsoft.com' -SendInvitationMessage:$false
    $state.external.guestUserId = $invitation.InvitedUser.Id
}
if ($env:AZ104_LICENSE_SKU_ID -and $state.external.guestUserId) {
    Set-MgUserLicense -UserId $state.external.guestUserId -AddLicenses @(@{SkuId = [Guid]$env:AZ104_LICENSE_SKU_ID}) -RemoveLicenses @()
    $state.external.licenseSkuId = $env:AZ104_LICENSE_SKU_ID
}
if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -eq 'YES') {
    $policy = Get-MgPolicyAuthorizationPolicy
    $state.external.originalAllowedToUseSspr = $policy.AllowedToUseSspr
    Update-MgPolicyAuthorizationPolicy -AllowedToUseSspr:$true
    $state.external.ssprChanged = $true
}
''',
    "03": r'''
if (-not $env:AZ104_PRINCIPAL_OBJECT_ID) { throw 'Set AZ104_PRINCIPAL_OBJECT_ID to a disposable principal object ID.' }
$scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
$assignment = New-AzRoleAssignment -ObjectId $env:AZ104_PRINCIPAL_OBJECT_ID -RoleDefinitionName Reader -Scope $scope
$state.external.roleAssignmentId = $assignment.RoleAssignmentId
$state.external.principalObjectId = $env:AZ104_PRINCIPAL_OBJECT_ID
Get-AzRoleDefinition -Name Reader | Out-Null
Get-AzRoleDefinition -Name Contributor | Out-Null
''',
    "05": r'''
$definition = Get-AzPolicyDefinition | Where-Object { $_.Properties.DisplayName -eq 'Require a tag and its value on resources' } | Select-Object -First 1
if (-not $definition) { throw 'Required built-in policy definition was not found.' }
$scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
$params = @{ tagName = @{ value = 'purpose' }; tagValue = @{ value = 'az104-lab' } }
$assignment = New-AzPolicyAssignment -Name ("require-purpose-" + $suffix) -DisplayName "AZ104 require purpose $RunId" -Scope $scope -PolicyDefinition $definition -PolicyParameterObject $params
$state.external.policyAssignmentId = $assignment.ResourceId
Start-AzPolicyComplianceScan -ResourceGroupName $ResourceGroupName -AsJob | Out-Null
Get-AzAdvisorRecommendation -Category Cost | Select-Object -First 20 | Out-Null
''',
    "07": r'''
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.7.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name storage -AddressPrefix '10.7.1.0/24' -ServiceEndpoint Microsoft.Storage | Set-AzVirtualNetwork | Out-Null
$vnet = Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name ("vnet-" + $suffix)
$storageName = "st07$suffix"
$rule = New-AzStorageAccountNetworkRuleSet -DefaultAction Deny -VirtualNetworkRule (New-AzStorageAccountVirtualNetworkRule -VirtualNetworkResourceId $vnet.Subnets[0].Id)
$account = New-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name $storageName -Location $Location -SkuName Standard_LRS -Kind StorageV2 -EnableHttpsTrafficOnly $true -MinimumTlsVersion TLS1_2 -NetworkRuleSet $rule -AllowBlobPublicAccess $false
$key = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $storageName)[0].Value
$context = New-AzStorageContext -StorageAccountName $storageName -StorageAccountKey $key
New-AzStorageContainer -Name private -Context $context -Permission Off | Out-Null
$start = (Get-Date).ToUniversalTime().AddMinutes(-5); $expiry = $start.AddHours(2)
Set-AzStorageContainerStoredAccessPolicy -Container private -Policy az104 -Permission rwl -StartTime $start -ExpiryTime $expiry -Context $context
$null = New-AzStorageContainerSASToken -Name private -Policy az104 -Context $context
Remove-Variable key -ErrorAction SilentlyContinue
''',
    "09": r'''
$storageName = "st09$suffix"
$account = New-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name $storageName -Location $Location -SkuName Standard_LRS -Kind StorageV2 -EnableHttpsTrafficOnly $true -MinimumTlsVersion TLS1_2 -AllowBlobPublicAccess $false
$key = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $storageName)[0].Value
$context = New-AzStorageContext -StorageAccountName $storageName -StorageAccountKey $key
New-AzStorageShare -Name files -Context $context -QuotaGiB 20 | Out-Null
Enable-AzStorageDeleteRetentionPolicy -RetentionDays 7 -Service File -Context $context
$share = Get-AzStorageShare -Name files -Context $context
$share.CloudFileShare.Snapshot() | Out-Null
Remove-Variable key -ErrorAction SilentlyContinue
''',
    "12": r'''
$availabilitySet = New-AzAvailabilitySet -ResourceGroupName $ResourceGroupName -Name ("avset-" + $suffix) -Location $Location -Sku Aligned -PlatformFaultDomainCount 2 -PlatformUpdateDomainCount 5
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.12.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name vmss -AddressPrefix '10.12.1.0/24' | Set-AzVirtualNetwork | Out-Null
$credential = New-Object PSCredential ('azureadmin', (ConvertTo-SecureString ([Guid]::NewGuid().ToString('N') + 'aA!9') -AsPlainText -Force))
New-AzVmss -ResourceGroupName $ResourceGroupName -VMScaleSetName ("vmss-" + $suffix) -Location $Location -VirtualNetworkName ("vnet-" + $suffix) -SubnetName vmss -PublicIpAddressName ("pip-" + $suffix) -LoadBalancerName ("lb-" + $suffix) -Credential $credential -ImageName UbuntuLTS -InstanceCount 1 -UpgradePolicyMode Manual | Out-Null
''',
    "15": r'''
$plan = New-AzAppServicePlan -ResourceGroupName $ResourceGroupName -Name ("plan-" + $suffix) -Location $Location -Tier Basic -WorkerSize Small -NumberofWorkers 1 -Linux
$app = New-AzWebApp -ResourceGroupName $ResourceGroupName -Name ("app-" + $suffix) -Location $Location -AppServicePlan $plan.Name
New-AzWebAppSlot -ResourceGroupName $ResourceGroupName -Name $app.Name -Slot staging | Out-Null
$settings = @{ LAB_STAGE = 'staging'; LAB_RUN = $RunId }
Set-AzWebAppSlot -ResourceGroupName $ResourceGroupName -Name $app.Name -Slot staging -AppSettings $settings | Out-Null
''',
    "17": r'''
$hub = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("hub-" + $suffix) -AddressPrefix '10.17.0.0/16'
$hub | Add-AzVirtualNetworkSubnetConfig -Name app -AddressPrefix '10.17.1.0/24' | Add-AzVirtualNetworkSubnetConfig -Name management -AddressPrefix '10.17.2.0/24' | Set-AzVirtualNetwork | Out-Null
$spoke = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("spoke-" + $suffix) -AddressPrefix '10.18.0.0/16'
$spoke | Add-AzVirtualNetworkSubnetConfig -Name app -AddressPrefix '10.18.1.0/24' | Add-AzVirtualNetworkSubnetConfig -Name management -AddressPrefix '10.18.2.0/24' | Set-AzVirtualNetwork | Out-Null
$hub = Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name ("hub-" + $suffix); $spoke = Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name ("spoke-" + $suffix)
Add-AzVirtualNetworkPeering -Name hub-to-spoke -VirtualNetwork $hub -RemoteVirtualNetworkId $spoke.Id | Out-Null
Add-AzVirtualNetworkPeering -Name spoke-to-hub -VirtualNetwork $spoke -RemoteVirtualNetworkId $hub.Id | Out-Null
New-AzPublicIpAddress -ResourceGroupName $ResourceGroupName -Name ("pip-" + $suffix) -Location $Location -Sku Standard -AllocationMethod Static | Out-Null
''',
    "19": r'''
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.19.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name service -AddressPrefix '10.19.1.0/24' -ServiceEndpoint Microsoft.Storage | Add-AzVirtualNetworkSubnetConfig -Name private -AddressPrefix '10.19.2.0/24' -PrivateEndpointNetworkPoliciesFlag Disabled | Set-AzVirtualNetwork | Out-Null
$vnet = Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name ("vnet-" + $suffix)
$storageName = "st19$suffix"
$account = New-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name $storageName -Location $Location -SkuName Standard_LRS -Kind StorageV2 -EnableHttpsTrafficOnly $true -AllowBlobPublicAccess $false
Add-AzStorageAccountNetworkRule -ResourceGroupName $ResourceGroupName -Name $storageName -VirtualNetworkResourceId $vnet.Subnets[0].Id | Out-Null
$connection = New-AzPrivateLinkServiceConnection -Name ("conn-" + $suffix) -PrivateLinkServiceId $account.Id -GroupId blob
New-AzPrivateEndpoint -ResourceGroupName $ResourceGroupName -Name ("pe-" + $suffix) -Location $Location -Subnet $vnet.Subnets[1] -PrivateLinkServiceConnection $connection | Out-Null
$zone = New-AzPrivateDnsZone -ResourceGroupName $ResourceGroupName -Name 'privatelink.blob.core.windows.net'
New-AzPrivateDnsVirtualNetworkLink -ResourceGroupName $ResourceGroupName -ZoneName $zone.Name -Name ("link-" + $suffix) -VirtualNetworkId $vnet.Id -EnableRegistration:$false | Out-Null
''',
    "21": r'''
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.21.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name backend -AddressPrefix '10.21.1.0/24' | Set-AzVirtualNetwork | Out-Null
$pip = New-AzPublicIpAddress -ResourceGroupName $ResourceGroupName -Name ("pip-" + $suffix) -Location $Location -Sku Standard -AllocationMethod Static
$frontend = New-AzLoadBalancerFrontendIpConfig -Name frontend -PublicIpAddress $pip
$backend = New-AzLoadBalancerBackendAddressPoolConfig -Name backend
$probe = New-AzLoadBalancerProbeConfig -Name http -Protocol Tcp -Port 80 -IntervalInSeconds 15 -ProbeCount 2
$rule = New-AzLoadBalancerRuleConfig -Name http -FrontendIpConfiguration $frontend -BackendAddressPool $backend -Probe $probe -Protocol Tcp -FrontendPort 80 -BackendPort 80 -IdleTimeoutInMinutes 4
New-AzLoadBalancer -ResourceGroupName $ResourceGroupName -Name ("lb-" + $suffix) -Location $Location -Sku Standard -FrontendIpConfiguration $frontend -BackendAddressPool $backend -Probe $probe -LoadBalancingRule $rule | Out-Null
Get-AzNetworkWatcher -Location $Location -ErrorAction SilentlyContinue | Out-Null
''',
    "24": r'''
$vault = New-AzRecoveryServicesVault -ResourceGroupName $ResourceGroupName -Name ("rsv-" + $suffix) -Location $Location
Set-AzRecoveryServicesVaultContext -Vault $vault
$policy = Get-AzRecoveryServicesBackupProtectionPolicy -WorkloadType AzureVM | Select-Object -First 1
$state.external.recoveryVaultId = $vault.ID
$backupVaultName = "bv-$suffix"
New-AzResource -ResourceGroupName $ResourceGroupName -ResourceType 'Microsoft.DataProtection/backupVaults' -Name $backupVaultName -ApiVersion '2023-01-01' -Location $Location -Properties @{ storageSettings = @(@{ datastoreType = 'VaultStore'; type = 'LocallyRedundant' }) } -Force | Out-Null
''',
    "25": r'''
$sourceVnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("source-" + $suffix) -AddressPrefix '10.25.0.0/16'
$sourceVnet | Add-AzVirtualNetworkSubnetConfig -Name workload -AddressPrefix '10.25.1.0/24' | Set-AzVirtualNetwork | Out-Null
$recoveryVnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $SecondaryLocation -Name ("recovery-" + $suffix) -AddressPrefix '10.26.0.0/16'
$recoveryVnet | Add-AzVirtualNetworkSubnetConfig -Name recovery -AddressPrefix '10.26.1.0/24' | Set-AzVirtualNetwork | Out-Null
$vault = New-AzRecoveryServicesVault -ResourceGroupName $ResourceGroupName -Name ("asr-" + $suffix) -Location $Location
$state.external.recoveryVaultId = $vault.ID
''',
    "27": r'''
$workspace = New-AzOperationalInsightsWorkspace -ResourceGroupName $ResourceGroupName -Name ("law-" + $suffix) -Location $Location -Sku PerGB2018 -RetentionInDays 30
$vault = New-AzRecoveryServicesVault -ResourceGroupName $ResourceGroupName -Name ("rsv-" + $suffix) -Location $Location
$vnet = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Location $Location -Name ("vnet-" + $suffix) -AddressPrefix '10.27.0.0/16'
$vnet | Add-AzVirtualNetworkSubnetConfig -Name workload -AddressPrefix '10.27.1.0/24' | Set-AzVirtualNetwork | Out-Null
$state.external.workspaceId = $workspace.ResourceId
$state.external.recoveryVaultId = $vault.ID
''',
}

SPECS.update({
    "19": s(
        "19",
        "Compare service endpoints and private endpoints",
        "Az PowerShell",
        "moderate",
        120,
        "Network Contributor and Storage Account Contributor on the lab resource group",
        "Create a storage account and two subnets, apply a Storage service endpoint and network rule to one, create a private endpoint and private DNS integration in the other, then compare routing, DNS, and access behavior.",
        ["resource group", "virtual network", "service-endpoint subnet", "private-endpoint subnet", "storage account", "private endpoint", "private DNS zone"],
        ["Microsoft.Network", "Microsoft.Storage"],
        ["Az.Accounts", "Az.Resources", "Az.Network", "Az.Storage", "Az.PrivateDns"],
        [
            "Create separate service-endpoint and private-endpoint subnets with appropriate policies.",
            "Enable Microsoft.Storage service endpoints and add a storage virtual-network rule.",
            "Create a blob private endpoint and approve its private link connection.",
            "Link privatelink.blob.core.windows.net to the VNet and verify the private A record and network policy differences.",
        ],
        ["Microsoft.Network/privateEndpoints", "Microsoft.Network/privateDnsZones", "Microsoft.Network/virtualNetworks", "Microsoft.Storage/storageAccounts"],
        [
            ("Storage account > Networking", "Service endpoint rule, private endpoint, and default access"),
            ("Private endpoint > DNS configuration", "FQDN and private IP mapping"),
            ("Private DNS zone > Recordsets", "Storage-account private A record"),
            ("Virtual network > Subnets", "Endpoint policies and service endpoint state"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview",
            "https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview",
            "https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints",
            "https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone",
        ],
        "Service endpoints keep the service's public endpoint while adding subnet identity, whereas private endpoints place a private NIC in the VNet and depend on correct private DNS resolution.",
    ),
    "20": s(
        "20",
        "Configure Azure DNS and secure administration with Bastion",
        "Azure CLI",
        "elevated",
        120,
        "Network Contributor; DNS Zone Contributor for an owned zone",
        "Create a hub VNet, AzureBastionSubnet, Standard public IP, and Azure Bastion host; create an isolated Azure DNS zone and records, while delegation of a real public domain remains gated by explicit ownership.",
        ["resource group", "virtual network", "AzureBastionSubnet", "Standard public IP", "Bastion host", "public DNS zone and recordsets"],
        ["Microsoft.Network"],
        [],
        [
            "Create a correctly named and sized AzureBastionSubnet with a Standard static public IP.",
            "Deploy Azure Bastion and inspect SKU, scale units, and supported native-client features.",
            "Create an isolated Azure DNS public zone and A/CNAME/TXT records using a lab-owned label.",
            "Verify authoritative name servers and perform external delegation only for AZ104_OWNED_DNS_ZONE.",
        ],
        ["Microsoft.Network/bastionHosts", "Microsoft.Network/dnsZones", "Microsoft.Network/publicIPAddresses", "Microsoft.Network/virtualNetworks"],
        [
            ("Bastion > Overview", "Provisioning state, SKU, public IP, and VNet"),
            ("Virtual network > Subnets", "AzureBastionSubnet prefix and association"),
            ("DNS zone > Overview", "Azure authoritative name servers"),
            ("DNS zone > Recordsets", "A, CNAME, and TXT examples"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/bastion/tutorial-create-host-cli",
            "https://learn.microsoft.com/en-us/azure/bastion/configuration-settings",
            "https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli",
            "https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation",
        ],
        "Bastion provides managed administrative connectivity without VM public IPs, while Azure DNS becomes authoritative only after the parent domain delegates to its assigned name servers.",
        "Real public DNS delegation requires AZ104_OWNED_DNS_ZONE and control of the parent registrar; the isolated zone path is always available.",
    ),
    "21": s(
        "21",
        "Load balance workloads and troubleshoot with Network Watcher",
        "Az PowerShell",
        "elevated",
        150,
        "Network Contributor and Virtual Machine Contributor on the lab resource group",
        "Create a Standard public load balancer, backend pool, probe, and rule with two small Linux backends; enable Network Watcher, then use connection troubleshooting and packet/effective configuration evidence to diagnose health and flow issues.",
        ["resource group", "virtual network", "two backend VMs", "Standard load balancer", "health probe", "load-balancing rule", "Network Watcher connection monitor"],
        ["Microsoft.Compute", "Microsoft.Network"],
        ["Az.Accounts", "Az.Resources", "Az.Network", "Az.Compute"],
        [
            "Create two backend NICs/VMs in an NSG-protected subnet without individual public IPs.",
            "Create a Standard public load balancer, backend pool, TCP probe, and frontend rule.",
            "Install a minimal HTTP response on each backend and verify probe health before testing the frontend.",
            "Run Network Watcher connection troubleshooting and configure a bounded connection monitor for the backend path.",
        ],
        ["Microsoft.Network/loadBalancers", "Microsoft.Compute/virtualMachines", "Microsoft.Network/networkWatchers"],
        [
            ("Load balancer > Backend pools", "Both backend NIC configurations"),
            ("Load balancer > Health probes", "Probe protocol, port, and health status"),
            ("Load balancer > Insights", "Data-path health and frontend/backend mapping"),
            ("Network Watcher > Connection troubleshoot", "Reachability, latency, and fault details"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-powershell",
            "https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status",
            "https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview",
            "https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview",
        ],
        "A load-balancing rule depends on a healthy probe and reachable backend, while Network Watcher distinguishes DNS, routing, NSG, guest firewall, and application-listener failures.",
    ),
    "22": s(
        "22",
        "Collect and analyze Azure Monitor metrics, logs, and Insights",
        "Azure CLI and KQL",
        "moderate",
        135,
        "Monitoring Contributor and Log Analytics Contributor on the lab resource group",
        "Create a Log Analytics workspace and storage account, send supported resource logs and metrics through diagnostic settings, query tables with KQL, inspect platform metrics, and review Insights onboarding requirements for VMs, storage, and networks.",
        ["resource group", "Log Analytics workspace", "storage account", "diagnostic setting", "optional data collection rule"],
        ["Microsoft.Insights", "Microsoft.OperationalInsights", "Microsoft.Storage"],
        [],
        [
            "Create a Log Analytics workspace with bounded retention and a monitored storage account.",
            "Discover diagnostic categories and create settings that send supported logs and metrics to the workspace.",
            "Run KQL queries that summarize activity by operation, result, and time range without assuming immediate ingestion.",
            "Query platform metrics and compare baseline monitoring with VM, Storage, and Network Insights dependencies.",
        ],
        ["Microsoft.OperationalInsights/workspaces", "Microsoft.Insights/diagnosticSettings", "Microsoft.Storage/storageAccounts"],
        [
            ("Monitor > Metrics", "Selected resource metric, aggregation, and time grain"),
            ("Log Analytics workspace > Logs", "KQL query text and returned schema/results"),
            ("Resource > Diagnostic settings", "Destination workspace and enabled categories"),
            ("Monitor > Insights", "Onboarding or interpreted health for VM, storage, and network"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/metrics-getting-started",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview",
            "https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview",
        ],
        "Metrics are numeric time series, logs are queryable records with ingestion delay and cost, and Insights packages add curated collection and interpretation for particular resource types.",
    ),
    "23": s(
        "23",
        "Build Azure Monitor alerts, action groups, and processing rules",
        "Azure CLI",
        "low",
        105,
        "Monitoring Contributor on the lab resource group",
        "Create a monitored storage account, action group, metric alert, activity-log alert, and scheduled alert processing rule; use a test notification only when AZ104_ALERT_EMAIL is explicitly provided.",
        ["resource group", "storage account", "action group", "metric alert", "activity-log alert", "alert processing rule"],
        ["Microsoft.Insights", "Microsoft.Storage"],
        [],
        [
            "Create an action group with a test email receiver only when AZ104_ALERT_EMAIL is supplied.",
            "Create a metric alert with explicit scope, aggregation, threshold, frequency, and window.",
            "Create an activity-log alert for a resource operation and inspect the common alert schema.",
            "Create a time-bounded alert processing rule and prove it suppresses actions rather than alert evaluation.",
        ],
        ["Microsoft.Insights/actionGroups", "Microsoft.Insights/metricAlerts", "Microsoft.Insights/activityLogAlerts", "Microsoft.AlertsManagement/actionRules"],
        [
            ("Monitor > Alerts > Alert rules", "Metric and activity-log conditions and scopes"),
            ("Monitor > Alerts > Action groups", "Receivers and common alert schema"),
            ("Monitor > Alerts > Alert processing rules", "Schedule, filters, and action behavior"),
            ("Monitor > Alerts", "A test or historical alert lifecycle when available"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules",
        ],
        "Alert rules evaluate signals, action groups deliver notifications or automation, and processing rules change action behavior without disabling signal evaluation.",
        "Email delivery and action-group testing require AZ104_ALERT_EMAIL; otherwise a receiver-free action group is used for configuration practice.",
    ),
    "24": s(
        "24",
        "Configure Azure Backup policies, protection, restore, reports, and alerts",
        "Az PowerShell",
        "moderate",
        150,
        "Backup Contributor and Virtual Machine Contributor on the lab resource group",
        "Create both Recovery Services and Backup vault resource types, define a VM backup policy, protect a small VM, trigger and monitor an on-demand backup, perform a file-level restore workflow, and configure monitoring evidence.",
        ["resource group", "Recovery Services vault", "Backup vault", "backup policy", "protected test VM", "backup instance and restore job"],
        ["Microsoft.Compute", "Microsoft.DataProtection", "Microsoft.RecoveryServices"],
        ["Az.Accounts", "Az.Resources", "Az.RecoveryServices", "Az.DataProtection", "Az.Compute", "Az.Network"],
        [
            "Create a Recovery Services vault and a separate modern Backup vault and compare their supported workloads.",
            "Create a bounded-retention VM backup policy and enable protection for the test VM.",
            "Trigger an on-demand backup, monitor its asynchronous job, and preserve evidence before restore testing.",
            "Run a restore workflow, inspect Backup reports/alerts prerequisites, then stop protection and delete backup data before vault cleanup.",
        ],
        ["Microsoft.RecoveryServices/vaults", "Microsoft.DataProtection/backupVaults", "Microsoft.Compute/virtualMachines"],
        [
            ("Recovery Services vault > Backup policies", "Schedule, retention, and protected item count"),
            ("Recovery Services vault > Backup jobs", "On-demand backup or restore job status"),
            ("Backup vault > Backup instances", "Modern vault workload and protection state"),
            ("Business Continuity Center > Alerts or Reports", "Configured monitoring destination and current state"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault",
            "https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault",
            "https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-powershell",
            "https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm",
            "https://learn.microsoft.com/en-us/azure/backup/configure-reports",
            "https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor",
        ],
        "Vault type must match the workload, protection creates retained recovery points, and vault deletion requires ordered removal of protected items, soft-delete state, and dependencies.",
    ),
    "25": s(
        "25",
        "Replicate and fail over an Azure VM with Site Recovery",
        "Az PowerShell",
        "elevated",
        180,
        "Site Recovery Contributor, Virtual Machine Contributor, and Network Contributor on both region scopes",
        "Create isolated source and recovery networks, a small source VM, and a Recovery Services vault; configure Azure-to-Azure replication, run an isolated test failover, clean it up, and document planned/unplanned failover and reprotection gates.",
        ["resource group", "source and recovery VNets", "source VM", "Recovery Services vault", "ASR fabric/container mappings", "replicated item"],
        ["Microsoft.Compute", "Microsoft.Network", "Microsoft.RecoveryServices"],
        ["Az.Accounts", "Az.Resources", "Az.RecoveryServices", "Az.Compute", "Az.Network"],
        [
            "Create non-overlapping source and recovery VNets in the configured primary and secondary regions.",
            "Create a source VM and Recovery Services vault, then configure Azure-to-Azure fabric, container, policy, and network mappings.",
            "Enable replication and wait for protected health before running an isolated test failover into a test subnet.",
            "Clean up test failover, compare planned and unplanned failover, and remove replication in the required order before vault deletion.",
        ],
        ["Microsoft.RecoveryServices/vaults", "Microsoft.Compute/virtualMachines", "Microsoft.Network/virtualNetworks"],
        [
            ("Recovery Services vault > Replicated items", "Replication health, RPO, and recovery region"),
            ("Replicated item > Compute and Network", "Target VM, disk, VNet, subnet, and IP choices"),
            ("Recovery Services vault > Site Recovery jobs", "Test failover and cleanup job sequence"),
            ("Resource group > Recovery VM", "Isolated test-failover VM before cleanup"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-powershell",
            "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill",
            "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback",
            "https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-manage-registration-and-protection",
        ],
        "Test failover validates recovery without committing production direction, while planned/unplanned failover, commit, reprotect, and failback are separate state transitions with cost and data-loss implications.",
        "This elevated lab requires two approved regions and explicit cost review before live execution; test failover must use an isolated network.",
    ),
    "26": s(
        "26",
        "Capstone — Build a governed, secure, observable Azure workload",
        "Azure CLI and Bicep",
        "moderate",
        180,
        "Contributor, User Access Administrator, Resource Policy Contributor, and Monitoring Contributor on the capstone resource group",
        "Build a small multi-tier workload from Bicep with governance tags, RBAC, secure storage, segmented networking, private access, resilient compute, load balancing, diagnostics, alerts, and a complete evidence/cleanup record.",
        ["resource group", "Bicep deployment", "segmented VNet", "NSG", "private storage", "resilient compute", "load balancer", "Log Analytics workspace", "diagnostic settings", "alerts"],
        ["Microsoft.Authorization", "Microsoft.Compute", "Microsoft.Insights", "Microsoft.Network", "Microsoft.OperationalInsights", "Microsoft.Storage"],
        [],
        [
            "Run Bicep build and what-if, then deploy the governed resource group and deterministic tags.",
            "Create segmented networking, NSG/ASG controls, resilient compute, load balancing, and a private storage endpoint.",
            "Apply the least-privileged recorded RBAC assignment and a scoped governance policy.",
            "Enable diagnostic settings, queries, alerts, and an operator dashboard before running end-to-end validation and cleanup.",
        ],
        ["Microsoft.Network/virtualNetworks", "Microsoft.Storage/storageAccounts", "Microsoft.Compute/virtualMachines", "Microsoft.Network/loadBalancers", "Microsoft.OperationalInsights/workspaces"],
        [
            ("Resource group > Overview", "Complete tagged deployment inventory"),
            ("Network topology", "Subnets, NSGs, private endpoint, and load balancer"),
            ("Resource group > Access control and Policies", "Scoped RBAC and policy evidence"),
            ("Monitor > Logs and Alerts", "Diagnostics, query results, and alert rules"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli",
            "https://learn.microsoft.com/en-us/azure/architecture/framework/",
            "https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings",
            "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli",
        ],
        "The build capstone proves that governance, identity, networking, compute, storage, and observability are coupled design decisions and must share a recorded deployment and cleanup boundary.",
        "Requires AZ104_PRINCIPAL_OBJECT_ID for the RBAC checkpoint; the workload path remains deployable without assigning a role when the value is absent.",
    ),
    "27": s(
        "27",
        "Capstone — Operate, troubleshoot, back up, and recover an Azure workload",
        "Az PowerShell and KQL",
        "elevated",
        180,
        "Contributor, Monitoring Contributor, Backup Contributor, and Network Contributor on the capstone resource group",
        "Deploy or discover an isolated workload, interpret access and policy state, diagnose a network fault, query logs and metrics, respond to alerts, restore protected data, and execute a documented recovery decision before complete cleanup.",
        ["resource group", "test workload", "Log Analytics workspace", "alerts", "Recovery Services vault", "backup policy", "fault injection and recovery evidence"],
        ["Microsoft.Authorization", "Microsoft.Compute", "Microsoft.Insights", "Microsoft.Network", "Microsoft.OperationalInsights", "Microsoft.RecoveryServices"],
        ["Az.Accounts", "Az.Resources", "Az.Network", "Az.Compute", "Az.Monitor", "Az.OperationalInsights", "Az.RecoveryServices"],
        [
            "Inventory the workload, interpret direct/inherited access, policy compliance, tags, locks, and current health before changing anything.",
            "Inject one bounded NSG or load-balancer fault, use effective rules and Network Watcher evidence to diagnose it, then repair only the identified cause.",
            "Query metrics/logs, process an alert, and record the operational timeline and validation output.",
            "Protect the test workload, run a restore or isolated recovery drill, verify recovered state, and remove protection/resources in dependency order.",
        ],
        ["Microsoft.Compute/virtualMachines", "Microsoft.OperationalInsights/workspaces", "Microsoft.RecoveryServices/vaults"],
        [
            ("Resource group > Activity log", "Operational timeline for fault, repair, backup, and cleanup"),
            ("Network Watcher", "Effective-rule or connection diagnostic evidence"),
            ("Monitor > Logs and Alerts", "KQL diagnosis and alert lifecycle"),
            ("Recovery Services vault > Jobs", "Backup and restore/recovery drill result"),
        ],
        [
            "https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-ip-flow-verify-overview",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview",
            "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview",
            "https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction",
            "https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access",
        ],
        "Operations should follow evidence: establish baseline, detect and scope the fault, repair the smallest cause, validate service state, then prove backup or recovery objectives before cleanup.",
        "The live recovery drill requires cost review and an isolated workload; production failover or irreversible deletion is never inferred from this capstone.",
    ),
})


def render_solution(number: str, spec: dict) -> str:
    actions = "\n".join(f"{index}. **Checkpoint {index}:** {action}" for index, action in enumerate(spec["actions"], 1))
    return f"""# Lab {number} solution and diagnostic notes

Use this only after completing the lab and knowledge check. The solution is evidence-led: it does not replace the independent validator or silently repair live state.

## Intended checkpoint sequence

{actions}

## Diagnostic order

1. Confirm that the active tenant and subscription match `.state/<run-id>/run.json`.
2. Confirm the exact resource group or tenant object ID; do not select by a name prefix.
3. Inspect provider registration, service quota, region support, and asynchronous provisioning state.
4. Compare the live configuration with the checkpoint statement in [the lab guide](../README.md).
5. Read `.state/<run-id>/validation.json` and reproduce the failing read-only query directly.
6. Repair only the smallest identified mismatch, then rerun validation.
7. If a prerequisite is absent, record `skipped` or `warning`; never convert a gate into a false pass.

## Expected reasoning

{spec['fact']}

The permission boundary is: {spec['role']}

The live gate is: {spec['gate']}

## Common failure classes

- **Context mismatch:** select the intended context yourself and rerun preflight. The scripts intentionally do not sign in or switch it.
- **Authorization failure:** inspect the failed action and required scope. Do not broaden to subscription or tenant scope without a justified objective.
- **Provider, quota, SKU, or region failure:** use the preflight evidence and choose an approved supported region/SKU; document any fallback.
- **Eventual consistency:** poll the documented operation state and retain timestamps. Do not interpret a transient empty query as final success.
- **Network or DNS failure:** inspect effective routes/rules, name resolution, private DNS links, listener/probe state, and the guest firewall/application separately.
- **Cleanup dependency:** remove recorded locks, role/policy assignments, protection or replication state, private links, and retained data in the service's required order.

## Completion evidence

A defensible result includes a run manifest, independent validation report, redacted CLI or PowerShell evidence, and a cleanup/residual audit. Offline repository tests alone do not establish live verification.
"""


def render_tests(number: str, lane: str) -> tuple[str, str, dict]:
    extension = "sh" if lane == "cli" else "ps1"
    stage_files = (
        ["preflight.sh", "setup.sh", "validate.sh", "cleanup.sh"]
        if lane == "cli"
        else ["Preflight.ps1", "Setup.ps1", "Validate.ps1", "Cleanup.ps1"]
    )
    files_literal = ", ".join(f"'{name}'" for name in stage_files)
    test = f'''#requires -Version 7.4
Describe 'LAB-{number} offline lifecycle contract' {{
    BeforeAll {{
        $labRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
        $lane = Join-Path $labRoot 'scripts/{lane}'
        $stageFiles = @({files_literal})
    }}

    It 'contains every lifecycle stage' {{
        foreach ($name in $stageFiles) {{ Test-Path -LiteralPath (Join-Path $lane $name) | Should -BeTrue }}
    }}

    It 'does not sign in or silently change Azure context' {{
        $content = ($stageFiles | ForEach-Object {{ Get-Content -LiteralPath (Join-Path $lane $_) -Raw }}) -join "`n"
        $content | Should -Not -Match '(?i)az\s+login|Connect-AzAccount|Set-AzContext|az\s+account\s+set'
    }}

    It 'keeps setup and cleanup preview-first' {{
        $setup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[1]) -Raw
        $cleanup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[3]) -Raw
        $setup | Should -Match '(?i)--execute|\[switch\]\$Execute'
        $cleanup | Should -Match '(?i)--execute|\[switch\]\$Execute'
    }}

    It 'records state and emits a schema-shaped validation report' {{
        $setup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[1]) -Raw
        $validate = Get-Content -LiteralPath (Join-Path $lane $stageFiles[2]) -Raw
        $setup | Should -Match '(?i)run\.json'
        $validate | Should -Match '(?i)validation\.json'
        $validate | Should -Match "LAB-{number}"
    }}

    It 'contains no cross-lab runtime dependency' {{
        $content = ($stageFiles | ForEach-Object {{ Get-Content -LiteralPath (Join-Path $lane $_) -Raw }}) -join "`n"
        $content | Should -Not -Match '\.\.[\\/][0-9]{{2}}-[a-z0-9-]+'
    }}
}}
'''
    readme = f"""# Lab {number} offline tests

Run from the repository root:

```powershell
Invoke-Pester -Path labs/*/tests -Output Detailed
```

The contract test checks that the `{lane}` lane contains preflight, setup, validation, and cleanup; never signs in or silently changes context; keeps mutations behind an explicit execution switch; records state; and has no runtime dependency on another lab.

These are offline safety and structure tests. They do not claim that Azure resources were deployed.
"""
    fixture = {
        "labId": f"LAB-{number}",
        "runId": f"az104l{number}-sample",
        "generatedAt": f"{REVIEW_DATE}T12:00:00Z",
        "result": "pass",
        "checks": [
            {
                "id": "contract.recorded-boundary",
                "status": "pass",
                "message": "The sample demonstrates the required validation document shape; it is not live evidence.",
            }
        ],
    }
    return test, readme, fixture


def artifact_files(number: str) -> dict[str, str]:
    if number == "10":
        return {
            "artifacts/main.bicep": '''@description('Globally unique Storage account name')
param storageName string

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
  properties: {
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
  tags: {
    purpose: 'az104-lab'
    labId: '10'
  }
}

output storageId string = storage.id
''',
            "artifacts/parameters.example.json": '''{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageName": { "value": "replacewithgloballyuniquename" }
  }
}''',
        }
    if number == "26":
        return {
            "artifacts/main.bicep": '''@minLength(3)
param suffix string
@description('Globally unique Storage account name')
param storageName string

var tags = { purpose: 'az104-lab', labId: '26', workload: 'capstone' }

resource vnet 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: 'vnet-${suffix}'
  location: resourceGroup().location
  tags: tags
  properties: {
    addressSpace: { addressPrefixes: [ '10.26.0.0/16' ] }
    subnets: [
      { name: 'web', properties: { addressPrefix: '10.26.1.0/24' } }
      { name: 'private-endpoints', properties: { addressPrefix: '10.26.2.0/24', privateEndpointNetworkPolicies: 'Disabled' } }
    ]
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
  tags: tags
  properties: { supportsHttpsTrafficOnly: true, minimumTlsVersion: 'TLS1_2', allowBlobPublicAccess: false, publicNetworkAccess: 'Disabled' }
}

resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'law-${suffix}'
  location: resourceGroup().location
  tags: tags
  properties: { retentionInDays: 30, sku: { name: 'PerGB2018' } }
}

resource publicIp 'Microsoft.Network/publicIPAddresses@2024-05-01' = {
  name: 'pip-${suffix}'
  location: resourceGroup().location
  tags: tags
  sku: { name: 'Standard' }
  properties: { publicIPAllocationMethod: 'Static' }
}

resource loadBalancer 'Microsoft.Network/loadBalancers@2024-05-01' = {
  name: 'lb-${suffix}'
  location: resourceGroup().location
  tags: tags
  sku: { name: 'Standard' }
  properties: { frontendIPConfigurations: [ { name: 'frontend', properties: { publicIPAddress: { id: publicIp.id } } } ] }
}

output virtualNetworkId string = vnet.id
output storageId string = storage.id
output workspaceId string = workspace.id
output loadBalancerId string = loadBalancer.id
''',
            "artifacts/README.md": """# Capstone Bicep baseline

The baseline intentionally stops short of creating credentials, public virtual machines, role assignments, policy assignments, or irreversible recovery state. Use `az bicep build` and `az deployment group what-if` before deployment, then complete the governed checkpoints from the lab guide with exact scopes and explicit gates.
""",
        }
    return {}


def generate_lab(number: str, spec: dict, objectives_index: dict[str, dict], force: bool, status: str) -> str:
    slug, objectives = slug_and_objectives(number, objectives_index)
    lab_dir = LABS_ROOT / slug
    if lab_dir.exists() and not force:
        raise FileExistsError(f"{lab_dir} already exists; use --force only for generated Labs 02-27")
    lab_dir.mkdir(parents=True, exist_ok=True)

    metadata = make_lab_metadata(number, slug, spec, objectives, status)
    questions = make_questions(number, spec, objectives)
    question_md, answer_md = render_questions(number, spec["title"], questions)
    mermaid, svg = render_diagram(number, spec)
    lane = command_lane(spec)
    test, test_readme, fixture = render_tests(number, lane)

    files: dict[str, str] = {
        "lab.yml": yaml_text(metadata),
        "README.md": render_readme(number, slug, spec, objectives),
        "assessment/questions.yml": yaml_text(questions),
        "assessment/QUESTIONS.md": question_md,
        "assessment/ANSWERS.md": answer_md,
        "diagrams/architecture.mmd": mermaid,
        "diagrams/architecture.svg": svg,
        "solution/README.md": render_solution(number, spec),
        "tests/Contract.Tests.ps1": test,
        "tests/README.md": test_readme,
        "tests/fixtures/validation.sample.json": json.dumps(fixture, indent=2),
        "images/README.md": render_images_readme(number),
        "images/portal/manifest.yml": yaml_text(render_portal_manifest(number, spec)),
    }
    if lane == "cli":
        files.update(
            {
                "scripts/cli/preflight.sh": cli_preflight(number, spec),
                "scripts/cli/setup.sh": cli_setup(number, spec),
                "scripts/cli/validate.sh": cli_validate(number, spec),
                "scripts/cli/cleanup.sh": cli_cleanup(number, spec),
            }
        )
    else:
        files.update(
            {
                "scripts/powershell/Preflight.ps1": ps_preflight(number, spec),
                "scripts/powershell/Setup.ps1": ps_setup(number, spec),
                "scripts/powershell/Validate.ps1": ps_validate(number, spec),
                "scripts/powershell/Cleanup.ps1": ps_cleanup(number, spec),
            }
        )
    files.update(artifact_files(number))
    for relative, content in files.items():
        write_text(lab_dir / relative, content)
    return slug


def update_catalog(status: str) -> None:
    path = LABS_ROOT / "catalog.yml"
    catalog = yaml.safe_load(path.read_text(encoding="utf-8"))
    for item in catalog["labs"]:
        if item["id"] in SPECS:
            item["status"] = status
    write_text(path, yaml_text(catalog))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Overwrite generated Labs 02-27")
    parser.add_argument(
        "--status",
        choices=["in-progress", "offline-validated"],
        default="in-progress",
        help="Metadata status applied to generated labs and catalog",
    )
    parser.add_argument("--only", nargs="*", help="Optional lab numbers, for example --only 02 03")
    args = parser.parse_args()
    selected = sorted(args.only or SPECS.keys())
    unknown = set(selected) - set(SPECS)
    if unknown:
        parser.error(f"Unknown generated lab number(s): {', '.join(sorted(unknown))}")
    objectives, _ = curriculum_index()
    for number in selected:
        slug = generate_lab(number, SPECS[number], objectives, args.force, args.status)
        print(f"WRITE labs/{slug}")
    if not args.only:
        update_catalog(args.status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
