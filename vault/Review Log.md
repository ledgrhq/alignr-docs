# Review log

Append dated entries. Keep evidence precise and do not turn planned checks into passed checks.

## 2026-09-27 — Curated standard draft copy (held candidate)

Prepared `mcp/copy-standard-draft.mdx` and a 25-tool generated catalogue against isolated application `04f63f0` and follow-up `057edb5`; this is not a deployed capability. Checked the REST/MCP route, service, response and scope contracts. The guide limits the action to a curated disabled draft with controls and manual checks, explains the user-owned `standards:copy` key, current owner permissions, opaque template revision, canonical UUID idempotency and historical replay. It directs a signed-in human to review and enable, and does not claim collection, evaluation, passing controls or vendor action. The MCP introduction and security guide, REST authentication, API-key and standard build guides, navigation and Information Architecture were updated. Reference generation used application source only, without a database or provider call; it emitted 13 curated reads and 25 MCP tools. The vault guard, generator compilation, JSON/whitespace checks, pinned Mintlify 4.2.939 `mint validate`, OpenAPI check, 90-page accessibility check and broken-link check passed. The initial validator attempt was blocked by sandbox access to the shared Mintlify preview cache; a scoped elevated rerun passed without changing the docs. Runtime, migration, independent content review, responsive preview, hosted release checks and publication remain pending.

## 2026-09-27 — Recoverable evidence refresh (held draft)

Prepared REST and MCP workflows against isolated application candidate `7c1e044`, not production. Read its route, schema, durable operation, worker and tool registry. The docs explain source-wide collection across all mapped clients, user-owned `integration:sync` and read-only `integration:read` for MCP versus the REST dot scopes, canonical UUID idempotency, same-caller/same-source replay, exact operation polling and safe `pending | running | completed | failed | interrupted` states. They distinguish completed evidence collection from unknown downstream assessment and passing controls. The generator, run offline with the candidate application source, emitted 12 curated REST reads and 21 MCP tools; it selected only the safe operation GET for the public OpenAPI snapshot. No DB or provider query was used for generation.

Initial DOC-R01/02/03/04/07 review traced token → source discovery → request → poll → uncertain-response recovery. It found the source list includes evidence-producing types regardless of current connection status, so the guide explicitly tells readers to check `status`; it also uses the exact code state `completed`, not the prose synonym “succeeded”. DOC-R08 local checks passed: 14-note vault guard, Python/JSON syntax, generated OpenAPI validation, 88-page accessibility check, whitespace and pinned Mintlify 4.2.939 `mint validate`. `mint broken-links` reported only the two existing maintainer README links to deliberately excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. Independent content review, mobile preview and production hosted checks remain pending. Astra's isolated runtime acceptance verified the source candidate with 25 passing tests, including authenticated REST/MCP probes and publication races; it does not establish production availability. Do not publish until the matching app implementation, migration, token picker and deployment are verified.

## 2026-09-27 — Exact-plan MCP review request (unpublished candidate)

Prepared an 18-tool draft against isolated application `925c29b`, checking the new MCP signatures/scopes, `remediation_review_service` preview/revision/idempotency flow and the existing pending approval path. The new `mcp/request-review.mdx` gives Claude Code and Codex users exact snake-case arguments, caller-generated UUID handling, the 15-minute revision and same-payload replay after an uncertain outcome. It distinguishes the old metadata-only outline from the local exact-plan request preview, and pending approval from execution or verified resolution. Introduction, connection, security, remediation and token guides were updated, and the tool catalogue was regenerated from source: eleven curated REST reads and eighteen MCP tools. The generator intentionally does not add the new REST routes to the selected read-only OpenAPI snapshot; the guide links the authenticated live schema for deployment-specific REST availability.

Source review found one draft overclaim: `mutating=True` does not imply `destructiveHint=true` for the request tool. Corrected generated warning against the actual registry annotation. Application commit `7a52214` adds `remediation:preview` and `remediation:request` to the token picker; the deployed contract still needs release verification. The docs vault guard, Python generator compilation, OpenAPI check, accessibility check across 86 MDX files and whitespace check passed. `mint broken-links` reported only the two existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. This is a documentation candidate only: no authenticated MCP call, DB test, responsive preview, deployment check or publication is claimed. Astra's follow-up review found four documentation gaps: the status/outline steps also need `remediation:read`; the two REST review routes accept the colon-named key scopes; a changed plan or target can block queued execution rather than the approval POST; and the token button reads **Deselect all**. Corrected the workflow, authentication and key guides against application source, including the now-offered token scopes in `7a52214`. Independent release-side review remains for the release owner.

