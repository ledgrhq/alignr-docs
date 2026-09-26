"""Run with Alignr's Python environment and PYTHONPATH pointing to its api directory.

Imports the application without starting its lifespan, querying data or calling vendors.
Publishes an explicit read-only endpoint selection, never the whole internal schema.
"""
from copy import deepcopy
import inspect
import json
from pathlib import Path
from ledgr.main import app
from ledgr.api.v1.developer import _api_routes, _permission_for_route
from ledgr.core.scopes import MCP_TOOL_SCOPES
from ledgr.mcp import server

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'Organizations': [('/organizations', 'List Organizations'), ('/organizations/{organization_id}', 'Get an Organization')],
    'Standards': [('/standards', 'List standards'), ('/standards/{standard_id}', 'Get a standard'), ('/standards/{standard_id}/controls', 'List controls')],
    'Alignment': [('/organizations/{organization_id}/compliance', 'Get client compliance'), ('/organizations/{organization_id}/compliance/trend', 'Get compliance trend')],
    'Detections': [('/detections', 'List detections'), ('/detections/{detection_id}', 'Get a detection')],
    'Evidence': [('/facts', 'List facts')],
    'Billing': [('/billing/estimate', 'Get a billing estimate')],
}
schema = app.openapi()
permissions = {path: _permission_for_route(route) for path, route in _api_routes(app.routes) if 'GET' in route.methods}
paths = {}
for group, endpoints in GROUPS.items():
    for suffix, title in endpoints:
        path = '/api/v1' + suffix
        operation = deepcopy(schema['paths'][path]['get'])
        permission = permissions[path]
        if not permission:
            raise ValueError(f'Expected an explicit permission for {path}')
        operation.update(summary=title, tags=[group], security=[{'BearerAuth': []}])
        operation['description'] = f'Requires `{permission}`. Results are scoped to the authenticated tenant. This reference is generated from source; consult the authenticated live schema for deployment-specific availability.'
        if suffix == '/billing/estimate':
            operation['description'] += ' Optional USD pre-tax catalogue estimate only. Uses this tenant’s non-archived Organization count with a minimum billable quantity of ten; it does not create a checkout, subscription, invoice or charge. Annual commitment terms are arranged separately.'
            operation['responses'].update({
                '403': {'description': 'The actor does not hold billing.read.'},
                '409': {'description': 'Billing is not configured, or the client count needs a tailored estimate.'},
                '429': {'description': 'The estimate request rate limit was reached.'},
                '503': {'description': 'The provider estimate is temporarily unavailable; no amount is returned.'},
            })
        operation['x-ledgr-permission'] = permission
        paths[path] = {'get': operation}
# Include only components reached by selected operations.
components = {'securitySchemes': {'BearerAuth': {'type': 'http', 'scheme': 'bearer', 'description': 'An Alignr API key.'}}}
pending = [paths]
seen = set()
while pending:
    node = pending.pop()
    if isinstance(node, dict):
        ref = node.get('$ref')
        if ref and ref not in seen:
            seen.add(ref)
            _, _, category, name = ref.split('/')
            value = deepcopy(schema['components'][category][name])
            components.setdefault(category, {})[name] = value
            pending.append(value)
        pending.extend(node.values())
    elif isinstance(node, list):
        pending.extend(node)
