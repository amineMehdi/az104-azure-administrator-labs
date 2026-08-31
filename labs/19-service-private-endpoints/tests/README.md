# Lab 19 offline tests

Run from the repository root:

```powershell
Invoke-Pester -Path labs/*/tests -Output Detailed
```

The contract verifies one complete `scripts/cli` lane with `Preflight.ps1`,
`Setup.ps1`, `Validate.ps1`, and `Cleanup.ps1`; Azure operations must use
Azure CLI, setup and cleanup remain preview-first, and scripts never sign in or
silently switch context. These offline tests do not claim a live deployment.
