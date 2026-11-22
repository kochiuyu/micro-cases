# A control area. Really out of reach?

<!-- legacy-case-id: 561 -->

MKT-47 · Hong Kong · 15 minutes · Geographic experiments · Spillovers · Ad incrementality

![Two bakery colleagues compare two neighbourhood maps at a table.](../a-holdout-across-the-street-scene.jpg)

## Administrative lines are not walking barriers

Hong Kong’s Lands Department Walkin’HK illustrates how connected pedestrian routes shape walkable areas. Geographic advertising experiments similarly have to account for people moving from one area to another. The two bakery markets and their numbers are fictional.

## Opening decision

You manage two lunch markets for a Hong Kong bakery chain. The experimental ad runs in area A but not intentionally in B. Area B was chosen for similar pretest volume; the areas were not assigned at random. Compare equal-length periods with the same weekdays. Count all paid lunch baskets at participating tills in each area, not just ad clicks or coupon scans.

Each genuinely incremental basket is worth HK$20 contribution, and the A ad buys cost HK$800. Prices, opening hours, capacity and product mix stay fixed. There is no additional spend in B, and no extra cost beyond the supplied ad buy. Use a simple change-in-A minus change-in-B comparison, conditional on the design assumptions.

The chain can pause a new buy, rerun the test or expand. Its aggregate records are sufficient for the exercise. It will not collect individual locations, inspect movement histories, or contact customers.

## Evidence

| Area | Before | During |
| --- | --- | --- |
| A: chosen for ads | 220 | 280 |
| B: comparison | 230 | 260 |

**Student question:** What uplift and contribution after ad cost does the initial comparison imply? Which assumption would you check before deciding whether to expand?

## Round two

A site walk finds a covered footbridge between the markets and a shared station entrance. A separate, voluntary anonymous intercept supports the possibility that some A ad viewers bought lunch at B tills. It measures no causal share of the 30 extra B baskets and cannot tell whether A buyers would otherwise have visited B.

For this arithmetic only, assume no sales are displaced between A and B. Let s be B baskets caused by the A ads, with illustrative values from zero to 25. Absent the ad, B’s change would then be 30 minus s; assume that is also the change A would have experienced absent the ad. The total added baskets across both markets include both the corrected A uplift and s. The range is a scenario, not a measured bound.

**Student question:** At what value of s does the campaign break even across both markets under those assumptions? Would you scale now, and how would you redesign the comparison to reduce spillover?

## Debrief · Different changes tell a conditional story

A rises by 60 baskets; B by 30. The initial contrast is 30, for HK$600 of additional margin and a net loss of HK$200. This is a proxy for ad lift only if B gives a credible no-ad baseline and the rest of the comparison is sound. Similar level before the test does not prove the changes would be parallel.

## Debrief · The same spillover changes two terms

Corrected A uplift is 60 − (30 − s) = 30 + s. Add s at B to get 30 + 2s across both markets, counting each basket once. Net is HK$20 × (30 + 2s) − HK$800. It breaks even at five B spillover baskets. At 25 the scenario yields 80 additional baskets and HK$800 net. These are conditional scenarios, not evidence that the ad paid off.

## Debrief · Randomize units that shoppers do not easily cross

Do not scale on this test alone. Match multiple pairs of nonadjacent walkable markets, keep a buffer outside the readout, randomize within pairs and check baseline trends. Verify campaign exposure separation using permitted aggregate checks. Measure all eligible sales and retain any known boundary overlap for sensitivity rather than hiding it.

## Instructor note

First compute the naïve contrast, then reveal the bridge. Ask why adjusting B affects both the counterfactual trend and the count of total ad-caused purchases. If visits merely shifted from A to B, the no-displacement sensitivity would no longer apply.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All locations, tills, sales, intercept facts, margins and costs are hypothetical. No real movement logs, precise customer locations or account tracking. Assumed parallel trends and positive spillover are used only for the supplied sensitivity.

- [Hong Kong Lands Department · Walkin’HK](https://usecases.csdi.geodata.gov.hk/walkinhk/?lang=en). Opened original walkable-zone tool and dataset descriptions. Connected walking routes are context, not evidence about the fictional bridge.
- [DATA.GOV.HK · 3D Pedestrian Network](https://data.gov.hk/en-data/dataset/hk-landsd-openmap-3d-pedestrian-network). Opened official dataset description of network features and accessibility attributes. Distinct original page from the tool description, not retail exposure data.
- [Google Research · Measuring Ad Effectiveness Using Geo Experiments](https://research.google.com/pubs/archive/38355.pdf). Opened original working paper on assigned geographic treatment and control. The bakery’s initial two-market comparison is not randomized.
- [Google Ads Help · Set up Conversion Lift based on geography](https://support.google.com/google-ads/answer/14097193?hl=en-11). Opened geographic units and Contamination sections; travel across groups can reduce the observed contrast. No assumption the product serves this particular bakery or market.
- [Randomized Experimental Design via Geographic Clustering](https://arxiv.org/abs/1611.03780). Opened original research text rendered on arXiv. Describes interference due to movement across assignment boundaries and clustering to reduce it. No novel algorithm prescribed in the exercise.
