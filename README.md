# Micro Cases in Business

Short classroom cases for business teaching. Each case has an opening decision, a second-round prompt, a debrief, presentation slides, and a printable student handout.

Browse the collection at [https://kochiuyu.github.io/micro-cases/](https://kochiuyu.github.io/micro-cases/). Search by title, topic, area code such as ACC-01 or FIN-01, or original number. Filter links keep the view you chose.

The collection has 600 published cases across 12 teaching areas. Area codes such as ACC-01 and HSP-01 appear on the cases; page URLs stay the same. A [numbering crosswalk](docs/case-numbering.md) maps codes to the original numbers.

Accounting cases can also be read in Simplified Chinese and in Hong Kong Traditional Chinese. Use the language links on those case pages.

## Acknowledgement

Cases 1–8, listed below, are based on teaching materials developed by Chiu Yu Ko with support from the "Innovation in Business Education, Business School, Chinese University of Hong Kong, 2024" award.

1. [Snow Town](https://kochiuyu.github.io/micro-cases/snow-town.html)
2. [When the star sits out](https://kochiuyu.github.io/micro-cases/match.html)
3. [The Shenzhen data puzzle](https://kochiuyu.github.io/micro-cases/shenzhen.html)
4. [Crossing Victoria Harbour](https://kochiuyu.github.io/micro-cases/tunnel.html)
5. [The checkout bag](https://kochiuyu.github.io/micro-cases/bag.html)
6. [The missing rubbish](https://kochiuyu.github.io/micro-cases/waste.html)
7. [The red minibus bid](https://kochiuyu.github.io/micro-cases/minibus.html)
8. [The offer expires Friday](https://kochiuyu.github.io/micro-cases/exam.html)

## Classroom convention

Keep external links in the optional sources section only. The opening, exhibits, questions, presentation slides, and handout must give students the facts they need without asking them to open a report. Preserve source attribution, and distinguish reported facts from classroom assumptions.

Every opening and round-two decision uses the highlighted **Your decision** box on the page and on its presentation slide. See the [question-format guide](docs/decision-questions.md).

## For authors

Editable case materials and the authoring template are in `authoring/`. Follow the [art direction and production guide](docs/art-direction.md) for every new or revised illustration, and keep the established watercolor-and-ink narrative style.

When adding a case, set its `data-discipline` and visible `.discipline` label to match the coverage ledger. Teaching area, Business topic, and Class time available work together on the site; Reset filters shows all cases. Primary areas follow the coverage ledger; secondary concepts remain in the topic menu.

Useful checks:

```bash
python tests/check_case_links.py
python tests/check_collection.py
python tests/check_decision_prompts.py
python tests/check_disciplines.py
```

Collection history and expansion plans are in `planning/`, including the [original roadmap](planning/collection-roadmap.md) and the approved plans to [240](planning/expansion-to-240.md), [360](planning/expansion-to-360.md), and [480](planning/expansion-to-480.md) cases, plus the [Finance and Economics extension](planning/finance-economics-extension-490.md). Planned cases are not counted as published. Identity fixtures protect permanent IDs, area codes, and URLs.
