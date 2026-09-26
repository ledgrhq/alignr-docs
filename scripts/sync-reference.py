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
config['navigation']['tabs'][1]['groups'] = config['navigation']['tabs'][1]['groups'][:2] + [{'group': group, 'openapi':'/api-reference/openapi.json','pages':['GET /api/v1'+suffix for suffix,_ in endpoints]} for group,endpoints in GROUPS.items()]
# Keep examples copyable without a hosted proxy accepting production credentials.
config['api'] = {'playground': {'display': 'none'}}
(ROOT/'docs.json').write_text(json.dumps(config,indent=2)+'\n')
lines = ['---', 'title: "MCP tools"', 'description: "Tool names, arguments and scopes generated from the Alignr server."', '---', '', 'This catalogue is generated from Alignr’s tool registry. Confirm deployment availability using the [live reference](/api-reference/live-schema). Tool identifiers retain their API spelling.', '', '## Tool catalogue', '', '| Tool | Required scope | Access |', '| --- | --- | --- |']
for spec in MCP_TOOL_SCOPES.values():
    lines.append(f'| `{spec.tool}` | `{spec.scope}` | {"Write" if spec.mutating else "Read"} |')
for spec in MCP_TOOL_SCOPES.values():
    function = getattr(server, spec.tool)
    lines += ['', f'## {spec.tool}', '', spec.summary, '', f'Required scope: `{spec.scope}`. Underlying permissions: '+', '.join(f'`{p}`' for p in spec.permissions)+'.', '', '| Argument | Required | Default |', '| --- | --- | --- |']
    for name, param in inspect.signature(function).parameters.items():
        required = param.default is inspect.Parameter.empty
        default = '—' if required else f'`{json.dumps(param.default)}`'
        lines.append(f'| `{name}` | {"Yes" if required else "No"} | {default} |')
    if spec.mutating:
        lines += ['', '<Warning>This tool writes a detection note. Confirm the target and note text before allowing the call.</Warning>']
(ROOT/'mcp/tools.mdx').write_text('\n'.join(lines)+'\n')
print(f'Generated {len(paths)} read endpoints and {len(MCP_TOOL_SCOPES)} MCP tools.')
