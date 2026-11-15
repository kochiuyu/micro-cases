"""Synchronize registry-derived case navigation; --check never writes pages."""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import quote
ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'<nav\b[^>]*class="case-navigation"[^>]*>.*?</nav>', re.S)


def navigation(data, case):
    area = next(a for a in data['areas'] if a['name'] == case['area'])
    group = sorted((c for c in data['cases'] if c['area'] == case['area']), key=lambda c: c['legacy_id'])
    i = group.index(case)
    esc = html.escape
    def neighbour(c, direction):
        return f'<a href="{esc(c["slug"], quote=True)}.html"><small>{direction} · {esc(c["code"])}</small><span>{esc(c["title"])}</span></a>'
    previous = neighbour(group[i-1], 'Previous') if i else '<span class="nav-boundary">First case in this area</span>'
    following = neighbour(group[i+1], 'Next') if i+1 < len(group) else '<span class="nav-boundary">Last case in this area</span>'
    browse = f'<a href="index.html?area={quote(area["name"], safe="")}#collection"><small>{area["code"]} · {len(group)} cases</small><span>Browse {esc(area["label"])}</span></a>'
    return '<nav class="case-navigation" aria-label="More cases in this teaching area">' + previous + browse + following + '</nav>'


def render(source, data, case):
    assert len(PATTERN.findall(source)) == 1, f'Expected one navigation: {case["slug"]}'
    return PATTERN.sub(lambda _: navigation(data, case), source)


def sync(root=ROOT, check=False):
    data = json.loads((root/'case-registry.json').read_text())
    for case in data['cases']:
        path = root/(case['slug']+'.html')
        source = path.read_text()
        expected = render(source, data, case)
        if check:
            assert expected == source, f'Stale navigation: {path.name}; run python scripts/sync_case_navigation.py'
        elif source != expected:
            path.write_text(expected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    sync(check=parser.parse_args().check)
