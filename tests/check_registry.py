"""Validate stable publication identity separately from visible teaching-area codes."""
import json,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,parse_qs
ROOT=Path(__file__).resolve().parents[1]
CODES=('ACC','FIN','MKT','OPS','PPL','STR','ENT','IS','GVR','SUS','ECO','HSP')
def validate_registry(data):
 assert data['schema_version']==1
 areas=data['areas'];cases=data['cases']
 assert len(areas)==12 and [a['code'] for a in areas]==list(CODES)
 names=[a['name'] for a in areas];assert len(set(names))==12
 assert all(a.get('label','').strip() for a in areas)
 assert 120 <= len(cases) <= 495, 'Expected staged expansion from 120 to 495 cases'
 assert all(type(c['legacy_id']) is int for c in cases), 'IDs must be integers'
 assert {c['legacy_id'] for c in cases}==set(range(1,len(cases)+1)), 'Permanent IDs must be contiguous'
 baseline=json.loads((ROOT/'tests/fixtures/original-case-identities.json').read_text())
 current={c['legacy_id']:c for c in cases}
 for original in baseline:
  assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Original identity changed: '+str(original['legacy_id'])
 # Historical staged fixtures may end before 240; every identity present is frozen.
 frozen=json.loads((ROOT/'tests/fixtures/published-240-case-identities.json').read_text())
 assert len(frozen)==240 and frozen[:120]==baseline, 'Identity snapshots disagree'
 for original in frozen:
  if original['legacy_id'] in current:
   assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Published identity changed: '+str(original['legacy_id'])
 latest=json.loads((ROOT/'tests/fixtures/published-360-case-identities.json').read_text())
 assert len(latest)==360 and latest[:240]==frozen, 'Identity snapshots disagree'
 for original in latest:
  if original['legacy_id'] in current:
   assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Published identity changed: '+str(original['legacy_id'])
 approved=json.loads((ROOT/'tests/fixtures/published-480-case-identities.json').read_text())
 assert len(approved)==480 and approved[:360]==latest, 'Identity snapshots disagree'
 for original in approved:
  if original['legacy_id'] in current:
   assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Published identity changed: '+str(original['legacy_id'])
 final490=json.loads((ROOT/'tests/fixtures/published-490-case-identities.json').read_text())
 assert len(final490)==490 and final490[:480]==approved, 'Identity snapshots disagree'
 for original in final490[480:]:
  if original['legacy_id'] in current:
   assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Published identity changed: '+str(original['legacy_id'])
 final493=json.loads((ROOT/'tests/fixtures/published-493-case-identities.json').read_text())
 assert len(final493)==493 and final493[:490]==final490, 'Identity snapshots disagree'
 for original in final493[490:]:
  if original['legacy_id'] in current:
   assert all(current[original['legacy_id']][key]==value for key,value in original.items()), 'Published identity changed: '+str(original['legacy_id'])
 for c in cases:
  if c['legacy_id']>490:
   assert c['code']=='FIN-'+str(c['legacy_id']-445), 'Unapproved expansion slot: '+str(c['legacy_id'])
  elif c['legacy_id']>480:
   expected=('FIN' if c['legacy_id']%2 else 'ECO')+'-'+str(41+(c['legacy_id']-481)//2)
   assert c['code']==expected, 'Unapproved expansion slot: '+str(c['legacy_id'])
 for key in ('legacy_id','code','slug'):
  assert len({c[key] for c in cases})==len(cases),f'Duplicate {key}'
 for area in areas:
  group=sorted([c for c in cases if c['area']==area['name']],key=lambda c:c['legacy_id'])
  assert 10 <= len(group) <= (50 if area['code']=='FIN' else 45 if area['code']=='ECO' else 40),area['name']
  assert [c['code'] for c in group]==[f"{area['code']}-{i:02}" for i in range(1,len(group)+1)],area['name']
 for c in cases:
  assert c['area'] in names and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',c['slug'])
  assert isinstance(c['title'],str) and c['title'].strip()
 return {c['legacy_id']:c for c in cases}
def load_registry(root=ROOT):
 data=json.loads((root/'case-registry.json').read_text());return data,validate_registry(data)
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.nav=False;self.links=[];self.css=[];self.codes=[];self.code=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='link' and a.get('rel')=='stylesheet':self.css.append(a.get('href'))
  if tag=='nav' and 'case-navigation' in a.get('class','').split():
   assert not self.nav;self.nav=True
   assert a.get('aria-label'), 'Navigation label missing'
  if self.nav and tag=='a':self.links.append(a.get('href'))
  if 'case-code' in a.get('class','').split():
   assert 'hidden' not in a and a.get('aria-hidden')!='true'
   self.code=[];self.codes.append(self.code)
 def handle_data(self,text):
  if self.code is not None:self.code.append(text)
 def handle_endtag(self,tag):
  if tag=='nav':self.nav=False
  if tag=='span':self.code=None

def check_identity_surfaces(source, case):
 from html import unescape
 code = case['code']
 title = re.findall(r'<title>(.*?)</title>', source, re.S)
 assert len(title) == 1 and unescape(title[0]).startswith(code + ' · '), (case['slug'], 'browser title code')
 header = re.findall(r'<header\b[^>]*>(.*?)</header>', source, re.S)
 assert len(header) == 1, (case['slug'], 'header missing')
 identity = re.findall(r'<strong[^>]*>(.*?)</strong>', header[0], re.S)
 assert identity == ['MICRO CASE · ' + code], (case['slug'], 'header code')
 dialogs = re.findall(r'<dialog\b[^>]*aria-label="([^"]*)"', source)
 assert dialogs == [code + ' classroom presentation'], (case['slug'], 'presentation label code')
 counters = re.findall(r"document\.querySelector\('\#counter'\)\.textContent=([^;]+)", source)
 assert len(counters) == 1 and counters[0].startswith("'" + code + " · '+"), (case['slug'], 'presentation counter code')

def check_pages(root,data):
 for c in data['cases']:
  source=(root/(c['slug']+'.html')).read_text()
  check_identity_surfaces(source,c)
  page=Page();page.feed(source)
  assert 'case-navigation.css' in page.css,c['slug']
  assert [''.join(v).strip() for v in page.codes]==[c['code']],c['slug']
  group=sorted([x for x in data['cases'] if x['area']==c['area']],key=lambda x:x['legacy_id']);i=group.index(c)
  expected=[]
  if i:expected.append(group[i-1]['slug']+'.html')
  if i<len(group)-1:expected.append(group[i+1]['slug']+'.html')
  direct=[l for l in page.links if urlsplit(l).path!='index.html']
  assert direct==expected,(c['slug'],direct,expected)
  browses=[l for l in page.links if urlsplit(l).path=='index.html'];assert len(browses)==1,c['slug']
  u=urlsplit(browses[0]);assert parse_qs(u.query)=={'area':[c['area']]} and u.fragment=='collection',c['slug']
 assert (root/'case-navigation.css').is_file()

def check(root=ROOT):
 import copy
 data,mapping=load_registry(root)
 check_pages(root,data)
 # Changing only one surface must fail even if metadata remains correct.
 case=data['cases'][0];source=(root/(case['slug']+'.html')).read_text();code=case['code']
 for before in ('<title>'+code+' · ', '<strong>MICRO CASE · '+code+'</strong>', 'aria-label="'+code+' classroom presentation"', "textContent='"+code+" · '+"):
  assert before in source
  bad=source.replace(before,before.replace(code,'WRONG-99'),1)
  try:check_identity_surfaces(bad,case)
  except AssertionError:pass
  else:raise AssertionError('Identity surface mutation escaped: '+before)
 for mutation in ('id','code','slug','area','order'):
  bad=copy.deepcopy(data)
  if mutation=='id':bad['cases'][0]['legacy_id']=bad['cases'][1]['legacy_id']
  elif mutation=='code':bad['cases'][0]['code']='ACC-99'
  elif mutation=='slug':bad['cases'][0]['slug']=bad['cases'][1]['slug']
  elif mutation=='area':bad['cases'][0]['area']='Wrong area'
  else:bad['areas'].reverse()
  try:validate_registry(bad)
  except AssertionError:pass
  else:raise AssertionError('Mutation escaped: '+mutation)
 from check_expansion import check as check_expansion
 check_expansion(root)
 print(f'PASS: {len(mapping)} stable IDs, 12 area codes, staged sequences, neighbour links and mutations.')
if __name__=='__main__':check()
