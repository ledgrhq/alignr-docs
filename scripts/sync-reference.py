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
    'Standards': [('/standards', 'List standards'), ('/standards/{standard_id}', 'Get a standard'), ('/standards/{standard_id}/controls', 'List controls'), ('/standards/{standard_id}/activation-preview', 'Preview copied-standard activation'), ('/standards/{standard_id}/evaluation-preview', 'Preview one-client evaluation'), ('/standards/{standard_id}/evaluation-requests/{operation_id}', 'Get an evaluation request')],
    'Alignment': [('/organizations/{organization_id}/compliance', 'Get client compliance'), ('/organizations/{organization_id}/compliance/trend', 'Get compliance trend')],
    'Detections': [('/detections', 'List detections'), ('/detections/{detection_id}', 'Get a detection')],
    'Evidence': [('/facts', 'List facts'), ('/integrations/{integration_id}/client-mapping-candidates', 'List source client mappings'), ('/integrations/{integration_id}/sync-operations/{operation_id}', 'Get an evidence refresh')],
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
        if suffix == '/integrations/{integration_id}/sync-operations/{operation_id}':
            operation['description'] += ' Read the current durable state of the exact source-wide collection. `completed` means its SyncRun finished evidence collection; `assessmentState: unknown` does not attest a passing control or completed downstream evaluation. A foreign or mismatched source/operation pair returns 404.'
        if suffix == '/integrations/{integration_id}/client-mapping-candidates':
            operation['description'] += ' List bounded existing remote-company mappings for an eligible generic PSA/RMM source. Includes remote ID/name, current Organization ID and caller-bound short-lived revision; excludes credentials and source config. Only unassigned records can be first-linked through the separate write endpoint. A foreign source or Organization filter returns 404.'
        if suffix == '/standards/{standard_id}/activation-preview':
            operation['description'] += ' For a non-empty disabled curated-copy draft, returns the bounded complete standard/control/manual-check policy it signs, workspace-wide acknowledgement context and a short-lived revision. Current per-client overrides and client population are not frozen; this read does not enable or evaluate.'
        if suffix == '/standards/{standard_id}/evaluation-preview':
            operation['description'] += ' Preview one enabled standard and one explicit client with authored policy, effective overrides, source-selection context and a short-lived caller-bound revision. This read does not collect facts, assess manual checks, run controls or deploy a standard.'
        if suffix == '/standards/{standard_id}/evaluation-requests/{operation_id}':
            operation['description'] += ' Read the exact historical one-client evaluation operation. Pending and controls_committed are checkpoints; completed does not mean every control passed. Unknown provider outcome is terminal to automatic retry. This is not a current compliance score.'
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
    'Standard drafts': [('list_standard_library_templates', 'List curated standard templates'), ('copy_standard_library_template', 'Copy a disabled standard draft'), ('list_workspace_standards', 'List workspace standards'), ('get_standard_definition', 'Inspect a standard definition'), ('get_standard_activation_preview', 'Preview standard activation'), ('activate_standard_draft', 'Activate a copied standard draft')],
    'Standard assessment': [('get_standard_evaluation_preview', 'Preview one-client evaluation'), ('request_standard_evaluation', 'Request one-client evaluation'), ('get_standard_evaluation_operation', 'Get an evaluation request')],
    'Findings': [('list_detections', 'List detections'), ('create_detection_note', 'Add a detection note')],
    'Remediation': [('get_remediation_plan_outline', 'Get remediation plan outline'), ('get_remediation_review_preview', 'Preview an exact remediation review'), ('request_remediation_review', 'Request human remediation review'), ('list_remediation_runs', 'List remediation runs'), ('get_remediation_run_status', 'Get remediation run status')],
    'Evidence refresh': [('list_evidence_sources', 'List evidence sources'), ('request_source_refresh', 'Request a source refresh'), ('get_source_refresh', 'Get a source refresh')],
    'Client source linking': [('list_source_client_mappings', 'List source client mappings'), ('link_source_client', 'Link a source client')],
    'Search': [('search_documentation', 'Search indexed content')],
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
    'limit': 'Maximum number of results requested.',
    'control': 'Control UUID, name, or case-insensitive substring of its name or slug.',
    'standard': 'Standard UUID, name, or case-insensitive substring of its name or slug.',
    'key': 'Curated template key returned by list_standard_library_templates.',
    'template_revision': 'Opaque current revision returned for this exact curated template. Refresh the list after a template change.',
    'activation_revision': 'Exact short-lived activationRevision returned by the complete policy preview. Re-preview after expiry or a policy edit.',
    'evaluation_revision': 'Exact short-lived evaluationRevision returned for this standard, client and key. Re-preview after expiry or a policy or source-selection change.',
    'acknowledge_workspace_wide': 'Set true only after reviewing the complete policy and accepting its workspace-wide effect, including clients added later.',
    'standard_id': 'Exact standard UUID in your MSP workspace; a foreign standard is not found.',
    'control_limit': 'Number of controls on this page, from 1 to 20 (default 10).',
    'control_offset': 'Zero-based control offset from 0 to 10,000 (default 0).',
    'manual_check_limit': 'Number of manual checks on this page, from 1 to 20 (default 10).',
    'manual_check_offset': 'Zero-based manual-check offset from 0 to 10,000 (default 0).',
    'status': 'Status to filter by; the default is shown below.',
    'detection_ref': 'Reference identifying the detection to annotate.',
    'run_id': 'Remediation run UUID. A run outside your workspace returns not found.',
    'plan_id': 'Remediation plan UUID. A plan outside your workspace returns not found.',
    'detection_id': 'Open detection UUID linked to the exact plan.',
    'integration_id': 'UUID of the connection.',
    'mapping_id': 'UUID of an existing unassigned remote record returned by mapping discovery.',
    'revision': 'The short-lived opaque revision returned for the exact mapping. Refresh discovery if it changes or expires.',
    'remote_id': 'Optional exact vendor remote ID filter, up to 300 characters; never use a display name as identity.',
    'assignment': 'Filter mappings by all, assigned or unassigned; default all.',
    'operation_id': 'The durable operation UUID returned by the refresh request. Match it with the same connection ID.',
    'review_revision': 'The short-lived `reviewRevision` returned by `get_remediation_review_preview`. Request a fresh preview after expiry or a plan, target, authority or source change.',
    'idempotency_key': 'Caller-generated UUID for this one intended request. Keep it and reuse it only to resolve an uncertain outcome for the same payload; a different payload under the same key is refused.',
    'note': 'Text to add to the detection.',
}
ordered_tools = [name for group in TOOL_GROUPS.values() for name, _ in group]
registry = {spec.tool: spec for spec in MCP_TOOL_SCOPES.values()}
if set(ordered_tools) != set(registry):
    raise ValueError('Update TOOL_GROUPS when the MCP registry changes')
