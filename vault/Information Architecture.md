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

The wizard has five optional, resumable steps: Microsoft connection method, PSA, RMM, teammates and standards. Keep PSA client/service context separate from RMM device observations; ConnectWise Automate remains unavailable in the RMM choice. The Standards step shows four guided domain rows that open their dedicated setup pages directly; the separate **Choose a domain** action opens the chooser. Checklist import remains a separate Standards workflow. Platform Direct and Partner Center Microsoft registrations have separate permissions and availability. Token documentation must explain that the bulk **Select all** action ignores the current text filter and selects all issuable current scopes.


The Standards step shows four rows that lead directly to their guided domain pages; **Choose a domain** still opens the domain chooser. Identity is suggested first; Devices, Backup and manual-only Email & domains are separate guided standards. A **← Setup** exit and post-save **Return to Standards setup** link lead back to the workspace wizard's Standards step when the page was opened from setup. Saved standards appear by domain with On/Off state. Each builder has **Questions**, **Sources** and **Review** stages. In Questions, explicit Yes/No answers include or exclude each check; neither is selected in a new browser draft, Yes reveals follow-up settings in place, and No leaves that check out. The question rail labels the current question, answered Yes/No items, the next question and locked later questions; users can revisit answered questions and completed stages but cannot skip ahead past prerequisites. The question rail is the only question-progress indicator; do not add a secondary progress line or counter. Let content use the shell width. Show a compact selected-check count during intake and put the full list in final review. Preserve the sources stage after questions, domain-first connector choices with other categories or All tools available. Saving creates an active standard with selected-client scope and no clients assigned; **Deploy to clients** sets applicability, and **Run checks** is a separate assessment. New blank/general standards, library copies and checklist imports keep their disabled, workspace-wide defaults; existing standards retain saved scope. Browser drafts restore from local storage per account, workspace and domain; only **Create standard** creates the guided server standard, and unavailable browser storage blocks saving. Mixed/general standards remain available. Keep setup, quickstart, standards and the visual tour aligned with this flow.

The Standards page's primary guided entry is **Create standard**, which opens the domain chooser; the workspace wizard labels the same destination **Choose a domain**. On the Clients alignment table, click a column heading to cycle ascending → descending → default order. Search/filter is applied before the full matching list is sorted and paginated; there is no separate sort dropdown. On a client detail page, **Run all checks** queues the enabled automated standards for that client only and reuses collected evidence; it does not collect new evidence or complete manual checks. The overview count summary uses the API's evidence-eligible `scoreCounts`, with exclusions outside the coverage denominator. Keep those details in the relevant guides rather than duplicating API reference prose.

The held Microsoft guidance adds optional public domain-to-tenant-ID discovery in the connection form and two distinct MSP partner steps: administrator consent return, then delegated account authorisation. A discovered ID is not ownership proof. A dated consent return is not a verified grant, token or customer access result. Keep customer assignment, consent and GDAP checks after partner sign-in. On a client page, **Check access** is an observational sample of current access for that client; **Connect client** is the explicit Partner action that may request missing read consent. Keep these separate in prose and diagrams. The visual-tour Microsoft capture shows the empty partner selection; the two action buttons appear only after a connection is chosen, so its caption and prose must not imply they are visible in that image.

## Continuing after the first result

Daily review → triage → supported remediation or client review → risk/roadmap → fixed report or authorised portal sharing. Vendor setup is grouped by category with per-product accordions; UniFi and SonicWall have dedicated mode guides. Keep API recipes in the developer tab and link them from task guidance.

## Buyer and account-manager journeys

The pilot guide in Start here establishes evidence-based evaluation checkpoints without promising trial terms or ROI. The client-meeting playbook joins reviews, risks, reports, portal responses and verification. Keep suggested operating practices distinct from app features.

## Visual, trust and developer handoffs

