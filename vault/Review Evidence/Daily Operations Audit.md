# Daily operations documentation audit

Scope: current routed frontend Overview, Issues, remediation/approvals/activity/logs, Ask rail, navigation/search/notifications. Read-only app and public docs review; only this report written. Docs inspected at committed HEAD `0bf7785de4d97ac9f8a759bb9626d837fa4feeca`; app HEAD `565fae53f166e14dae4f3d872572ab3e3bdfdc28` plus its current working tree (not a claim of deployed behaviour). Review baseline v1.1 REV-001/002 and documentation DOC-R01–04/07, source inspection only. No vendor actions or authenticated acceptance tests.

## Findings, ordered by reader impact

### DAILY-01 — P1: no executable issue-triage guide

User task: investigate an open issue, park it with a reason, or dismiss a supported false positive without mistaking either for a verified fix.

Route: `/detections`, top navigation **Issues**.

Evidence: `frontend/src/features/detections/DetectionsPage.tsx:29` offers Open/Snoozed/Resolved/Dismissed; `DetectionPanel.tsx:172` onwards shows status/subject/evidence/plan, `:365` supplies Snooze/Re-snooze and Dismiss; `TriageDialog.tsx:20` offers Tomorrow/1 week/2 weeks/30/90 days, `:29` explains lifecycle and required reasons. `api/ledgr/detection/engine.py:521` and `:697` suppress reraising snoozed/dismissed findings. `api/ledgr/services/detections_service.py:306` refuses dismissing already closed findings.

Committed docs have no snooze/dismiss instruction at all (`git grep` across HEAD MDX). `journeys/close-the-loop` remains conceptual. This leaves the primary operational queue undocumented, particularly the materially different effect of dismissal.

Proposed: `guides/triage-issues`: entry/filter/context → open evidence → compare finding to control result → choose supported remediation vs Snooze vs Dismiss → required reason → recover parked/closed records through Status and audit trail. State detection.read vs detection.write; do not promise a reopen action without source confirmation.

### DAILY-02 — P1: remediation guide lacks approval queue and exact execution handoffs

User task: move an issue from proposed fix through pending approval to reviewed result, and find supported rollback.

Routes: issue side panel → `/approvals` and `/remediations`, reached through **Activity → Approvals / Fix history**.

Evidence: `ActivityPage.tsx:7–10` provides permission-gated entry points. `DetectionPanel.tsx:335` shows primary supported action or Verification pending with blocked reason. `ApprovalsPage.tsx:25` contains Pending/Approved/Declined/All and :120 Review/View. `ApprovalDetailDrawer.tsx:143–147` supplies Decline/Approve; :246–248 confirms **Approve & run**; :167 says Approved — run enqueued. `approvalPermissions.ts:19–40` requires remediation.approve and refuses self-approval (own request can be declined). `api/ledgr/services/approvals_service.py:167` enqueues approved run. `RemediationsPage.tsx:196–199` distinguishes run status and verification, :230–238 uses server rollback eligibility, :319 confirmation. `remediation.read`, `approval.read`, `remediation.rollback` gate related UI.

`guides/remediation.mdx` correctly explains plans/runs, effective ceiling, verification and uncertainty, but supplies no UI entry point, approval step, separation of requester/approver, filters or rollback action. Its Change ticket summary is insufficient to operate the actual in-app queue and could be read as requiring an external ticket workflow.

Proposed: expand current guide with linked **Request a supported fix**, **Decide an approval**, **Read fix history / Roll back** sections. Preserve conceptual content. Explain queued is not executed; executed is not verified; simulated is not a live change. Do not invent an explicit Verify button (none found on run list).

### DAILY-03 — P1: Ask Alignr's reviewed configuration changes are undiscoverable in docs

User task: ask about evidence for the selected client/standard, review an exact configuration draft and apply it deliberately.

Surface: **Ask Alignr** header button and persistent rail; no `/ask` route.

Evidence: `AlignmentShell.tsx:32` gates ask.use and :45 mounts header trigger. `AlignmentAssistant.tsx:20` has evidence questions; :57–66 writer prompts; :136 composer. :193–205 resolves explicit client-page/filter scope before global selection and labels scope; :206–209 resets conversation on client/standard change. `StandardChangeCard.tsx:18–29` displays Before/After, Apply change/Dismiss and requires ask.use + detection_rule.write; :24 explicitly requires fresh assessment after configuration. `useStandardChanges.ts:18–32` applies token and requires a fresh draft after uncertain/error response rather than blind replay.

Committed docs contain no **Ask Alignr** guide; MCP material describes a different client interface and cannot substitute.

Proposed: `guides/ask-alignr`: open rail, inspect scope chips, example read-only question, inspect cited evidence, draft/configuration vs execution distinction, Before/After review, Apply change, View configuration, reassess. Include missing permission and stale/uncertain draft recovery. Avoid describing old AskPage conversation management unless reachable rail exposes it.

### DAILY-04 — P2: no day-to-day Overview interpretation or Refresh evidence task

