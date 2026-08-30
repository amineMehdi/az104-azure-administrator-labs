# Lab 05 offline tests

Run from the repository root:

```powershell
Invoke-Pester -Path labs/*/tests -Output Detailed
```

The contract test checks that the `powershell` lane contains preflight, setup, validation, and cleanup; never signs in or silently changes context; keeps mutations behind an explicit execution switch; records state; and has no runtime dependency on another lab.

These are offline safety and structure tests. They do not claim that Azure resources were deployed.
