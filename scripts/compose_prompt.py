#!/usr/bin/env python3
"""Print shared system instructions and one asset prompt. Python 3.9+."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    if len(sys.argv)!=2:
        sys.exit('Usage: python scripts/compose_prompt.py <category/slug>')
    catalog=json.loads((ROOT/'catalog/assets.json').read_text())
    obj=next((a for a in catalog if a['id']==sys.argv[1]),None)
    if obj is None:
        sys.exit(f'Unknown ID: {sys.argv[1]}. See catalog/INDEX.md')
    print('# SYSTEM INSTRUCTIONS\n')
    print((ROOT/'system/STYLE_AND_ENGINEERING.md').read_text())
    print('\n\n---\n\n# COMPONENT TASK\n')
    print((ROOT/obj['prompt']).read_text())
if __name__=='__main__': main()
