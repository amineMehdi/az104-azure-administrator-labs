# Contributing

Contributions should preserve objective traceability, safe Azure behavior, learner clarity, and lab portability.

## Before opening a change

- Use current official Microsoft documentation.
- Do not copy exam dumps or proprietary practice questions.
- Do not commit tenant IDs, subscription IDs, personal email addresses, secrets, SAS tokens, keys, or credentials.
- Keep every lab self-contained; no runtime import from another lab.
- Make validation read-only and cleanup idempotent.
- Update `lastVerified` metadata for changed technical instructions.

## Validation

Run:

```powershell
python tools/validate_repository.py
```

Run the relevant shell, PowerShell, Bicep, diagram, and assessment checks for the files changed. Live Azure testing requires a dedicated sandbox and explicit authorization.

## Assessment contributions

Each lab has exactly ten original four-option, single-answer questions. Map every question to objective IDs, provide a separate answer explanation, cite official Microsoft sources, and avoid predictable answer patterns.
