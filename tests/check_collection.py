"""Keep collection links, assets and the coverage ledger consistent as cases grow."""
from html.parser import HTMLParser
from pathlib import Path
import re
from check_registry import load_registry

ROOT = Path(__file__).resolve().parents[1]


class Cards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'card' in attrs.get('class', '').split():
            assert self.current is None, 'Nested collection cards'
            self.current = {'href': attrs.get('href'), 'attrs': attrs, 'images': [], 'text': []}
            self.cards.append(self.current)
        if tag == 'img' and self.current is not None:
            self.current['images'].append(attrs.get('src'))

    def handle_data(self, data):
        if self.current is not None:
            self.current['text'].append(data)

    def handle_endtag(self, tag):
        if tag == 'a':
            self.current = None


class PageMetadata(HTMLParser):
    """Read the case metadata, not case references in sources or navigation."""
    VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__()
        self.text = []
        self.depth = 0
        self.attrs = None

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID_TAGS:
            return
        if self.depth:
            self.depth += 1
        elif 'meta' in dict(attrs).get('class', '').split():
            assert self.attrs is None, 'Duplicate page metadata'
            self.attrs = dict(attrs)
            self.depth = 1

    def handle_endtag(self, tag):
        if tag in self.VOID_TAGS:
            return
        if self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.text.append(data)


def case_numbers(text):
    return [int(n) for n in re.findall(r'\bCase\s+(\d+)\b', text)]


def validate_cards(cards):
    links = [card['href'] for card in cards]
    assert all(links), 'Collection card missing href'
    assert len(links) == len(set(links)), 'Duplicate collection cards'
    for card in cards:
        assert len(card['images']) == 1 and card['images'][0], (
            f"{card['href']}: every card needs exactly one illustration")
        raw = card['attrs'].get('data-case-id', '')
        assert raw.isdigit(), 'Missing stable card ID'
        card['number'] = int(raw)
    return links


def check_collection(root=ROOT):
    parser = Cards()
    parser.feed((root / 'index.html').read_text())
    assert parser.current is None, 'Unclosed collection card'
    links = validate_cards(parser.cards)
    cases = {f.name for f in root.glob('*.html') if f.name != 'index.html'}
    assert set(links) == cases, 'Collection cards and case pages differ'

    registry, mapping = load_registry(root)
    expected_order = sorted(registry['cases'], key=lambda c: ([a['name'] for a in registry['areas']].index(c['area']), c['code']))
    assert [c['number'] for c in parser.cards] == [c['legacy_id'] for c in expected_order], 'Cards must follow area and code order'
    legacy_html_only = {'snow-town.html', 'match.html'}
    page_ids = []
    for card in parser.cards:
        name = card['href']; number = card['number']
        assert number in mapping, 'Unknown stable card ID'
        case = mapping[number]
        assert name == case['slug'] + '.html', 'Stable ID/URL mismatch'
        assert card['attrs'].get('data-case-code') == case['code'], 'Wrong card code'
        assert case['code'] in ' '.join(card['text']), 'Missing visible card code'
        assert (root / card['images'][0]).is_file(), f'{name}: missing card image'
        source = (root / name).read_text()
        metadata = PageMetadata(); metadata.feed(source)
        assert case['code'] in ' '.join(metadata.text), f'{name}: missing visible page code'
        assert metadata.attrs.get('data-case-id') == str(number), f'{name}: metadata stable ID'
        assert metadata.attrs.get('data-case-code') == case['code'], f'{name}: metadata code'
        page_ids.append(number)
        if name not in legacy_html_only:
            editable = root / 'authoring' / name.replace('.html', '.md')
            assert editable.is_file(), f'{name}: missing editable Markdown'
            intro = editable.read_text().split('##', 1)[0]
            assert re.search(r'<!--\s*legacy-case-id:\s*'+str(number)+r'\s*-->',intro), f'{name}: Markdown stable ID'
            assert case['code'] in re.sub(r'<!--.*?-->','',intro,flags=re.S), f'{name}: Markdown visible code'
    assert len(set(page_ids)) == len(page_ids), 'Duplicate case-page numbers'

    ledger = (root / 'planning/collection-roadmap.md').read_text()
    published = int(re.search(r'\*\*(\d+) published\*\*', ledger)[1])
    assert published == len(cases), 'Coverage total differs from live case count'
    rows = re.findall(r'^\| [^|]+ \| ([\d, ]+) \| [^|]+ \| \d+ \|', ledger, re.M)
    numbers = [int(n) for row in rows for n in row.split(',')]
    assert len(numbers) == len(set(numbers)) == published, 'Coverage counts repeat or omit cases'
    assert set(numbers) == set(page_ids), 'Coverage numbers differ from actual case pages'
    assert set(numbers) == set(range(1, published + 1)), 'Coverage numbering has gaps'
    assert f'**{480-published} approved editorial slots** | **{480-published}**' in ledger, 'Remaining total differs from approved capacity'
    for area in registry['areas']:
        row=re.search(r'^\| '+re.escape(area['name'])+r' \|[^\n]+',ledger,re.M)
        assert row, 'Missing coverage area'
        remaining=int(row[0].split('|')[4].strip())
        count=sum(c['area']==area['name'] for c in registry['cases'])
        assert remaining==40-count, 'Remaining area capacity mismatch: '+area['name']
    print(f'PASS: {published} unique cases, images, editable files and coverage entries agree.')


if __name__ == '__main__':
    check_collection()
