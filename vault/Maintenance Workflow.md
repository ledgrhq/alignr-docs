# Maintenance workflow

## Before editing

Read AGENTS.md, this vault's MOC and relevant decisions. Check branch and working changes in both docs and application checkouts; claim files and preserve concurrent work. Consult the application's vault for product decisions and source code for current implementation. Never make product decisions by changing public copy.

Reconcile affected routes, shell actions, connector modes and developer scopes with [Application documentation coverage](Documentation%20Coverage.md). Update its linked guide and remaining-gap status when closing a task; preserve dated audit evidence.

## Change impact

| Change | Update together |
| --- | --- |
| Navigation or audience journey | docs.json, Introduction, Information Architecture and affected next-step links |
| Theme or components | Public layouts, Editorial Standards and a decision if policy changes |
| Predicates or producer semantics | Human predicate data, generated reference, examples, diagrams and affected controls |
| Baselines/templates/manual checks | Control generator/reference, overview counts, recipes, source limitations and guided examples |
| API/MCP contracts | Curated generator output plus setup/authentication/error prose |
| Setup, account, settings or Microsoft connection behaviour | Wizard, settings directory, account/team guide, health guide and client connection instructions; check actual labels, permissions, selection precedence and completion signals |
| Learning example | Worked data, evaluator checks, links and Editorial Standards if conventions change |

Update the relevant living note in the same change. Append a numbered decision when changing an accepted principle. Add new notes to MOC. Record the implementation commit, source revision, checks, publication and remaining gaps in Review Log.

## Regeneration

From the application checkout with its dependencies:

```sh
PYTHONPATH=api api/.venv/bin/python /path/to/alignr-docs/scripts/build-control-reference.py /path/to/ledgr
PYTHONPATH=api api/.venv/bin/python /path/to/alignr-docs/scripts/sync-reference.py
```

From the docs checkout:

```sh
python3 scripts/build-predicate-reference.py /path/to/ledgr
```

Regenerate only affected references. Review against the intended release and inspect the diff. Never query production tenant records to generate references. The predicate/control catalogues combine source metadata with human interpretation; regeneration does not rewrite the surrounding guides.

## Review loops

Use [Review Checklist](Review%20Checklist.md) to review the affected user task, fix confirmed issues, and re-review the changes. Record both passes in Review Log. Check setup against real UI labels and preconditions; a valid Markdown build does not establish a usable workflow.

## Validation and publication

Use Node 22 and mint@4.2.939, matching the workflow and README:

```sh
python3 scripts/check-docs-vault.py
mint broken-links
mint openapi-check api-reference/openapi.json
mint a11y
mint validate
git diff --check
```

Preview changed journeys at desktop and 390px mobile widths. Test tabs, expandable navigation and deep links. For evaluator examples, use the application's pure evaluator with fictional records; report this separately from live application acceptance.

Publishing main triggers Mintlify. Confirm GitHub validation and Mintlify deployment for the intended commit, then inspect changed hosted URLs. When changing exclusions, verify vault URLs are unavailable and public indexing contains no vault entries. `.mintignore` prevents publication; repository visibility remains separate.

The application repository has its own Public Documentation Maintenance guide. Keep its pointer to this vault current, but keep detailed docs design governance here to avoid competing copies.

## Operational workflow coverage

Changes to review queues, reports, portal permissions, risk decisions, roadmap delivery, Ask drafts, recovery or domain lifecycle must update their task guides and Documentation Coverage. Connector changes require checking the catalogue, category credentials/mapping/observations, dedicated mode guides and maintenance consequences. Recheck provider contracts separately from local implementation: Pax8 delegated OAuth, Huntress credential compatibility and ConnectSecure pod discovery remain explicit follow-ups. Never convert implementation presence into a production acceptance claim.