Start here includes an annotated tour of current real app screens. Keep those captures in step with the released wizard and exclude video. Detailed Microsoft/Meraki setup stays in Connect your tools. Security/data and billing/support live in Manage your workspace, with buyer entry links on Introduction. The API tab includes an inactive-standard write recipe that explicitly distinguishes human access tokens from API keys, plus a client-management recipe for the three Organization writes supported by a user-owned scoped key. The latter explains owner permission checks, service-key refusal, audit attribution and recovery after an uncertain write. The MCP tab has a separate client-management guide for listing, creating and updating clients with the 13-tool first-release candidate registry; it explains the distinct MCP scopes, bounded paging, service-key refusal and uncertain-create recovery without implying general REST/MCP action parity. A separate candidate documents two remediation status reads, yielding 15 tools only when the matching API release is verified. Those reads distinguish execution status, verification and simulation, and do not imply rollback readiness. The next isolated candidate adds a metadata-only remediation plan outline as a 16th tool: the assistant can explain action types and approval/reversibility metadata, while the signed-in app remains the place to inspect targets and request an action. It cannot infer execution readiness or simulation mode from the outline. Both API and MCP introductions point to the in-app Developer Console and explain that its requests run against the real workspace.

The public site uses Geist for headings and body, matching the app. Headings use weight 500 and body text 400; keep the documentation legible and check navigation at desktop and mobile widths after font changes.

The MCP introduction and connection guide now explain two authenticated, static help resources: `alignr://help/getting-started` and `alignr://help/tools-and-scopes`. The generated tool catalogue keeps these resources separate from executable tools. `resources/list` and `resources/read` are the discovery path for capable Claude Code or Codex clients; `tools/list` supplies the deployed tool schemas. The in-app Developer Console shows the current MCP reference but its **Try it** panel executes REST requests against the real workspace, not MCP calls. The signed-in remediation guide remains the place for approvers to review current plan steps and concrete targets before an action.

The optional billing estimate belongs in **Billing and support** under Manage your workspace. Its route is deliberately excluded from the public OpenAPI schema and curated API reference; do not expose it as an API-key or MCP recipe. Keep USD catalogue estimates separate from contracted terms, checkout, payment and existing subscription-status records. The in-app estimate uses `billing.read` and the server's current non-archived Organization count; it is not an onboarding requirement. Ask Alignr remains an in-app assistant, not an MCP tool in the released registry.

The released source-refresh workflow adds a separate API guide and MCP workflow for a recoverable evidence collection. The reader chooses a connection rather than a client; the operation covers all mapped clients, returns a durable operation UUID, and is polled for its exact SyncRun outcome. Link token creation, source discovery, request and poll in that order. Explain REST dot scopes separately from MCP colon scopes, same-key retry after an uncertain response, and the distinction between completed collection and assessment. The curated API reference adds only the safe GET; the write is explained in the guide and authenticated live schema. Source refresh shipped before the first-link workflow.

The released first-link workflow adds `mcp/link-source-clients` and `api-reference/link-source-clients` before source refresh in the task journey. Discover an existing generic PSA/RMM remote-company mapping, identify the existing Organization, use its short-lived caller-bound revision and one saved idempotency UUID to first-link only an unassigned record, then explicitly refresh the whole source if needed. `integration:map` is a new MCP scope backed by `integration.manage`; REST retains dot scopes. Keep Microsoft selection, arbitrary remapping/unlinking, historical-fact reassignment and automatic refresh outside this guide. The published catalogue includes 23 tools and 13 selected read operations, matching the verified 7aeec59 release. Use the authenticated live reference for deployment-specific availability.

The standards-authoring guide adds `mcp/copy-standard-draft` beside client management. Lead with the human meaning of the curated library, then list its exact revision, copy one disabled draft with a user-owned key and one idempotency UUID, inspect its current controls and manual checks through the bounded read tools, and finish in the signed-in review-and-enable workflow. Distinguish `standards:read`/`standards:copy` MCP scopes from REST dot scopes and the human-only enable action. A historical copy receipt does not claim the current standard is still disabled or present. The generated 27-tool catalogue is tied to the verified application release; deployment-specific availability is discoverable in the authenticated live reference.

The standards-authoring workflow starts with the curated library, copies one disabled draft using a user-owned key and one idempotency UUID, then inspects its current controls and manual checks through bounded read tools. Inspection and activation-preview responses include saved scope and assignment counts; MCP does not return assigned client IDs. The activation workflow adds a complete bounded policy preview and a separate `standards:activate` action for a receipt-backed draft. It requires workspace-wide acknowledgement only when the preview reports workspace scope; it does not evaluate controls, collect evidence or change a vendor. Existing client overrides remain in force, and the preview does not freeze the client roster. Distinguish MCP colon scopes from REST dot scopes and most human-only editing routes. Historical copy and activation receipts do not claim a standard's current state. Keep the generated catalogue tied to the matching deployed application source.