## 2026-09-26 — MCP remediation plan outline (isolated candidate)

Prepared a separate 16-tool docs branch from `71e49e9`, preserving the 13-tool release and 15-tool remediation-status branches. Source inspection used the isolated application candidate `9d3c8fd`: the MCP scope and handler, `remediation_outline_service.py`, and its focused tests. The generated catalogue now documents `get_remediation_plan_outline` under `remediation:read`, backed by live `remediation.read` for user-owned keys. Regeneration produced eleven curated REST reads and 16 MCP tools; OpenAPI and navigation have no diff. The result is explicitly `metadata_only`, with unchecked execution/target readiness and unknown simulation mode. It gives bounded ID/action/reversibility/approval metadata, caps steps at 50 and signals truncation; it excludes parameters, targets, credentials, result payloads and plan fingerprints. Connection and remediation guides direct Claude Code and Codex to use the outline for broad plan intent, the separate run reads for lifecycle/verification, and the signed-in human workflow for target review and action.

Source/content review against DOC-R01/02/03/04/07/08 found no actionable claim that the outline authorises execution or establishes target readiness. `scripts/check-docs-vault.py` passed for 14 indexed notes; `mint openapi-check` passed; `mint a11y` passed for 85 MDX files; Python compilation of `scripts/sync-reference.py` and `git diff --check` passed. `mint broken-links` reported only the two existing README links to excluded `AGENTS.md` and `vault/MOC.md`, with no public MDX link failure. No responsive preview, authenticated MCP call, deployment check or publication was performed. Publish only after the matching application implementation and release are independently reviewed and verified.

## 2026-09-26 — Optional USD billing estimate (isolated draft)

Updated the separate 15-tool docs branch against application revision `96d4b05` (`1f7a17f` estimate implementation and `96d4b05` provider-error no-cache fix). Source inspection covered the billing route, response schema, tenant count query, fixed offer table, provider estimate validation and Account billing UI. Added the estimate section to Billing and support, a worked read-only API page, a token-scope example and one curated OpenAPI GET. Regeneration from the application checkout produced eleven REST reads and fifteen MCP tools; the MCP catalogue did not change. The example's $290.00/$261.00 monthly and $2,958.00 yearly ten-client subtotals were checked against source integer-cent prices and the generated offer enum.

Review against DOC-R01/02/03/04/07/08 kept billing optional and distinguished the displayed estimate from a checkout, invoice, payment or enforceable annual commitment. The response uses actual non-archived tenant client count and a ten-client billable floor; the documentation does not imply that the browser chooses quantity or price. `check-docs-vault.py` passed for 14 indexed notes, `mint openapi-check` passed, `mint a11y` passed for 85 MDX files, and `git diff --check` passed. `mint broken-links` again reported only two existing README links to excluded `AGENTS.md` and `vault/MOC.md`, with no public MDX link failure. The installed Mintlify CLI lacks `mint validate`. No authenticated estimate, provider charge, responsive preview, hosted-page check or publication was performed. Match the API deployment and independently review the content before publishing this branch.

## 2026-09-26 — MCP remediation status reads (isolated candidate)

Prepared a separate docs worktree from `c89cabe`, leaving the 13-tool release branch untouched. Source was the isolated application candidate `b095c17` + `6cd6b9a` + `cb429a7`, not a deployed endpoint. Regenerated `mcp/tools.mdx` against that checkout: 15 MCP tools, ten curated REST reads, no OpenAPI or navigation diff. Updated the MCP introduction, connection chooser, security and token-scope guide. The new copy limits the two tools to lifecycle status reads under `remediation:read`, backed by `remediation.read` for user-owned keys; it records bounds, exact status filter, stable ordering with unstarted runs last, tenant 404, fixed output fields and the distinction between execution, fresh verification, simulation and rollback eligibility. It makes no approval, execution or rollback claim.

Review against DOC-R01/02/03/04/07/08 found one wording issue: an initial security sentence implied all keys have owners; this was corrected to distinguish user-owned keys. No other confirmed content defect emerged in this local pass. `scripts/check-docs-vault.py` passed for 14 indexed notes. `mint openapi-check` passed; `mint a11y` passed for 84 MDX files. `mint broken-links` still reports only README links to deliberately excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. The installed Mintlify CLI has no `validate` command. `git diff --check` passed, and the generated catalogue diff contains only the two intended tools. No responsive preview, authenticated MCP call, live publication or production deployment was verified. This candidate must wait for the matching API review, DB/transport tests and release before publication.

