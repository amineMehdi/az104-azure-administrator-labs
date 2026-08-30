# Lab 01 offline test contract

These checks validate content and command safety without signing in to Microsoft Entra ID. They do not create, update, query, or delete tenant objects.

Run from the Lab 01 directory.

```powershell
Invoke-Pester tests/Contract.Tests.ps1 -Output Detailed
```

Parse the Bash scripts:

```bash
bash -n scripts/cli/preflight.sh
bash -n scripts/cli/setup.sh
bash -n scripts/cli/validate.sh
bash -n scripts/cli/cleanup.sh
```

When ShellCheck is available:

```bash
shellcheck scripts/cli/*.sh
```

The contract confirms that:

- preflight and validation contain only read operations;
- scripts never sign in or silently change Azure CLI context;
- setup requires `--execute` and keeps the temporary password out of run state;
- cleanup selects only the known recorded IDs and can recover a partial setup;
- soft deletion and permanent purge are separate decisions; and
- all runtime dependencies stay inside this lab folder.

Live acceptance additionally requires a disposable tenant, successful positive and negative command validation, and a cleanup audit. Until then, keep `lastLiveVerified: null`.
