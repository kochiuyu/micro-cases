"""Build Simplified and Traditional pages for FIN-01–FIN-10.

Reads authoring/i18n/<slug>-zh-cn.json and <slug>-zh-hk.json. English teaching
text stays authoritative. This script does not publish, commit or touch
Accounting pages.

Default is a dry run. Pass --write to update the ten English finance pages
and write zh-cn/ and zh-hk/ pages.
"""
import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUGS = [
    'match', 'minibus', 'cash-flow', 'invoice-exposure', 'same-gap',
    'smaller-payments', 'sooner-than-what', 'back-sooner',
    'protected-and-available', 'only-once',
]
CODES = {
    'match': 'FIN-01', 'minibus': 'FIN-02', 'cash-flow': 'FIN-03',
    'invoice-exposure': 'FIN-04', 'same-gap': 'FIN-05',
    'smaller-payments': 'FIN-06', 'sooner-than-what': 'FIN-07',
    'back-sooner': 'FIN-08', 'protected-and-available': 'FIN-09',
    'only-once': 'FIN-10',
}
SITE = 'https://kochiuyu.github.io/micro-cases'
UI_STYLE = (
    '<style data-accounting-language-ui>.accounting-languages{display:flex;flex-wrap:wrap;'
    'align-items:center;gap:.25em .5em;font:500 .85rem/1.45 system-ui,sans-serif}'
    '.accounting-languages [aria-current="page"]{font-weight:700;text-decoration:none}'
    '.accounting-languages a{color:inherit;text-underline-offset:2px}'
    '.accounting-languages a:focus-visible{outline:2px solid #99531d;outline-offset:3px}'
    '@media(max-width:620px){body>header{flex-wrap:wrap;gap:.6em}}'
    '@media print{.accounting-languages{display:none}}</style>'
)
FONT_STYLE = (
    '<style>html:lang(zh-Hant) body{font-family:"Noto Serif CJK TC","PingFang TC",'
    '"Microsoft JhengHei",system-ui,serif}html:lang(zh-Hans) body{font-family:'
    '"Noto Serif CJK SC","PingFang SC","Microsoft YaHei",system-ui,serif}'
    'html:lang(zh) h1{letter-spacing:0;line-height:1.2}html:lang(zh) p{overflow-wrap:anywhere}</style>'
)
NUMERIC = re.compile(
    r'^(?:FIN-\d{2}|Case \d+|[\d,]+(?:\.\d+)?|HK\$[\d,]+(?:\.\d+)?|[+\-−][\d,]+(?:\.\d+)?|'
    r'JPY[\d,]+|[\d]+%|\d+–\d+)$'
)
KEEP_EXACT = {'English', 'Snow Town', 'Micro Case', 'Micro Cases'}
ROUNDS = re.compile(r'const rounds=(.*?);\s*let step=0;', re.S)


class Collect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.skip = 0
        self.buf = ''
        self.texts = []
        self.attrs = []
        self.anchors = []
        self.in_a = False
        self.href = ''
        self.abuf = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'):
            self.skip += 1
        self.flush()
        if self.skip:
            return
        if tag == 'a':
            self.in_a = True
            self.href = attrs.get('href', '')
            self.abuf = ''
        for key in ('alt', 'aria-label'):
            if attrs.get(key):
                self.attrs.append(attrs[key])

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1
            self.flush()
            return
        self.flush()
        if tag == 'a' and self.in_a:
            self.anchors.append((self.href, self.abuf.strip()))
            self.in_a = False

    def handle_data(self, data):
        if self.skip:
            return
        self.buf += data
        if self.in_a:
            self.abuf += data

    def flush(self):
        if self.buf.strip():
            self.texts.append(self.buf.strip())
        self.buf = ''


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def load_map(slug, locale):
    path = ROOT / 'authoring' / 'i18n' / f'{slug}-{locale}.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    assert data['format'] == 'finance-case-translation-v1', path
    assert data['case'] == CODES[slug], path
    assert data['locale'] == locale, path
    assert data['source'] == f'{slug}.html', path
    mapping = data['text']
    assert isinstance(mapping, dict) and mapping, path
    return data, mapping, path


