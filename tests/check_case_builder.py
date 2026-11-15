"""Isolated builder regression tests. Never generates cases in the working repo."""
import contextlib
import copy
import importlib.util
import io
import json
import re
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'scripts/build_case.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)


def payload(repo):
    reg=json.loads((repo/'case-registry.json').read_text())
    area=next(a for a in reg['areas'] if sum(c['area']==a['name'] for c in reg['cases'])<30)
    number=max(c['legacy_id'] for c in reg['cases'])+1
    seq=sum(c['area']==area['name'] for c in reg['cases'])+1
    return dict(number=number,code=f"{area['code']}-{seq:02}",slug='builder-test-only',title='A fixture. Not a publication.',discipline=area['name'],topics=['Builder fixture'],teaser='An isolated test.',alt='A test illustration.',news_heading='Context',news='<p>Fictional context.</p>',opening='<p>A fictional decision.</p>',exhibit='<table><tr><th>Option</th><th>Units</th></tr><tr><td>A</td><td>2</td></tr></table>',exhibit_md='| Option | Units |\n| --- | --- |\n| A | 2 |',q1='Which option?',round2='<p>New fictional context.</p>',q2='Keep or change?',sections=[['Debrief','<p>Compare the evidence.</p>'],['Instructor note','<p>Discuss the evidence for twelve minutes.</p>']],notes='All facts are fictional test data.',sources=[[f'https://example.org/source-{i}','Fixture source','Not a real reviewed source.'] for i in range(5)],slides=[['Title','<p>A fixture.</p>'],['Context','<p>Fictional context.</p>'],['Decision','<p>Which option?</p>'],['Reveal','<p>New fictional context.</p>'],['Second decision','<p>Keep or change?</p>']])


def reduce_to_original_baseline(repo, limit=120):
    """Keep a protected historical prefix independent of production occupancy."""
    reg_path=repo/'case-registry.json'
    reg=json.loads(reg_path.read_text())
    reg['cases']=[c for c in reg['cases'] if c['legacy_id']<=limit]
    reg_path.write_text(json.dumps(reg),encoding='utf-8')
    keep={c['slug']+'.html' for c in reg['cases']}
    index=repo/'index.html'
    def card(match):
        href=re.search(r'href="([^"]+)"',match[0])
        return match[0] if href and href[1] in keep else ''
    source=re.sub(r'<a class="card".*?</a>',card,index.read_text(),flags=re.S)
    counts=builder.module(repo/'scripts/sync_collection.py','fixture_counts')
    index.write_text(counts.render(source,reg),encoding='utf-8')


class BuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo=Path(self.temp.name)/'repo'
        # Text-only disposable copy, never production writes or art generation.
        for p in ROOT.rglob('*'):
            if '.git' in p.parts or '__pycache__' in p.parts or not p.is_file() or p.suffix not in ('.html','.md','.json','.py'):continue
            target=self.repo/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
        reduce_to_original_baseline(self.repo,240)
        self.x=payload(self.repo)
        self.input=Path(self.temp.name)/'input.json'

    def snapshot(self):
        return {str(p.relative_to(self.repo)):p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}

    def run_builder(self,write=False):
        self.input.write_text(json.dumps(self.x),encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()):
            builder.main([str(self.input),'--repo',str(self.repo)]+(['--write'] if write else []))

    def reject(self,needle):
        before=self.snapshot()
        with self.assertRaisesRegex(ValueError,needle):self.run_builder()
        self.assertEqual(before,self.snapshot())

    def test_dry_run_and_portable_default(self):
        self.assertEqual(builder.ROOT,ROOT)
        before=self.snapshot();self.run_builder();self.assertEqual(before,self.snapshot())

    def test_original_fixture_remains_available(self):
        original=(self.repo/'tests/fixtures/original-case-identities.json').read_bytes()
        reduce_to_original_baseline(self.repo)
        self.assertEqual(len(json.loads((self.repo/'case-registry.json').read_text())['cases']),120)
        self.assertEqual((self.repo/'tests/fixtures/original-case-identities.json').read_bytes(),original)

    def stage_published(self, total):
        # Restore real protected identities before adding synthetic unpublished slots.
        reg=json.loads((ROOT/'case-registry.json').read_text())
        reg['cases']=[c for c in reg['cases'] if c['legacy_id']<=240]
        source=(ROOT/'index.html').read_text()
        keep={c['slug']+'.html' for c in reg['cases']}
        source=re.sub(r'<a class="card".*?</a>',lambda m:m[0] if re.search(r'href="([^"]+)"',m[0])[1] in keep else '',source,flags=re.S)
        first=source.index('<a class="card"')
        additions=[]
        template=(self.repo/(reg['cases'][0]['slug']+'.html')).read_text()
        while len(reg['cases'])<total:
            n=len(reg['cases'])+1
            area=next(a for a in reg['areas'] if sum(c['area']==a['name'] for c in reg['cases'])<30)
            seq=sum(c['area']==area['name'] for c in reg['cases'])+1
            slug=f'stage-fixture-{n}'
            reg['cases'].append(dict(legacy_id=n,code=f"{area['code']}-{seq:02}",slug=slug,title='Fixture',area=area['name']))
            (self.repo/(slug+'.html')).write_text(template)
            additions.append(f'<a class="card" href="{slug}.html">Fixture</a>')
        (self.repo/'case-registry.json').write_text(json.dumps(reg))
        (self.repo/'index.html').write_text(source[:first]+''.join(additions)+source[first:])

    def test_staged_241_and_360_and_overflow(self):
        for before in (240,359):
            with self.subTest(before=before):
                self.stage_published(before)
                self.x=payload(self.repo)
                self.x['slug']=f'builder-stage-{before+1}'
                (self.repo/(self.x['slug']+'-scene.jpg')).write_bytes(b'test-only')
                self.run_builder(write=True)
                reg=json.loads((self.repo/'case-registry.json').read_text())
                self.assertEqual(len(reg['cases']),before+1)
                ledger=(self.repo/'planning/collection-roadmap.md').read_text()
                self.assertIn(f'**{360-before-1} approved editorial slots**',ledger)
                self.assertIn(f'{before+1} decisions · 12 teaching areas',(self.repo/'index.html').read_text())
        self.x['number']=361;self.x['code']='ACC-31';self.x['slug']='overflow-test'
        self.reject('121–360')

    def test_area_overflow_and_frozen_identity_rejected(self):
        self.stage_published(250)
        self.x=payload(self.repo)
        reg=json.loads((self.repo/'case-registry.json').read_text())
        self.x['discipline']=reg['areas'][0]['name'];self.x['code']='ACC-31'
        self.reject('Wrong next area code')
        self.x=payload(self.repo)
        reg['cases'][239]['slug']='mutated-published-url'
        (self.repo/'case-registry.json').write_text(json.dumps(reg))
        self.reject('Published identity changed')

    def test_instructor_note_required(self):
        self.x['sections']=[row for row in self.x['sections'] if row[0]!='Instructor note']
        self.reject('dedicated Instructor note')
        self.x=payload(self.repo)
        self.x['sections'].append(['Instructor note','<p>Duplicate.</p>'])
        self.reject('dedicated Instructor note')

    def test_metadata(self):
        original=copy.deepcopy(self.x)
        for key,value,error in [('number',True,'integer'),('topics',[],'Topics'),('slug','../escape','Unsafe slug'),('discipline','Unknown','Unknown primary'),('sources',[['bad']],'Malformed sources')]:
            with self.subTest(key=key):
                self.x=copy.deepcopy(original);self.x[key]=value;self.reject(error)

    def test_prompts(self):
        self.x['slides'][2][1]='<p>No decision here.</p>';self.reject('exactly once')
        self.x=payload(self.repo);self.x['slides'].append(['Duplicate','<p>Which option?</p>']);self.reject('exactly once')
        self.x=payload(self.repo);self.x['slides'][2],self.x['slides'][4]=self.x['slides'][4],self.x['slides'][2];self.reject('precede')

    def test_no_body_links_or_active_html(self):
        for bad in ['<a href="/elsewhere">Read this</a>','<img src="x">','<p onclick="alert(1)">Bad</p>','<script>alert(1)</script>']:
            with self.subTest(bad=bad):self.x['opening']=bad;self.reject('HTML')

    def test_gap_duplicate_and_existing_output(self):
        self.x['number']+=1;self.reject('follow existing')
        self.x=payload(self.repo);self.x['code']='ACC-01';self.reject('Existing slug, ID or code')
        self.x=payload(self.repo);(self.repo/(self.x['slug']+'.html')).write_text('Keep me');self.reject('Existing output')

    def test_success_and_metadata(self):
        (self.repo/(self.x['slug']+'-scene.jpg')).write_bytes(b'fixture only: not visual QA')
        before=self.snapshot();self.run_builder(write=True)
        page=(self.repo/(self.x['slug']+'.html')).read_text()
        self.assertIn('data-case-code="'+self.x['code']+'"',page)
        self.assertIn('<title>'+self.x['code'],page)
        self.assertIn('aria-label="'+self.x['code']+' classroom presentation"',page)
        self.assertIn('**Student question:** '+self.x['q1'],(self.repo/'authoring'/(self.x['slug']+'.md')).read_text())
        self.assertEqual(json.loads((self.repo/'case-registry.json').read_text())['cases'][-1]['code'],self.x['code'])
        # Existing case content changes only inside its navigation.
        nav=builder.module(self.repo/'scripts/sync_case_navigation.py','test_nav')
        reg=json.loads(before['case-registry.json'])
        for case in reg['cases']:
            name=case['slug']+'.html'
            self.assertEqual(nav.PATTERN.sub('',before[name].decode()),nav.PATTERN.sub('',(self.repo/name).read_text()))

    def test_write_requires_art(self):
        before=self.snapshot()
        with self.assertRaisesRegex(ValueError,'illustration'):self.run_builder(write=True)
        self.assertEqual(before,self.snapshot())

    def test_rollback_and_concurrent_modification(self):
        old=self.repo/'rollback.txt';new=self.repo/'new-file.txt';old.write_text('original')
        originals={old:b'original',new:None};outputs={old:'changed',new:'new'}
        def failure():raise RuntimeError('injected verification failure')
        with self.assertRaisesRegex(RuntimeError,'injected'):
            builder.write_outputs(outputs,originals,{},failure)
        self.assertEqual(old.read_bytes(),b'original');self.assertFalse(new.exists())
        old.write_text('concurrent work')
        with self.assertRaisesRegex(ValueError,'Concurrent modification'):
            builder.write_outputs(outputs,originals,{},lambda:None)
        self.assertEqual(old.read_text(),'concurrent work');self.assertFalse(new.exists())

    def test_markdown_table(self):
        rendered=builder.markdown(self.x['exhibit'])
        self.assertIn('| Option | Units |',rendered)
        self.assertIn('| --- | --- |',rendered)
        self.assertIn('| A | 2 |',rendered)


if __name__=='__main__':unittest.main()
