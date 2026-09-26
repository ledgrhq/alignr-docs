# Alignr documentation

This separate repository publishes the public Mintlify site for docs.alignr.io.

- Use Almond, Inter and the restrained monochrome layout matching the owner's Resend reference. Use Alignr branding, never Resend's logo or copy.
- Public guides live in MDX. Internal architecture and accepted decisions remain in the application repository's vault; do not copy that vault here.
- Alignr is a technical alignment platform for MSPs. A tenant is an MSP workspace; an Organization is its client. Missing or stale evidence never counts as passing.
- Use British English, except the established label Organization. Use sentence case, direct instructions and bold UI labels.
- Check claims against the application source. Never invent endpoints, scopes, SDKs, supported integrations or production acceptance.
- Run scripts/sync-reference.py with the application Python environment to regenerate the curated read-only OpenAPI snapshot and MCP catalogue. Inspect generated output before publishing.
- Never add secrets, customer records, private operational configuration or authenticated schema-fetch credentials.
- Every MDX page needs title and description frontmatter. Add pages to docs.json; use root-relative internal links.
- Consult current Mintlify documentation. Prefer built-in components and docs.json settings to custom CSS.
- Before publishing, run mint broken-links, mint openapi-check api-reference/openapi.json, and mint validate when supported; preview desktop and mobile.
- Record verification and its limits honestly. A valid local build does not prove DNS or production API availability.
