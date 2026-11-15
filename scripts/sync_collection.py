"""Refresh registry-derived static counts without changing case content.

Run after adding a complete case/card/registry entry. --check is read-only.
All counts remain accurate without JavaScript; no runtime registry fetch needed.
"""
import argparse
import html
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def render(source, data):
    total = len(data['cases'])
    source = re.sub(r'\d+ illustrated business micro cases', f'{total} illustrated business micro cases', source)
    source = re.sub(r'Micro Cases in Business \| \d+ classroom decisions', f'Micro Cases in Business | {total} classroom decisions', source)
    source = re.sub(r'\d+ decisions · \d+ teaching areas', f"{total} decisions · {len(data['areas'])} teaching areas", source)
    source = re.sub(r'(<[^>]+id="count"[^>]*>)\d+ cases', rf'\g<1>{total} cases', source)
    counts = {a['name']: sum(c['area'] == a['name'] for c in data['cases']) for a in data['areas']}
    def tile(match):
        area = html.unescape(match[1])
        assert area in counts, f'Unknown area shortcut: {area}'
        return re.sub(r'<small>\d+ cases</small>', f'<small>{counts[area]} cases</small>', match[0])
    return re.sub(r'<button[^>]+class="area-tile"[^>]+data-area="([^"]+)"[^>]*>.*?</button>', tile, source)


def check(root=ROOT):
    source = (root/'index.html').read_text()
    data = json.loads((root/'case-registry.json').read_text())
    assert render(source, data) == source, 'Stale collection counts: run python scripts/sync_collection.py'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        check()
    else:
        path = ROOT/'index.html'
        path.write_text(render(path.read_text(), json.loads((ROOT/'case-registry.json').read_text())))
