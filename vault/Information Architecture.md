# Information architecture

## Readers and their jobs

- New MSP administrator: establish a source, map a client, choose expectations and explain a first result.
- Engineer: investigate a failure or coverage gap, adjust an expectation deliberately and verify the follow-up.
- Standard owner: choose a baseline, build a control, manage client exceptions and manual reviews.
- Developer or assistant user: obtain suitable credentials and use a supported API or MCP operation.

## Public navigation

Documentation contains Start here (Introduction, Setup wizard, Quickstart, Your first assessment) and expandable groups for workspace setup, connecting tools, workspace management, day-to-day work, reports/client portal, assessment concepts, controls, and help/reference. Controls contains the overview, baseline selection, recipes, category references, build/manage guides and advanced definitions.

API reference contains key setup, authentication, interface guidance and curated read operations. MCP contains connection, task-based tool reference and security guidance. Neither is a prerequisite for using the app.

`docs.json` is the executable navigation configuration. Generators must locate tabs by name, never by array position. Changing navigation also requires updating Introduction's explanation and checking mobile navigation.

## Guided path

`journeys/first-assessment` → `journeys/connect-and-map` → `journeys/read-your-first-result` → `journeys/close-the-loop`.

The path uses Acme throughout. It starts with administrator MFA registration and ends with evidence gaps, a supported operational follow-up and separate human policy review. It deliberately distinguishes registration from enforcement and a failed expectation from missing evidence.

`controls/recipes/overview` links focused practical examples. The vulnerability recipe tests zero, the exact boundary, an exceeding value and an absent observation; it explains that changing an override changes the question rather than improving the environment.

## Keep depth deliberate

Journeys teach one task end to end. How-to guides describe actions. Concept pages explain reasoning. References supply exact names, defaults and limits. Link between them; do not duplicate entire sections. A page should end with a completion checkpoint and an appropriate next step when it teaches a workflow.

Existing URLs are retained. New pages must appear in navigation or have a documented reason to be intentionally hidden. Hidden pages are still public; internal records use `.mintignore`.

## Recovery paths

Troubleshooting starts from the visible symptom and gives a recovery check for each path. The backup recipe connects automated protection/job/recency observations with a separate restore review. Keep its future-timestamp caveat beside the recency example; never imply the current within_days operator is past-only.

## Setup milestones

Keep client-directory import separate from evidence collection, and collection separate from running checks. Setup guides use actual Import clients / Clients & sites entry points. Library draft activation is an explicit prerequisite to evaluation. The evidence guide separates observation time from timestamps carried as values.

## Workspace administration

The wizard is the first configuration path. Readiness checks actual coverage, and Workspace health monitors collection, assessment freshness and follow-up. Keep these distinct from passing controls. Manage your workspace contains a Settings directory, accounts/team access and health. Client Microsoft connections belong beside client mapping, explaining workspace defaults, per-client overrides and direct access for clients outside Partner Center. Link detailed guides instead of making Quickstart a second reference catalogue.

The signup path leads to the wizard immediately and the welcome message links back to it; neither email delivery nor wizard navigation proves a working connection. Explain automatic connection-key preparation and its retry state in setup and integration guidance. The main app navigation exposes **MCP** as the token entry point; the MCP tab in these docs explains client configuration and the bounded available tools.

The wizard has five optional, resumable steps: Microsoft partner access, PSA, RMM, teammates and standards. Keep PSA client/service context separate from RMM device observations; ConnectWise Automate remains unavailable in the RMM choice. The current wizard offers a guided baseline; checklist import remains a Standards workflow outside it. Platform Direct and Partner Center Microsoft registrations have separate permissions and availability. Token documentation must explain that the bulk **Select all** action ignores the current text filter and selects all issuable current scopes.

The Standards step hands off to guided baseline setup with `from=setup`. Its Back/exit route returns to `/setup?step=standards`; an unfinished baseline is a same-browser, account-scoped draft that offers Resume or Start again on re-entry. Saving creates an inactive standard for review and does not itself finish the wizard or enable evaluation. Show these continuity and completion boundaries beside the Standards step, rather than treating the wizard and builder as separate journeys. Keep the five visual-tour step captures in sync with the released header and logo treatment.

## Continuing after the first result

Daily review → triage → supported remediation or client review → risk/roadmap → fixed report or authorised portal sharing. Vendor setup is grouped by category with per-product accordions; UniFi and SonicWall have dedicated mode guides. Keep API recipes in the developer tab and link them from task guidance.

## Buyer and account-manager journeys

The pilot guide in Start here establishes evidence-based evaluation checkpoints without promising trial terms or ROI. The client-meeting playbook joins reviews, risks, reports, portal responses and verification. Keep suggested operating practices distinct from app features.

