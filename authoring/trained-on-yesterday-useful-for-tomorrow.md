# Trained on yesterday. Useful for tomorrow?

<!-- legacy-case-id: 368 -->

IS-31 · Hong Kong · fictional online retailer · 12–15 minutes · Temporal validation · Distribution shift · Forecast evaluation

![Two retail colleagues compare a calendar and plain forecasting sheets beside neatly arranged gift parcels.](../trained-on-yesterday-useful-for-tomorrow-scene.jpg)

## A forecast test should face forward

Forecasting guidance evaluates predictions using observations later than the data used to fit the model. Google’s engineering guidance similarly recommends testing on later data, and research on temporal distribution shifts studies how performance changes when a model meets a later environment.

These sources do not measure the fictional Hong Kong retailer below. Every shop, promotion, forecast and result in this exercise is invented. The question is how well a test represents future use, not which algorithm is universally best.

## Opening decision

A fictional Hong Kong online gift retailer forecasts each day’s completed paid orders at 8am to inform packing-work preparation. The target is orders, not visitors or unconstrained demand. No employee is hired, dismissed or automatically scheduled by either forecast.

Two candidate methods, A and B, have the same operating cost and use only information genuinely available by 8am: calendar variables, promotions already scheduled and completed prior-day order records. No end-of-day revenue, revised future field or target-day order count enters either forecast. Parameters and preprocessing are fitted only on the designated training rows; test outcomes are not used to tune them.

The first report randomly selects 80 of the most recent 100 consecutive daily records for fitting and holds out the other 20 for scoring. Both methods use the same split and training allowance. The report shows the sum of absolute daily errors and the average obtained by dividing by 20. An absolute error of five means a forecast is five orders above or below the actual count.

The manager must provisionally choose a method for the next planning period. A chronological evaluation has also been prepared but has not yet been presented.

## Evidence

| Random holdout: same 20 test days | A | B |
| --- | --- | --- |
| Total absolute error | 80 orders | 120 orders |
| Mean absolute error: total ÷ 20 | 4 orders per day | 6 orders per day |

Training days and test days are interspersed across the 100-day history. No raw day-level errors or uncertainty intervals are supplied.

**Student question:** Based on this report, which forecasting method would you favour, A or B? What should the test reproduce before you use it for future mornings?

## Round two

On day 81 the retailer changed from a fixed weekly promotion calendar to a different schedule aimed at a different mix of shopping occasions. The new pattern is planned to continue for the next twenty days. The order definition, recording system and 8am input-availability rules did not change.

The random split contained 64 earlier and 16 later days in training, and 16 earlier and four later days in testing. It therefore exposed both models to some later-pattern examples while testing a mixture of periods.

The second evaluation instead fits both methods on days 1–80 and scores their frozen versions on the same twenty subsequent days, 81–100. Each morning’s legitimate lagged inputs are refreshed, but no model parameters are refitted during those twenty test days. Preprocessing, target and error measure remain unchanged. Both methods receive 80 training rows in either evaluation.

| Forward test: fit days 1–80; test days 81–100 | A | B |
| --- | --- | --- |
| Total absolute error | 220 orders | 140 orders |
| Mean absolute error: total ÷ 20 | 11 orders per day | 7 orders per day |

At the close of day 100, these two chronological-test versions are the only versions ready for operational use. They would remain frozen for the next twenty-day planning period, with ordinary monitoring and human oversight. No model refitted using days 81–100 has been evaluated or made available. There is no costed third option for today’s model choice.

The promotion change is a plausible explanation for a different environment, not proof that it caused the error difference. The scores alone do not establish the size or statistical significance of any future advantage.

**Student question:** Which of the two frozen forecasting versions would you use for the next planning period? Explain which test is more relevant and one claim these results cannot support.

## A holdout is not automatically a rehearsal

In the random holdout, A has the lower mean error: 80 ÷ 20 = 4, compared with B’s 120 ÷ 20 = 6. But that test mixes earlier and later business conditions and lets training include later dates than some scored days. It asks about held-out observations within a mixed history, not purely about forecasting a later period from an earlier one.

