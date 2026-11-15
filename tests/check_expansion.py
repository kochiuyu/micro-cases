"""Staged 121–240 registry and static-count regressions; never writes fixtures."""
import copy
import html
import re
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from sync_collection import render, check as check_counts
from sync_case_navigation import navigation, render as render_nav, sync as check_navigation
from check_registry import validate_registry


def expanded(base, total):
    data=copy.deepcopy(base)
    while len(data['cases']) < total:
        n=len(data['cases'])+1
        area=next(a for a in data['areas'] if sum(c['area']==a['name'] for c in data['cases'])<20)
        seq=sum(c['area']==area['name'] for c in data['cases'])+1
        data['cases'].append(dict(legacy_id=n,code=f"{area['code']}-{seq:02}",slug=f'fixture-{n}',area=area['name'],title=f'Fixture {n}'))
    return data


def check(root=ROOT):
    data=json.loads((root/'case-registry.json').read_text())
    # Use the original baseline even once production has grown past 121.
    base=copy.deepcopy(data);base['cases']=[c for c in base['cases'] if c['legacy_id']<=120]
    for total in (120,121,129,130,131,239,240):
        fixture=expanded(base,total)
        validate_registry(fixture)
        rendered=render((root/'index.html').read_text(),fixture)
        assert f'{total} decisions · 12 teaching areas' in rendered
        assert render(rendered,fixture)==rendered, 'Rendering is not idempotent'
        tiles=re.findall(r'class="area-tile"[^>]+data-area="([^"]+)"[^>]*>.*?<small>(\d+) cases</small>', rendered)
        assert len(tiles)==len(fixture['areas'])
        for area,count in tiles:
            assert int(count)==sum(c['area']==html.unescape(area) for c in fixture['cases'])
        assert re.search(r'id="count"[^>]*>'+str(total)+r' cases</span>',rendered)
    for kind in ('old-code','old-slug','old-area','gap','duplicate','overflow'):
        bad=expanded(base,121)
        if kind=='old-code':bad['cases'][0]['code']='HSP-02'
        elif kind=='old-slug':bad['cases'][0]['slug']='changed-original-url'
        elif kind=='old-area':bad['cases'][0]['area']=bad['areas'][0]['name']
        elif kind=='gap':bad['cases'][-1]['code']='ACC-12'
        elif kind=='duplicate':bad['cases'][-1]['legacy_id']=120
        else:
            bad=expanded(base,130)
            bad['cases'].append(dict(legacy_id=131,code='ACC-21',slug='overflow',area=bad['areas'][0]['name'],title='Overflow'))
        try:validate_registry(bad)
        except (AssertionError,KeyError):pass
        else:raise AssertionError('Expansion mutation escaped: '+kind)
    # Exercise every area's first, middle and last navigation at uneven/full sizes.
    for total in (120, 121, 131, 239, 240):
        fixture = expanded(base, total)
        for area in fixture['areas']:
            group = sorted((c for c in fixture['cases'] if c['area'] == area['name']), key=lambda c: c['legacy_id'])
            for i in sorted({0, len(group)//2, len(group)-1}):
                case = group[i]
                original = '<main>Unchanged teaching body</main><nav class="case-navigation">Old</nav><footer>Unchanged footer</footer>'
                updated = render_nav(original, fixture, case)
                assert render_nav(updated, fixture, case) == updated
                assert updated.startswith('<main>Unchanged teaching body</main>') and updated.endswith('<footer>Unchanged footer</footer>')
                assert f"{area['code']} · {len(group)} cases" in updated
                assert (f'Previous · {group[i-1]["code"]}' in updated) if i else ('First case in this area' in updated)
                assert (f'Next · {group[i+1]["code"]}' in updated) if i+1 < len(group) else ('Last case in this area' in updated)
                assert ('href="'+group[i-1]['slug']+'.html"' in updated) if i else True
                assert ('href="'+group[i+1]['slug']+'.html"' in updated) if i+1 < len(group) else True
    check_navigation(root, check=True)
    check_counts(root)
    print('PASS: staged 120–240 registries, immutable baseline, area limits and derived static counts.')


if __name__=='__main__':check()
