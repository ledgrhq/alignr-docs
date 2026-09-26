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

## Continuing after the first result

Daily review → triage → supported remediation or client review → risk/roadmap → fixed report or authorised portal sharing. Vendor setup is grouped by category with per-product accordions; UniFi and SonicWall have dedicated mode guides. Keep API recipes in the developer tab and link them from task guidance.

## Buyer and account-manager journeys

The pilot guide in Start here establishes evidence-based evaluation checkpoints without promising trial terms or ROI. The client-meeting playbook joins reviews, risks, reports, portal responses and verification. Keep suggested operating practices distinct from app features.
