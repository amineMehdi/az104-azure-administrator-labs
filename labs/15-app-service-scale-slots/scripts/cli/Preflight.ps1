#requires -Version 7.4
[CmdletBinding()]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Interactive lab progress is intentionally written to the host.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', '', Justification = 'Lifecycle scripts keep one consistent interface across all labs.')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Shared safe-naming variables are retained for a consistent learner path.')]
param(
    [string]$SubscriptionId = $env:AZURE_SUBSCRIPTION_ID,
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Location
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw 'Azure CLI is required. Install it, run az login deliberately, and retry.'
}

$account = az account show --output json | ConvertFrom-Json
if (-not $account) { throw 'No active Azure CLI context. Run az login deliberately before this lab.' }
if ($SubscriptionId -and $account.id -ne $SubscriptionId) {
    throw "Context mismatch: active subscription is $($account.id), expected $SubscriptionId. This script will not switch it."
}
if (-not $SubscriptionId) { $SubscriptionId = [string]$account.id }

Write-Host 'Lab: LAB-15'
Write-Host "Tenant: $($account.tenantId)"
Write-Host "Subscription: $SubscriptionId"
Write-Host "Location: $Location"
Write-Host 'Cost class: low'
Write-Host 'Role boundary: Website Contributor and Monitoring Contributor on the lab resource group'

$providers = @(
    'Microsoft.Insights'
    'Microsoft.Web'
)
foreach ($provider in $providers) {
    $registrationState = az provider show --namespace $provider --query registrationState --output tsv 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $registrationState) { $registrationState = 'Unavailable' }
    Write-Host ('Provider {0,-38} {1}' -f $provider, $registrationState)
}

if ('subscription' -eq 'tenant') {
    $null = az account get-access-token --resource-type ms-graph --query expiresOn --output tsv
    Write-Host 'Microsoft Graph access through Azure CLI is available.'
}
Write-Host 'Preflight is read-only. It does not sign in, switch context, register providers, or create resources.'
