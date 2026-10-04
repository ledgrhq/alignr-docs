"""Generate the complete built-in control catalogue from a matching Alignr checkout.

Run using Alignr's Python environment, with PYTHONPATH pointing to its api folder:
PYTHONPATH=api api/.venv/bin/python /path/to/alignr-docs/scripts/build-control-reference.py /path/to/ledgr
No database queries or seed execution. Seed declarations are read with ast.literal_eval.
"""
import ast
import json
from pathlib import Path
import sys
from ledgr.services.standards_library_service import TEMPLATES
from ledgr.detection.dsl import parse_rule_definition, derive_requires

root = Path(__file__).resolve().parents[1]
app = Path(sys.argv[1]).resolve()
module = ast.parse((app/'api/ledgr/db/seed.py').read_text())
node = next(n for n in module.body if isinstance(n, ast.AnnAssign) and getattr(n.target,'id','') == 'LEDGR_BASELINE_CONTROLS')
seed = [{k.arg:ast.literal_eval(k.value) for k in call.keywords} for call in node.value.elts]
labels = {p['name']:p['label'] for p in json.loads((root/'reference-data/predicates.json').read_text())}
groups = {
 'identity': ('Identity and access', 'Accounts, MFA registration, Conditional Access and privileged-access reviews.'),
 'endpoints': ('Endpoints and servers', 'Device reporting, patching, EDR, encryption and server hardening.'),
 'backup': ('Backup and recovery', 'Backup protection, job health, recency and restore testing.'),
 'vulnerability': ('Vulnerabilities and governance', 'Scanned findings, missing patches and operational security reviews.'),
 'licensing': ('Licensing', 'Licence presence and renewal-date evidence.'),
 'network': ('Networks and firewalls', 'Firmware availability, network inventory and configuration recovery.'),
 'email': ('Email and domains', 'DNS observations and the manual checks needed for broader mail protection.'),
 'external': ('External exposure', 'DNS resilience and human reviews of internet-facing assets and access.'),
}
seed_groups = {'Identity':'identity','Endpoint':'endpoints','Backup':'backup','Vulnerability':'vulnerability','Licensing':'licensing'}
template_groups = {'bios-identity':'identity','bios-endpoint-server':'endpoints','bios-network':'network','bios-backup':'backup','bios-vulnerability-governance':'vulnerability','email-domain-protection':'email','external-exposure':'external'}
# Fail loudly if an added or renamed template needs a deliberate category choice.
assert set(template_groups) == {t['key'] for t in TEMPLATES}, {t['key'] for t in TEMPLATES}
entries = {key:[] for key in groups}
for c in seed:
 entries[seed_groups[c['category']]].append(('Alignr Baseline (seeded)',c,False))
for t in TEMPLATES:
 for c in t['controls']:
  entries[template_groups[t['key']]].append((t['name'],c,False))
 for c in t['manual_checks']:
  entries[template_groups[t['key']]].append((t['name'],c,True))
