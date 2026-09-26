"""Summarise de-identified usability observations; never manufacture empty results."""
import argparse
import csv
import math
import statistics
from collections import Counter, defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('csv_file')
args = parser.parse_args()
rows = defaultdict(list)
with open(args.csv_file, newline='', encoding='utf-8') as stream:
    reader = csv.DictReader(stream)
    required = {'session_id', 'participant_role', 'device', 'task_id', 'outcome', 'elapsed_seconds', 'notes'}
    if len(reader.fieldnames or []) != len(required) or set(reader.fieldnames or []) != required:
        parser.error('CSV headers must match the usability worksheet.')
    seen = set()
    for line, row in enumerate(reader, 2):
        if None in row or any(value is None for value in row.values()):
            parser.error(f'Line {line}: wrong number of fields.')
        row = {key: value.strip() for key, value in row.items()}
        try:
            elapsed = float(row['elapsed_seconds'])
            if not math.isfinite(elapsed) or elapsed < 0:
                raise ValueError
        except (ValueError, TypeError):
            parser.error(f'Line {line}: duration must be a finite non-negative number.')
        if row['outcome'] not in {'completed', 'assisted', 'blocked', 'abandoned'}:
            parser.error(f'Line {line}: unknown outcome.')
        key = (row['session_id'], row['task_id'])
        if key in seen or not all(row[k] for k in ('session_id','task_id','device','participant_role')):
            parser.error(f'Line {line}: missing identity fields or duplicate session/task.')
        seen.add(key)
        rows[(row['task_id'], row['participant_role'], row['device'])].append((row['outcome'], elapsed))
if not rows:
    print('No observations recorded. No completion or duration claim can be made.')
for (task, role, device), values in sorted(rows.items()):
    counts = Counter(outcome for outcome, _ in values)
    durations = [elapsed for outcome, elapsed in values if outcome == 'completed']
    median = statistics.median(durations) if durations else 'unmeasured'
    print(f'{task} | {role} | {device} | n={len(values)} | ' +
          ' '.join(f'{outcome}={counts[outcome]}' for outcome in ('completed','assisted','blocked','abandoned')) +
          f' | completed_median_seconds={median}')
