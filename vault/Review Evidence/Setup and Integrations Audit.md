# Setup, integrations and client-configuration documentation audit

Scope: read-only source audit against docs commit `0bf7785de4d97ac9f8a759bb9626d837fa4feeca`; application HEAD `565fae53f166e14dae4f3d872572ab3e3bdfdc28`. Reviewed current router, not merely existing components. Excluded the uncommitted quickstart/integrations/MCP additions from the published baseline. Standards: DOC-R01–04/R07, REV-001/002, LOG-011/012. No runtime/vendor acceptance performed. No claim of complete security or live connector testing.

## Main findings

| Priority | User task / current route | Confirmed documentation gap | Source evidence | Proposed docs / acceptance |
|---|---|---|---|---|
| P1 | Choose and prepare an integration, `/integrations` | Published docs contain one generic connection page and detailed Microsoft guidance, but no complete offered-connector catalogue or vendor-specific prerequisites. A reader cannot determine credential kind, supported capabilities, matching unit or constraints before opening a form. | `api/ledgr/integrations/catalogue.py:72–333`; `frontend/src/features/integrations/AddIntegrationDrawer.tsx:115–145,452` uses each connector's credentialFields. | Integration index grouped by user job, then source-backed vendor pages covering prerequisites, exact fields, scope, mapping, first collection and omissions. Start PSA/RMM/identity/network/backups. Do not call code presence production certification. |
| P1 | Connect mode-sensitive network products | Generic advice hides materially different authentication/endpoints. UniFi remote and local require different keys; SonicWall mode selects different credentials/destinations. | `api/ledgr/integrations/unifi_network.py:180–211,240,287–310`; `sonicwall_nsm.py:372–418,463`. | Dedicated mode decision guides, exact field tables and wrong-mode troubleshooting. Any vendor-console click instructions need current official vendor verification. |
| P1 | Rotate credentials or move an integration destination, `/integrations/:id` → Edit | Reconnect prose exists, but the required whole-bundle replacement rule is undocumented. Leaving fields blank keeps credentials; changing credential/destination requires every required field, not just the changed secret. | `frontend/src/features/integrations/EditIntegrationDrawer.tsx:169–184` (rule displayed by form); detail Edit action at359. | Add maintenance guide with rotation steps, successful connection/collection checkpoint, and error recovery. Explain that secrets are not displayed after save. |
| P1 | Recover forgotten password or failed second-factor sign-in, `/forgot-password`, `/reset-password`, `/login` | Account guide covers authenticator registration and administrator replacement passwords, but not the routed self-service reset flow or failed login-key challenge. | `frontend/src/router.tsx:66–67`; `frontend/src/features/login/LoginPage.tsx:107`; `ResetPasswordPage.tsx:16–52`; `Login2faStep.tsx:49–67,129–135`. | Add sign-in/recovery section with reset-request privacy response, token expiry/used handling, minimum password, and expired-challenge restart versus retry. Verify backend expiry/session revocation before documenting exact values. |
| P2 | Remove an obsolete source, `/integrations/:id` → Delete | No guide explains consequences: scheduled syncs stop and mappings are removed, but prior facts remain; directory-only deletion leaves existing clients. | `frontend/src/features/integrations/IntegrationDetailPage.tsx:427–434`. | Include retiring/replacing a source in integration maintenance. Preserve history distinction and require checking affected client coverage. This audit did not execute deletion. |
| P2 | Operate client DNS checks, `/organizations/:id?tab=domains` | Configure-client has a good starter section, but omits 50-domain limit, inclusion/exclusion recovery, scheduler states and immediate check versus automatic scheduling. | `frontend/src/features/domain-checks/ClientDomainsTab.tsx:92–107,112,122–126`. | Dedicated domains guide with saved-target checkpoint, scheduled/paused scheduler branches, >50-domain recovery, source discovery versus manual domains, resulting predicate limits. |
| P2 | Understand catalogue-unavailable products | No public searchable availability reference. Eight catalogue entries are explicitly unavailable, not promised roadmap dates. | `api/ledgr/integrations/catalogue.py:56–68,381–650`; picker unavailable explanation `AddIntegrationDrawer.tsx:396`. | Put concise unavailable status in integration index. Do not publish speculative delivery dates or copy internal vendor assessments as current fact without checking. |
| P2 | Configure non-Microsoft source associations per client | Current configure-client guide covers Link site and named connections, but deeper operational questions (already assigned elsewhere, multi-instance products, deletion/move effects) are only scattered across mapping page. | `frontend/src/features/client-connections/ClientConnectionsTab.tsx:181–213,291–323,367–415`; detail mapping correction at`IntegrationDetailPage.tsx:602–651,725`. | Add concise decision links under Connections: link new, inspect assigned, correct wrong client, replace source. No invented general source-priority editor. |

