#requires -Version 7.4
Describe 'LAB-09 Azure CLI lifecycle contract' {
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
