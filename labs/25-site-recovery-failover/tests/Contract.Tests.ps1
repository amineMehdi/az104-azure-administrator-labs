#requires -Version 7.4
Describe 'LAB-25 offline lifecycle contract' {
    BeforeAll {
        $script:LabRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
        $script:SetupSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Setup.ps1') -Raw
        $script:ValidateSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Validate.ps1') -Raw
        $script:CleanupSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'scripts/cli/Cleanup.ps1') -Raw
        $script:RunFixtureSource = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/run.sample.json') -Raw
        $script:ValidationFixture = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/validation.sample.json') -Raw | ConvertFrom-Json
        $script:CleanupFixture = Get-Content -LiteralPath (Join-Path $script:LabRoot 'tests/fixtures/cleanup.sample.json') -Raw | ConvertFrom-Json
        $script:CheckpointIds = @('LAB25-CP01', 'LAB25-CP02', 'LAB25-CP03', 'LAB25-CP04', 'LAB25-CP05')
        $script:OptionalCheckpointIds = @('LAB25-CP03', 'LAB25-CP04')
        $script:ExpectedSubscriptionId = '11111111-1111-4111-8111-111111111111'
        $script:ExpectedTenantId = '22222222-2222-4222-8222-222222222222'

        function global:az {
            throw 'Offline lifecycle contract blocked an unmocked Azure CLI call.'
        }

        function New-LifecycleHarness {
            param([Parameter(Mandatory)][string]$Root)
            $cli = Join-Path $Root 'scripts/cli'
            New-Item -ItemType Directory -Path $cli -Force | Out-Null
            foreach ($name in @('Setup.ps1', 'Preflight.ps1', 'Validate.ps1', 'Cleanup.ps1')) {
                $source = Join-Path $script:LabRoot "scripts/cli/$name"
                $target = Join-Path $cli $name
                $text = Get-Content -LiteralPath $source -Raw
                # A failing generated script must fail this test, not terminate the
                # complete Pester process. Only the isolated harness copy is changed.
                $text = $text -replace '(?m)^\s*exit 1\s*$', "throw 'Lifecycle script reported failure.'"
                Set-Content -LiteralPath $target -Value $text -Encoding utf8
            }
            return $cli
        }

        function Write-HarnessRun {
            param(
                [Parameter(Mandatory)][string]$HarnessRoot,
                [Parameter(Mandatory)][object]$Run
            )
            $stateDirectory = Join-Path $HarnessRoot ".state/$($Run.runId)"
            New-Item -ItemType Directory -Path $stateDirectory -Force | Out-Null
            $Run | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $stateDirectory 'run.json') -Encoding utf8
            return $stateDirectory
        }
    }

    BeforeEach {
        $script:HarnessRoot = Join-Path $TestDrive ([guid]::NewGuid().ToString('n'))
        $script:HarnessCli = New-LifecycleHarness -Root $script:HarnessRoot
        $script:HarnessSetup = Join-Path $script:HarnessCli 'Setup.ps1'
        $script:HarnessValidate = Join-Path $script:HarnessCli 'Validate.ps1'
        $script:HarnessCleanup = Join-Path $script:HarnessCli 'Cleanup.ps1'
        $global:Az104ContractAzCalls = 0
        $global:LASTEXITCODE = 0
        Mock az {
            $global:Az104ContractAzCalls++
            $commandLine = @($args) -join ' '
            if ($commandLine -match '^account show(?:\s|$)') {
                $global:LASTEXITCODE = 0
                return (@{
                    id = '11111111-1111-4111-8111-111111111111'
                    tenantId = '22222222-2222-4222-8222-222222222222'
                    environmentName = 'AzureCloud'
                } | ConvertTo-Json -Compress)
            }
            # Every exact-object query reports absence. Post-cleanup validation
            # therefore proves residual reporting without reaching Azure.
            $global:LASTEXITCODE = 1
            return ''
        }
    }

    AfterAll {
        Remove-Item -LiteralPath Function:\az -Force -ErrorAction SilentlyContinue
        Remove-Variable -Name Az104ContractAzCalls -Scope Global -ErrorAction SilentlyContinue
    }

    It 'actually invokes Setup preview without Azure calls, mutations, or state' {
        $runId = 'preview-25'
        $output = & $script:HarnessSetup -SubscriptionId $script:ExpectedSubscriptionId -RunId $runId -Location 'westeurope' 6>&1 | Out-String

        $output | Should -Match 'Preview only'
        (Join-Path $script:HarnessRoot ".state/$runId") | Should -Not -Exist
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }

    It 'asserts successful and denied checks are independent in the complete fixture' {
        @($script:ValidationFixture.checks).Count | Should -Be ($script:CheckpointIds.Count * 2)
        foreach ($id in $script:CheckpointIds) {
            $pair = @($script:ValidationFixture.checks | Where-Object checkpointId -eq $id)
            @($pair.kind | Sort-Object -Unique) | Should -Be @('negative', 'positive')
            @($pair | Where-Object required).Count | Should -Be $(if ($id -in $script:OptionalCheckpointIds) { 0 } else { 2 })
            @($pair | Where-Object { $_.required -and $_.status -ne 'pass' }).Count | Should -Be 0
        }
        $script:ValidateSource | Should -Match "-Kind 'positive'"
        $script:ValidateSource | Should -Match "-Kind 'negative'"
        $script:ValidateSource | Should -Match '\$failedChecks\.Count -gt 0'
    }

    It 'persists recoverable state before mutation and across partial failure' {
        $initialSave = $script:SetupSource.IndexOf('# The manifest exists before the first Azure mutation.')
        $firstCheckpoint = $script:SetupSource.IndexOf('# CHECKPOINT ' + $script:CheckpointIds[0] + ' BEGIN')
        $initialSave | Should -BeGreaterOrEqual 0
        $firstCheckpoint | Should -BeGreaterThan $initialSave
        $script:SetupSource.Substring($initialSave, $firstCheckpoint - $initialSave) | Should -Match 'Save-RunState'

        foreach ($id in $script:CheckpointIds) {
            $pattern = '(?s)# CHECKPOINT ' + [regex]::Escape($id) + ' BEGIN(?<body>.*?)# CHECKPOINT ' + [regex]::Escape($id) + ' END'
            $block = [regex]::Match($script:SetupSource, $pattern).Groups['body'].Value
            $block | Should -Not -BeNullOrEmpty
            $block | Should -Match 'catch \{'
            $block | Should -Match ("Sync-ManagedResource -CheckpointId '" + [regex]::Escape($id) + "'")
            $block | Should -Match "-Status 'fail'"
            $block | Should -Match "\$state.status = 'failed'"
            $block | Should -Match 'Save-RunState'
            $block | Should -Match 'throw'
        }
    }

    It 'models optional checkpoint skips as a partial deployment result' {
        if ($script:OptionalCheckpointIds.Count -eq 0) {
            $script:ValidationFixture.summary.skipped | Should -Be 0
            $script:ValidationFixture.result | Should -Be 'pass'
            return
        }
        $script:ValidationFixture.result | Should -Be 'partial'
        $script:ValidationFixture.summary.skipped | Should -BeGreaterThan 0
        foreach ($id in $script:OptionalCheckpointIds) {
            @($script:ValidationFixture.checks | Where-Object checkpointId -eq $id | Select-Object -ExpandProperty status -Unique) | Should -Be @('skipped')
        }
    }

    It 'actually invokes Cleanup ownership refusal against an isolated fixture copy' {
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $run.labId = 'LAB-mismatch'
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run

        { & $script:HarnessCleanup -RunId $run.runId -Execute } | Should -Throw '*Cleanup ownership refusal*'

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'fail'
        $artifact.ownershipVerified | Should -BeFalse
        @($artifact.activeManagedObjects).Count | Should -Be @($run.managedObjects | Where-Object lifecycleStatus -eq 'active').Count
        @($artifact.actions | Where-Object status -ne 'failed').Count | Should -Be 0
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }

    It 'actually invokes PostCleanup validation and writes passing residual evidence' {
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run

        $output = & $script:HarnessValidate -RunId $run.runId -Mode PostCleanup 6>&1 | Out-String

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'validation.json') -Raw | ConvertFrom-Json
        $output | Should -Match 'Validation PostCleanup result: pass'
        $artifact.mode | Should -Be 'PostCleanup'
        $artifact.result | Should -Be 'pass'
        @($artifact.checks).Count | Should -Be $script:CheckpointIds.Count
        @($artifact.checks | Where-Object { $_.kind -ne 'residual' -or $_.status -ne 'pass' }).Count | Should -Be 0
        @($artifact.checks | Where-Object { $_.evidence.actual -notmatch '^active=' }).Count | Should -Be 0
        $global:Az104ContractAzCalls | Should -BeGreaterThan 0
        Should -Invoke az -Scope It
    }

    It 'actually invokes idempotent Cleanup for an already-cleaned empty state' {
        $run = $script:RunFixtureSource | ConvertFrom-Json
        $run.status = 'cleaned'
        foreach ($managedObject in @($run.managedObjects)) { $managedObject.lifecycleStatus = 'deleted' }
        $stateDirectory = Write-HarnessRun -HarnessRoot $script:HarnessRoot -Run $run
        $script:CleanupFixture | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Encoding utf8

        $output = & $script:HarnessCleanup -RunId $run.runId -Execute 6>&1 | Out-String

        $artifact = Get-Content -LiteralPath (Join-Path $stateDirectory 'cleanup.json') -Raw | ConvertFrom-Json
        $persistedRun = Get-Content -LiteralPath (Join-Path $stateDirectory 'run.json') -Raw | ConvertFrom-Json
        $output | Should -Match 'already cleaned'
        $artifact.result | Should -Be 'pass'
        $artifact.ownershipVerified | Should -BeTrue
        @($artifact.actions).Count | Should -Be 0
        @($artifact.activeManagedObjects).Count | Should -Be 0
        @($artifact.residualChecks).Count | Should -Be 1
        $artifact.residualChecks[0].id | Should -Be 'cleanup.idempotent'
        $artifact.residualChecks[0].status | Should -Be 'pass'
        $persistedRun.status | Should -Be 'cleaned'
        $global:Az104ContractAzCalls | Should -Be 0
        Should -Invoke az -Times 0 -Scope It
    }

    It 'retains a fully owned, residual-free successful cleanup fixture' {
        $script:CleanupFixture.result | Should -Be 'pass'
        $script:CleanupFixture.ownershipVerified | Should -BeTrue
        @($script:CleanupFixture.activeManagedObjects).Count | Should -Be 0
        @($script:CleanupFixture.actions | Where-Object { -not $_.ownership.verified -or $_.status -notin @('deleted', 'soft-deleted', 'skipped') }).Count | Should -Be 0
        @($script:CleanupFixture.residualChecks | Where-Object status -ne 'pass').Count | Should -Be 0
        $script:CleanupSource | Should -Match 'Irreversible purge is never automated'
    }
}
