# Case numbering and stable identity

Cases are displayed by teaching area and two-digit sequence, for example `ACC-01`. The initial collection contains ten cases per area; approved additions extend each area to twenty, released incrementally. This is a browsing identity, not an indication of difficulty or a prescribed teaching order.

## Canonical registry

`../case-registry.json` is the single mapping between permanent legacy IDs, visible codes, unchanged URL slugs, primary areas and card titles. Schema version: 1.

- `areas` is ordered for browsing. `code` is its prefix; `name` is the exact primary-area label; `label` is its compact navigation label.
- Each `cases` entry contains `legacy_id`, `code`, `slug`, `area` and `title`. A case URL remains `slug + ".html"`; image and authoring filenames remain unchanged.
- Initial area sequences 01–10 follow ascending legacy ID within that area. Do not renumber existing cases merely because cards are sorted differently or a title changes.
- A case page’s `.meta` carries `data-case-id` (permanent integer) and `data-case-code` (visible identifier). The visible metadata, browser title, header and presentation counter use the new code; print retains the visible metadata.
- Editable authoring Markdown uses the new code on its metadata line and `<!-- legacy-case-id: N -->` for traceability. The two original HTML-only cases, Snow Town and Match, remain HTML-only.
- Historical roadmap entries, award acknowledgements, historical source IDs and citations retain their original numeric references. Use the crosswalk below to interpret them. No source or historical attribution is renamed.
- When adding a future case, choose its primary area deliberately, allocate the next unused code, retain existing codes and URLs, then update registry, card/page metadata and authoring together. Reclassification requires an explicit identity migration, not an automatic re-sort.

## Expansion identity rules

- Allocate the next global permanent integer ID and next unused area code. Each published area sequence must be contiguous, 01 through its current length, with at most 20 cases. Uneven area totals during release are expected.
- The initial 120 identities (ID, code, URL slug and primary area) are locked in `tests/fixtures/original-case-identities.json`. Do not regenerate this fixture when adding cases. A title improvement does not change identity.
- `tests/check_registry.py` supports 120–240 published cases and checks the original identity lock, unique contiguous IDs, area sequences and previous/next links through the actual last case, not a fixed tenth case.
- Run `python scripts/sync_collection.py` to refresh visible totals. Do not enter 240 or twenty per area until those cases are actually published. The crosswalk below records the original collection; the live registry is authoritative for additions.

## Area prefixes

| Prefix | Navigation label | Full teaching area |
|---|---|---|
| ACC | Accounting | Accounting, audit and management control |
| FIN | Finance | Finance, banking and insurance |
| MKT | Marketing | Marketing, retail and consumer behaviour |
| OPS | Operations | Operations, supply chains and logistics |
| PPL | People | People, leadership and organisational behaviour |
| STR | Strategy | Strategy and international business |
| ENT | Entrepreneurship | Entrepreneurship, innovation and family business |
| IS | Information systems | Information systems, AI and business analytics |
| GVR | Governance | Governance, law, ethics and risk |
| SUS | Sustainability | Sustainability, social enterprise and public management |
| ECO | Economics | Economics, competition and pricing |
| HSP | Hospitality | Hospitality, tourism, property and service management |

## Legacy-to-current crosswalk