def required_strings(html):
    collector = Collect()
    collector.feed(html)
    collector.flush()
    external = {text for href, text in collector.anchors if href.startswith('http')}
    needed = []
    seen = set()

    def add(value):
        if value in seen or value in external or value in KEEP_EXACT or NUMERIC.match(value):
            return
        seen.add(value)
        needed.append(value)

    for value in collector.texts + collector.attrs:
        add(value)
    match = ROUNDS.search(html.split('<script>', 1)[1])
    assert match, 'presentation data marker missing'
    for title, body in json.loads(match.group(1)):
        add(title)
        slide = Collect()
        slide.feed(body)
        slide.flush()
        for value in slide.texts + slide.attrs:
            add(value)
    return needed, external


def apply_visible(html, mapping):
    """Replace complete text nodes and alt/aria values. Leave tags in place."""
    pieces = []
    index = 0
    length = len(html)
    in_script = False
    while index < length:
        if not in_script and html.startswith('<script', index):
            in_script = True
        if in_script and html.startswith('</script>', index):
            in_script = False
        if html[index] == '<' :
            end = html.find('>', index)
            assert end != -1
            tag = html[index:end + 1]
            if not in_script:
                tag = replace_attrs(tag, mapping)
            pieces.append(tag)
            index = end + 1
            continue
        end = html.find('<', index)
        if end < 0:
            end = length
        chunk = html[index:end]
        if not in_script:
            stripped = chunk.strip()
            if stripped in mapping:
                chunk = chunk.replace(stripped, mapping[stripped], 1)
        pieces.append(chunk)
        index = end
    return ''.join(pieces)


def replace_attrs(tag, mapping):
    def swap(match):
        value = match.group(2)
        if value in mapping:
            value = mapping[value].replace('"', '&quot;')
        return match.group(1) + value + match.group(3)
    return re.sub(r'(\b(?:alt|aria-label)=")([^"]*)(")', swap, tag)


def translate_rounds(html, mapping):
    script_at = html.find('<script>')
    match = ROUNDS.search(html, script_at)
    rounds = json.loads(match.group(1))
    translated = []
    for title, body in rounds:
        title = mapping.get(title, title)
        body = apply_visible(body, mapping)
        translated.append([title, body])
    encoded = json.dumps(translated, ensure_ascii=False, separators=(',', ':'))
    return html[:match.start(1)] + encoded + html[match.end(1):]


def language_nav(slug, current):
    labels = {
        'en': ('en', 'en', 'English'),
        'zh-hk': ('zh-Hant', 'zh-Hant', '繁體中文'),
        'zh-cn': ('zh-Hans', 'zh-Hans', '简体中文'),
    }
    aria = {'en': 'Case language', 'zh-cn': '案例语言', 'zh-hk': '個案語言'}
    parts = []
    for locale, (lang, hreflang, label) in labels.items():
        if locale == 'en':
            href = f'{slug}.html' if current == 'en' else f'../{slug}.html'
        elif locale == current:
            href = f'{slug}.html'
        elif current == 'en':
            href = f'{locale}/{slug}.html'
        else:
            href = f'../{locale}/{slug}.html'
        current_attr = ' aria-current="page"' if locale == current else ''
        parts.append(
            f'<a href="{href}" lang="{lang}" hreflang="{hreflang}"{current_attr}>{label}</a>'
        )
    return f'<nav class="accounting-languages" aria-label="{aria[current]}">{" ".join(parts)}</nav>'


def insert_language_ui(html, slug, locale):
    html = re.sub(r'<link rel="canonical"[^>]*>', '', html)
    html = re.sub(r'<link rel="alternate"[^>]*>', '', html)
    html = re.sub(r'<style data-accounting-language-ui>.*?</style>', '', html)
    html = re.sub(r'<style>html:lang\(zh-Hant\).*?</style>', '', html)
    html = re.sub(r'<nav class="accounting-languages".*?</nav>', '', html)
    links = alternate_links(slug, locale)
    style = UI_STYLE + (FONT_STYLE if locale != 'en' else '')
    html = html.replace('</title>', '</title>' + links + style, 1)
    html = html.replace('</header>', language_nav(slug, locale) + '</header>', 1)
    lang = {'en': 'en', 'zh-cn': 'zh-Hans', 'zh-hk': 'zh-Hant'}[locale]
    html = html.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    html = html.replace('<html lang="zh-Hans">', f'<html lang="{lang}">', 1)
    html = html.replace('<html lang="zh-Hant">', f'<html lang="{lang}">', 1)
    return html


