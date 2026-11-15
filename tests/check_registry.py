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
 assert len(cases)==120
 assert {c['legacy_id'] for c in cases}==set(range(1,121))
 for key in ('legacy_id','code','slug'):
  assert len({c[key] for c in cases})==120,f'Duplicate {key}'
 for area in areas:
  group=sorted([c for c in cases if c['area']==area['name']],key=lambda c:c['legacy_id'])
  assert len(group)==10,area['name']
  assert [c['code'] for c in group]==[f"{area['code']}-{i:02}" for i in range(1,11)],area['name']
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

def check_pages(root,data):
 for c in data['cases']:
  page=Page();page.feed((root/(c['slug']+'.html')).read_text())
  assert 'case-navigation.css' in page.css,c['slug']
  assert [''.join(v).strip() for v in page.codes]==[c['code']],c['slug']
  group=sorted([x for x in data['cases'] if x['area']==c['area']],key=lambda x:x['legacy_id']);i=group.index(c)
  expected=[]
  if i:expected.append(group[i-1]['slug']+'.html')
  if i<9:expected.append(group[i+1]['slug']+'.html')
  direct=[l for l in page.links if urlsplit(l).path!='index.html']
  assert direct==expected,(c['slug'],direct,expected)
  browses=[l for l in page.links if urlsplit(l).path=='index.html'];assert len(browses)==1,c['slug']
  u=urlsplit(browses[0]);assert parse_qs(u.query)=={'area':[c['area']]} and u.fragment=='collection',c['slug']
 assert (root/'case-navigation.css').is_file()

def check(root=ROOT):
 import copy
 data,mapping=load_registry(root)
 check_pages(root,data)
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
 print('PASS: stable120 IDs,12 area codes,ordered01–10 sequences, all120 neighbour/browse links and registry mutations.')
if __name__=='__main__':check()