## 2026-09-26 — Scoped MCP client-management documentation (draft)

Prepared a separate MCP client-management guide and corrected introduction, connection, security, token and REST cross-links against application commits `f047d6f` and `c98663e`. Source inspection covered the MCP registry and tool signatures, the Organization service's tenant-scoped name/ID page order, key/owner checks and write audit attribution. The guide limits its claims to list/create/update, gives exact snake-case tool arguments, distinguishes MCP `organization:write` from REST `organization.write`, requires a user-owned key and live owner permission, and directs uncertain creates to a slug lookup before retry. Regenerated the catalogue from source: ten curated REST reads and 13 MCP tools; the OpenAPI snapshot did not change.

`check-docs-vault.py`, `mint openapi-check`, `mint a11y` (84 MDX files) and `git diff --check` passed locally using Node 22 for Mintlify. `mint broken-links` found only the two existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. The installed Mintlify CLI does not provide `mint validate`. No authenticated MCP call, responsive preview or production-site check was performed. Do not publish this draft until the matching application release and public guide are verified.

Review correction: the Organization mutation principal also requires `must_change_password = false` for the key owner. The MCP guide, security page and generated create/update warnings now state this condition; they also clarify that revoked or expired keys cannot call the tools. This is source-backed documentation correction, not a fresh runtime verification.

## 2026-09-26 — Scoped client-write API documentation (draft)

Prepared a REST client-management recipe and corrected API-key, authentication and MCP guidance against application commit `366ecc5`. Source inspection covered the Organization routes, `mutation_principal` and integration tests for user-owned key writes, service-key refusal, owner permission and tenant checks, and agent audit attribution. The recipe describes only POST, PATCH and DELETE Organizations; it does not claim wider API-key writes or MCP client-write tools. Regenerated the curated reference from the current application checkout: ten read endpoints and ten MCP tools, with no generated diff. `check-docs-vault.py`, `mint openapi-check`, `mint a11y` and `git diff --check` passed locally using Node 22 for Mintlify. `mint broken-links` reported only the two existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. The installed Mintlify CLI does not provide `mint validate`. No responsive preview or authenticated live API check was performed. The source feature is not yet verified as deployed; do not publish this draft until matching API deployment and guide review are confirmed.

## 2026-09-26 — Five-step setup and separate Microsoft apps (draft)

Prepared public guide changes on `docs/five-step-setup-partner-tokens` against the clean docs checkout. Source inspection used application wizard commit `94a3461` for the five-step order and existing API-token form for bulk selection. The wizard commit is not yet the published app: the guide must be rechecked against the integrated release before publication. The two Microsoft registrations follow the production provider brief and purpose-specific backend work, whose deployment availability is still unverified. Direct subscribed-SKU wording was checked against Microsoft's Graph permission table: the already-required `Organization.Read.All` is an accepted application permission even though `LicenseAssignment.Read.All` is listed as least privileged.

Updated Quickstart, setup, Microsoft and token guides; marked older four-step screenshots as historical rather than presenting them as the current wizard. No generated API/MCP signature changed in this draft. `check-docs-vault.py`, `mint openapi-check`, `mint a11y` and `git diff --check` passed locally with Node 22 for Mintlify. `mint broken-links` reported only the two pre-existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`, with no public MDX failures. Responsive preview, independent content review, integrated app verification and hosted-page verification remain pending; do not publish this branch as release documentation until those pass.

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

## 2026-09-26 — Five-step setup and current still-image tour (draft)

Updated Quickstart, setup, Microsoft integration, token and MCP guidance against the five-step wizard and separate Direct/Partner registrations. PSA and RMM import guidance distinguishes client-record import from device evidence. Replaced the setup tour images with 1440×1000 captures of the current Microsoft, PSA, RMM, teammates and standards screens. Removed the public video, transcript and old four-step setup images. The API and MCP introductions now lead to the in-app Developer Console and state that Try it runs against the real workspace. Authentication guidance distinguishes key-compatible reads and MCP tools from ordinary REST writes requiring a human session; a matching write scope alone is insufficient. Docs typography now uses the app's Geist family with heading weight 500 and body weight 400. These changes are a local draft until the matching app release and hosted-page verification.

Draft validation: 14-note vault guard, OpenAPI check, 82-page accessibility check and whitespace passed. Mintlify broken-links reported only the two pre-existing maintainer README links to deliberately excluded `AGENTS.md` and `vault/MOC.md`; no public page failure. Local preview at 1440px and 390px rendered the tour with current setup tabs, images and navigation. Computed headings are weight 500, body weight 400, all Geist. API and MCP introductions rendered their Developer Console callouts. No production-hosted check or authenticated provider flow has been performed.


## 2026-09-26 — Typography governance reconciliation

The live/configured Geist family and prior verified 400/500 weights conflicted with the older DOC-002 and agent front-door Inter wording. Appended DOC-007, superseding only that font clause on the owner's explicit app/docs consistency instruction. Updated AGENTS without editing the historical decision or changing public presentation. Source comparison and vault guard only; no new browser result is claimed.

## 2026-09-27 — MCP help resources and approval review (draft)

Against app candidate `72bb978`, documented `alignr://help/getting-started` and `alignr://help/tools-and-scopes` as authenticated static MCP resources, separate from the 16 tools. Claude Code and Codex readers can discover them with `resources/list` and read them with `resources/read`; `tools/list` remains the source for deployed tool schemas. The Developer Console reference and REST **Try it** distinction is explicit, including execution against the real workspace. Against approval drawer candidate `a09604e`, the signed-in remediation guide now tells an approver to wait for current run, plan and concrete target details, use Retry after a load failure, and re-review if the target changes. No MCP approval or execution action is claimed.

