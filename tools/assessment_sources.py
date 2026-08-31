#!/usr/bin/env python3
"""Direct Microsoft Learn source contract for the assessment concept cycles.

Each lab assesses ten service concepts from five cognitive angles.  A question's
position within its ten-question cycle identifies the concept, and this module
binds that concept to documentation that directly supports the correct claim.
The assessment validator uses this contract to prevent an objective-level or
adjacent-service article from being attached to an otherwise valid question.
"""

from __future__ import annotations


def _source(title: str, url: str) -> dict[str, str]:
    return {"title": title, "url": url}


SOURCE_CATALOG: dict[str, dict[str, str]] = {
    # Identity and governance
    "entra_domains": _source("List domains with Microsoft Graph", "https://learn.microsoft.com/en-us/graph/api/domain-list?view=graph-rest-1.0"),
    "entra_user_cli": _source("Azure CLI reference for Microsoft Entra users", "https://learn.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest"),
    "entra_user_resource": _source("Microsoft Graph user resource type", "https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0"),
    "entra_group_cli": _source("Azure CLI reference for Microsoft Entra groups", "https://learn.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest"),
    "entra_group_member_cli": _source("Azure CLI reference for Microsoft Entra group membership", "https://learn.microsoft.com/en-us/cli/azure/ad/group/member?view=azure-cli-latest"),
    "entra_group_owner_cli": _source("Azure CLI reference for Microsoft Entra group owners", "https://learn.microsoft.com/en-us/cli/azure/ad/group/owner?view=azure-cli-latest"),
    "entra_restore_user": _source("Restore or permanently remove recently deleted users", "https://learn.microsoft.com/en-us/entra/fundamentals/users-restore"),
    "license_capacity": _source("List subscribed SKUs with Microsoft Graph", "https://learn.microsoft.com/en-us/graph/api/subscribedsku-list?view=graph-rest-1.0"),
    "license_user": _source("Assign licenses to a user with Microsoft Graph", "https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0"),
    "license_group": _source("Group-based licensing fundamentals", "https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing"),
    "guest_invitation": _source("Create a Microsoft Entra B2B invitation", "https://learn.microsoft.com/en-us/graph/api/invitation-post?view=graph-rest-1.0"),
    "guest_redemption": _source("Microsoft Entra B2B redemption experience", "https://learn.microsoft.com/en-us/entra/external-id/redemption-experience"),
    "guest_properties": _source("Properties of a Microsoft Entra B2B collaboration user", "https://learn.microsoft.com/en-us/entra/external-id/user-properties"),
    "sspr_scope": _source("How Microsoft Entra self-service password reset works", "https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks"),
    "sspr_methods": _source("Authentication methods for Microsoft Entra ID", "https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods"),
    "sspr_licensing": _source("Licensing requirements for Microsoft Entra self-service password reset", "https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing"),
    "rbac_definitions": _source("Understand Azure role definitions", "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions"),
    "rbac_general_roles": _source("Azure built-in general roles", "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general"),
    "rbac_privileged_roles": _source("Azure built-in privileged roles", "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged"),
    "rbac_best_practices": _source("Best practices for Azure RBAC", "https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices"),
    "rbac_scope": _source("Understand scope for Azure RBAC", "https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview"),
    "rbac_assign_cli": _source("Assign Azure roles using Azure CLI", "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli"),
    "rbac_list_cli": _source("List Azure role assignments using Azure CLI", "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli"),
    "rbac_deny": _source("Understand Azure deny assignments", "https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments"),
    "resource_groups_cli": _source("Manage Azure resource groups by using Azure CLI", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli"),
    "subscriptions_cli": _source("Manage Azure subscriptions with Azure CLI", "https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli"),
    "management_groups": _source("Azure management group hierarchy", "https://learn.microsoft.com/en-us/azure/governance/management-groups/overview"),
    "resource_tags": _source("Use tags to organize Azure resources", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli"),
    "resource_locks": _source("Lock Azure resources to protect infrastructure", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources"),
    "resource_moves": _source("Move Azure resources to a new resource group or subscription", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription"),
    "policy_overview": _source("Azure Policy overview", "https://learn.microsoft.com/en-us/azure/governance/policy/overview"),
    "policy_initiatives": _source("Azure Policy initiative definition structure", "https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure"),
    "policy_compliance": _source("Get Azure Policy compliance data", "https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data"),
    "policy_effects": _source("Understand Azure Policy effects", "https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics"),
    "policy_remediation": _source("Remediate noncompliant resources with Azure Policy", "https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources"),
    "policy_scope": _source("Azure Policy assignment scope", "https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope"),
    "budgets": _source("Tutorial for creating Azure budgets", "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets"),
    "advisor_cost": _source("Azure Advisor cost recommendations", "https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations"),

    # Storage
    "storage_create": _source("Create an Azure storage account", "https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create"),
    "storage_redundancy": _source("Azure Storage redundancy", "https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy"),
    "storage_secure_transfer": _source("Require secure transfer for Azure Storage", "https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer"),
    "storage_tls": _source("Configure a minimum TLS version for Azure Storage", "https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version"),
    "storage_shared_key": _source("Prevent Shared Key authorization for Azure Storage", "https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent"),
    "storage_keys": _source("Manage Azure Storage account access keys", "https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage"),
    "storage_encryption": _source("Azure Storage encryption for data at rest", "https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption"),
    "storage_firewall": _source("Configure Azure Storage firewalls and virtual networks", "https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security"),
    "sas_overview": _source("Grant limited access with shared access signatures", "https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview"),
    "user_delegation_sas": _source("Create a user delegation SAS with Azure CLI", "https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli"),
    "sas_expiration": _source("Create an expiration policy for shared access signatures", "https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy"),
    "stored_access_policy": _source("Define a stored access policy", "https://learn.microsoft.com/en-us/rest/api/storageservices/define-stored-access-policy"),
    "blob_anonymous": _source("Configure anonymous read access for containers and blobs", "https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure"),
    "blob_tiers": _source("Access tiers for blob data", "https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview"),
    "blob_lifecycle": _source("Azure Blob Storage lifecycle management overview", "https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview"),
    "blob_protection": _source("Azure Blob Storage data protection overview", "https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview"),
    "container_soft_delete": _source("Soft delete for containers", "https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview"),
    "blob_versioning": _source("Blob versioning", "https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview"),
    "object_replication": _source("Object replication for block blobs", "https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview"),
    "azcopy": _source("Transfer data with AzCopy", "https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10"),
    "files_create": _source("Create an Azure file share", "https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share"),
    "files_plan": _source("Plan for an Azure Files deployment", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning"),
    "files_identity": _source("Identity-based authentication for Azure Files", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview"),
    "files_permissions": _source("Assign share-level permissions for Azure Files", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions"),
    "files_acl": _source("Configure directory and file-level permissions for Azure Files", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-configure-file-level-permissions"),
    "files_network": _source("Azure Files networking considerations", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-overview"),
    "files_snapshots": _source("Azure Files snapshots", "https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files"),
    "files_soft_delete": _source("Prevent accidental deletion of Azure file shares", "https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion"),
    "azcopy_files": _source("Use AzCopy with Azure Files", "https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-files"),
    "files_smb_troubleshoot": _source("Troubleshoot Azure Files SMB connectivity", "https://learn.microsoft.com/en-us/troubleshoot/azure/azure-storage/files/connectivity/files-troubleshoot-smb-connectivity"),

    # Compute
    "bicep_overview": _source("Bicep language overview", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview"),
    "bicep_parameters": _source("Parameters in Bicep", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters"),
    "bicep_variables": _source("Variables in Bicep", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables"),
    "bicep_outputs": _source("Outputs in Bicep", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs"),
    "bicep_dependencies": _source("Resource dependencies in Bicep", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies"),
    "bicep_what_if": _source("Bicep what-if deployment operation", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if"),
    "bicep_deploy": _source("Deploy Bicep files with Azure CLI", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli"),
    "bicep_decompile": _source("Decompile ARM templates to Bicep", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile"),
    "arm_templates": _source("ARM template structure and syntax", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax"),
    "vm_images": _source("Find Azure Marketplace image information with Azure CLI", "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage"),
    "vm_create": _source("Create a Linux virtual machine with Azure CLI", "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli"),
    "vm_host_encryption": _source("Encryption at host for Azure virtual machines", "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli"),
    "vm_disks_overview": _source("Managed disks overview", "https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview"),
    "vm_disk_types": _source("Azure managed disk types", "https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types"),
    "vm_attach_disk": _source("Add a data disk to a Linux virtual machine with Azure CLI", "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/add-disk"),
    "vm_sizes": _source("Virtual machine sizes in Azure", "https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview"),
    "vm_resize": _source("Resize an Azure virtual machine", "https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm"),
    "vm_states": _source("Azure virtual machine states and billing status", "https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing"),
    "vm_snapshots": _source("Tutorial - Manage Azure disks with the Azure CLI", "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks"),
    "availability_zones": _source("Azure availability zones overview", "https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview"),
    "availability_sets": _source("Azure virtual machine availability sets", "https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview"),
    "vmss_flexible": _source("Flexible orchestration for Virtual Machine Scale Sets", "https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/flexible-virtual-machine-scale-sets"),
    "vmss_modes": _source("Orchestration modes for Virtual Machine Scale Sets", "https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes"),
    "vmss_autoscale": _source("Autoscale a Virtual Machine Scale Set", "https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview"),
    "vm_quota": _source("Check virtual machine vCPU quotas", "https://learn.microsoft.com/en-us/azure/quotas/per-vm-quota-requests"),
    "vm_move": _source("Move guidance for virtual machines", "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/virtual-machines-move-limitations"),
    "resource_mover": _source("Move Azure resources to another region", "https://learn.microsoft.com/en-us/azure/resource-mover/overview"),
    "vm_reliability": _source("Reliability in Azure Virtual Machines", "https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines"),
    "acr_tiers": _source("Azure Container Registry service tiers", "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus"),
    "acr_tags": _source("Container image tags and versioning", "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version"),
    "acr_auth": _source("Authenticate with an Azure container registry", "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication"),
    "acr_import": _source("Import container images into a registry", "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-import-images"),
    "aci_groups": _source("Azure Container Instances container groups", "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-groups"),
    "aci_create": _source("Create a container instance with Azure CLI", "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart"),
    "aci_env": _source("Set environment variables in Azure Container Instances", "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-environment-variables"),
    "aci_restart": _source("Azure Container Instances restart policies", "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-restart-policy"),
    "aci_limits": _source("Azure Container Instances resource availability", "https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability"),
    "container_apps_environment": _source("Azure Container Apps environments", "https://learn.microsoft.com/en-us/azure/container-apps/environment"),
    "container_apps_revisions": _source("Azure Container Apps revisions", "https://learn.microsoft.com/en-us/azure/container-apps/revisions"),
    "container_apps_ingress": _source("Azure Container Apps ingress", "https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview"),
    "container_apps_scale": _source("Set scaling rules in Azure Container Apps", "https://learn.microsoft.com/en-us/azure/container-apps/scale-app"),
    "container_apps_secrets": _source("Manage secrets in Azure Container Apps", "https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets"),
    "app_service_plans": _source("Azure App Service plans overview", "https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans"),
    "app_service_scale_up": _source("Scale up an App Service plan", "https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up"),
    "app_service_automatic_scale": _source("App Service automatic scaling", "https://learn.microsoft.com/en-us/azure/app-service/manage-automatic-scaling"),
    "app_service_slots": _source("Set up staging environments in App Service", "https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots"),
    "app_service_cli": _source("Azure CLI reference for App Service web apps", "https://learn.microsoft.com/en-us/cli/azure/webapp?view=azure-cli-latest"),
    "app_service_per_app": _source("Per-app scaling for App Service", "https://learn.microsoft.com/en-us/azure/app-service/manage-scale-per-app"),
    "app_service_tls": _source("Secure an App Service custom DNS name with TLS", "https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings"),
    "app_service_domain": _source("Map a custom DNS name to App Service", "https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain"),
    "app_service_backup": _source("Back up an App Service app", "https://learn.microsoft.com/en-us/azure/app-service/manage-backup"),
    "app_service_vnet": _source("Integrate an App Service app with an Azure virtual network", "https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration"),
    "app_service_private": _source("Use private endpoints for App Service", "https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint"),
    "app_service_restrictions": _source("Set up App Service access restrictions", "https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions"),

    # Networking
    "vnet_plan": _source("Plan Azure virtual networks", "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm"),
    "vnet_peering": _source("Create or change virtual network peering", "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering"),
    "public_ip": _source("Azure public IP addresses", "https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses"),
    "vnet_dns": _source("Azure virtual network name resolution", "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances"),
    "nsg": _source("Azure network security groups", "https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview"),
    "asg": _source("Azure application security groups", "https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups"),
    "routes": _source("Azure virtual network traffic routing", "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview"),
    "ip_flow": _source("Network Watcher IP flow verify", "https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview"),
    "service_endpoints": _source("Virtual network service endpoints", "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview"),
    "private_endpoint": _source("Azure Private Endpoint overview", "https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview"),
    "private_endpoint_dns": _source("Azure Private Endpoint DNS configuration", "https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns"),
    "private_dns": _source("Azure Private DNS zones", "https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone"),
    "dns_start": _source("Host a DNS zone in Azure DNS", "https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-cli"),
    "dns_delegate": _source("Delegate a domain to Azure DNS", "https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation"),
    "dns_records": _source("Azure DNS records and record sets", "https://learn.microsoft.com/en-us/azure/dns/dns-zones-records"),
    "bastion_cli": _source("Create an Azure Bastion host with Azure CLI", "https://learn.microsoft.com/en-us/azure/bastion/create-host-cli"),
    "load_balancer_components": _source("Azure Load Balancer components", "https://learn.microsoft.com/en-us/azure/load-balancer/components"),
    "load_balancer_probe": _source("Troubleshoot Azure Load Balancer health probes", "https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-troubleshoot-health-probe-status"),
    "load_balancer_outbound": _source("Outbound rules for Azure Load Balancer", "https://learn.microsoft.com/en-us/azure/load-balancer/outbound-rules"),
    "load_balancer_distribution": _source("Configure Azure Load Balancer distribution mode", "https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode"),
    "connection_troubleshoot": _source("Network Watcher connection troubleshoot", "https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview"),
    "connection_monitor": _source("Network Watcher Connection Monitor", "https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview"),

    # Monitoring and recovery
    "monitor_data": _source("Azure Monitor data platform", "https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform"),
    "monitor_metrics": _source("Azure Monitor metrics overview", "https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/data-platform-metrics"),
    "monitor_diagnostics": _source("Diagnostic settings in Azure Monitor", "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings"),
    "log_analytics": _source("Log Analytics workspace overview", "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview"),
    "kql_queries": _source("Log queries in Azure Monitor", "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-query-overview"),
    "log_ingestion": _source("Log data ingestion time in Azure Monitor", "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time"),
    "monitor_insights": _source("Insights and curated visualizations in Azure Monitor", "https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview"),
    "monitor_cost": _source("Azure Monitor Logs cost calculations and options", "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs"),
    "metric_alerts": _source("Azure Monitor metric alerts", "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types"),
    "action_groups": _source("Azure Monitor action groups", "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups"),
    "alert_processing": _source("Azure Monitor alert processing rules", "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules"),
    "activity_alerts": _source("Azure Monitor activity log alerts", "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log"),
    "dynamic_thresholds": _source("Dynamic thresholds in Azure Monitor metric alerts", "https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds"),
    "recovery_vault": _source("Create a Recovery Services vault", "https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault"),
    "backup_vault": _source("Create and manage an Azure Backup vault", "https://learn.microsoft.com/en-us/azure/backup/create-manage-backup-vault"),
    "backup_policy": _source("Azure Backup policy fundamentals", "https://learn.microsoft.com/en-us/azure/backup/backup-architecture"),
    "backup_vm": _source("Back up Azure virtual machines with Azure CLI", "https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli"),
    "backup_restore_vm": _source("Restore Azure virtual machines", "https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms"),
    "backup_restore_files": _source("Recover files from an Azure virtual machine backup", "https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm"),
    "backup_soft_delete": _source("Soft delete for Azure Backup", "https://learn.microsoft.com/en-us/azure/backup/backup-azure-security-feature-cloud"),
    "backup_monitor": _source("Monitor Azure Backup", "https://learn.microsoft.com/en-us/azure/backup/backup-azure-monitoring-built-in-monitor"),
    "asr_architecture": _source("Azure-to-Azure disaster recovery architecture", "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-architecture"),
    "asr_enable": _source("Set up disaster recovery for an Azure VM", "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-how-to-enable-replication"),
    "asr_drill": _source("Run an Azure Site Recovery disaster recovery drill", "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill"),
    "asr_failover": _source("Fail over and fail back Azure virtual machines", "https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failover-failback"),
}


# The ten entries correspond to Q01/Q11/Q21/Q31/Q41 through
# Q10/Q20/Q30/Q40/Q50 respectively.
LAB_CONCEPT_SOURCE_KEYS: dict[str, tuple[str, ...]] = {
    "01": ("entra_domains", "entra_user_cli", "entra_user_resource", "entra_user_resource", "entra_group_cli", "entra_group_member_cli", "entra_group_owner_cli", "entra_user_resource", "entra_restore_user", "entra_user_resource"),
    "02": ("license_capacity", "license_user", "license_user", "license_group", "guest_invitation", "guest_redemption", "guest_properties", "sspr_scope", "sspr_methods", "sspr_licensing"),
    "03": ("rbac_definitions", "rbac_general_roles", "rbac_general_roles", "rbac_privileged_roles", "rbac_best_practices", "rbac_scope", "rbac_scope", "rbac_assign_cli", "rbac_list_cli", "rbac_deny"),
    "04": ("resource_groups_cli", "subscriptions_cli", "management_groups", "management_groups", "resource_tags", "resource_tags", "resource_locks", "resource_locks", "resource_moves", "resource_groups_cli"),
    "05": ("policy_overview", "policy_initiatives", "policy_compliance", "policy_effects", "policy_remediation", "budgets", "budgets", "budgets", "advisor_cost", "policy_scope"),
    "06": ("storage_create", "storage_create", "storage_redundancy", "storage_redundancy", "storage_redundancy", "storage_secure_transfer", "storage_tls", "storage_shared_key", "storage_keys", "storage_encryption"),
    "07": ("storage_firewall", "storage_firewall", "storage_firewall", "storage_firewall", "sas_overview", "user_delegation_sas", "sas_expiration", "stored_access_policy", "stored_access_policy", "storage_shared_key"),
    "08": ("blob_anonymous", "blob_tiers", "blob_lifecycle", "blob_lifecycle", "blob_lifecycle", "blob_protection", "container_soft_delete", "blob_versioning", "object_replication", "azcopy"),
    "09": ("files_create", "files_plan", "files_identity", "files_permissions", "files_acl", "files_network", "files_snapshots", "files_soft_delete", "azcopy_files", "files_smb_troubleshoot"),
    "10": ("bicep_overview", "bicep_parameters", "bicep_variables", "bicep_outputs", "bicep_dependencies", "bicep_what_if", "bicep_deploy", "bicep_overview", "bicep_decompile", "arm_templates"),
    "11": ("vm_images", "vm_create", "vm_host_encryption", "vm_disks_overview", "vm_disk_types", "vm_attach_disk", "vm_sizes", "vm_resize", "vm_states", "vm_snapshots"),
    "12": ("availability_zones", "availability_sets", "vmss_flexible", "vmss_modes", "vmss_autoscale", "vm_quota", "vm_move", "vm_move", "resource_mover", "vm_reliability"),
    "13": ("acr_tiers", "acr_tags", "acr_auth", "acr_import", "aci_groups", "aci_create", "aci_env", "aci_restart", "aci_limits", "acr_auth"),
    "14": ("container_apps_environment", "container_apps_revisions", "container_apps_revisions", "container_apps_revisions", "container_apps_revisions", "container_apps_ingress", "container_apps_ingress", "container_apps_scale", "container_apps_scale", "container_apps_secrets"),
    "15": ("app_service_plans", "app_service_plans", "app_service_scale_up", "app_service_automatic_scale", "app_service_automatic_scale", "app_service_slots", "app_service_slots", "app_service_slots", "app_service_cli", "app_service_per_app"),
    "16": ("app_service_tls", "app_service_tls", "app_service_tls", "app_service_domain", "app_service_domain", "app_service_backup", "app_service_backup", "app_service_vnet", "app_service_private", "app_service_restrictions"),
    "17": ("vnet_plan", "vnet_plan", "vnet_peering", "vnet_peering", "vnet_peering", "public_ip", "public_ip", "public_ip", "vnet_dns", "vnet_peering"),
    "18": ("nsg", "nsg", "nsg", "asg", "nsg", "routes", "routes", "routes", "routes", "ip_flow"),
    "19": ("service_endpoints", "service_endpoints", "service_endpoints", "private_endpoint", "private_endpoint_dns", "private_endpoint_dns", "private_dns", "private_endpoint", "private_endpoint", "service_endpoints"),
    "20": ("dns_start", "dns_delegate", "dns_records", "dns_records", "dns_records", "dns_records", "bastion_cli", "bastion_cli", "bastion_cli", "bastion_cli"),
    "21": ("load_balancer_components", "load_balancer_components", "load_balancer_probe", "load_balancer_components", "load_balancer_probe", "load_balancer_outbound", "load_balancer_distribution", "load_balancer_probe", "connection_troubleshoot", "connection_monitor"),
    "22": ("monitor_data", "monitor_metrics", "monitor_diagnostics", "monitor_diagnostics", "log_analytics", "kql_queries", "log_ingestion", "monitor_insights", "connection_monitor", "monitor_cost"),
    "23": ("metric_alerts", "metric_alerts", "action_groups", "action_groups", "alert_processing", "alert_processing", "activity_alerts", "metric_alerts", "dynamic_thresholds", "metric_alerts"),
    "24": ("recovery_vault", "backup_vault", "backup_policy", "backup_vm", "backup_vm", "backup_restore_vm", "backup_restore_files", "backup_restore_vm", "backup_soft_delete", "backup_monitor"),
    "25": ("asr_architecture", "asr_architecture", "asr_enable", "asr_architecture", "asr_enable", "asr_enable", "asr_drill", "asr_failover", "asr_failover", "asr_failover"),
}


def expected_source(lab_number: str, question_number: int) -> dict[str, str]:
    """Return a copy of the direct source for a question's concept."""
    concept_index = (question_number - 1) % 10
    key = LAB_CONCEPT_SOURCE_KEYS[lab_number][concept_index]
    return dict(SOURCE_CATALOG[key])


def validate_source_contract() -> list[str]:
    """Return internal contract errors without reading assessment content."""
    errors: list[str] = []
    for lab_number, keys in LAB_CONCEPT_SOURCE_KEYS.items():
        if len(keys) != 10:
            errors.append(f"Lab {lab_number} maps {len(keys)} concepts instead of 10")
        for key in keys:
            if key not in SOURCE_CATALOG:
                errors.append(f"Lab {lab_number} references unknown source key {key}")
    return errors
