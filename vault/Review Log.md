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

## 2026-09-26 — Troubleshooting and backup recipe

Reworked troubleshooting into symptom-led investigations with recovery checkpoints. Added a backup recipe combining source-verified template settings, illustrative timestamp cases and a separate restore review. Clarified the false-versus-missing wording in the results guide. Validation: build, broken-link, whitespace and vault checks passed. Template defaults (1 day, range 1–30; restore cadence 30 days) and 12-hour, 36-hour, future and exact-boundary timestamp comparisons passed against application source with a fixed evaluation clock. Browser checks covered symptom-anchor navigation, opening the missing-observation branch and its mobile layout. No client assessment or vendor recovery operation was performed.

## 2026-09-26 — Setup review loop

Two independent source/content reviewers inspected the setup and learning paths.
Confirmed findings: generic integration instructions conflated client-directory import
with evidence collection; mapping instructions omitted real entry points; copied disabled
standards had no explicit enable step before a guarded Run checks action; optional
scenario tabs introduced names used without context on the next page.

Fixes: explicit import/evidence paths, Clients → Import clients and Clients & sites
instructions, Review & enable → Enabled → Save changes, explained partial/zero-result
run outcomes, a recap at the journey handoff and a two-clock evidence diagram.
Source inspection covered IntegrationDetailPage, ClientImportWorkspace,
DeployWizardPage, StandardDetailPage and EditStandardDrawer. Added a reusable
Review Checklist. The second independent pass found no blockers. It refined identity-source wording and the observation-time label; both fixes were applied. Link, whitespace and vault checks passed. Desktop and 390px mobile mapping previews were inspected; diagram labels were shortened after the mobile review and the example IDs retained in an adjacent table. Exact staged-build validation passed. No authenticated app workflow was executed.

## 2026-09-26 — Final review and workspace administration

Source review used application revision bacee09 plus current working UI (SettingsPage contains concurrent changes). Added six focused guides: setup wizard, Workspace health, accounts/team, Settings directory, client configuration and Microsoft default/override selection. Navigation keeps these under Documentation; Introduction and Quickstart point to the wizard and ongoing administration. Updated the maintenance impact map.

Independent reviews checked setup and health against frontend/service logic, account invitations and authentication against UI/services, and Microsoft selection against ADR-0029 and the connection policy service. Five evaluator scenarios (pass, fail, missing, mixed failure/missing and empty population) matched the first-assessment journey. Confirmed and corrected two override issues: the current route is Checks → Automated checks, and Save override also enables the client control. Re-review verified the reachable menu and hidden-excluded toggle. Client creation instructions deliberately do not describe the retired general Edit client drawer as available.

Desktop and 390px mobile previews covered new guides, wizard diagram, Microsoft choice tabs and sidebar grouping. Shortened Microsoft diagram labels after the mobile pass. Vault, link, OpenAPI and accessibility checks passed during review; exact staged-build validation passed. No authenticated invitation, portal sign-in, Microsoft consent or production app workflow was performed. The guides describe current source, not independent production acceptance. Concurrent unrelated drafts in integrations, MCP and the longer quickstart remain outside this release.

## 2026-09-26 — Whole-app documentation coverage audit

Three subagents and the coordinator compared committed docs 0bf7785 with current app 565fae5. Reconciled 46 staff route declarations, separate external portal, shell actions and 38 connector-backed plus 8 unavailable catalogue entries. See [coverage map](Documentation%20Coverage.md) and four indexed evidence notes for source lines, coverage and prioritised missing tasks. Major gaps are operational workflows, manual reviews/reports, risk/roadmap, portal sharing and vendor/maintenance guides. This is source-based coverage, not whole-app runtime acceptance. No app behaviour or customer data changed.

Immediate fixes: token location/ownership/expiry/revocation, live explorer workflow and filtered-schema wording, retained MCP UI-scope boundary, optional argument text and manual-library count scope. Reference generation produced ten read endpoints (no schema diff) and ten tools; existing environment deprecation/email-validator warnings were recorded in evidence. An independent reviewer found the full-schema overstatement; corrected against developer.py. Remaining guides are deliberately recorded as open, not claimed complete.

Release verification: exact staged Mintlify build passed; vault guard checks all 12 notes recursively and rejected an intentionally unindexed nested probe. Desktop token and 390px advanced-definition previews inspected. No new endpoint schema changes.
