BeforeAll {
    $labRoot = Split-Path -Parent $PSScriptRoot
    $cliRoot = Join-Path $labRoot 'scripts\cli'
    $powerShellRoot = Join-Path $labRoot 'scripts\powershell'
}

Describe 'Lab 00 command safety contract' {
    It 'provides all four lifecycle stages in each lane' {
        @('preflight.sh', 'setup.sh', 'validate.sh', 'cleanup.sh') |
            ForEach-Object { Test-Path -LiteralPath (Join-Path $cliRoot $_) | Should -BeTrue }
        @('Preflight.ps1', 'Setup.ps1', 'Validate.ps1', 'Cleanup.ps1') |
            ForEach-Object { Test-Path -LiteralPath (Join-Path $powerShellRoot $_) | Should -BeTrue }
    }

    It 'does not sign in or silently change Azure CLI context' {
        $content = Get-Content -Path (Join-Path $cliRoot '*.sh') -Raw
        $content | Should -Not -Match '(?m)^\s*az\s+login(?:\s|$)'
        $content | Should -Not -Match '(?m)^\s*az\s+account\s+set(?:\s|$)'
    }

    It 'does not contain Azure CLI mutation commands' {
        $content = Get-Content -Path (Join-Path $cliRoot '*.sh') -Raw
        $content | Should -Not -Match '(?m)^\s*az\s+(?:group\s+(?:create|delete)|provider\s+register|role\s+assignment\s+(?:create|delete))'
    }

    It 'does not sign in or change Az PowerShell context' {
        $content = Get-Content -Path (Join-Path $powerShellRoot '*.ps1') -Raw
        $content | Should -Not -Match '(?m)^\s*Connect-AzAccount(?:\s|$)'
        $content | Should -Not -Match '(?m)^\s*Set-AzContext(?:\s|$)'
    }

    It 'does not contain Az PowerShell resource mutations' {
        $content = Get-Content -Path (Join-Path $powerShellRoot '*.ps1') -Raw
        $content | Should -Not -Match '(?m)^\s*(?:New|Set|Remove)-Az(?:ResourceGroup|RoleAssignment|PolicyAssignment)'
        $content | Should -Not -Match '(?m)^\s*Register-AzResourceProvider'
    }

    It 'requires explicit execution for local cleanup' {
        (Get-Content -LiteralPath (Join-Path $cliRoot 'cleanup.sh') -Raw) |
            Should -Match '--execute'
        (Get-Content -LiteralPath (Join-Path $powerShellRoot 'Cleanup.ps1') -Raw) |
            Should -Match '\[switch\]\s*\$Execute'
    }
}