## Visual, trust and developer handoffs

Start here includes an annotated tour of current real app screens. Keep those captures in step with the released wizard and exclude video. Detailed Microsoft/Meraki setup stays in Connect your tools. Security/data and billing/support live in Manage your workspace, with buyer entry links on Introduction. The API tab includes an inactive-standard write recipe that explicitly distinguishes human access tokens from API keys, plus a client-management recipe for the three Organization writes supported by a user-owned scoped key. The latter explains owner permission checks, service-key refusal, audit attribution and recovery after an uncertain write. The MCP tab has a separate client-management guide for listing, creating and updating clients with the 13-tool first-release candidate registry; it explains the distinct MCP scopes, bounded paging, service-key refusal and uncertain-create recovery without implying general REST/MCP action parity. A separate candidate documents two remediation status reads, yielding 15 tools only when the matching API release is verified. Those reads distinguish execution status, verification and simulation, and do not imply rollback readiness. The next isolated candidate adds a metadata-only remediation plan outline as a 16th tool: the assistant can explain action types and approval/reversibility metadata, while the signed-in app remains the place to inspect targets and request an action. It cannot infer execution readiness or simulation mode from the outline. Both API and MCP introductions point to the in-app Developer Console and explain that its requests run against the real workspace.

The public site uses Geist for headings and body, matching the app. Headings use weight 500 and body text 400; keep the documentation legible and check navigation at desktop and mobile widths after font changes.

The MCP introduction and connection guide now explain two authenticated, static help resources: `alignr://help/getting-started` and `alignr://help/tools-and-scopes`. The generated tool catalogue keeps these resources separate from executable tools. `resources/list` and `resources/read` are the discovery path for capable Claude Code or Codex clients; `tools/list` supplies the deployed tool schemas. The in-app Developer Console shows the current MCP reference but its **Try it** panel executes REST requests against the real workspace, not MCP calls. The signed-in remediation guide remains the place for approvers to review current plan steps and concrete targets before an action.

The optional billing estimate belongs in **Billing and support** under Manage your workspace, with a linked API recipe and one curated read operation in the API reference. Keep USD catalogue estimates separate from contracted terms, checkout, payment and existing subscription-status records. The estimate page uses `billing.read` and the server's current non-archived Organization count; it is not an onboarding requirement.

The released source-refresh workflow adds a separate API guide and MCP workflow for a recoverable evidence collection. The reader chooses a connection rather than a client; the operation covers all mapped clients, returns a durable operation UUID, and is polled for its exact SyncRun outcome. Link token creation, source discovery, request and poll in that order. Explain REST dot scopes separately from MCP colon scopes, same-key retry after an uncertain response, and the distinction between completed collection and assessment. The curated API reference adds only the safe GET; the write is explained in the guide and authenticated live schema. Source refresh shipped before the first-link workflow.

The released first-link workflow adds `mcp/link-source-clients` and `api-reference/link-source-clients` before source refresh in the task journey. Discover an existing generic PSA/RMM remote-company mapping, identify the existing Organization, use its short-lived caller-bound revision and one saved idempotency UUID to first-link only an unassigned record, then explicitly refresh the whole source if needed. `integration:map` is a new MCP scope backed by `integration.manage`; REST retains dot scopes. Keep Microsoft selection, arbitrary remapping/unlinking, historical-fact reassignment and automatic refresh outside this guide. The published catalogue includes 23 tools and 13 selected read operations, matching the verified 7aeec59 release. Use the authenticated live reference for deployment-specific availability.

The standards-authoring guide adds `mcp/copy-standard-draft` beside client management. Lead with the human meaning of the curated library, then list its exact revision, copy one disabled draft with a user-owned key and one idempotency UUID, inspect its current controls and manual checks through the bounded read tools, and finish in the signed-in review-and-enable workflow. Distinguish `standards:read`/`standards:copy` MCP scopes from REST dot scopes and the human-only enable action. A historical copy receipt does not claim the current standard is still disabled or present. The generated 27-tool catalogue is tied to the verified application release; deployment-specific availability is discoverable in the authenticated live reference.

The standards-authoring workflow starts with the curated library, copies one disabled draft using a user-owned key and one idempotency UUID, then inspects its current controls and manual checks through bounded read tools. The held activation candidate adds a complete bounded policy preview and a separate `standards:activate` action for a receipt-backed draft. It requires an explicit workspace-wide acknowledgement; it does not evaluate controls, collect evidence or change a vendor. Existing client overrides remain in force, and the preview does not freeze the client roster. Distinguish MCP colon scopes from REST dot scopes and most human-only editing routes. Historical copy and activation receipts do not claim a standard's current state. Keep the generated catalogue tied to the matching application source and hold publication until that release is verified.