User task: decide the first action each day and understand why a high live alignment percentage can coexist with incomplete coverage.

Route: `/`, **Overview**.

Evidence: `AlignmentPage.tsx:26–30` dashboard.read and sweep.execute+sweep.read; :57 Refresh evidence; :62 Next step; :70–90 Live alignment / Checks completed / Open issues / Fix history; :98 Needs attention; :102 Tool health explicitly workspace-wide. `overview/RunDiscovery.tsx:32` posts `/sweeps` without organization_id and :54–69 follows its terminal state/per-source outcomes.

Committed control-status and workspace-health guides cover evidence semantics well, but there is no Overview score/denominator explanation or Refresh evidence instruction (`git grep HEAD`). Do not imply the org switcher scopes this global sweep.

Proposed: `guides/daily-review` or introduction-linked **Start your day** section: Next step → scores plus coverage → selected-client checks → issues → workspace health. Explain Refresh evidence vs Run checks, sweep scope and per-source outcome/retry investigation.

### DAILY-05 — P2: Activity/Audit trail recovery task absent

User task: find who changed a setting or triaged a finding; export the matching trail for a handover.

Routes: `/activity` → **Audit trail** `/logs`; closed issue panel links filtered audit.

Evidence: `ActivityPage.tsx:9–10` audit.read; `DetectionPanel.tsx:323–326` Resolved/Dismissed — view audit trail with record filters. `LogsPage.tsx:97` resets pagination when filters change; :141–156 CSV uses current URL filters without pagination; :247 Export filtered CSV/Export CSV; :268–325 Actor kind/Action/Record type/Record id/From/To.

Committed docs mention audit abstractly but lack the operational inspection/export path.

Proposed: add **Activity and audit trail** section linked from triage/remediation. Explain safe filtered URL sharing to authorised colleagues, reviewing record context and export scope. Check export permission/cap before publishing exact limits (not fully inspected in this pass).

### DAILY-06 — P2: app navigation/scope and search not taught

User task: jump to an issue/client and avoid confusing selected-client data with workspace settings.

Evidence: `alignment/navigation.ts:5–17` separates daily vs workspace destinations; `AlignmentShell.tsx:35–60` desktop/mobile navigation, switcher, docs/help and account menu. `components/ui/SearchCommand.tsx:42–57` Ctrl/Cmd+K; :87–98 searches organizations/detections after two characters; :75–80 page shortcuts permission-filtered. `AlignmentAssistant.tsx:193–205` explicit route/filter scope supersedes global selector.

Introduction documents *docs* navigation, not app navigation; that is appropriate but leaves this app-user task uncovered. Proposed a compact **Find your way around Alignr** section on daily-review, with keyboard search, Clients/Issues/Reviews/Activity vs workspace settings, scope cues and permission-hidden links. Do not claim app search searches every entity or docs content.

## Complete assigned surface inventory

| Surface | Current reachability | Existing docs coverage / disposition |
| --- | --- | --- |
| Overview `/` | Active, dashboard.read | Partial semantics in control-status and health; DAILY-04 |
| Issues `/detections` + detail rail | Active, detection.read; triage detection.write | Conceptual result/remediation pages only; DAILY-01 |
| Remediation confirmation modal and `/remediations` | Active through Issues and Activity/Fix history | Concepts accurate, task steps missing; DAILY-02 |
| Approvals `/approvals` | Active through Activity; approval.read | No queue instructions; DAILY-02 |
| Activity `/activity` | Active primary nav | No guide; DAILY-02/05 |
| Audit `/logs` | Active through Activity / closed issue | No task guide; DAILY-05 |
| Ask Alignr rail | Active shell, ask.use | Undocumented; DAILY-03 |
| Legacy `features/ask/AskPage.tsx` | Not imported/routed by current router | Do not publish as current page; rail is canonical |
| Agents standalone management | No `/agents` route in current router | No standalone agent-UI guide needed; explain relevant actions in their existing surfaces |
| Search command palette | Active shell | Undocumented app keyboard/navigation task; DAILY-06 |
| Notification inbox/preferences | No current route or shell bell/inbox found | Do not invent one. Current notifications are toast messages and operational-health banner |
| Operational health banner | Active shell, `operations/OperationalNotice.tsx:16` | Workspace-health guide covers underlying warnings adequately; optional navigation cross-link |
| Desktop/mobile/account navigation | Active shell | Account guide covers destination but not app-wide wayfinding; DAILY-06 |
| Old `features/overview/OverviewPage.tsx` | Not current routed Overview | Avoid its old page labels; router aliases AlignmentPage |

## Limits

Source-backed documentation audit only. No full security or backend behaviour audit, no authenticated live UI, no external vendor/queue execution, no runtime tests in this pass. Source and UI confirmation of exact low-level remediation/CSV service limits remains required before adding detailed instructions. No hard false statement discovered in the assigned committed pages; primary findings are substantial missing workflows around already reachable functionality. Health, result semantics and conceptual remediation are useful existing foundations rather than material to rewrite wholesale.
