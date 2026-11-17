# Averages are stable. What happens on the worst days?

<!-- legacy-case-id: 392 -->

IS-33 · Hong Kong · 15–20 minutes · Prediction bounds · Coverage calibration · Operational uncertainty

![Two adult parcel-dispatch colleagues compare restrained dashboard panels and a calendar beside neatly stacked unlabelled parcels in a fictional Hong Kong depot.](../same-average-different-tail-scene.jpg)

## Predicting a day, not just its average

Forecasting guidance distinguishes uncertainty about an estimated average from variation in a new outcome. A prediction bound must also be checked against outcomes, including relevant operating conditions. The parcel business, dashboards, audit counts and costs below are original fiction; no source reports these results.

## Opening decision

You manage fictional Harbour Parcel in Hong Kong. Its dashboard supports next-day capacity for optional, uncommitted parcel requests. Existing contractual deliveries, safe staffing and breaks are protected separately. Demand logs record every eligible request, including requests not accepted; capacity does not censor the observed target.

Two equally priced dashboards, A and B, share exactly the same daily mean forecasts. Each adds its own claimed 90% upper prediction bound U for next-day requests: the intended target is demand at or below U on 90% of days. This is one-sided, not a central 90% interval.

Both versions were frozen before the same 200 consecutive evaluation days. Inputs were available before each day; no outcomes were used to fit, tune or select thresholds. Calendar campaign days were flagged in advance, not chosen because actual demand turned out high. Both ordinary and campaign conditions occurred throughout the evaluation.

The headline reports mean absolute error of 100 parcels for each dashboard and demand at or below its upper bound on 180 of 200 days for each. Average headroom, upper bound minus mean forecast, is also 180 parcels for each. Management proposes treating them as interchangeable.

Before evaluation, management set a planning target of 90% upper-bound coverage separately on ordinary and scheduled campaign days. Choose which dashboard, if either, deserves a supervised pilot. The complete condition-level audit is available. This target is a fictional operating preference, not a regulator’s rule or a proven optimum.

## Evidence

| Measure | A / B |
| --- | --- |
| Mean absolute error | 100 / 100 parcels |
| Demand ≤ upper bound | 180 / 180 days |
| Mean headroom | 180 / 180 parcels |

**Student question:** Would you treat the dashboards as interchangeable? Explain what the average error and overall 90% coverage do not establish before choosing a capacity-planning pilot.

## Round two

The audit divides each consecutive 100-day half into 80 ordinary and 20 scheduled campaign days. Neither type changed definition. The following coverage counts recur in both halves, so the headline is not concealing a single switch to a new regime. Counts include equality: demand exactly at U is covered.

| Day type | A | B |
| --- | --- | --- |
| Ordinary | 78 / 80 | 72 / 80 |
| Campaign | 12 / 20 | 18 / 20 |

Across the complete audit, A’s average headroom is 200 parcels on ordinary days and 100 on campaign days; B’s is 150 and 300 respectively. Thus neither simply adds a larger buffer everywhere. These are supplied summary statistics, not enough to reconstruct individual errors, exceedance sizes or total operating costs.

Tomorrow is a scheduled campaign day. Both mean forecasts are 1,000 requests, with a supplied 95% confidence interval of 980–1,020 for the conditional mean. A’s claimed 90% upper prediction bound is 1,100; B’s is 1,300. The confidence interval and prediction bounds answer different questions and have different nominal levels.

A supervised pilot would reserve one slot per chosen upper-bound parcel. Safe capacity up to 1,400 is available. Each slot above the separately funded 1,000-slot base costs HK$2, all-in and non-refundable for tomorrow. Both options are affordable. Unused slots have no recovery value; incremental costs below the base are irrelevant here.

Requests above reserved capacity are declined before acceptance, not silently delayed or accepted without capacity. Campaign shortages can lose customer goodwill as well as contribution, but no monetary shortage loss is supplied. Keeping the funded existing human planning process is feasible; its forecast performance is not supplied.

**Student question:** Which pilot, if any, would you approve? Calculate coverage by day type and both incremental slot costs. Explain why neither the confidence interval for the mean nor overall 90% coverage guarantees tomorrow’s capacity.

## Debrief · Open the coverage denominator

Each dashboard covers 180 ÷ 200 = 90% overall. Across both halves, A covers 156 ÷ 160 = 97.5% of ordinary days but only 24 ÷ 40 = 60% of campaign days. B covers 144 ÷ 160 = 90% and 36 ÷ 40 = 90% respectively.

The same pattern occurs in each half: A has 78/80 ordinary and 12/20 campaign coverage; B has 72/80 and 18/20. A misses 40% of campaign days, versus B’s observed 10%. This repeated descriptive shortfall matters for the stated target, without establishing an exact future failure probability.

