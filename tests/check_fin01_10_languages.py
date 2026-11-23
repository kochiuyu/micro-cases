"""FIN-01–FIN-10 language pages: structure, figures, and hidden answers.

English pages stay the fact source. Simplified and traditional pages are
parallel teaching pages, not extra catalog cases.
"""
import json
import re
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
# Digit strings that must survive in every language. Amounts rewritten as
# 万/萬 are checked separately.
FIGURES = {
    'match': ['5,000', '40,000', '8,000', '3,000', '20%'],
    'minibus': ['110,000', '125,000', '15,000', '100,000', '25,000'],
    'cash-flow': ['120,000', '40,000', '50,000', '30,000', '60,000', '20,000'],
    'invoice-exposure': ['1,000,000', '600,000', '400,000', '50,000', '55,000', '20,000', '22,000'],
    'same-gap': ['2,000', '30,000', '20,000', '10,000'],
    'smaller-payments': ['4,500', '2,500', '108,000', '120,000', '8,000', '12,000', '100,000'],
    'sooner-than-what': ['100,000', '98,000', '3,000', '15,000', '20,000', '985,000', '980,000'],
    'back-sooner': ['101,947', '137,299', '1,947', '37,299', '1,946.59', '37,299.36', '2.67'],
    'protected-and-available': ['36,000', '18,000', '16,800', '34,800', '1,200', '1,800', '3,000', '800,000'],
    'only-once': ['64%', '16%', '36%', '70%', '12.5%'],
}
# Debrief results that must stay off the first three Present slides.
EARLY = {
    'match': ['8,000', '3,000', '80港元'],
    'minibus': ['125,000', '100,000港元。若仍', '蝕10,000'],
    'cash-flow': ['60,000'],
    'invoice-exposure': ['400,000日元', '400,000日圓'],
    'same-gap': ['赔付都是', '賠償都是'],
    'smaller-payments': ['108,000', '120,000'],
    'sooner-than-what': ['净成本5,000', '淨成本5,000', '985,000'],
    'back-sooner': ['101,947', '37,299'],
    'protected-and-available': ['36,000', '100万港元', '100萬港元'],
    'only-once': ['64%', '12.5%'],
}
MARKERS = {
    'zh-cn': {
        'match': '梅西',
        'minibus': '红色小巴',
        'cash-flow': '订金',
        'invoice-exposure': '风险敞口',
        'same-gap': '基差风险',
        'smaller-payments': '实际年利率',
        'sooner-than-what': '过渡融资',
        'back-sooner': '净现值',
        'protected-and-available': '存款人',
        'only-once': '股权稀释',
    },
    'zh-hk': {
        'match': '美斯',
        'minibus': '紅色小巴',
        'cash-flow': '訂金',
        'invoice-exposure': '外匯風險',
        'same-gap': '基礎風險',
        'smaller-payments': '實際年利率',
        'sooner-than-what': '過渡融資',
        'back-sooner': '淨現值',
        'protected-and-available': '存戶',
        'only-once': '股權攤薄',
    },
}
FORBIDDEN = {
    'zh-cn': ['美斯', '訂金', '存戶於每間', '股權攤薄', '基礎風險'],
    'zh-hk': ['梅西', '订金', '存款人于每家', '股权稀释', '基差风险', '这', '还是'],
}


def rounds_of(text):
    match = re.search(r'const rounds=(.*?);let step=0;', text, re.S)
    assert match, 'presentation data marker missing'
    data = json.loads(match.group(1))
    assert data and all(isinstance(row, list) and len(row) == 2 for row in data)
    return data


def anchors(text):
    return re.findall(r'<a href="(https:[^"]+)">([^<]+)</a>', text)


