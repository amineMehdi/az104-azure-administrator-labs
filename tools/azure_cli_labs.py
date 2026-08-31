#!/usr/bin/env python3
"""Normalize every lab to Azure CLI commands hosted by PowerShell.

The repository command contract is singular: each lab has one ``scripts/cli``
lane containing four ``.ps1`` files, and cloud operations in those files are
performed by ``az`` or ``az rest``.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

import yaml

from sync_inline_commands import sync_lab


ROOT = Path(__file__).resolve().parents[1]
LABS_ROOT = ROOT / "labs"
LAB_PATTERN = re.compile(r"^(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
TENANT_LABS = {"01", "02"}
LOCAL_ONLY_LABS = {"00"}


def ps_array(values: list[str]) -> str:
    return "\n".join(f"    '{value.replace(chr(39), chr(39) * 2)}'" for value in values)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content.replace("\r\n", "\n").rstrip() + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(normalized)


def render(template: str, **values: object) -> str:
    for key, value in values.items():
        template = template.replace(f"__{key.upper()}__", str(value))
    return template


COMMON_HEADER = r'''#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
__PARAMETERS__
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Install it, run az login deliberately, and retry.'
}
'''


def preflight_script(number: str, metadata: dict) -> str:
    providers = list((metadata.get("providers") or {}).get("observed") or [])
    parameters = """    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location"""
    body = render(COMMON_HEADER, parameters=parameters)
    role = "; ".join(
        (metadata.get("permissions") or {}).get("azureRbacRoles")
        or (metadata.get("permissions") or {}).get("entraRoles")
        or ["See lab metadata"]
    )
    body += render(
        r'''
$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and $account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. This script will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }

Write-Host 'Lab: LAB-__LAB__'
Write-Host "Tenant: $($account.tenantId)"
Write-Host "Subscription: $SubscriptionId"
Write-Host "Location: $Location"
Write-Host 'Cost class: __COST__'
Write-Host 'Role boundary: __ROLE__'

$providers = @(
__PROVIDERS__
)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $registrationState) { $registrationState = 'Unavailable' }
    Write-Host ('Provider {0,-38} {1}' -f $provider, $registrationState)
}

if ('__SCOPE__' -eq 'tenant') {
    $null = az account get-access-token --resource-type ms-graph --query expiresOn --output tsv
    Write-Host 'Microsoft Graph access through Azure CLI is available.'
}
Write-Host 'Preflight is read-only. It does not sign in, switch context, register providers, or create resources.'
''',
        lab=number,
        cost=(metadata.get("cost") or {}).get("class", "unknown"),
        role=role,
        providers=ps_array(providers),
        scope="tenant" if number in TENANT_LABS else "subscription",
    )
    return body


AZURE_CLI_ACTIONS: dict[str, str] = {
    "01": r'''
if (-not $env:AZ104_LAB_INITIAL_PASSWORD -or $env:AZ104_LAB_INITIAL_PASSWORD.Length -lt 12) {
    throw 'Set AZ104_LAB_INITIAL_PASSWORD to a policy-compliant temporary password of at least 12 characters.'
}

if (-not $env:AZ104_TENANT_DOMAIN) { throw 'Set AZ104_TENANT_DOMAIN to a verified tenant domain.' }
$domain = $env:AZ104_TENANT_DOMAIN
$aliases = @("az104l01a$suffix", "az104l01b$suffix")
$displayNames = @("AZ104-L01-$RunId-Alex", "AZ104-L01-$RunId-Blair")
$userIds = @()
for ($index = 0; $index -lt 2; $index++) {
    $upn = "$($aliases[$index])@$domain"
    $secretPath = Join-Path $StateDir ".user-$index.json"
    $body = [ordered]@{
        accountEnabled = $true
        displayName = $displayNames[$index]
        mailNickname = $aliases[$index]
        userPrincipalName = $upn
        passwordProfile = [ordered]@{ forceChangePasswordNextSignIn = $true; password = $env:AZ104_LAB_INITIAL_PASSWORD }
    }
    try {
        $body | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $secretPath -Encoding utf8
        $created = az rest --method post --url 'https://graph.microsoft.com/v1.0/users' --body "@$secretPath" --output json | ConvertFrom-Json
    }
    finally {
        Remove-Item -LiteralPath $secretPath -Force -ErrorAction SilentlyContinue
    }
    $userIds += [string]$created.id
}
$group = az ad group create --display-name "AZ104-L01-$RunId-Operators" --mail-nickname "az104l01g$suffix" --output json | ConvertFrom-Json
az ad group member add --group $group.id --member-id $userIds[0] --output none
az ad group owner add --group $group.id --owner-object-id $userIds[1] --output none
$state.external['userIds'] = @($userIds)
$state.external['groupId'] = [string]$group.id
Remove-Item Env:AZ104_LAB_INITIAL_PASSWORD -ErrorAction SilentlyContinue
''',
    "02": r'''
$group = az ad group create --display-name "AZ104-L02-$RunId-SSPR-Pilot" --mail-nickname "az104l02$suffix" --output json | ConvertFrom-Json
$state.external['groupId'] = [string]$group.id
if ($env:AZ104_GUEST_EMAIL) {
    $inviteBody = @{ invitedUserEmailAddress = $env:AZ104_GUEST_EMAIL; inviteRedirectUrl = 'https://myapps.microsoft.com'; sendInvitationMessage = $false } | ConvertTo-Json -Compress
    $invitation = az rest --method post --url 'https://graph.microsoft.com/v1.0/invitations' --body $inviteBody --output json | ConvertFrom-Json
    $state.external['guestUserId'] = [string]$invitation.invitedUser.id
}
if ($env:AZ104_LICENSE_SKU_ID -and $state.external.guestUserId) {
    $licenseBody = @{ addLicenses = @(@{ skuId = $env:AZ104_LICENSE_SKU_ID }); removeLicenses = @() } | ConvertTo-Json -Depth 6 -Compress
    az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($state.external.guestUserId)/assignLicense" --body $licenseBody --output none
    $state.external['licenseSkuId'] = $env:AZ104_LICENSE_SKU_ID
}
if ($env:AZ104_ALLOW_SSPR_POLICY_CHANGE -eq 'YES') {
    $policy = az rest --method get --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --output json | ConvertFrom-Json
    $state.external['originalAllowedToUseSspr'] = [bool]$policy.allowedToUseSspr
    az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body '{"allowedToUseSspr":true}' --output none
    $state.external['ssprChanged'] = $true
}
''',
    "03": r'''
if (-not $env:AZ104_PRINCIPAL_OBJECT_ID) { throw 'Set AZ104_PRINCIPAL_OBJECT_ID to a disposable principal object ID.' }
$scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
$assignment = az role assignment create --assignee-object-id $env:AZ104_PRINCIPAL_OBJECT_ID --assignee-principal-type ServicePrincipal --role Reader --scope $scope --output json | ConvertFrom-Json
$state.external['roleAssignmentId'] = [string]$assignment.id
$state.external['principalObjectId'] = $env:AZ104_PRINCIPAL_OBJECT_ID
$null = az role definition list --name Reader --output json
$null = az role definition list --name Contributor --output json
''',
    "04": r'''
az lock create --name "lock-$RunId" --lock-type CanNotDelete --resource-group $ResourceGroupName --notes "AZ-104 Lab 04 run $RunId" --output none
az group update --name $ResourceGroupName --set tags.stage=managed tags.costCenter=training --output none
if ($env:AZ104_ALLOW_MANAGEMENT_GROUP_CHANGE -eq 'YES') {
    $managementGroup = "mg-az104-$suffix"
    az account management-group create --name $managementGroup --display-name "AZ104 $RunId" --output none
    $state.external['managementGroup'] = $managementGroup
}
''',
    "05": r'''
$definitionId = az policy definition list --query "[?displayName=='Require a tag and its value on resources'].id | [0]" --output tsv
if (-not $definitionId) { throw 'Required built-in policy definition was not found.' }
$scope = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName"
$parameters = '{"tagName":{"value":"purpose"},"tagValue":{"value":"az104-lab"}}'
$assignment = az policy assignment create --name "require-purpose-$suffix" --display-name "AZ104 require purpose $RunId" --scope $scope --policy $definitionId --params $parameters --output json | ConvertFrom-Json
$state.external['policyAssignmentId'] = [string]$assignment.id
az policy state trigger-scan --resource-group $ResourceGroupName --no-wait
$null = az advisor recommendation list --category Cost --output json
''',
    "06": r'''
$storage = "st06$suffix"
az storage account create --name $storage --resource-group $ResourceGroupName --location $Location --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --tags purpose=az104-lab labId=06 runId=$RunId --output none
az storage account keys renew --resource-group $ResourceGroupName --account-name $storage --key secondary --output none
''',
    "07": r'''
$vnet = "vnet-$suffix"; $storage = "st07$suffix"
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.7.0.0/16 --subnet-name storage --subnet-prefixes 10.7.1.0/24 --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name storage --service-endpoints Microsoft.Storage --output none
$subnetId = az network vnet subnet show --resource-group $ResourceGroupName --vnet-name $vnet --name storage --query id --output tsv
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --default-action Deny --output none
az storage account network-rule add --resource-group $ResourceGroupName --account-name $storage --subnet $subnetId --output none
az storage container create --name private --account-name $storage --auth-mode login --output none
$start = (Get-Date).ToUniversalTime().AddMinutes(-5).ToString('yyyy-MM-ddTHH:mmZ')
$expiry = (Get-Date).ToUniversalTime().AddHours(2).ToString('yyyy-MM-ddTHH:mmZ')
az storage container policy create --account-name $storage --container-name private --name az104 --permissions rwl --start $start --expiry $expiry --auth-mode login --output none
$null = az storage container generate-sas --account-name $storage --name private --policy-name az104 --auth-mode login --as-user --output none
''',
    "08": r'''
$source = "st08a$suffix"; $destination = "st08b$suffix"
foreach ($account in @($source, $destination)) {
    az storage account create --name $account --resource-group $ResourceGroupName --location $Location --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --enable-change-feed true --enable-versioning true --output none
    az storage account blob-service-properties update --account-name $account --resource-group $ResourceGroupName --enable-delete-retention true --delete-retention-days 7 --enable-container-delete-retention true --container-delete-retention-days 7 --output none
}
az storage container create --name source --account-name $source --auth-mode login --output none
az storage container create --name destination --account-name $destination --auth-mode login --output none
$policyPath = Join-Path $StateDir 'lifecycle-policy.json'
'{"rules":[{"enabled":true,"name":"cool-after-30","type":"Lifecycle","definition":{"actions":{"baseBlob":{"tierToCool":{"daysAfterModificationGreaterThan":30}}},"filters":{"blobTypes":["blockBlob"]}}}]}' | Set-Content -LiteralPath $policyPath -Encoding utf8
az storage account management-policy create --account-name $source --resource-group $ResourceGroupName --policy "@$policyPath" --output none
''',
    "09": r'''
$storage = "st09$suffix"
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false --output none
az storage share create --name files --account-name $storage --quota 20 --auth-mode login --output none
az storage account file-service-properties update --resource-group $ResourceGroupName --account-name $storage --enable-delete-retention true --delete-retention-days 7 --output none
az storage share snapshot --name files --account-name $storage --auth-mode login --output none
''',
    "10": r'''
$storage = "st10$suffix"
az bicep build --file "$LabRoot/artifacts/main.bicep" --outfile "$StateDir/main.json"
az deployment group what-if --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters storageName=$storage --result-format ResourceIdOnly --no-pretty-print | Set-Content -LiteralPath "$StateDir/what-if.txt"
az deployment group create --name "deploy-$RunId" --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters storageName=$storage --output none
az group export --name $ResourceGroupName --output json | Set-Content -LiteralPath "$StateDir/exported-template.json"
''',
    "11": r'''
$vnet = "vnet-$suffix"; $vm = "vm-$suffix"; $disk = "disk-$suffix"
$keyPath = Join-Path $StateDir 'id_ed25519'
ssh-keygen -t ed25519 -N '' -f $keyPath | Out-Null
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.11.0.0/16 --subnet-name workload --subnet-prefixes 10.11.1.0/24 --output none
az vm create --resource-group $ResourceGroupName --name $vm --image Ubuntu2204 --size Standard_B1s --admin-username azureadmin --ssh-key-values "$keyPath.pub" --vnet-name $vnet --subnet workload --public-ip-address '""' --nsg-rule NONE --output none
az disk create --resource-group $ResourceGroupName --name $disk --size-gb 8 --sku Standard_LRS --output none
az vm disk attach --resource-group $ResourceGroupName --vm-name $vm --name $disk --caching ReadWrite --output none
''',
    "12": r'''
$availabilitySet = "avset-$suffix"; $vnet = "vnet-$suffix"; $vmss = "vmss-$suffix"
az vm availability-set create --resource-group $ResourceGroupName --name $availabilitySet --location $Location --platform-fault-domain-count 2 --platform-update-domain-count 5 --output none
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.12.0.0/16 --subnet-name vmss --subnet-prefixes 10.12.1.0/24 --output none
az vmss create --resource-group $ResourceGroupName --name $vmss --image Ubuntu2204 --vm-sku Standard_B1s --instance-count 1 --upgrade-policy-mode Manual --admin-username azureadmin --generate-ssh-keys --vnet-name $vnet --subnet vmss --output none
''',
    "13": r'''
$registry = "acr13$suffix"; $container = "aci-$suffix"
az acr create --resource-group $ResourceGroupName --name $registry --sku Basic --admin-enabled false --output none
az acr import --name $registry --source mcr.microsoft.com/azuredocs/aci-helloworld:latest --image az104/hello:v1 --output none
az container create --resource-group $ResourceGroupName --name $container --image mcr.microsoft.com/azuredocs/aci-helloworld:latest --cpu 1 --memory 1 --restart-policy OnFailure --ports 80 --ip-address Public --dns-name-label "aci-$suffix" --output none
''',
    "14": r'''
az extension add --name containerapp --upgrade --only-show-errors
$workspace = "law-$suffix"; $environment = "cae-$suffix"; $app = "ca-$suffix"
az monitor log-analytics workspace create --resource-group $ResourceGroupName --workspace-name $workspace --location $Location --output none
$customerId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query customerId --output tsv
$sharedKey = az monitor log-analytics workspace get-shared-keys --resource-group $ResourceGroupName --workspace-name $workspace --query primarySharedKey --output tsv
az containerapp env create --resource-group $ResourceGroupName --name $environment --location $Location --logs-workspace-id $customerId --logs-workspace-key $sharedKey --output none
Remove-Variable sharedKey -ErrorAction SilentlyContinue
az containerapp create --resource-group $ResourceGroupName --name $app --environment $environment --image mcr.microsoft.com/k8se/quickstart:latest --target-port 80 --ingress external --min-replicas 0 --max-replicas 3 --scale-rule-name http --scale-rule-http-concurrency 20 --env-vars LAB_RUN=$RunId --output none
''',
    "15": r'''
$plan = "plan-$suffix"; $app = "app-$suffix"
az appservice plan create --resource-group $ResourceGroupName --name $plan --is-linux --sku B1 --output none
az webapp create --resource-group $ResourceGroupName --plan $plan --name $app --runtime 'PYTHON:3.12' --output none
az webapp deployment slot create --resource-group $ResourceGroupName --name $app --slot staging --output none
az webapp config appsettings set --resource-group $ResourceGroupName --name $app --slot staging --settings LAB_STAGE=staging LAB_RUN=$RunId --output none
''',
    "16": r'''
$plan = "plan-$suffix"; $app = "app-$suffix"; $storage = "st16$suffix"; $vnet = "vnet-$suffix"
az appservice plan create --resource-group $ResourceGroupName --name $plan --is-linux --sku B1 --output none
az webapp create --resource-group $ResourceGroupName --plan $plan --name $app --runtime 'PYTHON:3.12' --output none
az webapp update --resource-group $ResourceGroupName --name $app --https-only true --set siteConfig.minTlsVersion=1.2 --output none
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.16.0.0/16 --subnet-name integration --subnet-prefixes 10.16.1.0/24 --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name integration --delegations Microsoft.Web/serverFarms --output none
az webapp vnet-integration add --resource-group $ResourceGroupName --name $app --vnet $vnet --subnet integration --output none
''',
    "17": r'''
$hub = "hub-$suffix"; $spoke = "spoke-$suffix"
az network vnet create --resource-group $ResourceGroupName --name $hub --address-prefixes 10.17.0.0/16 --subnet-name app --subnet-prefixes 10.17.1.0/24 --output none
az network vnet subnet create --resource-group $ResourceGroupName --vnet-name $hub --name management --address-prefixes 10.17.2.0/24 --output none
az network vnet create --resource-group $ResourceGroupName --name $spoke --address-prefixes 10.18.0.0/16 --subnet-name app --subnet-prefixes 10.18.1.0/24 --output none
az network vnet subnet create --resource-group $ResourceGroupName --vnet-name $spoke --name management --address-prefixes 10.18.2.0/24 --output none
$hubId = az network vnet show --resource-group $ResourceGroupName --name $hub --query id --output tsv
$spokeId = az network vnet show --resource-group $ResourceGroupName --name $spoke --query id --output tsv
az network vnet peering create --resource-group $ResourceGroupName --vnet-name $hub --name hub-to-spoke --remote-vnet $spokeId --output none
az network vnet peering create --resource-group $ResourceGroupName --vnet-name $spoke --name spoke-to-hub --remote-vnet $hubId --output none
az network public-ip create --resource-group $ResourceGroupName --name "pip-$suffix" --location $Location --sku Standard --allocation-method Static --output none
''',
    "18": r'''
$vnet = "vnet-$suffix"; $nsg = "nsg-$suffix"; $front = "asg-front-$suffix"; $back = "asg-back-$suffix"; $route = "rt-$suffix"
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.18.0.0/16 --subnet-name app --subnet-prefixes 10.18.1.0/24 --output none
az network nsg create --resource-group $ResourceGroupName --name $nsg --output none
az network asg create --resource-group $ResourceGroupName --name $front --location $Location --output none
az network asg create --resource-group $ResourceGroupName --name $back --location $Location --output none
az network nsg rule create --resource-group $ResourceGroupName --nsg-name $nsg --name AllowFrontendToBackend443 --priority 200 --direction Inbound --access Allow --protocol Tcp --source-asgs $front --destination-asgs $back --destination-port-ranges 443 --output none
az network route-table create --resource-group $ResourceGroupName --name $route --location $Location --output none
az network route-table route create --resource-group $ResourceGroupName --route-table-name $route --name DefaultToInternet --address-prefix 0.0.0.0/0 --next-hop-type Internet --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name app --network-security-group $nsg --route-table $route --output none
''',
    "19": r'''
$vnet = "vnet-$suffix"; $storage = "st19$suffix"; $endpoint = "pe-$suffix"
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.19.0.0/16 --subnet-name service --subnet-prefixes 10.19.1.0/24 --output none
az network vnet subnet update --resource-group $ResourceGroupName --vnet-name $vnet --name service --service-endpoints Microsoft.Storage --output none
az network vnet subnet create --resource-group $ResourceGroupName --vnet-name $vnet --name private --address-prefixes 10.19.2.0/24 --disable-private-endpoint-network-policies true --output none
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
$serviceSubnetId = az network vnet subnet show --resource-group $ResourceGroupName --vnet-name $vnet --name service --query id --output tsv
az storage account network-rule add --resource-group $ResourceGroupName --account-name $storage --subnet $serviceSubnetId --output none
$storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
az network private-endpoint create --resource-group $ResourceGroupName --name $endpoint --location $Location --vnet-name $vnet --subnet private --private-connection-resource-id $storageId --group-id blob --connection-name "conn-$suffix" --output none
az network private-dns zone create --resource-group $ResourceGroupName --name privatelink.blob.core.windows.net --output none
az network private-dns link vnet create --resource-group $ResourceGroupName --zone-name privatelink.blob.core.windows.net --name "link-$suffix" --virtual-network $vnet --registration-enabled false --output none
''',
    "20": r'''
$vnet = "vnet-$suffix"; $pip = "pip-$suffix"; $bastion = "bas-$suffix"; $zone = "lab$suffix.example.invalid"
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.20.0.0/16 --subnet-name AzureBastionSubnet --subnet-prefixes 10.20.0.0/26 --output none
az network public-ip create --resource-group $ResourceGroupName --name $pip --sku Standard --allocation-method Static --output none
az network bastion create --resource-group $ResourceGroupName --name $bastion --vnet-name $vnet --public-ip-address $pip --location $Location --sku Basic --output none
az network dns zone create --resource-group $ResourceGroupName --name $zone --output none
az network dns record-set a add-record --resource-group $ResourceGroupName --zone-name $zone --record-set-name app --ipv4-address 192.0.2.10 --output none
az network dns record-set txt add-record --resource-group $ResourceGroupName --zone-name $zone --record-set-name verify --value "az104-$RunId" --output none
''',
    "21": r'''
$vnet = "vnet-$suffix"; $pip = "pip-$suffix"; $loadBalancer = "lb-$suffix"
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.21.0.0/16 --subnet-name backend --subnet-prefixes 10.21.1.0/24 --output none
az network public-ip create --resource-group $ResourceGroupName --name $pip --location $Location --sku Standard --allocation-method Static --output none
az network lb create --resource-group $ResourceGroupName --name $loadBalancer --sku Standard --public-ip-address $pip --frontend-ip-name frontend --backend-pool-name backend --output none
az network lb probe create --resource-group $ResourceGroupName --lb-name $loadBalancer --name http --protocol Tcp --port 80 --interval 15 --threshold 2 --output none
az network lb rule create --resource-group $ResourceGroupName --lb-name $loadBalancer --name http --protocol Tcp --frontend-port 80 --backend-port 80 --frontend-ip-name frontend --backend-pool-name backend --probe-name http --idle-timeout 4 --output none
$null = az network watcher list --query "[?location=='$Location']" --output json
''',
    "22": r'''
$workspace = "law-$suffix"; $storage = "st22$suffix"
az monitor log-analytics workspace create --resource-group $ResourceGroupName --workspace-name $workspace --location $Location --retention-time 30 --output none
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --https-only true --allow-blob-public-access false --output none
$workspaceId = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
$storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
az monitor diagnostic-settings create --name "diag-$RunId" --resource $storageId --workspace $workspaceId --metrics '[{"category":"Transaction","enabled":true}]' --output none
''',
    "23": r'''
$storage = "st23$suffix"; $actionGroup = "ag-$suffix"; $alert = "alert-$suffix"
az storage account create --resource-group $ResourceGroupName --name $storage --location $Location --sku Standard_LRS --kind StorageV2 --output none
if ($env:AZ104_ALERT_EMAIL) {
    az monitor action-group create --resource-group $ResourceGroupName --name $actionGroup --short-name AZ104 --action email lab $env:AZ104_ALERT_EMAIL --output none
} else {
    az monitor action-group create --resource-group $ResourceGroupName --name $actionGroup --short-name AZ104 --output none
}
$storageId = az storage account show --resource-group $ResourceGroupName --name $storage --query id --output tsv
$actionId = az monitor action-group show --resource-group $ResourceGroupName --name $actionGroup --query id --output tsv
az monitor metrics alert create --resource-group $ResourceGroupName --name $alert --scopes $storageId --condition 'avg UsedCapacity > 1' --window-size 15m --evaluation-frequency 5m --action $actionId --description 'AZ-104 Lab 23 capacity signal' --output none
az monitor activity-log alert create --resource-group $ResourceGroupName --name "activity-$suffix" --scope $storageId --condition category=Administrative operationName=Microsoft.Storage/storageAccounts/write --action-group $actionId --output none
''',
    "24": r'''
$vault = "rsv-$suffix"; $backupVault = "bv-$suffix"
az backup vault create --resource-group $ResourceGroupName --name $vault --location $Location --output none
$state.external['recoveryVaultId'] = az backup vault show --resource-group $ResourceGroupName --name $vault --query id --output tsv
$properties = '{"storageSettings":[{"datastoreType":"VaultStore","type":"LocallyRedundant"}]}'
az resource create --resource-group $ResourceGroupName --resource-type Microsoft.DataProtection/backupVaults --name $backupVault --api-version 2023-01-01 --location $Location --properties $properties --output none
''',
    "25": r'''
if (-not $SecondaryLocation) { throw 'Supply -SecondaryLocation or set AZURE_SECONDARY_LOCATION.' }
az network vnet create --resource-group $ResourceGroupName --name "source-$suffix" --location $Location --address-prefixes 10.25.0.0/16 --subnet-name workload --subnet-prefixes 10.25.1.0/24 --output none
az network vnet create --resource-group $ResourceGroupName --name "recovery-$suffix" --location $SecondaryLocation --address-prefixes 10.26.0.0/16 --subnet-name recovery --subnet-prefixes 10.26.1.0/24 --output none
az backup vault create --resource-group $ResourceGroupName --name "asr-$suffix" --location $Location --output none
$state.external['recoveryVaultId'] = az backup vault show --resource-group $ResourceGroupName --name "asr-$suffix" --query id --output tsv
''',
    "26": r'''
$storage = "st26$suffix"
az bicep build --file "$LabRoot/artifacts/main.bicep" --outfile "$StateDir/main.json"
az deployment group what-if --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --result-format ResourceIdOnly --no-pretty-print | Set-Content -LiteralPath "$StateDir/what-if.txt"
az deployment group create --name "capstone-$RunId" --resource-group $ResourceGroupName --template-file "$LabRoot/artifacts/main.bicep" --parameters suffix=$suffix storageName=$storage --output none
''',
    "27": r'''
$workspace = "law-$suffix"; $vault = "rsv-$suffix"; $vnet = "vnet-$suffix"
az monitor log-analytics workspace create --resource-group $ResourceGroupName --workspace-name $workspace --location $Location --retention-time 30 --output none
az backup vault create --resource-group $ResourceGroupName --name $vault --location $Location --output none
az network vnet create --resource-group $ResourceGroupName --name $vnet --address-prefixes 10.27.0.0/16 --subnet-name workload --subnet-prefixes 10.27.1.0/24 --output none
$state.external['workspaceId'] = az monitor log-analytics workspace show --resource-group $ResourceGroupName --workspace-name $workspace --query id --output tsv
$state.external['recoveryVaultId'] = az backup vault show --resource-group $ResourceGroupName --name $vault --query id --output tsv
''',
}


def setup_script(number: str, metadata: dict) -> str:
    creates = metadata.get("creates") or {}
    resources = list(creates.get("azureResources") or creates.get("entraObjects") or [])
    parameters = """    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location,
    [string]$SecondaryLocation = $env:AZURE_SECONDARY_LOCATION,
    [switch]$Execute"""
    header = render(COMMON_HEADER, parameters=parameters)
    scope = "local" if number in LOCAL_ONLY_LABS else "tenant" if number in TENANT_LABS else "subscription"
    action = AZURE_CLI_ACTIONS.get(
        number, "Write-Host 'Continue with the documented guided checkpoints after this recorded baseline.'"
    )
    body = render(
        r'''
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$ResourceGroupName = "rg-az104-l__LAB__-$RunId"
$suffix = (($RunId -replace '[^a-z0-9]', '') + '000000000000').Substring(0, 12)

Write-Host 'LAB-__LAB__ plan'
Write-Host "  subscription: $SubscriptionId"
Write-Host "  location: $Location"
Write-Host '  scope: __SCOPE__'
Write-Host '  cost class: __COST__'
Write-Host '  resources: __RESOURCES__'
if (-not $Execute) {
    Write-Host 'Preview only. Re-run with -Execute after approving context, permissions, cost, and gates.'
    return
}

& (Join-Path $PSScriptRoot 'Preflight.ps1') -SubscriptionId $SubscriptionId -Location $Location
if (Test-Path -LiteralPath $Manifest) { throw "State already exists at $Manifest; choose a new run ID." }
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
$state = [ordered]@{
    labId = 'LAB-__LAB__'
    runId = $RunId
    tenantId = [string]$account.tenantId
    subscriptionId = $SubscriptionId
    location = $Location
    createdAt = (Get-Date).ToUniversalTime().ToString('o')
    status = 'recorded-before-mutation'
    resourceGroup = [ordered]@{ name = $null; id = $null }
    resources = @()
    external = [ordered]@{}
}
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8

if ('__SCOPE__' -eq 'subscription') {
    $expiresOn = (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd')
    az group create --subscription $SubscriptionId --name $ResourceGroupName --location $Location --tags purpose=az104-lab labId=__LAB__ runId=$RunId expiresOn=$expiresOn --output none
    $state.resourceGroup.name = $ResourceGroupName
    $state.resourceGroup.id = az group show --subscription $SubscriptionId --name $ResourceGroupName --query id --output tsv
    $state.status = 'baseline-created'
    $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
}

__ACTION__

if ('__SCOPE__' -eq 'subscription') {
    $state.resources = @(az resource list --subscription $SubscriptionId --resource-group $ResourceGroupName --output json | ConvertFrom-Json | ForEach-Object {
        [ordered]@{ id = $_.id; name = $_.name; type = $_.type; location = $_.location }
    })
}
$state.status = 'setup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host "Setup complete. State: $Manifest"
Write-Host 'Run Validate.ps1 before recording command evidence.'
''',
        lab=number,
        scope=scope,
        cost=(metadata.get("cost") or {}).get("class", "unknown"),
        resources=", ".join(resources) or "local state only",
        action=action.strip(),
    )
    return header + body


def validate_script(number: str, metadata: dict) -> str:
    expected_types = []
    for resource in (metadata.get("creates") or {}).get("azureResources") or []:
        if isinstance(resource, str) and "/" in resource:
            expected_types.append(resource)
    parameters = """    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId"""
    header = render(COMMON_HEADER, parameters=parameters)
    scope = "local" if number in LOCAL_ONLY_LABS else "tenant" if number in TENANT_LABS else "subscription"
    tenant_checks = ""
    if number == "01":
        tenant_checks = r'''
foreach ($userId in @($state.external.userIds)) {
    $user = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$userId" --output json 2>$null
    if ($LASTEXITCODE -eq 0 -and $user) { Add-Check "entra.user.$userId" pass 'The exact recorded user exists.' }
    else { Add-Check "entra.user.$userId" fail 'A recorded user is absent.' }
}
$group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output json 2>$null
if ($LASTEXITCODE -eq 0 -and $group) { Add-Check entra.group pass 'The exact recorded group exists.' }
else { Add-Check entra.group fail 'The recorded group is absent.' }
'''
    elif number == "02":
        tenant_checks = r'''
$group = az rest --method get --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output json 2>$null
if ($LASTEXITCODE -eq 0 -and $group) { Add-Check entra.group pass 'The exact recorded pilot group exists.' }
else { Add-Check entra.group fail 'The recorded pilot group is absent.' }
if ($state.external.guestUserId) {
    $guest = az rest --method get --url "https://graph.microsoft.com/v1.0/users/$($state.external.guestUserId)" --output json 2>$null
    if ($LASTEXITCODE -eq 0 -and $guest) { Add-Check entra.guest pass 'The exact invited guest exists.' }
    else { Add-Check entra.guest fail 'A guest ID was recorded but the guest is absent.' }
} else { Add-Check entra.guest skipped 'Guest invitation was gated because AZ104_GUEST_EMAIL was not supplied.' }
'''
    body = render(
        r'''
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$StateDir = Join-Path $LabRoot ".state/$RunId"
$Manifest = Join-Path $StateDir 'run.json'
$Report = Join-Path $StateDir 'validation.json'
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
if ($account.id -ne $SubscriptionId -or $state.subscriptionId -ne $SubscriptionId) { throw 'Active or recorded subscription mismatch.' }

$checks = [System.Collections.Generic.List[object]]::new()
function Add-Check([string]$Id, [ValidateSet('pass','fail','warning','skipped')][string]$Status, [string]$Message) {
    $checks.Add([ordered]@{ id = $Id; status = $Status; message = $Message })
}

if ('__SCOPE__' -eq 'local') {
    Add-Check state.local pass 'The manifest records a local-only bootstrap run.'
} elseif ('__SCOPE__' -eq 'tenant') {
__TENANT_CHECKS__
} else {
    $resourceGroup = az group show --subscription $SubscriptionId --name $state.resourceGroup.name --output json 2>$null | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0 -or -not $resourceGroup) {
        Add-Check context.resource-group fail 'The exact recorded resource group is absent.'
    } elseif ($resourceGroup.id -ne $state.resourceGroup.id) {
        Add-Check context.resource-group fail 'The resource-group ID differs from the manifest.'
    } else {
        Add-Check context.resource-group pass 'The exact recorded resource group exists.'
    }
    if ($resourceGroup.tags.purpose -eq 'az104-lab' -and $resourceGroup.tags.labId -eq '__LAB__' -and $resourceGroup.tags.runId -eq $RunId) {
        Add-Check ownership.tags pass 'purpose, labId, and runId tags match.'
    } else { Add-Check ownership.tags fail 'Ownership tags do not match.' }
    $resources = @(az resource list --subscription $SubscriptionId --resource-group $state.resourceGroup.name --output json | ConvertFrom-Json)
    $expectedTypes = @(
__EXPECTED_TYPES__
    )
    if ($expectedTypes.Count -eq 0) {
        Add-Check resources.boundary pass "The recorded boundary contains $($resources.Count) top-level resource(s)."
    }
    foreach ($type in $expectedTypes) {
        $count = @($resources | Where-Object type -EQ $type).Count
        if ($count -gt 0) { Add-Check ("resource." + ($type -replace '[/\.]','-')) pass "Found $count resource(s) of type $type." }
        else { Add-Check ("resource." + ($type -replace '[/\.]','-')) warning "No top-level $type was returned; inspect nested or gated state." }
    }
}

$failures = @($checks | Where-Object status -EQ fail).Count
$warnings = @($checks | Where-Object status -IN @('warning', 'skipped')).Count
$result = if ($failures -gt 0) { 'fail' } elseif ($warnings -gt 0) { 'partial' } else { 'pass' }
$output = [ordered]@{ labId = 'LAB-__LAB__'; runId = $RunId; generatedAt = (Get-Date).ToUniversalTime().ToString('o'); result = $result; checks = @($checks) }
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Report -Encoding utf8
$output | ConvertTo-Json -Depth 20
if ($result -eq 'fail') { exit 1 }
''',
        scope=scope,
        tenant_checks="\n".join("    " + line if line else line for line in tenant_checks.strip().splitlines()),
        lab=number,
        expected_types=ps_array(expected_types),
    )
    return header + body


def cleanup_script(number: str, metadata: dict) -> str:
    del metadata
    parameters = """    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$RunId,
    [switch]$Execute"""
    header = render(COMMON_HEADER, parameters=parameters)
    if number == "00":
        action = r'''
$runDirectory = Split-Path -Parent $Manifest
$resolvedRoot = [IO.Path]::GetFullPath((Join-Path $LabRoot '.state'))
$resolvedRun = [IO.Path]::GetFullPath($runDirectory)
if (-not $resolvedRun.StartsWith($resolvedRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Resolved cleanup target is outside the lab state directory.'
}
Remove-Item -LiteralPath $resolvedRun -Recurse -Force
Write-Host 'The selected local Lab 00 run was removed. No Azure resources were changed.'
return
'''
    elif number == "01":
        action = r'''
foreach ($userId in @($state.external.userIds)) { az rest --method delete --url "https://graph.microsoft.com/v1.0/users/$userId" --output none 2>$null }
if ($state.external.groupId) { az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output none 2>$null }
'''
    elif number == "02":
        action = r'''
if ($state.external.licenseSkuId -and $state.external.guestUserId) {
    $body = @{ addLicenses = @(); removeLicenses = @([string]$state.external.licenseSkuId) } | ConvertTo-Json -Depth 5 -Compress
    az rest --method post --url "https://graph.microsoft.com/v1.0/users/$($state.external.guestUserId)/assignLicense" --body $body --output none
}
if ($state.external.guestUserId) { az rest --method delete --url "https://graph.microsoft.com/v1.0/users/$($state.external.guestUserId)" --output none 2>$null }
if ($state.external.groupId) { az rest --method delete --url "https://graph.microsoft.com/v1.0/groups/$($state.external.groupId)" --output none 2>$null }
if ($state.external.ssprChanged -and $null -ne $state.external.originalAllowedToUseSspr) {
    $allowed = ([bool]$state.external.originalAllowedToUseSspr).ToString().ToLowerInvariant()
    az rest --method patch --url 'https://graph.microsoft.com/v1.0/policies/authorizationPolicy' --body "{`"allowedToUseSspr`":$allowed}" --output none
}
'''
    else:
        before = ""
        after = ""
        if number == "04":
            before = r'''
$lockId = az lock show --name "lock-$RunId" --resource-group $state.resourceGroup.name --query id --output tsv 2>$null
if ($LASTEXITCODE -eq 0 -and $lockId) { az lock delete --ids $lockId --output none }
'''
            after = r'''
if ($state.external.managementGroup) { az account management-group delete --name $state.external.managementGroup --output none }
'''
        action = before + r'''
$resourceGroup = az group show --subscription $SubscriptionId --name $state.resourceGroup.name --output json 2>$null | ConvertFrom-Json
if ($LASTEXITCODE -ne 0 -or -not $resourceGroup) { Write-Host 'Resource group is already absent; cleanup is idempotent.'; return }
if ($resourceGroup.id -ne $state.resourceGroup.id -or $resourceGroup.tags.purpose -ne 'az104-lab' -or $resourceGroup.tags.labId -ne '__LAB__' -or $resourceGroup.tags.runId -ne $RunId) {
    throw 'ID or ownership-tag verification failed; refusing cleanup.'
}
az group delete --subscription $SubscriptionId --name $state.resourceGroup.name --yes --output none
'''.replace("__LAB__", number) + after + r'''
$stillExists = az group exists --subscription $SubscriptionId --name $state.resourceGroup.name --output tsv
if ($stillExists -eq 'true') { throw 'Resource group still exists; inspect locks, dependencies, or asynchronous deletion.' }
'''
    scope = "local" if number == "00" else "tenant objects" if number in TENANT_LABS else "resource group"
    body = render(
        r'''
$LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$Manifest = Join-Path $LabRoot ".state/$RunId/run.json"
if (-not (Test-Path -LiteralPath $Manifest)) { throw "Missing state: $Manifest" }
$state = Get-Content -LiteralPath $Manifest -Raw | ConvertFrom-Json -Depth 20
$account = az account show --output json | ConvertFrom-Json
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }
if ($account.id -ne $SubscriptionId -or $state.subscriptionId -ne $SubscriptionId) { throw 'Active or recorded subscription mismatch.' }
Write-Host 'Cleanup preview for LAB-__LAB__'
Write-Host '  exact target scope: __SCOPE__'
Write-Host ($state | ConvertTo-Json -Depth 6 -Compress)
Write-Host '  residual and soft-delete behavior must be audited after deletion.'
if (-not $Execute) { Write-Host 'Preview only. Re-run with -Execute after checking every target.'; return }

__ACTION__

$state.status = 'cleanup-complete'
$state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Manifest -Encoding utf8
Write-Host 'Cleanup completed for the exact recorded boundary. Audit retained or soft-deleted items separately.'
''',
        lab=number,
        scope=scope,
        action=action.strip(),
    )
    return header + body


def contract_test(number: str) -> str:
    return render(
        r'''#requires -Version 7.4
Describe 'LAB-__LAB__ Azure CLI lifecycle contract' {
    BeforeAll {
        $labRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
        $lane = Join-Path $labRoot 'scripts/cli'
        $stageFiles = @('Preflight.ps1', 'Setup.ps1', 'Validate.ps1', 'Cleanup.ps1')
        $content = ($stageFiles | ForEach-Object { Get-Content -LiteralPath (Join-Path $lane $_) -Raw }) -join "`n"
    }

    It 'contains every PowerShell-hosted Azure CLI lifecycle stage' {
        foreach ($name in $stageFiles) { Test-Path -LiteralPath (Join-Path $lane $name) | Should -BeTrue }
    }

    It 'uses Azure CLI and contains no alternate command path' {
        $content | Should -Match '(?m)^\s*(?:\$[^=]+=\s*)?(?:\$null\s*=\s*)?az\s'
        $content | Should -Not -Match '(?i)#!/usr/bin/env|\[\[|\b(?:Connect|Get|New|Set|Remove)-Az[A-Z]'
    }

    It 'does not sign in or silently change Azure CLI context' {
        $content | Should -Not -Match '(?im)^\s*az\s+login(?:\s|$)'
        $content | Should -Not -Match '(?im)^\s*az\s+account\s+set(?:\s|$)'
    }

    It 'keeps setup and cleanup preview-first' {
        (Get-Content -LiteralPath (Join-Path $lane 'Setup.ps1') -Raw) | Should -Match '\[switch\]\$Execute'
        (Get-Content -LiteralPath (Join-Path $lane 'Cleanup.ps1') -Raw) | Should -Match '\[switch\]\$Execute'
    }

    It 'records state and emits a schema-shaped validation report' {
        (Get-Content -LiteralPath (Join-Path $lane 'Setup.ps1') -Raw) | Should -Match 'run\.json'
        (Get-Content -LiteralPath (Join-Path $lane 'Validate.ps1') -Raw) | Should -Match 'validation\.json'
    }
}
''',
        lab=number,
    )


def tests_readme(number: str) -> str:
    return f"""# Lab {number} offline tests

