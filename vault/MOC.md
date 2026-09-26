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
- [Review log](Review%20Log.md) — verification, known gaps and next improvements.

## Publication boundary

`vault/` is excluded from Mintlify through `.mintignore`, together with agent instructions and maintainer scripts. Never add vault pages to public navigation or link to them from public MDX. This is a publication boundary, not a secret store: repository readers can still see these notes. Do not store credentials or customer data here.

Agents must consult these files when working; there is no background process that automatically reads or updates them. CI checks the index, exclusion rules and public links, while maintainers remain responsible for semantic accuracy.
