# Alignr docs

Public setup, API and MCP documentation for **docs.alignr.io**, hosted by Mintlify.
This repository is separate from the Alignr application and its internal vault.

## Preview

Use Node 22 or newer supported LTS and the current `mint` CLI:

```sh
npm install -g mint@4.2.939
mint dev
```

## Check

```sh
mint broken-links
mint openapi-check api-reference/openapi.json
mint validate
```

## Regenerate reference

From the application checkout, run the generator using its installed Python environment:

```sh
PYTHONPATH=api api/.venv/bin/python /path/to/alignr-docs/scripts/sync-reference.py
```

The generator imports application metadata without starting its lifespan or querying data.
It publishes an explicit selection of read endpoints and the registered MCP tool signatures.
Review the snapshot against the intended release before committing. The authenticated live
schema remains authoritative for deployment-specific availability. No private API credentials
are needed for generation or hosting. API playground execution is disabled; examples remain copyable.

## Publish

Mintlify is connected to this repository. Push reviewed changes to its configured deployment
branch. Configure `docs.alignr.io` in the Mintlify dashboard and use the exact DNS record it
provides. Confirm HTTPS, redirects and a nested guide after DNS resolves.

The design uses Almond, Inter, a monochrome palette and Alignr's blue icon. It matches the
Resend reference through native theme settings rather than copied page code or assets.

## Reference provenance

Initial reference generated on 26 September 2026 from application commit
`19794f3bfafdd3fbc8e79cfd115980e342b2401e`. The application checkout had unrelated
operational vault changes; no application source was changed by this docs work.
Ten read endpoints and ten MCP tools are included. Responses whose backend schema
is an untyped object remain untyped here; do not invent response fields.

Local browser review covered the introduction at desktop and 390px mobile,
the MCP catalogue and an API endpoint page. Mobile introduction document width
matched the viewport (390px). Production search indexing, domain configuration
and authenticated API/MCP requests require hosted acceptance.