## Debrief · An average and a future outcome

The 980–1,020 confidence interval concerns the conditional mean, not the number of parcels tomorrow. Even a precisely estimated average can coexist with substantial day-to-day variation. Reserving 1,020 slots because it is the confidence interval’s upper endpoint would confuse estimation precision with operational uncertainty.

A one-sided 90% prediction bound aims to put the new outcome below its upper limit with the stated coverage under its assumptions. It is not a worst-case maximum or a guarantee for every campaign day. Nor is its meaning the same as the upper endpoint of a central 90% prediction interval.

## Debrief · Calibration is not just width

The common point forecast gives identical mean absolute error. That score cannot validate either uncertainty bound. Overall coverage can also conceal an operationally important weakness: generous ordinary-day coverage offsets A’s campaign shortfall. The prespecified calendar groups are available when planning, unlike groups defined after observing unusually high demand.

Both average headrooms equal 180: A uses 0.8 × 200 + 0.2 × 100; B uses 0.8 × 150 + 0.2 × 300. B reallocates uncertainty allowance toward campaign days. Neither a smaller average headroom nor a larger upper bound everywhere would alone establish a useful, calibrated forecast.

## Debrief · Choose a bounded next step

B is the stronger candidate for a supervised pilot under the stated condition-specific target. Tomorrow A reserves 100 extra slots for HK$200; B reserves 300 for HK$600. B costs HK$400 more. These are reservation costs, not measured net losses or a demonstrated return on investment.

B’s empirical 90% in each group is encouraging, not proof of exact calibration or economic optimality. Only 40 campaign days were evaluated, and daily outcomes may be dependent. No uncertainty interval for coverage is supplied. Retaining human planning is defensible if management will not accept the extra cost or remaining uncertainty.

For a pilot, retain human oversight and the safe capacity ceiling; record each forecast, bound, calendar flag and actual request count. Monitor coverage and exceedance size separately by day type alongside capacity costs. Specify review and stop rules in advance; use genuinely new days to evaluate any recalibrated version.

## Instructor note

Minutes 0–4: vote on the tied headline. Minutes 4–9: compute the separate coverage fractions and reconcile 90% overall. Minutes 9–14: distinguish the mean confidence interval from a new-day prediction bound and price tomorrow’s slots. Minutes 14–18: defend a pilot without claiming a guarantee or an optimal safety buffer.

IS-21 concerns uncertainty around a mean improvement; IS-16 prices point errors under asymmetric losses; IS-31 tests a changed time regime. Here the shared point forecast and valid forward evaluation are fixed. The decision turns on uncertainty-bound calibration across prespecified operating conditions, with limited evidence about future reliability.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional company, capacity, forecasts and audits. The 200 consecutive held-out days include 160 ordinary and 40 prespecified campaign days, equally split across two halves. Frozen bounds and shared point forecasts use timely inputs and complete uncensored demand. Coverage includes equality. Numerical summaries are stipulated mutually compatible classroom data, not estimates from a real dataset. One-sided 90% bound, distinct from a central interval; supplied 95% confidence interval concerns the conditional mean only. No conformal algorithm, distributional model, exact coverage guarantee, independent daily errors or causal savings are assumed. Coverage sampling uncertainty and shortage magnitudes are not supplied. Costs cover additional reservation above the funded base; no accepted commitments, safety requirements or unpaid work are compromised. Sources support methods, not these fictional values.

- [NIST/SEMATECH · Predicting a single response](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm). Distinguishes uncertainty of an estimated average from the extra variation of a new observation. Its regression formula is not used to derive the fictional bounds.
- [Hyndman and Athanasopoulos · Forecasting: Principles and Practice · Chapter 5](https://otexts.com/fpp3/toolbox.html). Sections on forecast distributions and prediction intervals support interpreting uncertainty around future outcomes; no source dataset is reproduced.
- [Angelopoulos and Bates · A Gentle Introduction to Conformal Prediction · version 6, December 2022](https://arxiv.org/abs/2107.07511). Section 3 explains why marginal coverage need not ensure coverage within input-defined groups. The case does not claim a conformal method or its theoretical guarantee.
- [scikit-learn · Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html). The coverage-fraction example checks outcomes against forecast intervals and distinguishes coverage uncertainty from the interval’s target coverage. No code or fitted model is imported.
- [AWS · Evaluating Predictor Accuracy](https://docs.aws.amazon.com/forecast/latest/dg/metrics.html). Explains held-out evaluation, mean versus quantile forecasts and upper quantiles. Used as methodological documentation, not a recommendation to purchase this service.
