# OPS-31 source and calculation review

Draft: `ops-31-draft.json`. Tentative legacy ID 364; confirm sequential ID at integration. Author review performed 17 November 2026. **Not independent review, not built, not deployed.**

## Five distinct source documents actually read

1. **Hong Kong Government, LCQ21 reply, 25 September 2025**
   - URL: https://www.info.gov.hk/gia/general/202509/25/P2025092300502p.htm
   - Access: full 36-line printable body read through web open, including reply paragraphs (1)–(3). Original non-print page returned no readable lines; printable version succeeded.
   - Supports: dated Hong Kong hook; reply discusses secure loading, enforcement, suitable vehicles and load placement.
   - Use: short historical context. No prosecution counts, penalties, causal safety results or current legal advice imported. It is distinct from the Road Users' Code, though both are official Hong Kong sources and overlapping guidance is not independent empirical corroboration.
2. **Transport Department, Road Users' Code, Loads, Long Vehicles, Towing**
   - URL: https://www.td.gov.hk/en/road_safety/road_users_code/index/chapter_6_for_professional_drivers/loads_/
   - Access: body read, especially carrying-loads lines 0–14 and overhang lines 20–28.
   - Supports: securing and separate gross/axle constraints; gross weight includes non-cargo items.
   - Use: defines why classroom net cargo allowance must not be labelled gross vehicle weight. No actual load compliance inferred from the mathematical exercise.
3. **HSE, Loading, 11 May 2021**
   - URL: https://www.hse.gov.uk/workplacetransport/information/loading.htm
   - Access: guidance body read, lines 48–84.
   - Supports: advance agreement, stable and secured pallets, load distribution, suitable loading/unloading arrangements.
   - Use: safety boundaries only; UK guidance is not presented as Hong Kong law. No restraint method or technical loading procedure prescribed.
4. **DHL Freight, Equipment specifications**
   - URL: https://www.dhl.com/content/dam/dhl/local/fi/dhl-freight/documents/pdf/fi-freight-equipment.pdf
   - Access: four-page PDF text read (60 extracted lines), with separate length/width/height, pallet-place, tonnage fields and country-weight caveat. No need to reproduce diagrams. Equipment landing-page body also read but not counted as a sixth source.
   - Supports: real specifications are multidimensional, not simply tonnage.
   - Use: no European truck dimensions or limits copied to the invented Hong Kong fleet. Do not date this undated PDF from search crawl time.
5. **DHL Freight Sweden, Terms and Conditions, valid from 1 November 2026**
   - URL: https://www.dhl.com/content/dam/dhl/local/se/dhl-freight/documents/pdf/se-freight-general-terms-and-conditions-en.pdf
   - Access: relevant text on printed page 14, section 6.1 and nearby context, read through PDF open/find; not a full review of every term in the 52-page document.
   - Supports: distinguishes stackable cubic-volume treatment from floor-use/loading-metre treatment, includes pallet/packaging in measurements.
   - Use: demonstrates commercial relevance of stackability and unusable floor area. Swedish tariff factors, liability rules and prices are not used in the classroom calculations. This is a distinct tariff document, not a duplicate format of source 4.

## Excluded leads

UNECE CTU wiki and full 2014 PDF returned 403 on substantive open. Search snippets were not treated as full reading. Neither is cited or counted. The scope was met with the five accessible documents above rather than claiming a blocked standard was reviewed.

## Original assumptions and self-check

All commercial quotations and physical figures are invented. Quotes are full-package charges; no forgotten driver/fuel/handling cost. Identical arrival windows and one trip per vehicle; no free second trip. Two small trucks count as one package at HK$2,200, not HK$2,200 each.

- Total cargo: 8 × 180 = 1,440 kg.
- A cargo allowance use: 1,440/3,000 = 48%.
- B: four per truck × 180 = 720 kg ≤ 900 kg each.
- Planning footprint each: 1.20 × 1.00 = 1.20 m². Allowances explicitly included in planning footprint; net usable planning rectangles supplied.
- A floor: 4 × 2 = 8 m². Eight need 9.6; seven need 8.4. So even clever rotation cannot fit seven. Six fit 3 rows × 2 across, 3.6 × 2 m. This establishes six as maximum in the single-level rectangular model.
- Each B: four fit 2 rows × 2 across = 2.4 × 2 m ≤ 2.5 × 2 m. Each 1.4 m high pallet fits 1.6 m door height and 2 m internal height; 1 m narrow side fits 1.8 m door width. Stated handling/axle/restraint checks supplied, not inferred from area.
- Planning volume: 8 × 1.2 × 1 × 1.4 = 13.44 m³; A = 4 × 2 × 3 = 24 m³; ratio 56%. Geometric volume spare is unusable without stacking/deck permission. No double deck offered.
- B premium: 2,200 − 1,800 = HK$400. A's apparent saving is not a feasible whole-delivery saving.

Python assertions confirmed all arithmetic and `validate_payload()` passed. Both student questions occur exactly once as standalone slide paragraphs in the required order. Full build cannot be attempted at tentative ID before preceding cases are integrated. No illustration created by this worker. No full rendered-slide, mobile or print checks run.

## Remaining production gates

Independent conceptual/source/arithmetic review, artwork generation and inspection, integration with actual next ID, full repository tests, slide/table rendering checks, live page and asset verification. The case is distinct from OPS-02 (modal expediting) and OPS-14 (route time windows); this is physical loading feasibility with a necessary-versus-sufficient capacity test.
