# Security policy

## Reporting a problem

Do not open a public issue containing credentials or account identifiers. Report suspected secret exposure privately to the repository owner and revoke or rotate the affected credential immediately.

## Repository rules

- Never commit passwords, tokens, keys, connection strings, certificates with private keys, or SAS values.
- Treat `.state/` as local and disposable.
- Use interactive authentication locally and OIDC for any future GitHub-to-Azure workflow.
- Use the narrowest practical role and scope.
- Never expose SSH or RDP to `0.0.0.0/0`.
- Review screenshots for tenant, subscription, identity, billing, and secret data before commit.
- Live tests must use an explicitly approved sandbox, never production.

Pull-request workflows perform offline validation only and must not contain Azure credentials.
