"""FIN-11–FIN-50 language pages: structure, figures, and hidden answers.

English pages stay the fact source. Simplified and traditional pages are
parallel teaching pages, not extra catalog cases.
"""
import json
import re
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_fin_i18n import APPROVED, CODES, REMAINING  # noqa: E402

LOCALIZED = set(APPROVED + REMAINING)
NUMBER = re.compile(r'\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?')
ROUNDS = re.compile(r'const rounds=(.*?);let step=0;', re.S)
HANS_BANNED = set('這還為們個與時發開關買賣價銀證險資債國營權稅費質據數學問應從並槓裏後經對會過優項軟訊繫總餘認購攤麼於恆')
HANT_BANNED = set('这还为们个与时发开关买卖价银证险资债国营权税费质据数学问应从并杠里后经过对会过优项质软讯总余认购摊么于恒')


def rounds_of(text):
    match = ROUNDS.search(text)
    assert match, 'presentation data marker missing'
    data = json.loads(match.group(1))
    assert data and all(isinstance(row, list) and len(row) == 2 for row in data)
    return data


def anchors(text):
    return re.findall(r'<a href="(https:[^"]+)">([^<]+)</a>', text)


def numbers(text):
    # Layout rules are not case figures. “Round two” is the same label as “Round 2”.
    text = re.sub(r'<style\b[^>]*>.*?</style>', '', text, flags=re.S)
    # &#x27; is an apostrophe. Its digits are not a case figure.
    text = re.sub(r'&#x?[0-9A-Fa-f]+;', '', text)
    text = re.sub(r'Round [Tt]wo', 'Round', text)
    text = re.sub(r'[Rr]ound 2\b', 'Round', text)
    text = (text.replace('第2轮', 'Round').replace('第2輪', 'Round')
            .replace('第二轮', 'Round').replace('第二輪', 'Round'))
    # 2025年6月9日 uses a digit for the month English spells out. The day and year stay.
    text = re.sub(r'(?<=年)\d{1,2}(?=月)', '', text)
    text = re.sub(r'(?<![\d年])\d{1,2}(?=月\d{1,2}日)', '', text)
    # HK$000, 千港元000 and a bare 000港元 name the thousands unit, not an amount.
    text = re.sub(r'HK\$000(?!\d)', '', text)
    text = re.sub(r'千港元000', '千港元', text)
    text = re.sub(r'(?<![\d,])000(?=港元)', '', text)
    # “80 per cent Guarantee Product” repeats 八成. Its digits are not a second figure.
    text = re.sub(r'80 per cent', '', text)
    # 期初（第0年） names time zero. English says “time zero”, so this digit is a label.
    # A bare 第0年 still counts: it translates “year 0”.
    text = re.sub(r'期初（第0年）', '期初', text)
    # 200万 / 160万 restates 2 million / 1.6 million. FIN-33 writes the same
    # amounts as 万 (1,000万 for 10 million and for 10.0m). Trailing zeros are
    # not a second figure, so 10.0 and 10 compare as one value.
    def fold_wan(match):
        million = Decimal(match.group(1).replace(',', '')) / Decimal(100)
        rendered = format(million, 'f')
        if '.' in rendered:
            rendered = rendered.rstrip('0').rstrip('.')
        return rendered
    text = re.sub(r'(\d+(?:,\d{3})*(?:\.\d+)?)(?:万|萬)', fold_wan, text)

    def canon(token):
        if '.' in token:
            token = token.rstrip('0').rstrip('.')
        return token
    return [canon(token) for token in NUMBER.findall(text)]


def debrief_at(rounds):
    for index, (title, _body) in enumerate(rounds):
        if title.startswith('Debrief') or title.startswith('讲评') or title.startswith('講評'):
            return index
    return None


def check(root=ROOT):
    for slug in REMAINING:
        code = CODES[slug]
        english = (root / f'{slug}.html').read_text(encoding='utf-8')
        assert '<html lang="en">' in english
        assert f'href="zh-cn/{slug}.html"' in english
        assert f'href="zh-hk/{slug}.html"' in english
        assert 'hreflang="zh-Hans"' in english and 'hreflang="zh-Hant"' in english
        assert 'aria-label="Case language"' in english
        assert '<details open' not in english
        en_rounds = rounds_of(english)
        en_prompts = english.count('class="student-prompt"')
        assert en_prompts >= 2, slug
        en_numbers = numbers(english)
        reveal_at = debrief_at(en_rounds)
        early_en = '\n'.join(body for _, body in en_rounds[:reveal_at]) if reveal_at else ''
        later_en = '\n'.join(body for _, body in en_rounds[reveal_at:]) if reveal_at else ''
        leaked = set(numbers(later_en)) - set(numbers(early_en))
        for locale, lang, banned in (
            ('zh-cn', 'zh-Hans', HANS_BANNED),
            ('zh-hk', 'zh-Hant', HANT_BANNED),
        ):
            text = (root / locale / f'{slug}.html').read_text(encoding='utf-8')
            assert f'<html lang="{lang}">' in text, (slug, locale)
            assert f'../{slug}-scene.jpg' in text
            assert 'href="../case-navigation.css"' in text
            assert 'href="../index.html' in text
            assert f'hreflang="en" href="https://kochiuyu.github.io/micro-cases/{slug}.html"' in text
            assert '<details open' not in text
            assert text.count('class="student-prompt"') == en_prompts, (slug, locale)
            rounds = rounds_of(text)
            assert len(rounds) == len(en_rounds), (slug, locale, len(rounds), len(en_rounds))
            assert 'Sources and case assumptions' not in text.split('<script>', 1)[1]
            assert Counter(numbers(text)) == Counter(en_numbers), (slug, locale, 'figure multiset changed')
            if reveal_at:
                early = '\n'.join(body for _, body in rounds[:reveal_at])
                present = set(numbers(early))
                assert not (leaked & present), (slug, locale, sorted(leaked & present)[:6])
            found = sorted(set(text) & banned)
            assert not found, (slug, locale, ''.join(found[:12]))
            assert anchors(english) == anchors(text), (slug, locale)
            for neighbour in LOCALIZED:
                if neighbour == slug:
                    continue
                assert f'href="../{neighbour}.html"' not in text, (slug, locale, neighbour)
            assert f'href="../{slug}.html"' in text
            assert f'href="{slug}.html"' in text
            assert code in text
        simplified = (root / 'zh-cn' / f'{slug}.html').read_text(encoding='utf-8')
        traditional = (root / 'zh-hk' / f'{slug}.html').read_text(encoding='utf-8')
        assert simplified != traditional, slug
        assert '演示模式' in simplified and '簡報模式' in traditional
        assert '你的决策' in simplified and '你的決定' in traditional


if __name__ == '__main__':
    check()
    print('PASS')
