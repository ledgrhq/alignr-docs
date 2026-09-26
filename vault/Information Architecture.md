# Information architecture

## Readers and their jobs

- New MSP administrator: establish a source, map a client, choose expectations and explain a first result.
- Engineer: investigate a failure or coverage gap, adjust an expectation deliberately and verify the follow-up.
- Standard owner: choose a baseline, build a control, manage client exceptions and manual reviews.
- Developer or assistant user: obtain suitable credentials and use a supported API or MCP operation.

## Public navigation

Documentation contains Start here (Introduction, Quickstart, Your first assessment) and expandable groups for workspace setup, assessment concepts, controls, and help/reference. Controls contains the overview, baseline selection, recipes, category references, build/manage guides and advanced definitions.

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
