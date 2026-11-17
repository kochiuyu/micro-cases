# A model improved. Is the target still the same?

<!-- legacy-case-id: 404 -->

IS-34 · Singapore · 15–20 minutes · Prediction target definition · Label governance · Comparable evaluation

![Fictional adult membership-service analysts compare two plain calendar windows and a model scorecard in a Singapore office, with no readable member information.](../model-improved-target-changed-scene.jpg)

## A score needs a defined outcome

A prediction score measures agreement with a defined outcome, not with an undefined business idea. Changing what counts as inactive changes the question being scored. Measurement research and model-documentation guidance support recording the target, its observation window and intended use. The membership business, models and results below are entirely fictional.

## Opening decision

You lead analytics for fictional Singapore membership business SeasonPass, which offers adult craft-workshop bookings. Management wants to identify members likely to make no booking in the next 90 days for a later retention-planning review. No automatic outreach, account restriction, price change or membership cancellation is authorised by this exercise.

Two frozen models, A and B, have been tested offline on the same 100 held-out member accounts. The dashboard labels both results churn accuracy: A shows 86%, B shows 92%. An analyst says the inactive-account rule changed during development, although the dashboard title stayed the same.

Choose whether to recommend B as an improvement for the existing 90-day planning task, or hold that recommendation while reconciling target definitions. One funded review session can recover the label rules and rescore both frozen prediction sets. Existing manual planning continues; there is no deadline requiring an unverified model release.

Each account contributes one prediction made at a common starting point. Both models used only information available then, with no overlap between training and test accounts. Every test account has a complete 90-day outcome record. Features, records and timestamps are valid; the unresolved issue is what outcome the labels mean.

## Evidence

| Model | Displayed churn accuracy |
| --- | --- |
| A | 86% |
| B | 92% |

**Student question:** Would you recommend B for the existing planning task now? Identify the target-definition information needed before interpreting the six-percentage-point difference. Explain why using the same 100 accounts does not by itself make the two displayed scores comparable.

## Round two

The original target, T90, is one if an account makes no booking during days 1–90 after prediction, and zero otherwise. The revised target, T30, uses days 1–30 instead. Days are complete local calendar days starting the day after prediction; each window includes its numbered endpoints.

Of the 100 accounts, 20 make no booking in all 90 days. Another 30 make none in days 1–30 but return during days 31–90; the exercise identifies these as seasonal returners. The remaining 50 book during days 1–30. Thus T90 has 20 positive labels and T30 has 50.

A was trained on T90 labels. Before training B, staff retrospectively regenerated labels on the separate historical training accounts using T30. They also generated T30 test labels after outcomes matured. The dashboard compared A against T90 and B against T30. No outcome information entered either model’s prediction features.

The review keeps each model’s binary predictions fixed, with its existing decision threshold. Scoring both against T90 gives A 86 correct accounts and B 68. Scoring both against T30 gives A 68 correct and B 92. Every score uses all 100 test accounts with equal weight; no model is retrained for this comparison.

Management confirms that the immediate brief remains 90-day absence, not a short booking pause. The 30-day label may be useful for a separate early-engagement task, but that task and any resulting customer contact have not been approved. Neither inactivity label proves cancellation, dissatisfaction or permanent departure.

**Student question:** Compare A and B separately under each fixed target. How many accounts changed label, and why is the dashboard’s apparent improvement not an improvement on the existing task? Specify what must be versioned and what further evidence is needed before any operational release.

## Debrief · Hold the business question fixed

Hold the improvement recommendation until the target is explicit. The dashboard’s 92% minus 86% is six percentage points, but it changes both model and outcome definition. Equal accounts, valid timestamps and complete records do not repair that mismatch. Accuracy answers whether predictions match the supplied labels; it does not decide which labels serve the business.

The 30 seasonal returners change from zero under T90 to one under T30. The 20 with no booking remain positive and the 50 early bookers remain negative. The positive share therefore rises from 20% to 50% solely through relabelling the same outcomes, not because more members actually left.

## Debrief · Read the stable-definition comparisons

On T90, A is correct for 86/100 = 86% and B for 68/100 = 68%. B is 18 percentage points worse on this held-out sample for the stated task. On T30, A scores 68% and B 92%; B is 24 points better on that different target.

These results support retaining A as the better of the two candidates for further T90 evaluation, not declaring A universally superior or ready for release. They also do not prove which development change caused the difference. B was developed for another target; a new model trained and tested consistently on T90 would be a new experiment.

