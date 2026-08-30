# Portal evidence checklist

Status: **pending live authorization**. This folder intentionally contains no placeholder screenshots.

Capture these images only after the user authorizes Portal access to the exact sandbox tenant and subscription. Portal navigation is for verification and UI recognition; do not use it to configure anything.

## Required captures

1. `01-subscription-overview.png`
   - Open **Subscriptions > selected sandbox subscription > Overview**.
   - Show the subscription state and the subscription name only if it contains no personal or employer information.
   - Crop or irreversibly redact subscription ID, tenant ID, billing identifiers, email addresses, and unrelated navigation history.
2. `02-resource-providers.png`
   - Open **Subscriptions > selected sandbox subscription > Resource providers**.
   - Filter to one of the providers inspected by this lab and show its registration state.
   - Do not register or unregister a provider for the screenshot.
3. `03-usage-quotas.png`
   - Open **Quotas > Compute** and select the configured primary region.
   - Show one non-sensitive usage/limit row that corresponds to the read-only command output.
   - Exclude support-request details and unrelated subscriptions.

## Capture and sanitization rules

- Use a real Azure Portal session from this lab's authorized live-verification run.
- Never capture account menus, sign-in screens, billing pages, access tokens, secrets, keys, connection strings, or SAS values.
- Frame narrowly; if redaction is needed, flatten it irreversibly before saving.
- Strip PNG metadata and visually inspect the final pixels at 100% zoom.
- Use a consistent light theme, browser zoom, and readable viewport.
- Update `manifest.yml` after each image is captured, sanitized, and reviewed.
- Add `Captured YYYY-MM-DD; Portal UI may change` beneath the image when it is added to the lab README.
