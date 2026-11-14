"""Keep the classroom experience self-contained; preserve optional attribution."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CaseParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = self.in_footer = False
        self.main_links = []
        self.source_links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'main': self.in_main = True
        if tag == 'footer': self.in_footer = True
        if tag == 'a' and re.match(r'https?://', attrs.get('href', '')):
            (self.source_links if self.in_footer else self.main_links).append(attrs['href'])
    def handle_endtag(self, tag):
        if tag == 'main': self.in_main = False
        if tag == 'footer': self.in_footer = False

cases = [p for p in ROOT.glob('*.html') if p.name != 'index.html']
for p in cases:
    text = p.read_text()
    parsed = CaseParser(); parsed.feed(text)
    assert not parsed.main_links, (p.name, parsed.main_links)
    assert len(set(parsed.source_links)) >= 5, p.name
    assert 'Read the report' not in text, p.name
    # Check literal slide markup, including JSON-escaped quotes.
    script = text.split('<script>')[-1].replace('\\"', '"')
    assert not re.search(r'<a\b[^>]*href=[\"\']https?://', script), p.name
    assert 'optional reading' in text, p.name
for p in (ROOT/'authoring').glob('*.md'):
    if p.name == 'case-template.md': continue
    body, sources = p.read_text().split('## Sources and case assumptions', 1)
    assert not re.search(r'\]\(https?://', body), p.name
    assert len(set(re.findall(r'\]\((https?://[^)]+)\)', sources))) >= 5, p.name
print(f'PASS: {len(cases)} published cases and editable sources have no external reading links in teaching content; sources retained.')
