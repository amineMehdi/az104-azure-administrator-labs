# Lab 07 portal evidence

This folder holds sanitized Azure Portal screenshots for Lab 07 and the manifest that tracks them.

## Contract

- [portal/manifest.yml](portal/manifest.yml) lists every planned capture with its checkpoint, blade, and expected evidence.
- A PNG enters this folder only after an authorized live run and full sanitization; fabricated or placeholder images are forbidden.
- Statuses progress `pending` → `captured` → `sanitized` → `verified`; raw (`captured`) files must never be committed.
- Two to five captures per lab, PNG only, at most 1920 px wide, and roughly 500 KB or less after optimization.

## Sanitization checklist

Before a capture may be recorded as `sanitized`:

1. Crop to the relevant blade and remove browser chrome, bookmarks, other tabs, and unrelated resources.
2. Irreversibly redact tenant and subscription GUIDs, account names, email addresses and UPNs, tokens, keys, public IPs, and billing details.
3. Strip all image metadata (EXIF, XMP, and text chunks) and re-encode as an optimized PNG.
4. Update the matching manifest entry: capture date, region (or `not-applicable` for tenant-plane blades), the redactions performed, `portalConfirmed: true`, and the new status.
5. Record `verified` only after a second manual review confirms no identifying content remains.

Repository-wide rules live in [docs/evidence-handling.md](../../../docs/evidence-handling.md).
