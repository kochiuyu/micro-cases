# MKT-31 independent review

Reviewed 17 November 2026 against mkt-31-draft.json and mkt-31-source-review.md. Outcome: **accepted for illustration and preview/build**, subject to rendered layout, generated-output parity and live release checks. No required conceptual or arithmetic corrections found. No build or publication performed by this reviewer.

## Sources independently opened and read

1. [Circana penetration dictionary](https://www.circana.com/liquid-data-go/cpg-dictionary/penetration), definition and calculation sections: directly supports buying households divided by the household universe in a specified period. The draft correctly defines its own fixed universe rather than extrapolating to Hong Kong.
2. [Circana consumer-behaviour article](https://www.circana.com/post/three-principles-of-consumer-behavior-for-increasing-brand-equity-and-market-growth), longitudinal metrics section: distinguishes current-period frequency from successive-period retention. Its strong strategic generalisations are not needed for the fictional exercise and are not adopted as causal findings.
3. [Nielsen presentation hosted by BLS](https://www.bls.gov/cex/redpanl1_link.pdf), pages 6–7: supports distinct roles of scanner and household-panel measures, and multiplicative volume decomposition. This is Nielsen material, not BLS research. Public access does not remove its copyright; the draft reproduces neither artwork nor original numerical examples.
4. [Kantar Worldpanel historical China article](https://market.worldpanelbynumerator.com/global/News/Setting-targets-for-growth), dated 30 January 2014: relevant background on penetration/frequency relationships. The draft correctly avoids importing its approximate additive target arithmetic or treating historical figures as current evidence. Optional bibliographic improvement: include the exact 2014 date already visible on the page.
5. [Worldpanel by Numerator China article](https://worldpanelbynumerator.com/insights/fmcg-growth-china-penetration-vs-loyalty-brand-strategy), dated 12 May 2026: the provider does report that the great majority of growing brands increased buyer numbers. The opening accurately attributes a reported pattern, not independent verification or proof of campaign effectiveness. Its numerical benchmarks, commercial framework and stronger causal claims are not reproduced.

Five documents, not five independent organisations. Sources provide definitions and context; all case records are explicitly fictional.

## Independent arithmetic and denominator checks

Recalculated and checked with Python: 2,000 × 4 × 1 = 1,600 × 5 × 1 = 8,000 packs; each period's revenue is 8,000 × HK$30 = HK$240,000. Buyer-count change is −20%; frequency change is +25%; factors 0.80 × 1.25 = 1.00. Additive percentage reasoning would be wrong.

All-household penetration: 20% to 16%, −4 percentage points and −20% relative. Category-buyer reach: 25% to 20%, −5 percentage points and −20% relative. Category membership is defined within each period, and brand buyers are subsets. Neither ratio is volume share. No category-volume denominator is supplied.

The fixed complete universe and matched 12-week windows make the stipulated comparison internally coherent. Frequency refers to purchasing occasions, not consumption. The product identity is valid with purchase-weighted average pack size; since every purchase averages one identical pack here, there is no weighting ambiguity affecting the exercise.

## Inference and decision quality

Net loss of 400 buyers is not 400 identified departures. No cross-period overlap is supplied, and a higher group average does not establish that continuing households individually bought more. The draft explicitly preserves both limitations and does not call frequency retention or lifetime value.

R is defensible as a diagnostic priority because reach has narrowed, but not a mathematically established optimum: no costs, margins, responses or causal intervention evidence are supplied. The instructor permits a reasoned F alternative and the debrief expressly rejects guaranteed acquisition success. Retain these caveats in every format. No claim about actual Bay Jar customers or market representativeness is made.

## Slide parity and distinctiveness

Programmatic checks confirm exact shared news and aggregate exhibit, exact q1/q2 each once on standalone slides, and exact bodies for all three substantive debrief sections. The split reveal preserves counts, unknown cross-period overlap, missing reasons/experiment, formula and both denominators. Opening slides faithfully retain the research-only decision and observation assumptions. Markdown exhibit matches the HTML values and definitions.

This replaces the problematic original cohort/retention proposal. Actual MKT-13, valuable-relationship.md, addresses expected multi-year contribution, serving costs and conditional renewal in fixed cohorts. This case instead decomposes repeated-period aggregate sales into buyer reach and frequency without known household transitions; no substantive duplication remains.

## Remaining release checks

Inspect generated artwork for style and no numerical/reveal leakage. Render the five-row dashboard, buyer table and especially the long final debrief slide; split slides if needed without dropping causal limits. Verify page/handout/Markdown and standalone prompts after build, then normal registry/navigation/collection gates and deployed revision. This review does not certify print layout, mobile appearance or classroom use.
