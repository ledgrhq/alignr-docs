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

## 2026-09-26 — Close application documentation gaps

Delivered 22 new pages and expanded remediation, organised under task-based Documentation groups. All thirteen audited writing gaps are covered. Three subagents supplied source-backed implementations and independent cross-review; see [implementation evidence](Review%20Evidence/Implementation%20Review.md). Corrected domain withdrawal, integration fact retention, SonicWall scope, portal setup and standalone-rule defaults. Provider limitations remain explicit, especially Pax8 delegated OAuth.

Validation: 73-page build, broken links, API schema command, accessibility media-attribute check, whitespace and 13-note vault guard passed. Representative desktop and mobile previews inspected; fictional parser/evaluator/API fixture checks passed. This is documentation verification, not authenticated app/vendor acceptance. Concurrent signup/integration/MCP drafts are excluded from this release.

## 2026-09-26 — Signup, own-directory setup and MCP client entry

Reviewed the pending Quickstart, integration and MCP connection drafts against application `b844f92`. The checkout was at `89bb8ec` for reference generation; the affected MCP, integration-route, API-key and developer-contract files had no diff since `b844f92`. Checked signup/welcome-email queuing, automatic connection-key status and retry, the wizard's optional navigation, own-partner-directory scope and bounded preview, and the explicit invitation step. Corrected the token entry path to the main **MCP** navigation item. The Codex bearer-token configuration matches [official OpenAI guidance](https://learn.chatgpt.com/docs/extend/mcp?surface=cli); the Claude Code environment-expanded HTTP header matches [its MCP guide](https://code.claude.com/docs/en/mcp). The connection guide describes only the currently exposed bounded tool set; it makes no promise of headless setup or remediation parity.

Re-review: followed Quickstart into the wizard and integration guide, and MCP token creation into client configuration. API `POST /integrations/{integration_id}/microsoft-directory-users` requires both `integration.manage` and `user.manage`; the service checks the selected MSP partner tenant, returns at most two pages and records whether more remain. Preview does not send invitations. The welcome email is queued after signup and links back to `/setup`; local source inspection does not prove inbox delivery. Key protection must be ready before new credentials or OAuth authorisation; there is no user-managed AWS key step.

Validation: reference generation produced 10 curated read endpoints and 10 MCP tools with no generated diff. `check-docs-vault.py`, `mint openapi-check` and `mint a11y` passed (74 MDX pages); `git diff --check` passed for the owned files. Local Mintlify preview was inspected at 1440px and 390px for Quickstart, and at 390px for the new integration and MCP sections; headings, links, code blocks and navigation rendered. `mint broken-links` returned two links in unchanged maintainer `README.md` to intentionally excluded `AGENTS.md` and `vault/MOC.md`; it reported no public MDX failures. This Mintlify CLI has no `mint validate` command. No authenticated Microsoft consent, welcome-email inbox check, live MCP client session or production-site check was performed. The docs commit is held locally for coordinated publication after the app release.

## 2026-09-26 — AI assistant capability guide

Expanded Ask Alignr with a task/prompt matrix, first-message walkthrough, supported draft operations, client-only backup example, permissions and limitations. Introduction links directly to it. Checked AlignmentAssistant, AskComposer, answer/tools, standard_change_tools and assistant_changes_service. Corrected omitted detection_rule.read and organization.read permissions. New standards/controls remain inactive; global edits, inheritance restoration and autonomy constraints are explicit. Source review and documentation checks only; no live AI or configuration mutation exercised.

Assistant-guide validation: Mintlify build, broken links, OpenAPI command, media accessibility and vault guard passed. Desktop and 390px mobile previews inspected; the capability table uses horizontal scrolling on narrow screens. No live assistant session was exercised.

## 2026-09-26 — Evaluation and client-meeting journeys

Added pilot success criteria, five verifiable checkpoints, evaluation worksheet, operational handover and a complete client-meeting playbook. Independent journey audit confirmed five gaps: evaluation criteria, pilot-to-operation handoff, meeting narrative, honest historical comparisons and decision routing. Reviewer caught the global activation boundary: a one-client Run checks selection is not an isolated global standard. Added an explicit warning and owner/cadence handoff. Claims reuse source-reviewed setup/report/risk/portal semantics; no new product feature or ROI promise.

Remaining quality work: genuine app screenshots and short annotated walkthroughs; deeper vendor prerequisites/consent/error walkthroughs verified with authorised test accounts; public trust/data-handling information verified against actual operations and approved policy; developer write-workflow coverage beyond the curated read reference; plan/entitlement and support guidance once authoritative public commitments exist; observed usability sessions and measurement of search failures, task completion and setup abandonment. These are unverified needs, not invented guarantees or production claims.

Journey validation: 75-page Mintlify build, broken-link check, accessibility check, OpenAPI command and 13-note vault guard passed. Desktop pilot and 390px meeting previews inspected. No live client meeting, pilot outcome or conversion improvement was measured.

## 2026-09-26 — Visual onboarding, trust, developer writes and measurement

Added six genuine local-demo screenshots and an 18-second screen slideshow with adjacent time-coded transcript; captures verified in browser, no production/customer data used. Microsoft and Meraki setup guides checked against current app source and official provider documentation. Added operational security/data and billing/support guides without promoting aspirational vault policy into commitments. Added a dry-run-first inactive-standard Python recipe: human JWT required, parent and control disabled, one POST/no automatic retry. Ten offline tests, app schema/definition validation and independent review passed.

Three subagents supplied bounded implementations and independent reviews. Source ranged from 858bcaf through 002938e amid unrelated concurrent worker changes. Corrected the application vault's registration-report permission to AuditLog.Read.All against Microsoft Graph documentation. Captured source/code evidence is summarised in the new Usability and Measurement note.

Live docs search exposed invitation and non-GDAP findability issues; improved titles/wording. Prepared eight human-study tasks, an empty de-identified CSV worksheet and validated summariser (assisted outcomes preserved; non-finite duration rejected). This is study infrastructure plus an agent walkthrough, not completed human research. Mintlify dashboard redirects to login; analytics entitlement/configuration is unverified. No paid add-on or tracker was installed. Approved commercial/privacy policies and vendor test accounts remain external prerequisites.

Final verification: 81-page Mintlify build, links, OpenAPI and media accessibility checks passed; 14-note vault guard passed. Desktop/mobile visual tour and Microsoft guide rendered; responsive video reached its 18-second end state. Mintlify omitted nested caption tracks, so a time-coded text transcript is provided. Independent review caught malformed CSV acceptance; exact headers, row shape and blank-identity checks now reject all three reproduced cases. No live vendor, billing, API-write or independent-human acceptance is claimed.

Release 5502799: GitHub validation and Mintlify deployment passed. All six new guides plus the MP4 and screenshot assets returned HTTP 200 with correct media types. Live search for invite teammates now returned the intended account/team guide first; before the title change it was absent from the six displayed results. This verifies one search task, not independent-human usability or conversion uplift.
