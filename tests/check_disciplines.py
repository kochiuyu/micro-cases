"""Check primary-area metadata and execute the real browse script with a tiny DOM.

No browser dependencies: structural/accessibility assertions complement a Node VM
regression. Live keyboard, screen-reader and responsive QA remain separate.
"""
from html.parser import HTMLParser
from pathlib import Path
import copy
import json
import re
import subprocess
from check_registry import load_registry

ROOT = Path(__file__).resolve().parents[1]


class Browse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.card = None
        self.labels = []
        self.selects = {}
        self.select = None
        self.option = None
        self.ids = {}
        self.script = None
        self.scripts = []
        self.in_discipline = False
        self.area_buttons = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            assert a['id'] not in self.ids, 'Duplicate DOM id'
            self.ids[a['id']] = (tag, a, bool(self.labels))
        if 'area-tile' in a.get('class', '').split():
            self.area_buttons.append((tag, a))
        if tag == 'label':
            self.labels.append(a)
        if tag == 'a' and 'card' in a.get('class', '').split():
            self.card = dict(attrs=a, text=[], labels=[])
            self.cards.append(self.card)
        if self.card and 'discipline' in a.get('class', '').split():
            assert tag == 'span', 'Expected visible discipline span'
            assert 'hidden' not in a and a.get('aria-hidden') != 'true'
            self.in_discipline = True
            self.card['labels'].append([])
        if tag == 'select':
            self.select = a.get('id')
            self.selects[self.select] = []
        if tag == 'option' and self.select:
            self.option = dict(value=a.get('value'), text=[])
            self.selects[self.select].append(self.option)
        if tag == 'script' and 'src' not in a:
            self.script = []
            self.scripts.append(self.script)

    def handle_data(self, data):
        if self.card:
            self.card['text'].append(data)
            if self.in_discipline:
                self.card['labels'][-1].append(data)
        if self.option is not None:
            self.option['text'].append(data)
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == 'a':
            self.card = None
        if tag == 'span':
            self.in_discipline = False
        if tag == 'label':
            self.labels.pop()
        if tag == 'option':
            self.option = None
        if tag == 'select':
            self.select = None
        if tag == 'script':
            self.script = None


def values(options):
    return [o['value'] if o['value'] is not None else ''.join(o['text']).strip()
            for o in options]


def ledger_map(text):
    areas, mapping = [], {}
    for area, nums in re.findall(r'^\| ([^|]+?) \| ([\d, ]+) \|[^\n]+$', text, re.M):
        area = area.strip()
        assert area not in areas, 'Duplicate ledger discipline'
        areas.append(area)
        for number in map(int, nums.split(',')):
            assert number not in mapping, 'Repeated ledger case'
            mapping[number] = area
    assert len(areas) == 12, 'Expected twelve primary teaching areas'
    return areas, mapping


def validate(p, areas, mapping):
    options = values(p.selects['discipline'])
    assert len(options) == 13 and options.count('') == 1
    assert len(set(options)) == len(options) and set(options) == set(areas) | {''}, 'Area options differ from ledger'
    topics = values(p.selects['concept'])
    assert len(set(topics)) == len(topics) and '' in topics
    durations = values(p.selects['time'])
    assert '0' in durations and all(v.isdigit() for v in durations)
    seen = set()
    for c in p.cards:
        raw = c['attrs'].get('data-case-id', '')
        assert raw.isdigit(), 'Missing stable card ID'
        n = int(raw)
        assert n not in seen and n in mapping, 'Duplicate or unknown card'
        seen.add(n)
        a = c['attrs']
        assert a.get('data-discipline') == mapping[n], f'Case {n}: wrong primary area'
        assert len(c['labels']) == 1 and ''.join(c['labels'][0]).strip() == mapping[n], f'Case {n}: missing/wrong visible label'
        assert 'hidden' not in a, 'Cards must be available without JavaScript'
        tokens = a.get('data-concepts', '').split('|')
        assert all(t and t in topics for t in tokens), f'Case {n}: unselectable topic'
        assert a.get('data-minutes', '').isdigit() and int(a['data-minutes']) > 0
    assert seen == set(mapping), 'Ledger/card case coverage differs'
    for name in ('discipline', 'concept', 'time'):
        assert p.ids[name][0] == 'select' and p.ids[name][2], f'{name}: native select needs a label'
    assert p.ids['reset-filters'][0] == 'button' and p.ids['reset-filters'][1].get('type') == 'button'
    assert p.ids['count'][1].get('role') == 'status', 'Result count needs status role'
    assert p.ids['search'][0] == 'input' and p.ids['search'][2], 'Search needs native labelled input'
    assert p.ids['show-more'][0] == 'button' and p.ids['show-more'][1].get('type') == 'button'
    assert 'hidden' in p.ids['show-more'][1], 'No-JS show-more must be hidden'
    assert 'hidden' in p.ids['area-shortcuts'][1]
    assert len(p.area_buttons) == 12
    assert {a.get('data-area') for tag,a in p.area_buttons} == set(areas)
    assert all(tag=='button' and a.get('type')=='button' for tag,a in p.area_buttons)

    assert 'hidden' in p.ids['filters'][1], 'Hide nonfunctional filters without JS'