Source review covered resource registration and authentication middleware tests, the tool registry, Developer Console behaviour and the approval drawer. Generated the catalogue from the application registry: 11 selected API read endpoints and 16 MCP tools, with only the resource section changed. DOC-R01/02/04/07 self-review traced introduction → connection → resource discovery → read and approval guide → current target review. It found no unsupported MCP action claim; the two resource URIs and real-workspace REST caveat match source. The vault guard, OpenAPI check, 85-page media accessibility check and whitespace check passed. Broken-links reports only the two pre-existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. This installed Mint CLI does not support `validate` (unknown command). This is a local docs candidate, not a published or live-MCP-verified guide. Independent editorial review and hosted protocol checks remain with the release owner.

Independent source review found two overclaims in the draft: approval POST checks pending state, requester separation and the autonomy ceiling, while the plan fingerprint and target are rechecked before execution; static MCP help-resource listing/reads authenticate but do not write workspace audit events. Corrected the remediation and MCP security guides accordingly. The approved run may later refuse execution, and help reads may update key-usage metadata without a workspace audit row. These corrections require release-side re-review; the earlier local checks do not establish the corrected text's hosted behaviour.

## Developer console request keys — 27 September 2026

Updated live-schema and remediation review guidance against the isolated TryIt implementation. UUID keys are explicit and stable, shared by cURL/confirmation/fetch; the console does not auto-retry. Candidate source tests and independent review remain in progress; docs remain held for the matching production release.

Independent Astra review approved this four-file documentation delta against TryIt24ae554. Pinned Node22/Mintlify4.2.939 vault(14notes), broken-links, OpenAPI and build validation pass. Initial build cache write was sandbox-denied; rerun with authorised cache access passed. Root local demo verified required-key UI and matching cURL/confirmation UUID without submitting. Publication remains held for matching API/frontend.
## 2026-09-27 — Held first-link API/MCP documentation candidate

Prepared source-backed REST and MCP first-link guides from isolated application `78fac8b` plus its REST query-alias follow-up, with the source-refresh docs at `b411109` as the base. Regenerated the curated snapshot offline from that candidate: 13 selected read operations and 23 MCP tools. Added `integration:map` token guidance, an exact existing PSA/RMM remote-record workflow, revision/idempotency replay rules, and the boundary between mapping, source-wide collection and assessment. DOC-R01/02/03/04/07/08 local review checked source paths, scopes, finite page bounds, response allowlists and failure/retry wording. The docs vault guard, whitespace, OpenAPI schema, pinned Mintlify 4.2.939 build validation, broken links and accessibility across 89 MDX pages passed. This is a held draft; no application migration, authenticated runtime call, mobile/browser preview, docs publication or hosted-page check has yet been completed. Revalidate the matching released API/MCP registry before publication.

## 27 September 2026 — First-link publication status

Production 7aeec59 completed workflow 36294031412; API/worker revision 17, exact image digest, migration 0068 exit zero and old-task retirement were verified. Matching frontend dpl_EXBpvqMKL56h2jXNSnN6E9K4GTW1 was promoted. Docs 8a3e167 passed workflow 36296145986 and both first-link hosted pages returned 200 with their respective contracts. Removed stale held-release wording, retaining live-schema discovery and real-workspace warnings. This does not claim real vendor acceptance or publish the later standards-copy candidate.

