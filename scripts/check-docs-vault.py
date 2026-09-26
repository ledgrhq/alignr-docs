"""Check docs-vault structure and its public-site exclusion boundary (stdlib only)."""
from pathlib import Path
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
required = {'vault/', 'AGENTS.md', 'CLAUDE.md', 'scripts/'}
ignored = {line.strip() for line in (ROOT / '.mintignore').read_text().splitlines() if line.strip() and not line.startswith('#')}
for entry in sorted(required - ignored):
    errors.append(f'.mintignore must exclude {entry}')
notes = list((ROOT / 'vault').rglob('*.md'))
moc = ROOT / 'vault/MOC.md'
if not moc.exists():
    errors.append('Missing vault/MOC.md')
else:
    indexed = {unquote(target.split('#')[0]) for target in re.findall(r'\]\(([^)]+)\)', moc.read_text())}
    for note in notes:
        if note != moc and note.relative_to(ROOT / 'vault').as_posix() not in indexed:
            errors.append(f'Vault note is not indexed: {note.name}')
for note in notes:
    for target in re.findall(r'\]\(([^)]+)\)', note.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        path = (note.parent / unquote(target.split('#')[0])).resolve()
        if not path.exists():
            errors.append(f'{note.relative_to(ROOT)}: missing link {target}')
for name in ('AGENTS.md', 'CLAUDE.md'):
    if 'vault/MOC.md' not in (ROOT / name).read_text():
        errors.append(f'{name} must direct agents to vault/MOC.md')
config = json.loads((ROOT / 'docs.json').read_text())
if re.search(r'vault/', json.dumps(config.get('navigation', {}))):
    errors.append('Public navigation contains a vault path')
for page in ROOT.rglob('*.mdx'):
    if any(part.startswith('.') or part in {'node_modules', 'vault'} for part in page.relative_to(ROOT).parts):
        continue
    if re.search(r'(?:href=["\']|\]\()[^\s"\')]*\bvault/', page.read_text()):
        errors.append(f'Public page links to vault: {page.relative_to(ROOT)}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(notes)} indexed vault notes, agent entry points and publication boundaries')