NODE = r"""
const vm=require('node:vm'),assert=require('node:assert/strict');
let input='';process.stdin.on('data',s=>input+=s);process.stdin.on('end',()=>{
 const p=JSON.parse(input);
 function boot(query='') {
  const controls={},location={href:'https://example.org/micro-cases/index.html'+query};let focused=null;
  for(const [id,options] of Object.entries(p.selects)) controls['#'+id]={value:options[0],options:options.map(value=>({value}))};
  for(const id of ['filters','area-shortcuts','count','reset-filters','show-more'])controls['#'+id]={hidden:true,textContent:''};
  controls['#search']={value:''};
  const cards=p.cards.map(c=>({dataset:{discipline:c.attrs['data-discipline'],concepts:c.attrs['data-concepts'],minutes:c.attrs['data-minutes'],caseId:c.attrs['data-case-id'],caseCode:c.attrs['data-case-code']},textContent:c.text.join(' '),hidden:false,focus(){focused=this}}));
  const areas=p.areaButtons.map(a=>({dataset:{area:a['data-area']},attrs:{},setAttribute(k,v){this.attrs[k]=v}}));
  const doc={querySelector:s=>{assert(s in controls,'Unexpected selector '+s);return controls[s]},querySelectorAll:s=>{if(s==='.card')return cards;if(s==='.area-tile')return areas;throw Error('Unexpected selector '+s)}};
  const history={replaceState(a,b,url){location.href=new URL(url,location.href).href}};
  vm.runInNewContext(p.script,{document:doc,window:{location,history},URL},{timeout:1000});
  assert.equal(controls['#filters'].hidden,false);assert.equal(controls['#area-shortcuts'].hidden,false);
  let limit=24;
  const norm=s=>s.toLowerCase().trim().replace(/\s+/g,' ');
  function check(sync=false){
   const d=controls['#discipline'].value,c=controls['#concept'].value,t=controls['#time'].value,q=controls['#search'].value;
   const tokens=norm(q).split(' ').filter(Boolean),legacy=norm(q).match(/^(?:case\s*)?(\d+)$/);
   const matches=cards.filter(x=>(!d||x.dataset.discipline===d)&&(!c||x.dataset.concepts.split('|').includes(c))&&(!Number(t)||Number(x.dataset.minutes)<=Number(t))&&(legacy?Number(x.dataset.caseId)===Number(legacy[1]):tokens.every(z=>norm(x.textContent+' '+x.dataset.caseCode+' '+x.dataset.caseId+' case '+x.dataset.caseId).includes(z))));
   const visible=matches.slice(0,limit);assert.deepEqual(cards.filter(x=>!x.hidden),visible,'Wrong intersection/pagination');
   const status=controls['#count'].textContent;
   if(matches.length===0){assert(/no cases/i.test(status));assert(/reset/i.test(status))}
   else if(matches.length>visible.length)assert.equal(status,`Showing ${visible.length} of ${matches.length} cases`);
   else assert.equal(status,`${matches.length} ${matches.length===1?'case':'cases'}`);
   assert.equal(controls['#show-more'].hidden,visible.length>=matches.length);
   if(visible.length<matches.length)assert.equal(controls['#show-more'].textContent,`Show ${Math.min(24,matches.length-visible.length)} more cases`);
   for(const a of areas)assert.equal(a.attrs['aria-pressed'],String(a.dataset.area===d));
   if(sync){let u=new URL(location.href);for(const [k,v] of [['q',q.trim()],['area',d],['topic',c],['time',t==='0'?'':t]])assert.equal(u.searchParams.get(k),v||null)}
   return matches;
  }
  function change(id,value){controls['#'+id].value=value;limit=24;controls['#'+id][id==='search'?'oninput':'onchange']();check(true)}
  function more(){const before=cards.filter(c=>!c.hidden);limit+=24;controls['#show-more'].onclick();const matches=check();if(matches.length>before.length)assert.equal(focused,matches[before.length])}
  function reset(){limit=24;controls['#reset-filters'].onclick();assert.equal(controls['#search'].value,'');assert.equal(controls['#discipline'].value,'');assert.equal(controls['#concept'].value,'');assert.equal(controls['#time'].value,'0');check(true)}
  return {controls,cards,areas,check,change,more,reset,location};
 }
 const b=boot();b.check();while(!b.controls['#show-more'].hidden)b.more();assert.equal(b.cards.filter(c=>!c.hidden).length,p.cards.length);
 b.change('search','NONEXISTENT XYZ');assert.equal(b.cards.filter(c=>!c.hidden).length,0);b.reset();assert.equal(b.cards.filter(c=>!c.hidden).length,24);
 for(const d of p.selects.discipline)for(const c of p.selects.concept){b.change('discipline',d);b.change('concept',c);for(const t of p.selects.time)b.change('time',t)}
 b.reset();for(const q of [p.cards[0].attrs['data-case-code'],'  '+p.cards[0].attrs['data-case-code'].toLowerCase()+'  ','case 120','119','Case119','Case 119','001','999','risk capacity','& <script>'])b.change('search',q);
 b.reset();for(const q of ['119','Case119','Case 119']){b.change('search',q);assert.deepEqual(b.cards.filter(c=>!c.hidden).map(c=>c.dataset.caseId),['119'])}b.reset();b.more();b.change('time','0');assert.equal(b.cards.filter(c=>!c.hidden).length,24);
 for(const a of b.areas){b.change('search','impossible');b.change('concept',p.selects.concept[1]);a.onclick();assert.equal(b.controls['#search'].value,'');assert.equal(b.controls['#concept'].value,'');assert.equal(b.controls['#time'].value,'0');b.check(true)}
 const q=new URLSearchParams({area:p.selects.discipline[1],topic:p.selects.concept[1],time:p.selects.time[1],q:'risk'}).toString();const deep=boot('?'+q+'#catalogue');deep.check();assert.equal(deep.controls['#search'].value,'risk');assert.equal(deep.controls['#discipline'].value,p.selects.discipline[1]);deep.change('search','');assert(new URL(deep.location.href).hash==='#catalogue');
 const bad=boot('?area=invalid&topic=invalid&time=-1&q=ACC-01');bad.check();assert.equal(bad.controls['#discipline'].value,'');assert.equal(bad.controls['#concept'].value,'');assert.equal(bad.controls['#time'].value,'0');assert.equal(bad.controls['#search'].value,'ACC-01');
 console.log('PASS: real index search, filters,24-card pagination,show-more focus,area shortcuts,reset and URL state.');
});
"""