## 2026-09-27 — Held standard inspection guidance

The isolated application candidate adds two read-only MCP tools to inspect the
current workspace standards and an exact standard's controls/manual checks after a
disabled template copy. Updated the copy guide, permissions and generated catalogue
against that source. Offline generation produced 13 selected REST reads and 27 MCP
tools. The guide distinguishes controlled definition/instructions as untrusted data,
current state from historical copy receipt, and inspection from evaluation or
approval. Source runtime, independent review, full gate, live tool availability and
publication remain unverified at this draft stage.

## 2026-09-27 — Standards copy and inspection release preparation

Application release `ca2f0b3` has API and worker task revisions 18 with the release manifest's exact image digest. The Vercel production alias `app.alignr.io` independently read back deployment `dpl_7oUhZZio7jFAtKgJcs5PVjmR7VE5`, READY from the same source SHA. Reconciled this docs branch with current `origin/main` at `2770c36`, preserving the first-link publication note and the 27-tool standards copy/inspection catalogue. Replaced the copy guide's held-release notice with authenticated live-tool discovery wording. Vault guard, broken links, OpenAPI and pinned Mintlify 4.2.939 build validation passed on the reconciled branch. Desktop 1440×900 and mobile 390×844 previews showed readable heading, scoped-key guidance and navigation. Docs CI, hosted readback and live MCP invocation remain to verify before claiming publication.

Docs `e099248` published to main and workflow `36334882660` passed. The hosted [copy guide](https://docs.alignr.io/mcp/copy-standard-draft) showed the live-reference notice and scoped-key workflow; the hosted [tool catalogue](https://docs.alignr.io/mcp/tools) contained all four standard-library/copy/inspection tool names. This confirms public-page availability, not an authenticated live MCP invocation, a copied customer draft or an assessment result.

## 2026-09-27 — Held copied-standard activation guidance

Prepared a separate MCP workflow and REST recipe against the isolated activation candidate `53d1b65`. The workflow previews the complete bounded standard, control and manual-check policy, then enables only a disabled receipt-backed draft through a user-owned scoped key and one saved idempotency UUID. It distinguishes the historical activation receipt from current enabled state, workspace defaults from per-client overrides, and activation from evaluation or vendor action. Workspace-authored text in the preview is explicitly treated as potentially sensitive, untrusted data. The application candidate's focused activation tests passed 12 cases, including a same-count policy-edit regression; disposable migration and old-writer enabled-toggle checks passed. The offline generator produced 14 selected REST reads and 29 MCP tools. Vault guard, broken links, OpenAPI and pinned Mintlify 4.2.939 build validation passed; the first build attempt hit only a shared-cache permission error and the authorised rerun passed. These are candidate checks, not a public release or hosted protocol proof. Independent documentation review and publication remain outstanding.


## 2026-09-27 — Activation release reconciliation

Root reconciled held29-tool/14-read activation documentation with published
main1ad3bda, retaining the verified copy/inspection publication record and the
unpublished activation guide. Application candidate4dbe590 passed the complete
local gate; release PR10 at e11ebc9 awaits its final remote backend check. Held
activation notices remain until immutable API/worker and frontend verification.
No public documentation has been pushed by this reconciliation.


## 2026-09-27 — Activation validation before production rollout

Against application release candidate `e11ebc9` (merged to production as `7d74c18`), regenerated the curated reference offline: 14 reads and 29 MCP tools, with no generated drift. The vault guard (14 notes), whitespace, pinned Node22/Mintlify4.2.939 broken links, OpenAPI validation, build validation and accessibility checks all passed; accessibility examined 92 MDX pages. Production workflow `36338616971` is still running its pre-cloud gate, so activation notices remain held and this branch is unpublished.

Browser DOM previews loaded the exact MCP guide at desktop1440 and mobile390 widths, with the expected heading/body and document width equal to the viewport. Mobile navigation exposed the new guide. Screenshot capture repeatedly timed out in the browser CLI and in an isolated headless Chrome fallback. A subsequent measurement accidentally observed about:blank and was discarded; repeated measurements explicitly asserted the guide URL and heading. Native link/navigation completion was not verified: the preview retained the source route after activation, although the anchor href points to the valid REST recipe. Do not count these partial DOM checks as a complete screenshot or interaction pass. Existing published setup screenshots have not been replaced by these attempts.