Run from the repository root:

```powershell
Invoke-Pester -Path labs/*/tests -Output Detailed
```

The contract verifies one complete `scripts/cli` lane with `Preflight.ps1`,
`Setup.ps1`, `Validate.ps1`, and `Cleanup.ps1`; Azure operations must use
Azure CLI, setup and cleanup remain preview-first, and scripts never sign in or
silently switch context. These offline tests do not claim a live deployment.
"""


def simple_readme(lab_dir: Path, metadata: dict) -> str:
    number = lab_dir.name[:2]
    objective_rows = "\n".join(
        f"| `{item}` | See the official objective map. |" for item in metadata.get("objectives", [])
    )
    assessment = (
        "Complete [assessment/QUESTIONS.md](assessment/QUESTIONS.md), then review [assessment/ANSWERS.md](assessment/ANSWERS.md)."
        if (metadata.get("assessment") or {}).get("enabled")
        else "This lab has no separate question set. Continue with the [domain question-bank index](../../docs/question-bank-index.md)."
    )
    return f"""# Lab {number}: {metadata['title']}

Use Azure CLI commands hosted in PowerShell to complete this isolated AZ-104 exercise. The lab never requires a browser portal workflow.

## Learning objectives

| ID | Objective |
|---|---|
{objective_rows}

