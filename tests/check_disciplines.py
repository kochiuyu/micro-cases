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

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            assert a['id'] not in self.ids, 'Duplicate DOM id'
            self.ids[a['id']] = (tag, a, bool(self.labels))
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
        ids = re.findall(r'\bCase\s+(\d+)\b', ' '.join(c['text']))
        assert len(ids) == 1, 'Missing or ambiguous card number'
        n = int(ids[0])
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
    assert 'hidden' in p.ids['filters'][1], 'Hide nonfunctional filters without JS'


NODE = r'''
const vm=require('node:vm'),assert=require('node:assert/strict');
let input='';process.stdin.on('data',s=>input+=s);process.stdin.on('end',()=>{
 const p=JSON.parse(input), controls={};
 for(const [id,options] of Object.entries(p.selects)) controls['#'+id]={value:options[0]};
 controls['#filters']={hidden:true};controls['#count']={textContent:''};controls['#reset-filters']={};
 const cards=p.cards.map(c=>({dataset:{discipline:c['data-discipline'],concepts:c['data-concepts'],minutes:c['data-minutes']},hidden:false}));
 const doc={querySelector:s=>{assert(s in controls,'Unexpected selector '+s);return controls[s]},querySelectorAll:s=>{assert.equal(s,'.card');return cards}};
 vm.runInNewContext(p.script,{document:doc}, {timeout:1000});
 assert.equal(controls['#filters'].hidden,false);
 function check(d,c,t){
  const expected=cards.map(x=>(!d||x.dataset.discipline===d)&&(!c||x.dataset.concepts.split('|').includes(c))&&(!Number(t)||Number(x.dataset.minutes)<=Number(t)));
  assert.deepEqual(cards.map(x=>!x.hidden),expected,'Wrong filter intersection');
  const count=expected.filter(Boolean).length,status=controls['#count'].textContent;
  if(count) assert(new RegExp('\\b'+count+'\\s+case').test(status),'Incorrect result count');
  else {assert(/no cases/i.test(status));assert(/reset/i.test(status),'No-result guidance must offer reset');}
  assert.equal(controls['#discipline'].value,d);assert.equal(controls['#concept'].value,c);assert.equal(controls['#time'].value,t);
 }
 check('','','0');
 for(let cycle=0;cycle<2;cycle++) for(const d of p.selects.discipline) for(const c of p.selects.concept) for(const t of p.selects.time){
  const vals={discipline:d,concept:c,time:t};
  for(const id of ['discipline','concept','time']) {controls['#'+id].value=vals[id];assert.equal(typeof controls['#'+id].onchange,'function');controls['#'+id].onchange();}
  check(d,c,t);
 }
 controls['#reset-filters'].onclick();check('','','0');
 console.log('PASS: real index JS intersections, empty results, repeated changes and reset.');
});
'''


def check(root=ROOT):
    p = Browse()
    p.feed((root / 'index.html').read_text())
    areas, mapping = ledger_map((root / 'planning/collection-roadmap.md').read_text())
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
    payload = dict(cards=[c['attrs'] for c in p.cards],
                   selects={k: values(v) for k, v in p.selects.items()},
                   script='\n'.join(''.join(s) for s in p.scripts))
    result = subprocess.run(['node', '-e', NODE], input=json.dumps(payload),
                            text=True, capture_output=True, timeout=30)
    assert result.returncode == 0, result.stdout + result.stderr
    print(result.stdout.strip())
    print(f'PASS: {len(p.cards)} cards match all 12 ledger areas, visible labels and selectors; mutations rejected.')


if __name__ == '__main__':
    check()
