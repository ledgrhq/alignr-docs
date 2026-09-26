# Alignr documentation vault

This is the source of truth for **how the public docs are designed, written and maintained**. The application repository's vault remains authoritative for product behaviour and engineering decisions. This vault records documentation decisions; it does not redefine the product.

## Read at the start of every docs task

1. Read [Decisions](Decisions.md) before changing structure or presentation.
2. Read [Information architecture](Information%20Architecture.md) and [Editorial standards](Editorial%20Standards.md) for the affected journey or page type.
3. Follow [Maintenance workflow](Maintenance%20Workflow.md), including source checks and validation.
4. Review [Review log](Review%20Log.md) for known gaps and prior evidence.
5. Update the affected living notes and the review log in the same change. Add every new vault note to this index.

## Records

- [Decisions](Decisions.md) — accepted decisions, rationale and change policy.
- [Information architecture](Information%20Architecture.md) — readers, navigation and learning paths.
- [Editorial standards](Editorial%20Standards.md) — writing, examples, visuals and completion criteria.
- [Maintenance workflow](Maintenance%20Workflow.md) — source ownership, generators, publication and vault updates.
- [Review checklist](Review%20Checklist.md) — repeatable criteria for independent review and re-review.
- [Review log](Review%20Log.md) — verification, known gaps and next improvements.

## Coverage audit

- [Application documentation coverage](Documentation%20Coverage.md) — route reconciliation, prioritised backlog and completed corrections.
- [Daily operations evidence](Review%20Evidence/Daily%20Operations%20Audit.md).
- [Setup and integrations evidence](Review%20Evidence/Setup%20and%20Integrations%20Audit.md).
- [Assessments and sharing evidence](Review%20Evidence/Assessments%20and%20Sharing%20Audit.md).
- [API and MCP evidence](Review%20Evidence/API%20and%20MCP%20Audit.md).

- [Implementation review](Review%20Evidence/Implementation%20Review.md) — delivered gap coverage, independent review and verification limits.

## Publication boundary

`vault/` is excluded from Mintlify through `.mintignore`, together with agent instructions and maintainer scripts. Never add vault pages to public navigation or link to them from public MDX. This is a publication boundary, not a secret store: repository readers can still see these notes. Do not store credentials or customer data here.

Agents must consult these files when working; there is no background process that automatically reads or updates them. CI checks the index, exclusion rules and public links, while maintainers remain responsible for semantic accuracy.
