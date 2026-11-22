#!/usr/bin/env python3
"""Check component catalog schema, IDs, and matching prompt files."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'catalog/assets.json').read_text())
issues=[];ids=set();paths=set()
for a in items:
    if a['id'] in ids: issues.append('duplicate ID: '+a['id'])
    ids.add(a['id'])
    if a['prompt'] in paths: issues.append('duplicate path: '+a['prompt'])
    paths.add(a['prompt'])
    p=ROOT/a['prompt']
    if not p.is_file(): issues.append('missing prompt: '+str(p)); continue
    content=p.read_text()
    for token in [a['name'],'Specific construction instructions','Required TypeScript API','Verification criteria']:
        if token not in content: issues.append('missing content in '+a['id']+': '+token)
    if any(a['dimensions'][k]<=0 for k in ('width','depth','height')): issues.append('invalid dimensions: '+a['id'])
actual={str(p.relative_to(ROOT)) for p in (ROOT/'prompts').rglob('*.md')}
for extra in actual-paths: issues.append('unregistered prompt: '+extra)
if issues:
    print('\n'.join(issues));sys.exit(1)
print(f'PASS: {len(items)} assets, {len(set(a["category"] for a in items))} categories, all prompt files present and unique.')
