# Review log

Append dated entries. Keep evidence precise and do not turn planned checks into passed checks.

## 2026-09-26 — Foundation and navigation

Existing public commits include `6f09980` (control catalogue), `b0c0f42` (provisioning wording) and `0c08dc4` (unified navigation and newcomer improvements). Three reviewers examined setup, learning/control and API/MCP pages for the latter change. Local build/link/accessibility checks and hosted deployment were verified. This records prior work, not a fresh retest of every page.

## 2026-09-26 — Guided journey and documentation vault

Added a four-page Acme assessment journey, a recipe index and vulnerability threshold recipe. Updated Introduction and navigation to make guided learning discoverable. Established the docs vault, agent entry points and a CI structural guard. Validation: Mintlify build and broken-link checks passed; the vault guard passed and rejected three injected faults (missing exclusion, public vault link, unindexed note). The identity and vulnerability scenarios passed against the application pure evaluator. The local `/vault/MOC` URL returned 404. Scenario tabs were exercised in browser; this is not a live assessment of a client. Main application AGENTS/CLAUDE docs guidance parity also passed.

### Remaining improvements

- Annotated screenshots from a current, authorised, non-sensitive app workspace. No suitable screenshot source has been established in this task; do not substitute invented UI.
- Observe real first-time users completing the journey and record where they hesitate. No usability study or completion-time claim has been made.
- Extend recipes only when each has a distinct useful question and source-verified outcome.
- Review the new journey when source collection, control evaluation or UI labels change; updating the catalogue alone is insufficient.