notes = {
 'mfa_registered':'This checks MFA registration, not effective enforcement at every sign-in. Review policy coverage, allowed methods and emergency exclusions separately.',
 'ca_policy_state':'The title is broader than the measured condition: an observed All users policy being enabled does not establish all policy interactions, exclusions or sign-in enforcement.',
 'edr_agent_installed':'Agent installation is not agent health or recent reporting. Correlate the same endpoint across sources.',
 'patch_status':'`compliant` passes and a recognised non-compliant state fails. Datto’s explicit `unknown` is not a result: if no known state fails, the control needs evidence (`no_data`). A validated complete Datto inventory that omits patch status withdraws Datto’s previous observation. A malformed or incomplete inventory leaves that observation in place; freshness rules still determine whether it can be used. This check does not prove absence of every vulnerability.',
 'device_encryption_enabled':'Reported encryption does not establish recovery-key custody or successful recovery.',
 'device_compliance_state':'Compliant means compliant with the MDM source’s configured policies, not every Alignr expectation.',
 'backup_protected_by':'Recorded product presence is not a successful backup or a tested restore. Missing evidence must be investigated rather than treated as passing.',
 'backup_job_state':'The expected state is the normalised value ok. Review the job/workload identity and timing; this is not a restore test.',
 'backup_last_successful_at':'This measures backup recency, despite any title mentioning a retention window. It does not inspect retention policy, recovery time or restored-data integrity.',
 'vulnerability_max_severity':'This excludes the exact value critical. A non-critical value does not mean zero vulnerabilities, and absent severity evidence does not pass.',
 'vulnerability_open_count':'The limit applies to the source-reported count for a subject. Keep scanner scopes comparable; a low count is not proof of low business risk.',
 'missing_patch':'Important limitation: not_exists compares an observed null value. No missing_patch row is unknown, not a clean patch result. An observed missing patch fails; do not use a lack of rows as proof that the endpoint is patched.',
 'has_licence':'This checks that an observed licence value exists, not that the licence is paid, appropriate, actively used or required for every account type. Review exceptions for service and other special-purpose identities.',
 'licence_renewal_date':'This checks that a renewal value is present, not that the date is in the future or the commercial terms are suitable.',
 'firmware_update_available':'No reported update is not proof of supported firmware or full device hardening. An available update still needs risk review and scheduling.',
 'external_spf_present':'This is the bounded DNS presence check, not a full validation of authorised senders or every SPF include. Complete the manual SPF review.',
 'external_dmarc_enforced':'This checks the collected DNS enforcement signal. It does not test actual message alignment, reporting operation or every mail flow.',
 'external_mx_present':'A usable MX observation does not prove mail acceptance or correct routing for every sender. Null MX does not satisfy the source check.',
 'external_nameserver_count':'Two or more name servers do not prove independent providers, fault domains or recovery readiness.',
 'account_enabled':'Review the selected account population and its business purpose before acting. An automated disabled-state expectation does not authorise disabling an account.',
 'mfa_bypass_enabled':'A registered factor and an active bypass can coexist. Review approved emergency access and any temporary exception before changing the account.',
}
ops = {'eq':'equals','neq':'does not equal','gt':'is greater than','gte':'is at least','lt':'is less than','lte':'is at most','in':'is one of','not_in':'is not one of','exists':'has a non-null observed value','not_exists':'has an observed null value','matches':'matches the case-sensitive pattern','contains':'contains','older_than_days':'is more than this many days in the past:','within_days':'is within this many days of now (past or future):'}
def value(v):
 if isinstance(v,dict) and 'param' in v:return f'parameter `{v["param"]}`'
 return '`'+json.dumps(v,ensure_ascii=False)+'`'
def fact(p):return f'**{labels[p]}** (`{p}`)'
def condition(c):
 text=f'{fact(c["fact"])} {ops[c["op"]]}'
 if c['op'] not in ('exists','not_exists'):text+=' '+value(c.get('value'))
 return text+'.'
def page(path,title,desc,body):
 (root/(path+'.mdx')).write_text('---\ntitle: '+json.dumps(title)+'\ndescription: '+json.dumps(desc)+'\n---\n\n'+body.rstrip()+'\n')