The forward test has the same training count and metric, but preserves the direction in which time unfolds. B’s error is 140 ÷ 20 = 7, below A’s 220 ÷ 20 = 11 on those later days. The test changes which observations are used, not just their order on a report.

## Choose B on the relevant evidence, without promising seven

B is the better-supported choice among the two ready frozen versions for the stated next period. It performed better on the later period under the continuing promotion pattern, with the same operational restrictions. A’s stronger mixed-history score does not outweigh that more relevant comparison by itself.

This does not promise an error of seven orders next period, establish a statistically certain ranking, or prove that simple methods beat complex ones. The case supplies no model-class details, repeated forward windows or daily error distribution. Future weather, customers or campaigns could change the comparison again.

## Available inputs can still meet a changed world

Every prediction input here existed at its stated decision time. That avoids the unavailable same-day revenue problem in IS-06. The concern is instead whether the fitted relationships and evaluation population match the later business setting. Correct timestamps do not make changing conditions stationary.

The calendar change motivates investigating shift but does not isolate a causal mechanism. Different training/test compositions and sampling variation also affect scores. Do not subtract A’s 4 from 11 and call the seven-order difference “the effect of the promotion”.

## What a later update would need

A refitted version using more recent days is a new candidate, not the tested frozen version. Evaluate its complete retraining policy on later, untouched periods using only the information then available, or collect prospective outcomes under the intended use. Use more than one relevant forward window when the data permit; match the prediction horizon and update schedule to operations.

Continue tracking input patterns and realised errors. Equal computational cost and mean error do not provide a conversion into staffing savings, customer harm or profit. Those require separate evidence and decisions.

## Instructor note

Allow three minutes for the first vote, four for the split and promotion reveal, and five for the second decision. Ask students to sketch days 1–80 followed by 81–100, then mark where the random training observations came from.

Require a choice of ready A or B rather than an untested “retrain both now”. Discuss a future update separately. Reward distinguishing legitimate prediction inputs from time-representative evaluation. Ask what raw errors, additional periods or operational outcomes would be needed for a stronger conclusion.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The retailer, records, promotions, methods, error totals and deployment choices are fictional. No real algorithm was run and no actual company result is reported. All decision-time features are available; no test outcomes tune the models. The random and chronological tests use different observations, with the same 80 training and 20 scoring counts. Chronological models remain frozen; legitimate prior-day features refresh. Only those frozen versions are ready for the next period. Results are descriptive and contain no significance estimate, causal attribution or financial conversion. Sources were substantively read on 17 November 2026. The two scikit-learn documents share project authorship and methodological context, not independent empirical confirmation.

- [scikit-learn · TimeSeriesSplit documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html). Official reference explains chronological training/test splits and why fitting on later observations while evaluating earlier ones can be inappropriate. The classroom exercise uses one fixed 80/20 split, not a claim to run the library’s complete cross-validation routine.
- [Hyndman and Athanasopoulos · Forecasting: Principles and Practice, section 5.10](https://otexts.com/fpp3/toolbox.html#time-series-cross-validation). Authors’ textbook explains rolling forecasting origins, preceding training observations and matching forecast horizons. It supports forward evaluation; no source data or published error estimates are reused.
- [Martin Zinkevich / Google · Rules of Machine Learning, training-serving skew and Rule 33](https://developers.google.com/machine-learning/guides/rules-of-ml). Original engineering guidance distinguishes data changes from pipeline differences and recommends evaluation after the training period. Its advice is not a guarantee that a later sample perfectly predicts future performance.
- [Yao and colleagues · Wild-Time: A Benchmark of in-the-Wild Distribution Shift over Time · 2023 revision](https://arxiv.org/html/2211.14238v2). Original research separates fixed and streaming temporal evaluation and compares standard with mixed-time splits. Its benchmark focuses on gradual shifts and different tasks; neither its numerical results nor a causal effect are imported into this abrupt fictional promotion change.
- [scikit-learn · Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html). Official worked bike-demand example contrasts shuffled and time-based evaluation and illustrates overly optimistic shuffled results in that example. Related to the TimeSeriesSplit documentation, not an independent general proof that random splits always fail.
