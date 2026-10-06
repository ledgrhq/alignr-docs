# Overview assessment terminology and automatic reassessment — candidate, 5 October 2026

## Scope and source

This documentation candidate aligns the Overview metrics and retry with PR107
source `7ba12813`, merged as `70bbd36e` and present in current production source
`66433b34ae2838f5c048904c3eea291c3054c334`. It describes durable native-control
assessment requests in final PR108 head
`0ffbae16de981d34e716e8c92c0a686def841dec`, whose merge base is that same
production source. The affected public guides are
`guides/daily-review.mdx`, `guides/standards.mdx` and
`guides/workspace-health.mdx`.

Overview **Checks passing** is the pass share among current assessed checks;
**Assessment coverage** is the share of applicable checks with a current pass or
fail result. Coverage is not a run-progress indicator. When there are applicable
checks but no current results, Overview uses an em dash and says **No current
results**. Recorded issues are separate: an open issue can remain available for
investigation when evidence goes stale and the assessment no longer has a current
pass or fail.

The automatic-reassessment copy is intentionally limited to the implemented trigger
scope: real changes to a control definition, parameters or enabled state; the
standard's enabled state; effective client overrides; and standard assignment
changes. Cosmetic changes and no-op resends do not queue work. Work is asynchronous
with no promised completion time. It evaluates
existing eligible evidence and does not collect from vendors or complete manual
reviews. Missing or stale evidence remains unknown or uncovered. Assignment and
archive state are rechecked before evaluation, so a removed or archived client is
skipped. This refreshes native control evaluations only; recorded issue creation,
reuse, refutation or closure remains in the separate detection/Verifier workflow.
Connection-policy and catalogue-upgrade hooks remain separate follow-up work; this
copy does not promise reassessment after every workspace or source change.

## Verification and publication status

The UI terminology and bounded retry are source-checked against
`WorkspaceOverviewPage`. The reassessment scope and limitations are checked against
the final service, mutation hooks, worker registration, integration tests and
`vault/09-Delivery/Automatic Reassessment Trigger Candidate 2026-10-05.md` at the
PR108 head above. Its post-Fleet focused workflow
[`37505935404`](https://github.com/ledgrhq/ledgr/actions/runs/37505935404) passed the
ordered PostgreSQL migration/reassessment suite and claim-loss red/green proof. This
remains a documentation candidate: the matching application release, independent
docs review, publication and hosted readback are not yet complete.

No OpenAPI, MCP, predicate, seeded-control or template contract changes are involved.
Generated references therefore do not require regeneration. Docs build, link checks
and accessibility checks passed with Node `22.13.1` and workflow-pinned Mint
`4.2.939`. Local 1440px and 390px renders of all three affected pages showed the
expected text without horizontal overflow. Independent semantic review, matching
app release, publication and hosted readback remain pending.
