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

Standalone `/monitoring` remains directly routed but absent from the main shell. Its advanced guide states that boundary explicitly. Portal contact access currently needs administrator/support setup because the current People & views screen lacks the required editor; do not invent a self-service screen.

## Deliberately excluded from new public promises

Unrouted legacy Ask/Overview/client editing screens; standalone agents or notification inboxes that do not exist; historical asset/document/migration UI retired by ADR-0023; arbitrary portal file sharing; automatic proposal execution; scheduled emailed reports without evidence; future integration delivery dates. Retained backend operations are accounted for but do not justify resurrecting retired product positioning. Operator AWS/ClickHouse work remains in internal operational runbooks and is not certified by this review.

## Keep this map current

The setup and developer guides now have a draft update for the five-step wizard, separate Direct/Partner Microsoft registrations, token bulk-selection behaviour and Developer Console entry. The tour uses new five-step local captures and removes the video and old four-step setup images. The other client, assistant and report captures remain from the same day's local demo and need final UI comparison before publication. Publication and hosted-page verification remain pending the matching application release.

A further draft against application `366ecc5` documents user-owned API-key client create/update/archive in `api-reference/manage-clients-recipe.mdx` and corrects authentication boundaries. The subsequent MCP draft against application `f047d6f` and `c98663e` adds `mcp/manage-clients.mdx` for list/create/update, revises the MCP introduction, connection, security and token guides, and regenerates the catalogue at 13 tools. The curated OpenAPI snapshot remains an explicit ten-read-operation subset. This draft must not be published before the matching API release is verified.

For each implemented guide, change its row to linked coverage with source revision and verification evidence. Reconcile new/removed routes, shell actions, connector modes and server-tool scope choices during feature changes. Re-audit the changed user task rather than treating this dated inventory as permanent proof. Preserve the original audit notes as historical evidence.
