# A good forecast. Available when?

<!-- legacy-case-id: 71 -->

IS-06 · Hong Kong · 10–15 minutes · Business analytics · Forecast evaluation · Data leakage

![An owner and colleague prepare a stationery shop for opening beside a blank notebook and a modest laptop.](../forecast-cutoff-scene.jpg)

## In the news

On 27 August 2026, HKPC announced its AI for All programme, including practical business training relevant to data analysis and workflows.

The initiative is context for assessing how a model would actually be used, not evidence of a forecasting result. The stationery shop and test report below are fictional and unrelated to that programme.

## Opening decision

Fictional classroom situation. At 8am, before opening, a Hong Kong stationery shop allocates its existing staff between the customer counter and back-room work. It wants a forecast of that day’s completed purchase transactions, not all visitors or unconstrained demand. No jobs will be cut.

The current rule uses the previous comparable weekday’s transaction count. A new model has been tested retrospectively on 20 later trading days held out from its fitting data. Its reported average absolute error is four transactions, versus 12 for the current rule.

The owner proposes using the new forecast to inform next week’s morning allocation. A colleague wants a shadow trial before relying on it. No launch has occurred. The report gives no transaction-to-staff conversion, wage saving or sales uplift.

## Evidence

| Same 20 retrospective test days | New model | Current rule |
|---|---|---|
| Sum of absolute transaction-count errors | 80 | 240 |
| Mean absolute error: total ÷ 20 | 4 transactions | 12 transactions |

**Student question:** Would you use the new forecast next week or retain the current rule while checking it? What would you need to know about how the historical test was constructed?

## Round two

An input audit finds that every model test row included that same trading day’s final till revenue. This total is exported only after the shop closes at 6pm. At 8am, neither that total nor a forecast substituting for it exists, and there is no earlier feed of it.



| At the 8am decision | Only after the 6pm close |
|---|---|
| Date and weekday; decided promotions; completed previous days’ counts | That day’s final till revenue |
| Can be available for a genuine morning forecast | Included in retrospective test rows, but unavailable that morning |

The test days really were held out from fitting. The problem is not necessarily repeated training rows: the scoring inputs contain later information. The revenue is genuine, but it arrives too late for this decision.

**Student question:** Does the reported error justify using the model at 8am now? What exactly should be changed and retested before it informs the morning allocation?

## The decision time is part of the test

A genuine 8am forecast must work with information available by 8am. The reported four-transaction error was obtained using a later closing total, so it is not valid evidence of morning performance.

This is prediction-time data leakage: later information enters a test intended to represent an earlier decision. Holding out rows from fitting is useful, but does not by itself make every input in those rows legitimate. No deception or misconduct by any person is established.

## Rebuild the information set, not just the launch screen

Keep current arrangements temporarily while removing unavailable inputs from both model fitting and evaluation. Rebuild the model and test later periods using historical snapshots of what the shop could actually know at 8am, including when data arrived, not merely the date to which they refer.

Deleting the live revenue input, filling it with zero or substituting a revenue forecast does not preserve the old score. If a forecast of revenue is introduced, evaluate that complete two-stage workflow using its real information constraints.

Same-day information is not automatically forbidden. A genuine preorder or forecast already available before the cutoff can be a valid input if the test reproduces that availability. The question is when the business could know it.

## Record predictions before observing outcomes

In a shadow trial, log the forecast and its inputs at 8am without letting the unvalidated model direct allocation. After close, compare its transaction forecast with the actual count and score the current rule on the same days.

Define practical checks for customer service and staff allocation before deployment. A count-error improvement alone does not tell the manager how many staff to move or whether service improves. Twenty days is a classroom sample, not a universal sufficient launch threshold.

## Keep the units and the uncertainty clear

Mean absolute error averages the size of the misses without cancelling overpredictions against underpredictions. Here, 80 ÷ 20 = 4 transactions and 240 ÷ 20 = 12 transactions. These are not percentage errors, correctness rates or changes in sales.

The corrected model might still outperform the current rule, or it might not. No corrected result is supplied. The current rule is a temporary fallback, not proven optimal. Do not invent a replacement score or assume the new model has no value because its first test was invalid.

## Instructor note

Ask students to draw a boundary at 8am and place each input on the side where it first becomes available. A truthful business record can still be an invalid input for an earlier forecast.

A strong answer rejects reliance on the reported score for launch, specifies rebuilding and a fair time-aware test, and distinguishes evaluation from staff-deployment policy. Simply saying “use more data” or “delete the column at launch” leaves the problem unresolved.

The shop, reports and figures are invented. The case does not accuse any real provider of leakage or supply code, a fitted model or an estimated operational improvement.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The shop, model, test days and errors are invented. The target is completed purchase transactions, not visitors, revenue or un constrained demand. The later final till revenue is unavailable at the 8 am decision; no substitute forecast exists. Test days are held out from fitting, so the stated defect is prediction-time input availability rather than necessarily overlapping rows. No corrected score, staffing formula, sales uplift or wage saving is supplied. Sources checked 14 November 2026. The HKPC announcement is a programme launch, not evidence of accuracy or completed training outcomes. The technical sources explain evaluation and pipeline principles; none studied this shop. The Microsoft page’s article text was readable despite a generic access notice.

1. [HKPC, AI for All Inclusive Programme announcement, 27 August 2026](https://www.hkpc.org/en/about-us/media-centre/press-releases/2026/hkpc-ai-for-all-inclusive-programme) — Dated local business-training initiative. Planned activities and aspirations are not treated as measured productivity or forecasting results.
2. [scikit-learn, Common pitfalls and recommended practices, section 12.2: Data leakage, maintained documentation](https://scikit-learn.org/stable/common_pitfalls.html) — Explains leakage through information unavailable at prediction time and optimistic evaluation. A preprocessing pipeline alone does not audit future-information features.
3. [Rob J. Hyndman and George Athanasopoulos, Forecasting: Principles and Practice, third edition, chapter 5](https://otexts.com/fpp3/toolbox.html) — Author-published educational text explaining genuine forecast evaluation and mean absolute error in original units. No universal test-sample threshold is inferred.
4. [Martin Zinkevich / Google, Rules of Machine Learning, Training-Serving Skew and Rules 29–31](https://developers.google.com/machine-learning/guides/rules-of-ml) — Engineering guidance on consistency between training and live inputs and logging feature values. It does not quantify the fictional model’s corrected performance.
5. [Microsoft Learn, Offline feature retrieval using a point-in-time join, updated 30 January 2026](https://learn.microsoft.com/en-us/azure/machine-learning/offline-retrieval-point-in-time-join-concepts?view=azureml-api-2) — Explains availability at prediction time, including source-data arrival delays. Used for a simple availability check, not a recommendation to buy a feature-store product.