## Architecture

![Lab {number} architecture](diagrams/architecture.svg)

The editable source is [diagrams/architecture.mmd](diagrams/architecture.mmd).

## Sign in and confirm Azure CLI context

```powershell
az login
az account show --query '{{subscription:id,tenant:tenantId,user:user.name}}' --output json
```

Select the intended disposable sandbox yourself if the displayed context is wrong. The lifecycle scripts refuse a mismatch and never switch it for you.

## Command and safety contract

- Install Azure CLI and PowerShell 7.4 or later.
- Sign in deliberately with `az login`, then confirm the displayed tenant and subscription.
- Use a disposable non-production environment and the smallest documented role scope.
- Setup and cleanup are previews until `-Execute` is supplied.
- Keep credentials and tokens out of command evidence, state files, and Git history.
- Use a unique run ID if you repeat the lab or try another execution lane.

<!-- BEGIN GENERATED INLINE COMMANDS -->
<!-- END GENERATED INLINE COMMANDS -->

## Run the lab

Set values for your sandbox, then invoke the lifecycle scripts. For Labs 01 and 02, also read the environment-variable gates embedded in `Setup.ps1`.

```powershell
$subscriptionId = '<subscription-id>'
$location = '<region>'
$runId = 'az104l{number}-01'

pwsh ./scripts/cli/Preflight.ps1 -SubscriptionId $subscriptionId -Location $location
pwsh ./scripts/cli/Setup.ps1 -SubscriptionId $subscriptionId -Location $location -RunId $runId
pwsh ./scripts/cli/Setup.ps1 -SubscriptionId $subscriptionId -Location $location -RunId $runId -Execute
pwsh ./scripts/cli/Validate.ps1 -SubscriptionId $subscriptionId -RunId $runId
```

