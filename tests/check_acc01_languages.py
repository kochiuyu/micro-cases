"""ACC-01 language pilot: approved terms, hidden answers, unchanged sources.

English tarts.html remains the fact source and the case-builder template.
Simplified and traditional pages live beside it and are not extra catalog cases.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    'en': ROOT / 'tarts.html',
    'zh-cn': ROOT / 'zh-cn' / 'tarts.html',
    'zh-hk': ROOT / 'zh-hk' / 'tarts.html',
}
SOURCES = [
    ('https://varsity.com.cuhk.edu.hk/index.php/2024/06/rescuing-leftover-bread-for-the-needy/',
     'CUHK Varsity, June 2024', 'Reports the opening event.'),
    ('https://www.epd.gov.hk/epd/english/environmentinhk/waste/prob_solutions/food_waste_challenge.html',
     'Food Waste Challenge | Environmental Protection Department', 'Describes the Hong Kong food-waste setting.'),
    ('https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint',
     '2.1 How Individuals Make Choices Based on Their Budget Constraint - Principles of Economics 3e | OpenStax',
     'Defines opportunity cost in individual choices.'),
    ('https://www.epa.gov/sustainable-management-food/prevent-wasted-food-through-source-reduction',
     'Prevent Wasted Food Through Source Reduction', 'Describes preventing surplus through planning.'),
    ('https://www.epa.gov/sustainable-management-food/wasted-food-scale?trk=article-ssr-frontend-pulse_little-text-block',
     'Wasted Food Scale', 'Distinguishes uses for surplus food.'),
    ('https://www.info.gov.hk/gia/general/201305/18/P201305180667.htm',
     'Hong Kong Government, Food Wise Hong Kong Campaign launch', 'Describes the local food-waste reduction campaign.'),
]
GLOSSES = {
    'zh-cn': ['报道开篇所述事件。', '说明香港食物浪费的背景。', '说明个人选择中的机会成本。', '说明如何通过规划减少过剩。', '区分剩余食物的不同用途。', '说明本港减少食物浪费的宣传运动。'],
    'zh-hk': ['報道開篇所述事件。', '說明香港食物浪費的背景。', '說明個人選擇中的機會成本。', '說明如何通過規劃減少過剩。', '區分剩餘食物的不同用途。', '說明本港減少食物浪費的宣傳運動。'],
}
BANNED = ('break-even', 'Break-even', '打平', '保本', 'Closing ledger', 'Already spent on baking', 'Extra cost of selling', 'the till', 'offers to take the whole tray', 'give up HK$12')
EARLY_ANSWER = ('sunk cost', '沉没成本', '沉沒成本', 'Indifference offer', '无差异出价', '無差異出價', 'Tonight’s cash', '今晚的现金', '今晚的現金', 'Compare the uses', '比较两种用途', '比較兩種用途', 'relevant cash flows', '相关的现金流量', '相關的現金流量', 'HK$84', '84 港元')


def rounds_of(text):
    match = re.search(r'const rounds=(.*?);let step=0;', text, re.S)
    assert match, 'presentation data marker missing'
    data = json.loads(match.group(1))
    assert len(data) == 6 and all(isinstance(row, list) and len(row) == 2 for row in data)
    return data


def source_items(text):
    refs = re.search(r'<div class="references">(.*?)</div>', text, re.S).group(1)
    items = re.findall(r'<li>(.*?)</li>', refs, re.S)
    parsed = []
    for item in items:
        match = re.fullmatch(r'<a href="([^"]+)">([^<]+)</a>\.\s*(.*)', item.strip())
        assert match, item
        parsed.append((match.group(1), match.group(2), re.sub(r'\s+', ' ', match.group(3)).strip()))
    return parsed


def check(root=ROOT):
    pages = {key: (root / path.relative_to(ROOT)).read_text(encoding='utf-8') for key, path in PAGES.items()}
    english = pages['en']
    assert english.count('<main>') == 1 and english.count('<dialog') == 1
    assert 'zh-cn/' not in english.split('<main>', 1)[0], 'Language pilot must not leak into the case-builder template'
    assert '<strong>MICRO CASE · ACC-01</strong>' in english
    assert 'header,details,button{display:none}' in english and '.printonly{display:block}' in english
    for banned in BANNED:
        assert banned not in english, banned
    for phrase in (
        'Closing figures, HK$ per tart · classroom assumptions',
        'Baking cost already incurred',
        'Incremental cost of selling',
        'makes to cash',
        'That cost is a sunk cost.',
        'opportunity cost of selling',
        'leave you HK$12 worse off',
        'Indifference offer: HK$7 per tart.',
        'relevant cash flows',
        'included in both alternatives',
        'not a news report of that collection',
        'offers to buy the whole tray',
        'Twelve tarts are on the tray.',
        'Wan Chai volunteers collected unsold bread',
        'June 2024',
        'alt="A baker considers an offer for the last tray at closing."',
        'Classroom assumptions, not a news report',
        'src="tarts-scene.jpg"',
    ):
        assert phrase in english, phrase
    assert source_items(english) == SOURCES
    assert 'optional reading' in english
    rounds = rounds_of(english)
    assert [title for title, _ in rounds] == [
        'Hong Kong in the news · June 2024', 'The last tray of egg tarts', 'Your first decision',
        'One fact changes', 'Compare the choices', 'Take the discussion further',
    ]
    early = '\n'.join(body for _, body in rounds[:4])
    for phrase in EARLY_ANSWER:
        assert phrase not in early, phrase
    assert 'not a news report of that collection' in rounds[0][1]
    assert 'offers to buy the whole tray' in rounds[1][1] and '<table' not in rounds[1][1]
    assert 'Twelve tarts are on the tray.' in rounds[2][1] and 'makes to cash' in rounds[2][1]
    assert rounds[3][1].count('student-prompt') == 1 and 'bread pudding' in rounds[3][1]
    assert rounds[4][1].count('<table>') == 2 and 'sunk cost' in rounds[4][1] and 'Tonight’s cash' in rounds[4][1] and 'Compare the uses' in rounds[4][1]
    assert rounds[5][1].startswith('<p>The indifference offer is HK$7 per tart.')
    assert 'Minutes 0' not in rounds[5][1] and 'break-even' not in rounds[5][1]
    handout = re.search(r'<section class="printonly">(.*?)</section>', english, re.S).group(1)
    assert 'Would you still sell the tray to the café?' in handout
    assert 'sunk cost' not in handout and 'Indifference offer' not in handout and 'Instructor note' not in handout
    assert '<details open' not in english
    assert len(re.findall(r'<a\b[^>]*aria-current="page"', english)) == 1
    assert 'href="zh-cn/tarts.html"' in english and 'href="zh-hk/tarts.html"' in english

    simplified, traditional = pages['zh-cn'], pages['zh-hk']
    assert '最后一盘蛋挞' in simplified and '最後一盤蛋撻' not in simplified and '无差异出价' in simplified and '無差異出價' not in simplified
    assert '最後一盤蛋撻' in traditional and '最后一盘蛋挞' not in traditional and '無差異出價' in traditional and '无差异出价' not in traditional
    for key, text, alt, caption, assumption in (
        ('zh-cn', simplified, '打烊时，面包师傅在考虑最后一盘的出价。', '课堂假设，不是新闻报道', '并不是对该次收集行动的新闻报道。'),
        ('zh-hk', traditional, '打烊時，麵包師傅在考慮最後一盤的出價。', '課堂假設，不是新聞報道', '並不是對該次收集行動的新聞報道。'),
    ):
        for banned in BANNED:
            assert banned not in text, (key, banned)
        assert f'alt="{alt}"' in text and caption in text and assumption in text
        assert 'src="../tarts-scene.jpg"' in text and 'href="../case-navigation.css"' in text
        assert 'href="../index.html?area=Accounting%2C%20audit%20and%20management%20control#collection"' in text
        assert '<details open' not in text and len(re.findall(r'<a\b[^>]*aria-current="page"', text)) == 1
        parsed = source_items(text)
        assert [(url, title) for url, title, _ in parsed] == [(url, title) for url, title, _ in SOURCES]
        assert [note for _, _, note in parsed] == [annotation + ' ' + gloss for (_, _, annotation), gloss in zip(SOURCES, GLOSSES[key])]
        data = rounds_of(text)
        assert len(data) == 6 and data[4][1].count('<table>') == 2
        early = '\n'.join(body for _, body in data[:4])
        for phrase in EARLY_ANSWER:
            assert phrase not in early, (key, phrase)
        assert '无差异出价' not in early and '無差異出價' not in early
        assert data[5][1].count('打平') == 0 and '保本' not in data[5][1]
        handout = re.search(r'<section class="printonly">(.*?)</section>', text, re.S).group(1)
        assert 'student-prompt' in handout and '无差异出价' not in handout and '無差異出價' not in handout
    assert rounds_of(simplified)[5][0] == '把讨论再推进一步'
    assert rounds_of(traditional)[5][0] == '把討論再推進一步'
    assert '蛋挞' not in (root / 'index.html').read_text(encoding='utf-8')
    for path in root.glob('*.html'):
        if path.name in ('tarts.html', 'index.html'):
            continue
        text = path.read_text(encoding='utf-8')
        assert '无差异出价' not in text and '無差異出價' not in text and 'Closing figures, HK$ per tart' not in text
    print('PASS: ACC-01 English terms, Chinese pages, hidden answers, and unchanged sources.')


if __name__ == '__main__':
    check()
