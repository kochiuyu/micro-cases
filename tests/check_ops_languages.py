"""OPS-01–OPS-50 language pages: structure, figures, and hidden answers.

English pages stay the fact source. Simplified and traditional pages are
parallel teaching pages, not extra catalog cases.

Figure comparison, script bans and anchor checks follow the FIN-11–FIN-50
test. Two narrow differences:

- Wrong-script scanning ignores link href addresses. OPS-01 cites an HK01
  URL whose path contains traditional characters; the link text stays English.
- 公里 is allowed in zh-hk. It is the Hong Kong word for kilometre on OPS-14
  and OPS-25. The character 里 stays banned everywhere else.

No OPS answer is identified by requiring every slide title to start with
Debrief. The hidden-answer check starts at the first slide after the last
decision prompt, which every operations page has. Where a slide title does
start with Debrief, that title is the same slide.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'tests'))
from build_ops_i18n import CODES, SLUGS  # noqa: E402
from check_fin11_50_languages import (  # noqa: E402
    HANS_BANNED,
    HANT_BANNED,
    anchors,
    numbers,
    rounds_of,
)

LOCALIZED = set(SLUGS)


def answer_at(rounds):
    """First slide after the last decision prompt.

    Returning None would skip the leak check. Operations pages do not share
    one Debrief title prefix, so the prompt is the marker.
    """
    last_prompt = None
    for index, (_title, body) in enumerate(rounds):
        if 'student-prompt' in body:
            last_prompt = index
    assert last_prompt is not None, 'no decision prompt in slides'
    start = last_prompt + 1
    assert start < len(rounds), 'answer slides missing after the last decision'
    return start


def without_hrefs(text):
    """Drop link addresses before a character scan. Link text stays."""
    return re.sub(r'\bhref="[^"]*"', 'href=""', text)


def check(root=ROOT):
    cases_with_hidden_figures = 0
    for slug in SLUGS:
        code = CODES[slug]
        english = (root / f'{slug}.html').read_text(encoding='utf-8')
        assert '<html lang="en">' in english
        assert f'href="zh-cn/{slug}.html"' in english
        assert f'href="zh-hk/{slug}.html"' in english
        assert 'hreflang="zh-Hans"' in english and 'hreflang="zh-Hant"' in english
        assert 'aria-label="Case language"' in english
        assert 'class="accounting-languages"' in english
        assert '<details open' not in english
        en_rounds = rounds_of(english)
        en_prompts = english.count('class="student-prompt"')
        assert en_prompts >= 2, slug
        en_numbers = numbers(english)
        reveal_at = answer_at(en_rounds)
        debrief_titles = [
            index for index, (title, _body) in enumerate(en_rounds)
            if title.startswith('Debrief')
        ]
        if debrief_titles:
            assert debrief_titles[0] == reveal_at, (slug, debrief_titles[0], reveal_at)
        early_en = '\n'.join(body for _, body in en_rounds[:reveal_at])
        later_en = '\n'.join(body for _, body in en_rounds[reveal_at:])
        leaked = set(numbers(later_en)) - set(numbers(early_en))
        if leaked:
            cases_with_hidden_figures += 1
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
            if locale == 'zh-cn':
                for (en_title, _), (zh_title, _) in zip(en_rounds, rounds):
                    if en_title.startswith('Debrief'):
                        assert zh_title.startswith('讲评'), (slug, en_title, zh_title)
                assert '复盘 ·' not in text and '复盘：' not in text, slug
            assert 'Sources and case assumptions' not in text.split('<script>', 1)[1]
            assert Counter(numbers(text)) == Counter(en_numbers), (slug, locale, 'figure multiset changed')
            early = '\n'.join(body for _, body in rounds[:reveal_at])
            present = set(numbers(early))
            assert not (leaked & present), (slug, locale, sorted(leaked & present)[:6])
            scanned = without_hrefs(text)
            if locale == 'zh-hk':
                scanned = scanned.replace('公里', '')
            found = sorted(set(scanned) & banned)
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
    assert cases_with_hidden_figures, 'answer check matched no hidden figure'
    # OPS-01 is the case whose URL would fail a whole-page script scan,
    # and whose slides are not titled Debrief.
    opening = rounds_of((root / 'sold-out.html').read_text(encoding='utf-8'))
    assert not any(title.startswith('Debrief') for title, _ in opening)
    assert answer_at(opening) > 0


if __name__ == '__main__':
    check()
    print('PASS')
