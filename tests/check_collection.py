"""Keep collection links, assets and the coverage ledger consistent as cases grow."""
from html.parser import HTMLParser
from pathlib import Path
import re

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
            self.current = {'href': attrs.get('href'), 'images': [], 'text': []}
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

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID_TAGS:
            return
        if self.depth:
            self.depth += 1
        elif 'meta' in dict(attrs).get('class', '').split():
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
        ids = case_numbers(' '.join(card['text']))
        assert len(ids) == 1, f"{card['href']}: missing or ambiguous card case number"
        card['number'] = ids[0]
    return links


def check_collection(root=ROOT):
    parser = Cards()
    parser.feed((root / 'index.html').read_text())
    assert parser.current is None, 'Unclosed collection card'
    links = validate_cards(parser.cards)
    cases = {f.name for f in root.glob('*.html') if f.name != 'index.html'}
    assert set(links) == cases, 'Collection cards and case pages differ'

    # The original eight HTML pages have unnumbered metadata. Pin their stable
    # IDs rather than accidentally reading a neighbour's number in navigation.
    # Their numbered Markdown is also checked where it exists.
    legacy_unnumbered = {
        'snow-town.html': 1, 'match.html': 2, 'shenzhen.html': 3,
        'tunnel.html': 4, 'bag.html': 5, 'waste.html': 6,
        'minibus.html': 7, 'exam.html': 8,
    }
    # Only these two predate the editable Markdown convention entirely.
    legacy_html_only = {'snow-town.html', 'match.html'}
    page_ids = []
    for card in parser.cards:
        name = card['href']
        assert (root / card['images'][0]).is_file(), f'{name}: missing card image'
        metadata = PageMetadata()
        metadata.feed((root / name).read_text())
        ids = case_numbers(' '.join(metadata.text))
        if name in legacy_unnumbered:
            expected = legacy_unnumbered[name]
            assert not ids or ids == [expected], f'{name}: incorrect legacy page number'
        else:
            assert len(ids) == 1, f'{name}: missing or ambiguous page case number'
            expected = ids[0]
        assert card['number'] == expected, f'{name}: card and page numbers differ'
        page_ids.append(expected)
        if name not in legacy_html_only:
            editable = root / 'authoring' / name.replace('.html', '.md')
            assert editable.is_file(), f'{name}: missing editable Markdown'
            md_ids = case_numbers(editable.read_text().split('##', 1)[0])
            assert md_ids == [expected], f'{name}: Markdown and page numbers differ'
    assert len(set(page_ids)) == len(page_ids), 'Duplicate case-page numbers'

    ledger = (root / 'planning/collection-roadmap.md').read_text()
    published = int(re.search(r'\*\*(\d+) published\*\*', ledger)[1])
    assert published == len(cases), 'Coverage total differs from live case count'
    rows = re.findall(r'^\| [^|]+ \| ([\d, ]+) \| — \| \d+ \|', ledger, re.M)
    numbers = [int(n) for row in rows for n in row.split(',')]
    assert len(numbers) == len(set(numbers)) == published, 'Coverage counts repeat or omit cases'
    assert set(numbers) == set(page_ids), 'Coverage numbers differ from actual case pages'
    assert set(numbers) == set(range(1, published + 1)), 'Coverage numbering has gaps'
    print(f'PASS: {published} unique cases, images, editable files and coverage entries agree.')


if __name__ == '__main__':
    check_collection()