def alternate_links(slug, locale):
    canonical = {
        'en': f'{SITE}/{slug}.html',
        'zh-cn': f'{SITE}/zh-cn/{slug}.html',
        'zh-hk': f'{SITE}/zh-hk/{slug}.html',
    }[locale]
    return (
        f'<link rel="canonical" href="{canonical}">'
        f'<link rel="alternate" hreflang="en" href="{SITE}/{slug}.html">'
        f'<link rel="alternate" hreflang="zh-Hant" href="{SITE}/zh-hk/{slug}.html">'
        f'<link rel="alternate" hreflang="zh-Hans" href="{SITE}/zh-cn/{slug}.html">'
    )


def relocate(html, slug):
    html = html.replace('href="case-navigation.css"', 'href="../case-navigation.css"')
    html = html.replace(f'src="{slug}-scene.jpg"', f'src="../{slug}-scene.jpg"')
    # Present stores the same markup inside a JSON string, so the quotes are escaped.
    html = html.replace(f'src=\\"{slug}-scene.jpg\\"', f'src=\\"../{slug}-scene.jpg\\"')
    html = html.replace('href="index.html', 'href="../index.html')
    html = html.replace('href="snow-town.html"', 'href="../snow-town.html"')
    html = html.replace(
        'href="lower-rate-less-certainty.html"',
        'href="../lower-rate-less-certainty.html"',
    )
    return html


def translate_print_heading(html, mapping):
    heading = mapping.get('Sources and case assumptions')
    if not heading:
        return html
    old = "'<h2>Sources and case assumptions</h2>'"
    new = "'<h2>" + heading + "</h2>'"
    assert old in html, 'print-handout source heading missing'
    return html.replace(old, new, 1)


def build_locale(english, slug, locale, mapping):
    if locale == 'en':
        return insert_language_ui(english, slug, 'en')
    page = apply_visible(english, mapping)
    page = translate_rounds(page, mapping)
    page = translate_print_heading(page, mapping)
    page = relocate(page, slug)
    page = insert_language_ui(page, slug, locale)
    return page


def uncovered(english, mapping):
    needed, _external = required_strings(english)
    missing = [item for item in needed if item not in mapping]
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    for slug in SLUGS:
        english_path = ROOT / f'{slug}.html'
        english = english_path.read_text(encoding='utf-8')
        # Build from the teaching page, ignoring a language switch already inserted.
        bare = strip_language_ui(english)
        for locale in ('zh-cn', 'zh-hk'):
            data, mapping, path = load_map(slug, locale)
            assert data['source_sha256'] == sha256(bare), (
                f'{path.name} source hash does not match {slug}.html without language UI'
            )
            missing = uncovered(bare, mapping)
            assert not missing, (slug, locale, missing[:8], len(missing))
            page = build_locale(bare, slug, locale, mapping)
            assert 'const rounds=' in page and f'lang="{ {"zh-cn":"zh-Hans","zh-hk":"zh-Hant"}[locale] }"' in page
            if args.write:
                target = ROOT / locale / f'{slug}.html'
                target.parent.mkdir(exist_ok=True)
                target.write_text(page, encoding='utf-8')
        english_out = build_locale(bare, slug, 'en', {})
        if args.write:
            english_path.write_text(english_out, encoding='utf-8')
        print(f'OK {slug}')
    print('PASS' if args.write else 'DRY RUN PASS')


def strip_language_ui(html):
    html = re.sub(r'<link rel="canonical"[^>]*>', '', html)
    html = re.sub(r'<link rel="alternate"[^>]*>', '', html)
    html = re.sub(r'<style data-accounting-language-ui>.*?</style>', '', html)
    html = re.sub(r'<nav class="accounting-languages".*?</nav>', '', html)
    html = html.replace('<html lang="zh-Hans">', '<html lang="en">')
    html = html.replace('<html lang="zh-Hant">', '<html lang="en">')
    return html


if __name__ == '__main__':
    main()
