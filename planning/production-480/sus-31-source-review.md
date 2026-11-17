# SUS-31 production research and self-review

17 November 2026. **Draft, not accepted or published.** Tentative permanent ID 370 must be reconciled by the single integration writer. Payload: `sus-31-draft.json`. No page, art or registry entry has been built.

## Source audit

Five distinct substantive primary/official sources were opened and their relevant text read using the web tool, rather than relying on search snippets. No source supplied the fictional quantities. Links belong only in the optional reference section.

1. **European Environment Agency, Textiles and the environment: the role of design in Europe’s circular economy.** https://www.eea.europa.eu/en/analysis/publications/textiles-and-the-environment-the-role-of-design-in-europes-circular-economy-1
   - Read the water, land and greenhouse-emissions sections. The assessment distinguishes these pressures and discusses international supply chains. Used only to establish multi-category textile context; no European population totals or per-kilogram cotton estimates transferred to the fictional order.
2. **Life Cycle Initiative, Criteria for Good LCA Practice.** https://www.lifecycleinitiative.org/criteria-good-lca-practice/
   - Read criteria 1–4: purpose alignment, equivalent functional unit/boundaries, relevant categories, transparent exclusions, uncertainty and independent review. Supports the same-service comparison and the refusal to call a two-indicator exercise a complete assessment. It does not supply an automatic weighting rule or certify this draft.
3. **European Commission, Life Cycle Assessment & the EF methods.** https://green-forum.ec.europa.eu/green-business/environmental-footprint-methods/lca-ef-methods_en
   - Read the LCA overview and climate/water categories. Supports separating kg CO₂e from water indicators and considering regional scarcity. No claim that the case follows every PEF requirement or implements its complete category set.
4. **US DOE Advanced Manufacturing Office, Introduction to Life Cycle Assessment (2022).** https://www.energy.gov/sites/default/files/2022-07/2022-07-14%20-%20Intro%20to%20LCA%20-%20Slides%20and%20Transcript_compliant_0.pdf
   - Read substantive transcript on PDF page 3 (cross-impact burden shifting), page 9 (different categories), and pages 10–12 (attributional versus consequential framing). Text extraction was available; figures/layout were not needed or reproduced. Used to avoid describing an attributed comparison as proven real-world causal savings.
5. **WULCA, AWARE FAQ.** https://wulca-waterlca.org/what-is-aware/faq/
   - Read native monthly/basin factors and aggregation, water consumption definition, and multiplication by local factors. Supports consumption versus withdrawal and the need for location-sensitive assessment. We deliberately provide no numerical factor and calculate no AWARE score. The current website's method/version caveats are not hidden: this is a concept exercise, not use of a factor database.

All five returned substantive accessible text. The EEA study and official methods materials have different purposes; they are not five independent empirical tests of uniform performance. No copied tables, images, or extended quotations. The local Hong Kong connection is the explicitly fictional buyer, not a fabricated local news event.

## Fictional assumptions and calculations

- Equal service: 20 shirts × 50 clean wear-days = 1,000 clean wear-days per order. Repairs, laundering and end of life included; no replacement advantage is hidden.
- Equal price: HK$8,000 each. Both feasible and meet the stated safety/rights/chemical requirements; the case gives no water-law violation to trade off.
- A versus B climate indicator: 120 versus 160 kg CO₂e. Difference 40; relative to B, A is 25% lower.
- Freshwater consumption: 6 versus 4 m³. Difference 2; relative to B, A is 50% higher.
- Reveal inventory reconciles: A 5 high-scarcity + 1 lower-scarcity = 6 m³; B 4 lower-scarcity = 4 m³.
- Qualitative scarcity labels are not factors or measured harm. No percentages combined across environmental categories; no carbon/water conversion invented.
- Neither offer dominates across the supplied dimensions. Revelation strengthens context rather than mandating vote reversal. Choices must state the priority and accepted cost.

## Novelty and teaching checks

Main mechanism is a cross-category environmental trade-off for equal delivered service. SUS-13 focuses on comparing water interventions across catchments; SUS-25 on financial life-cycle costs. This case should not become a generic “location matters” repeat. Keep the carbon comparison and bounded claim central.

Every fact required for the two decisions is internal. No external main-text links. Questions occur once each as standalone slide paragraphs, in order; builder provides their highlighted treatment. Introductory slides do not reveal the basin information. Alternative redesign is not a free third option. Fictional textile systems are unnamed to avoid unsupported fibre stereotypes.

Self-checks performed: `validate_payload`; exact one occurrence of each decision in slides; five distinct HTTPS reference URLs; arithmetic assertions. **Not performed:** independent source/arithmetic review, artwork, rendered-page/slide/handout review, mobile/print tests, integration, deployment or live verification. These remain release gates. The full builder was intentionally not run because this is a staged draft and ID 370 is not yet the next registry ID.

## Art brief for later production

Warm watercolor-and-ink, calm Hong Kong community-centre procurement scene. Two adult colleagues compare two visually equal plain uniform shirts and blank supplier folders on a wooden table. Neither shirt should look morally “green” or conspicuously superior. No readable words, numbers, logos, environmental charts, dry riverbed or other spoiler of the second-round basin evidence. Inspect established scene artwork first; generate and inspect the final crop before integration.