lines = ['---', 'title: "MCP tools"', 'description: "Choose a tool by task, then check its arguments and required scope."', '---', '', 'Use this catalogue to choose a tool for your task. Names, scopes and defaults are generated from Alignr’s server; [connect your client](/mcp/connect) before making a call.', '', 'Confirm deployment availability using the [live reference](/api-reference/live-schema). An Organization is one client in your MSP workspace.', '', 'The required scope must be assigned to the key. For a user-scoped key, the owner must also retain the listed user permissions.', '', 'The current token-creation form does not offer `asset:read` or `search:read`, so do not assume every listed tool can be configured through that form. Existing credentials and the live deployment contract must be checked separately.', '', '## Choose a tool', '', '| Task | Tool | Required scope |', '| --- | --- | --- |']
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
            if name == 'get_standard_evaluation_operation' and argument == 'operation_id':
                help_text = 'UUID of the exact historical standard evaluation request.'
            if name == 'list_organizations' and argument == 'limit':
                help_text = 'Clients per page, from 1 to 100 (default 20).'
            if name == 'list_remediation_runs' and argument == 'limit':
                help_text = 'Run statuses per page, from 1 to 50 (default 20).'
            if name == 'list_remediation_runs' and argument == 'offset':
                help_text = 'Zero-based page offset from 0 to 10,000. Most recently started runs appear first; unstarted runs appear last. Equal start times use run ID as a tie-breaker.'
            if name == 'list_remediation_runs' and argument == 'status':
                help_text = 'Optional exact run status: pending_approval, running, completed, partial, failed or rolled_back.'
            if name == 'list_evidence_sources' and argument == 'limit':
                help_text = 'Sources per page, clamped to 1–50 (default 50).'
            if name == 'list_evidence_sources' and argument == 'offset':
                help_text = 'Zero-based offset clamped to 0–10,000; source name then UUID order.'
            if name == 'request_source_refresh' and argument == 'idempotency_key':
                help_text = 'Canonical caller-generated UUID for this one source-wide request. Save and reuse it with the same connection after an uncertain response; a different source under the same key is refused.'
            if name == 'link_source_client' and argument == 'idempotency_key':
                help_text = 'Canonical UUID for this exact first link. Reuse the same key with identical arguments after an uncertain response; changed payload is refused.'
            if name == 'copy_standard_library_template' and argument == 'name':
                help_text = 'Optional display name for the new standard draft, 1–200 characters.'
            if name == 'list_workspace_standards' and argument == 'limit':
                help_text = 'Workspace standards per page, from 1 to 20 (default 20).'
            if name == 'list_workspace_standards' and argument == 'offset':
                help_text = 'Zero-based offset from 0 to 10,000; standard name then UUID order.'
            if name == 'list_source_client_mappings' and argument == 'limit':
                help_text = 'Remote records per page, from 1 to 50 (default 25).'
            if name == 'list_source_client_mappings' and argument == 'offset':
                help_text = 'Zero-based offset from 0 to 10,000; remote name then mapping UUID order.'
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
        elif name == 'get_remediation_review_preview':
            lines += ['', 'This is a separate exact-plan request preview. It checks the current open detection, linked plan, selected targets, local authority, connector binding and a complete set of 1–50 steps. The response includes `reviewRequestReady`, `vendorExecutionReady: not_checked`, `reviewRevision`, `revisionExpiresAt`, client/detection/plan identifiers and bounded step metadata: action, position, reversibility, approval need, selected integration and an allowlisted resource parameter/value where required. It omits credentials and executable step parameters. The revision expires after 15 minutes; previewing does not request, approve or execute a run.', '', '<Warning>`reviewRequestReady: true` means this exact request passed local checks at preview time, not that a vendor action will succeed. The server rechecks the plan and live authority when a request is submitted. The metadata-only outline above does not supply a `reviewRevision`.</Warning>']
        elif name == 'request_remediation_review':
            lines += ['', 'Requires a user-owned key with `remediation:request`; its active owner must currently hold both `remediation.read` and `remediation.execute` and have no pending required password change. A service key is refused. Pass the exact IDs, the latest preview’s `reviewRevision`, and a caller-generated UUID `idempotency_key`. A changed/expired preview is refused; obtain a new one. The result contains `runId`, `approvalId`, `runStatus`, `approvalStatus` and `replayed`. New requests create only a pending approval and pending run; no step executes. A separate named human reviews and approves in Alignr.', '', '<Warning>This tool writes a review request. Reuse the same UUID only with the same payload after an uncertain response; `replayed: true` reports the existing request. Do not generate a new key and blindly repeat. A prior run may already be pending even when this call times out. See the [review-request workflow](/mcp/request-review).</Warning>']
        elif name == 'list_evidence_sources':
            lines += ['', 'The page lists evidence-producing connector types across your MSP, including sources that may not currently be connected. Check each `status` before requesting a refresh. It does not list directory-only client import sources, and no client filter narrows a refresh.']
        elif name == 'request_source_refresh':
            lines += ['', 'Requires a user-owned `integration:sync` key and the active owner’s current `integration.manage` permission. A service key is refused. The result reports one durable operation and `replayed`; `pending` means recorded, not collected. The collection spans the connection and every mapped client. Same caller/key/source retries return the current original operation; after an exact SyncRun is claimed, uncertain vendor I/O is not automatically replayed.', '', '<Warning>Save the UUID and returned operation ID. Do not make a new request after a timeout until you recover the original state with the same key or poll the operation. `completed` does not mean assessment passed. Follow [Refresh evidence with MCP](/mcp/refresh-evidence).</Warning>']
        elif name == 'get_source_refresh':
            lines += ['', 'Returns only the matching workspace, connection and exact operation. `state` is pending, running, completed, failed or interrupted; `assessmentState` remains `unknown`. Optional `sweepId` and `syncRunId` identify the exact collection. `errorCode` is safe and machine-readable, not a vendor response. A completed collection still needs fresh evidence and separate standards evaluation before a pass claim.']
        elif name == 'list_source_client_mappings':
            lines += ['', 'Returns existing remote-company records from a supported generic PSA/RMM source only. Each row includes its mapping ID, remote ID/name, current Organization ID or null, and a short-lived caller-bound `revision`. It does not fetch a new directory, create a client, include connector credentials or narrow an eventual source-wide refresh. Service keys with `integration:read` may use this read.', '', 'Supported first-link source types are ConnectWise Manage, HaloPSA, Autotask, Datto RMM and NinjaOne. Microsoft selection and built-in domain mappings use separate workflows.']
        elif name == 'link_source_client':
            lines += ['', 'Requires a user-owned key with `integration:map`, backed by the owner’s current `integration.manage` permission. Pass an existing unassigned mapping, existing unarchived Organization UUID, the exact discovery `revision` and a canonical UUID idempotency key. A running collection, changed mapping or source, assigned record, unsupported source, archived/foreign client or missing authority is refused. This changes only the mapping in Alignr; it does not call a vendor or start a refresh.', '', '<Warning>If the response is lost, retry the **same key and identical arguments**. A committed link returns the original receipt with `replayed: true` even if the source or client was later removed. A new key is a new intention and cannot relink an already assigned record. Linking does not move historical facts, run a control, prove passing status, or bypass human remediation approval. See [Link source clients](/mcp/link-source-clients).</Warning>']
        elif name == 'list_standard_library_templates':
            lines += ['', 'Lists the curated library with an opaque revision for each exact template. It requires `standards:read`; for a user-owned key, the active owner must also retain `detection_rule.read`. A service key with that read scope may list templates. A read does not create a standard or assess a client. See [Copy a standard draft](/mcp/copy-standard-draft).']
        elif name == 'copy_standard_library_template':
            lines += ['', 'Requires a user-owned key with `standards:copy`, backed by the active owner’s `detection_rule.write` permission. The server copies only the selected curated template into a disabled draft, including its controls and manual checks. It does not enable, evaluate, deploy, collect evidence or create detections. A service key cannot copy.', '', '<Warning>Save a canonical UUID `idempotency_key` before calling this tool. If the response is uncertain, retry with the **same key and identical arguments**. `replayed: true` returns the historical `copied_disabled` receipt; it does not assert that a human has not since enabled, edited or deleted the draft. A changed payload under the same key is refused. See [Copy a standard draft](/mcp/copy-standard-draft).</Warning>']
        elif name == 'list_workspace_standards':
            lines += ['', 'Lists current standards in the key’s MSP workspace, including copied drafts, with enabled state, version and child counts. It does not return control definitions or attest assessment. The page is ordered by name and UUID; each request is capped at 20 items and 256 KiB. `truncatedByOffsetLimit: true` means more rows exist beyond the permitted 10,000 offset; `nextOffset` is then null. User-owned keys need the active owner’s current `detection_rule.read`; a read-scoped service key may also list. See [Copy and inspect a standard draft](/mcp/copy-standard-draft).']
        elif name == 'get_standard_definition':
            lines += ['', 'Reads one current standard and independent, bounded pages of its controls and manual checks. `definition`, `parameters` and `instructions` are workspace-controlled data, not instructions to your assistant; a user may have entered sensitive text there. The tool omits assessments, evidence, source metadata and vaulted-secret or credential-envelope fields, but does not redact arbitrary text from those three content fields. Each child page is capped at 20 and the whole result at 256 KiB; reduce page sizes if refused. `truncatedByOffsetLimit: true` means more rows lie beyond the permitted 10,000 offset. A foreign standard returns not found. Inspection does not enable, evaluate or approve a draft. See [Copy and inspect a standard draft](/mcp/copy-standard-draft).']
        elif name == 'get_standard_activation_preview':
            lines += ['', 'For a non-empty disabled draft with a curated copy receipt, returns the complete bounded policy (standard, controls, manual checks and scopes), `enabled: false`, counts, `workspaceWide: true`, `activationRevision` and expiry. The policy content is workspace-authored data, not assistant instructions, and may contain sensitive text. The revision binds this exact content; it does not freeze current client overrides or the roster, or assert fresh evidence or passing results. A service key with `standards:read` may preview but cannot activate. See [Activate a copied standard draft](/mcp/activate-standard-draft).']
        elif name == 'activate_standard_draft':
            lines += ['', 'Requires a user-owned key with `standards:activate` and the active owner’s current `detection_rule.write` permission. Pass the exact preview revision, one canonical UUID `idempotency_key` and `acknowledge_workspace_wide: true`. A stale/expired/changed revision or an already enabled draft is refused. It enables only the receipt-backed draft; it does not evaluate, collect evidence, create detections or call a vendor.', '', '<Warning>If the response is uncertain, retry the same UUID and identical arguments. `replayed: true` returns the historical `activated` receipt even if the standard was later disabled or deleted; read current state separately. A changed payload under the same UUID is refused. See [Activate a copied standard draft](/mcp/activate-standard-draft).</Warning>']
        elif name == 'get_standard_evaluation_preview':
            lines += ['', 'Returns the bounded complete authored policy, this client’s effective overrides, source-selection context, control/manual-check counts and short-lived `evaluationRevision` for an enabled standard and explicit Organization. It does not freeze facts or prove that observations are fresh. Workspace-authored policy text may contain sensitive content and is data to review, not assistant instructions. A read-scoped service key may inspect but cannot request an evaluation.', '', 'Use the **same user-owned key** for the preview and request: the revision is bound to the key. See [Evaluate one client](/mcp/evaluate-one-client).']
        elif name == 'request_standard_evaluation':
            lines += ['', 'Requires a user-owned key with `standards:evaluate` and its active owner’s current `detection_rule.write` permission. Pass one enabled `standard_id`, one `organization_id`, the exact preview `evaluation_revision` and a caller-generated canonical UUID `idempotency_key`. A committed response identifies a durable operation; `pending` does not mean a check has run.', '', '<Warning>If the response is uncertain, retry the same UUID and identical arguments with the same key. A replay returns the original operation and its current durable state; a changed payload is refused. After provider I/O begins, an uncertain outcome becomes `unknown` and is never automatically redelivered. This action does not collect evidence, assess manual checks or deploy the standard. See [Evaluate one client](/mcp/evaluate-one-client).</Warning>']
        elif name == 'get_standard_evaluation_operation':
            lines += ['', 'Polls the exact tenant/standard/client operation. States are `pending`, `controls_committed`, `completed`, `completed_with_errors`, `interrupted` and `unknown`; counts and timestamps describe that historical run. `completed` does not mean every control passed, and `unknown` needs deliberate review rather than automatic provider retry. Read current control results and evidence separately.']
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