def check(root=ROOT):
    for slug in SLUGS:
        english = (root / f'{slug}.html').read_text(encoding='utf-8')
        assert f'<html lang="en">' in english
        assert f'href="zh-cn/{slug}.html"' in english
        assert f'href="zh-hk/{slug}.html"' in english
        assert 'hreflang="zh-Hans"' in english and 'hreflang="zh-Hant"' in english
        assert 'aria-label="Case language"' in english
        assert '<details open' not in english
        en_rounds = rounds_of(english)
        en_prompts = english.count('class="student-prompt"')
        assert en_prompts >= 2, slug
        for locale, lang in (('zh-cn', 'zh-Hans'), ('zh-hk', 'zh-Hant')):
            text = (root / locale / f'{slug}.html').read_text(encoding='utf-8')
            assert f'<html lang="{lang}">' in text, (slug, locale)
            assert f'../{slug}-scene.jpg' in text or slug == 'minibus'
            assert 'href="../case-navigation.css"' in text
            assert 'href="../index.html' in text
            assert f'hreflang="en" href="https://kochiuyu.github.io/micro-cases/{slug}.html"' in text
            assert '<details open' not in text
            assert text.count('class="student-prompt"') == en_prompts, (slug, locale)
            rounds = rounds_of(text)
            assert len(rounds) == len(en_rounds), (slug, locale, len(rounds), len(en_rounds))
            assert 'Sources and case assumptions' not in text.split('<script>', 1)[1]
            early = '\n'.join(body for _, body in rounds[:3])
            for phrase in EARLY[slug]:
                assert phrase not in early, (slug, locale, phrase)
            for figure in FIGURES[slug]:
                assert figure in text, (slug, locale, figure)
            assert MARKERS[locale][slug] in text, (slug, locale)
            for banned in FORBIDDEN[locale]:
                assert banned not in text, (slug, locale, banned)
            assert anchors(english) == anchors(text), (slug, locale)
            # Localized neighbours stay in the language folder.
            for neighbour in SLUGS:
                if neighbour == slug:
                    continue
                assert f'href="../{neighbour}.html"' not in text or neighbour in ('',)
            assert f'href="{slug}.html"' in text  # current language
        simplified = (root / 'zh-cn' / f'{slug}.html').read_text(encoding='utf-8')
        traditional = (root / 'zh-hk' / f'{slug}.html').read_text(encoding='utf-8')
        assert simplified != traditional, slug

    match_hk = (root / 'zh-hk' / 'match.html').read_text(encoding='utf-8')
    match_cn = (root / 'zh-cn' / 'match.html').read_text(encoding='utf-8')
    assert 'href="../snow-town.html">Snow Town' in match_hk
    assert 'href="../snow-town.html">Snow Town' in match_cn
    assert '预期短缺' not in match_cn and '預期短缺' not in match_hk

    only_cn = (root / 'zh-cn' / 'only-once.html').read_text(encoding='utf-8')
    only_hk = (root / 'zh-hk' / 'only-once.html').read_text(encoding='utf-8')
    assert 'href="../lower-rate-less-certainty.html"' in only_cn
    assert 'A lower rate. A less certain payment?' in only_cn
    assert '第一期已经完成' not in only_cn and '第一期已經完成' not in only_hk
    assert '单独就有用' in only_cn and '單獨已經有用' in only_hk
    assert '60万港元' in only_cn and '60萬港元' in only_hk
    assert 'Case 7' in (root / 'zh-cn' / 'back-sooner.html').read_text(encoding='utf-8')
    assert 'Case 62' in (root / 'zh-hk' / 'back-sooner.html').read_text(encoding='utf-8')
    assert '不要把B的回收期插值成2.67年' in (root / 'zh-cn' / 'back-sooner.html').read_text(encoding='utf-8')
    assert '不要把B的回本期插值成2.67年' in (root / 'zh-hk' / 'back-sooner.html').read_text(encoding='utf-8')
    prot = (root / 'zh-cn' / 'protected-and-available.html').read_text(encoding='utf-8')
    assert '20万港元' in prot and '100万港元' in prot and '每名存款人于每家成员银行' in prot
    assert '每名存戶於每間成員銀行' in (root / 'zh-hk' / 'protected-and-available.html').read_text(encoding='utf-8')
    # Accounting pilot template is not a finance page.
    tarts = (root / 'tarts.html').read_text(encoding='utf-8')
    assert 'zh-cn/' not in tarts.split('<main>', 1)[0]


if __name__ == '__main__':
    check()
    print('PASS')