## Offered integration inventory

Canonical source declares **38 connector-backed types**, including 2 directory-only; plus **8 unavailable catalogue types**. This is implementation availability, not evidence that every provider is operational in the deployed workspace.

| Group | Connector-backed codes / products |
|---|---|
| Built-in DNS | external_dns — Alignr Domain Checks |
| Microsoft identity/device | microsoft_partner_graph — delegated Microsoft 365; entra — Microsoft 365 / Entra ID; intune — Microsoft Intune; cipp — CIPP |
| Client directories only | itglue — IT Glue; hudu — Hudu |
| Other identity | duo — Duo; google_workspace — Google Workspace; keeper_msp — Keeper MSP; jumpcloud — JumpCloud |
| PSA | halopsa — HaloPSA; connectwise_manage — ConnectWise Manage; autotask — Autotask |
| RMM | datto_rmm — Datto RMM; ninjaone — NinjaOne; ncentral — N-central; syncro — Syncro |
| EDR | sentinelone — SentinelOne; huntress — Huntress; crowdstrike — CrowdStrike Falcon |
| Vulnerability | connectsecure — ConnectSecure; tenable — Tenable VM |
| Network | unifi_network — UniFi; sonicwall_nsm — SonicWall NSM; cisco_meraki — Meraki; auvik — Auvik; fortigate — FortiGate; twingate — Twingate |
| Backup | veeam — Veeam; acronis — Acronis Cyber Protect Cloud |
| Configuration monitoring | liongard — Liongard |
| Email security | mimecast — Mimecast; proofpoint_essentials — Proofpoint Essentials |
| Licensing | pax8 — Pax8; partner_center — Microsoft Partner Center; ingram_micro — Ingram Micro; cloudblue_connect — CloudBlue Connect |

Unavailable: tdsynnex_streamone, sherweb, datto_bcdr, inforcer, domotz, atera, dropsuite, datto_saas. Source line anchors respectively381,426,450,489,527,567,606,642.

Connection axes must stay separate: LIVE versus SIMULATED is evidence provenance; directory-only versus evidence-source is function; Direct versus Partner is Microsoft route; UniFi local/remote and SonicWall provider modes select authentication/endpoints. Do not collapse all of these into one generic 'mode' promise.

Specific credential examples source-backed for first vendor guides: Datto RMM API key/API secret plus endpoint (`datto_rmm.py:93`); Autotask integration code/API username/API secret (`autotask.py:243`); Google Workspace credential/delegation details (`google_workspace.py:289`); UniFi and SonicWall mode fields as above. Exact vendor permission grants and administrative UI paths need independent official-doc verification before publication.

## Already covered / no new broad rewrite needed

Published setup-wizard, settings, account-and-team, configure-client and client-microsoft-connections give substantially complete navigation for their documented tasks. Microsoft method precedence, direct exception for non-GDAP clients, partner-account selection, Intune limitation, immediate-save client approval limits, invitation permissions and portal separation are explicitly covered. Remaining improvement should deepen missing tasks rather than duplicate those pages.

## Retired and unavailable boundaries

- `frontend/src/router.tsx:29,99` routes client details to `alignment/ClientPage`, aliased as OrganizationDetailPage. The old `organization-detail/OrganizationDetailPage.tsx` and its EditOrganizationDrawer are not the current route. Do not advertise general profile editing/archiving from that retired screen. Published configure-client correctly says no general Edit client form.
- `settings/` is an index; Account Tenancy details are displayed, not an all-purpose workspace editor. Do not invent billing/residency switches.
- No general client source-priority/default editor was found in the current ClientConnectionsTab. Microsoft's explicit policy is documented; future generic selection design is not a current workflow.
- Unavailable catalogue products are not upcoming integrations with a date. Client-directory IT Glue/Hudu support is not asset/document migration.
- Portal policies and named views are covered in existing settings/configure-client, but full portal audience/approval audit belongs to the portal reviewer.

## Limits

Source-only review proves reachable components and documentation omissions. It does not prove deployment flags, usable credentials, vendor permissions, scheduled collection, email delivery, password-reset inbox arrival or browser UX. No external write, no tests and no source/public docs edits were performed. This report is the only written artefact.
