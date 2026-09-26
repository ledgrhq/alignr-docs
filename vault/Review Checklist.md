# Repeatable documentation review

Use this checklist for a review loop. Record the scope and findings in Review Log, fix confirmed issues, then have the relevant changes read again before publication. Do not add pages or diagrams solely to make the diff larger.

| ID | Property to check | Evidence to record |
| --- | --- | --- |
| DOC-R01 | A new reader can choose the right starting point. | Trace Introduction through the intended task; distinguish app setup, assessment and developer paths. |
| DOC-R02 | Every instructed action exists and is reachable. | Compare exact UI labels, permissions, preconditions and disabled states with current source or authorised runtime. |
| DOC-R03 | Milestones are distinct. | Check import, mapping, collection, standard activation, evaluation, manual review and remediation are not conflated. |
| DOC-R04 | Success and recovery are observable. | Each workflow has a checkpoint; failures and partial outcomes lead to a specific investigation. |
| DOC-R05 | Examples preserve evidence semantics. | Test true/false/missing, empty population, boundary values and effective overrides where relevant. |
| DOC-R06 | Diagrams explain a real relationship. | Compare arrows and labels with behaviour; inspect desktop/mobile rendering and adjacent prose. Avoid invented automatic transitions. |
| DOC-R07 | Handoffs survive selective reading. | Follow next links without opening optional tabs; introduce example names and prerequisites where needed. |
| DOC-R08 | Navigation and publication boundaries hold. | Run build/link/vault checks; inspect changed hosted routes, and exclusions when they change. |

## Closing a loop

For each finding, record the source/page, why it blocks or misleads a reader, the fix and re-review outcome. Distinguish source inspection, local docs browser checks, live published-page checks and authenticated app acceptance. None substitutes for another. Record unresolved issues rather than describing an incomplete check as passing.

Keep the review bounded to meaningful user tasks. Future loops should start from new user friction, source changes or the remaining improvements in Review Log.
