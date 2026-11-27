"""Build Simplified and Traditional pages for one teaching area.

Reads authoring/i18n/<slug>-zh-cn.json and <slug>-zh-hk.json. The format
name is <stem>-case-translation-v1 (operations, people, strategy, and the
other area stems). English teaching text stays authoritative. This script
does not publish or commit.

Default is a dry run of OPS-01–OPS-50. Pass --area PPL (or another area
code) to build that area. Pass --write to update the English pages with the
language switch and write zh-cn/ and zh-hk/ pages. Pass --slugs to build a
subset.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_fin_i18n import (  # noqa: E402
    KEEP_EXACT,
    NUMERIC,
    ROOT,
    Collect,
    apply_visible,
    insert_language_ui,
    required_strings,
    sha256,
    strip_language_ui,
    translate_print_heading,
    translate_rounds as translate_json_rounds,
)

SLUGS = [
    'sold-out', 'split-shipment', 'packing-line', 'mixed-collection',
    'shared-factory', 'planned-stop', 'empty-counter', 'harder-to-miss',
    'keep-the-design-open', 'same-process', 'time-to-reorder',
    'stock-is-not-ready', 'promise-by-when', 'route-and-window',
    'returned-checked-where-next', 'started-is-not-finished',
    'steady-output-later-peak', 'orders-are-not-consumption',
    'through-the-depot-or-to-a-shelf', 'count-the-risky-shelves',
    'components-ready-in-the-right-week', 'shorten-the-task-or-the-project',
    'next-ticket-next-eligible-ticket', 'bulk-price-total-stock-cost',
    'units-sold-trips-walked', 'same-pass-rate-different-flow',
    'short-shipment-which-allocation', 'reserve-capacity-commit-units',
    'service-percentage-which-denominator', 'one-lot-shared-ingredient',
    'half-empty-is-there-room', 'first-in-first-to-expire',
    'sample-passed-shipment-passed', 'equal-work-balanced-line',
    'mostly-zero-forecast-nothing', 'project-time-specialist-time',
    'punctual-trucks-one-bay', 'best-score-missing-condition',
    'shorter-task-more-handoffs', 'standard-input-visible-exception',
    'typhoon-ends-what-restarts-first', 'full-terminal-empty-boxes',
    'cold-room-which-cartons-warmed', 'online-orders-at-a-busy-shop',
    'the-locker-fit-is-not-the-pickup', 'which-chiller-carries-the-peak',
    'can-the-relabelled-parcel-still-make-it',
    'one-night-which-work-belongs-together',
    'the-spare-is-in-the-repair-queue', 'full-carts-slow-connections',
]
CODES = {
    'sold-out': 'OPS-01', 'split-shipment': 'OPS-02', 'packing-line': 'OPS-03',
    'mixed-collection': 'OPS-04', 'shared-factory': 'OPS-05',
    'planned-stop': 'OPS-06', 'empty-counter': 'OPS-07',
    'harder-to-miss': 'OPS-08', 'keep-the-design-open': 'OPS-09',
    'same-process': 'OPS-10', 'time-to-reorder': 'OPS-11',
    'stock-is-not-ready': 'OPS-12', 'promise-by-when': 'OPS-13',
    'route-and-window': 'OPS-14', 'returned-checked-where-next': 'OPS-15',
    'started-is-not-finished': 'OPS-16', 'steady-output-later-peak': 'OPS-17',
    'orders-are-not-consumption': 'OPS-18',
    'through-the-depot-or-to-a-shelf': 'OPS-19',
    'count-the-risky-shelves': 'OPS-20',
    'components-ready-in-the-right-week': 'OPS-21',
    'shorten-the-task-or-the-project': 'OPS-22',
    'next-ticket-next-eligible-ticket': 'OPS-23',
    'bulk-price-total-stock-cost': 'OPS-24', 'units-sold-trips-walked': 'OPS-25',
    'same-pass-rate-different-flow': 'OPS-26',
    'short-shipment-which-allocation': 'OPS-27',
    'reserve-capacity-commit-units': 'OPS-28',
    'service-percentage-which-denominator': 'OPS-29',
    'one-lot-shared-ingredient': 'OPS-30', 'half-empty-is-there-room': 'OPS-31',
    'first-in-first-to-expire': 'OPS-32',
    'sample-passed-shipment-passed': 'OPS-33',
    'equal-work-balanced-line': 'OPS-34',
    'mostly-zero-forecast-nothing': 'OPS-35',
    'project-time-specialist-time': 'OPS-36',
    'punctual-trucks-one-bay': 'OPS-37',
    'best-score-missing-condition': 'OPS-38',
    'shorter-task-more-handoffs': 'OPS-39',
    'standard-input-visible-exception': 'OPS-40',
    'typhoon-ends-what-restarts-first': 'OPS-41',
    'full-terminal-empty-boxes': 'OPS-42',
    'cold-room-which-cartons-warmed': 'OPS-43',
    'online-orders-at-a-busy-shop': 'OPS-44',
    'the-locker-fit-is-not-the-pickup': 'OPS-45',
    'which-chiller-carries-the-peak': 'OPS-46',
    'can-the-relabelled-parcel-still-make-it': 'OPS-47',
    'one-night-which-work-belongs-together': 'OPS-48',
    'the-spare-is-in-the-repair-queue': 'OPS-49',
    'full-carts-slow-connections': 'OPS-50',
}
LOCALIZED = set(SLUGS)
# stem, translation-format name. OPS keeps the lists above so a rebuild
# cannot drift from the operations pages already on this branch.
AREA_META = {
    'OPS': ('operations', 'operations-case-translation-v1'),
    'PPL': ('people', 'people-case-translation-v1'),
    'STR': ('strategy', 'strategy-case-translation-v1'),
    'ENT': ('entrepreneurship', 'entrepreneurship-case-translation-v1'),
    'IS': ('information-systems', 'information-systems-case-translation-v1'),
    'GVR': ('governance', 'governance-case-translation-v1'),
    'SUS': ('sustainability', 'sustainability-case-translation-v1'),
    'ECO': ('economics', 'economics-case-translation-v1'),
    'HSP': ('hospitality', 'hospitality-case-translation-v1'),
}
SELECTOR = re.compile(
    r'(?:main(?:\s[>.]\s?[\w.-]+)?|table|p|\.[\w-]+|#[\w-]+)\Z'
)


def area_bundle(code):
    """Slugs, case codes, and format name for one area.

    OPS returns the lists in this file. Every other area follows case-registry
    order by case code.
    """
    code = code.upper()
    if code not in AREA_META:
        raise SystemExit(f'Unknown area code: {code}')
    _stem, format_name = AREA_META[code]
    if code == 'OPS':
        return list(SLUGS), dict(CODES), format_name
    data = json.loads((ROOT / 'case-registry.json').read_text(encoding='utf-8'))
    rows = [case for case in data['cases'] if case['code'].split('-', 1)[0] == code]
    rows.sort(key=lambda case: case['code'])
    slugs = [case['slug'] for case in rows]
    codes = {case['slug']: case['code'] for case in rows}
    assert len(slugs) == 50, (code, len(slugs))
    return slugs, codes, format_name


def load_map(slug, locale, codes=None, format_name='operations-case-translation-v1'):
    if codes is None:
        codes = CODES
    path = ROOT / 'authoring' / 'i18n' / f'{slug}-{locale}.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    assert data['format'] == format_name, path
    assert data['case'] == codes[slug], path
    assert data['locale'] == locale, path
    assert data['source'] == f'{slug}.html', path
    mapping = data['text']
    assert isinstance(mapping, dict) and mapping, path
    return data, mapping, path


def relocate(html, slug, localized=None):
    """Same link rules as the Finance builder, for this area's neighbours."""
    if localized is None:
        localized = LOCALIZED
    html = html.replace('href="case-navigation.css"', 'href="../case-navigation.css"')
    html = html.replace(f'src="{slug}-scene.jpg"', f'src="../{slug}-scene.jpg"')
    html = html.replace(f'src=\\"{slug}-scene.jpg\\"', f'src=\\"../{slug}-scene.jpg\\"')

    def lift(match):
        href = match.group(1)
        if '://' in href or href.startswith(('//', '/', '../', '#')):
            return match.group(0)
        path = href.split('?', 1)[0].split('#', 1)[0]
        if path.endswith('.html'):
            name = path[:-5]
            if name not in localized:
                return f'href="../{href}"'
        return match.group(0)

    return re.sub(r'href="([^"]+)"', lift, html)


