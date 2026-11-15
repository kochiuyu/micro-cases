# Collection browsing

The collection preserves every original case URL and all teaching content. `case-registry.json` owns stable identity; see `case-numbering.md` before adding or moving cases.

- Cards are statically ordered by registry area order, then visible code. All 120 cards remain available without JavaScript.
- With JavaScript, initially show 24 matching cards; Show more reveals the next 24 and focuses the first newly visible card. A changed filter resets the display limit.
- Area shortcuts choose one area and clear other filters. Native teaching-area, topic and duration selectors can be intersected with search.
- Search uses case-insensitive AND terms across rendered card text and identifiers. A number alone, or `Case 119`, resolves the exact historical ID, not a substring.
- The results status counts all matches and explains when only a subset is visible. No-result guidance retains Reset filters. All interactive controls retain visible keyboard focus.
- Query parameters `q`, `area`, `topic`, and `time` preserve the filter view on reload or when sharing the URL. Parameter values are validated against available native select options. No cookies, account or analytics are added. Pagination is not stored in the URL.
- Existing watercolor-and-ink illustrations are shown in landscape cards. CSS uses three, two and one card columns at descending viewport widths, with two-column area shortcuts on phones. Reduced-motion preference removes smooth scrolling and hover movement.
- Each case has previous/next links within its teaching area and an area-browse link. These links are omitted from printed handouts. Original case text, sources, highlighted decisions and slides remain in place.

## Regression checks

Run `tests/check_registry.py`, `tests/check_collection.py`, `tests/check_disciplines.py`, `tests/check_case_links.py`, and `tests/check_decision_prompts.py`. The registry check validates codes, historical IDs, URLs and case neighbours. The discipline check executes the actual collection JavaScript, including filtering, search, pagination and URL restoration. Visual browser checks remain separate from these static/runtime checks.