def check(root=ROOT):
    p = Browse()
    p.feed((root / 'index.html').read_text())
    areas, mapping = ledger_map((root / 'planning/collection-roadmap.md').read_text())
    registry, entries = load_registry(root)
    assert {n: c['area'] for n, c in entries.items()} == mapping, 'Registry/ledger mismatch'
    validate(p, areas, mapping)
    # Mutate parsed structures only: never rewrite the shared checkout.
    for change in ('area', 'label', 'option', 'missing', 'topic'):
        bad = copy.deepcopy(p)
        if change == 'area':
            bad.cards[0]['attrs']['data-discipline'] = 'Wrong area'
        elif change == 'label':
            bad.cards[0]['labels'] = []
        elif change == 'option':
            bad.selects['discipline'].append(copy.deepcopy(bad.selects['discipline'][1]))
        elif change == 'missing':
            bad.cards.pop()
        else:
            bad.cards[0]['attrs']['data-concepts'] = 'Unselectable'
        try:
            validate(bad, areas, mapping)
        except AssertionError:
            pass
        else:
            raise AssertionError(f'Mutation escaped validation: {change}')
    payload = dict(cards=[dict(attrs=c['attrs'],text=c['text']) for c in p.cards],
                   areaButtons=[a for tag,a in p.area_buttons],
                   selects={k: values(v) for k, v in p.selects.items()},
                   script='\n'.join(''.join(s) for s in p.scripts))
    # Exhaustive area/topic/time combinations grow with the catalogue; allow
    # runtime headroom without reducing assertions or the per-VM deadline.
    result = subprocess.run(['node', '-e', NODE], input=json.dumps(payload),
                            text=True, capture_output=True, timeout=300)
    assert result.returncode == 0, result.stdout + result.stderr
    print(result.stdout.strip())
    for target in (121, 240, 241, 360, 361, 480, 481, 490, 491, 493):
        fixture = copy.deepcopy(payload)
        fixture['cards'] = [c for c in fixture['cards'] if int(c['attrs']['data-case-id']) <= target]
        while len(fixture['cards']) < target:
            i = len(fixture['cards'])
            area = next(a for a in registry['areas'] if a['code']==('FIN' if i>=490 or (i+1)%2 else 'ECO'))
            prototype=next(card for card in payload['cards'] if card['attrs']['data-discipline']==area['name'])
            c = copy.deepcopy(prototype)
            c['attrs']['data-case-id'] = str(i + 1)
            c['attrs']['data-case-code'] = c['attrs']['data-case-code'].split('-')[0] + '-' + str(i-444 if i>=490 else 41 + (i-480)//2)
            fixture['cards'].append(c)
        result = subprocess.run(['node', '-e', NODE], input=json.dumps(fixture), text=True, capture_output=True, timeout=300)
        assert result.returncode == 0, result.stdout + result.stderr
    print('PASS: synthetic 121/240/241/360/361/480/481/490/491/493-card browse flows.')
    print(f'PASS: {len(p.cards)} cards match all 12 ledger areas, visible labels and selectors; mutations rejected.')


if __name__ == '__main__':
    check()
