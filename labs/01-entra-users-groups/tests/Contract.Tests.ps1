BeforeAll {
    $labRoot = Split-Path -Parent $PSScriptRoot
    $cliRoot = Join-Path $labRoot 'scripts/cli'
}

Describe 'Lab 01 Azure CLI safety contract' {
    BeforeAll {
        $preflight = Get-Content (Join-Path $cliRoot 'preflight.sh') -Raw
        $setup = Get-Content (Join-Path $cliRoot 'setup.sh') -Raw
        $validate = Get-Content (Join-Path $cliRoot 'validate.sh') -Raw
        $cleanup = Get-Content (Join-Path $cliRoot 'cleanup.sh') -Raw
        $allScripts = $preflight, $setup, $validate, $cleanup -join "`n"
    }

    It 'provides all four lifecycle stages' {
        'preflight.sh', 'setup.sh', 'validate.sh', 'cleanup.sh' | ForEach-Object {
            Test-Path (Join-Path $cliRoot $_) | Should -BeTrue
        }
    }

    It 'never signs in or silently changes Azure CLI context' {
        $allScripts | Should -Not -Match '(?m)^\s*az\s+login\b'
        $allScripts | Should -Not -Match '(?m)^\s*az\s+account\s+set\b'
    }

    It 'keeps preflight and validation free of directory mutations' {
        ($preflight, $validate -join "`n") | Should -Not -Match '(?m)^\s*az\s+ad\s+.+\s(create|delete|add|remove|update)\b'
        ($preflight, $validate -join "`n") | Should -Not -Match '(?m)^\s*az\s+rest\s+.*--method\s+(post|patch|put|delete)\b'
    }

    It 'stops validation when the active tenant differs from recorded state' {
        $validate | Should -Match 'context\.tenant'
        $validate | Should -Match 'validation stopped before trusting directory results'
        $validate | Should -Match 'exit 1'
    }

    It 'requires an explicit execute flag before setup mutations' {
        $setup | Should -Match 'execute=false'
        $setup | Should -Match 'if \[\[ "\$execute" != "true" \]\]'
        $setup | Should -Match 'PLAN ONLY'
    }

    It 'takes the initial password from an environment variable and excludes it from state' {
        $setup | Should -Match 'AZ104_LAB_INITIAL_PASSWORD'
        $setup | Should -Match 'passwordStored:false'
        $setup | Should -Not -Match '(?i)password\s*=\s*["''][^$][^"'']{8,}["'']'
    }

    It 'requires explicit execution and exact recorded IDs for cleanup' {
        $cleanup | Should -Match 'execute=false'
        $cleanup | Should -Match 'select\(\.kind=="group"\)'
        $cleanup | Should -Match 'select\(\.key=="userA"\)'
        $cleanup | Should -Match 'select\(\.key=="userB"\)'
        $cleanup | Should -Match 'resource_count > 3'
        $cleanup | Should -Match 'unknown_resources'
        $cleanup | Should -Not -Match 'az ad (user|group) list.*\|.*delete'
    }

    It 'can clean a recorded partial run instead of requiring all three objects' {
        $cleanup | Should -Not -Match 'resource_count" != "3'
        $cleanup | Should -Match '<not recorded>'
        $cleanup | Should -Match '\[\[ -n "\$user_a_id" \]\]'
    }

    It 'separates recoverable deletion from irreversible purge' {
        $cleanup | Should -Match '--purge-deleted-users'
        $cleanup | Should -Match 'permanently'
        $cleanup | Should -Match 'directory/deletedItems/\$object_id'
    }
}
