"""Check readable descriptions against the application vocabulary and render the guide.

Usage: python3 scripts/build-predicate-reference.py /path/to/ledgr
Only executes the dependency-free vocabulary module; no app startup or database access.
"""
import json
from pathlib import Path
import runpy
import sys

root = Path(__file__).resolve().parents[1]
app = Path(sys.argv[1]).resolve()
vocabulary = runpy.run_path(str(app/'api/ledgr/models/facts.py'))
canonical = {p.value for p in vocabulary['FactPredicate']}
multi = vocabulary['MULTI_VALUED_PREDICATES']
entries = json.loads((root/'reference-data/predicates.json').read_text())
names = [entry['name'] for entry in entries]
assert len(names) == len(set(names)), 'Duplicate predicate descriptions'
assert set(names) == canonical, f'Update descriptions: missing={canonical-set(names)}, removed={set(names)-canonical}'
lines = ['---', 'title: "Predicate reference"', 'description: "Plain-English meanings and interpretation notes for every registered fact predicate."', '---', '', 'Use this reference when choosing evidence for a control or reading a technical result. Start with [Understanding predicates](/guides/predicates) if these names are unfamiliar.', '', '## How to use this reference', '', f'This catalogue covers **{len(entries)} registered predicates** in the application vocabulary. Availability depends on your connected sources and deployment. Check client-specific coverage and actual observations before using a predicate in a control.', '', 'Use the docs search to find a technical identifier, or the page contents to jump to a topic category.', '', 'Expand an entry to see its readable label, the exact technical identifier, its meaning and an interpretation limit. **Multiple values** means several values can legitimately coexist for a subject; it does not change a control operator into an automatic check of every member.', '', 'Boolean values distinguish true, false and missing evidence. Counts, state strings, dates and relationships must be interpreted in their source context. These descriptions are not a replacement for inspecting the observed value.', '']
previous = None
for index, entry in enumerate(entries):
    if entry['group'] != previous:
        previous = entry['group']
        lines += [f'## {previous}', '', '<AccordionGroup>', '']
    name = entry['name']
    lines += [f'<Accordion title="{entry["label"]}">', '', f'`{name}`', '', entry['description'], '', f'**Interpretation:** {entry["interpretation"]}', '']
    if name in multi:
        lines += ['**Multiple values:** several values can legitimately coexist for one subject.', '']
    lines += ['</Accordion>', '']
    if index == len(entries)-1 or entries[index+1]['group'] != previous:
        lines += ['</AccordionGroup>', '']
lines += ['## Choosing the right observation', '', 'Write the question you need to answer, identify its subject, then choose the predicate that directly addresses it. Confirm your source supplies that predicate and inspect an actual value before choosing an operator.', '', 'For example, “is a backup product present?”, “did a backup succeed recently?” and “can we restore this system?” are three different questions. The first two have separate observations; neither replaces a restore test.', '', '[Build a control condition](/guides/control-conditions) or [troubleshoot missing evidence](/guides/troubleshooting).', '']
(root/'guides/predicate-reference.mdx').write_text('\n'.join(lines))
print(f'Rendered and checked {len(entries)} predicate descriptions.')
