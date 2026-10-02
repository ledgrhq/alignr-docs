# Application documentation coverage

Fact-volume capacity candidate: REST and MCP one-client evaluation guides explain
streamed current-fact snapshots and truthful partial outcomes; Workspace health
distinguishes the removed aggregate scheduled-evidence ceiling from remaining
per-rule and provider constraints. Held for the matching capacity release, after
Health PR25 and scoring PR26. No route, schema, predicate or control definition
changed, so generated references remain unchanged.

Living coverage map. Last audited 2026-09-26 against application `565fae53f166e14dae4f3d872572ab3e3bdfdc28` and published documentation `0bf7785de4d97ac9f8a759bb9626d837fa4feeca`. The audit used three independent subagents plus the coordinator, followed by a separate review of the immediate corrections.

## What this review proves

Source inspection reconciled all 46 staff route declarations (including index/fallback), the separate portal SPA and route-linked dialogs, rails and connector catalogue with committed public docs. Backend services were inspected where necessary to establish the workflow. It identifies documentation coverage and source-backed gaps. It is not an authenticated whole-app walkthrough, production availability certification, security audit or full application test run.

Concurrent quickstart, integrations and MCP connection drafts were excluded from the published baseline and preserved. App code was unchanged during the inspected target; concurrent infrastructure/delivery work is outside this audit. New docs must still verify exact permissions, edge cases and live provider instructions before publication.

The subsequent signup and developer-entry update reviews those three drafts against application `b844f92` and adds the token navigation correction. It covers the welcome message's setup link, automatic connection-key preparation, own-directory staff preview and manual invitation, and bearer-key MCP client setup. The dated baseline audit above remains historical; these source-backed additions do not certify production email delivery, Microsoft consent, or a live MCP session.

## Evidence

- [Daily operations audit](Review%20Evidence/Daily%20Operations%20Audit.md): Overview, Issues, approvals, fixes, Ask, search, Activity and audit.
- [Setup and integrations audit](Review%20Evidence/Setup%20and%20Integrations%20Audit.md): authentication, workspace setup, client connections/domains, settings and connector inventory.
- [Assessments and sharing audit](Review%20Evidence/Assessments%20and%20Sharing%20Audit.md): standards/intake/import, manual review work, risk, roadmap, reports, staff/external portal.
- [API and MCP audit](Review%20Evidence/API%20and%20MCP%20Audit.md): tokens, developer console, generated references and retained backend boundaries.

## Delivered coverage — 2026-09-26

All thirteen audited documentation gaps now have source-backed guides. This closes the writing backlog, not production acceptance of every workflow. See [implementation review](Review%20Evidence/Implementation%20Review.md) for verification and remaining product limitations.

| Task | Delivered guide |
| --- | --- |
| Issue triage and remediation | [guides/triage-issues](../guides/triage-issues.mdx); [guides/remediation](../guides/remediation.mdx) |
| Client reviews | [guides/client-reviews](../guides/client-reviews.mdx) |
| Risk and roadmap | [guides/risk-and-roadmap](../guides/risk-and-roadmap.mdx) |
| Reports and portal | [guides/client-reports](../guides/client-reports.mdx); [guides/client-portal](../guides/client-portal.mdx) |
| Catalogue and vendor setup | [guides/integration-catalogue](../guides/integration-catalogue.mdx) |
| Integration maintenance and modes | [guides/maintain-integrations](../guides/maintain-integrations.mdx) |
| Ask Alignr | [guides/ask-alignr](../guides/ask-alignr.mdx) |
| Sign-in recovery | [guides/sign-in-recovery](../guides/sign-in-recovery.mdx) |
| Build/import standards | [guides/build-or-import-standard](../guides/build-or-import-standard.mdx) |
| Daily review | [guides/daily-review](../guides/daily-review.mdx) |
| Domain operations | [guides/domain-checks](../guides/domain-checks.mdx) |
| Standalone rules | [controls/standalone-rules](../controls/standalone-rules.mdx) |
| API/MCP assessment recipe | [api-reference/client-assessment-recipe](../api-reference/client-assessment-recipe.mdx) |

## Immediate corrections completed in this audit

