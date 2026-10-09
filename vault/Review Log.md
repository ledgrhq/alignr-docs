# Review log

Append dated entries. Keep evidence precise and do not turn planned checks into passed checks.

## 9 October 2026 — docs logo verified live after PR49

After PR49 merged as `12ac46af1bfb38d14adf48d4a82b894ef3857065`, a browser
review of the public `https://docs.alignr.io/introduction` page confirmed the
new logo is clear and unclipped in desktop light and dark themes and at 390 ×
844 mobile in dark theme. GitHub Documentation checks for the merge commit
completed successfully in [run 37900063273](https://github.com/ledgrhq/alignr-docs/actions/runs/37900063273).

The public page is live, but GitHub's deployment record for the merge SHA is
labelled `staging` even though its target URL is `docs.alignr.io`; the GitHub
production deployment record has not caught up. This browser readback verifies
the visible page, not a production deployment record. No full-site accessibility
or broader browser-matrix review was performed.

## 9 October 2026 — application logo live; PR49 hold cleared

The application logo from PR211, with the 22px sidebar adjustment from PR228,
is live at `app.alignr.io`. The exact Vercel production candidate
`dpl_414vZp72kaJRWuoeNSMKbrFVqs92` was read back on the public alias after
promotion. Its protected build was checked against the production API base
`https://api.alignr.io/api/v1` before promotion. The public `/login` page then
served the candidate's assets; its home link contained the outlined SVG and no
`alignr-wordmark-text` element. Browser captures of the public sign-in page in
dark and light themes showed legible blue icon and outlined lettering. The
owned test browser was closed.

This supersedes the *publication hold* in the 8 October entry, not that entry's
preview evidence. PR49's hosted preview and validation were independently
reviewed again before merge: the preview renders the logo in both themes,
`mint a11y` passed on 97 MDX files, and the two `mint broken-links` failures
remain the same excluded README links on clean `main`. The docs production
deployment and `docs.alignr.io` live header still require verification after
the PR merges. This is a logo release check, not a full-site accessibility or
browser-matrix audit.

## 8 October 2026 — logo drawn as outlined artwork (held for application PR211)

Claude replaced `logo/light.svg` and `logo/dark.svg`. They previously set the
"alignr" wordmark as live Arial text (21px/400, −0.9px), which rendered with
whatever font the reader's system had. They now carry the same outlined
artwork as the application's `Logo.tsx`: the 20px icon tile, a 7px gap and
Geist Medium lettering drawn as paths, in `#202024` (light) and `#EEEEEF` (dark)
to match the application's workspace text colours. `favicon.svg` already
matched the application's icon and is unchanged. This keeps DOC-002/DOC-007's
exact Alignr branding; no decision changes.

Source: application PR211 (`claude/logo-as-image`, commit `2df7274e`), which
moves the app logo from Arial text to the same outlined SVG. alignr.io and its
brand page already use this artwork (ledgr-website `b56a23a`, `432e3ae`).
Publication is held until PR211 merges and deploys, so the help site never
shows a logo the application does not.

Checks on PR49's original logo commit `0ed479dd8a6f00a30232c2a9989d5ebf093dec07`:
`python3 scripts/check-docs-vault.py` and GitHub's documentation validation
passed. `mint broken-links` reported only the two README links to excluded
`AGENTS.md` and `vault/MOC.md`, also present on clean `main`; the installed
Mintlify CLI does not provide `mint validate`, so that command was not run.
No page content, navigation or reference data changed.

Codex root reviewed the [hosted PR49 preview](https://alignr-brand-docs-logo.mintlify.site/introduction)
on 8 October before publication. At 1280px desktop in dark and light themes,
the blue tile and outlined wordmark rendered cleanly with the intended white
and dark lettering. At 390px light mobile, the header logo remained legible
without clipping. The preview's interactive tree exposed an `Alignr home page`
logo link. This is a rendered header check, not a full-site accessibility or
browser-matrix review. The owned browser session was closed after inspection.
The publication hold above remains until the application is deployed.

## 7 October 2026 — PR47 hosted preview review, publication still held

Codex root reviewed the hosted PR47 preview at source
`c862ea668aa4dad8e2ef5a4aef14b9521043a32d`, after its GitHub validation and
Mintlify preview checks passed. Application PR170 merged as
`435cd668d4ade5a07bd6558a0b2901d07a867ed7`; production workflow
`37679369462` is still running its repository gate at 20:25 UTC. This does not
establish deployment or live timeout acceptance. Docs PR46 is now published;
PR47 has been retargeted to main and remains held for the application runtime.

The changed errors guide rendered at 1440×1000 desktop and 390×844 mobile.
The timeout explanation and retry guidance wrapped legibly; mobile document
width matched the 390px viewport, with no horizontal overflow. The desktop
capture includes the lower timeout prose and retry section; the dedicated
mobile timeout capture includes the paragraph from its beginning. This is
limited rendered prose/layout evidence, not a fresh keyboard or full-site
accessibility audit. Source/contract review and four independent PostgreSQL
checks are recorded below; they remain distinct from live behaviour.

Review artifacts are private under `/private/tmp/alignr-docs47-root-review`
(`desktop-errors.png`, `mobile-timeout.png`, `mobile-errors.png`). The owned
`alignr-docs47-root` browser session was closed after inspection. No local
preview server was started for this hosted review. Next: verify the matching
application runtime, merge the reviewed docs after required checks, and inspect
the public errors URL before claiming publication.

## 7 October 2026 — Dashboard read timeout errors (held)

Updated `api-reference/errors.mdx` against the ALI-83 dashboard deadline candidate
in `/private/tmp/alignr-ali83-dashboard-deadline` (application checkout based at
`62a5048e`). Source review covered the two route call sites, the 12-second
read-only service wrapper, `DashboardReadTimeout`, its safe 504 envelope, and
the shared-session cleanup path. A timed alignment or operations read returns
HTTP 504 / `dashboard_read_timeout` without partial data. If bounded cleanup
cannot close the request session, the cleanup exception inherits the generic
HTTP 503 / `dependency_unavailable` response. The 12 seconds cover only the
service read; authentication and other request dependencies are outside the
budget, with up to three seconds of cleanup grace. The text expressly excludes
`/dashboard/workspace-home`, which remains a separate contract.

The curated OpenAPI snapshot contains `GET /api/v1/dashboard/workspace-home`
but not the alignment or operations reads, so no generated reference was
regenerated. The errors page directs deployment-specific callers to the
authenticated live schema and recommends a bounded backoff for transient read
failures. Application evidence independently rerun for this review was four
focused PostgreSQL integration tests: timeout stops the active statement and
the same session can run another query; operations returns its positive empty
workspace result; foreign-Organization reads return 404; and the permission
check remains enforced. All four passed. The test-owned post-timeout connection
is explicitly closed; no SQLAlchemy connection-GC warning appeared. This does
not establish full CI, broad load behaviour, deployment availability or hosted
documentation acceptance. The change is held on a branch based on open docs PR
#46 until matching application release and independent docs review.

Docs checks passed: `check-docs-vault.py` (14 indexed notes),
`mint openapi-check api-reference/openapi.json`, `mint a11y` (97 MDX pages) and
`git diff --check`. `mint broken-links` found only the two existing README links
to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link
failed. The available CLI was Mintlify 4.2.229 under Node 22.13.1; the repository
workflow's pinned 4.2.939 was unavailable, and this CLI has no `mint validate`
command. `mint dev` reported ready and a local GET of the changed page returned
200 with the new error text in its response; the preview process also logged
`ResponseAborted`. No desktop/mobile visual inspection or hosted readback was
performed.

## 2026-10-01 — Published Standards and Facts table search/sort docs

Updated `guides/standards.mdx` for the routed Standards table and
`guides/evidence.mdx` for Facts heading sorting. Standards search, filters,
sorting and pagination apply before the page slice; the bare `GET /standards`
retains its historical full-list response. Facts sorting applies to the complete
matching result before paging and value order uses the safe public projection.
The generated OpenAPI reference was checked against composed app source
`c21594796c4436447a0cec0681d6506592d9c6da`; no MCP catalogue change was needed.

Docs PR #19 exact head `eafc2b40e91d6cd44667657e4bf901564e0f5f74` merged to main
as `0f7ab8ba229c2c97e6e29cc20dadb853f100103e` at 13:58:29 UTC, after matching
application PR #50 was promoted. Main workflow `36872717239` succeeded, including
the vault guard, broken-link check, OpenAPI check and pinned `mint validate`.

Hosted readback at 14:01 UTC confirmed `https://docs.alignr.io/guides/standards`,
`https://docs.alignr.io/guides/evidence` and
`https://docs.alignr.io/api-reference/openapi.json`. The hosted Standards text
states the search and page-size bounds, sort orders and bare-list compatibility;
the Facts text states full-result sort order, newest-first default and safe value
ordering. The hosted OpenAPI schema exposes the documented query options, and
reported Mintlify version `dpl_5WfBKS6uvB3ch6FqbAMNWRNXnopx`. No live application
endpoint call or hosted visual inspection was performed.

## 2026-10-01 — Held paged standard activation reference

Prepared an additive REST/MCP documentation candidate against frozen source in
`/private/tmp/alignr-standard-authoring-scaling`, based on application
`ffecfd01929f24abbd196c607388f26211bd397e` with activation summary/pages and
migration 0079 present in the worktree. The candidate adds the REST summary and
page routes to the selected OpenAPI reference and documents
`get_standard_activation_summary` and `get_standard_activation_page` under the
existing `standards:read` scope. Existing legacy preview/activation contracts
and MCP scopes remain available.

The guides lead with the paged flow: one 15-minute revision, three complete
sections, up to 25 rows and 240 KiB per page, and a new review after a stale
revision. They retain the legacy one-response preview and its 50-control,
50-check and 200-rule-scope bounds. Summary and page reads have a 10-second
service budget; final activation has a 5-second full-policy recheck budget. The
revision signs authored policy and saved assignments, not per-client overrides
or the full client roster; adding a client alone does not invalidate it. Copy
distinguishes these processing bounds from initial 30-control / 30 manual-check
create batches and the 5,000-ID assignment replacement request bound; it does
not claim unlimited total standard capacity. Activation still requires the same
user-owned key, current permission, explicit workspace acknowledgement when
applicable and an idempotency UUID. No evaluation, evidence collection or vendor
action is implied.

`scripts/sync-reference.py` ran in the isolated activation-validation API image
with `--no-deps`; it did not start a database or application stack. The source
registry produced 18 selected REST reads and 33 MCP tools. Generated output was
inspected for route parameters, schemas, error statuses, scopes and tool names.
With Node 22.13.1 and the locally cached Mintlify 4.2.939 package, the docs vault
guard, `mint broken-links`, `mint openapi-check api-reference/openapi.json`,
`mint a11y`, `mint validate`, Python generator compilation, JSON parsing and
`git diff --check` passed. The first validator attempt lacked access to the
shared Mintlify preview cache; the authorised rerun passed. Root's independent
review caught that the older offset-paged standard definition reader has a
10,000-offset limit and should not be a prerequisite for a full scalable review.
REST/MCP first steps now use it only for identity/scope sanity checks; the v2
summary and all policy pages are the authoritative complete review. Root
re-read and accepted the corrected contract explanations. A local `mint dev`
preview could not start because ports 3000–3009 were already occupied, so no
desktop/mobile visual read is claimed. This docs pass did not run application
suites; app focused evidence and the full gate are owned by the application
workstream. Independent review and the final application commit remain
outstanding. Branch is based on docs main
`3e368670c584daadb4e22973623a2da0c3a7620b` and remains held until the matching
app release; no production availability or hosted readback is claimed.

The candidate is in draft docs PR #17 on branch `docs/standard-activation-paging`
(reviewed content through `3f9d38b`). It remains intentionally unmerged until
the matching application change passes its full gate and is released.

## 2026-09-27 — Held setup continuity and five-step visual refresh

Prepared `guides/setup-wizard.mdx` and `journeys/visual-tour.mdx` against application UI source `506cf71` after checking `SetupWizardPage` and `BaselineIntakePage`. The guide now explains the Standards-to-baseline hand-off, Back to the Standards step, account-scoped same-browser Resume/Start again and inactive-save review boundary. It does not describe the later requested Microsoft domain lookup or separate admin-consent flow, which are not in this release candidate.

An authenticated local seeded demonstration workspace at `http://localhost:5173` supplied all five current wizard captures at 1440×1000, replacing only `images/walkthroughs/setup-{partner,psa,rmm,teammates,standards}.png`. Capture date: 2026-09-27; the mounted application's setup UI files matched reviewed candidate `506cf71` (no diff in the affected UI paths). The PSA/RMM choices were allowed to finish loading before capture. The Microsoft image includes a local environment-specific Partner application availability notice; it does not assert production availability. Visual inspection found no customer records, credentials or transient loading state in the captures. Browser navigation to each supported step URL was read-only; no connection, invite or standard was submitted. Agent-browser's click reported success without changing the SPA route, so URL-based step navigation supplied the captures and native click/keyboard behaviour is not established by this pass. Prior application browser QA independently checked the Standards hand-off and draft return at 390 px.

The docs vault guard passed for 14 indexed notes, `git diff --check` passed, and cached pinned Mintlify 4.2.939 checks passed: no broken links, valid OpenAPI, accessibility across 92 MDX files and build validation. Desktop 1440×900 and mobile 390×844 local previews loaded both exact routes, rendered the guide and all five tour images, and had document width equal to viewport width. Captures: `/private/tmp/alignr-setup-docs-{guide,tour}-{1440,390}.png`. The full desktop screenshots scale down within the tour's Frame; the prose remains the readable instruction. The preview did not test a hosted page or production setup. This candidate remains held pending independent copy/image review, matching PR11 application release, docs CI, publication and hosted readback. API/MCP generated references are unaffected.

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

Review against DOC-R01/02/03/04/07/08 found one wording issue: an initial security sentence implied all keys have owners; this was corrected to distinguish user-owned keys. No other confirmed content defect emerged in this local pass. `scripts/check-docs-vault.py` passed for 14 indexed notes. `mint openapi-check` passed; `mint a11y` passed for 84 MDX files. `mint broken-links` still reports only README links to deliberately excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. `git diff --check` passed, and the generated catalogue diff contains only the two intended tools. No responsive preview, authenticated MCP call, live publication or production deployment was verified. This candidate must wait for the matching API review, DB/transport tests and release before publication.

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

## 2026-09-27 — Activation release verified; publication preparation

Production workflow36338616971 succeeded for7d74c18. Direct AWS readback confirms migration0071 stopped with exit0 and the exact manifest digest, API/worker revision19 are sole COMPLETED primaries at desired/running1, and remembered old tasks actually STOPPED. Public readiness and activation OpenAPI contracts pass. Matching Vercel deployment dpl_CRfTTSScQvBNkg8Pzuh3noeKMmmp is promoted with domain readback; temporary build access was revoked. Removed only the two stale held-release notices, retaining authenticated live-schema/tool discovery. This is not evidence of an authenticated production activation mutation or live vendor assessment.

An independent fresh agent-browser session resolved the earlier preview capture failure. Both REST and MCP activation guides loaded their exact URLs/titles and settled article content at1440 and390px. Captures are `/private/tmp/alignr-docs-activation-{rest,mcp}-{1440,390}.png`; mobile menu captures end `-mobile-nav.png`. The reviewer inspected all four article captures, found readable layout without obvious overflow, and checked mobile menu links and the cross-guide destinations. Root also inspected the REST390px capture. These captures include the pre-removal hold notices; page structure is unchanged. Docs CI and hosted publication readback remain pending.

Publication completed as **274862d**, validation workflow **36341693672 SUCCESS**.
Both hosted activation guides return200, contain the expected title and no longer
contain the stale held-release notice. Readback is retained in
`/tmp/alignr-prod-work/release-pr10/docs-hosted-readback.json`. This closes public
publication acceptance, not an authenticated activation mutation or assessment.

## 2026-09-27 — Setup continuity published

Application production `dfcc95e744383c7a292b6e2948acf4de8767a832` completed
workflow36344303838. API/worker revision20, migration0071 and exact image digest
were independently verified; matching frontend `dpl_GMjtdJ55C7beaHa4bWBPSujTjDJh`
was promoted with app-domain readback. Docs `c1d8b9d` published with validation
workflow36347252295 SUCCESS. Hosted `/guides/setup-wizard` and
`/journeys/visual-tour` returned200 with updated return/draft copy, and all five
`images/walkthroughs/setup-*.png` matched the reviewed local SHA-256 bytes exactly.
Readback retained in application release evidence `/tmp/alignr-prod-work/release-pr11/`.
Domain lookup and explicit partner admin-consent are separate candidates and are
not claimed by this publication. No real Microsoft connection acceptance is implied.

## 2026-09-27 — Held Microsoft lookup and partner consent guidance

Updated the setup wizard, workspace settings, Microsoft preparation, client connection and visual-tour prose against isolated application candidates `/private/tmp/alignr-microsoft-domain-lookup` (`e2068e7`) and `/private/tmp/alignr-partner-admin-consent` (`1cbd8c2`). The optional domain lookup is in the **Add connection** form, reads public Microsoft metadata and requires a human to confirm the tenant ID; it does not establish ownership, consent or connection. The partner flow now has separate administrator-consent and delegated-authorisation actions. The consent callback records only a dated return; actual authorisation and per-customer access remain separate checks. Existing Direct and customer consent instructions remain. No API/MCP reference changed.

This is an unpublished candidate. The exact cross-resource Microsoft admin-consent request has not been accepted by a live provider, and neither app candidate has completed the combined release gate. The docs vault check passed for 14 indexed notes; `git diff --check`, OpenAPI validation and accessibility (93 MDX pages) passed under Node 22. Broken-links found only the two unchanged maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. Desktop/mobile docs preview and hosted readback remain outstanding.

Rebased this held draft onto published docs `559a7db`, retaining the verified setup-continuity publication record. Revalidated with pinned Node 22.13.1 and Mintlify CLI 4.2.939: `mint validate`, `mint broken-links`, `mint openapi-check` and `mint a11y` all passed (92 MDX pages on the rebased source), as did the 14-note vault guard and whitespace check. The first `mint validate` attempt could not clean Mintlify's shared preview cache under sandbox permissions; an authorised rerun passed. Publication and provider acceptance remain outstanding.

Recaptured the empty Microsoft wizard step from authenticated local demo app `5b4f600` at 1440×1000 and inspected its full 390px layout on 2026-09-27. The mounted `SetupWizardPage.tsx` and `WorkspaceMicrosoftConnection.tsx` SHA-256 values matched the root source before capture. No connection was selected, consent requested, provider contacted or workspace write submitted. The 1440px capture `/private/tmp/alignr-microsoft-wizard-1440.png` was byte-identical (SHA-256 `8b05f43dfd2ca8cb36d96a8920fe82cbdff580c2525066369e718fdea6051aa9`) to the existing `images/walkthroughs/setup-partner.png`, so the public image needs no binary replacement. The 390px full capture `/private/tmp/alignr-microsoft-wizard-390-full.png` showed readable guidance and actions without horizontal overflow. This empty state does not show the two buttons, which appear only after choosing a connection; the tour caption makes no claim that they are pictured. A staged/mock consent screenshot was not used.

## 2026-09-27 — Held one-client headless evaluation guides

Prepared REST and MCP workflows from isolated app candidate `d65fc8a`. They bind one enabled standard and explicit Organization to a 15-minute same-key preview, a durable idempotent request and an exact historical poll. They distinguish controls from manual checks, source collection and standard deployment, and describe `unknown` as terminal to automatic provider replay. The generator produced 16 selected REST reads and 32 MCP tools from the candidate registry. The vault guard passed 14 indexed notes; pinned Mintlify 4.2.939 broken-links, OpenAPI check and build validation passed. The first sandboxed build reported an EPERM on the shared preview cache despite exit zero; the authorised cache rerun passed. This is a held source draft, not a published or production-verified feature. Independent source-alignment review and hosted release checks remain pending.

## 2026-09-27 — Combined held Microsoft and evaluation draft

Reconciled the Microsoft lookup/consent copy and one-client evaluation REST/MCP guides in a new worktree from published docs `559a7db`. Retained both Information Architecture boundaries and both dated review records; no public screenshot bytes changed. The combined source includes 16 selected REST reads and 32 MCP tools generated by the evaluation candidate. Pinned Node 22.13.1/Mintlify 4.2.939 checks passed: 14-note vault guard, whitespace, broken links, OpenAPI, 94-page accessibility and build validation. The sandboxed build first hit Mintlify's shared-cache EPERM; the authorised rerun passed. Independent Astra source review against application `5b4f600` found the copy aligned after `guides/settings.mdx` changed “an administrator's return” to “a return from Microsoft’s consent flow”; that callback does not verify the respondent's Microsoft role or identity. Astra reviewed source and content but did not run suites or a browser session. This is still a held draft: matching application release, hosted readback and live Microsoft mixed-resource consent acceptance remain outstanding. No docs push or publication occurred.

## 2026-09-29 — Guided domain setup and reference reconciliation candidate

Reviewed the released application checkout `e5f7e929e6614cbc39d086f83613f58bf70b25ba` against the setup and standards guides and visual tour. DOC-R01/02/03/04/07: checked the Standards and wizard entry labels, four guided domains, questions → connectors → review order, domain-first connector filter with category/All tools escape, per-account/workspace/domain browser draft, inactive save and workspace-wide activation boundary. The proposed Identity screenshot was omitted because the available older capture had stale step labels. No screenshot is presented as current without evidence.

The same source excludes billing from public OpenAPI and omits `ask_ledgr` from its MCP scope registry. Removed the obsolete billing API page/navigation/card and MCP Ask entry, retaining the human Billing guide and in-app Ask guidance. Offline regeneration from exactly `e5f7e92` yielded 15 selected API reads and 31 MCP tools. Inspected the other generated OpenAPI changes: detection/fact query bounds and source/domain filters, `failingSubjects` preview and standard `setupDomain` are source-derived release drift. The Issues UI category/domain follow-up is held separately until its application source and release are final.

Pinned Node 22.13.1 and isolated Mintlify 4.2.939 checks passed: vault guard (14 indexed notes), broken links, OpenAPI, 93-page accessibility, build validation and whitespace. The first `mint validate` run hit only a sandbox denial clearing Mintlify's shared preview cache; its authorised rerun passed. Local preview checked the standard guide and visual tour at 1440px and 390px, the setup guide, MCP tools and API introduction at 390px, and opened the tour's Standards tab. Exact URLs, headings and page width were checked; the old three-column table on the standard guide was changed to readable lists after the initial mobile capture. No authenticated app action, hosted docs readback, docs publication or independent human usability study is claimed.

## 2026-09-29 — Guided domain setup published and hosted readback

Docs PR [#1](https://github.com/ledgrhq/alignr-docs/pull/1) merged reviewed content commit `3d67b353` as `a271e5c08c5a882670d3145dc2ecfe8b12207234`. Main-branch Documentation checks workflow `36603305811` and Mintlify Deployment both completed successfully for that merge commit. An independent read-only review of the candidate found no blocker before publication.

The hosted HTTPS root redirected to `/introduction`. Direct hosted reads confirmed the guided-domain content in `/guides/setup-wizard`, `/quickstart`, `/guides/standards`, `/guides/build-or-import-standard` and `/journeys/visual-tour`. The MCP catalogue at `/mcp/tools` no longer showed `ask_ledgr`, and `/api-reference/introduction` no longer offered the billing estimate recipe. Hosted search for “guided domain” returned **Build one domain at a time** and **Use the setup wizard**; the first result opened `/guides/build-or-import-standard#build-one-domain-at-a-time` with **Answer questions**, **All tools** and **Save inactive standard** visible. This confirms public routing, rendered copy and search indexing, not an authenticated app workflow or live API/MCP call. The Issues Domain-filter guide remains a separate held follow-up until its application change is released.

## 2026-09-29 — Held Issues technical-domain filter guidance

Prepared `guides/triage-issues.mdx` against frozen application PR26 source `bcbac66249837bd4e9d742859e98ac6e7c011b61`. The Issues UI now labels a tenant-scoped `Detection.category` facet **Domain**, alongside Client, Issue type, Source, Severity and Status. Its options are queried from the full matching detection set before pagination; the selected facet is excluded from its own option scope. This is separate from the legacy `domain` URL parameter, which filters email/domain subjects and appears as a removable **Email domain** label. The guide avoids a fixed category list and does not equate finding category with standard setup domain. The existing curated API reference already includes the `category` and `domain` list parameters; the UI's option endpoint is outside the curated read-only API snapshot. Publication is held until PR26 production runtime is verified.

## 2026-09-29 — Issues technical-domain guide published

The application release owner reported PR26 production workflow `36605073368` successful, API/worker/scheduled image and readiness checks passing, and frontend deployment `dpl_HRr8S1VCfsFS4YW53FMoSZDacg7J` promoted to `app.alignr.io`. Their public bundle readback contained the technical-category facet, **All domains** and separate legacy **Email domain** label. These are release-owner runtime checks, not an authenticated Issues interaction by this docs reviewer.

Docs PR [#3](https://github.com/ledgrhq/alignr-docs/pull/3) merged independently reviewed content commit `5e66c4fd0dce3a547d913dba7edfd2d424d61880` as `857b0c8e7bcb90585b430847924d3492b0f020d9`. Main-branch Documentation checks workflow `36611540349` and Mintlify Deployment both succeeded for the merge commit. The hosted `/guides/triage-issues` page rendered the technical **Domain** category explanation, the non-fixed matching choices and the separate removable **Email domain** filter. Hosted search for “technical category” returned **Investigate before deciding** in **Review and triage issues** and opened `/guides/triage-issues#investigate-before-deciding`. This verifies public routing, text and indexing, not a live filtered result set or tenant-permission test.

## 2026-09-29 — Held Opus UI refinement guidance

Reviewed frozen application PR27 source `41548c6f653bfc4c12cd8bcd16bfb23083ce84fc` in `/private/tmp/alignr-opus-ui-elegance` against the public Reviews, Run checks, standards and guided-domain guides (DOC-R02/03/08). `AssessmentWorkPage.tsx` changes the queue tab to **Client reviews**, puts **Start client review** and **Schedule one check** together in the page header, and gives review rows **Start review**, **Continue review**, **Resume review** or **View review** according to state. It also uses **Scheduled**, **In progress**, **Paused**, **Completed** and **Cancelled** review statuses, plus **To review**, **Recorded**, **Skipped** and conditional **Needs decision** check labels. Updated `guides/client-reviews.mdx` to follow those actions and distinguish review progress from outcomes.

The inspected Deploy wizard still opens from **Run checks**, selects a standard and clients, reviews defaults and approval limits, and ends with **Run checks for N clients**. Guided-domain setup still follows questions → connectors → review; the new domain tiles and step indicators are decorative visual cues. Existing `quickstart.mdx`, `guides/standards.mdx`, `guides/build-or-import-standard.mdx`, `guides/setup-wizard.mdx` and visual-tour prose remain task-accurate. The visual tour has no Reviews, Deploy wizard or domain-setup screenshot; its Microsoft, PSA, RMM and teammate images are outside this pass's changed UI. No API/MCP, predicates or control catalogue changed, so generated references were not regenerated.

This is source comparison and a held docs candidate, not rendered application verification or publication. The final source-label recheck against `41548c6` found no copy change needed. Independent documentation review remains pending. No authenticated review outcome or app deployment is claimed.

Pinned Node 22.13.1 with local `mint` package 4.2.939 passed the 14-note vault guard, broken-links, OpenAPI, 93-page accessibility, build validation and whitespace checks on the first draft. An initial PATH ordered a different global Mint version first; its README-only link warning was discarded, and the pinned tool was rerun successfully. The first pinned build validation could not clear Mintlify's shared preview cache under sandbox permissions; an authorised rerun passed. The local `/guides/client-reviews` preview at 1440×900 and 390×844 showed the new labels, no old **Scheduled reviews** wording and document widths equal to the viewport. Screenshots: `/private/tmp/alignr-opus-docs-reviews-desktop.png` and `/private/tmp/alignr-opus-docs-reviews-mobile.png`. These are documentation renders, not the unreleased application UI. Independent source review found one omission in the first draft: **Needs decision** appears on a pending changed/disabled check. The guide and status inventory now include it; the vault guard, whitespace and pinned Mintlify build passed again after that correction. Independent read-only re-review against app `41548c6` closed the finding with no new blocker. Draft PR #5 checks passed on guide commit `6ffa26d` (Documentation checks workflow `36618143440` and Mintlify preview); the later vault-only record changes no public MDX. Application release and hosted docs publication remain pending.

## 2026-09-29 — Opus UI Reviews guide published

The application release owner confirmed PR27 merge `e9218389b533c3e995d477c6cd03ba6e077a0360`, successful production workflow `36619514451`, pinned runtime readiness and promotion of Vercel deployment `dpl_5skhbttTPXzJzVKVDt2dZ1tApeDp` to `app.alignr.io`, with alias readback and temporary-access revocation. These are release-owner checks, not an authenticated review completed by this docs reviewer.

Docs PR [#5](https://github.com/ledgrhq/alignr-docs/pull/5) merged the reviewed guide commit `6ffa26df09f376436b1a78c3442ef6038650c291` and final vault record `c0cfbf0cdd9260bb5e38ac5274d0940169a8eba3` as `86e544e89f34025990daa948429454805c92ef8a`. Main-branch Documentation checks workflow `36624834277` and Mintlify Deployment both succeeded for the merge commit. The hosted `/guides/client-reviews` page showed **Client reviews**, **Start review**, **Continue review**, **Resume review** and **Needs decision**, with no stale **Scheduled reviews** text. Hosted search for “Needs decision” returned **Work through a client review** and opened `/guides/client-reviews#work-through-a-client-review`. This verifies public routing, rendered copy and indexing, not a live manual assessment or permission check.

## 2026-09-29 — Guided domain questionnaire polish (held docs candidate)

Updated the setup, quickstart, standards and build/import guides against the isolated app candidate `/private/tmp/alignr-domain-setup-polish` (base `e9218389b533c3e995d477c6cd03ba6e077a0360`, candidate commit `e8bf24b82a7082d892466203fbf8456eff7c7c36`; `DomainIntakePage.tsx` SHA256 `f3c3732606c285abd7be770b55b1e9e0c31e404d2dcab93563e2dd6816feeb21`). The copy now describes one question per screen, optional check inclusion and skipped validation for excluded checks, a compact selected-check count, and the full check list at final review. It retains the connector stage, domain-first tool choices with other categories available, client matching, human-only Email & domains, and the inactive-save/activation boundary. Updated Information Architecture and Documentation Coverage alongside the guides. No API, MCP, predicate or control contract changed, so generated references were not regenerated.

`check-docs-vault.py` passed for 14 indexed notes; `git diff --check` passed. With Node 22.13.1 and installed Mintlify CLI 4.2.229, OpenAPI validation passed and accessibility passed across 94 MDX files. Broken links reported only the two existing maintainer README links to intentionally excluded `AGENTS.md` and `vault/MOC.md`. The prescribed `mint validate` command is unavailable in this installed CLI. The docs maintenance workflow pins Mintlify 4.2.939, which is not installed here. Local desktop/mobile preview remains unverified: Mintlify could not start because ports 3000–3009 were occupied, and agent-browser could not access its user-level socket directory under the current sandbox. No hosted readback was performed. Root independently reviewed the doc diff against the current PR28 candidate and passed the source claims, including the uncertain-save lock and same-save retry wording. This is an unpublished documentation candidate pending app integration/release, pinned CLI validation and responsive preview.

## 2026-09-30 — Guided standard question answers (held for app release)

Updated `guides/build-or-import-standard.mdx` to explain explicit Yes/No answer cards, inline follow-up settings, exclusion on No, unanswered state on new drafts, preservation of saved answers, question progress and full-width content. Updated the existing guided-domain design note in Information Architecture while preserving the newer released domain chooser and connector flow. Compared the copy with the in-progress `DomainIntakePage` changes in application worktree `feat/wizard-question-progress`, based at `f666395` with uncommitted implementation work. That base commit alone does not contain this behaviour; the docs change is a held draft and must not publish before the matching implementation.

`python3 scripts/check-docs-vault.py`, `git diff --check`, `mint openapi-check api-reference/openapi.json` and `mint a11y` passed under Node 22. `mint broken-links` reported only the two existing maintainer README links to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX failures. The installed CLI has no `mint validate` command. No Mintlify preview or app acceptance was performed; inspect desktop/mobile and verify against the completed implementation before publication. No screenshot or production availability is claimed.

## 2026-09-30 — Client overview and freshness (held app candidate)

Updated [Your daily review](../guides/daily-review.mdx) and [Run a client review](../guides/client-reviews.mdx) against the isolated application candidate in `/private/tmp/alignr-client-overview`, based at `0573e8ac9376e45e2244b9d41c7e79a5f6f16ddf` with uncommitted UI changes. Source inspection covered `ClientPage`, `ClientOverview`, `ClientControlsTab`, the query client and the manual review outcome handler. The guides explain the persistent client summary (current versus last-loaded assessment, recorded outcome counts and permission-dependent open issues), collapsed next steps and compact run disclosures, refresh on page focus with visible cached information after a failed refresh, and the standard-coverage refresh after a saved manual outcome. The summary chart is described as a result distribution, not a trend. Navigation and public API/MCP contracts did not change; generated references were not regenerated. The candidate remains held until the matching application release is confirmed.

Against docs `origin/main` `df5866b0`, `python3 scripts/check-docs-vault.py`, `mint openapi-check api-reference/openapi.json`, `mint a11y` (94 MDX files) and `git diff --check` passed with Node 22.13.1 and installed Mintlify CLI 4.2.229. `mint broken-links` reported only the two existing maintainer README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. `mint validate` is unavailable in CLI 4.2.229; the maintenance workflow pins 4.2.939. A local preview attempt could not start because Mintlify found every port from 3000 through 3009 occupied. Desktop/mobile preview, hosted readback and authenticated application acceptance remain outstanding before publication. No API/MCP catalogue changes or screenshots were made.


### 30 September — independent client overview source review

Review against application PR #33 corrected the summary label to **Check coverage** and clarified that the distribution includes never-run, not-covered and excluded checks. Navigation refresh, retained-data warning and manual-review invalidation claims matched source. Open issues card/link requires detection.read; dashboard aggregate-count permissions are a separate existing application contract, not a claim of this guide. Publication still awaits app promotion.

## 2026-09-30 — Designer workspace wizard flow (held for app release)

Updated `quickstart.mdx`, `guides/setup-wizard.mdx` and `guides/build-or-import-standard.mdx` against the unmerged application candidate in `/private/tmp/alignr-designer-wizard` (base application commit `4b1347f13e475c88c7dacf3c54ec767395e3f1c6`). Source inspection of `SetupWizardPage.tsx`, `SetupJourneyChrome.tsx` and `DomainIntakePage.tsx` confirmed that choosing a domain card opens its dedicated page outside the workspace wizard; **← Setup** and **Return to Standards setup** return to the workspace Standards step. The guided page labels its stages **Questions**, **Sources** and **Review**. Question labels show **Current**, **Current · Yes/No**, **Yes**, **No**, **Up next** or **Locked**; answered questions and completed stages can be revisited while future questions/stages remain locked until prerequisites are satisfied. Answers restore from browser local storage per account/workspace/domain, while **Save inactive standard** creates the server-side standard. Updated Information Architecture and Documentation Coverage accordingly. No API/MCP or generated reference changed.

Re-review against the changed task flow (DOC-R01/02/03/04/07): the quickstart gives the shortest correct entry; setup instructions distinguish the workspace wizard, dedicated domain page, browser draft and server save; the standard guide preserves the chooser and separate general/mixed standards path. The direct-card routes, labels, answer states, navigation limits and return links match the source. There is no API/MCP contract or generated reference change.

With Node 22.13.1 and locally installed Mintlify CLI 4.2.229, the 14-note vault guard, OpenAPI check, 94-page accessibility scan and `git diff --check` passed. `mint broken-links` reported only the two pre-existing maintainer README links to `AGENTS.md` and `vault/MOC.md`, which are intentionally excluded from publication. The prescribed Mintlify 4.2.939 package could not be downloaded because `registry.npmjs.org` DNS lookup returned `ENOTFOUND`; therefore the installed CLI's `mint validate` command is unavailable. Local preview could not start because all ports 3000–3009 were occupied. No app tests, rendered app acceptance, hosted docs readback or publication are claimed. This documentation branch is held until the matching app release is verified.


## 2026-09-30 — Selected-client standard and client-page documentation (held candidate)

Updated the guided-standard and setup explanations to state that **Create standard** saves an active selected-client standard with no assignments; **Deploy to clients** and **Save assignments** set applicability, while **Run checks** is a separate assessment. Clarified that new blank/general standards, curated library copies and checklist imports remain disabled and workspace-wide by default, while existing standards keep their saved scope. Updated the one-client pilot warning so it distinguishes selected-client applicability from choosing a client for a run.

Checked source in `/private/tmp/alignr-client-checks-clarity` (app base `0531397` plus uncommitted candidate) for `DomainIntakePage`, standard detail/deploy flow, assignments routes/service, connection chooser, client list controls and Facts table. Added a public REST recipe for `GET`/`PUT /standards/{standard_id}/assignments` and included the read operation in the selected OpenAPI snapshot generator. The GET requires `organization.read` and `detection_rule.read`; PUT requires `organization.read` and `detection_rule.write` plus a user identity. The write replaces the full unique ID set (up to 5,000); it does not run checks. MCP remains at 31 tools with no tool-name or scope change. `get_standard_definition` now reports `scopeMode` and `assignedClientCount`; activation preview reports actual `workspaceWide` and `assignedClientCount`, and signs `scope_mode`, `assigned_client_count` and `assignment_fingerprint` in policy. These MCP responses do not expose assigned client IDs; the REST assignments read is documented for that roster. Updated the MCP guides and catalogue descriptions accordingly. This docs candidate is held for matching application review and release; it is not a claim of production availability.

DOC-R01/02/03/04/07/08 source reconciliation is complete for the changed workflows. The generator completed against the candidate app and produced 16 selected REST reads and 31 MCP tools; the assignment GET was added to the curated REST selection. MCP tool names and scopes remain unchanged, but `get_standard_definition` now reports `scopeMode`/`assignedClientCount` and activation preview reports actual `workspaceWide`/`assignedClientCount` plus signed policy scope/fingerprint; its client IDs remain absent, so the REST assignments read is documented for that roster. `python3 scripts/check-docs-vault.py`, `mint openapi-check api-reference/openapi.json`, `mint a11y` (95 MDX files) and `git diff --check` passed with Node 22.13.1 and Mintlify CLI 4.2.229. `mint broken-links` reported only the two existing README links to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link failed. The installed CLI has no `mint validate` command. Local preview could not start because Mintlify found every port from 3000 through 3009 occupied. The existing Issues guide already explains the Status and Severity filters and their meanings; the current source change only places the dropdowns together, so no user guidance change is needed for that layout-only adjustment. I did not run app behavior tests, authenticated API use or hosted readback. These remain outstanding; publication waits for matching app review and release.


## 2026-10-01 — active guided setup follow-up

Updated the build/import guide against the isolated application candidate
`feat/active-standard-setup`: both domain and earlier baseline questionnaires
create active selected-client standards, followed by Choose clients. Corrected
the button label to Create active standard and clarified assignment entry points.
Blank creation, imports and library copies retain disabled workspace defaults.
Application source review includes truthful existing-standard readback; no claim
of absent prior checks for a recovered standard. This PR remains unpublished
until API0078 and the corresponding guided UI are verified live.

## 2026-10-01 — first-day client and page clarity (held PR candidate)

Updated `guides/daily-review.mdx`, `guides/organizations.mdx`,
`guides/standards.mdx`, `guides/build-or-import-standard.mdx` and `quickstart.mdx`
against application `feat/active-standard-setup` at `bc4b310` (count-first
overview, client-scoped Run all checks, Create standard, and Audit trail title)
and the isolated client-sort commit `74d8850` (heading sort cycle). Source review
verified that the client overview displays API `scoreCounts`: the API coverage
denominator is passing + failed + unknown + uncovered; excluded checks are
shown separately. Non-live pass/fail states are converted to unknown before
the API computes either percentage. The guides distinguish the one-client
automated evaluation from source collection and manual assessment; the Clients
guide says heading clicks cycle ascending, descending, then clear to default,
after search/filter and before pagination. Create standard opens the domain
chooser; workspace setup keeps its separate **Choose a domain** label. The audit
page heading now matches the Activity destination.

Updated Information Architecture, Documentation Coverage and this review log.
The change is explanatory UI guidance; no API/MCP contract or generated
reference changed. This is an update for held docs PR #11; it must not merge
until the matching application release. No production availability is claimed.
With Node 22.13.1 and Mintlify CLI 4.2.229, the vault guard (14 indexed notes),
OpenAPI check (valid), accessibility scan (95 MDX files) and `git diff --check`
passed. `mint broken-links` found only the two existing maintainer README links
to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link
failed. This CLI does not support `mint validate`. Local preview could not start
because all ports 3000–3009 are occupied; desktop/mobile rendering remains
unverified. The initial sandboxed fetch could not resolve `github.com`; an
authorised fetch then confirmed the PR branch was still at its base before the
commit. No authenticated app action or hosted docs readback was performed.
`1286ddf2192d744ce77399be93dfdceed508f203` was pushed to the existing PR
branch after `git fetch` confirmed the remote branch was at its base commit.
GitHub reports PR #11 head `1286ddf2192d744ce77399be93dfdceed508f203` and its
Mintlify Deployment check completed successfully. The branch remains unmerged;
the hosted docs were not read back, and the change remains held until the app
release.

An independent root review corrected the client-detail map: the active-check
coverage count and percentage belong to **Current assessment**, while **Check
coverage** shows the status bar, legend and total. The expandable progress
sections are named **Evidence collection** and **Automatic checks** in the
Checks tab, not “Details”. The daily-review guide now uses those exact locations
and labels. The vault guard, OpenAPI check, 95-MDX accessibility scan and
whitespace check passed again for this correction; broken-links still reports
only the two excluded README maintainer links. Mintlify CLI 4.2.229 still lacks
`validate`, and preview remains unavailable on ports 3000–3009. No hosted
readback was performed.


## 2026-10-01 — Held roles, API-key and detected-risk table controls

Updated `guides/account-and-team.mdx`, `guides/api-keys.mdx` and `guides/risk-and-roadmap.mdx` against the uncommitted table-controls candidate in `/private/tmp/alignr-client-checks-clarity` (application base `d349133548c901b262d72d998482eda6433058d6`, branch `feat/admin-risk-table-controls`). Source comparison covered `RolesPage.tsx`, `ApiKeysPage.tsx`, `RiskTab.tsx`, and the role/API-key list routes and services. The role and API-key list endpoints return the complete collection permitted to the caller; search, filters, sort and 25/50/100-row pagination then operate on that collection. Role search covers name/description, type filters cover all/system/custom, and sorting covers name, user count and granted-permission count. API-key search covers name, prefix and owner name/email, with status and owner/name sorting. Detected risks retain search across title/reference/client and severity/decision filters; sort choices are rank score, severity and name. Pagination applies to detected risks; manual assessment risks remain separate. No API/MCP contract changed, so generated references were not regenerated.

This is source inspection of an unmerged app candidate and an unpublished documentation draft. It does not establish app test results, authenticated interaction, deployment or public availability. Hold publication until the application owner verifies the implementation and release.

For this candidate, `python3 scripts/check-docs-vault.py`, `git diff --check`, `mint openapi-check api-reference/openapi.json` and `mint a11y` passed (94 MDX files) with Node 22.13.1 and Mint 4.2.229. `mint broken-links` found only the pre-existing README links to the intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX links failed. This CLI does not provide the prescribed `mint validate` command. Mint's `--port` option was not shown by `mint dev --help`, but the CLI accepted `mint dev --no-open --port 3100`; it started after `lsof` confirmed no listeners on 3100–3110 and local bind permission was granted. I stopped only this preview process. With agent-browser, I reviewed all three changed paragraphs at 1440×900 and 390×844; text wrapped within the content column without horizontal overflow. Captures are in `/private/tmp/alignr-docs-roles-anchor-desktop.png`, `/private/tmp/alignr-docs-roles-mobile-paragraph.png`, `/private/tmp/alignr-docs-api-keys-desktop.png`, `/private/tmp/alignr-docs-api-keys-mobile.png`, `/private/tmp/alignr-docs-risk-desktop.png` and `/private/tmp/alignr-docs-risk-mobile.png`. These are local documentation renders only. No app tests, authenticated interaction, hosted readback or publication were performed.



## 1 October — Issues search and sorting candidate

Draft guides explain indexed word search, exact email tokens, scope limits and named sort orders over the full result set. Application candidate: `/private/tmp/alignr-issues-search-sort`; no deployment claim. Curated OpenAPI regeneration and validation are part of this workstream. Hold publication until the API contract and UI are released together; the existing backend scan hold is not waived.

Prior table guides PR12 merged as `62bc54d`; main validation passed. Live Roles, API keys and risk guide paragraphs were checked, and hosted search found the risk guide. Matching application PR38 frontend is live; authenticated tenant workflows were not repeated in production.

Reference generation used the Issues candidate and produced its q/sort parameters. Unrelated unreleased standard-scope component changes were excluded from this PR; held PR11 owns those schema changes. This branch retains the baseline schema except the generated detections operation.

## 2026-10-01 — PR11 conflict reconciliation

Fetched docs `origin/main` at `62bc54d` (PR #12) and merged it into the held
PR11 branch. The only merge conflict was the append-only Review Log: preserved
both PR11's active-standard/client summary, Run all checks, sorting and label
records and PR #12's roles, API-key and risk table-controls record. PR #12's
published account/team, API-key and risk guides are also retained unchanged.
The PR11 candidate remains draft; neither PR is being merged as part of this
conflict resolution. The matching app release remains the publication gate.
With Node 22.13.1 and Mintlify CLI 4.2.229, the vault guard (14 indexed notes),
OpenAPI check, accessibility scan (95 MDX files) and `git diff --check` passed.
`mint broken-links` reports only the two pre-existing maintainer README links to
intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX links fail.
This CLI does not support `mint validate`. A local preview was attempted but did
not become available, so desktop/mobile rendering remains unverified. No hosted
docs readback or authenticated application check was performed.


## 2026-10-01 — PR11 public release

PR #11 merged to docs `main` as `4d7bc3124b60cebdc5fde28d4f07f282c832de97`
following successful GitHub validation and Mintlify Deployment checks. Application
release PR40 is live at `app.alignr.io`, aliasing deployment
`dpl_2f2dBJtaNaVnmjN7ENHhEaRN6hU8` from source `a7347a9435cccbea5622106ee2dab92ed518a671`;
API deployment workflow `36815756972` succeeded. Hosted docs readback will be
recorded after all approved guides are published.

## 2026-10-01 — PR11 and PR13 hosted documentation readback

PR #13 merged to docs `main` as `26fdcc14ffe3d4aee47716b242c2eadc02099290`
after successful GitHub validation and Mintlify Deployment checks. The public
readback was performed on `https://docs.alignr.io` after deployment, using
agent-browser. On Organizations and clients, the published client list guidance
says sorting cycles ascending, descending and default, applies to matching
clients before pagination, and has no separate sort menu. The Standards and
Build or import a standard pages confirm guided save creates an active
selected-client standard with no clients assigned, followed by Choose clients;
assignments do not run checks. Daily review describes Run all checks for enabled
automated checks on that client using collected evidence and distinguishes
Current assessment counts/coverage from the Check coverage bar and total.

The Issues guide and Pagination API reference read back the `q` search fields,
200-character API bound, word-token behavior, four sort values (`risk`,
`severity_desc`, `title_asc`, `title_desc`), tie-breaking and filtering before
count/page selection. The Assign standard clients page says an empty selected
scope means no clients; the activation guide says activation preserves saved
scope. No sign-in or customer data was used for this readback.

For the PR13 reconciled branch, the vault guard, OpenAPI check, accessibility
scan (95 MDX files) and `git diff --check` passed. GitHub `validate` and
Mintlify Deployment checks passed on PR13. `mint broken-links` reported only
the two pre-existing maintainer README links to intentionally excluded
`AGENTS.md` and `vault/MOC.md`; no public MDX links failed. Mintlify CLI 4.2.229
does not provide `mint validate`. Local preview was not available during the
prior PR11 validation; the post-release browser readback confirms hosted text,
not app behavior or responsive rendering.

## 2026-10-01 — Held workspace Billing navigation

Updated `guides/billing-and-support.mdx` to direct readers from the Settings directory
to **Billing**, matching the composed app candidate's `/settings/billing` route. Source
inspection at app commit `d5587da4e986b3c609625c3dba54fead7852d4c1` confirms that the
page requires `billing.read`, mutations require `billing.manage`, Account no longer
contains Billing, and legacy `/account?checkout=return` hints redirect to the new
route while preserving the server lookup hint. The provider route maps the
allowlisted `configuration_incompatible` response to HTTP 409 with the safe message
“Billing portal setup is incomplete. Contact support to finish setup.”; other provider
failures keep the generic temporary-unavailability response. The guide gives those
two distinct next steps. It does not claim that the provider's Chargebee Login versus
Single Sign On API setting has been changed, or that portal opening now succeeds.
There is no API/MCP contract or catalogue change, so generated references were not
changed. App test source and the combined candidate were inspected; this docs review
did not run application suites because the root agent owns the active serial gate.
The docs branch remains draft/held for app42 release and has not been published or
read back from the hosted site.

## 2026-10-01 — Held Datto unknown patch-status guidance

Prepared a documentation candidate against application commits `cd99774`
(`fix(detection): keep unknown Datto patch state out of failures`) and `e617d33`
(`fix(integrations): fail closed on malformed Datto snapshots`). Updated the
Datto RMM section of `integrations/psa-rmm.mdx`, `patch_status` human metadata
and generated predicate reference, and the generated seeded/BIOS endpoint
control explanations. Copy distinguishes an unfamiliar non-empty vendor value
(`unknown`, Needs evidence / `no_data`) from a recognised non-compliant failure;
a validated complete inventory can withdraw Datto's previous patch observation,
while malformed or incomplete inventory does not promote partial results.
Retained observations still follow freshness rules. No API/MCP schema, predicate
vocabulary, seed control or control definition changed, so the generated control
catalogue and OpenAPI/MCP references were not changed. Source inspection also reviewed the focused assertions for recognised pass/fail versus `unknown`/`no_data`, malformed pagination, and retention after malformed device identity; these app tests were not run in the docs workstream. This PR remains held
until the matching PR41 application release is verified; no public availability
or live connector acceptance is claimed.

The vocabulary/reference generators rendered 88 predicate descriptions and
retained the existing control catalogue counts (18 seeded controls, 7 templates,
15 library controls and 19 manual checks); `reference-data/control-catalogue.json`
did not change. The vault guard, OpenAPI check, accessibility scan (95 MDX files)
and whitespace check passed. `mint broken-links` reports only the pre-existing
README links to excluded `AGENTS.md` and `vault/MOC.md`; no public MDX links fail.
Mintlify CLI 4.2.229 does not support `mint validate`. A local preview at port
3111 was inspected at 1440×900 and 390×844; the edited Datto and patch-control
paragraphs wrapped without horizontal overflow (`scrollWidth` matched the
390px viewport). Captures are `/private/tmp/alignr-docs-datto-psa-rmm-final-desktop.png`,
`/private/tmp/alignr-docs-datto-psa-rmm-final-mobile.png`,
`/private/tmp/alignr-docs-datto-endpoints-final-desktop.png` and
`/private/tmp/alignr-docs-datto-endpoints-final-mobile.png`. This is a local
render only; hosted readback and app test execution are not claimed.

## 2026-10-01 — PR16 reconciliation with docs main

Merged docs `origin/main` at `2df1c88` into the held billing-settings branch.
The merge retained the PR16 Settings → **Billing** guide and its HTTP 409 setup
recovery versus temporary HTTP 503 guidance; it also retained the PR11/PR13
hosted-readback entry and the incoming PR15 Datto unknown-status guide, coverage
record and review evidence. The billing guide itself was unchanged by the merge.
The only conflict was this append-only review log, resolved by keeping both the
PR16 billing candidate entry and PR15 Datto entry. No provider settings, public
publication or hosted readback were changed or performed.

With Node 22.13.1 and Mintlify CLI 4.2.939, `python3
scripts/check-docs-vault.py` passed (14 indexed notes), `mint broken-links`
reported no broken links, `mint openapi-check api-reference/openapi.json`
passed, and `mint validate` passed. The merge whitespace check also passed.
No responsive preview was repeated because the public billing guide did not
change in this merge; the branch remains held for the matching application
release and independent review.

## 2026-10-01 — Held standard activation paging reference provenance

The generated REST/MCP reference and activation workflow guides in draft docs
PR #17 were generated against application source `86fa7439a5228c0a023babdceca600538ac8981f`
([app PR #44](https://github.com/ledgrhq/ledgr/pull/44)). The final app source
commit retained the same OpenAPI and MCP contract inputs, so the generated
reference files remain aligned; no regeneration was needed after that source
commit. The docs change is [PR #17](https://github.com/ledgrhq/alignr-docs/pull/17)
and remains draft/held pending the app release. Validation run `36839569397`
passed on the docs candidate.

The requested separate local runtime audit of Clients and Integrations is
unverified: a fresh agent-browser session authenticated and loaded Overview,
but navigation stalled before page screenshots or layout measurements could
be captured. No desktop/mobile rendering claim is made for this docs work;
see `/private/tmp/client-integration-runtime-audit-2026-10-01.md` for the
standalone audit record. No customer data or mutations were involved.

## 2026-10-01 — Held Ask risk-answer clarity guidance

Updated `guides/ask-alignr.mdx` to describe the expected structure for risk
questions: state the recorded condition, explain only a cited possible
significance, and give a specific verification step. It says that when no
explanation of the risk is recorded, Ask Alignr should state that and avoid
guessing impact; a control description states an expectation, not an observed
outcome. This aligns with application PR #47 (`83102664798093f9e16ba1b129695d3c30ed1944`),
where the prompt and citation context support this response and preserve exact
claim grounding. Existing Ask guidance already required users to inspect the
client, subject, time and supporting citations; this addition makes the risk
interpretation limit explicit. Wording was revised from “authored risk
rationale” to “explanation of the risk” so the public guidance avoids evaluator
terminology. The corresponding prompt and guide wording are integrated in
application PR #49 (candidate `042454a`), which retains PR #47 as the component
change's provenance; this docs candidate remains held for PR49's release.

No API or MCP tool, permission or generated reference changed. The application
candidate's three focused grounding tests passed before the wording-only
refinement; they were not rerun afterward because Docker access was denied in
the current shell. No live AI/model response was requested or observed.
`check-docs-vault.py`, `mint openapi-check`, `mint a11y`
and `git diff --check` passed. `mint broken-links` reported only the two existing
README links to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public
MDX link failed. The installed Mintlify CLI is 4.2.229 and does not implement
`mint validate`. A local `mint dev --no-open` attempt could not start because
ports 3000 through 3009 were already occupied; no other preview server was
stopped or changed. Desktop/mobile rendering and hosted readback remain pending.
Keep this docs change unpublished until the matching app release is verified.

## 2026-10-01 — Published Users and API Keys table guides

Updated `guides/account-and-team.mdx` and `guides/api-keys.mdx` against the
reachable page source in app candidates `b3eff8eb2382c567ff88827ac6977dd24087d4a7`
(Users) and final API Keys candidate `fc179c3498bd28a08c5ae2cab660113681880c5f`.
The Users
guide names the search fields, status and role filters including **No role**,
sortable table headings, 25-row display pages and the **Sort users** mobile
control. The source fetches all API pages then filters, sorts and slices in the
browser; this guide does not claim server-side query support. The API Keys guide
documents search by name/prefix/owner, status filtering, all six sortable
headings, desktop heading buttons and the **Sort API keys** mobile control. The
existing **Name A–Z** default remains; null owner/date values stay last in either
direction. The final API Keys revision removed the desktop selector; the guide
now identifies headings as desktop controls and the selector as mobile-only.

No OpenAPI or MCP reference changed because neither candidate changes an API
contract. The pages were checked against the two isolated application commits
and existing public-page structure. The matching application PR #51 is live. This remains an unpublished docs
draft pending final docs checks, merge and hosted readback; no live application
interaction is claimed.

`python3 scripts/check-docs-vault.py` passed with 14 indexed notes and
publication boundaries; `git diff --check`, `mint openapi-check
api-reference/openapi.json` and `mint a11y` across 95 MDX files passed under
Node 22.13.1. `mint broken-links` completed and found only the two existing
`README.md` links to excluded `AGENTS.md` and `vault/MOC.md`; neither public guide
link failed. An earlier invocation under Node 16 exited before checking files
with `ReferenceError: Blob is not defined`. Docs review checked the visible labels
and collection behaviour against the two pinned application sources. The final
API Keys app pin uses column-heading buttons on desktop and retains the
**Sort API keys** select only below the desktop breakpoint. Root reports the
app owner's final 9/9 focused tests, red/green proof and static checks, and root's
390px/1440px visual review; those checks were not rerun by docs work. No docs
build, full Mintlify validation, docs responsive preview or hosted readback was
run. Publication remains held for the matching app releases.

### Local preview follow-up for draft PR #20

Started `mint dev --port 3011` with Node 22.13.1 and read both changed guides
through a browser session against `http://localhost:3011`. At 1440×900 and
390×844, `document.documentElement.scrollWidth` matched the viewport width for
both pages (1440 and 390 respectively). The rendered Users controls text block
measured 576×168 at desktop and 308×308 at mobile; the API Keys block measured
576×224 and 308×420. Both paragraphs rendered with the documented labels and
order; no `vault`/review-log links appeared on either page. The browser session
was read-only and closed after inspection; the local preview was stopped with
Ctrl-C. Screenshot capture hung and was stopped, so there are no saved captures
or pixel-level screenshot claims. This preview does not establish hosted
publication or application runtime behavior.

## 2026-10-01 — Held Controls table guidance

Updated `controls/parameters.mdx` for the Controls tab collection controls in
application candidate `cf98db8f1edf7f2b36c854f23cd1a582738dd1fc`; the retained
draft behavior is from Controls implementation commit
`fda1783a66021c0105c08a4b444fa681e11c46b7`. The guide covers full-collection
search, category and On/Off filters, sortable headings and the narrow-screen
selector, page sizes, category grouping, and parameter edit retention while
filtering/paging. It advises users to resolve a failed or pending save before
leaving the standard. Source review confirms search/filter/sort precede paging,
uncategorised controls are last in category view, and the page may split one
category across page boundaries. No REST/MCP contract, permission, generated
reference or control definition changed, so no reference regeneration is
needed. The application candidate is not verified live and this docs change is
held for the matching application release. A separate source-diff review of
`e7c500a0dd57b255be1ad5742710ec3997b3eb1f` confirmed its wrapper/grid changes
are responsive layout only; the search, filter, sort and edit handlers are
unchanged. No application test was run in this docs workstream.

With Node 22.13.1 and Mintlify CLI 4.2.229, `python3
scripts/check-docs-vault.py` passed (14 indexed notes), `mint openapi-check
api-reference/openapi.json`, `mint a11y` (95 MDX files) and `git diff --check`
passed. `mint broken-links` reports the two pre-existing README links to
intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public MDX link
failed. This installed Mintlify CLI does not support `mint validate`. A local
preview attempt could not start because Mint reported no available port in its
3115–3124 range, so desktop/mobile rendering and hosted readback remain
unverified. Keep this docs change unpublished until the matching app release
is verified.

## 2026-10-01 — Remediations collection candidate (held)

Based on held docs PR21 at reconciled head `730321933759c4fd3fbd4b9c13a0f6acff3d6d63`, now targeting main. Read
AGENTS/MOC, decisions, architecture, editorial/workflow and review checklist.
Claimed scope: `guides/remediation.mdx`, curated reference generator/output and
its navigation group, Documentation Coverage and this review log. Compared
the exact composed application source `a9be8793a6e09dc429d8864f4ff289614ee74963`
in `/private/tmp/alignr-remediations-composed` (clean) with the implemented
Remediations page/list router/service. No application code or tests changed.

The guide explains q search fields/literal semantics and length bound, combining
existing filters, all five heading cycles, mobile selector, complete-collection
server paging, missing-date placement, default started-time order and reset.
Result sorting is distinct from verification/simulation; collection controls do
not invoke actions or change rollback eligibility. Existing approval and rollback
guidance is preserved. DOC-R02/03/04/07 source checks completed; browser and
published acceptance remain separate gates.

Regenerated using the application Python environment with PYTHONPATH pointing
to the exact composed source, without lifespan, database or vendor access:
`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/private/tmp/alignr-remediations-composed/api
<application-python> scripts/sync-reference.py`. The generated selection is now
20 read endpoints and 33 unchanged MCP tools. Semantic comparison found no
changed prior endpoint: only GET `/api/v1/remediations` and `/api/v1/approvals` were added. Both generated
schemas have q maxLength200 and their ten sort values. Existing Remediations
Organization aliases and Approvals subject-type filters remain. Permissions
remain remediation.read and approval.read respectively, with tenant scoping.
Mintlify official OpenAPI setup/CLI documentation was consulted for validation.

Validation results are recorded before the candidate commit. Hold publication
until app PR53 is verified live and docs PR21 plus its dependencies are published.

Scope expanded, at the coordinator's request, to the independently reviewed
Approvals list controls batched in the same app PR53. The exact combined source
above is clean; its feature blobs match the reviewed candidates. The guide
explains requester/title/reference/client search, status chips, five heading
cycles, mobile ordering, reset and page changes. Existing named-human decision,
review-context and rollback instructions were not changed.

Local preview used pinned Mint4.2.939 with Node22.13.1 at localhost3245, in an
isolated agent-browser session. Inspected both changed sections at1440x1000 and
390x844: readable text and table, no page-level horizontal overflow (390 document
width equals390 viewport width). Screenshots are local `/private/tmp/fix-history-
docs-1440.png`, `fix-history-docs-390.png`, `approvals-docs-1440.png` and
`approvals-docs-390.png`. These are candidate docs previews, not live app/public
site evidence. The read-fix-history TOC link was exercised.

Final validation of the combined candidate: `check-docs-vault.py` passed
(14 indexed notes); pinned Mint4.2.939 `broken-links` found no broken links,
`openapi-check` passed (with its CLI deprecation notice), `a11y` passed
(94 MDX files) and `validate` passed. `git diff --check` passed. Existing API
paths remain semantically unchanged; only the two reviewed GET operations
and their reachable schemas were added. MCP tools are unchanged. The local
preview and dedicated browser session were stopped.

The draft targets `docs/controls-table-controls` (docs PR21), now based on main.
Docs PR20 is published; PR21 remains draft pending its matching Controls app
release. Keep PR22 draft until app PR53 is live and PR21 is published.

## 2026-10-01 — Global Organization filter and Fix history picker (held)

Updated the separate public-guidance draft stacked on Docs PR22, preserving that
PR's alignment with the app PR53 collection controls. The global header selector
and Remediations picker were checked against composed application commit
`d8f586785c961c621ad381b982bf88dd1700a0ef`; the Monitoring RuleScope picker was
checked against candidate head
`8dfaf3aec4db46b9678146a284b779809f194bf4` in
`/private/tmp/alignr-client-picker-composed`. Its component matches the
independently reviewed `41b26d82f9a7cc2805ba4a85e9198d8e5d391bd9`
byte-for-byte. The global header selector searches Organizations by
name/slug and pages 25 at a time; only selecting a client or **All organizations**
changes the filter. Fix history uses `AsyncSelect` with **Load more** for further
25-row pages, separately from run-history search. Its explicit Organization URL
filter overrides the global filter; clearing it returns to header scope. The
Monitoring scope editor distinguishes **Every organization** from **Selected
clients only**, retains selected IDs while searching or paging, prevents removing
the final selected client, and retains scope when `organization.read` is absent.
Viewing Fix history still requires `remediation.read`.

No API, OpenAPI or MCP contract changed: these pickers use the existing
Organization list/detail endpoints and existing Remediations filters. No browser
preview or hosted readback has been performed; the copy remains held pending the
matching app release and docs CI.

## 2026-10-01 — Docs PR21 publication and PR22 reconciliation

Docs PR21 was approved for publication after the matching application PR52 was
verified live. Exact PR21 head `730321933759c4fd3fbd4b9c13a0f6acff3d6d63`
merged at 16:36:59 UTC as `63b422fc02e744a343442a7d1c18d07ae9689e85`. Main
documentation validation run `36893332012` passed vault validation, broken-link
checks, OpenAPI checks and Mint validation. Hosted readback of
`https://docs.alignr.io/controls/parameters` confirmed the search, category and
state filters, sortable headings, paging, grouping and draft-retention guidance.

PR22 remains an unpublished draft matched to app PR53. Its PR21 dependency is
reconciled with the published main branch; this does not release PR22. No hosted
PR22 content or app PR53 release is claimed.

## 2026-10-01 — Workspace health table guidance (held preparation)

Separate main-based branch from e131b1f, with no Docs23/24 dependency. The routed
component is frontend/src/features/operations/OperationalHealthPage.tsx, imported
by router.tsx for /health. App143b92 and the owner's working clarity refinement
were inspected read-only. The draft describes sources searched by name/type/hint,
clients searched by name, independent state/readiness filters, local full-array
sorting before paging, missing dates last, and unchanged workspace counters.
Clear filters preserves sorting in the refinement; final commit must confirm it.
No publication until final source and independent review are verified.

Preparation checks passed: pinned mint@4.2.939 broken-links and validate under
Node22, check-docs-vault and whitespace validation. No browser preview, final
source-pin comparison or independent content review yet; these remain pending.

Final source pin: `90c9d0ea6a1821ae99f0f02cd1c0f8c2b617ffe4`. Coordinator verified
three feature files byte-identical in composed candidate9a4518c and independently
cleared the guide's claims. Final source comparison confirms column-specific sort
labels and Clear filters preserving ordering. Public API remains unchanged.
Browser preview results follow. Publication is held for the Health app release.

Final preview inspected at 1440×1000 and 390×844 with agent-browser against the
unchanged reviewed guide. The ordering, local paging and preserved-sort guidance
render legibly; mobile document width equals 390px. Screenshots are
`/private/tmp/health-docs-desktop.png` and `/private/tmp/health-docs-mobile.png`.
Pinned Mintlify accessibility, vault and whitespace checks passed. Earlier
links/build checks apply to the unchanged public MDX; only this internal evidence
was added afterwards. Dedicated browser and preview were stopped. No hosted
publication or production Health acceptance is claimed.

## 2026-10-01 — Activity collection and export safety (held)

Prepared from docs main `63b422fc02e744a343442a7d1c18d07ae9689e85`, independently
of held Docs22/23. The prior uncommitted export-scope draft was preserved in its
original checkout. Claims were checked against committed application source
`18fada94c706c3b6cc2c547c3606b423238ccc9f`; the application working tree had unrelated
Docker/compose/vault changes, which were excluded by reading committed blobs.
No new API reference group or MCP claim is introduced. Public guide changes cover
search/filter/order/paging, client scope parity and the CSV apostrophe boundary.
The 50,000-row limit is described honestly while its removal remains outstanding.
Publication and hosted acceptance are held pending the matching app release.
Validation and preview results follow before the candidate freeze.

Validation passed using Node 22.13.1 and pinned mint@4.2.939: broken-links,
openapi-check, validate, a11y, check-docs-vault and git diff --check. OpenAPI check
validated the unchanged curated snapshot; no audit operation is selected there.
Desktop 1440×1000 and mobile 390×844 previews were inspected using agent-browser.
Search/order/client-scope guidance, CSV example and cap warning render legibly;
mobile document width equals the 390px viewport. The security guide's existing
export-guide link resolves to the retained Activity section anchor. Screenshots:
`/private/tmp/audit-docs-desktop.png`, `/private/tmp/audit-docs-mobile-export.png`
and `/private/tmp/audit-docs-mobile-security.png`. Preview and dedicated browser
were stopped. No hosted publication, hosted search or production workflow test
is claimed. Independent content review and matching app release remain required.

## 2026-10-01 — Per-control live-score eligibility (held)

Updated the daily review, Workspace health and client report guides against the
alignment scoring refinement in application commit
`4da5d2a5f3c4b03ad102bae11259875bbe67385b` and saved-report consumer follow-up
`5f33b867cf6def951866fbd630697f39ca253bc4`. The copy explains that each
control needs its own current live evidence from a connected selected source,
collected no later than evaluation. Missing, stale, simulated and later-collected
evidence remains unknown; unrelated stale client information remains a warning
without cancelling an otherwise eligible control result. Saved reports remain
historical snapshots. No API, MCP or schema contract changed, so generated
references are unchanged. This draft is held pending the matching application
release; it makes no production availability claim.

The daily-review text distinguishes the UI's **No live checks to score** state
for existing clients from **Not assessed yet** when the workspace has no clients.
Its example uses four eligible checks (two passing and two failing) plus an
unrelated stale asset to show that a 50% score is not an overall health grade.
New automated report snapshots identify the score policy with
`scoring_policy: per_control_v1`. The report guide warns that older unmarked
snapshots may still contain counts from the earlier policy; readers must retain
their recorded label and value, not infer per-control eligibility or
recalculate historical eligibility.

Validation: `check-docs-vault.py`, `mint openapi-check` and `mint a11y` passed;
`git diff --check` passed. The available Mint CLI is 4.2.229 under Node 22, while
the repository pins 4.2.939. Attempting `npx mint@4.2.939` stalled without
output and was stopped. The available CLI does not implement `mint validate`.
Its `mint broken-links` check reports only the existing README links to
maintainer-only `AGENTS.md` and `vault/MOC.md`. Local preview could not start
because ports 3000–3009 were already occupied. No hosted preview or publication
was performed. Before publication, reconcile this draft with the held Workspace
health Docs25 change so its table-controls guidance is preserved.

## 2026-10-01 — Health guide release reconciliation

Merged published documentation main `5335f8a` into the Health guide branch.
The conflicts were append-only internal review and coverage records; both the
Health and Activity records were retained. The reviewed Health MDX is unchanged.
Application PR58 has passed its production repository gate and is deploying;
publication remains held until the matching API and frontend are verified live.
No additional local browser or build was started, respecting the owner's laptop
resource constraint. Structural and whitespace checks were rerun; remote docs
validation must pass this merged head before publication.

## 2026-10-01 — Combined Health and scoring guidance

Reconciled scoring PR26 with Health PR25 at `2db5a6a`, retaining both internal
review records. The public Health page now includes both table controls and the
per-control eligibility explanation. Daily review and saved-report guidance,
including `scoring_policy: per_control_v1` and legacy snapshot preservation, are
unchanged. Both guide updates remain held for application PR58 API and frontend
deployment verification. Vault and whitespace checks passed on the combined tree;
remote documentation validation remains required for this exact head. No new
local build or browser session was started.


## Held workspace shell candidate — 2 October 2026

Source: application PR61, frozen commit `3837e3f7daf50a511923b2c4d08b568ce1dad947`, ADR-0051. Introduction and daily review explain the sidebar, client filter, utility bar and remembered theme choices. Settings, account/team and billing guides distinguish workspace options from personal-account options within the same top-left logo dropdown and retain existing Settings paths. Team and billing links retain their read/manage permission boundaries. The Settings directory's previously omitted Billing row is now documented. No Inbox rename, workspace switching, new billing behaviour or score changes are claimed.

Publication is held until the matching app release is verified. Source review is separate from rendered acceptance; desktop/390px/light/dark/keyboard and changed docs previews remain outstanding. Refresh affected visual-tour screenshots from authorised non-sensitive UI before publication, or explicitly retain them as dated prior-layout examples. No new screenshots were fabricated. Public `docs.json` navigation and reference catalogues are unchanged because pages, API/MCP contracts, predicates and controls did not move or change.

Independent source review by `run_diagnostics` found two label/scope mismatches: Introduction implied the mobile navigation menu included personal Account settings, and daily review retained the old Main navigation label. The trigger label changed to Open navigation; the daily summary now qualifies permission-gated Team members and Billing. A later source check corrected an inaccurate statement in this entry: `WorkspaceMenu` puts Account settings and Sign out in the same top-left logo dropdown as workspace settings, teammates and billing; there is no separate top-right account menu in this candidate. Structural vault and whitespace checks pass. Remote validation and rendered acceptance remain pending.

Final source review against application merge `2c80354b33d714d420f6d6365ff7d7c0d213b8d8` caught a remaining reference to the old header Organization filter in the Audit trail section. Replaced it with the workspace Client filter and retained explicit URL precedence, share-link behaviour and reset semantics, verified against `LogsPage.tsx` and its scope tests. This is a location/copy correction only; no API or catalogue regeneration applies. Matching app promotion and hosted documentation verification remain pending.

Independent follow-up review found a second old header-filter instruction in the same guide. Root searched the public guides for sibling references and corrected daily review, issue triage and remediation to use the workspace client filter; daily review also now places help in the desktop sidebar/mobile navigation, matching the released-candidate shell. Existing client/URL precedence is unchanged. No reference regeneration is needed for these navigation-copy corrections.

## 2026-10-01 — Aggregate fact capacity guidance (held)

Prepared against application PR59 (`2abd6fb`, with a test-only review follow-up
pending) on top of Health PR25 and scoring PR26. REST and MCP evaluation guides
explain the removed 5,000-current-fact snapshot rejection and partial outcomes
without equating zero failed rules with completion. Workspace health explains the
removed aggregate scheduled evidence ceiling while retaining per-rule/provider
limitations. The implementation preserves source eligibility, receipt encoding,
API schemas, predicates and control definitions; generated references are unchanged.

The candidate must remain unpublished until PR59 is verified live. Structural vault
and whitespace checks pass; remote validation and independent content review are
pending. No local browser or build was started because of the owner's laptop
resource constraint. Earlier guide screenshots do not establish visual acceptance
of the added paragraphs.

Reconciled published capacity docs main `4fd460c` into this candidate before publication. The only conflict was appended review-log history; both records are retained. Navigation MDX stayed unchanged. The previous conflict prevented GitHub pull-request validation from starting on recent heads; exact merged-head validation is now required.


## Held Linear workspace navigation and setup guides — 2 October 2026

Updated `introduction.mdx`, `guides/daily-review.mdx`, `guides/settings.mdx`,
`guides/account-and-team.mdx`, `guides/billing-and-support.mdx`,
`guides/setup-wizard.mdx`, `guides/organizations.mdx`, `guides/configure-client.mdx`,
`guides/integrations.mdx`, `guides/standards.mdx` and `guides/triage-issues.mdx`
against the application redesign candidate in
`/private/tmp/alignr-linear-ui-rebuild`, including Standards setup and questionnaire
source in `frontend/src/features/workspace-standards/`, connection list/setup/detail
in `frontend/src/features/workspace-integrations/`, navigation in
`frontend/src/features/workspace/WorkspaceShell.tsx`, and Issues in
`frontend/src/features/workspace-issues/`. The checked source was candidate HEAD
`719c9bd7d1cbf8e68e677b258ed3c5f4f65bf399`; relevant feature commits are shell
`b1a0e0d6e6306c8e203fc4c4379c5861b0486465`, Standards and integration setup
`b40b7ed9701edd2edb53aee51289607c3bc1aeed`, Clients list `487e1fa647b7bf1bcc1d948d01b79ba71bb72433`, Issues view
`2fff1e6b0705ca750d47ce6f98f3a0b0d0ea43ab` and filter/status correction
`b36ebd8edc2ea14c7de1ea0b262e8cdf7f444d1c`. The app branch was clean at that
pin, but release validation is still pending.

The copy uses the four explicit issue statuses (Open, Snoozed, Resolved, Dismissed),
not an All-status choice; it describes search/filter/display controls and retains the
PR29 functional clarifications around URL state, filter chips, client scoping and
email-domain versus technical-category semantics. The Clients guide reflects the current search/filter/page controls and headings.
The copy preserves current routes, permission language, and the separate
questionnaire save, assignment and assessment steps. No API/MCP contract or generated reference changed.
A follow-up source review corrected the earlier mistaken description of a top-right account menu: `WorkspaceMenu` places workspace links and Account settings/Sign out in one top-left logo dropdown. The Standards detail link rebuilds the list URL with `q`, `state`, `page` and `pageSize`; the guide now names **← Standards** and no longer repeats the compact-list summary.

This is source review only: docs CI, Mintlify validation, rendered preview, hosted
readback, application tests and authenticated browser journey were not run. The
matching app release is pending; do not publish until its exact final source and
release are verified.

### Global client selector removal — documentation correction

The app owner removed the global workspace client selector after the source pin
used by this held draft. Updated `introduction.mdx`, `guides/daily-review.mdx`,
`guides/triage-issues.mdx`, `guides/ask-alignr.mdx` and `guides/remediation.mdx` to
remove claims that a shared selection scopes other pages. The current copy states
that client scope comes from the route or a page's own controls and that a client
link's URL carries its own scope. Activity export instructions remain page-URL
scoped. Historical review entries describing the earlier selector are preserved;
the latest Documentation Coverage entry marks that source pin superseded.

This correction is source-copy only. It does not assert final app release parity;
the exact final source pin, docs checks, rendered preview and hosted readback are
still pending. Do not publish until those checks are complete.

### 2 October — inline setup and method selection reconciliation

Updated setup, integration, guided-standard and quickstart instructions against
application candidate `1948d88` and `aa834fc`, retaining the held release status.
Microsoft setup now explicitly chooses Direct or Partner Center; provider cards
and Add connection use one inline dialog, preserving the current stage/draft and
allowing another connection. Corrected the stale Setup checklist label. No API,
predicate, baseline or evaluator behavior changed in this presentation pass, so
no reference regeneration is needed.

The owner explicitly authorised all required publishing/deployment work. This
resolves the earlier docs-push approval question. Source/structural checks are
separate from the pending remote Mintlify checks and final hosted readback.

### Setup labels and OAuth return path — source review correction

Independent review compared the setup and integration guides with the current
workspace UI and Microsoft callback route. The inline connection dialog labels its
repeat action **Add another connection**, not **Add another**; corrected the setup
wizard and guided-standard instructions to match. Setup-origin Microsoft OAuth
returns directly to `/setup?step=microsoft&oauth=...`; it does not display a
**Return to setup** link. Updated the Microsoft paragraph in the integrations guide
to describe the direct return while retaining **Return to standard setup** for
guided-standard connection flows. Assignment remains separate from **Run checks**.

Evidence: `WorkspaceSetupMicrosoftConnection.tsx` sends `returnContext: "setup"`,
`api/v1/microsoft_connections.py` redirects to the wizard route, and
`WorkspaceConnectionSetupPage.tsx` labels the inline action **Add another
connection**. This is source review only; no docs build, rendered preview,
application test, or hosted readback was run. Publication remains held for the
matching app release and required documentation validation.


### 2 October — final UI source and release validation

Reconciled this guide update with application candidate
`35f0a138b215c0897b793e1945c5dfe264d3c4f5`, now merged by application PR65 as
`00d3962a29f9f39cbac557c74af211a39abfb275`. The merge and candidate have the same
source tree. Later application fixes concern responsive layout, accessible field
labels, report headers and test cleanup; they do not change the documented setup
actions or separate activation, assignment and evaluation milestones.

Application CI 36981959892 passed (5,045 backend and 3,664 frontend tests). The
clean-stack `make check` step in 36981987817 also passed; its synthetic browser
proof passed 344 checks. Focused jobs in 36985648886 passed external-portal and
short-screen coverage plus real disposable-API creation and persisted client
assignment for Identity, Backup and Device standards. These checks do not prove
third-party authorisation against customer credentials.

Documentation candidate `691e39535593e4dd2c9b74a1465d61ea135ba415` passed remote
validation run 36977198604 and Mintlify preview deployment. This appended evidence
record changes no public prose. Publication remains held for production frontend
promotion after application API release run 36986239142; hosted documentation
readback follows publication. No API, MCP or predicate reference regeneration is
needed for this UI-only change.

### Visual-tour screenshot review — 2 October 2026

Compared the embedded client-checks, Ask Alignr and client-reports screenshots with
the merged workspace navigation. Each shows the former horizontal app header. The
proof-run captures use synthetic fixtures, so they are not suitable as public
product screenshots under the screenshot policy. Retained the existing demo images
with explicit earlier-layout captions and current entry-point directions rather
than presenting them as current shell captures. Setup-wizard captures remain in
their dedicated setup flow. Source: application PR65 merge `00d3962`; no application
source changes. This is a documentation source review only; Mintlify build, hosted
preview and production readback remain outstanding for these caption changes.


## Setup refinement follow-up — 2 October 2026 (candidate)

Reviewed against application branch `fix/setup-ui-refinement` based on production `00d3962a29f9f39cbac557c74af211a39abfb275`; application candidate `7b13efc538d2564ad9d6889b131043036dbc3f38` (PR66). Updated setup action labels, shared catalogue entry, staff-directory dialog entry and Standards Sources guidance. DOC-R02/03/04/07 source comparison performed. No API, MCP, predicate or baseline changes, so no reference regeneration required. Remote validation and publication are pending. No new screenshots or live vendor claims are included.

Independent source review confirmed the setup action labels and corrected the distinction between requirement observations and source-gap suggestions. Publication remains held for the application release and remote documentation checks.

### Issue properties and source-reference follow-up

Updated the triage guide for Properties before Evidence and the Source record dialog. Source review also found and removed one remaining global-client-scope claim and reconciled Snooze, Dismiss, reason and audit-history labels with WorkspaceIssueDetail/WorkspaceIssueTriageDialog. No status transition or evidence semantics changed. Final application source and publication evidence are pending.


## 2026-10-02 — import and connection-readiness follow-up

Updated Organizations and Integrations guides for the compact Source row, Refresh records, Record status filter, linked/review counts and Create unmatched confirmation. The integrations guide also explains that setup displays **Setting up your tenant** while connection-key protection is prepared and opens connection choices automatically when the matching tenant is ready; retry remains available when setup needs attention. Verified labels and the tenant-matched readiness gate against application candidate `1256007777cb70dfef53a220622d417b5b36dbf8` in `fix/setup-ui-refinement`. This does not claim production readiness or change API, mapping or evidence semantics. Publication remains paired with app PR66.

## 2026-10-02 — connector recovery and collection diagnostics (held)

Updated maintain-integrations, client-microsoft-connections, microsoft-setup,
workspace-health and settings against application d1eb6c0d (scoped automatic
partner consent), e6d98451 (accepted optional grants), c0565267 (collection
history), and d26d2a64 (client Direct setup and navigation). Reviewed the actual
client preparation endpoint and corrected a source-review discovery: the general
catalogue excludes Microsoft in a client context, so Direct now uses its dedicated
dialog. No public screenshots or customer operational data added.

The curated OpenAPI/MCP generator does not include the internal sync-history or
Microsoft capability routes. No exposed curated contract, predicate or control
changed, so reference regeneration is not required. This does not claim that
these candidates are live. Publication remains held for corresponding application
release verification. Vault checks and remote documentation validation follow.

### 2 October 2026 — unanswered refresh recovery

- Application PR 76 adds one automatic reconciliation of the original request on returning to Overview.
- Updated `guides/maintain-integrations.mdx`; retain draft publication until the application release.
- No generated API or predicate references changed.

### 2 October 2026 — delegated mailbox boundary

Application candidate `6e32d8346e63a90121e30ab45a12811dcda78dc0` excludes tenant-wide mailbox reads from Partner Center. Updated Microsoft guides and the three predicate interpretation notes; regenerated predicate reference from that checkout. Publication remains held for application release.

### 2 October 2026 — progressive issue publication candidate

Updates `guides/triage-issues.mdx` and `guides/standards.mdx` against application
PR79 source `3b933424bf82c0f2e581acbe4006db5ae9b3b4bc`. Rule-based standard batches
commit one verified candidate per chunk; visible Issues list polling is five
seconds. Explicitly retain complete-collection and generated-rule boundaries.
No new UI controls, diagrams, API schema, predicates or MCP scopes; no generated
references require changes. Publication is held until the matching app candidate
passes remote tests and ships. Validation is pending; no production claim.


### 3 October 2026 — verification policy context

`guides/standards.mdx` now explains effective client thresholds and the distinction
between a failed control and a verified issue, with a 30-/90-day worked example.
Source: application d002b35f, control-engine resolved-policy handoff and uncached
UTC verifier clock. No predicate, control-definition, API or MCP changes, so the
generated references remain unchanged. Remote app regression37082512776 passed;
public validation follows. Keep publication held until application PR79 ships.
### 3 October 2026 — scoped refresh and compact assessment UI (held)

Checked application PR80 source: selected standards intersect active assigned clients; changed policy targets are blocked individually; bulk assignment is search-scoped and preserves hidden selections until explicit save; Evidence uses a row-end View JSON value menu. Updated three guides and their living coverage records. No customer information added and no generated contracts changed. App PR78 has shipped, but this additional docs revision remains held for PR80 release. Vault checks and remote validation follow; rendering not yet reviewed for this revision.


### 3 October 2026 — paired product release verified

Application PR79 (including PR80) is deployed at eebdbce1, with the coordinated
staff build promoted. One Microsoft-cited issue was independently confirmed in
production and by the owner. PR32 published as658643b; this branch reconciles its
final compact-UI guide changes with progressive findings. Both append-only vault
records are retained. Public remote validation and hosted readback remain gates.

### 3 October — readable issue explanations (held for application PR82)

Triage guide follows application3465ff2698f53d85432299970ea25c20344c5c37: recorded
account state/date, historical inactivity limit only when known, registration vs
enforcement and observation dates. No API/predicate/control definition contract
change; generated references need no regeneration. No customer data or screenshot
is published. Existing prose layout/components unchanged. App focused regression
and1440/390px render proofs passed; full gate/publication still pending.


### 3 October 2026 — scoped Standard Run checks (candidate; held)

Drafted [Standards and controls](../guides/standards.mdx), the new [scoped Standard Run checks REST recipe](../api-reference/run-scoped-standard-checks.mdx), and cross-links from the assignment, refresh and API introduction pages against app candidate `744b659e` in `/private/tmp/alignr-standard-runs`. Source review checked the request schema, route permissions, durable request handling, progress response and modal selection behaviour. The docs describe one standard and 1–200 selected applicable active clients, collection before assessment, exact key/body recovery, and no assignment changes. This is source-aligned candidate copy, not production acceptance.

The docs worktree is a clean branch from locally available `origin/main` at `00ed898`; fetching a newer remote head failed because the environment could not resolve `github.com`. No generated reference changed: the curated OpenAPI selection does not include write operations, and the new request is documented as a recipe rather than added to its read-only snapshot. No Mintlify checks, hosted preview, publication or hosted readback have run. Reconcile against the matching app release, refresh the docs base if needed, then complete vault/link/Mintlify and independent review gates before publication.

### 3 October 2026 — scoped Standard Run review correction (held)

Reviewed the docs against app source `fc426173e6d25e0c8e05ba3f6f96d0e193d2dff1` in `/private/tmp/alignr-standard-runs`; test-only fixes remain pending. Corrected the scope description: selected-client evidence alone is published and assessed, while some connected sources may read a broader provider inventory. Clarified that signed-in human authentication is supported alongside a user-owned API key. The curated OpenAPI generator selects GET routes only and excludes `POST /sweeps`; the request is explained in the manual recipe, so generated references/catalogues do not need regeneration. Not live; matching app release, full docs checks, preview and publication remain pending.

### 4 October 2026 — scoped-run authentication correction (held)

Independent review against application PR93 a26a2ebc found the prior API-key claim
incorrect: POST /sweeps depends on get_current_user, which requires a human access
JWT. The recipe and examples now match that route. No API permission is broadened.
This supersedes the API-key sentence in the earlier review record. Prior docs head
13cf99b passed remote validation; the correction requires its own remote check.
Publication stays held until the composed scoped-checks application release.

## 3 October 2026 — Overview receipt and client UI polish (held)

Updated `guides/daily-review.mdx`, `guides/configure-client.mdx`,
`guides/domain-checks.mdx`, `guides/client-microsoft-connections.mdx` and
`guides/risk-and-roadmap.mdx` against app source
`35626ea9242e2ea734a43ed818f85b316fff1213` and
`cf202d42f38889a241177943c526e4ee556d0334`. Source review verified that the
Overview Retry status callback refetches the saved sweep receipt and does not
call the collection-start mutation; uncertain acceptance uses the existing
request reconciliation path. Client copy now follows the discovered/manual
domain groups, explicit client sites/access action, separate risk/manual
filter menus and conditional roadmap save state. No successful-activity
semantics, Exchange claims or new scoped-run modal are included.

No API, MCP, permission, predicate or control-definition contract changed; no
generated references were required. The vault structural check passed (14
indexed notes and publication boundaries), and `git diff --check` passed.
Review covers source and prose only, not a Mintlify build, rendered
desktop/mobile preview, app/browser acceptance or hosted readback. Publication
stays held for matching application release and independent docs review.

### 3 October 2026 — Independent client UI copy review

Compared the held client UI guides with active application sources at
`35626ea9242e2ea734a43ed818f85b316fff1213` and
`cf202d42f38889a241177943c526e4ee556d0334`. Corrected one remaining
`Domains from Microsoft` label, distinguished the Microsoft **Client sites and
access** action from other sources' **Client site access** action, and replaced
the obsolete client-tab **Microsoft setup** navigation with current add/link
actions. Clarified that **Sites and Microsoft access** is the dialog title and
**Check access** is its action.

Source review confirms Overview **Retry status** refetches the saved sweep ID;
**Check refresh** reconciles the same retained request. Domain save/check
conditions, separate risk/manual filters, and valid-pending/invalid-disabled
roadmap behaviour match source. Vault structural check and `git diff --check`
passed. This was a source/prose review only: no Mintlify build, rendered or
browser acceptance, app deployment, hosted readback or publication was done.
Publication remains held for the matching application release and review.


### UI guide candidate final source binding — 2026-10-03

Root accepted the independent label/path corrections. Current reviewed app UI
candidate is `a0d99aa5ea9127cc276527121c57a84f8986f7e5` (PR86), which includes
the PR84 orb/status release `ae8a2b4f382bc8053e559e00a9e2ccddd16227d9`.
This update changes prose only; no schema/predicate/control/MCP catalogue changed.
Draft PR validation must run remotely. Publication remains held until matching
app release; hosted readback and rendered guide review remain unverified.


### 4 October — composed scoped-run documentation validation

Reconciled this candidate with published main ae2e763, retaining both independent
append-only review histories. The previously conflicting base prevented GitHub's
pull-request validation workflow from running on f0bb28f, although Mintlify passed.
The resolved branch requires fresh remote validation and rendered desktop/mobile
acceptance. Application PR93 is merged as3fe5a298 and deployment37225095097 is
running. These public changes remain held until the matching staff release is live.


### 7 October — held issue-guide PR29 reconciliation

ALI-46 coordinator: Codex root. Documentation main `e0864d0` and application
release candidate `a494c772fb02cbc590b8f3b259eba04f57b7a4b8` were inspected in
clean isolated checkouts. PR29 `d9f1763` describes an older Issues toolbar. All
four changed paragraphs were compared with main and the current
`WorkspaceIssueFilters` / `WorkspaceIssuesPage` / toolbar source.

- Removable chips, Clear filters and email-domain compatibility are already in
  the published-main guide. The current fields are Category and Email domain.
- Search, sort, filter and pagination URL state, reset to page one, and 25/50/100
  row choices are already documented.
- The old More filters inline expansion and Finding-heading sorting do not
  describe the current single filter popover and Display options control.
- The old global-client-selector advice is superseded by the current workspace
  shell; the guide explains page URL and Client filtering.

The useful changes are accounted for in main (notably the rebuilt workspace
revision `ea5fc5a`); merging PR29 would restore obsolete instructions. It should
be closed as superseded, not merged. No public page or navigation is changed by
this reconciliation. Source/prose inspection passes DOC-R02 for this narrow
comparison; it is not a new rendered or authenticated production acceptance.

Docs PR37–41 remain held for fresh activity/Guest/reassessment and runtime
acceptance. Grouped conditions and draft preview are being implemented in the
application and are not publicly documented as available. Their eventual docs
need the custom-control, condition, advanced-definition and rollout guides plus
the curated API reference and actual create/edit/preview worked examples.

## 7 October — compact workspace Overview API reference (held)

Updated the curated API reference and added `api-reference/workspace-overview.mdx`
against application PR #165 head `5abbff250fef594092dca600e25865e89e2e330f`
([PR #165](https://github.com/ledgrhq/ledgr/pull/165)), based on the reviewed
prod source at `3f3ed0265129d8ec54f3d9672c512ff0bc6d14c4`. Source inspection
covered `dashboard.py`, `workspace_home.py`, `dashboard_service.py`, the mounted
`WorkspaceOverviewPage`, `useWorkspaceHome` and tenant-isolation tests. The
contract requires `dashboard.read`, accepts optional `organizationId` and the
legacy `organization_id` (camelCase wins), returns only `needsAttention`,
`integrationHealth` and `discovery`, and uses 404 rather than widening an invalid
or foreign Organization filter. Selected-client discovery fields narrow; the
six-row connection preview, connection totals, unmapped remote-company count
and terminal-sweep history remain tenant-wide. Discovery observation counts use active, non-superseded, unretracted facts; they do not assert freshness, collection completeness or a passing control. Alignment/coverage statistics
are a separate read and are not added to this response. `/dashboard/overview`
remains a separate broad compatibility contract.

The generator now selects the read-only `GET /api/v1/dashboard/workspace-home`
operation in the Dashboard group. Regeneration from the exact PR #165 application
checkout produced 21 selected GET operations and left the 33-tool MCP catalogue
unchanged. The operation includes the `WorkspaceHomeRead` schema, both query
spellings, `dashboard.read`, and 403/404 explanations. It states that generated
source does not establish deployment availability.

The docs vault guard passed (14 indexed notes and publication boundaries),
`mint openapi-check` passed, `mint a11y` passed for 97 MDX pages and
`git diff --check` passed. `mint broken-links` reports only the two existing
README links to intentionally excluded `AGENTS.md` and `vault/MOC.md`; no public
MDX link failed. The installed Mintlify CLI is 4.2.229 on Node 22.13.1; it does
not provide `mint validate`. Local `mint dev` reported the preview ready, then
logged a `transformAlgorithm` TypeError; the new prose page and generated
operation nevertheless rendered. Desktop and 390px mobile previews showed the
page, navigation and response table without visible overflow. No authenticated
API call, production runtime check, hosted docs readback or publication was
performed. Application PR #165 remains open; keep this docs change held until
matching application review/release and fresh docs review.


### 8 October 2026 — Microsoft account Guest population explanation (candidate)

Updated `controls/baselines/identity.mdx` and `controls/advanced-definitions.mdx`
to explain the source-backed default Member population, selected-source current
`user_type` requirement, Guest opt-in and unknown handling. Member service and
non-mailbox accounts remain eligible. No address heuristic is specified. The app
candidate is isolated at `/private/tmp/alignr-ali15-guest-exclusion-20261008`; its
relationship to production issue CD-4846 remains unverified, and historical issue
reconciliation requires a fresh Microsoft collection/identity witness. No predicate,
control definition or generated catalogue changed. The docs worktree is an isolated
branch from `origin/main`; source edits are a candidate only. Mintlify validation,
rendered preview, independent review, merge, publication and hosted readback remain
unverified.


## 9 October — PR #50 guest-population preview review

Reviewed the hosted PR #50 preview at source head
`c2c23ac4a8d2c206ba01897ee82805d02d0b46d3`:
`https://alignr-docs-ali15-guest-population-20261008.mintlify.site/`. The changed
pages, `controls/baselines/identity` and `controls/advanced-definitions`, rendered
in light and dark themes at desktop and 390 × 844 mobile dimensions. At 390 CSS
pixels, both the document and body measured 390 pixels wide; neither page had
horizontal document overflow. The guest-scope copy was readable in both themes.
The advanced-definition code example remains horizontally scrollable within its
own block on mobile.

No visual defect was found. Mintlify's fixed Ask Assistant composer occupies the
bottom of the mobile viewport while scrolling; both changed paragraphs remained
readable after scrolling. This is rendered preview evidence only. It does not
verify the application behavior described by the copy, production deployment,
keyboard or screen-reader behavior, or the live docs URL. Review screenshots were
kept outside the repository under `/tmp/pr50-review/`. The docs vault guard passed
(14 indexed notes); with Mintlify 4.2.939 on Node 22.13.1, `mint broken-links`,
`mint openapi-check api-reference/openapi.json`, `mint a11y` (96 MDX files),
`mint validate` and `git diff --check` passed. The OpenAPI command reports that it
is deprecated in favour of `mint validate`, but the definition was valid. GitHub
Documentation checks and Mintlify Deployment were green on the original PR head
when this review began; the review-log-only change does not alter public MDX or
generated references. Its updated CI result is available from PR #50.
