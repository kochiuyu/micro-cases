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
| 142 | SUS-12 | [same-energy-different-time.html](../same-energy-different-time.html) | The same electricity. A different time? |
| 143 | ECO-12 | [winning-is-information.html](../winning-is-information.html) | The highest estimate. The best bid? |
| 144 | HSP-12 | [find-the-entrance.html](../find-the-entrance.html) | They can read the map. Can they find the entrance? |
| 145 | ACC-13 | [cheaper-material-dearer-batch.html](../cheaper-material-dearer-batch.html) | Cheaper material. A dearer batch? |
| 146 | FIN-13 | [cash-before-risk.html](../cash-before-risk.html) | The invoice is sold. Is the risk gone? |
| 147 | MKT-13 | [valuable-relationship.html](../valuable-relationship.html) | Our biggest customer. Our most valuable relationship? |
| 148 | OPS-13 | [promise-by-when.html](../promise-by-when.html) | Promise Friday. Based on which stock? |
| 149 | PPL-13 | [same-leave-fair-process.html](../same-leave-fair-process.html) | The same leave entitlement. The same fair process? |
| 150 | STR-13 | [open-before-the-network.html](../open-before-the-network.html) | Open first. Be ready first? |
| 151 | ENT-13 | [beyond-familiar-contacts.html](../beyond-familiar-contacts.html) | Ask the people we know. Meet the people they do not know? |
| 152 | IS-13 | [same-mix-different-answer.html](../same-mix-different-answer.html) | Better in both groups. Worse overall? |
| 153 | GVR-13 | [flag-and-review.html](../flag-and-review.html) | The score flagged the refund. Who can review it? |
| 154 | SUS-13 | [a-litre-in-which-place.html](../a-litre-in-which-place.html) | A litre saved. In which place? |
| 155 | ECO-13 | [promise-costs.html](../promise-costs.html) | A promise of quality. Costly for whom? |
| 156 | HSP-13 | [a-window-not-any-time.html](../a-window-not-any-time.html) | A tidy room. An unwanted interruption? |
| 157 | ACC-14 | [an-invoice-not-a-receipt.html](../an-invoice-not-a-receipt.html) | An invoice issued. Cash likely? |
| 158 | FIN-14 | [same-money-same-rate.html](../same-money-same-rate.html) | Rising cash flows. The same discount rate? |
| 159 | MKT-14 | [same-price-two-comparisons.html](../same-price-two-comparisons.html) | The same price. Two comparisons. |
| 160 | OPS-14 | [route-and-window.html](../route-and-window.html) | A shorter route. A missed window? |
| 161 | PPL-14 | [market-rate-existing-colleague.html](../market-rate-existing-colleague.html) | A market-rate recruit. An overlooked colleague? |
| 162 | STR-14 | [own-or-share-the-operation.html](../own-or-share-the-operation.html) | Own the operation. Share the local knowledge? |
| 163 | ENT-14 | [sell-now-stay-to-build.html](../sell-now-stay-to-build.html) | Sell now. Stay to build? |
| 164 | IS-14 | [accurate-alerts-useful-alerts.html](../accurate-alerts-useful-alerts.html) | Accurate alerts. Useful alerts? |
| 165 | GVR-14 | [training-not-a-holiday.html](../training-not-a-holiday.html) | A training visit. A supplier’s holiday? |
| 166 | SUS-14 | [shade-now-shade-later.html](../shade-now-shade-later.html) | A cooler courtyard. Ready for a hotter summer? |
| 167 | ECO-14 | [entry-fee-extra-visit.html](../entry-fee-extra-visit.html) | A low visit price. A high-use member? |
| 168 | HSP-14 | [script-and-occasion.html](../script-and-occasion.html) | Follow the script. Recognise the occasion? |
| 169 | ACC-15 | [profit-not-cash.html](../profit-not-cash.html) | A profit. Where did the cash go? |
| 170 | FIN-15 | [one-company-one-hurdle.html](../one-company-one-hurdle.html) | One company. One hurdle rate? |
| 171 | MKT-15 | [same-benefit-different-frame.html](../same-benefit-different-frame.html) | The same benefit. A different frame? |
| 172 | OPS-15 | [returned-checked-where-next.html](../returned-checked-where-next.html) | Returned and checked. Where next? |
| 173 | PPL-15 | [who-gets-a-chance.html](../who-gets-a-chance.html) | The reliable choice. The only person who gets a chance? |
| 174 | STR-15 | [nearby-or-three-cities.html](../nearby-or-three-cities.html) | Three nearby outlets. Three different cities? |
| 175 | ENT-15 | [equal-votes-no-decision.html](../equal-votes-no-decision.html) | Equal votes. No decision? |
| 176 | IS-15 | [challenge-and-authorise.html](../challenge-and-authorise.html) | Challenge the forecast. Who may override it? |
| 177 | GVR-15 | [paid-for-which-use.html](../paid-for-which-use.html) | We bought the photograph. May we reuse it? |
| 178 | SUS-15 | [more-trees-better-habitat.html](../more-trees-better-habitat.html) | More trees. Better habitat? |
| 179 | ECO-15 | [printer-and-printing.html](../printer-and-printing.html) | A cheaper printer. More expensive printing? |
| 180 | HSP-15 | [before-guests-travel.html](../before-guests-travel.html) | Decide before guests travel. Or wait? |
| 181 | ACC-16 | [small-but-in-the-note.html](../small-but-in-the-note.html) | A small payment. An important correction? |
| 182 | FIN-16 | [cash-moves-together.html](../cash-moves-together.html) | Two income streams. One bad month? |
| 183 | MKT-16 | [new-pack-new-sales.html](../new-pack-new-sales.html) | A new pack. New sales? |
| 184 | OPS-16 | [started-is-not-finished.html](../started-is-not-finished.html) | Keep every station busy. Finish orders sooner? |
| 185 | PPL-16 | [someone-else-can-cover.html](../someone-else-can-cover.html) | One expert. Who else can cover? |
| 186 | STR-16 | [compatible-with-what.html](../compatible-with-what.html) | Join the standard. Keep the distinctive feature? |
| 187 | ENT-16 | [one-first-market.html](../one-first-market.html) | Many possible users. One first market? |
| 188 | IS-16 | [same-error-different-loss.html](../same-error-different-loss.html) | The same average error. The same business cost? |
| 189 | GVR-16 | [same-exception-same-reasons.html](../same-exception-same-reasons.html) | One exception. A fair rule? |
| 190 | SUS-16 | [a-booking-not-just-a-button.html](../a-booking-not-just-a-button.html) | Online first. A service for everyone? |
| 191 | ECO-16 | [one-more-quotation.html](../one-more-quotation.html) | One more quotation. Worth the search? |
| 192 | HSP-16 | [a-room-for-this-conversation.html](../a-room-for-this-conversation.html) | Lively to one table. Too loud to another? |
| 193 | ACC-17 | [coverage-is-not-a-population.html](../coverage-is-not-a-population.html) | Most of the value. Enough of the evidence? |
| 194 | FIN-17 | [cheaper-credit-tighter-promise.html](../cheaper-credit-tighter-promise.html) | More credit. A tighter promise? |
| 195 | MKT-17 | [which-improvement-would-you-give-up.html](../which-improvement-would-you-give-up.html) | They want everything. What will they trade? |
| 196 | OPS-17 | [steady-output-later-peak.html](../steady-output-later-peak.html) | Steady output. Or follow the peak? |
| 197 | PPL-17 | [whose-evidence-reached-the-table.html](../whose-evidence-reached-the-table.html) | Everyone agrees. Has everyone’s evidence been heard? |
| 198 | STR-17 | [defend-the-position-not-every-price.html](../defend-the-position-not-every-price.html) | Defend every customer. Defend the right position? |
| 199 | ENT-17 | [partners-change-the-opportunity.html](../partners-change-the-opportunity.html) | A venture plan. Which partners help shape it? |
| 200 | IS-17 | [cover-the-task-not-every-permission.html](../cover-the-task-not-every-permission.html) | Easy access. Appropriate access? |
| 201 | GVR-17 | [the-date-that-changes-the-rule.html](../the-date-that-changes-the-rule.html) | A new policy. Effective from when? |
| 202 | SUS-17 | [cover-the-service-not-the-signup-count.html](../cover-the-service-not-the-signup-count.html) | Many volunteers. A dependable service? |
| 203 | ECO-17 | [ready-only-if-both-are-ready.html](../ready-only-if-both-are-ready.html) | We will launch if you do. |
| 204 | HSP-17 | [keys-are-not-a-completion-record.html](../keys-are-not-a-completion-record.html) | Keys handed over. Ready to move in? |
| 205 | ACC-18 | [one-target-two-views.html](../one-target-two-views.html) | Keep the budget. Update the forecast? |
| 206 | FIN-18 | [cash-on-the-day-it-is-needed.html](../cash-on-the-day-it-is-needed.html) | Earn more interest. Available on which day? |
| 207 | MKT-18 | [permission-is-not-a-message-quota.html](../permission-is-not-a-message-quota.html) | More reminders. More relationships? |
| 208 | OPS-18 | [orders-are-not-consumption.html](../orders-are-not-consumption.html) | Customer demand moved a little. Orders moved a lot. |
| 209 | PPL-18 | [count-the-work-not-only-the-reports.html](../count-the-work-not-only-the-reports.html) | More people to lead. The same manager’s day? |
| 210 | STR-18 | [another-way-to-spend-the-evening.html](../another-way-to-spend-the-evening.html) | The rival across the road. Or a different way to meet the need? |
| 211 | ENT-18 | [will-the-routine-travel.html](../will-the-routine-travel.html) | It worked in the last business. Will the routine travel? |
| 212 | IS-18 | [features-pass-work-still-waits.html](../features-pass-work-still-waits.html) | The feature is delivered. Is the work supported? |
| 213 | GVR-18 | [keep-the-meeting-in-bounds.html](../keep-the-meeting-in-bounds.html) | A useful industry meeting. Which topics are off limits? |
| 214 | SUS-18 | [who-can-shape-the-ballot.html](../who-can-shape-the-ballot.html) | Residents will vote. Who can get onto the ballot? |
| 215 | ECO-18 | [ready-stock-is-not-endless.html](../ready-stock-is-not-endless.html) | The shared resource is open. Will it last? |
| 216 | HSP-18 | [rent-is-not-the-whole-site.html](../rent-is-not-the-whole-site.html) | The highest rent. The right neighbour? |
| 217 | ACC-19 | [lower-return-better-investment.html](../lower-return-better-investment.html) | A lower return. A better investment? |
| 218 | FIN-19 | [best-project-best-package.html](../best-project-best-package.html) | The best project. The best set of projects? |
| 219 | MKT-19 | [one-name-two-promises.html](../one-name-two-promises.html) | One name for two promises? |
| 220 | OPS-19 | [through-the-depot-or-to-a-shelf.html](../through-the-depot-or-to-a-shelf.html) | Straight through the depot. Or onto a shelf? |
| 221 | PPL-19 | [lose-a-team-member-keep-a-colleague.html](../lose-a-team-member-keep-a-colleague.html) | Lose a team member. Keep a colleague? |
| 222 | STR-19 | [next-market-missing-capability.html](../next-market-missing-capability.html) | The next market. The next missing capability? |
| 223 | ENT-19 | [start-a-business-buy-one-to-run.html](../start-a-business-buy-one-to-run.html) | Start a business. Or buy one to run? |
| 224 | IS-19 | [one-switch-two-records.html](../one-switch-two-records.html) | One switch-over. Two records to reconcile? |
| 225 | GVR-19 | [board-agreed-record-the-conditions.html](../board-agreed-record-the-conditions.html) | The board agreed. Did it record the conditions? |
| 226 | SUS-19 | [carbon-project-happen-anyway.html](../carbon-project-happen-anyway.html) | A carbon project. Would it happen anyway? |
| 227 | ECO-19 | [price-cap-shortage-remains.html](../price-cap-shortage-remains.html) | A price cap. Which shortage remains? |
| 228 | HSP-19 | [ten-minutes-without-knowing.html](../ten-minutes-without-knowing.html) | Ten minutes to wait. Ten minutes without knowing? |
| 229 | ACC-20 | [internal-price-two-refusals.html](../internal-price-two-refusals.html) | An internal price. Two sensible refusals? |
| 230 | FIN-20 | [good-year-distributable-surplus.html](../good-year-distributable-surplus.html) | A good year. A distributable surplus? |
| 231 | MKT-20 | [points-earned-benefits-understood.html](../points-earned-benefits-understood.html) | Points earned. Benefits understood? |
| 232 | OPS-20 | [count-the-risky-shelves.html](../count-the-risky-shelves.html) | Count everything twice. Or risky shelves more often? |
| 233 | PPL-20 | [whose-example-changes-the-habit.html](../whose-example-changes-the-habit.html) | The instruction is clear. Whose example changes the habit? |
| 234 | STR-20 | [one-network-local-decisions.html](../one-network-local-decisions.html) | One network. Every decision at headquarters? |
| 235 | ENT-20 | [stop-the-venture-keep-the-promise.html](../stop-the-venture-keep-the-promise.html) | Stop the venture. Keep the promise? |
| 236 | IS-20 | [trace-the-number-not-only-the-chart.html](../trace-the-number-not-only-the-chart.html) | A persuasive dashboard. Can we trace the number? |
| 237 | GVR-20 | [one-response-clear-authority.html](../one-response-clear-authority.html) | An incident declared. Who is directing the response? |
| 238 | SUS-20 | [fund-the-years-after-opening.html](../fund-the-years-after-opening.html) | The pilot grant ends. Who maintains the benefit? |
| 239 | ECO-20 | [the-rival-customers-would-choose.html](../the-rival-customers-would-choose.html) | Two sellers merge. Which competition disappears? |
| 240 | HSP-20 | [one-booking-different-visits.html](../one-booking-different-visits.html) | One booking. Several different visits? |
| 241 | ACC-21 | [two-products-which-cost-changes.html](../two-products-which-cost-changes.html) | Two products. Which cost changes? |
| 242 | FIN-21 | [same-yield-different-duration.html](../same-yield-different-duration.html) | Same yield. Same interest-rate risk? |
| 243 | MKT-21 | [one-customer-which-channel.html](../one-customer-which-channel.html) | One customer. Which channel earns the sale? |
| 244 | OPS-21 | [components-ready-in-the-right-week.html](../components-ready-in-the-right-week.html) | Enough components. Ready in the right week? |
| 245 | PPL-21 | [useful-feedback-useful-to-do-what.html](../useful-feedback-useful-to-do-what.html) | Useful feedback. Useful to do what? |
| 246 | STR-21 | [follow-the-plan-recognise-the-pattern.html](../follow-the-plan-recognise-the-pattern.html) | Follow the plan. Recognise a better pattern? |
| 247 | ENT-21 | [clever-solution-costly-problem.html](../clever-solution-costly-problem.html) | The clever solution. The costly problem? |
| 248 | IS-21 | [improvement-beyond-ordinary-variation.html](../improvement-beyond-ordinary-variation.html) | The number improved. Beyond ordinary variation? |
| 249 | GVR-21 | [cheap-contract-uncapped-exposure.html](../cheap-contract-uncapped-exposure.html) | A cheap contract. An uncapped exposure? |
| 250 | SUS-21 | [efficient-device-total-energy.html](../efficient-device-total-energy.html) | A more efficient device. Less total energy? |
| 251 | ECO-21 | [lower-price-groups-stay-separate.html](../lower-price-groups-stay-separate.html) | A lower price for some. Can the groups stay separate? |
| 252 | HSP-21 | [room-features-usable-space.html](../room-features-usable-space.html) | The room is larger. Does it feel usable? |
| 253 | ACC-22 | [more-production-more-profit.html](../more-production-more-profit.html) | More production. More profit? |
| 254 | FIN-22 | [pay-for-time-to-decide.html](../pay-for-time-to-decide.html) | Commit now. Pay for the option to wait? |
| 255 | MKT-22 | [last-click-whole-contribution.html](../last-click-whole-contribution.html) | The last click. The whole contribution? |
| 256 | OPS-22 | [shorten-the-task-or-the-project.html](../shorten-the-task-or-the-project.html) | Shorten the longest task. Finish the project sooner? |
| 257 | PPL-22 | [different-priorities-better-package.html](../different-priorities-better-package.html) | A disagreement over pay. Or over the package? |
| 258 | STR-22 | [copy-the-product-copy-the-advantage.html](../copy-the-product-copy-the-advantage.html) | A copied product. A copied advantage? |
| 259 | ENT-22 | [enough-pledges-enough-capacity.html](../enough-pledges-enough-capacity.html) | Enough pledges. Enough capacity to fulfil? |
| 260 | IS-22 | [one-winner-many-comparisons.html](../one-winner-many-comparisons.html) | One winning result. How many chances to win? |
| 261 | GVR-22 | [complaint-upheld-protection-continues.html](../complaint-upheld-protection-continues.html) | A complaint upheld. Is retaliation prevented? |
| 262 | SUS-22 | [cash-choice-goods-available.html](../cash-choice-goods-available.html) | Cash support. Or the goods people need? |
| 263 | ECO-22 | [two-markups-one-final-customer.html](../two-markups-one-final-customer.html) | Two markups. One final customer? |
| 264 | HSP-22 | [same-nights-more-departures.html](../same-nights-more-departures.html) | The same occupied nights. The same cleaning workload? |
| 265 | ACC-23 | [on-the-truck-in-whose-stock.html](../on-the-truck-in-whose-stock.html) | On the truck. In whose year-end stock? |
| 266 | FIN-23 | [unpriced-not-ownership-free.html](../unpriced-not-ownership-free.html) | No price today. No dilution tomorrow? |
| 267 | MKT-23 | [better-taste-different-expectation.html](../better-taste-different-expectation.html) | Better taste. Or a different expectation? |
| 268 | OPS-23 | [next-ticket-next-eligible-ticket.html](../next-ticket-next-eligible-ticket.html) | One shared line. Who can serve the next ticket? |
| 269 | PPL-23 | [one-team-bonus-visible-contribution.html](../one-team-bonus-visible-contribution.html) | One team bonus. Whose contribution is visible? |
| 270 | STR-23 | [profitable-division-useful-parent.html](../profitable-division-useful-parent.html) | A profitable division. A useful parent? |
| 271 | ENT-23 | [available-resources-repeatable-service.html](../available-resources-repeatable-service.html) | Use what is available. Build what is repeatable? |
| 272 | IS-23 | [lowest-score-next-month.html](../lowest-score-next-month.html) | The worst branches improved. Did coaching work? |
| 273 | GVR-23 | [evidence-exists-history-shown.html](../evidence-exists-history-shown.html) | The evidence exists. Can its history be shown? |
| 274 | SUS-23 | [small-raise-large-withdrawal.html](../small-raise-large-withdrawal.html) | Just above the threshold. No help at all? |
| 275 | ECO-23 | [better-wages-more-than-higher-cost.html](../better-wages-more-than-higher-cost.html) | Better wages. More than a higher cost? |
| 276 | HSP-23 | [see-the-dish-build-the-meal.html](../see-the-dish-build-the-meal.html) | A beautiful display. An easy meal to assemble? |
| 277 | ACC-24 | [expected-repairs-already-liability.html](../expected-repairs-already-liability.html) | Expected repairs. Already a liability? |
| 278 | FIN-24 | [lower-premium-repeated-deductible.html](../lower-premium-repeated-deductible.html) | A lower premium. How much risk stays here? |
| 279 | MKT-24 | [preferred-compared-never-shortlist.html](../preferred-compared-never-shortlist.html) | Preferred when compared. Never on the shortlist? |
| 280 | OPS-24 | [bulk-price-total-stock-cost.html](../bulk-price-total-stock-cost.html) | A bulk discount. A lower total stocking cost? |
| 281 | PPL-24 | [reward-suggestion-change-reason.html](../reward-suggestion-change-reason.html) | Reward the suggestion. Change the reason for suggesting? |
| 282 | STR-24 | [common-training-separate-businesses.html](../common-training-separate-businesses.html) | Compete in sales. Cooperate in the foundation? |
| 283 | ENT-24 | [paid-work-paid-result.html](../paid-work-paid-result.html) | Paid for the work. Paid for the result? |
| 284 | IS-24 | [same-customer-different-records.html](../same-customer-different-records.html) | The same customer. Two different records? |
| 285 | GVR-24 | [permission-service-permission-research.html](../permission-service-permission-research.html) | Permission for service. Permission for research? |
| 286 | SUS-24 | [outside-site-not-outside-impact.html](../outside-site-not-outside-impact.html) | Cleaner here. Dirtier somewhere else? |
| 287 | ECO-24 | [split-surplus-compare-alternative.html](../split-surplus-compare-alternative.html) | Split the surplus. Compare which alternative? |
| 288 | HSP-24 | [review-history-current-offer.html](../review-history-current-offer.html) | More reviews. A more trustworthy picture? |
| 289 | ACC-25 | [depreciated-schedule-worth-carrying.html](../depreciated-schedule-worth-carrying.html) | Depreciated on schedule. Still worth carrying? |
| 290 | FIN-25 | [shipment-complete-documents-complying.html](../shipment-complete-documents-complying.html) | Payment promised. Documents accepted? |
| 291 | MKT-25 | [every-week-present-moment.html](../every-week-present-moment.html) | Advertise every week. Or be present at the moment? |
| 292 | OPS-25 | [units-sold-trips-walked.html](../units-sold-trips-walked.html) | The most units sold. The most trips walked? |
| 293 | PPL-25 | [two-managers-one-workday.html](../two-managers-one-workday.html) | Two reasonable managers. One impossible instruction? |
| 294 | STR-25 | [better-product-missing-installer.html](../better-product-missing-installer.html) | A better product. Who will install it? |
| 295 | ENT-25 | [founder-at-the-right-moment.html](../founder-at-the-right-moment.html) | Every customer gets the founder. Can the business grow? |
| 296 | IS-25 | [recorded-at-noon-happened-at-noon.html](../recorded-at-noon-happened-at-noon.html) | Recorded at noon. Happened at noon? |
| 297 | GVR-25 | [different-team-same-firms-work.html](../different-team-same-firms-work.html) | A different team. Reviewing whose work? |
| 298 | SUS-25 | [cheaper-now-through-the-service-life.html](../cheaper-now-through-the-service-life.html) | The cheapest green purchase. Over which lifetime? |
| 299 | ECO-25 | [buy-today-wait-for-the-discount.html](../buy-today-wait-for-the-discount.html) | Buy today. Wait for tomorrow’s discount? |
| 300 | HSP-25 | [festival-spending-stays-local.html](../festival-spending-stays-local.html) | The festival fills the town. Does the town benefit? |
| 301 | ACC-26 | [a-group-sale-a-group-profit.html](../a-group-sale-a-group-profit.html) | A group sale. A group profit? |
| 302 | FIN-26 | [cash-flows-continue-ending-worth.html](../cash-flows-continue-ending-worth.html) | Cash flows continue. How much is the ending worth? |
| 303 | MKT-26 | [same-price-clearer-customer-value.html](../same-price-clearer-customer-value.html) | A lower price. A clearer customer business case? |
| 304 | OPS-26 | [same-pass-rate-different-flow.html](../same-pass-rate-different-flow.html) | Ninety-eight per cent at every stage. What leaves the line? |
| 305 | PPL-26 | [slower-colleague-harder-queue.html](../slower-colleague-harder-queue.html) | A slower colleague. Or a harder queue? |
| 306 | STR-26 | [local-design-global-learning.html](../local-design-global-learning.html) | One global product. One global learning direction? |
| 307 | ENT-26 | [endorsed-by-whom-credible-to-whom.html](../endorsed-by-whom-credible-to-whom.html) | Endorsed by whom. Credible to whom? |
| 308 | IS-26 | [two-confirmations-one-order.html](../two-confirmations-one-order.html) | Two confirmations. One order? |
| 309 | GVR-26 | [dispute-pending-service-continuing.html](../dispute-pending-service-continuing.html) | A dispute pending. What can still continue? |
| 310 | SUS-26 | [transition-jobs-between-dates.html](../transition-jobs-between-dates.html) | A better transition. For whom, and when? |
| 311 | ECO-26 | [same-cap-different-reductions.html](../same-cap-different-reductions.html) | Same target. Same reduction at every plant? |
| 312 | HSP-26 | [confirmed-here-missed-there.html](../confirmed-here-missed-there.html) | The check-in works. Does the handoff work? |
| 313 | ACC-27 | [result-improved-warning-missed.html](../result-improved-warning-missed.html) | The result improved. Which warning was missed? |
| 314 | FIN-27 | [credit-limit-available-draw.html](../credit-limit-available-draw.html) | A credit limit. How much can we draw? |
| 315 | MKT-27 | [smaller-pack-cheaper-quantity.html](../smaller-pack-cheaper-quantity.html) | A smaller price tag. A cheaper quantity? |
| 316 | OPS-27 | [short-shipment-which-allocation.html](../short-shipment-which-allocation.html) | Short supply. Which allocation keeps promises? |
| 317 | PPL-27 | [flexible-business-predictable-team.html](../flexible-business-predictable-team.html) | Flexible for the business. Predictable for the team? |
| 318 | STR-27 | [one-acquisition-one-operating-system.html](../one-acquisition-one-operating-system.html) | One acquisition. One operating system? |
| 319 | ENT-27 | [one-experiment-comparable-learning.html](../one-experiment-comparable-learning.html) | Learn from one experiment. Keep the learning comparable? |
| 320 | IS-27 | [consistent-sensor-correct-measurement.html](../consistent-sensor-correct-measurement.html) | The sensor is consistent. Is it measuring correctly? |
| 321 | GVR-27 | [local-limits-shared-exposure.html](../local-limits-shared-exposure.html) | Within every limit. Outside the overall boundary? |
| 322 | SUS-27 | [restore-later-not-reversible.html](../restore-later-not-reversible.html) | Restore later. Lose something now? |
| 323 | ECO-27 | [winning-effort-vanishing-prize.html](../winning-effort-vanishing-prize.html) | More effort. No larger prize. |
| 324 | HSP-27 | [fewer-stops-clearer-story.html](../fewer-stops-clearer-story.html) | Three landmarks, or one connected story? |
| 325 | ACC-28 | [market-price-design-cost-gap.html](../market-price-design-cost-gap.html) | A market price. A design cost gap? |
| 326 | FIN-28 | [hedge-moves-delivered-cost.html](../hedge-moves-delivered-cost.html) | The hedge moves. Does it move with our cost? |
| 327 | MKT-28 | [understand-benefit-picture-setup.html](../understand-benefit-picture-setup.html) | They understand the benefit. Can they picture doing it? |
| 328 | OPS-28 | [reserve-capacity-commit-units.html](../reserve-capacity-commit-units.html) | Reserve capacity. Commit to every unit? |
| 329 | PPL-28 | [cheerful-greeting-emotional-cost.html](../cheerful-greeting-emotional-cost.html) | A cheerful greeting. At what emotional cost? |
| 330 | STR-28 | [attractive-segment-mobility-barrier.html](../attractive-segment-mobility-barrier.html) | Enter the attractive segment. Cross which barrier? |
| 331 | ENT-28 | [family-successor-fair-path.html](../family-successor-fair-path.html) | A family successor. A fair path into responsibility? |
| 332 | IS-28 | [dramatic-line-axis-context.html](../dramatic-line-axis-context.html) | The line looks dramatic. What does the axis say? |
| 333 | GVR-28 | [stopped-until-cleared.html](../stopped-until-cleared.html) | Stop the work. Who may restart it? |
| 334 | SUS-28 | [better-place-same-people.html](../better-place-same-people.html) | A neighbourhood improved. Who can still stay? |
| 335 | ECO-28 | [chosen-lock-unexpected-need.html](../chosen-lock-unexpected-need.html) | Choose freely now. Restrict a future choice? |
| 336 | HSP-28 | [booked-time-shared-room.html](../booked-time-shared-room.html) | A full appointment book. A workable morning? |
| 337 | ACC-29 | [one-package-three-promises.html](../one-package-three-promises.html) | One package price. Three promises? |
| 338 | FIN-29 | [same-ownership-different-exit.html](../same-ownership-different-exit.html) | The same ownership. The same exit proceeds? |
| 339 | MKT-29 | [private-remedy-public-reassurance.html](../private-remedy-public-reassurance.html) | Resolve one complaint. Reassure which audience? |
| 340 | OPS-29 | [service-percentage-which-denominator.html](../service-percentage-which-denominator.html) | Ninety-five per cent service. Of what? |
| 341 | PPL-29 | [project-ends-team-learning.html](../project-ends-team-learning.html) | A project ends. What does the team learn? |
| 342 | STR-29 | [current-model-different-unit.html](../current-model-different-unit.html) | Improve the current model. Protect a different one? |
| 343 | ENT-29 | [internal-idea-independent-venture.html](../internal-idea-independent-venture.html) | An internal idea. An independent venture? |
| 344 | IS-29 | [assigned-pilot-actual-use.html](../assigned-pilot-actual-use.html) | Assigned to the pilot. Actually using it? |
| 345 | GVR-29 | [accurate-for-whom.html](../accurate-for-whom.html) | A high average accuracy. An uneven burden? |
| 346 | SUS-29 | [later-benefit-present-choice.html](../later-benefit-present-choice.html) | A benefit far away. Less valuable to whom? |
| 347 | ECO-29 | [still-enrolled-still-preferred.html](../still-enrolled-still-preferred.html) | The default stays. Is it the preferred choice? |
| 348 | HSP-29 | [same-entitlement-different-remedy.html](../same-entitlement-different-remedy.html) | A fair recovery. Must it be identical? |
| 349 | ACC-30 | [ratio-rises-cash-falls.html](../ratio-rises-cash-falls.html) | A healthier ratio. A healthier business? |
| 350 | FIN-30 | [interest-paid-principal-due.html](../interest-paid-principal-due.html) | Affordable interest. A repayable principal? |
| 351 | MKT-30 | [same-shoppers-different-missions.html](../same-shoppers-different-missions.html) | One customer profile. Two shopping missions? |
| 352 | OPS-30 | [one-lot-shared-ingredient.html](../one-lot-shared-ingredient.html) | One production lot. One recall boundary? |
| 353 | PPL-30 | [contract-unchanged-promise-changed.html](../contract-unchanged-promise-changed.html) | Nothing in the contract changed. Did the promise? |
| 354 | STR-30 | [stronger-position-for-how-long.html](../stronger-position-for-how-long.html) | A stronger position. For how long? |
| 355 | ENT-30 | [venture-story-testable-assumptions.html](../venture-story-testable-assumptions.html) | One venture story. Several testable assumptions? |
| 356 | IS-30 | [summary-or-bounded-retrieval.html](../summary-or-bounded-retrieval.html) | A summary alone. Or bounded retrieval? |
| 357 | GVR-30 | [delegated-work-retained-accountability.html](../delegated-work-retained-accountability.html) | The supplier promises compliance. Who remains accountable? |
| 358 | SUS-30 | [trigger-to-review-not-to-build.html](../trigger-to-review-not-to-build.html) | A new safeguard. Who helps decide when it changes? |
| 359 | ECO-30 | [outside-the-quiet-deal.html](../outside-the-quiet-deal.html) | A better private deal. A cost outside the contract? |
| 360 | HSP-30 | [rooms-without-a-destination.html](../rooms-without-a-destination.html) | A busy season. A destination all year? |
| 361 | ACC-31 | [half-finished-units-of-work.html](../half-finished-units-of-work.html) | Half finished. How many units of work? |
| 362 | FIN-31 | [higher-percentage-more-value.html](../higher-percentage-more-value.html) | A higher percentage. More value created? |
| 363 | MKT-31 | [same-sales-smaller-buyer-base.html](../same-sales-smaller-buyer-base.html) | The same sales. A smaller buyer base? |
| 364 | OPS-31 | [half-empty-is-there-room.html](../half-empty-is-there-room.html) | The truck is half empty. Is there room? |
| 365 | PPL-31 | [trained-them-can-they-use-it.html](../trained-them-can-they-use-it.html) | We trained them. Can they use it? |
| 366 | STR-31 | [control-the-core-design-every-extension.html](../control-the-core-design-every-extension.html) | Control the core. Design every extension? |
| 367 | ENT-31 | [enthusiasts-love-it-ordinary-buyers-adopt-it.html](../enthusiasts-love-it-ordinary-buyers-adopt-it.html) | Enthusiasts love it. Can ordinary buyers adopt it? |
| 368 | IS-31 | [trained-on-yesterday-useful-for-tomorrow.html](../trained-on-yesterday-useful-for-tomorrow.html) | Trained on yesterday. Useful for tomorrow? |
| 369 | GVR-31 | [information-without-challenge.html](../information-without-challenge.html) | The board has information. Does it have time to challenge? |
| 370 | SUS-31 | [lower-carbon-heavier-water-footprint.html](../lower-carbon-heavier-water-footprint.html) | Lower carbon. A heavier water footprint? |
| 371 | ECO-31 | [average-quality-who-sells.html](../average-quality-who-sells.html) | The average quality. Who still sells? |
| 372 | HSP-31 | [fewer-bookings-behind-the-curve.html](../fewer-bookings-behind-the-curve.html) | Fewer bookings today. Behind the booking curve? |
| 373 | ACC-32 | [rejects-which-loss-belongs-in-stock.html](../rejects-which-loss-belongs-in-stock.html) | Rejects. Which loss belongs in stock? |
| 374 | FIN-32 | [more-return-more-equity-risk.html](../more-return-more-equity-risk.html) | More return on equity. More risk to equity? |
| 375 | MKT-32 | [same-reward-different-recipient.html](../same-reward-different-recipient.html) | A generous referral. A trustworthy recommendation? |
| 376 | OPS-32 | [first-in-first-to-expire.html](../first-in-first-to-expire.html) | First in. First to expire? |
| 377 | PPL-32 | [someone-knows-who-knows-who.html](../someone-knows-who-knows-who.html) | Someone knows. Who knows who? |
| 378 | STR-32 | [on-both-platforms.html](../on-both-platforms.html) | On both platforms. Loyal to neither? |
| 379 | ENT-32 | [investor-access-commercial-freedom.html](../investor-access-commercial-freedom.html) | The investor brings customers. Which customers may we serve? |
| 380 | IS-32 | [positive-average-same-rollout.html](../positive-average-same-rollout.html) | A positive average. The same rollout for everyone? |
| 381 | GVR-32 | [generous-donation-whose-benefit.html](../generous-donation-whose-benefit.html) | A donation is generous. Whose interests does it serve? |
| 382 | SUS-32 | [one-contaminated-load.html](../one-contaminated-load.html) | A clean recycling stream. One contaminated load? |
| 383 | ECO-32 | [two-plans-who-chooses.html](../two-plans-who-chooses.html) | Two plans. Who chooses which one? |
| 384 | HSP-32 | [open-rooms-unavailable-purpose.html](../open-rooms-unavailable-purpose.html) | The rooms stay open. Can the stay still work? |
| 385 | ACC-33 | [same-revenue-different-break-even.html](../same-revenue-different-break-even.html) | The sales target is met. Are the costs covered? |
| 386 | FIN-33 | [business-price-share-price.html](../business-price-share-price.html) | A business price. A price for the shares? |
| 387 | MKT-33 | [free-trial-time-to-experience.html](../free-trial-time-to-experience.html) | A free trial. Enough time to experience the benefit? |
| 388 | OPS-33 | [sample-passed-shipment-passed.html](../sample-passed-shipment-passed.html) | A sample passed. Did the shipment pass? |
| 389 | PPL-33 | [strong-inside-disconnected-outside.html](../strong-inside-disconnected-outside.html) | Strong inside. Disconnected outside. |
| 390 | STR-33 | [larger-factory-lower-cost-from-what.html](../larger-factory-lower-cost-from-what.html) | Larger factory. Lower cost from what? |
| 391 | ENT-33 | [patent-to-use-freedom-to-sell.html](../patent-to-use-freedom-to-sell.html) | A patent to use. Freedom to sell? |
| 392 | IS-33 | [same-average-different-tail.html](../same-average-different-tail.html) | Averages are stable. What happens on the worst days? |
| 393 | GVR-33 | [terms-disclosed-terms-understood.html](../terms-disclosed-terms-understood.html) | The terms are disclosed. Are they understood? |
| 394 | SUS-33 | [useful-heat-dependable-supply.html](../useful-heat-dependable-supply.html) | A useful by-product. A dependable input? |
| 395 | ECO-33 | [seller-tax-who-bears-it.html](../seller-tax-who-bears-it.html) | A tax on the seller. Who pays in the end? |
| 396 | HSP-33 | [upgrade-accepted-right-room-unsold.html](../upgrade-accepted-right-room-unsold.html) | An upgrade accepted. The right room left unsold? |
| 397 | ACC-34 | [useful-prototype-recognition-date.html](../useful-prototype-recognition-date.html) | A useful prototype. An asset already? |
| 398 | FIN-34 | [guaranteed-loan-future-cash.html](../guaranteed-loan-future-cash.html) | A guaranteed loan. Whose future cash? |
| 399 | MKT-34 | [same-message-who-must-agree.html](../same-message-who-must-agree.html) | The same message. Who must agree? |
| 400 | OPS-34 | [equal-work-balanced-line.html](../equal-work-balanced-line.html) | Equal work. A balanced line? |
| 401 | PPL-34 | [one-company-two-identities.html](../one-company-two-identities.html) | One company. Two identities. |
| 402 | STR-34 | [strong-threat-costly-commitment.html](../strong-threat-costly-commitment.html) | A strong threat. A costly commitment? |
| 403 | ENT-34 | [large-market-reachable-business.html](../large-market-reachable-business.html) | A large market. A reachable first business? |
| 404 | IS-34 | [model-improved-target-changed.html](../model-improved-target-changed.html) | A model improved. Is the target still the same? |
| 405 | GVR-34 | [optional-consent-blocked-service.html](../optional-consent-blocked-service.html) | The customer is unhappy. Is consent still voluntary? |
| 406 | SUS-34 | [help-available-document-barrier.html](../help-available-document-barrier.html) | Help is available. Can people claim it? |
| 407 | ECO-34 | [more-demand-more-supply-when.html](../more-demand-more-supply-when.html) | More demand today. More supply when? |
| 408 | HSP-34 | [minimum-spend-exclusive-time.html](../minimum-spend-exclusive-time.html) | A minimum spend. A banquet worth accepting? |
