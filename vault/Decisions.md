# Documentation decisions

Accepted decisions are historical records. Add a new numbered decision to supersede one; do not silently rewrite its rationale. Living implementation detail belongs in the other vault notes.

## DOC-001 — Separate public documentation repository

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** explicit owner direction.

Publish `docs.alignr.io` from `ledgrhq/alignr-docs` using Mintlify. Keep application code and its product/engineering vault in `ledgr`. Docs-specific governance belongs in this repository's excluded vault.

**Reason:** independent documentation delivery, with explicit cross-repository maintenance when product behaviour changes.

## DOC-002 — Native theme and exact Alignr branding

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** owner-selected Resend reference and frontend branding.

Use Almond, Inter and restrained monochrome presentation with the application's blue icon and lowercase wordmark. Keep the light-mode logo legible. Prefer native Mintlify components over custom CSS and decorative widgets.

**Reason:** consistent navigation and responsive behaviour, with attention directed towards the content.

## DOC-003 — One app-user documentation journey

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** explicit owner feedback that a separate Controls top tab was disjointed.

Keep setup, assessments, controls, recipes and reference under Documentation with expandable sidebar groups. API reference and MCP remain separate developer tabs. Preserve existing page URLs when reorganising navigation.

**Reason:** readers should be able to progress from setup to understanding a control without changing documentation areas.

## DOC-004 — Explanations before definitions

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** review of dense baseline entries with the owner.

Control entries open with plain-English intent, applicability, defaults and limits. Put identifiers, metadata and JSON in a separate Definition tab. Tabs operate independently. Keep generated definitions tied to source declarations.

**Reason:** operational readers need the meaning first; engineers still need the exact condition.

## DOC-005 — Guided learning with honest examples

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** owner request for diagrams, examples and complete learning journeys.

Use fictional Acme consistently in the first-assessment journey. Provide checkpoints, recovery links and one recommended next action. Label illustrative observations; verify result examples against the evaluator. Keep quickstart short and reference pages searchable. Do not invent product screens or claim screenshot/example execution as a live acceptance test.

**Reason:** users learn by completing a meaningful task and understanding its result, not by reading a catalogue in order.

## DOC-006 — Documentation vault and continuous maintenance

**Status:** Accepted. **Recorded:** 2026-09-26. **Basis:** explicit owner request for a vault in the docs repo.

Require agents to read the docs vault before editing, update affected notes alongside public pages, and record decisions and validation. Exclude the vault from publishing and check its index and publication boundary in CI.

**Reason:** design intent and lessons must survive individual editing sessions. The requirement is a working practice backed by structural checks, not a claim of autonomous background synchronisation.