The next held headless evaluation candidate follows activation with a separate **one client, one enabled standard** task. Its REST and MCP guides lead from complete authored/effective policy preview to a user-owned-key request with a saved idempotency UUID, then an exact historical operation poll. It does not refresh evidence, assess manual checks or deploy a standard. `completed` does not mean pass, and `unknown` does not trigger automatic provider retry. The candidate catalogue has 32 tools and 16 selected REST reads against app `d65fc8a`; these are draft counts until matching release verification. The Developer Console link explains that Try it reaches the real workspace.


## Held Linear workspace shell and workflow copy

The current application redesign candidate keeps existing route identities and groups the left sidebar into daily work (**Overview**, **Issues**, **Reviews**, **Activity**), workspace work (**Clients**, **Standards**, **Integrations**) and management (**MCP**, **Settings**). The top-left workspace menu contains Workspace settings, Team members and Billing when permitted, followed by Account settings and Sign out for the personal account. Settings uses its own sidebar groups (Workspace, Access, Client services, Personal), with permission-dependent destinations and a search field. Do not infer workspace switching from the menu; no such capability is documented. Keep the product label **Issues**, not Inbox.

The Standards route keeps a compact searchable/state-filtered list and opens full details; **Create standard** enters the domain chooser, while library/run/blank actions are grouped under More. Its **← Standards** detail link carries the list search, state, page and page-size query parameters back to the list. The guided domain wizard remains Questions → Sources → Review, preserves browser drafts and uses inline connector creation with explicit return links from connection mapping. A guided save creates an active selected-client standard with no clients assigned; assignment and assessment remain separate. The Issues view uses compact search/filter/display controls, URL-backed filters/search/sort/page, and a persistent desktop detail pane with a narrow-screen return-to-list path. Public guides must match candidate source and remain held until the matching app release. Existing docs page routes and API/MCP catalogues are unchanged; the app navigation change does not itself require a docs.json navigation edit.

The held October 2 candidate reuses one connection-creation dialog across workspace setup provider cards, Standards Sources, Integrations, client import and connection entry points. Saving or adding another connection preserves the parent route and questionnaire draft. Microsoft setup first chooses Direct or Partner Center; save the method separately from provider authorisation.


## Setup refinement follow-up — 2 October 2026

The candidate setup refinement keeps the existing five steps and routes. Saved connection actions remain inline, Connect another tool opens the shared catalogue dialog, and Microsoft Setup guidance opens the method-specific help dialog. The optional staff directory opens from Use your Microsoft staff directory. Standards use compact domain rows; the completion screen keeps Overview and readiness separate. Standard Sources readouts use client names and focused requirement/gap dialogs. These layout changes do not alter evidence, authorisation, evaluation or assignment semantics.

The issue detail panel presents Properties before Evidence. Keep the triage guide focused on client, source, severity and observation times first; Source record opens the optional internal fact reference without placing UUIDs in the main reading flow.

## Connection health and recovery follow-up

The next workspace navigation places Connection health immediately below
Integrations, retaining the main shell. It is removed from the Settings workspace
list. Microsoft client entry separates Link Partner Center connection and Add
Microsoft connection; collection troubleshooting leads to Collection history and
View details. Existing public guide URLs stay stable; no docs.json change is needed.

## Compact assessment follow-up — 3 October 2026

Keep bulk assignment instructions with Standards, refresh scope and changed-target recovery with Maintain integrations, and end-of-row JSON inspection with Evidence. Setup header alignment and the Standards pointer affordance do not change the navigation or workflow.

## October 3 — Overview receipt and client workspace polish (held)

Keep Overview loading and saved-receipt checking distinct from current collection
progress. **Retry status** reads the accepted receipt again; uncertain request
reconciliation checks the original request before a new refresh. Client guidance
uses the current **Discovered domains**/**Manual domains** and **Client sites and
access** labels. Risk and manual-failure tables have separate filter menus; the
manual-failure menu filters standard and category. Explain pending saves only for
valid in-flight changes, and retain the draft after a rejected roadmap save.
These are app presentation/recovery details; do not claim successful-activity
semantics, Exchange coverage or a new scoped-run modal.
