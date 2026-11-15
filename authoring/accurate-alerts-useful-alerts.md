# Accurate alerts. Useful alerts?

<!-- legacy-case-id: 164 -->

IS-14 · Hong Kong · 10–15 minutes · Base rates · Precision and recall · Operational thresholds

![A household-goods shop manager and colleague discuss stock checks beside shelves and a replenishment trolley.](../accurate-alerts-useful-alerts-scene.jpg)

## Industry context

On 10 December 2025, DFI Retail Group described Wellcome’s Hong Kong ICT Awards recognition for a smart-logistics project involving slow-moving inventory and a hybrid picking system. Its account connects warehouse information and operations with store availability.

That company account is context, not an independent performance test or evidence about shelf-alert accuracy. The small shop, detector and every count and cost below are original fiction; no results are attributed to Wellcome or its partners.

## Opening decision

A fictional Hong Kong household-goods shop tests a read-only alert that asks staff to inspect a possibly empty product facing. One observation means one product-facing at one scheduled snapshot. A gap means the facing is empty at that moment. This is ordinary, non-safety-critical stock checking, not theft detection, food-safety monitoring or an employee-performance score. No customer or staff images are used.

The same detector offers two fixed score cutoffs. Lower threshold L generates more alerts; higher threshold H generates fewer. The scores are not assumed to be calibrated probabilities. Staff check every alert before any replenishment action; the tool cannot place orders. Routine replenishment and required safety work continue under either choice. Both workloads fit the paid staffing plan, with no overtime or speed-up required.

An independent manual audit labels all 1,000 observations, including those without alerts. Of these, 200 are actual gaps and 800 are not. The table gives each threshold’s complete outcomes on this same audit. Neither threshold was selected or tuned on these observations. For this classroom comparison only, use these rates as the next comparable batch’s planning assumptions, not as a performance guarantee.

An alert costs HK$2 to check, whether true or false. Each gap left unalerted incurs an additional expected HK$14 lost contribution before the next routine round. Checking a true alert enables prompt correction and avoids that loss; its HK$2 includes the incremental action cost. These are supplied complete marginal planning values, not measured sales effects. There is no additional detector fee difference, and ordinary operating costs are unchanged. Choose between L and H to minimise expected checking cost plus missed-gap loss.

## Evidence

| Outcome per 1,000 observations | L | H |
|---|---:|---:|
| Gap, alert | 180 | 100 |
| No gap, alert | 80 | 40 |
| Gap, no alert | 20 | 100 |
| No gap, no alert | 720 | 760 |

**Student question:** Would you use L or H for a comparable 1,000-observation batch? Count all staff checks and missed gaps, calculate the supplied expected cost, and explain why a more selective alert is not automatically the better business choice.

## Round two

The manager considers a second aisle with a lower gap frequency. A separate complete audit supplies a planning mix of 20 actual gaps and 980 non-gaps per 1,000 observations. For this thought experiment, assume the within-group detection rates transfer unchanged: L alerts on 90% of actual gaps and 10% of non-gaps; H alerts on 50% of actual gaps and 5% of non-gaps. This stability is explicitly stipulated, not inferred merely because the software is unchanged. The two settings are not a before-and-after estimate of the alert’s causal effect.

The resulting planning counts are L: 18 true alerts, 98 false alerts, 2 missed gaps and 882 correctly unalerted non-gaps. H: 10 true alerts, 49 false alerts, 10 missed gaps and 931 correctly unalerted non-gaps. There are still 1,000 observations, and check cost HK$2, missed-gap expected loss HK$14, staffing and operating assumptions are unchanged. No retraining or threshold change has occurred. These are modelled counts for the supplied mix, not a forecast that real batches must hit exactly.

**Student question:** Which threshold would you choose for the second aisle under the supplied model? Calculate the share of alerts that are genuine gaps and the expected cost for both settings, then say how confident you should be in the cost difference.

## Count the work, not just the mistakes

Every alert creates a check, including a useful one. Initially L generates 180 + 80 = 260 checks and misses 20 gaps. Its expected cost is 260 × HK$2 + 20 × HK$14 = HK$800. H generates 100 + 40 = 140 checks and misses 100 gaps: 140 × HK$2 + 100 × HK$14 = HK$1,680. L costs HK$240 more in checks but avoids HK$1,120 in modelled missed-gap loss. It is the lower-cost choice between these two thresholds under the supplied assumptions.

## Keep the denominator visible

Among actual gaps, L detects 90% and H detects 50%: this is recall, also called sensitivity. Among non-gaps, L correctly stays quiet 90% of the time and H 95%: this is specificity. Precision instead asks what share of alerts are actual gaps. Initially L’s precision is 180/260 ≈ 69.2%; H’s is 100/140 ≈ 71.4%. H has slightly more useful alerts proportionally but finds far fewer gaps.

