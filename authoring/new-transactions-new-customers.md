# New transactions. Or genuinely new customers?

<!-- legacy-case-id: 416 -->

IS-35 · Hong Kong · 15–20 minutes · Grouped validation · Customer-level dependence · Generalisation population

![Two adult colleagues at a fictional Hong Kong stationery shop sort abstract transaction cards into customer-group folders beside plain and patterned notebooks, without readable personal information.](../new-transactions-new-customers-scene.jpg)

## A new row may belong to a familiar customer

A held-out transaction is not necessarily a held-out customer. Validation guidance distinguishes random rows from entire groups when observations share stable characteristics. The useful split depends on whom the model must predict for. The retailer, customers, records and scores below are fictional; no personal data or real model is used.

## Opening decision

You manage an offline evaluation for fictional Hong Kong stationery retailer PaperHarbour. The intended model predicts whether a first-time adult customer will choose a plain or patterned notebook. It uses a short, voluntary style questionnaire completed before the choice. It will not set prices, eligibility or access, and no recommendation is live.

The research file contains five distinct completed purchase occasions for each of 100 adult customers: 500 rows. Each occasion has its own questionnaire and observed binary choice. All answers existed before that choice. Customer codes are used only for grouping, never as predictors; no purchase history, future field or target-derived feature enters the model.

Both evaluation designs use the same predetermined learning procedure, features, target and error rule: one error for the wrong category, zero otherwise. Preprocessing is fitted only within training data. No scored outcomes tune settings. The historical period has no stipulated regime change; the question is new-customer generalisation, not a forecast across a changed market.

Design A randomly holds out 100 transaction rows and fits on 400. Design B holds out all five rows of 20 customers and fits on the 400 rows of the other 80. Both are funded. The manager prefers A’s reported 92 correct predictions because the rows themselves were never used for fitting.

## Evidence

| Measure | Result |
| --- | --- |
| Training / scored rows | 400 / 100 |
| Correct / incorrect | 92 / 8 |
| Accuracy / error rate | 92% / 8% |

**Student question:** Which design better evaluates predictions for first-time customers, A or B? What must be checked before treating A’s 92% accuracy as evidence for that intended use, even though the rows and prediction-time features are valid?

## Round two

An audit shows A’s 100 scored rows belong to 80 customers: 60 contribute one scored row and 20 contribute two. Every one of those customers also has training rows. The remaining 20 customers appear only in training. No transaction row is duplicated, and all 100 customers are represented in A’s training set.

The questionnaire includes recurring combinations of style answers that differ across customers and correlate with their choices. Even without a customer-code predictor, a flexible model can exploit those patterns when the same customer appears on both sides. The audit establishes overlap and a plausible mechanism, not how much of the score it caused.

Design B’s model is fitted afresh using the same fixed procedure. Its 100 scored rows come exclusively from 20 unseen customers. It correctly predicts 68 choices, making 32 errors. The two designs have equal training-row counts but different training customers and different test rows; they are not two scores on one frozen fitted model.

The planned first-time service concerns one initial purchase per customer, not all repeat transactions. Before scoring, the team specified B’s first recorded purchase for each held-out customer as the relevant subset. On those 20 initial purchases it gets 14 correct and six wrong. No held-out customer’s later outcome is used to fit or update it.

This cohort contains only customers with five recorded purchases. It may not represent first-time visitors who never return. No performance threshold, uncertainty interval, sales effect or prospective first-time-customer result is supplied. The current non-personalised display remains available while the team chooses a defensible evaluation design; neither score authorises deployment.

**Student question:** Which evaluation would you carry forward? Calculate B’s overall and first-purchase error rates, distinguish transaction counts from customer counts, and specify what remains untested. Can the 92% versus 68% difference be called a causal measure of leakage?

## Debrief · Hold out the unit you want to generalise to

A’s score is 92/100 = 92% accuracy, or eight errors per 100 scored transactions. Those transactions are new rows but not new customers relative to fitting. Holding out each row once does not establish the customer separation required by this first-time-customer question.

B keeps each customer entirely on one side. Its 80 training customers contribute 400 rows; its 20 held-out customers contribute 100. This better represents predicting for people whose previous records were not available to the learner. It does not make the questionnaire more informative or guarantee a better score.

## Debrief · Use the relevant occasion as well as the right group

B’s all-transaction accuracy is 68/100 = 68%, with 32% error. Its prespecified first-purchase subset gives 14/20 = 70% accuracy and 6/20 = 30% error. The latter is more directly relevant to an initial-purchase service, although it is based on only 20 customers from this selected cohort.

