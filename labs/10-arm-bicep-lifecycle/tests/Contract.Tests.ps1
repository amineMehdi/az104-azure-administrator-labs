#requires -Version 7.4
Describe 'LAB-10 offline lifecycle contract' {
    BeforeAll {
        $labRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
        $lane = Join-Path $labRoot 'scripts/cli'
        $stageFiles = @('preflight.sh', 'setup.sh', 'validate.sh', 'cleanup.sh')
    }

    It 'contains every lifecycle stage' {
        foreach ($name in $stageFiles) { Test-Path -LiteralPath (Join-Path $lane $name) | Should -BeTrue }
    }

    It 'does not sign in or silently change Azure context' {
        $content = ($stageFiles | ForEach-Object { Get-Content -LiteralPath (Join-Path $lane $_) -Raw }) -join "`n"
        $content | Should -Not -Match '(?i)az\s+login|Connect-AzAccount|Set-AzContext|az\s+account\s+set'
    }

    It 'keeps setup and cleanup preview-first' {
        $setup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[1]) -Raw
        $cleanup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[3]) -Raw
        $setup | Should -Match '(?i)--execute|\[switch\]\$Execute'
        $cleanup | Should -Match '(?i)--execute|\[switch\]\$Execute'
    }

    It 'records state and emits a schema-shaped validation report' {
        $setup = Get-Content -LiteralPath (Join-Path $lane $stageFiles[1]) -Raw
        $validate = Get-Content -LiteralPath (Join-Path $lane $stageFiles[2]) -Raw
        $setup | Should -Match '(?i)run\.json'
        $validate | Should -Match '(?i)validation\.json'
        $validate | Should -Match "LAB-10"
    }

    It 'contains no cross-lab runtime dependency' {
        $content = ($stageFiles | ForEach-Object { Get-Content -LiteralPath (Join-Path $lane $_) -Raw }) -join "`n"
        $content | Should -Not -Match '\.\.[\/][0-9]{2}-[a-z0-9-]+'
    }
}
