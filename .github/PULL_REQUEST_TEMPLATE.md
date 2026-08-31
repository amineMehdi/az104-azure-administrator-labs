## Summary

Describe the learner-visible outcome and the mapped AZ-104 objectives.

## Validation

- [ ] `python tools/validate_repository.py --release`
- [ ] `python tools/render_diagrams.py --check`
- [ ] Relevant PowerShell-hosted Azure CLI and Bicep static checks
- [ ] `python tools/validate_assessments.py` and rendered assessment drift checks
- [ ] Strict documentation-site build if learner-facing content changed
- [ ] Lab folder portability check
- [ ] Cleanup reviewed for exact scope and idempotency
- [ ] Question and answer explanations reviewed
- [ ] Mermaid source, generated SVG, title, description, and alt text reviewed if visuals changed

## Azure impact

- [ ] No live Azure action was performed
- [ ] Live action was authorized and documented
- [ ] Cleanup and residual-resource audit passed

Do not include tenant IDs, subscription IDs, personal email addresses, secrets, keys, tokens, or SAS values.