| Former case | Current code | Unchanged page | Title |
|---|---|---|---|
| 1 | HSP-01 | [snow-town.html](../snow-town.html) | Snow Town |
| 2 | FIN-01 | [match.html](../match.html) | When the star sits out |
| 3 | IS-01 | [shenzhen.html](../shenzhen.html) | The Shenzhen data puzzle |
| 4 | ECO-01 | [tunnel.html](../tunnel.html) | Crossing Victoria Harbour |
| 5 | SUS-01 | [bag.html](../bag.html) | The checkout bag |
| 6 | SUS-02 | [waste.html](../waste.html) | The missing rubbish |
| 7 | FIN-02 | [minibus.html](../minibus.html) | The red minibus bid |
| 8 | PPL-01 | [exam.html](../exam.html) | The offer expires Friday |
| 9 | ACC-01 | [tarts.html](../tarts.html) | The last tray of egg tarts |
| 10 | SUS-03 | [court.html](../court.html) | Who gets the last badminton court? |
| 11 | MKT-01 | [ferry-pass.html](../ferry-pass.html) | Would you share a ten-trip ferry pass? |
| 12 | GVR-01 | [battery.html](../battery.html) | The phone with a fresh battery |
| 13 | STR-01 | [cafes.html](../cafes.html) | Two cafés, one lunch rush |
| 14 | SUS-04 | [walkway.html](../walkway.html) | Who funds the covered walkway? |
| 15 | PPL-02 | [parcel.html](../parcel.html) | Pay per parcel? |
| 16 | ECO-02 | [stall.html](../stall.html) | One stall, one bid |
| 17 | OPS-01 | [sold-out.html](../sold-out.html) | Sold out by noon. Double tomorrow? |
| 18 | FIN-03 | [cash-flow.html](../cash-flow.html) | The biggest order, the smallest cash balance |
| 19 | MKT-02 | [coupon.html](../coupon.html) | A thousand coupons. A better business? |
| 20 | PPL-03 | [supervisor.html](../supervisor.html) | The best seller. The best supervisor? |
| 21 | STR-02 | [distributor.html](../distributor.html) | A bigger market. Whose customers? |
| 22 | GVR-02 | [customer-notice.html](../customer-notice.html) | The warning changed. Did customers notice? |
| 23 | ENT-01 | [family-name.html](../family-name.html) | Would you sell the family name? |
| 24 | ACC-02 | [branch-loss.html](../branch-loss.html) | Close the loss-making branch? |
| 25 | HSP-02 | [replacement-room.html](../replacement-room.html) | A room is ready. Is the guest’s trip restored? |
| 26 | IS-02 | [chatbot.html](../chatbot.html) | 97% right. Ready to reply? |
| 27 | OPS-02 | [split-shipment.html](../split-shipment.html) | Fly the whole order, or just what is missing? |
| 28 | ENT-02 | [paid-pilot.html](../paid-pilot.html) | They like the prototype. Will they buy it? |
| 29 | ECO-03 | [booking-fee.html](../booking-fee.html) | No booking fee. A lower price? |
| 30 | ACC-03 | [returns-target.html](../returns-target.html) | Target reached. Returns still coming? |
| 31 | MKT-03 | [character-collaboration.html](../character-collaboration.html) | They remember the character. Do they remember us? |
| 32 | GVR-03 | [supplier-review.html](../supplier-review.html) | The best quote. The right reviewer? |
| 33 | STR-03 | [prototype-bench.html](../prototype-bench.html) | The cheaper batch and the prototype bench |
| 34 | OPS-03 | [packing-line.html](../packing-line.html) | A faster machine. More finished boxes? |
| 35 | IS-03 | [recovery-rehearsal.html](../recovery-rehearsal.html) | The backup is green. Can the shop work again? |
| 36 | ENT-03 | [separate-version.html](../separate-version.html) | The big client wants its own version |
| 37 | HSP-03 | [two-night-stays.html](../two-night-stays.html) | One busy night. Two nights of business. |
| 38 | FIN-04 | [invoice-exposure.html](../invoice-exposure.html) | The invoice is not the exposure |
| 39 | PPL-04 | [ready-for-handoff.html](../ready-for-handoff.html) | The handbook is complete. Are they ready? |
| 40 | ACC-04 | [count-and-value.html](../count-and-value.html) | The stock is all there. Is it worth the same? |
| 41 | MKT-04 | [return-friction.html](../return-friction.html) | More days to return it, or less trouble? |
| 42 | OPS-04 | [mixed-collection.html](../mixed-collection.html) | Fewer changeovers. A later customer. |
| 43 | STR-04 | [portable-promise.html](../portable-promise.html) | Export the product, or export the promise? |
| 44 | IS-04 | [one-source.html](../one-source.html) | Two approvals. One source. |
| 45 | GVR-04 | [less-of-what.html](../less-of-what.html) | Twenty per cent less. Less of what? |
| 46 | HSP-04 | [unread-cancellation.html](../unread-cancellation.html) | They did not come. Did they try to cancel? |
| 47 | ECO-04 | [fewer-jobs.html](../fewer-jobs.html) | Fewer sales. A worse price? |
| 48 | ENT-04 | [usable-support.html](../usable-support.html) | HK$60,000 of support. Can we use it? |
| 49 | SUS-05 | [actually-reused.html](../actually-reused.html) | Reusable fifty times. Used how many? |
| 50 | FIN-05 | [same-gap.html](../same-gap.html) | A larger limit. The same gap? |
| 51 | PPL-05 | [more-reports.html](../more-reports.html) | Four times the reports. Four times the mistakes? |
| 52 | ACC-05 | [over-budget.html](../over-budget.html) | Over budget. Out of control? |
| 53 | IS-05 | [order-units.html](../order-units.html) | The file arrived. What did we order? |
| 54 | HSP-05 | [direct-cost.html](../direct-cost.html) | No commission. No acquisition cost? |
| 55 | OPS-05 | [shared-factory.html](../shared-factory.html) | Two suppliers. One factory? |
| 56 | GVR-05 | [birthday-fields.html](../birthday-fields.html) | A birthday offer. A full birth date? |
| 57 | MKT-05 | [small-basket.html](../small-basket.html) | A slow seller. An important basket? |
| 58 | ENT-05 | [founder-timing.html](../founder-timing.html) | Equal partners. Earned when? |
| 59 | ECO-05 | [local-matches.html](../local-matches.html) | One hundred couriers. One hundred matches? |
| 60 | STR-05 | [combined-clients.html](../combined-clients.html) | Two hundred clients. Two hundred new clients? |
| 61 | ACC-06 | [paid-earned.html](../paid-earned.html) | Paid today. Earned today? |
| 62 | FIN-06 | [smaller-payments.html](../smaller-payments.html) | Smaller payments. Cheaper loan? |
| 63 | MKT-06 | [qualified-contacts.html](../qualified-contacts.html) | More contacts. More customers? |
| 64 | OPS-06 | [planned-stop.html](../planned-stop.html) | Keep running, or stop on purpose? |
| 65 | PPL-06 | [shared-time.html](../shared-time.html) | Choose your days. Coordinate your work. |
| 66 | STR-06 | [shared-advantage.html](../shared-advantage.html) | Share the studio. Share the advantage? |
| 67 | SUS-06 | [edible-surplus.html](../edible-surplus.html) | Eighty kilos wasted. Eighty kilos to donate? |
| 68 | ENT-06 | [visible-secret.html](../visible-secret.html) | Keep it secret. For how long? |
| 69 | ECO-06 | [faster-at-both.html](../faster-at-both.html) | Faster at both. Do both? |
| 70 | HSP-06 | [table-mix.html](../table-mix.html) | Same seats. Same capacity? |
| 71 | IS-06 | [forecast-cutoff.html](../forecast-cutoff.html) | A good forecast. Available when? |
| 72 | GVR-06 | [one-commitment.html](../one-commitment.html) | Three small orders. One big commitment? |
| 73 | ACC-07 | [machine-cost.html](../machine-cost.html) | One machine invoice. One asset cost? |
| 74 | FIN-07 | [sooner-than-what.html](../sooner-than-what.html) | A discount for paying sooner. Sooner than what? |
| 75 | MKT-07 | [chosen-by-whom.html](../chosen-by-whom.html) | Designed for an age group. Chosen by whom? |
| 76 | OPS-07 | [empty-counter.html](../empty-counter.html) | An empty counter. A waiting customer. |
| 77 | PPL-07 | [right-skill.html](../right-skill.html) | A realistic test. The right skill? |
| 78 | STR-07 | [repeatable-format.html](../repeatable-format.html) | Four signs. One business system? |
| 79 | ENT-07 | [next-promise.html](../next-promise.html) | Funded. What should we promise next? |
| 80 | SUS-07 | [reached-and-helped.html](../reached-and-helped.html) | More people reached. More people helped? |
| 81 | IS-07 | [first-rollout.html](../first-rollout.html) | A quiet pilot. Enough to learn? |
| 82 | GVR-07 | [credible-improvement.html](../credible-improvement.html) | A supplier failed. Must the relationship end? |
| 83 | ECO-07 | [cheaper-for-whom.html](../cheaper-for-whom.html) | A cheaper delivery. Cheaper for whom? |
| 84 | HSP-07 | [meal-pace.html](../meal-pace.html) | A faster lunch. Which part should be faster? |
| 85 | ACC-08 | [machine-hours.html](../machine-hours.html) | A quiet year. Less machine used? |
| 86 | FIN-08 | [back-sooner.html](../back-sooner.html) | Back sooner. Worth more? |
| 87 | MKT-08 | [familiar-pack.html](../familiar-pack.html) | A fresher pack. Still easy to find? |
| 88 | OPS-08 | [harder-to-miss.html](../harder-to-miss.html) | Check it again. Or make the mistake harder? |
| 89 | PPL-08 | [whole-job.html](../whole-job.html) | More variety. More ownership? |
| 90 | STR-08 | [more-than-one-future.html](../more-than-one-future.html) | One forecast. Three strategies? |
| 91 | ENT-08 | [route-to-market.html](../route-to-market.html) | Sell the product. Or license the invention? |
| 92 | IS-08 | [better-system-harder-exit.html](../better-system-harder-exit.html) | A better system. A harder exit? |
| 93 | GVR-08 | [no-name-still-a-conversation.html](../no-name-still-a-conversation.html) | No name. No conversation? |
| 94 | SUS-08 | [landlord-pays-who-saves.html](../landlord-pays-who-saves.html) | The landlord pays. Who saves? |
| 95 | ECO-08 | [both-or-one.html](../both-or-one.html) | A package deal. Must everyone buy both? |
| 96 | HSP-08 | [more-than-one-way-in.html](../more-than-one-way-in.html) | One exhibit. More than one way in. |
| 97 | ACC-09 | [two-balances-one-payment.html](../two-balances-one-payment.html) | Two balances. One payment. |
| 98 | FIN-09 | [protected-and-available.html](../protected-and-available.html) | One bank. Two kinds of safety. |
| 99 | MKT-09 | [more-new-people.html](../more-new-people.html) | A smaller audience. More new people? |
| 100 | OPS-09 | [keep-the-design-open.html](../keep-the-design-open.html) | Print now. Or keep the design open? |
| 101 | PPL-09 | [repair-the-handoff.html](../repair-the-handoff.html) | Separate the colleagues. Or repair the handoff? |
| 102 | STR-09 | [same-business.html](../same-business.html) | A premium offer. The same business? |
| 103 | ENT-09 | [who-still-decides.html](../who-still-decides.html) | A new leader. Who still decides? |
| 104 | IS-09 | [fresher-screen.html](../fresher-screen.html) | A fresher screen. A better decision? |
| 105 | GVR-09 | [what-was-checked.html](../what-was-checked.html) | Externally checked. What was checked? |
| 106 | SUS-09 | [bigger-order-more-mission.html](../bigger-order-more-mission.html) | A bigger order. More mission? |
| 107 | ECO-09 | [more-money-more-kits.html](../more-money-more-kits.html) | Five per cent more. More of what? |
| 108 | HSP-09 | [useful-conversations.html](../useful-conversations.html) | A busy reception. Useful conversations? |
| 109 | ACC-10 | [through-our-till.html](../through-our-till.html) | Through our till. All our revenue? |
| 110 | FIN-10 | [only-once.html](../only-once.html) | Twenty per cent. Only once? |
| 111 | MKT-10 | [easier-to-choose.html](../easier-to-choose.html) | More to choose. Easier to choose? |
| 112 | OPS-10 | [same-process.html](../same-process.html) | Within specification. Still the same process? |
| 113 | PPL-10 | [clearer-method.html](../clearer-method.html) | A higher target. A clearer method? |
| 114 | STR-10 | [anchor-customer.html](../anchor-customer.html) | One large customer. Too much dependence? |
| 115 | ENT-10 | [keep-the-job.html](../keep-the-job.html) | Keep the job. Start the business? |
| 116 | IS-10 | [separate-groups.html](../separate-groups.html) | Two versions. Two separate groups? |
| 117 | GVR-10 | [bigger-risk.html](../bigger-risk.html) | The smaller average loss. The bigger risk? |
| 118 | SUS-10 | [replace-which-part.html](../replace-which-part.html) | Repair the chair. Replace which part? |
| 119 | ECO-10 | [covered-damage.html](../covered-damage.html) | Covered damage. Unchanged behaviour? |
| 120 | HSP-10 | [whose-story.html](../whose-story.html) | A village tour. Whose story? |
| 121 | ACC-11 | [same-units-different-setups.html](../same-units-different-setups.html) | Same units. Same overhead? |
| 122 | FIN-11 | [lower-rate-less-certainty.html](../lower-rate-less-certainty.html) | A lower rate. A less certain payment? |
| 123 | MKT-11 | [see-the-advice.html](../see-the-advice.html) | A promise of expertise. What can buyers see? |
| 124 | OPS-11 | [time-to-reorder.html](../time-to-reorder.html) | Plenty on the shelf. Time to reorder? |
| 125 | PPL-11 | [strong-finish-strong-year.html](../strong-finish-strong-year.html) | A strong finish. A strong year? |
| 126 | STR-11 | [what-remains.html](../what-remains.html) | Keep improving it. Or harvest what remains? |
| 127 | ENT-11 | [complementary-founder.html](../complementary-founder.html) | The impressive co-founder. The complementary co-founder? |
| 128 | IS-11 | [respondents-or-customers.html](../respondents-or-customers.html) | Most respondents liked it. Most customers? |
| 129 | GVR-11 | [which-version.html](../which-version.html) | The meeting agreed. Which version applies? |
| 130 | SUS-11 | [collected-where.html](../collected-where.html) | Compostable here. Collected where? |
| 131 | ECO-11 | [one-more-hour.html](../one-more-hour.html) | A profitable day. One more hour? |
| 132 | HSP-11 | [another-promise.html](../another-promise.html) | A cancellation forecast. Another promise? |
| 133 | ACC-12 | [margin-per-minute.html](../margin-per-minute.html) | The best margin. Per what? |
| 134 | FIN-12 | [rent-and-exit.html](../rent-and-exit.html) | Rent the equipment. Keep the exit? |
| 135 | MKT-12 | [where-journey-breaks.html](../where-journey-breaks.html) | Many visits. Where does the journey break? |
| 136 | OPS-12 | [stock-is-not-ready.html](../stock-is-not-ready.html) | Two stores. One safety stock? |
| 137 | PPL-12 | [explain-the-difficult-part.html](../explain-the-difficult-part.html) | Fill the vacancy. Explain the difficult part? |
| 138 | STR-12 | [dedicated-tool.html](../dedicated-tool.html) | A dedicated tool. A dependable agreement? |
| 139 | ENT-12 | [better-for-whom.html](../better-for-whom.html) | Better ratings. The same business? |
| 140 | IS-12 | [blank-cell.html](../blank-cell.html) | A blank cell. A harmless average? |
| 141 | GVR-12 | [preserve-an-exception.html](../preserve-an-exception.html) | Delete on schedule. Preserve an exception? |