- Token navigation changed to **Settings → MCP/API Tokens → + Generate token**; corrected own-key permissions, service-key requirements, UTC expiry and revoke workflow.
- Added developer explorer instructions explaining current execution identity and live read/write behaviour.
- Corrected the claim that the authenticated schema is the full mounted API: it filters retired reference roots.
- Generated MCP catalogue now states that retained tools may require scopes not offered by the current token form. The server tools are not described as removed.
- Generator only gives optional/workspace-wide Organization advice for actually optional arguments.
- Added the control-versus-standalone-rule semantic distinction to advanced definitions; an editor tutorial remains conditional on intended discoverability.
- Extended the vault guard to nested evidence notes and verified it rejects an unindexed nested note.
- Narrowed “all 19 supplied manual checks” to the 19 in standard-library templates; guided intake supplies additional configurable manual areas.

## Route reconciliation

The historical audit notes retain the complete route inventory. Recovery now covers authentication; build/import covers standards intake; domain operations and client reviews cover client tabs and `/assessments/work`; reports/portal cover sharing; risk/roadmap covers decisions and delivery; daily review, triage, remediation and Ask cover operational routes and shell actions. The catalogue and maintenance guides cover all 38 implemented connector types and distinguish eight unavailable entries. The API recipe completes the developer task gap.

The 2026-09-30 client overview candidate is covered by [Your daily review](../guides/daily-review.mdx) and [Run a client review](../guides/client-reviews.mdx): current versus last-loaded assessment, recorded-result counts, permission-dependent open issues, expandable next steps and run details, focus refresh with retained cached results on failure, and updated standard coverage after recording a manual outcome. These claims were checked against the isolated application candidate and remain held for its release; no generated API/MCP references change.

The 2026-10-01 first-day clarity update extends [Your daily review](../guides/daily-review.mdx) with the evidence-eligible pass count and active-check coverage denominator, one-client **Run all checks** semantics, and the renamed **Audit trail** page title. [Organizations and clients](../guides/organizations.mdx) now explains client-table heading sort cycles and order of search/filter → sort → pagination. The standards guides use the current **Create standard** entry label. These are app UI changes; no public API/MCP contract or generated reference changed. The docs candidate remains held for the matching app release.