def js_literals(blob):
    for match in re.finditer(r"'((?:\\'|[^'])*)'", blob):
        yield match.group(1).replace("\\'", "'").replace('\\/', '/')


def translate_legacy_rounds(html, match, mapping):
    """HSP-01 keeps copy() calls. Translate titles and HTML literals only."""
    def repl(found):
        inner = found.group(1).replace("\\'", "'").replace('\\/', '/')
        if SELECTOR.match(inner):
            return found.group(0)
        new = apply_visible(inner, mapping) if '<' in inner else mapping.get(inner, inner)
        if new == inner:
            return found.group(0)
        escaped = new.replace('\\', '\\\\').replace("'", "\\'")
        return "'" + escaped + "'"

    blob = re.sub(r"'((?:\\'|[^'])*)'", repl, match.group(1))
    return html[:match.start(1)] + blob + html[match.end(1):]


def translate_rounds_any(html, mapping):
    from build_fin_i18n import ROUNDS
    script_at = html.find('<script>')
    match = ROUNDS.search(html, script_at)
    try:
        json.loads(match.group(1))
    except json.JSONDecodeError:
        return translate_legacy_rounds(html, match, mapping)
    return translate_json_rounds(html, mapping)


def required_legacy(html):
    """Strings the HSP-01 map must cover. Selectors and kept names are not strings."""
    from build_fin_i18n import ROUNDS
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
    blob = ROUNDS.search(html.split('<script>', 1)[1]).group(1)
    for literal in js_literals(blob):
        if '<' in literal:
            slide = Collect()
            slide.feed(literal)
            slide.flush()
            for value in slide.texts + slide.attrs:
                add(value)
        elif SELECTOR.match(literal):
            continue
        else:
            add(literal)
    return needed