spec = {'openapi': schema['openapi'], 'info': {'title': 'Alignr API', 'version': schema['info']['version'], 'description': 'Selected read operations. Generated from the Alignr application; no tenant data is included.'}, 'servers': [{'url': 'https://api.alignr.io'}], 'paths': paths, 'components': components}
(ROOT/'api-reference/openapi.json').write_text(json.dumps(spec, indent=2)+'\n')
config = json.loads((ROOT/'docs.json').read_text())
api_tab = next(tab for tab in config['navigation']['tabs'] if tab['tab'] == 'API reference')
api_tab['groups'] = [group for group in api_tab['groups'] if 'openapi' not in group] + [{'group': group, 'openapi':'/api-reference/openapi.json','pages':['GET /api/v1'+suffix for suffix,_ in endpoints]} for group,endpoints in GROUPS.items()]
# Keep examples copyable without a hosted proxy accepting production credentials.
config['api'] = {'playground': {'display': 'none'}}
(ROOT/'docs.json').write_text(json.dumps(config,indent=2)+'\n')
# Human explanations complement generated names, scopes and defaults.
TOOL_GROUPS = {
    'Client context': [('get_organization', 'Get an Organization'), ('list_organizations', 'List clients'), ('get_asset', 'Get an asset')],
    'Client actions': [('create_organization', 'Create a client'), ('update_organization', 'Update a client')],
    'Control results': [('get_organization_compliance', 'Read client control results'), ('explain_control_status', 'Explain a control result'), ('list_organizations_by_control_status', 'Find clients by control status'), ('get_standard_rollup', 'Review a standard across clients')],
    'Findings': [('list_detections', 'List detections'), ('create_detection_note', 'Add a detection note')],
    'Remediation reads': [('get_remediation_plan_outline', 'Get remediation plan outline'), ('list_remediation_runs', 'List remediation runs'), ('get_remediation_run_status', 'Get remediation run status')],
    'Search and questions': [('search_documentation', 'Search indexed content'), ('ask_ledgr', 'Ask an evidence-backed question')],
}
ARGUMENT_HELP = {
    'organization_id': 'Organization UUID.',
    'name': 'Client display name, 1–200 characters.',
    'slug': 'Unique client slug, 1–200 characters. Record it before creation so an uncertain result can be looked up.',
    'seats': 'Non-negative integer seat count (up to 2,147,483,647).',
    'psa_ref': 'Optional PSA client reference, up to 200 characters.',
    'clear_psa_ref': 'Set true to remove the current PSA reference; do not also supply `psa_ref`.',
    'offset': 'Zero-based offset for the next bounded client page.',
    'q': 'Optional name or slug search, up to 200 characters.',
    'asset_id': 'UUID of the asset to retrieve.',
    'query': 'Text to search for.',
    'question': 'The question you want answered from available evidence.',
    'limit': 'Maximum number of results requested.',
    'control': 'Control UUID, name, or case-insensitive substring of its name or slug.',
    'standard': 'Standard UUID, name, or case-insensitive substring of its name or slug.',
    'status': 'Status to filter by; the default is shown below.',
    'detection_ref': 'Reference identifying the detection to annotate.',
    'run_id': 'Remediation run UUID. A run outside your workspace returns not found.',
    'plan_id': 'Remediation plan UUID. A plan outside your workspace returns not found.',
    'note': 'Text to add to the detection.',
}
ordered_tools = [name for group in TOOL_GROUPS.values() for name, _ in group]
registry = {spec.tool: spec for spec in MCP_TOOL_SCOPES.values()}
if set(ordered_tools) != set(registry):
    raise ValueError('Update TOOL_GROUPS when the MCP registry changes')
lines = ['---', 'title: "MCP tools"', 'description: "Choose a tool by task, then check its arguments and required scope."', '---', '', 'Use this catalogue to choose the tool for your question. Names, scopes and defaults are generated from Alignr’s server; [connect your client](/mcp/connect) before making a call.', '', 'Confirm deployment availability using the [live reference](/api-reference/live-schema). An Organization is one client in your MSP workspace.', '', 'The required scope must be assigned to the key. For a user-scoped key, the owner must also retain the listed user permissions.', '', 'The catalogue includes retained server tools. The current token-creation form does not offer `asset:read`, `search:read` or `ask:use`, so do not assume every listed tool can be configured through that form. Existing credentials and the live deployment contract must be checked separately.', '', '## Choose a tool', '', '| Task | Tool | Required scope |', '| --- | --- | --- |']
for group in TOOL_GROUPS.values():
    for name, title in group:
        spec = registry[name]
        anchor = title.lower().replace(' ', '-')
        lines.append(f'| [{title}](#{anchor}) | `{name}` | `{spec.scope}` |')
