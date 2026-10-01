# Application documentation coverage

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
