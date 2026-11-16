# The same customer. Two different records?

<!-- legacy-case-id: 284 -->

IS-24 · Hong Kong · fictional distributor · 15–20 minutes · Entity resolution · False and missed links · Linkage validation

![Two fictional colleagues compare plain customer folders in a small distributor office.](../same-customer-different-records-scene.jpg)

## A name is evidence, not an identity guarantee

Data linkage connects records believed to describe the same entity. Similar names can belong to different businesses; one business can change its displayed name. More links do not automatically mean better links. Validation must examine both incorrect links and genuine matches that were missed.

The following distributor, records and workload estimates are fictional. The exercise uses authorised business information only, not personal identifiers.

## Opening decision

A distributor must prepare tomorrow’s internal customer-return report. Its metric is the proportion of prior-quarter legal customer entities that placed at least one order again in the current quarter. It is not revenue retention, branch retention or retention of a corporate group. Each list below contains one record per active legal entity in that quarter; there are no within-quarter duplicates or invalid orders. Row alignment is for display only, not evidence of a match.

A one-hour exact-name pass would nominate Beacon Office and Maple Goods as candidates. It would leave the other names unlinked, producing a provisional 2/4, or 50%. A three-hour reviewed multi-field pass would also examine authorised organisation-reference records, dated trading-name history and business addresses. Both approaches fit tomorrow’s deadline. All staff time is funded; the two extra hours displace optional catalogue cleanup, not required work.

Choose the initial workflow, not permission to publish unchecked links. Exact-name candidates also require validation before release. Names or a shared business address alone are not conclusive. Keep original records unchanged and maintain a separate reviewable link table. No account access, credit, payment or customer outreach decision is being made.

## Evidence

| Prior-quarter display names | Current-quarter display names |
|---|---|
| Alder Paper | Alder Supplies |
| Beacon Office | Beacon Office |
| Harbour Desk | Harbor Desk |
| Maple Goods | Maple Goods |

**Student question:** Would you begin with exact-name candidates or a reviewed multi-field linkage? Explain the resource trade-off and what evidence you would require before releasing a customer-return rate.

## Round two

Before release, an analyst demonstrates a broader name rule: it links Harbor Desk to Harbour Desk as well as the two exact-name candidates. It reports 3/4, or 75%, but still leaves Alder Paper unlinked.

The authorised document review then establishes these facts. Alder Paper and Alder Supplies are the same legal entity, with a documented trading-name change and verified teaching reference K01. Beacon Office is K02 in both quarters; Maple Goods is K04 in both. Harbour Desk is K03, while Harbor Desk is a different legal entity, K05. Their similar names and shared serviced-office address do not make them one business. K01–K05 are invented teaching keys, not real registration numbers. For this small exercise, these reviewed identity findings are stipulated as correct.

**Student question:** Which customers actually returned, and what rate should the report show? Explain why a matching headline percentage can conceal wrong links, then specify how uncertain pairs should be handled.

## Resolve the entity, then count

Alder, Beacon and Maple returned. Harbour did not; Harbor is new. The return rate is 3/4 = 75%. The denominator remains the four prior-quarter legal entities. A trading-name change is not a lost customer followed by a new customer.

## A correct total can have incorrect members

The broader name rule wrongly links Harbour to Harbor: a false link. It misses Alder’s genuine continuity: a missed link. In this constructed example, one mistaken inclusion offsets one mistaken exclusion, leaving the same 75% headline as the reviewed result. The equality does not validate that rule. Exact-name-only candidates also miss Alder; even exact agreement is not a universal guarantee of identity.

## Make uncertainty visible

Maintain a versioned pair-level table containing source record keys, proposed entity key, reviewed evidence, decision, reviewer and date. Keep a separate unresolved status rather than forcing every pair into matched or unmatched. Review both accepted links and plausible missed matches. Release a qualified or delayed metric if unresolved pairs materially affect it; never invent certainty to meet a deadline. Restrict access to the authorised fields and retain source records unchanged.

## Defend the workflow choice

Exact matching can be a transparent, inexpensive candidate generator. Its one-hour estimate does not buy a validated final answer. Multi-field review uses two additional staff hours here and can detect a name change, but human review can also be wrong outside this stipulated example. The justified recommendation is a workflow with evidence and an explicit validation gate, not a claim that any algorithm or manual reviewer is infallible.

## Instructor note

0–4 minutes: show the two name lists and vote on the starting workflow. Ask what the denominator represents. 4–8 minutes: reveal the broader rule and documentary findings; calculate the rate and identify the customers behind it. 8–12 minutes: contrast a false link with a missed link and explain the accidental cancellation. 12–15 minutes: design an unresolved status and release condition.

Do not introduce invented probabilities of error, treat shared addresses as identity, or infer real-world accuracy from four entities. This is identity resolution, not IS-05’s unit interpretation or IS-20’s data-version lineage. A legal entity is the stipulated counting unit; subsidiaries and corporate-group consolidation are not extra topics to solve here.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All firms, records, teaching keys, timings and findings are fictional. Four unique active legal entities per quarter. Actual overlap is K01/K02/K04; prior set K01/K02/K03/K04, current K01/K02/K04/K05. Exact-name candidates: two of four (50%); broader name rule: three of four (75%) with one false link and one missed match; reviewed return: three of four (75%). No general accuracy, causal effect or cost saving is estimated. Row position is explicitly not a link. Actual reference documents are authorised organisational information only. Five substantive source bodies were read; optional references supply methods, not case facts. Preserve original rows; no destructive CRM merges or customer-impacting actions.

- [ONS: Data linkage and matching policy](https://www.ons.gov.uk/aboutus/transparencyandgovernance/datastrategy/datapolicies/datalinkageandmatchingpolicy). Wrong and missed links; match rate alone is not linkage quality; privacy and method trade-offs. UK policy is not a Hong Kong requirement.
- [Doidge, Christen and Harron: Quality assessment in data linkage](https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/quality-assessment-in-data-linkage). Distinguishes true matches from inferred links; discusses error, validation and uncertainty. No business error rate is imported.
- [ONS: Developing standard tools for data linkage](https://www.ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/developingstandardtoolsfordatalinkagefebruary2021). Entity-level linkage, candidate comparison and review effort. The January 2023 correction is acknowledged; no removed accuracy formula is used.
- [GLEIF: Level 1 data, Who is Who](https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-who-is-who). Organisation identifiers connect to reference information and history. This case does not require or assert universal LEI coverage.
- [Statistics Canada: Record Linkage Project Process Model (2017, archived)](https://www150.statcan.gc.ca/n1/pub/12-605-x/12-605-x2017001-eng.htm). Sections 5–6 address review, validation, linkage keys and documenting limitations. Historical methodological reference, not current local policy.
