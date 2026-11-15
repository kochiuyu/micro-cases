"""Check decision boxes in page markup and decoded presentation data."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'<div\s+class=[\"\']student-prompt[\"\']\s*>(.*?)</div>', re.S)


def presentation_markup(script, name):
    match = re.search(r'const rounds=(.*?);let step=0;', script, re.S)
    assert match, (name, 'presentation data marker missing')
    if name == 'snow-town.html':
        # Original hand-authored JS uses DOM copy() calls and single-quoted HTML,
        # rather than a JSON array. Keep this narrow documented legacy exception.
        return match[1].replace('\\"', '"').replace('\\/', '/')
    rounds = json.loads(match[1])
    assert isinstance(rounds, list), (name, 'presentation must be an array')
    assert all(isinstance(r, list) and len(r) == 2 and all(isinstance(v, str) for v in r) for r in rounds), (name, 'invalid slide pair')
    return '\n'.join(markup for title, markup in rounds)


def check_markup(markup, name, surface):
    prompts = PATTERN.findall(markup)
    assert len(prompts) >= 2, (name, surface, 'opening and round-two decision boxes required')
    for prompt in prompts:
        assert '<strong>' in prompt and '</strong>' in prompt, (name, surface, 'visible decision label missing')
        assert re.search(r'<p>\s*[^<\s]', prompt), (name, surface, 'empty decision question')


def regression():
    first = '<div class="student-prompt"><strong>Your decision</strong><p>Order now?</p></div>'
    second = '<div class="student-prompt"><strong>Your decision</strong><p>Order tomorrow?</p></div>'
    def decode(markup, safe):
        data = json.dumps([['First', first], ['Second', markup]])
        if safe:
            data = data.replace('</', '<\\/')
        return presentation_markup('const rounds=' + data + ';let step=0;', 'fixture.html')
    for safe in (False, True):
        check_markup(decode(second, safe), 'fixture', 'slides')
        for invalid in ('<p>Order tomorrow?</p>', '<div class="student-prompt"><p>Order tomorrow?</p></div>', '<div class="student-prompt"><strong>Your decision</strong><p> </p></div>'):
            try:
                check_markup(decode(invalid, safe), 'fixture', 'slides')
            except AssertionError:
                pass
            else:
                raise AssertionError('Plain, unlabeled or empty prompt escaped regression')


def check(root=ROOT):
    regression()
    for path in root.glob('*.html'):
        if path.name == 'index.html':
            continue
        page, script = path.read_text().split('<script>', 1)
        check_markup(page, path.name, 'page')
        check_markup(presentation_markup(script, path.name), path.name, 'slides')
    print('PASS: pages and decoded slides have labeled, nonempty decision boxes; escaped-slash and invalid-prompt regressions pass.')


if __name__ == '__main__':
    check()
