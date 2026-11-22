# Building a reviewed expansion case

`scripts/build_case.py` renders one already-reviewed case into the existing static-site presentation. It does **not** research, approve content, create artwork, publish, commit or certify source/visual quality. Its default repository is the parent of its own `scripts` directory, independent of the current working directory.

The verified 558-case collection is the protected baseline for the fourth balanced wave. The builder accepts reviewed fourth-wave slots through 579; the slot plan alone does not add catalogue entries or reserve public identities.

## Usage

Python 3 with `lxml` installed is required. Run from the repository root:

```sh
python scripts/build_case.py reviewed-case.json
python scripts/build_case.py reviewed-case.json --write
python tests/check_case_builder.py
```

The first command is a read-only dry run. `--dry-run` is an explicit synonym for the default; it cannot be combined with `--write`. `--repo PATH` selects a different complete checkout, including its trusted local synchronization scripts. Do not use an untrusted checkout: those Python helpers are executed.

## Input contract

Provide a UTF-8 JSON object with these required fields:

- `number`: next consecutive integer legacy ID, 121–579. Original IDs are immutable.
- `code`, `slug`, `title`, `discipline`: next available area code (for example `ACC-11`), new lowercase hyphenated URL slug, title and exact registry area name. No existing identity or page may be overwritten. The pre-wave collection permits 50 Finance cases, 45 Economics cases, and 40 in each other area. IDs 481–490 retain their protected alternating FIN/ECO identities. IDs 491–495 correspond only to FIN-46–50. For IDs 496–516, the machine-readable first-wave plan places one Economics slot first, then two slots each in the other ten teaching areas outside Finance and Economics. The next two 21-slot waves use the same balance and independently checked area order; Wave 3 spans 538–558; Wave 4 spans 559–579. Finance is not expanded. The reviewed slot order is checked independently of the configuration.
- `topics`: nonempty, unique plain-text strings. `teaser`, `alt`, `news_heading`, `notes`: nonempty plain text. Optional `location` and `duration` default to Hong Kong and 10–15 minutes.
- `news`, `opening`, `exhibit`, `round2`: HTML fragments. `sections` and `slides`: nonempty arrays of `[heading, HTML fragment]` pairs. Supported fragment tags are `p`, `strong`, `b`, `em`, `i`, `br`, `ul`, `ol`, `li`, `table`, `thead`, `tbody`, `tfoot`, `tr`, `th`, `td`, `caption`. Attributes, links, embedded media, scripts and body URLs are rejected. The builder owns presentation styling and artwork placement.
- `sections` must contain exactly one dedicated `Instructor note` entry, with concise 10–15 minute pacing, discussion prompts and case-specific conceptual limits. Pacing buried in source notes does not replace this accordion.
- `q1`, `q2`: distinct plain-text decision questions. Each must occur exactly once in `slides` as its own literal `<p>QUESTION</p>`, first decision before second. The builder supplies the gold question boxes; do not supply custom prompt wrappers.
- `exhibit_md`: matching self-contained Markdown evidence for the authoring copy, with no links or raw HTML. Human review must verify equivalence to the HTML exhibit.
- `sources`: at least five `[HTTPS URL, source title, support/limitations note]` triples with distinct URLs. URL count does not establish independent evidence. Read actual source bodies and document what each supports.

Review the entire draft before building: all essential facts must appear in both page and slides, fiction must be separated from reported facts, decisions must be fair, and calculations and timing must be independently checked. Sources remain optional end references; no links belong in student-facing main text. The builder cannot verify these substantive requirements.

## Write workflow and scope

1. Independently review content and sources against the approved plan and nearby existing cases.
2. Prepare and visually approve `<slug>-scene.jpg` under the repository's illustration guide. A write requires this file to exist; file existence is **not** visual approval.
3. Run dry mode and inspect its planned-file list. Resolve validation failures rather than disabling checks.
4. Ensure no other worker is writing this checkout, then run `--write` once.
5. Inspect the diff and run the repository's full collection, registry, expansion, decision-prompt, discipline, link and navigation checks. Run this builder's isolated tests too.
6. Check page, slides and print/handout layout, including decision highlights, artwork and mobile presentation. Review source links. Only then commit/publish under the user's authorization and verify the deployed result.

The builder creates the case HTML and authoring Markdown; updates the registry, index card/topics/counts, README, numbering ledger and coverage roadmap; and synchronizes related case navigation. Existing teaching bodies must remain unchanged outside navigation. It uses the established `tarts.html` shell and fails if expected presentation markers are missing.

Before writing it checks snapshotted text files for concurrent changes. If a caught write or post-write count/navigation check fails, it restores original bytes and removes newly created outputs. This is a **best-effort rollback**, not a crash-safe transaction or an interprocess lock. Process termination, disk failures or simultaneous writers may prevent recovery. Use version control and one writer per checkout; inspect the working tree after any failure. Publication is never automatic.

## Focused regression coverage

`tests/check_case_builder.py` uses disposable text-only copies, not production case generation. Each copy is reduced to the immutable published 558-case baseline, so tests remain usable after the fourth wave is filled. Staged tests replay historical boundaries and build fourth-wave boundaries, reject 580 or incorrect area assignments, and protect all earlier identity snapshots including the 558-case baseline. It covers read-only dry mode, portable default location, metadata, question duplication/order, prohibited HTML/links, ID gaps and overwrite refusal, artwork presence, generated metadata, Markdown tables, unchanged existing teaching bodies, caught-failure rollback and concurrent-change rejection. Fixtures are fictional and are not source or artwork certifications.
