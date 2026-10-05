# Overview assessment terminology and automatic reassessment — candidate, 5 October 2026

## Scope and source

This documentation candidate aligns the Overview metrics with app source
`4f9b8597d6fb717eaa644b4edca787b38595a284` and describes the proposed durable
assessment requests in the application candidate
`feat/automatic-control-reassessment`. The affected public guides are
`guides/daily-review.mdx`, `guides/standards.mdx` and
`guides/workspace-health.mdx`.

Overview **Checks passing** is the pass share among current assessed checks;
**Assessment coverage** is the share of applicable checks with a current pass or
fail result. Coverage is not a run-progress indicator. When there are applicable
checks but no current results, Overview uses an em dash and says **No current
results**. Recorded issues are separate: an open issue can remain available for
investigation when evidence goes stale and the assessment no longer has a current
pass or fail.

The automatic-reassessment copy is intentionally limited to the proposed trigger
scope: supported changes to standard/control definition, parameters or enabled
state; standard activation; effective client overrides; and standard assignment
changes. Work is asynchronous with no promised completion time. It evaluates
existing eligible evidence and does not collect from vendors or complete manual
reviews. Missing or stale evidence remains unknown or uncovered. Connection-policy
and catalogue-upgrade hooks remain separate follow-up work; this copy does not
promise reassessment after every workspace or source change.

## Verification and publication status

The UI terminology is source-checked against the Overview component. The
reassessment scope and limitations are source-checked against the application
candidate note `vault/09-Delivery/Automatic Reassessment Trigger Candidate
2026-10-05.md`. This is a draft on a separate docs branch based on held PR38; PR38
was not edited. The app implementation, migration, database tests, queue operation
and production behavior are not yet accepted. Therefore the reassessment wording
is a documentation candidate only, not a statement that the feature is shipped.

No OpenAPI, MCP, predicate or control catalogue changes are involved. No generated
references require regeneration. Docs build, link checks, mobile/desktop render,
independent semantic review, matching app release and publication remain pending.
