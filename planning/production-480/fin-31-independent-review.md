# FIN-31 independent review · 17 November 2026

**Decision:** accepted for illustration/build and rendered testing. No substantive arithmetic, conceptual or source-support blocker found. This review does not certify publication, classroom use or layout.

## Independent source reading

Independently opened all five cited original-publisher URLs and read the relevant public text:

- ACCA: zero-NPV definition and relevant cash flows, then scale and mutually exclusive ranking discussion. Its general reinvestment language is not adopted by the case.
- OpenStax Finance 2e 16.5: mutually exclusive projects, highest-NPV objective and scale differences. Its illustrative table is not reproduced.
- CFA Institute 2026 public summary: NPV estimates added value, IRR estimates a rate, and cash-flow modelling requires consistent after-tax treatment without double counting. No gated reading was inspected.
- FAO chapter 6: one-year conflicting-ranking example and incremental cash-flow explanation. Source has some typographical inconsistencies elsewhere; this case does not copy those figures and its own calculations were checked independently.
- Damodaran NYU Stern original exercises: problems 11–14 explicitly pose ranking comparisons and capital-rationing questions. Correctly presented as exercises, not an asserted worked solution or empirical study.

All five are educational sources. They do not establish this fictional workshop's returns, funding, risk or customer choices. No fabricated news hook, empirical claim or reused source illustration was found.

## Arithmetic and assumptions

Exact rational recalculation: S IRR=3/10; L IRR=6/25. At the supplied 10% requirement, S NPV=80,000/11, or HK$7,272.73; L NPV=140,000/11, or HK$12,727.27. The increment is HK$60,000 today for HK$72,000 in one year, IRR20%, NPV60,000/11=HK$5,454.55. The statement explicitly compares NPVs before rounding, avoiding the one-cent discrepancy from subtracting the displayed rounded totals.

At HK$100,000 both projects are feasible individually and L best fulfils the stated objective. At HK$70,000, S alone is the feasible positive-NPV choice; L's NPV is unchanged and its immediate shortfall is HK$30,000. The withdrawal is properly common to alternatives and excluded from project cash flows. Single-period cash flows, equal supplied risk/hurdle, nonrepeatability, indivisibility, mutual exclusivity, no postponement and no extra funding close the usual loopholes. Returning unused cash prevents treating it as destroyed wealth or inventing additional projects.

The comparison is educational, not an investment recommendation. Optional wording refinement: call the exhibit receipts "forecast net receipts" explicitly so readers cannot mistake the supplied model for a guarantee. The existing hypothetical and risk statements already make its scope clear.

## Novelty and parity

Read the actual FIN-08 (back-sooner.md) and FIN-19 (best-project-best-package.md). This is a distinct IRR scale-conflict case with one terminal receipt, unlike FIN-08's payback/full-life timing contrast and FIN-19's compatible but indivisible project-package optimisation and complementarity. Its funding reveal reinforces feasibility rather than reusing those mechanisms.

Shared news, exhibit/formulas and round-two text match the slide payload exactly. Opening constraints are faithfully compressed across the two opening slides. Each decision appears exactly once as a standalone paragraph, before debriefs. HTML and Markdown data and formulas agree. Independent checks confirmed both questions' sequencing. The source list remains separate from student teaching content.

## Remaining production gates

Review illustration for visual consistency and no numeric/reveal leakage; inspect final page, handout and all slides for fit and parity. Dense formula/debrief slides may need splitting. Run the full repository checks after integration and confirm the deployed revision and live behaviour. No mobile, physical-print or classroom certification follows from this content review.
