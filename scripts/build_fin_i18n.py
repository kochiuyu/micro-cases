"""Build Simplified and Traditional pages for finance cases.

Reads authoring/i18n/<slug>-zh-cn.json and <slug>-zh-hk.json. English teaching
text stays authoritative. This script does not publish, commit or touch
Accounting pages.

Default is a dry run of FIN-11–FIN-50. Pass --write to update those English
pages and write zh-cn/ and zh-hk/ pages. Pass --slugs to build a subset,
including an approved FIN-01–FIN-10 slug when a navigation link must be rebuilt.
"""
import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = [
    'match', 'minibus', 'cash-flow', 'invoice-exposure', 'same-gap',
    'smaller-payments', 'sooner-than-what', 'back-sooner',
    'protected-and-available', 'only-once',
]
REMAINING = [
    'lower-rate-less-certainty', 'rent-and-exit', 'cash-before-risk',
    'same-money-same-rate', 'one-company-one-hurdle', 'cash-moves-together',
    'cheaper-credit-tighter-promise', 'cash-on-the-day-it-is-needed',
    'best-project-best-package', 'good-year-distributable-surplus',
    'same-yield-different-duration', 'pay-for-time-to-decide',
    'unpriced-not-ownership-free', 'lower-premium-repeated-deductible',
    'shipment-complete-documents-complying', 'cash-flows-continue-ending-worth',
    'credit-limit-available-draw', 'hedge-moves-delivered-cost',
    'same-ownership-different-exit', 'interest-paid-principal-due',
    'higher-percentage-more-value', 'more-return-more-equity-risk',
    'business-price-share-price', 'guaranteed-loan-future-cash',
    'cheaper-forward-flexible-protection', 'cheaper-machine-service-years',
    'monthly-reserve-later-start', 'faster-payment-more-stock',
    'early-repayment-after-which-fee', 'same-payout-different-shareholders',
    'protection-when-the-portfolio-falls', 'a-buy-order-a-higher-quote',
    'customer-paid-can-we-make-payroll', 'the-peg-holds-which-rate-resets',
    'same-forecast-dearer-option', 'which-share-would-you-sell',
    'who-gets-the-lending-subsidy', 'who-funds-the-rescue-investment',
    'tougher-loan-collect-less', 'big-ipo-allocation-good-news',
]
SLUGS = APPROVED + REMAINING
CODES = {
    'match': 'FIN-01', 'minibus': 'FIN-02', 'cash-flow': 'FIN-03',
    'invoice-exposure': 'FIN-04', 'same-gap': 'FIN-05',
    'smaller-payments': 'FIN-06', 'sooner-than-what': 'FIN-07',
    'back-sooner': 'FIN-08', 'protected-and-available': 'FIN-09',
    'only-once': 'FIN-10',
    'lower-rate-less-certainty': 'FIN-11', 'rent-and-exit': 'FIN-12',
    'cash-before-risk': 'FIN-13', 'same-money-same-rate': 'FIN-14',
    'one-company-one-hurdle': 'FIN-15', 'cash-moves-together': 'FIN-16',
    'cheaper-credit-tighter-promise': 'FIN-17',
    'cash-on-the-day-it-is-needed': 'FIN-18',
    'best-project-best-package': 'FIN-19',
    'good-year-distributable-surplus': 'FIN-20',
    'same-yield-different-duration': 'FIN-21',
    'pay-for-time-to-decide': 'FIN-22',
    'unpriced-not-ownership-free': 'FIN-23',
    'lower-premium-repeated-deductible': 'FIN-24',
    'shipment-complete-documents-complying': 'FIN-25',
    'cash-flows-continue-ending-worth': 'FIN-26',
    'credit-limit-available-draw': 'FIN-27',
    'hedge-moves-delivered-cost': 'FIN-28',
    'same-ownership-different-exit': 'FIN-29',
    'interest-paid-principal-due': 'FIN-30',
    'higher-percentage-more-value': 'FIN-31',
    'more-return-more-equity-risk': 'FIN-32',
    'business-price-share-price': 'FIN-33',
    'guaranteed-loan-future-cash': 'FIN-34',
    'cheaper-forward-flexible-protection': 'FIN-35',
    'cheaper-machine-service-years': 'FIN-36',
    'monthly-reserve-later-start': 'FIN-37',
    'faster-payment-more-stock': 'FIN-38',
    'early-repayment-after-which-fee': 'FIN-39',
    'same-payout-different-shareholders': 'FIN-40',
    'protection-when-the-portfolio-falls': 'FIN-41',
    'a-buy-order-a-higher-quote': 'FIN-42',
    'customer-paid-can-we-make-payroll': 'FIN-43',
    'the-peg-holds-which-rate-resets': 'FIN-44',
    'same-forecast-dearer-option': 'FIN-45',
    'which-share-would-you-sell': 'FIN-46',
    'who-gets-the-lending-subsidy': 'FIN-47',
    'who-funds-the-rescue-investment': 'FIN-48',
    'tougher-loan-collect-less': 'FIN-49',
    'big-ipo-allocation-good-news': 'FIN-50',
}
LOCALIZED = set(SLUGS)
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

    def handle_entityref(self, name):
        # Keep the source spelling. Otherwise 13.5 &lt; x &lt; 18 loses its inequality.
        token = f'&{name};'
        if self.skip:
            return
        self.buf += token
        if self.in_a:
            self.abuf += token

    def handle_charref(self, name):
        token = f'&#{name};'
        if self.skip:
            return
        self.buf += token
        if self.in_a:
            self.abuf += token

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

    def lift(match):
        href = match.group(1)
        # External and already-rooted links stay as written. Only a sibling
        # page that has no language version moves up to the site root.
        if '://' in href or href.startswith(('//', '/', '../', '#')):
            return match.group(0)
        path = href.split('?', 1)[0].split('#', 1)[0]
        if path.endswith('.html'):
            name = path[:-5]
            if name not in LOCALIZED:
                return f'href="../{href}"'
        return match.group(0)

    return re.sub(r'href="([^"]+)"', lift, html)


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
    parser.add_argument('--slugs', nargs='*', help='Build only these slugs. Default: FIN-11–FIN-50.')
    args = parser.parse_args()
    chosen = args.slugs or REMAINING
    unknown = [slug for slug in chosen if slug not in CODES]
    if unknown:
        raise SystemExit(f'Unknown finance slug: {unknown}')
    for slug in chosen:
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
