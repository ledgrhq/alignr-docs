# Alignr documentation

This separate repository publishes the public Mintlify site for docs.alignr.io.

## Read before every change

Read [vault/MOC.md](vault/MOC.md) and the relevant linked decisions, information architecture, editorial standards and maintenance workflow before editing. This vault is the source of truth for documentation design and governance; the application vault remains authoritative for product behaviour. Update affected vault notes and the review log in the same change as public content. Record new decisions explicitly, and index new notes in MOC. Do not claim the vault is automatically maintained: agents must perform this work.

Run `python3 scripts/check-docs-vault.py` before publication. The vault and agent instructions must remain excluded by `.mintignore`; never link them from public MDX.

## Public documentation rules

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
- Explain predicates using a readable label, what is observed, and what the observation cannot establish. Registration is not enforcement; product presence is not health or successful recovery.
- Maintain `reference-data/predicates.json` and run `python3 scripts/build-predicate-reference.py /path/to/ledgr` when the fact vocabulary changes. Keep missing/false/zero distinctions and set-valued semantics accurate.
- Diagrams use Mermaid code fences and must have an adjacent prose explanation. Check their rendered desktop/mobile layout, not just their syntax.

- When seeded controls, library templates, manual checks or parameter defaults change, run `scripts/build-control-reference.py /path/to/ledgr` using the application Python environment and `PYTHONPATH`. Review generated categories and the catalogue snapshot, then update hand-written controls guides and baseline overview counts. Keep seed availability distinct from copyable library drafts.
- Changes to predicates, producer semantics, operators or overrides also require reviewing worked examples, interpretation limits and diagrams; regeneration alone is not sufficient.

- Keep app setup, assessment and control guides together under Documentation using expandable sidebar groups. API reference and MCP are developer tabs. Explain this reading path on Introduction; never address navigation tabs by array index in generators.
- Lead control entries with a plain-English explanation and applicability. Keep predicate identifiers, metadata and JSON in the Definition tab, with tabs independent per entry.
