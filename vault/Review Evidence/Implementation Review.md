# Implementation review — 2026-09-26

## Coverage and source

Completed all thirteen gaps from the whole-app audit with 22 new task/reference pages and expanded remediation. Three implementation agents owned daily operations, assessments/sharing and vendor setup; the coordinator owned recovery, domains, standalone rules, API recipe, navigation and vault. Source inspection spans application revisions b844f92 through 41c08802 and concurrent current source; this is not a frozen production acceptance run.

All 38 connector declarations are represented with declared credential fields, mapping units, observations and limitations; eight unavailable entries remain distinct. Category pages use product accordions; UniFi and SonicWall have dedicated authentication-mode guides. Provider-console instructions were checked against official sources where given. Other entries describe Alignr's fields, not independently tested vendor provisioning.

## Independent corrections

- Domain target removal/disable immediately withdraws that source's observations; the guide now explains this.
- Generic integration deletion does not retract existing facts or immediately remove their contribution to results. Avoid claiming explicit queued-job cancellation.
- SonicWall SaaS discovers multiple tenants but collects the selected tenant; mappings cannot widen the credential scope.
- New standalone rules default enabled; drafting instructions explicitly disable them first. Standalone match/where detects a candidate violation, unlike control population/expect semantics.
- Portal individual-access setup has no current People & views editor. Document administrator/support prerequisite and retained backend route separately; do not direct readers to a filtered schema that hides that route.
- Risk-derived proposals require detection.read as well as roadmap.write.

## Verification

Fictional CSV accepted by the real import parser; missing header, empty input and over-limit rows rejected. Five standalone evaluator cases passed: enabled account/MFA false matches; true, absent MFA, disabled account and absent enabled observation do not. API Python example executed with mocked HTTP paging, mixed statuses and empty control grid, without external requests. Navigation existence/uniqueness checked. Desktop client-review layout and mobile expanded vendor instructions inspected. Final build, links, OpenAPI, accessibility and vault checks are recorded in Review Log.

## Product follow-ups and limits

Pax8 official third-party authentication requires delegated OAuth and prohibits sharing partner client credentials; the current connector uses client_credentials. Public guides warn against bypassing this contract. Application onboarding needs resolution before this path can be endorsed. Source: https://devx.pax8.com/docs/authentication.

Huntress's new user-based credential compatibility with the current API v1 connector remains unverified. ConnectSecure discovery requires per-pod validation. Portal individual access requires administrator/support setup until the app exposes the editor.

No authenticated customer workflow, vendor collection, password reset email, invitation, portal sign-in or production API/MCP session was exercised. No application behaviour changed and no full application test-suite pass is claimed. AWS/ClickHouse infrastructure remains outside this documentation release.
