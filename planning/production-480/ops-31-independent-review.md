# OPS-31 independent review

**Verdict: content/source/arithmetic review passed, 17 November 2026.** Reviewed by a worker other than the draft author. No build or publication performed. Art, rendered-page/slide/handout, mobile, print and live checks remain separate gates.

Reviewed `ops-31-draft.json` and `ops-31-source-review.md`. ID 364 is provisional until integration. No substantive correction required.

## Independent source reads

I reopened all five sources and read substantive relevant material, rather than accepting the author's ledger or search snippets:

1. **Hong Kong Government LCQ21, 25 September 2025**: https://www.info.gov.hk/gia/general/202509/25/P2025092300502p.htm
   - Read the printable reply, including suitable-vehicle/load-placement guidance and enforcement context. The draft's limited historical hook is supported. It does not import penalties, prosecution counts or a real truck specification.
2. **Transport Department Road Users' Code, Loads, Long Vehicles, Towing**: https://www.td.gov.hk/en/road_safety/road_users_code/index/chapter_6_for_professional_drivers/loads_/
   - Read carrying-loads and overhang sections. The source distinguishes gross and axle weights and load security. Draft correctly defines remaining cargo allowance and does not present the mathematical footprint exercise as legal compliance or engineering approval.
3. **UK HSE, Loading**: https://www.hse.gov.uk/workplacetransport/information/loading.htm
   - Read the substantive loading guidance, including distribution, securing, floor checks, safe unloading and advance arrangements. Its role is general context, explicitly not Hong Kong law.
4. **DHL European equipment PDF**: https://www.dhl.com/content/dam/dhl/local/fi/dhl-freight/documents/pdf/fi-freight-equipment.pdf
   - Read all four pages' extracted specification text, including length, width, height, pallet places, tonnage and country-specific weight caveat. Supports multidimensional specification only; none of the fictional dimensions is claimed to come from it.
5. **DHL Freight Sweden terms, effective 1 November 2026**: https://www.dhl.com/content/dam/dhl/local/se/dhl-freight/documents/pdf/se-freight-general-terms-and-conditions-en.pdf
   - Read the effective-date context and the printed-page-14 section 6.1 rules: stackable cubic-volume treatment versus floor/load-metre calculation, including unusable area and packaging. Full-document terms review was not necessary or claimed. Web find initially returned no matches; direct reading at the relevant page succeeded. The draft expressly does not apply Swedish tariff multipliers or terms to its Hong Kong fixed quotations.

Five distinct documents, not five independent empirical studies. The two DHL documents are legitimately different equipment and pricing materials. No blocked source is counted. No source text/table is copied into the classroom exhibit.

## Geometry and arithmetic, independently checked

Python Decimal assertions and direct reasoning passed:

- Cargo is 8 × 180 = 1,440 kg; A allowance use is 48%. Four per B truck is 720 kg, below 900 kg.
- Each planning rectangle occupies 1.20 m². A has 8 m², less than eight rectangles' 9.60 m² or seven rectangles' 8.40 m². Area alone therefore proves seven/eight impossible in the nonoverlapping one-level model, even with rotation.
- Six fit A in three lengthwise rows of two: 3.60 × 2.00 m. The safe handling/restraint/distribution assumptions are separately supplied; geometry is not used to prove them.
- Four fit each B in two rows of two: 2.40 × 2.00 m, within 2.50 × 2.00 m. Their 1.40 m height fits the 1.60 m door height and 2.00 m interior. The 1.00 m transverse dimension fits the 1.80 m opening. Actual manoeuvring is covered by the stated qualified handling assessment, not derived from door width alone.
- Planning volume is 13.44 m³ versus A's 24 m³, or 56%. Spare overhead volume cannot cure the single-level floor deficit. No stacking/deck/repacking exception is available.
- B package total is HK$2,200, not per vehicle; premium is HK$400. Charges explicitly include all delivery services. B is the only quoted complete delivery, rather than merely a more expensive equally feasible choice.

## Decision integrity and fictional boundaries

All information required for the first provisional decision is available: quantities, payload allowances, package costs, trip limit, arrival constraint and the ability to request missing details. Dimensions and stackability are deliberately withheld until round two, consistent with asking what must be checked before booking.

Before the second prompt, all required floor/height/door dimensions, non-stackability and restrictions are available. Clear usable planning rectangles and agreed allowances avoid a misleading zero-clearance loading prescription. Mandatory safety checks are not a negotiable cost saving. The six/four supplied safety assessments somewhat foreshadow feasibility but students must still prove the floor constraint and cost comparison; this is acceptable for a logistics decision exercise rather than a packing puzzle.

The presentation reproduces each question exactly once and in order. First-round slides do not expose the dimensions or no-stacking reveal. The second-round slide carries the dimensions, allowances and independently verified handling/restraint/axle assumption. Floor strength remains stated in the complete page; adding the words “floor strength” to that slide's safety list would improve verbatim completeness but does not change the calculation or verdict.

## Automated checks actually run

- `validate_payload()` passed.
- Exact standalone-slide question counts and ordering checked.
- Five distinct HTTPS sources confirmed.
- Independent Decimal arithmetic/inequality assertions passed.

No full builder call, registry mutation, file integration, visual rendering, art inspection, browser test, push or live-site check was performed. Those must not be inferred from this review.