The remaining 80 repeat-purchase rows contain 54 correct predictions and 26 errors, reconciling to 68 correct overall. Do not substitute repeat-transaction performance for first-purchase performance. The 100 rows are observations from 20 held-out people, not 100 independently sampled new customers.

## Debrief · Do not turn a score gap into a causal effect

The all-row accuracy difference is 92% − 68% = 24 percentage points. But the fitted models, training customers and scored rows differ. That gap alone cannot identify the amount caused by overlap, establish statistical significance or predict the exact performance drop at deployment.

The overlap audit and stable response patterns explain why A fails to isolate unseen-customer performance. Removing customer codes alone would not remove dependence carried by other features. Conversely, do not accuse the questionnaire of containing future information: every supplied predictor genuinely existed at the decision time.

## Debrief · Keep the training pipeline inside the boundary

Carry forward customer-grouped evaluation, with the first-purchase outcome and population defined in advance. Keep feature selection, imputation, scaling and any tuning inside the training side, using customer-separated validation there. Reserve a final untouched customer holdout for the chosen procedure; do not repeatedly redesign the model against its answers.

A future evaluation should recruit an appropriate first-time cohort, including people who do not return, and preserve the real prediction-time information rules. Check subgroup coverage and uncertainty using the customer as the grouping unit. Do not calculate a confidence interval that treats all repeat rows as independent people.

## Debrief · A design choice is not launch approval

B addresses customer overlap but does not repair the cohort’s repeat-purchaser selection. First-visit performance for these 20 customers need not represent all new visitors. More appropriate customers and prospective first-purchase observations are needed before making a broad claim; adding more repeat transactions alone does not solve that problem.

For a different service predicting returning customers, their legitimate prior records could be useful and a different evaluation might be appropriate. The split must reproduce that service’s information boundary. Here the stated first-time use remains fixed, and neither 70% accuracy nor a cleaner split supplies a business case or launch threshold.

## Instructor note

Minutes 0–4: ask whether unseen rows imply unseen people. Minutes 4–8: draw the customer overlap under A and separation under B. Minutes 8–13: calculate 32% versus 30% error and reconcile repeat rows. Minutes 13–18: identify the remaining cohort-selection limit and explain why no launch verdict follows.

Require students to distinguish three issues: customer overlap, which purchase occasion is scored, and which customers entered the research file. Correcting the first does not automatically correct the others. Reward a clearly defined future test, not a claim that grouping always lowers accuracy or makes every random-row split invalid.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All retailer, customer, records and scores are fictional. Each of 100 adults has five distinct transactions. No future features, customer codes, target-derived variables or prior-purchase predictors enter fitting. A uses 400 training and 100 test rows: 60 test customers contribute one row, 20 contribute two, and 20 contribute none. All 100 customers have training rows. B uses 80 whole customers for training and 20 for scoring, with the same fixed procedure but a separately fitted model. Overall B gives 68/100 correct; its prespecified 20 first purchases give 14/20 correct; remaining 80 rows give 54 correct. Error rates are 32% and 30%. Different fitted models and test sets prevent a causal interpretation of the 24-point accuracy gap. Customer grouping is necessary for the stated unseen-customer question but does not solve selection of eventual repeat purchasers. No model, data collection or deployment is performed.

- [scikit-learn · Cross-validation: evaluating estimator performance · grouped data](https://scikit-learn.org/stable/modules/cross_validation.html). Official methodology explains why dependent observations require group separation when evaluating unseen groups. No library routine was run for the fictional scores.
- [Tidymodels rsample · Simple Training/Test Set Splitting](https://rsample.tidymodels.org/reference/initial_split.html). Package authors specify whole-group assignment to training or testing. This supports a single grouped holdout, not a claim that grouping ensures representative customers.
- [Chaibub Neto and colleagues · Learning Disease vs Participant Signatures · 2018 preprint](https://arxiv.org/html/1712.03120). Original methodological research investigates identity confounding and competing explanations for split-score differences. Its clinical examples and permutation-test results are not transferred to retail or asserted to have been run here.
- [Kaufman, Rosset and Perlich · Leakage in Data Mining: Formulation, Detection, and Avoidance · 2011](https://www.cs.umb.edu/~ding/history/470_670_fall_2011/papers/cs670_Tran_PreferredPaper_LeakingInDataMining.pdf). Original research defines legitimacy in relation to the intended inference problem and information boundary. Its competition examples are not evidence about this retailer.
- [Google · Datasets: Dividing the original dataset](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets). Original educational guidance separates model-development validation from final testing and emphasises representative evaluation. Removing duplicate rows alone does not solve the distinct repeated-customer problem here.
