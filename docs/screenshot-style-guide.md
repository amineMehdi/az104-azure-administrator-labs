# Azure Portal screenshot style guide

Screenshots are real verification evidence, never synthetic UI.

## Capture

- Capture only after command-line validation succeeds.
- Use a consistent Portal theme, browser zoom, and readable viewport.
- Capture 2–5 images per lab unless complexity justifies more.
- Frame only the resource and state relevant to the checkpoint.

## Privacy

- Avoid account menus, sign-in pages, billing pages, tokens, keys, connection strings, and SAS values.
- Crop or irreversibly flatten redactions over tenant IDs, subscription IDs, emails, object IDs, and unrelated resources.
- Strip metadata and inspect the final committed image again.

## Documentation

- Store images under `images/portal/` in the owning lab.
- Use descriptive filenames and useful alt text.
- State what the image proves and the capture date.
- Record every image in `images/manifest.yml`.
- If live access is unavailable, use a textual checklist without broken or fake placeholder images.