## A smaller base rate changes the alert mix

In the second aisle, only 2% rather than 20% of observations are gaps. L’s precision becomes 18/116 ≈ 15.5%; H’s becomes 10/59 ≈ 16.9%. The within-group rates stayed fixed by assumption, but the much larger non-gap group supplies most alerts. “It finds 90% of gaps” never meant “90% of its alerts are gaps”. Lower precision alone does not prove the detector deteriorated. In actual use, check both the population mix and the conditional rates.

## A calculated winner, a fragile margin

Second aisle: L costs 116 × HK$2 + 2 × HK$14 = HK$260; H costs 59 × HK$2 + 10 × HK$14 = HK$258. H narrowly wins the specified two-option model by HK$2 per 1,000 observations. That is not strong evidence of a robust real-world advantage. L entails 57 extra checks to avoid 8 additional missed gaps. With check cost fixed at HK$2, the break-even loss per missed gap is HK$114/8 = HK$14.25. Above that value L wins; below it H wins, holding all counts fixed.

## Measure the decision, then validate locally

Report the counts, alert workload, useful-alert share and missed gaps together. Accuracy alone can flatter a quiet detector when gaps are rare. Before committing at scale, validate both thresholds on representative held-out observations and check the marginal costs and ability to act in time. Do not use the same data repeatedly to tune and then claim an unbiased final test. No conclusion here chooses the best threshold among every possible cutoff or proves a financial return over turning the system off.

## Instructor note

Start with the first table and ask pairs to circle the cells that create staff work. Reveal the second setting only after the first cost choice. Ask students to predict whether the share of useful alerts rises or falls before calculating it. Accept H as the exact second-round answer under the stated objective, with a clear warning that HK$2 is fragile; do not award “higher precision always wins”. Have students identify the different denominators for recall and precision. An optional sensitivity discussion uses HK$14.25, without claiming the true missed-gap loss is known. No coding or outside reading is required.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All shop details, classifier outcomes, audits, staffing conditions and monetary values are original fiction. No source model, company or real dataset is evaluated. Two fixed thresholds are compared, not every possible policy. All observations receive independent ground-truth labels in the fictional audit, including unalerted observations, avoiding verification only among alerts. Separate settings have different base rates; this is not a causal before-after intervention. Sensitivity and specificity are expressly held constant in the second setting for the exercise; real-world transfer requires validation. Both thresholds are evaluated on the same observations within each setting, and H can be nested within L. Counts are planning outcomes under the supplied assumptions, not guaranteed future frequencies. HK$2 applies to all alerts and includes incremental checking and correction; HK$14 applies only to missed gaps and is a supplied expected contribution loss. No additional correction loss, fixed-cost difference, overtime or omitted safety obligation is assumed. There are no personal-data, medical, lending or worker-selection decisions. Source publications do not validate these costs or guarantee successful replenishment. Distinct from IS-02 chatbot authority/consequences, IS-09 freshness/action timing and IS-13 composition-standardised comparisons: the mechanism here is base-rate-dependent precision and threshold economics using a complete confusion table. Five source bodies were read on 15 November 2026. Two Google lessons share one publisher and two scikit-learn documentation sections share one project; these are complementary teaching references, not four independent empirical studies. DFI is a first-party corporate account. No source examples or tables are copied.

- [DFI Retail Group · Wellcome smart-logistics recognition · 10 December 2025](https://www.dfiretailgroup.com/en/about-us/awards/wellcome-s-smart-logistics-wins-certificate-of-merit-at-hong-kong-ict-awards-2025/). Dated regional inventory-technology context. First-party account, not an independent shelf-alert trial or evidence for the fictional figures.
- [Google ML Crash Course · Thresholds and the confusion matrix](https://developers.google.com/machine-learning/crash-course/classification/thresholding). Explains thresholding and the four classification outcomes. Supports the conceptual distinction, not any store-performance claim.
- [Google ML Crash Course · Accuracy, recall and precision](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall). Defines denominators and discusses choosing metrics in light of error consequences. Same publisher as the preceding lesson.
- [scikit-learn · Tuning the decision threshold for class prediction](https://scikit-learn.org/stable/modules/classification_threshold.html). Distinguishes statistical prediction from operational decision and discusses validation when tuning thresholds. No software use is required in the case.
- [scikit-learn · Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html). Binary precision/recall and class-likelihood-ratio sections explain denominators and prevalence-dependent predictive interpretation. Same project as preceding documentation; conditional-rate transfer is an explicit case assumption, not a universal guarantee.