The 2026-10-01 Ask risk-context candidate updates [Use the AI assistant](../guides/ask-alignr.mdx) to explain the expected risk answer shape: recorded condition, cited possible significance and a verification step, including an explicit missing-explanation statement without guessed impact. The component change originated in app [PR #47](https://github.com/ledgrhq/ledgr/pull/47), commit `83102664798093f9e16ba1b129695d3c30ed1944`; its plain-language refinement is now included in integrated app [PR #49](https://github.com/ledgrhq/ledgr/pull/49), candidate commit `042454a`. It changes no API/MCP contract or generated reference and remains held until PR49's application release is verified.

The held per-control scoring clarification updates [Your daily review](../guides/daily-review.mdx), [Workspace health](../guides/workspace-health.mdx) and [Prepare a client report](../guides/client-reports.mdx) against the alignment scoring refinement in app commit `4da5d2a5f3c4b03ad102bae11259875bbe67385b` and the saved-report consumer follow-up `5f33b867cf6def951866fbd630697f39ca253bc4`. The guides explain that each control's result depends on its own current live required evidence from selected connected sources, while unrelated stale client evidence remains a warning without erasing an otherwise eligible result. Missing, stale, simulated and later-collected evidence stays unknown; historical reports remain snapshots. New automated report snapshots carry `scoring_policy: per_control_v1`; unmarked older snapshots may still contain counts but do not establish per-control eligibility. This adds no route or generated OpenAPI/MCP schema, so reference generation is unchanged. Hold this copy until the matching application release is verified; these source commits are not a production-availability claim.

Standalone `/monitoring` remains directly routed but absent from the main shell. Its advanced guide states that boundary explicitly. Portal contact access currently needs administrator/support setup because the current People & views screen lacks the required editor; do not invent a self-service screen.

## Deliberately excluded from new public promises

Unrouted legacy Ask/Overview/client editing screens; standalone agents or notification inboxes that do not exist; historical asset/document/migration UI retired by ADR-0023; arbitrary portal file sharing; automatic proposal execution; scheduled emailed reports without evidence; future integration delivery dates. Retained backend operations are accounted for but do not justify resurrecting retired product positioning. Operator AWS/ClickHouse work remains in internal operational runbooks and is not certified by this review.

## Keep this map current

The held one-client evaluation candidate is covered by [REST evaluation](../api-reference/evaluate-one-client.mdx), [MCP evaluation](../mcp/evaluate-one-client.mdx), authentication, standards and developer introductions, plus two curated GETs and three generated tools against application `d65fc8a`. The request write is explained in the guide and authenticated live schema, not silently added to the selected read-only snapshot. This work remains unpublished and unverified against a deployed evaluation worker; no current production availability is claimed.


The setup and developer guides now have a draft update for the five-step wizard, separate Direct/Partner Microsoft registrations, token bulk-selection behaviour and Developer Console entry. The tour uses new five-step local captures and removes the video and old four-step setup images. The other client, assistant and report captures remain from the same day's local demo and need final UI comparison before publication. Publication and hosted-page verification remain pending the matching application release.

A further draft against application `366ecc5` documents user-owned API-key client create/update/archive in `api-reference/manage-clients-recipe.mdx` and corrects authentication boundaries. The subsequent MCP draft against application `f047d6f` and `c98663e` adds `mcp/manage-clients.mdx` for list/create/update, revises the MCP introduction, connection, security and token guides, and regenerates the catalogue at 13 tools. The curated OpenAPI snapshot remains an explicit ten-read-operation subset. This draft must not be published before the matching API release is verified.

The isolated remediation-read candidate against application commits `b095c17`, `6cd6b9a` and `cb429a7` adds two status-only MCP tools to the generated catalogue, taking that **candidate** snapshot to 15 tools. The key picker offers `remediation:read` only in the candidate application branch. Public copy explains tenant-bound paging, current owner permission, verification and simulation, and the absence of rollback readiness or execution powers. The ten-read REST OpenAPI subset is unchanged. This separate docs branch must not replace the 13-tool release documentation before the matching API implementation and deployment are reviewed and verified.

The optional USD billing-estimate documentation candidate uses app revision `96d4b05` (`1f7a17f` implementation and `96d4b05` no-cache error fix). It expands the curated API snapshot to eleven read operations while preserving 15 MCP tools. `guides/billing-and-support.mdx` and `api-reference/billing-estimate.mdx` explain the non-archived tenant client count, ten-client floor, fixed USD offers, integer-cent response, test/live mode, 409/503 recovery and the absence of checkout, payment or annual-contract enforcement. Billing remains optional; this docs branch is not a publication or live-provider verification claim.

The held 2026-10-01 billing-settings candidate moves the existing workspace billing section from personal `/account` to the Settings directory's `/settings/billing` destination. `guides/billing-and-support.mdx` directs readers to Settings → **Billing** and documents the safe **Billing portal setup is incomplete** recovery response. Source review against composed app commit `d5587da4e986b3c609625c3dba54fead7852d4c1` confirms `billing.read` gates page access, `billing.manage` gates mutations, and provider configuration errors return HTTP 409 with support instructions; transient provider failures retain the generic 503 response. The guide does not claim that the Chargebee login-mode mismatch has been changed or that a portal session now succeeds. Keep this docs branch unpublished until app42 is released; no API/MCP references change.

The released `e5f7e92` contract excludes the billing router from public OpenAPI and omits `ask_ledgr` from MCP. The current docs retain the human Billing and in-app Ask guides but remove the billing API recipe and MCP Ask entry. See the dated reconciliation in [API and MCP evidence](Review%20Evidence/API%20and%20MCP%20Audit.md); the earlier candidate record above remains historical.

The guided-domain guides and this reference reconciliation were published in docs PR #1 (`a271e5c`, content `3d67b353`) after application PR25. Main-branch validation and Mintlify deployment succeeded; direct hosted-page and search readback are recorded in the [Review Log](Review%20Log.md). The Issues Domain-filter correction remains held for its separate application release.

The held designer-wizard update covers the Standards domain cards opening the dedicated domain setup page, its `Questions` / `Sources` / `Review` stages, question-rail states and navigation limits, and the distinction between browser-stored answers and the server-side inactive-standard save. The workspace setup guide explains the `← Setup` return and post-save **Return to Standards setup** link. These claims are checked against the unmerged application candidate; keep this change held until its matching app release is verified.

The separate Issues technical-domain guide correction was published after application PR26 in docs PR #3 (`857b0c8`, content `5e66c4f`). It distinguishes technical finding category from the legacy email-domain URL filter. Main-branch docs validation, Mintlify deployment, direct hosted-page readback and hosted search passed; see the dated [Review Log](Review%20Log.md) for limits.

The held Opus UI refinement updates [Run a client review](../guides/client-reviews.mdx) for the **Client reviews** tab, header actions and review-row labels. The existing Run checks and guided-domain guides still match the inspected source actions and ordering; domain icons are decorative and do not change the task. No Reviews, Run checks or domain-setup screenshot is currently published, so no image is presented as evidence of the unreleased layout. Publication awaits the matching application release and final source re-review.

That Reviews guide correction was published after application PR27 in docs PR #5 (`86e544e`, final content `6ffa26d`). It includes the conditional **Needs decision** state identified during independent review. Main-branch docs validation, Mintlify deployment, direct hosted-page readback and search indexing passed; see the dated [Review Log](Review%20Log.md) for limits.

The further isolated candidate against application `9d3c8fd` adds `get_remediation_plan_outline` under the existing `remediation:read` scope, taking this branch's generated catalogue to **16 MCP tools** while keeping eleven curated REST reads. The fixed result exposes only plan/detection/Organization IDs, autonomy and reversible metadata, and at most 50 ordered step IDs, action types and approval/reversibility flags. It marks execution and target readiness `not_checked` and simulation `unknown`; truncation means the displayed steps are incomplete. The MCP guide directs Claude Code and Codex to use the outline for broad plan intent, run-status reads for lifecycle and verification, and the signed-in human workflow for targets, approval and action. No matching app deployment, authenticated call, public publication or live provider outcome is established by this branch.

The next **unpublished candidate** against application `925c29b` adds `get_remediation_review_preview` and `request_remediation_review`, taking this branch's generated catalogue to **18 MCP tools** while retaining eleven curated REST reads. The new [MCP workflow](../mcp/request-review.mdx) explains exact detection/plan IDs, a 15-minute signed review revision, selected target metadata, local readiness versus unchecked vendor execution, current user-key scopes and owner permissions, a caller UUID idempotency key, pending-only run/approval creation, replay and uncertain-response recovery. The metadata-only outline cannot supply this revision. Separate named-human approval, execution, verification and rollback remain outside these two calls. The draft also updates introduction, connection, security, token and remediation guides. Application commit `7a52214` adds the new scopes to the key form. The workflow includes `remediation:read` for optional outline and run-status calls, alongside the preview/request scopes; publication must wait for the matching app release and independent review. The curated OpenAPI snapshot still excludes these conditional write routes and directs readers to the authenticated live schema for deployment-specific REST availability.

For each implemented guide, change its row to linked coverage with source revision and verification evidence. Reconcile new/removed routes, shell actions, connector modes and server-tool scope choices during feature changes. Re-audit the changed user task rather than treating this dated inventory as permanent proof. Preserve the original audit notes as historical evidence.

The held 18-tool release docs now explain the Developer Console Idempotency-Key input, explicit UUID generation, stable same-payload retries and unsupported-required-header refusal. Publish only with the corresponding reviewed console implementation.

The next held candidate against isolated application `7c1e044` adds [REST evidence refresh](../api-reference/refresh-evidence.mdx) and [MCP evidence refresh](../mcp/refresh-evidence.mdx), three generated MCP tools (21 total) and one safe curated operation GET (12 total). It documents source-wide collection across mapped clients, user-owned `integration:sync` versus read-only `integration:read`, REST dot scopes, stable same-key replay, exact operation polling, no automatic repeat of uncertain vendor work after claim, and `completed` collection versus unknown assessment. The app candidate and docs both remain under independent review; these counts describe generated draft references, not a deployed or published capability.

The first-link release added [REST first-link guidance](../api-reference/link-source-clients.mdx), [MCP first-link guidance](../mcp/link-source-clients.mdx), a curated mapping-discovery GET (13 selected reads) and `list_source_client_mappings`/`link_source_client` (23 MCP tools). It documents the generic PSA/RMM first-link allowlist, distinct REST/MCP scopes, persisted-record discovery, caller-bound short-lived revision, same-key receipt replay, and the separate source-wide refresh and assessment steps. Application release 7aeec59 and docs release 8a3e167 were verified in the corresponding workflows; both hosted first-link pages returned 200. This does not establish a real vendor link or publish the later standards-copy and inspection candidates.

The standards-copy and inspection release adds [MCP disabled-draft copy guidance](../mcp/copy-standard-draft.mdx) and four tools: `list_standard_library_templates`, `copy_standard_library_template`, `list_workspace_standards` and `get_standard_definition`. The generated catalogue has 27 tools and 13 selected REST reads. Copy uses a user-owned `standards:copy` key backed by the owner's live `detection_rule.write`; the exact curated template revision and one idempotency UUID produce an atomic disabled draft with controls and manual checks. The historical copy receipt does not assert current state. The two inspection reads use `standards:read`; a user-owned key needs live `detection_rule.read`, while a read-scoped service key may inspect. Returned definitions and instructions are workspace-authored data, not assistant instructions, and inspection does not assess or enable a standard. Application `ca2f0b3` and docs `e099248` were deployed; the hosted copy guide and catalogue were read back. No authenticated live MCP invocation or real client outcome is claimed.

The released activation workflow adds [MCP copied-draft activation](../mcp/activate-standard-draft.mdx) and a [REST activation recipe](../api-reference/activate-standard-draft.mdx). Its verified catalogue has 29 MCP tools and 14 selected REST reads, including the full-policy activation preview. A user-owned key needs `standards:activate` or REST `detection_rule.write` plus the owner's live permission to enable an existing disabled receipt-backed draft; service keys can preview with the read scope but cannot activate. The short-lived revision covers the complete bounded workspace policy, while client overrides and the roster remain independent. A historical receipt does not assert current enabled state. Activation does not run checks or change vendors. The application and hosted docs release are recorded in the review log; no authenticated activation mutation was claimed.

The held activation-scaling candidate adds REST summary and page reads and the MCP `get_standard_activation_summary` / `get_standard_activation_page` tools to the existing activation workflow. Its 15-minute revision signs authored policy and saved assignments; bounded pages use at most 25 rows and 240 KiB, while the new paged protocol has no total row ceiling for controls, manual checks or rule-scope rows. The legacy full-preview route remains available with its 50-control, 50-check and 200-scope-row bounds. Summary and page reads have a 10-second service budget; activation's final policy recheck has a 5-second budget. The revision does not freeze per-client overrides or the full client roster. These time, page and request bounds do not declare total standard capacity. Initial creation still batches 30 controls/checks per request and selected-client assignment replacement accepts up to 5,000 IDs per request. Generated draft references now contain 18 selected REST reads and 33 MCP tools, both from the current app candidate. Hold publication until app release and independent review; these counts describe the candidate, not production availability.

The Standards/Facts table update documents server-side search, filters, complete-result counts, sorting and pagination to the actual routed pages. Standards list search matches name, slug, description and setup domain; its enabled filter and whitelisted name/control/client-count/status orders apply before paging. Only an unparameterized `GET /standards` retains its historical full-list response; explicit page/filter/sort requests default to page 1 and 25 rows (maximum 100; `q` maximum 200 characters). Facts sorting accepts `subject`, `predicate`, `value`, `sourceSystem` or `observedAt`, with `asc` / `desc`; default remains `observedAt desc`. Sorting runs over the complete tenant/client/filter-matched result before paging, and value order uses the safe public projection. These features do not change assessment, activation or fact-read permissions. This does not move all work into SQL: the Standards index service still computes full tenant summaries before filtering and slicing. Docs PR #19 exact head `eafc2b40e91d6cd44667657e4bf901564e0f5f74` merged as `0f7ab8ba229c2c97e6e29cc20dadb853f100103e` after app PR #50 went live. Main workflow `36872717239` passed; hosted Standards and Evidence guides and `/api-reference/openapi.json` were read back. See the dated Review Log for exact evidence and limits. No live table interaction or hosted visual inspection is claimed.

## Guided setup questionnaire update — 2026-09-29

A held documentation draft now reflects the guided setup polish candidate at `/private/tmp/alignr-domain-setup-polish` (application base `e9218389b533c3e995d477c6cd03ba6e077a0360`, candidate commit `e8bf24b82a7082d892466203fbf8456eff7c7c36`; `DomainIntakePage.tsx` SHA256 `f3c3732606c285abd7be770b55b1e9e0c31e404d2dcab93563e2dd6816feeb21`). It updates [Build or import a standard](../guides/build-or-import-standard.mdx), [Use the setup wizard](../guides/setup-wizard.mdx), [Quickstart](../quickstart.mdx) and [Standards and controls](../guides/standards.mdx) to explain one question at a time, optional check inclusion, the compact selected-check count, the final review, preserved connector and client-mapping stage, and inactive save. This supersedes the earlier held Opus note that said the guided-domain copy remained accurate. The source is an unmerged candidate; do not publish until application integration and release are confirmed.


## 2026-09-30 — selected-client standards and client-page updates (held app candidate)

This candidate aligns `quickstart.mdx`, `guides/setup-wizard.mdx`, `guides/standards.mdx`, `guides/build-or-import-standard.mdx`, `journeys/visual-tour.mdx` and `journeys/evaluate-alignr.mdx` with the guided standard's active selected-client save, empty initial assignments, explicit **Deploy to clients** assignment and separate **Run checks** assessment. It preserves disabled workspace-wide defaults for new blank/general standards, library copies and checklist imports, and the saved scope of existing standards. `guides/configure-client.mdx` now follows the saved-connection chooser; `guides/organizations.mdx` describes client-list filters as triage only; `guides/evidence.mdx` describes the Facts table as observations, not a result. The REST assignment recipe and generated read operation document replacement semantics and their permission boundary.

Compared UI and route behavior with application candidate `/private/tmp/alignr-client-checks-clarity` at base `0531397` plus the selected-scope work in its uncommitted tree. This is source comparison only; the application candidate still needs its own review/release. MCP still has 31 tools with unchanged tool names and scopes, but standard-inspection and activation-preview responses now expose scope metadata and assignment counts; activation preview also signs an assignment fingerprint. The curated REST reference now includes the assignment read and selected-scope fields. No control catalogue changed.

## 2026-10-01 — Datto patch-state correction (held)

The held Datto correction against application commits `cd99774` and `e617d33`
updates the Datto RMM integration summary, the `patch_status` predicate
interpretation, and both generated endpoint baseline control explanations. It
states that an unfamiliar Datto state is unknown evidence (`no_data`), not pass
or fail; only a validated complete inventory can withdraw Datto's previous
patch observation, while malformed or partial inventory preserves it subject
to freshness rules. The canonical predicate vocabulary and control definitions
did not change, so the generated control catalogue,
OpenAPI and MCP references remain unchanged. Keep these pages held until PR41's
matching application release is verified.

The Users and API Keys table update at `/private/tmp/alignr-docs-users-api-keys` updates [Manage your account and invite teammates](../guides/account-and-team.mdx) and [Create an API key](../guides/api-keys.mdx) against Users app commit `b3eff8eb2382c567ff88827ac6977dd24087d4a7` and final API Keys app commit `fc179c3498bd28a08c5ae2cab660113681880c5f`. Users search covers name, email and role; status and role filters include the **No role** option, heading sorts cover name/email/roles/status/second factor/last login, and mobile uses **Sort users**. The Users UI loads API pages and then filters, sorts and paginates the collection locally; this is not a new server-side search or sort contract. API Keys documents the existing name/prefix/owner search and status filter plus sortable Name, Accountable to, Scopes, Last used, Expires and Status headings; desktop uses heading buttons and mobile retains **Sort API keys**; the prior default remains Name A–Z, and missing owners/dates remain last. No API schema, generated OpenAPI or MCP change is included. The matching app PR #51 is live; the docs update remains unpublished pending final docs checks, merge and hosted readback. No authenticated production interaction is claimed.

The held Controls table update at `/private/tmp/alignr-docs-controls-settings` aligns [Parameters and client overrides](../controls/parameters.mdx) with application Controls candidate `cf98db8f1edf7f2b36c854f23cd1a582738dd1fc` (Controls collection and draft-settlement behavior from `fda1783a66021c0105c08a4b444fa681e11c46b7`). The follow-on `e7c500a0dd57b255be1ad5742710ec3997b3eb1f` changes only the responsive filter layout; source diff review found no handler or contract change. The guide explains search across name, identifier, description and category; category and On/Off filters; desktop heading sort and mobile selector; 25/50/100-row pages; optional category grouping; and parameter draft retention while filtering or paging, including recovery after a failed save. These are Controls-tab display/editing affordances only; no API or MCP contract, permission, generated reference or control definition changed. Hold publication until the matching app release and independent docs review; the source has not been deployed or accepted live.

## 2026-10-01 — Fix history search and ordering (held)

`guides/remediation.mdx` now explains whole-history literal search, composing
Organization/result filters, five heading cycles, mobile sorting, 25-row pages
and default newest-started ordering. The curated API selection adds only
GET `/api/v1/remediations` and `/api/v1/approvals`, each with q200 and ten
explicit sort values. The approval guidance retains status chips, default
newest-requested order, missing-context behaviour and the Reset view action.
Source: composed app PR53 `a9be8793a6e09dc429d8864f4ff289614ee74963`.
No action, rollback, approval, verification or MCP capability changes are claimed.
This branch builds on docs PR21 at reconciled head
`730321933759c4fd3fbd4b9c13a0f6acff3d6d63`; Docs PR20 has since published.
At this candidate checkpoint PR21 was still held for the Controls app release.
PR22 was held for app PR53 and the PR21 dependency. This was source-aligned
candidate evidence, not hosted acceptance; see the later PR21 publication and
PR22 reconciliation record below.

## 2026-10-01 — Global Organization filter and Fix history picker (held)

The separate picker follow-up branch updates [Daily review](../guides/daily-review.mdx),
[Review remediation](../guides/remediation.mdx) and [Standalone detection rules](../controls/standalone-rules.mdx)
against application source head
`8dfaf3aec4db46b9678146a284b779809f194bf4` in
`/private/tmp/alignr-client-picker-composed`. The global Organization filter
and Fix history picker are present at
`d8f586785c961c621ad381b982bf88dd1700a0ef`; the Monitoring RuleScope picker
and its permission-retention correction are included in the pinned head. The
RuleScope file matches independently reviewed commit
`41b26d82f9a7cc2805ba4a85e9198d8e5d391bd9` byte-for-byte.
The guides explain name/slug search, 25-row directory pages, explicit selection,
clearing and permission-denied behavior. Fix history has a separate run search,
an `organization.read`-guarded picker with **Load more**, and a URL-scoped client
filter that takes precedence over the global filter. Monitoring explains
**Every organization** versus **Selected clients only**, independent retention
of selections while browsing, a non-removable final selection and retained scope
when directory access is denied. The Organization list API search/page contract
is existing; no API/OpenAPI/MCP or permission change is documented. Keep this
draft stacked on Docs PR22 and unpublished pending matching app release and
final docs checks.

## 2026-10-01 — Docs PR21 publication and PR22 reconciliation

Docs PR21 (`730321933759c4fd3fbd4b9c13a0f6acff3d6d63`) was published after the
matching Controls app PR52 was verified live. PR21 merged as
`63b422fc02e744a343442a7d1c18d07ae9689e85`; main validation run `36893332012`
passed. PR22 remains a held draft for app PR53; its dependency on the now-published
PR21 has been reconciled to main, but PR22 is not released or hosted-accepted.

## Held Workspace health table controls — 1 October 2026

The existing Workspace health guide now explains both tables' full loaded-collection
search, state/readiness filters, heading cycles, equivalent selector choices and
25/50/100-row paging. It distinguishes local array paging from server pagination
and retains full-workspace summary semantics. Source verified against final application
`90c9d0ea6a1821ae99f0f02cd1c0f8c2b617ffe4`; the composed 9a4518c candidate has
identical feature source. Coordinator independent content review cleared the
guide. Publication remains held until the matching Health application release. No API or MCP
contract changes or generated reference updates are implied.

## Held Activity collection controls — 1 October 2026

Daily review and security/data export guidance now cover full-collection search,
heading/mobile ordering, pagination, URL-over-header client scope, matching export
filters/order, query metadata privacy and CSV formula-safe presentation. Source:
application `18fada94c706c3b6cc2c547c3606b423238ccc9f`, identical feature source to
reviewed `0d27682`. Publication is held until the matching application release.
Audit routes are absent from curated generator GROUPS, so this slice does not add
or regenerate public OpenAPI operations. The existing 50,000-row cap is a current
implementation limitation, not an accepted new policy. The owner's direction to
remove collection/export limits remains outstanding application work; do not
claim unlimited export before implementation and verification.


## Held workspace shell candidate — 2 October 2026

The initial draft described a global client selector. The latest app direction removes that selector; the Introduction, daily review, Issues, Ask Alignr and Fix history guides now describe route- or page-control-specific client scope instead. The prior source pin `3837e3f7daf50a511923b2c4d08b568ce1dad947` is superseded for this behavior. Final source-pin review, docs checks and rendered preview remain pending.

Settings, account/team and billing guides distinguish workspace-specific and personal-account actions inside the same top-left workspace menu and retain existing Settings paths. Team and billing links retain their read/manage permission boundaries. The Settings directory's previously omitted Billing row is now documented. No Inbox rename, workspace switching, new billing behaviour or score changes are claimed.

Publication is held until the matching app release is verified. Source review is separate from rendered acceptance; desktop/390px/light/dark/keyboard and changed docs previews remain outstanding. Refresh affected visual-tour screenshots from authorised non-sensitive UI before publication, or explicitly retain them as dated prior-layout examples. No new screenshots were fabricated. Public `docs.json` navigation and reference catalogues are unchanged because pages, API/MCP contracts, predicates and controls did not move or change.


## Held Linear workspace navigation and setup guides — 2 October 2026

Updated Introduction, daily review, Settings, account/team, billing, setup, client,
integration, standards and issue-triage wording against app candidate
`/private/tmp/alignr-linear-ui-rebuild` at `719c9bd7d1cbf8e68e677b258ed3c5f4f65bf399`.
Relevant route commits include shell `b1a0e0d`, Standards/integration setup `b40b7ed`,
Clients list `487e1fa`, and Issues list/details `2fff1e6` plus four-status correction
`b36ebd8`. The guides describe the sidebar's
Overview/Issues/Reviews/Activity, Clients/Standards/Integrations and MCP/Settings
groups; the top-left logo menu contains both workspace actions and personal-account actions; the
Settings directory and permission-dependent links; current compact integration and
standards entry points; guided questionnaire/source/review stages and safe return
links; and the Issues search/filter/display controls with the persistent desktop
detail pane. The Clients guide matches the current four sortable headings and four filters. The Standards detail **← Standards** link was checked to retain `q`, `state`, `page` and `pageSize` when returning. The
issue page incorporates the functional clarifications prepared on
`docs/issues-workspace` without claiming an unsupported **All statuses** option or
obsolete heading-sort interaction. No API/MCP schema, endpoint, generated reference
or Mintlify navigation configuration changed.

This documents a held app candidate, not a released workflow. The app worktree is
still active, so the exact final source pin and remote UI/CI acceptance remain to be
reconciled before publication. No hosted readback, rendered docs preview,
authenticated product journey or app test is claimed here.


Final UI release source: application PR65 merged candidate `35f0a13` as `00d3962`
on 2 October 2026. The documented navigation and inline setup flows remain aligned
with that source; see the final validation entry in Review Log. Public prose is
ready, with publication and hosted readback pending the application promotion.