## Break/fix exercise

Pass a different subscription ID to validation. Confirm that the script refuses the mismatched context without changing it, then rerun with the correct ID and inspect `validation.json`.

## Cleanup

```powershell
pwsh ./scripts/cli/Cleanup.ps1 -SubscriptionId $subscriptionId -RunId $runId
pwsh ./scripts/cli/Cleanup.ps1 -SubscriptionId $subscriptionId -RunId $runId -Execute
```

Confirm that the exact recorded active resources or tenant objects are absent. Review service-specific soft-delete retention separately.

## Exam practice

{assessment}
"""


def normalize_readme(lab_dir: Path, metadata: dict) -> None:
    number = lab_dir.name[:2]
    if number in {"00", "01"}:
        write_text(lab_dir / "README.md", simple_readme(lab_dir, metadata))
        return

    path = lab_dir / "README.md"
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    begin = "<!-- BEGIN GENERATED INLINE COMMANDS -->"
    end = "<!-- END GENERATED INLINE COMMANDS -->"
    if begin in text and end in text:
        prefix, remainder = text.split(begin, 1)
        _, suffix = remainder.split(end, 1)
        text = prefix.rstrip() + f"\n\n{begin}\n{end}\n" + suffix.lstrip()

    sign_in = """## Sign in and confirm Azure CLI context

