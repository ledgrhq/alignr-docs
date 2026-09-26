# Application documentation coverage

Living coverage map. Last audited 2026-09-26 against application `565fae53f166e14dae4f3d872572ab3e3bdfdc28` and published documentation `0bf7785de4d97ac9f8a759bb9626d837fa4feeca`. The audit used three independent subagents plus the coordinator, followed by a separate review of the immediate corrections.

## What this review proves

Source inspection reconciled all 46 staff route declarations (including index/fallback), the separate portal SPA and route-linked dialogs, rails and connector catalogue with committed public docs. Backend services were inspected where necessary to establish the workflow. It identifies documentation coverage and source-backed gaps. It is not an authenticated whole-app walkthrough, production availability certification, security audit or full application test run.

Concurrent quickstart, integrations and MCP connection drafts were excluded from the published baseline and preserved. App code was unchanged during the inspected target; concurrent infrastructure/delivery work is outside this audit. New docs must still verify exact permissions, edge cases and live provider instructions before publication.

## Evidence

- [Daily operations audit](Review%20Evidence/Daily%20Operations%20Audit.md): Overview, Issues, approvals, fixes, Ask, search, Activity and audit.
- [Setup and integrations audit](Review%20Evidence/Setup%20and%20Integrations%20Audit.md): authentication, workspace setup, client connections/domains, settings and connector inventory.
- [Assessments and sharing audit](Review%20Evidence/Assessments%20and%20Sharing%20Audit.md): standards/intake/import, manual review work, risk, roadmap, reports, staff/external portal.
- [API and MCP audit](Review%20Evidence/API%20and%20MCP%20Audit.md): tokens, developer console, generated references and retained backend boundaries.

## What to write next

P1 means the missing guidance blocks a major task or conceals a consequential distinction. P2 deepens an already usable path. These are documentation priorities, not product incident severity. Each row is open unless explicitly marked complete below.

| Order | Priority | Deliverable | Reader outcome and acceptance checkpoint |
| --- | --- | --- | --- |
| 1 | P1 | Triage issues + expand remediation guide | Find an issue, inspect evidence, explain Snooze versus Dismiss, request a supported fix, locate approval, understand requester/approver separation, inspect execution/verification and eligible rollback. |
| 2 | P1 | Run a client review | Schedule/assign manual work, start and resume a batch, handle changed items with reasons, complete pending work, follow up failures and reassess. Progress must never be described as pass rate. |
| 3 | P1 | Risk and roadmap | Accept a risk with reason/expiry or propose work, compare one-off/recurring costs, record decisions and delivery. Proposal approval/work completion do not prove verified resolution. |
| 4 | P1 | Client reports and portal handoff | Prepare and inspect a fixed report snapshot; print/JSON export. Configure portal sign-in, views and independent proposal-response permission; verify external audience. Report, internal preview and external portal are different outputs. |
| 5 | P1 | Integration index + first vendor guides | Catalogue 38 connector-backed types (including 2 directory-only) and 8 unavailable entries by task. State credential mode, scope, matching unit and evidence limitations; verify vendor-console instructions using official sources. Start Microsoft-adjacent PSA/RMM, then network, identity and backup. |
| 6 | P1 | Maintain a connection | Rotate the whole required credential bundle, reconnect, inspect successful collection, replace/retire a source and understand mappings/history. Dedicated UniFi/SonicWall mode decisions. |
| 7 | P1 | Ask Alignr | Open the rail, verify client/standard context, ask an evidence question, inspect citations, review Before/After and apply a configuration draft. Explain fresh assessment and uncertain-response recovery. |
| 8 | P1 | Sign-in and recovery | Self-service reset, used/expired token and second-factor challenge recovery. Verify exact backend expiry and session consequences before publishing numbers. |
| 9 | P2 | Build or import a standard | Choose guided intake/library/spreadsheet/blank. Explain local draft versus saved inactive standard, row review/split/skip and manual definitions versus completed assessments. Add a fictional validated CSV. |
| 10 | P2 | Daily review and app wayfinding | Interpret Overview score alongside coverage; Refresh evidence scope versus Run checks; search/shortcuts, client scope, Activity and filtered audit export. |
| 11 | P2 | Domain-check operations | Microsoft/manual targets, 50-domain limit, enabled/scheduled/paused states, saved settings and Check now, evidence boundaries. |
| 12 | P2 | Standalone rule boundary | Explain that standalone match/where identifies a candidate violation, whereas control match/where selects a population and expect defines the requirement. Confirm discoverability before adding a tutorial. |
| 13 | P2 | API/MCP worked recipe | Produce a read-only client assessment summary with exact scopes, paging, timestamps and missing-evidence handling; reconcile retained-tool versus current UI scope selection. |