for category, group in TOOL_GROUPS.items():
    lines += ['', f'## {category}']
    for name, title in group:
        spec = registry[name]
        function = getattr(server, name)
        lines += ['', f'### {title}', '', f'`{name}`', '', spec.summary, '', f'**Required scope:** `{spec.scope}`', '', '**User permissions:** '+', '.join(f'`{permission}`' for permission in spec.permissions)+'.', '', '| Argument | Required | Default |', '| --- | --- | --- |']
        parameters = inspect.signature(function).parameters
        for argument, param in parameters.items():
            required = param.default is inspect.Parameter.empty
            default = '—' if required else f'`{json.dumps(param.default)}`'
            lines.append(f'| `{argument}` | {"Yes" if required else "No"} | {default} |')
        lines += ['']
        for argument in parameters:
            help_text = ARGUMENT_HELP[argument]
            if name == 'list_organizations' and argument == 'limit':
                help_text = 'Clients per page, from 1 to 100 (default 20).'
            if name == 'list_remediation_runs' and argument == 'limit':
                help_text = 'Run statuses per page, from 1 to 50 (default 20).'
            if name == 'list_remediation_runs' and argument == 'offset':
                help_text = 'Zero-based page offset from 0 to 10,000. Most recently started runs appear first; unstarted runs appear last. Equal start times use run ID as a tie-breaker.'
            if name == 'list_remediation_runs' and argument == 'status':
                help_text = 'Optional exact run status: pending_approval, running, completed, partial, failed or rolled_back.'
            if argument == 'organization_id' and parameters[argument].default is not inspect.Parameter.empty:
                help_text += ' Omit it to use the tool’s workspace-wide scope.'
            lines.append(f'- **`{argument}`:** {help_text}')
        if name == 'create_organization':
            lines += ['', '<Warning>This creates a client. There is no idempotency key or automatic retry; if the result is uncertain, look up the recorded slug before trying again. A valid user-owned key and its active owner’s current `organization.write` permission are required; the owner must have no pending required password change. Service keys cannot perform this write.</Warning>']
        elif name == 'update_organization':
            lines += ['', '<Warning>This changes a client. Confirm the exact Organization ID and intended fields before calling it. A valid user-owned key and its active owner’s current `organization.write` permission are required; the owner must have no pending required password change. Service keys cannot perform this write.</Warning>']
        elif name == 'create_detection_note':
            lines += ['', '<Warning>This tool writes a detection note. Confirm the target and note text before allowing the call.</Warning>']
        elif name == 'list_remediation_runs':
            lines += ['', 'The `total` count and `items` page are restricted to your MSP workspace. Each item contains only the run, detection and plan UUIDs; lifecycle and verification statuses; a `simulated` flag; and creation, start, finish and update timestamps. The page never includes step outputs, vendor payloads, result summaries, labels or rollback material.']
        elif name == 'get_remediation_run_status':
            lines += ['', '<Note>The detail returns the same fixed fields as each list item. A run marked `completed` means execution reached that state; it does not prove the control was fixed. Check `verificationStatus` and fresh source evidence. `simulated: true` means at least one step was rehearsed rather than applied. Neither this tool nor the list reports rollback eligibility: status alone cannot establish that a rollback window is open or an eligible token remains.</Note>']
        elif name == 'get_remediation_plan_outline':
            lines += ['', 'This is a metadata-only outline, not an execution preview. `previewKind` is `metadata_only`; `executionReadiness` and `targetReadiness` are `not_checked`; `simulationMode` is `unknown`. The result gives plan, detection and Organization UUIDs, required autonomy and reversibility, plus at most 50 steps ordered by position and ID. Each step contains only its UUID, position, allowlisted `actionType` (or `unsupported`), reversibility and `requiresApproval`. `stepsTruncated: true` means more steps exist; never treat the displayed page as the whole plan.', '', '<Warning>No step parameters, target binding or eligible targets, credentials, descriptions, result payloads or plan fingerprint are returned. Reversibility and approval metadata do not establish that the action is ready, permitted or safe to run. Use the signed-in [remediation workflow](/guides/remediation) to inspect current targets and authority and request or approve an action.</Warning>']
lines += [
    '', '## Authenticated help resources', '',
    'These are MCP resources, not tools. Use `resources/list` to discover them and `resources/read` to open them in a connected client. Both require a valid bearer key, but reading them grants no tool scope or permission. Use `tools/list` for the deployed tool definitions and input schemas.', '',
    '| Resource URI | What it contains |', '| --- | --- |',
    '| `alignr://help/getting-started` | Connection, discovery, common read workflows and capability limits. |',
    '| `alignr://help/tools-and-scopes` | Registered tool names, MCP scopes, required owner permissions and summaries from the server registry. |', '',
    'The signed-in [Developer Console](https://app.alignr.io/developer) shows the current MCP reference. Its **Try it** console executes REST requests against the real workspace; use an MCP client to read these resources or call MCP tools.',
    '', '## Understand the answer', '',
    'A missing result is not proof that a control passed. Read [control statuses](/guides/control-status), retain the client and evidence context, and review [MCP permissions](/mcp/security).',
]
(ROOT/'mcp/tools.mdx').write_text('\n'.join(lines)+'\n')
print(f'Generated {len(paths)} read endpoints and {len(MCP_TOOL_SCOPES)} MCP tools.')
