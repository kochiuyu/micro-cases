"""Language pages for OPS and the areas built from the same path.

English pages stay the fact source. Simplified and traditional pages are
parallel teaching pages, not extra catalog cases.

Figure comparison, script bans and anchor checks follow the FIN-11–FIN-50
test. Narrow differences:

- Wrong-script scanning ignores link href addresses. OPS-01 cites an HK01
  URL whose path contains traditional characters; the link text stays English.
- 公里 is allowed in zh-hk. It is the Hong Kong word for kilometre. The
  character 里 stays banned everywhere else, except the proper noun 佛羅里達.
- 恒 stays banned, except the proper noun 恒生.
- A classroom Debrief is 讲评 / 講評. The reveal starts at that slide when
  the page has one. Operations pages put it on the first slide after the
  last decision. A few later cases insert analysis slides before the slide
  titled Debrief; the boundary follows the title. sold-out has no Debrief
  title, so the last decision prompt is the marker.

CHECKED_AREAS lists the areas this file checks. Area page branches append
their own code.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'tests'))
from build_ops_i18n import area_bundle  # noqa: E402
from check_fin11_50_languages import (  # noqa: E402
    HANS_BANNED,
    HANT_BANNED,
    anchors,
    numbers,
    rounds_of,
)

# Collection order after OPS. Area branches append one code each.
CHECKED_AREAS = ['OPS', 'PPL']
# Official Hong Kong names that use a character the zh-hk scan otherwise bans.
# 佛羅里達 is the standard form of Florida (SUS-32). 恒生 is Hang Seng’s
# official name (ECO-41). Both stay flagged for faculty; this is not a
# general exception for 里 or 恒.
HK_PROPER_NOUNS = ('佛羅里達', '恒生')
# English source runs figures together. Faculty approval is required before
# that English is edited, so only these tokens are ignored. Chinese keeps
# the separated figures.
FIGURE_EXEMPT = {
    'local-reduction-displaced-pressure': {
        'en': ('150.100', '50.5'),
        'zh': ('150', '100', '50', '5'),
        'why': 'SUS-38 English "released150.100hours" and "50.5/40"',
    },
    'two-markups-one-final-customer': {
        'en': ('90,100', '2'),
        'zh': ('90', '100'),
        'why': 'ECO-22 English "50,60,70,80,90,100" and "round2"',
    },
    'same-average-different-risk-choice': {
        'en': ('75,100',),
        'zh': ('75', '100'),
        'why': 'ECO-40 English "75,100"',
    },
    'visible-care-usable-lobby': {
        'en': ('600.6',),
        'zh': ('600', '6'),
        'why': 'HSP-38 English "600.6"',
    },
}


def prompt_answer_at(rounds):
    """First slide after the last decision prompt. None if that prompt is last."""
    last_prompt = None
    for index, (_title, body) in enumerate(rounds):
        if 'student-prompt' in body:
            last_prompt = index
    assert last_prompt is not None, 'no decision prompt in slides'
    start = last_prompt + 1
    if start >= len(rounds):
        return None
    return start


def answer_at(rounds):
    """Classroom reveal: the Debrief slide, or else the post-decision slide.

    A Debrief title may sit after analysis slides that follow the last
    decision. Those slides are not the hidden answer. sold-out has no
    Debrief title. HSP-01's last slide still contains a prompt, so there
    is no later hidden slide and this returns None.
    """
    for index, (title, _body) in enumerate(rounds):
        if title.startswith('Debrief') or title.startswith('讲评') or title.startswith('講評'):
            return index
    return prompt_answer_at(rounds)


def case_numbers(text, slug, side):
    found = list(numbers(text))
    spec = FIGURE_EXEMPT.get(slug)
    if not spec:
        return found
    for token in spec['en' if side == 'en' else 'zh']:
        if token in found:
            found.remove(token)
    return found


def assert_debrief_title(en_title, zh_title, locale):
    if locale == 'zh-cn':
        mark, dotted, colon = '讲评', '讲评 ·', '讲评：'
    else:
        mark, dotted, colon = '講評', '講評 ·', '講評：'
    if en_title.startswith('Debrief ·'):
        assert zh_title.startswith(dotted), (locale, en_title, zh_title)
    elif en_title.startswith('Debrief:'):
        assert zh_title.startswith(colon), (locale, en_title, zh_title)
    elif en_title.startswith('Debrief'):
        assert zh_title.startswith(mark), (locale, en_title, zh_title)
    else:
        assert not zh_title.startswith(mark), (locale, en_title, zh_title)


def without_hrefs(text):
    """Drop link addresses before a character scan. Link text stays."""
    return re.sub(r'\bhref="[^"]*"', 'href=""', text)


def without_original_titles(text):
    """Drop published titles of works cited in their original Chinese.

    Snow Town quotes mainland headlines with lang="zh". Those characters are
    the source title, not the case's Hong Kong or mainland register.
    """
    return re.sub(
        r'(<a\b[^>]*\blang="zh(?:-[A-Za-z]+)?"[^>]*>)(.*?)(</a>)',
        r'\1\3',
        text,
        flags=re.S,
    )


def summaries(text):
    return [item.strip() for item in re.findall(r'<summary>([^<]*)</summary>', text)]


def check(root=ROOT, areas=None):
    areas = areas or CHECKED_AREAS
    for area in areas:
        slugs, codes, _format_name = area_bundle(area)
        localized = set(slugs)
        cases_with_hidden_figures = 0
        for slug in slugs:
            code = codes[slug]
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
            en_numbers = case_numbers(english, slug, 'en')
            reveal_at = answer_at(en_rounds)
            debrief_titles = [
                index for index, (title, _body) in enumerate(en_rounds)
                if title.startswith('Debrief')
            ]
            if debrief_titles:
                assert debrief_titles[0] == reveal_at, (slug, debrief_titles[0], reveal_at)
            if area == 'OPS' and debrief_titles:
                # Operations still titles the first post-decision slide Debrief.
                assert reveal_at == prompt_answer_at(en_rounds), (slug, reveal_at)
            if reveal_at is None:
                leaked = set()
            else:
                early_en = '\n'.join(body for _, body in en_rounds[:reveal_at])
                later_en = '\n'.join(body for _, body in en_rounds[reveal_at:])
                leaked = set(case_numbers(later_en, slug, 'en')) - set(case_numbers(early_en, slug, 'en'))
                if leaked:
                    cases_with_hidden_figures += 1
            en_summaries = summaries(english)
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
                for (en_title, _), (zh_title, _) in zip(en_rounds, rounds):
                    assert_debrief_title(en_title, zh_title, locale)
                zh_summaries = summaries(text)
                assert len(zh_summaries) == len(en_summaries), (slug, locale)
                for en_summary, zh_summary in zip(en_summaries, zh_summaries):
                    assert_debrief_title(en_summary, zh_summary, locale)
                if locale == 'zh-cn':
                    assert '复盘 ·' not in text and '复盘：' not in text, slug
                assert 'Sources and case assumptions' not in text.split('<script>', 1)[1]
                assert Counter(case_numbers(text, slug, 'zh')) == Counter(en_numbers), (
                    slug, locale, 'figure multiset changed')
                if reveal_at is not None:
                    early = '\n'.join(body for _, body in rounds[:reveal_at])
                    present = set(case_numbers(early, slug, 'zh'))
                    assert not (leaked & present), (slug, locale, sorted(leaked & present)[:6])
                scanned = without_original_titles(without_hrefs(text))
                if locale == 'zh-hk':
                    for token in ('公里',) + HK_PROPER_NOUNS:
                        scanned = scanned.replace(token, '')
                found = sorted(set(scanned) & banned)
                assert not found, (slug, locale, ''.join(found[:12]))
                assert anchors(english) == anchors(text), (slug, locale)
                for neighbour in localized:
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
            # Older pages say Present and Vote, not “Presentation mode” / “Your decision”.
            if 'Your decision' in english:
                assert '你的决策' in simplified and '你的決定' in traditional
        assert cases_with_hidden_figures, (area, 'answer check matched no hidden figure')
    if 'OPS' in areas:
        # OPS-01 is the case whose URL would fail a whole-page script scan,
        # and whose slides are not titled Debrief.
        opening = rounds_of((root / 'sold-out.html').read_text(encoding='utf-8'))
        assert not any(title.startswith('Debrief') for title, _ in opening)
        assert answer_at(opening) > 0


if __name__ == '__main__':
    check()
    print('PASS')