## Debrief · A proxy is not a customer decision

No booking for 30 days and no booking for 90 days are observable behaviours with different meanings. Neither establishes that a membership ended. A customer may return seasonally, remain satisfied without booking or formally cancel for another reason. Use precise names for the measured outcomes instead of silently treating churn as a single unquestioned fact.

T30 is not inherently wrong. If managers want to study early pauses, define that separate purpose and its consequences before selecting a model. Do not choose the easier-looking target merely to improve a score or use a pause prediction to terminate access. No real member identities or sensitive information are needed for this classroom exercise.

## Debrief · Version the labels, not just the model

Retain both target specifications and label-generation versions. Record the prediction starting point, event definition, inclusive window, eligible account population, missing-outcome handling, data snapshot and owner approving the purpose. Preserve old labels and scores alongside newly generated versions so retrospective changes remain visible and reproducible.

Each reported result should name the model, threshold, target version, evaluation cohort and scoring rule. Explain that A86% uses T90 while B92% uses T30; replace the misleading comparison with separate target-specific results. Add boundary tests for bookings on days 30, 31 and 90, and do not label incomplete follow-up as absence.

## Debrief · Evaluation does not authorise intervention

Before release, evaluate the chosen target on additional appropriate cohorts, including seasonal patterns, and inspect false positives, missed absences and uncertainty. Accuracy alone does not price those errors or show whether contacting someone helps. The 100-account table is descriptive, not a guarantee of future performance or a causal retention effect.

Keep the existing manual planning process while the target owner and model reviewer approve a documented evaluation. Any later outreach design needs its own purpose, permissions, costs and assessment of customer experience. A model can predict a pause without establishing that a particular intervention will prevent it.

## Instructor note

Minutes 0–4: vote on the improvement claim and request definitions. Minutes 4–8: assign T30 and T90 labels to the three outcome groups. Minutes 8–12: compare models within each target. Minutes 12–18: design a versioned scorecard and explain why changing the target is a business decision, not routine cleanup.

IS-05 addresses quantity-unit meaning across systems; IS-24 resolves whether records describe the same entity; IS-25 separates event time from receipt time. This case stipulates correct entities, records and clocks. Its central issue is a changed prediction outcome, including retrospectively regenerated labels and incompatible evaluation meanings.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional membership company and models.100 unique adult-member test accounts, one prediction each, complete90dayoutcomes; separate historical training accounts, no future outcome features, no linkage/timestamp/missingness errors. T90 no bookingdays1–90;T30 no bookingdays1–30, inclusive localcalendar windows starting nextday.20noneall90,30firstbookingdays31–90,50bookingdays1–30.Thus20vs50positive. A trainedT90,BtrainedretrospectivelyregeneratedT30labels; fixed frozen binary predictions rescoredwithoutthresholdchange. T90 correctA86B68;T30correctA68B92, all100equalweight. InitialdisplayA86T90vsB92T30 notcomparable;stableT90difference−18points;T30+24points. All data constructed consistently, not sourceempirics; no significanceorcausalclaims. Existing90daypurpose unchanged; reviewfunded/manualplanningcontinues/no automatic customer action. Sources support concepts, not model endorsement or local legal compliance.

- [Jacobs and Wallach · Measurement and Fairness · 2021 publication / 2019 preprint](https://arxiv.org/pdf/1912.05511). Original measurement research distinguishes a construct from its operationalisation and discusses construct validity. Applied here as a bounded conceptual distinction, not an empirical finding about membership churn.
- [Mitchell and colleagues · Model Cards for Model Reporting · 2019](https://arxiv.org/pdf/1810.03993). Original documentation framework specifies intended use, metrics, thresholds and training/evaluation data. Supports explicit target-specific reporting, not certification of either fictional model.
- [NIST AI RMF Playbook · Map](https://airc.nist.gov/airmf-resources/playbook/map/). Primary guidance addresses task purpose, proxy targets, data lineage and labelling assumptions. Voluntary risk-management guidance, not a Singapore legal requirement or claim of compliance.
- [scikit-learn · accuracy_score documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html). Official metric documentation defines accuracy as the fraction correctly classified against supplied labels. That calculation does not establish the business validity of a label definition.
- [UK Government · The Government Data Quality Framework · 3 December 2020](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework). Original government guidance treats quality as fitness for purpose and calls for metadata, clear communication and change management. Used as general data-governance guidance, not local regulation.
