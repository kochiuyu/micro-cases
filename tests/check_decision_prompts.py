"""Prevent plain-paragraph opening/revote prompts in new or revised cases."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r'<div\s+class=[\"\']student-prompt[\"\']\s*>(.*?)</div>', re.S)
for path in root.glob('*.html'):
    if path.name == 'index.html':
        continue
    page, script = path.read_text().split('<script>', 1)
    # Slides are serialized as JSON in newer cases, literal JS in older ones.
    script = script.replace('\\"', '"')
    for surface, markup in [('page', page), ('slides', script)]:
        prompts = pattern.findall(markup)
        assert len(prompts) >= 2, (path.name, surface, 'opening and round-two decision boxes required')
        for prompt in prompts:
            assert '<strong>' in prompt and '</strong>' in prompt, (path.name, surface, 'visible decision label missing')
            assert re.search(r'<p>\s*[^<\s]', prompt), (path.name, surface, 'empty decision question')
print('PASS: every case has labeled, nonempty decision boxes on its page and presentation slides.')
