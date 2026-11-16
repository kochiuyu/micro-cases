# One production lot. One recall boundary?

<!-- legacy-case-id: 352 -->

OPS-30 · Hong Kong · 15–20 minutes · Lot genealogy · Traceability · Mock recall

![A food-packing supervisor examines sealed ingredient containers and two lot trays during a tabletop traceability exercise.](../one-lot-shared-ingredient-scene.jpg)

## The reporting question

Traceability standards link transformed inputs to outputs. This fictional prospective design exercise tests whether finer run codes remain useful when material crosses a boundary.

## Opening decision

Fictional Hong Kong food packer Bay Pantry is designing records for a future dry-snack packing process. This is a tabletop mock recall using invented quantities and simulated ingredient movements: no food is unsafe, released or sold. The safety lead has fixed all applicable food-safety, notification, withdrawal and disposal procedures; students may not relax them. Both proposed designs are stipulated to meet the applicable requirements when implemented as specified. The choice concerns additional traceability granularity, not whether to comply.

A day contains runs A, B and C producing 600, 400 and 800 packs respectively. Each pack has one identifier at the selected design level. Design D assigns one day lot and records all ingredient sources and destinations for that whole day, taking four staff-minutes. Design R assigns three run lots and records each run’s ingredient inputs and output destinations, taking four minutes per run. All other recording and operating work is identical. The manager can afford either and prefers R if its additional eight minutes provide a defensible narrower boundary; there is no monetary estimate of future recall savings.

## Evidence

| Run | Packs | Opening ingredient and process assumptions |
| --- | --- | --- |
| A | 600 | Ingredient X only; complete input/output and destination links. |
| B | 400 | Ingredient Y only; complete input/output and destination links. |
| C | 800 | Ingredient Z only; complete input/output and destination links. |
| Separation | All runs | Inputs, tools and processes are segregated; no transfers, carryover, shared rework or other cross-links. |
| Exercise rule | All descendants | If X is implicated, contain every output that could include X. Do not narrow below what the chosen records and verified physical evidence establish. D cannot distinguish packs by run; R can. |

**Student question:** Which prospective lot-recording design would you choose, and what containment quantity could each design support if ingredient X were implicated under the opening assumptions?

## Round two

During the tabletop test of R, an observer’s time-stamped exercise log reveals a simulated transfer from ingredient X’s opened container into run B before B’s entire 400-pack batch was mixed. The proposed run log still says “Y only”: it has no field or approval step for transfers. The observer evidence is sufficient to establish that the transfer occurred, but cannot identify a smaller subset within B. Run A’s 600 packs remain linked to X.

The exercise evidence independently confirms that C used sealed Z on a physically separate line with dedicated tools and no transfers, rework or shared process contact. No other outputs or ingredient remnants exist in this deliberately bounded scenario. A and B have complete downstream destination records. C’s exclusion is supported by these verified facts, not merely by its different code. The team must correct the prototype and repeat the test before any future production; the mock event does not authorise releasing real food.

**Student question:** After the mock transfer is revealed, what is the defensible exercise containment boundary, and what must change before the finer design is approved for future production?

## The opening choice

Choose R conditionally on its records matching actual material movements. D takes four minutes and can support only a whole-day 1,800-pack boundary. R takes 12 minutes, eight more, and under the stated complete separation can support an X-related 600-pack boundary for A. Its potential narrowing is 1,200 packs, but that is not expected savings or a guarantee about an actual incident. D remains a defensible simpler option when the wider boundary is accepted; neither option may omit required safety steps.

## Follow ingredients, not just labels

After the reveal, X has two output descendants: A’s 600 packs and B’s 400. The exercise boundary is therefore 1,000 packs with their downstream destinations, not A alone. Because B was mixed and no smaller subset is identifiable, all 400 B packs belong in the boundary. C’s 800 packs can be excluded in this bounded exercise only because independent evidence establishes separation. In a real incident, unresolved links require escalation and a suitably conservative scope, not presumptive exclusion.

## Repair the physical genealogy

Add transfer events linking source ingredient lot/container, quantity and unit, time, destination run and responsible operator. Capture additions, returns, carryover and rework, not only scheduled ingredients. Link every transformed input to output run codes, pack quantities and destinations. Use contemporaneous entry and a verification step before accepting a run’s completed record. Quantities help reconcile the path but a balanced total alone does not establish which packs received an ingredient.

## Retest before use

Repeat a mock trace in both directions, from X to all output destinations and from B back to every ingredient source. Include an unexpected transfer and check that the revised record detects the A–B link without relying on the observer’s separate rescue log. Document gaps and corrective action; approve the prototype only when the evidence is complete. Extra identifiers cannot make shared material independent. Finer lots improve resolution only when event records and physical controls support the claimed boundaries.

## Instructor note

Release the opening and table, then Q1. Reveal the simulated transfer and ask Q2 before giving either answer. Draw X to A and B, with Z separately feeding C. Confirm arithmetic: 600 + 400 + 800 gives 1,800; three times four minutes gives 12; 600 + 400 gives 1,000. Challenge “different codes mean safe” and “all-day containment is always necessary.” This is prospective design and a mock exercise, not advice to delay an actual recall or exclude products contrary to authorities’ directions.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Fictional prospective design and tabletop exercise. All quantities, times, movements and evidence are invented. No actual unsafe product or recall is represented. Foreign standards and guidance provide operational background, not Hong Kong legal advice.

- [Hong Kong Centre for Food Safety, Food Recall Guidelines](https://www.cfs.gov.hk/english/import/import_icfsg_08.html). Local guidance on prompt action, identification, segregation, records and corrective action. Mandatory procedures are not traded against recordkeeping effort.
- [GS1 Global Traceability Standard, Release 2.0 (August 2017)](https://www.gs1.org/sites/default/files/docs/traceability/GS1_Global_Traceability_Standard_i2.pdf). Input/output relationships and event records support traceability across transformations. Identification granularity has implementation trade-offs; this is a standard, not local law.
- [GS1 US, Foodservice Implementation Guideline for Case-Level Traceability, Release 1.0 (2017), Appendix B](https://www.gs1us.org/content/dam/gs1us/documents/industries-insights/foodservice-traceability-application-guideline-r1.0-fnl-feb-14.pdf). Transformation input and output events require shared links. Related GS1 implementation guidance, not an independent empirical validation.
- [US FDA, Traceability Lot Code](https://www.fda.gov/food/food-safety-modernization-act-fsma/traceability-lot-code). Explains lot identifiers, linked data and the possible scope benefit of smaller lots. US regulatory context is not applied as a Hong Kong legal requirement or compliance timetable.
- [Food Standards Australia New Zealand, Food Industry Food Recall Protocol (September 2024), section 5.7](https://www.foodstandards.gov.au/sites/default/files/2024-09/Food%20Industry%20Food%20Recall%20Protocol_September%202024%20%5B1MB%5D.pdf). Mock exercises, review and training identify weaknesses before genuine recalls. Australian legal obligations and prescribed reporting times are not imported into this case.