for key,(title,desc) in groups.items():
 auto=sum(not manual for _,_,manual in entries[key]);manual_count=sum(manual for _,_,manual in entries[key])
 lines=[f'This category contains **{auto} automated control definitions** and **{manual_count} manual check{"s" if manual_count != 1 else ""}** across the sources named below. Similar controls from different standards are listed separately because names, thresholds or severity can differ.','', 'Whether the seeded Alignr Baseline is available depends on how your workspace was provisioned. Library templates are copied as disabled drafts. See [Choose a baseline](/controls/baselines/overview) before enabling anything.','', '## Automated controls','', 'Expand a control to see the exact population, expectation and defaults. A pass requires usable evidence for the selected population. A known contrary observation can prove failure; missing observations or an empty population must not become a pass.','', '<AccordionGroup>','']
 for source,c,manual in entries[key]:
  if manual:continue
  d=c['definition'];parse_rule_definition(d)
  population = {
   'account_enabled': 'Accounts observed as enabled.' if d['match'].get('object') is True else 'Accounts with an enabled-state observation.',
   'has_role': 'Accounts observed with the Global Administrator role.',
   'ca_policy_scope': 'Conditional Access policies observed with an All users scope.',
   'device_managed_by': 'Devices reported as managed by an RMM.',
   'mdm_enrolled_by': 'Devices with an MDM enrolment observation.',
   'backup_protected_by': 'Workloads with a recorded backup product.',
   'backup_job_state': 'Backup jobs with a recorded status.',
   'licence_seats_purchased': 'Licences with a purchased-seat observation.',
  }.get(d['match']['predicate'], 'Subjects with a recorded '+labels[d['match']['predicate']].lower()+' observation.')
  explanations = {
   'mfa_registered': 'Each selected account should have MFA registered.',
   'ca_policy_state': 'Each selected policy should be enabled.',
   'mfa_bypass_enabled': 'MFA bypass should be off for each selected account.',
   'account_enabled': 'Accounts selected by the inactivity filter should be disabled.',
   'edr_agent_installed': 'Each selected device should report an installed EDR agent.',
   'device_last_checkin': 'Each selected device should have a check-in timestamp within the configured day window.',
   'patch_status': 'Each selected device should report a compliant patch status.',
   'device_encryption_enabled': 'Each selected device should report encryption enabled.',
   'device_compliance_state': 'Each selected device should report a compliant MDM state.',
   'backup_protected_by': 'Each selected server should have a recorded backup product.',
   'backup_job_state': 'Each selected job should report a healthy status.',
   'backup_last_successful_at': 'Each selected workload should have a successful-backup timestamp within the configured day window.',
   'vulnerability_max_severity': 'The recorded maximum vulnerability severity should not be critical.',
   'vulnerability_open_count': 'The recorded open-vulnerability count should be at or below the configured limit.',
   'missing_patch': 'The selected device needs an explicit null observation for missing patches to satisfy this comparison.',
   'has_licence': 'Each selected account should have a recorded licence.',
   'licence_renewal_date': 'Each selected licence should have a recorded renewal date.',
   'firmware_update_available': 'Each selected device should report that no firmware update is available.',
   'external_spf_present': 'Each selected domain should have the expected SPF presence signal.',
   'external_dmarc_enforced': 'Each selected domain should have the expected DMARC enforcement signal.',
   'external_mx_present': 'Each selected domain should have a usable MX observation.',
   'external_nameserver_count': 'Each selected domain should have at least two observed name servers.',
  }
  lines += [f'<Accordion title="{c["name"]}">', '', '<Tabs sync={false}>', '<Tab title="Explanation">', '']
  lines += [explanations[e['fact']] for e in d['expect']]
  lines += ['', f'Part of **{source}**.', '', '**Applies to**', '', population, '']
  for w in d.get('where',[]):
   if w['fact']=='last_successful_sign_in': lines += ['Only accounts whose reported successful sign-in is older than the configured inactivity limit are selected. Microsoft includes successful interactive and background sign-ins, without identifying which app was used. Google supplies its reported last account login; its user-list response may be inaccurate and does not establish every kind of background OAuth activity. Confirm the individual Google account before acting on suspected dormancy.', '', 'A mailbox is not required: service and non-mailbox accounts remain eligible. Missing successful sign-in history is unknown, not proof of dormancy. Failed login attempts do not count as successful activity. Mailbox activity is not currently part of this condition.', '', 'The selected connection must report account state and activity in the same completed collection, no more than seven days old. That limit concerns collection time, not the age of the sign-in. A later account read without activity makes its older activity unavailable for current checks. [Understand successful sign-in evidence](/guides/predicates#successful-sign-in-activity).', '']
   elif w['fact']=='last_sign_in': lines += ['Only accounts whose recorded sign-in value is older than the configured inactivity limit are selected. Microsoft reports interactive attempts here, including failures; this historical condition does not establish last successful access.', '']
   elif w['fact']=='os_platform': lines += ['The operating-system name must also match the case-sensitive pattern `Server`.', '']
   else: lines += [condition(w), '']
  params=c.get('parameters',{})
  if params:
   lines+=['**Default settings**', '', '| Setting | Default | Allowed range |','| --- | --- | --- |']
   for n,p in params.items():lines.append(f'| {p.get("label",n)} | {value(p["default"])} | {p.get("min","—")}–{p.get("max","—")} |')
   lines += ['', 'Client overrides can change these values. [Check the effective settings](/controls/parameters) when interpreting a result.', '']
  lines += ['**What the result tells you**', '']
  for e in d['expect']:
   if e['fact'] in notes:lines += [notes[e['fact']], '']
   if e['op']=='within_days':lines += ['The time window includes timestamps before or after now. Investigate unexpected future timestamps.', '']
  lines += ['</Tab>', '<Tab title="Definition">', '', '| Setting | Value |', '| --- | --- |', f'| Standard | {source} |', f'| Severity | {c["severity"].capitalize()} |', f'| Declared autonomy | {c["autonomy"].replace("_", " ").capitalize()} |', '', '**Population condition**', '', fact(d['match']['predicate'])+(' equals '+value(d['match']['object']) if 'object' in d['match'] else ' has an observation')+'.', '']
  for w in d.get('where',[]):lines += ['- Filter: '+condition(w)]
  lines += ['', '**Expected evidence**', '']
  for e in d['expect']:lines += ['- '+condition(e)]
  lines += ['', '**Required predicates:** '+', '.join('`'+p+'`' for p in sorted(derive_requires(parse_rule_definition(d))))+'.', '', '```json', json.dumps(d,indent=2), '```', '', '</Tab>', '</Tabs>', '', '</Accordion>', '']
 lines+=['</AccordionGroup>','','## Manual checks','']
 if not manual_count:lines+=['No manual checks are bundled in these catalogue entries. Add a separate manual check where the expectation needs human judgement.','']
 else:
  lines+=['These are human reviews, not automated evidence. The interval below is the template default; review ownership, evidence and suitability for the client.','','<AccordionGroup>','']
  for source,c,manual in entries[key]:
   if not manual:continue
   instructions=c['instructions']
   # Keep private workflow identifiers out of public reader instructions.
   import re
   instructions=re.sub(r'using the WF-\d+ runbook','using your approved runbook',instructions)
   instructions=re.sub(r'full WF-\d+ configuration baseline','full configuration baseline',instructions)
   instructions=instructions.replace('these BIOS controls','the full set of expectations')
   lines += [f'<Accordion title="{c["name"]}">','',f'**Review every {c["review_interval_days"]} days** · {source}','',instructions,'','**Record:** who performed the review, when it was performed, the evidence, the conclusion and any follow-up or approved exception. A due review is not evidence of a completed review.','','</Accordion>','']
  lines+=['</AccordionGroup>','']
 lines+=['## Investigate a result', '', 'Confirm the client and the account, device or other item being assessed. Check the source, observation time and effective settings, then compare the recorded evidence with the expectation. Missing evidence needs investigation; a change to the environment requires a separate review.', '', '## Next steps','','[Create a custom control](/controls/create-custom) · [Parameters and client overrides](/controls/parameters) · [Record a manual check](/controls/manual-checks)','']
 page('controls/baselines/'+key,title,desc,'\n'.join(lines))
counts={'seeded_controls':len(seed),'library_templates':len(TEMPLATES),'library_controls':sum(len(t['controls']) for t in TEMPLATES),'manual_checks':sum(len(t['manual_checks']) for t in TEMPLATES)}
(root/'reference-data/control-catalogue.json').write_text(json.dumps({'counts':counts,'seeded_controls':seed,'templates':[{k:v for k,v in t.items() if k!='_source_label'} for t in TEMPLATES]},indent=2)+'\n')
print(json.dumps(counts))