def build_locale(english, slug, locale, mapping, localized=None):
    if localized is None:
        localized = LOCALIZED
    if locale == 'en':
        return insert_language_ui(english, slug, 'en')
    page = apply_visible(english, mapping)
    page = translate_rounds_any(page, mapping)
    page = translate_print_heading(page, mapping)
    page = relocate(page, slug, localized)
    page = insert_language_ui(page, slug, locale)
    return page


def uncovered(english, mapping):
    try:
        needed, _external = required_strings(english)
    except json.JSONDecodeError:
        needed = required_legacy(english)
    return [item for item in needed if item not in mapping]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--area', default='OPS', help='Area code. Default: OPS.')
    parser.add_argument('--slugs', nargs='*', help='Build only these slugs. Default: the whole area.')
    args = parser.parse_args()
    code = args.area.upper()
    slugs, codes, format_name = area_bundle(code)
    localized = set(slugs)
    chosen = args.slugs or slugs
    unknown = [slug for slug in chosen if slug not in codes]
    if unknown:
        raise SystemExit(f'Unknown {code} slug: {unknown}')
    for slug in chosen:
        english_path = ROOT / f'{slug}.html'
        english = english_path.read_text(encoding='utf-8')
        bare = strip_language_ui(english)
        for locale in ('zh-cn', 'zh-hk'):
            data, mapping, path = load_map(slug, locale, codes, format_name)
            assert data['source_sha256'] == sha256(bare), (
                f'{path.name} source hash does not match {slug}.html without language UI'
            )
            missing = uncovered(bare, mapping)
            assert not missing, (slug, locale, missing[:8], len(missing))
            page = build_locale(bare, slug, locale, mapping, localized)
            lang = {'zh-cn': 'zh-Hans', 'zh-hk': 'zh-Hant'}[locale]
            assert 'const rounds=' in page and f'lang="{lang}"' in page
            if args.write:
                target = ROOT / locale / f'{slug}.html'
                target.parent.mkdir(exist_ok=True)
                target.write_text(page, encoding='utf-8')
        english_out = build_locale(bare, slug, 'en', {}, localized)
        if args.write:
            english_path.write_text(english_out, encoding='utf-8')
        print(f'OK {slug}')
    print('PASS' if args.write else 'DRY RUN PASS')


if __name__ == '__main__':
    main()