```powershell
az login
az account show --query '{subscription:id,tenant:tenantId,user:user.name}' --output json
```

Select the intended disposable sandbox yourself if the displayed context is wrong. The lifecycle scripts refuse a mismatch and never switch it for you.

"""
    if "## Sign in and confirm Azure CLI context" not in text:
        marker = "## Before you begin\n"
        if marker not in text:
            raise ValueError(f"{lab_dir.name}: README has no preflight insertion point")
        text = text.replace(marker, sign_in + marker, 1)

    text = re.sub(
        r"\| Command surface \|.*\|",
        "| Command surface | Azure CLI (`az`) hosted in PowerShell |",
        text,
    )
    text = re.sub(
        r"^- PowerShell modules used when applicable:.*$",
        "- Required command tools: Azure CLI and PowerShell 7.4 or later",
        text,
        flags=re.MULTILINE,
    )
    text = text.replace("```sh", "```powershell")
    text = text.replace("CLI/PowerShell query", "Azure CLI query")
    text = text.replace("command modules evolve", "command syntax evolves")
    tenant = number in TENANT_LABS
    subscription = "" if tenant else " -SubscriptionId <subscription-id>"
    commands = {
        "Setup": f"pwsh ./scripts/cli/Setup.ps1 -RunId az104l{number}-01{subscription} -Location <region>",
        "Validate": f"pwsh ./scripts/cli/Validate.ps1 -RunId az104l{number}-01{subscription}",
        "Cleanup": f"pwsh ./scripts/cli/Cleanup.ps1 -RunId az104l{number}-01{subscription}",
    }
    for stage, command in commands.items():
        pattern = rf"^.*(?:\./)?scripts/cli/{stage}\.ps1.*$"
        matches = list(re.finditer(pattern, text, flags=re.MULTILINE))
        for match in reversed(matches):
            line = command
            original = match.group(0)
            if "-Execute" in original or "--execute" in original:
                line += " -Execute"
            text = text[: match.start()] + line + text[match.end() :]
    text = text.replace("`--execute` or `-Execute`", "`-Execute`")
    write_text(path, text)


def update_metadata(lab_dir: Path, metadata: dict) -> None:
    number = lab_dir.name[:2]
    metadata["track"] = "azure-cli-bicep" if number in {"10", "26"} else "azure-cli"
    metadata["testedToolVersions"] = {"azureCli": ">=2.88.0", "powershell": ">=7.4"}
    if number == "01":
        metadata.setdefault("permissions", {})["graphScopes"] = [
            "User.ReadWrite.All",
            "Group.ReadWrite.All",
            "Directory.ReadWrite.All",
        ]
    elif number == "02":
        metadata.setdefault("permissions", {})["graphScopes"] = [
            "User.Invite.All",
            "User.ReadWrite.All",
            "Group.ReadWrite.All",
            "Directory.ReadWrite.All",
            "Policy.ReadWrite.Authorization",
        ]
    prerequisites = list(metadata.get("prerequisites") or [])
    prerequisites = [
        item
        for item in prerequisites
        if not re.search(r"(?i)command surface|powershell module", item)
    ]
    prerequisites.append("Azure CLI hosted in PowerShell 7.4 or later")
    metadata["prerequisites"] = list(dict.fromkeys(prerequisites))
    validation = metadata.setdefault("validation", {})
    validation["commandLanes"] = ["scripts/cli/Validate.ps1"]
    write_text(
        lab_dir / "lab.yml",
        yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True, width=110),
    )


def update_diagram(lab_dir: Path) -> None:
    for name in ("architecture.mmd", "architecture.svg"):
        path = lab_dir / "diagrams" / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("CLI + Bicep", "Azure CLI + Bicep")
        write_text(path, text)


def replace_script_lane(lab_dir: Path, metadata: dict) -> None:
    scripts_root = (lab_dir / "scripts").resolve()
    if scripts_root.parent != lab_dir.resolve():
        raise ValueError(f"Refusing to replace unexpected scripts path: {scripts_root}")
    if scripts_root.exists():
        shutil.rmtree(scripts_root)
    lane = scripts_root / "cli"
    write_text(lane / "Preflight.ps1", preflight_script(lab_dir.name[:2], metadata))
    write_text(lane / "Setup.ps1", setup_script(lab_dir.name[:2], metadata))
    write_text(lane / "Validate.ps1", validate_script(lab_dir.name[:2], metadata))
    write_text(lane / "Cleanup.ps1", cleanup_script(lab_dir.name[:2], metadata))


def update_catalog() -> None:
    path = LABS_ROOT / "catalog.yml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    for item in data.get("labs", []):
        number = str(item.get("id", "")).zfill(2)
        item["track"] = "azure-cli-bicep" if number in {"10", "26"} else "azure-cli"
    write_text(path, yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110))


def normalize_lab(lab_dir: Path) -> None:
    if not LAB_PATTERN.fullmatch(lab_dir.name):
        raise ValueError(f"Unexpected lab directory: {lab_dir}")
    metadata = yaml.safe_load((lab_dir / "lab.yml").read_text(encoding="utf-8"))
    replace_script_lane(lab_dir, metadata)
    update_metadata(lab_dir, metadata)
    normalize_readme(lab_dir, metadata)
    update_diagram(lab_dir)
    write_text(lab_dir / "tests" / "Contract.Tests.ps1", contract_test(lab_dir.name[:2]))
    write_text(lab_dir / "tests" / "README.md", tests_readme(lab_dir.name[:2]))
    if lab_dir.name[:2] in {"00", "01"}:
        write_text(
            lab_dir / "solution" / "README.md",
            f"""# Lab {lab_dir.name[:2]} solution notes

Use the complete Azure CLI commands embedded in the parent [lab README](../README.md).
Validate with `pwsh ./scripts/cli/Validate.ps1`, perform the documented break/fix exercise,
and preview `Cleanup.ps1` before supplying `-Execute`. Retain only redacted command evidence.
""",
        )
    sync_lab(lab_dir, check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Retained for compatibility; normalization is explicit.")
    parser.add_argument("--only", nargs="*", help="Optional two-digit lab IDs")
    args = parser.parse_args()
    selected = set(args.only or [])
    labs = sorted(
        path for path in LABS_ROOT.iterdir() if path.is_dir() and LAB_PATTERN.fullmatch(path.name)
    )
    if selected:
        labs = [path for path in labs if path.name[:2] in selected]
    for lab_dir in labs:
        normalize_lab(lab_dir)
        print(f"WRITE {lab_dir.relative_to(ROOT)} Azure CLI PowerShell lane")
    update_catalog()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