Suggested composition: retain Documentation as the single app-user tab. Add expandable **Review and follow up** when the new operational guides exist. Keep vendor pages under a grouped integration catalogue. Extend existing guides when a section completes the task; do not create a page for every dialog. Do not add empty navigation entries in anticipation of this backlog.

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

| Route family / surface | Audit owner | Coverage disposition |
| --- | --- | --- |
| `/login`, `/signup`, `/accept-invite`, `/forgot-password`, `/reset-password` | Setup | Signup/invitation basics covered; recovery missing. |
| `/setup`, `/setup/readiness`, `/health` | Setup | Recently added guides largely complete for intended tasks. |
| `/setup/baseline`, `/standards`, `/standards/library`, `/standards/import`, `/standards/deploy`, `/standards/:id` | Assessments | Library/custom definition/run covered; intake/import task gaps. |
| `/organizations`, `/organizations/import`, `/organizations/:id`, connection/domain/check tabs | Setup + Assessments | Creation/mapping/Microsoft well covered; domain depth and review work need follow-up. |
| `/assessments/work` | Assessments | Review batches, queue and follow-up guide missing. |
| `/organizations/:id/reports`, `/organizations/:id/reports/:reportId` | Assessments | Fixed snapshot/export workflow missing. |
| `/risk`, `/roadmap`, corresponding client tabs | Assessments | Operational workflows missing. |
| `/organizations/:id/portal`, `/settings/client-portal`, separate portal SPA routes | Assessments | Settings basics covered; sharing/view/decision/external journey incomplete. |
| `/`, `/detections`, `/remediations`, `/approvals`, `/activity`, `/logs` | Daily operations | Concepts covered; action-oriented daily guidance missing. |
| `/monitoring`, `/monitoring/rules/new`, `/monitoring/rules/:ruleId` | Assessments | Routed but not linked in current shell; clarify standalone violation predicates versus control expectations before promoting an editor tutorial. |
| `/settings`, `/settings/microsoft`, `/account`, `/users`, `/users/:id`, `/roles`, `/roles/:id` | Setup | New admin guides largely cover primary actions; recovery extends them. |
| `/integrations`, `/integrations/:id`, all offered connector types/modes | Setup | Generic/Microsoft guide present; catalogue/vendor and maintenance gaps. |
| `/api-keys`, `/api-keys/:id`, `/developer`, API/MCP | Coordinator | Narrow inaccuracies corrected; recipe and product-boundary backlog retained. |
| Shell Ask rail, command search, mobile navigation, notices; fallback | Daily operations | Ask/navigation undocumented; health notice has destination guide; fallback needs no standalone guide. |

## Deliberately excluded from new public promises

Unrouted legacy Ask/Overview/client editing screens; standalone agents or notification inboxes that do not exist; historical asset/document/migration UI retired by ADR-0023; arbitrary portal file sharing; automatic proposal execution; scheduled emailed reports without evidence; future integration delivery dates. Retained backend operations are accounted for but do not justify resurrecting retired product positioning. Operator AWS/ClickHouse work remains in internal operational runbooks and is not certified by this review.

## Keep this map current

For each implemented guide, change its row to linked coverage with source revision and verification evidence. Reconcile new/removed routes, shell actions, connector modes and server-tool scope choices during feature changes. Re-audit the changed user task rather than treating this dated inventory as permanent proof. Preserve the original audit notes as historical evidence.
