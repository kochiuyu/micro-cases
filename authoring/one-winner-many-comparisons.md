# One winning result. How many chances to win?

<!-- legacy-case-id: 260 -->

IS-22 · Hong Kong · fictional online shop · 15–20 minutes · Multiple comparisons · Exploration and confirmation · Selection bias

![Two fictional colleagues discuss landing-page design samples in a modest stationery business office.](../one-winner-many-comparisons-scene.jpg)

## A promising result needs its selection history

Online experimentation research distinguishes choosing a promising candidate from checking whether it really improves an outcome. Testing several versions creates both multiple-comparison risk and optimistic selection of an apparent winner. The shop and every number below are original fiction, not findings about a real platform.

## Opening decision

**Fictional classroom situation.** You manage a Hong Kong online stationery shop. An analyst has compared harmless landing-page layouts and recommends version 13. It changes the arrangement of product photographs, not prices, claims, checkout, accessibility or customer rights. Technical, privacy and usability checks have passed. Participation and limited measurement are appropriately authorised; no sensitive personal information or employee evaluation is involved.

The briefing reports 135 product-detail-page visits among 1,000 people shown version 13, versus 100 among 1,000 shown the current page. Each person contributes one yes/no outcome: whether they opened a product-detail page during their assigned session. That is a browsing action, not a purchase or profit. A supplied ordinary two-sided comparison gives p = 0.0151. The analyst calls it the most promising result. The briefing does not explain the selection process.

A launches version 13 now for HK$2,000, with the old layout retained for a rapid reversal and funded monitoring. B spends HK$4,000 on a separate confirmation before deciding, delaying broad launch two weeks; any later launch still costs HK$2,000. Both complete paths fit the HK$6,000 budget. Current service continues normally while waiting. Management considers a one-percentage-point increase in this browsing rate worth investigating, but has not assigned it a monetary value. Waiting could postpone a real benefit; launching could commit effort to a chance winner. You may retain the current page without further spending.

## Evidence

| Measure | Current page | Version 13 |
| --- | --- | --- |
| People assigned | 1,000 | 1,000 |
| Opened a product-detail page | 100 | 135 |
| Observed rate | 10.0% | 13.5% |

Observed difference +3.5 percentage points; unadjusted two-sided p = 0.0151. Neither accounts for winner selection.

**Student question:** Would you launch the reported winning page now or pay for an independent confirmation first? What must you know about how the winner was selected before treating its result as evidence?

## Round two

The complete analysis log shows **twenty versions, each compared with the same current-page control**. All layouts and the single outcome definition were fixed before screening. There were 1,000 different people in each of the twenty version groups and 1,000 in the shared control: 21,000 people in total. Random assignment, complete recording and the assumptions of the supplied large-sample tests are valid for this exercise. No person saw more than one version, there was no interference, and no early stopping, subgroup search or second outcome. The twenty two-sided comparisons are the entire screening family.

Version 13 was selected only after every result was seen: it had both the largest positive observed difference and the lowest p-value. The other nineteen versions each recorded between 92 and 119 product-detail visits out of 1,000. None had a smaller p-value. The same 100 control visits were reused in every comparison, so the twenty test results are not independent. This is exploratory selection, not evidence of misconduct.

The confirmation package has reserved a fresh, non-overlapping cohort; none of its outcomes exists yet or has influenced selection. It can randomly assign 18,000 eligible people to the unchanged version 13 and 18,000 to the current page, over the stated two weeks, with a fixed end point and the same single outcome. The analyst has checked recruitment and the design against the stated one-point planning effect; no successful result is guaranteed. The package covers this work and independent analysis. It is not permission to try all twenty pages again and report whichever wins.

For this discussion, use a simple Bonferroni screen: divide an overall 0.05 false-positive allowance by the twenty planned comparisons. Compare the smallest unadjusted p-value with 0.0025. This conservative procedure does not require independent comparisons. It is a statistical screen, not an automatic business decision rule.

**Student question:** With twenty comparisons and an untouched validation cohort, would you launch now, confirm version 13 alone, or retain the current page? Specify what can honestly be claimed and how you would protect the confirmation from another search for a winner.

## Count opportunities, not only the reported winner

The initial difference is 13.5% − 10.0% = 3.5 percentage points, or a 35% relative increase from the control rate. Neither is a sales increase. The p-value describes incompatibility with equal browsing rates under the specified test model for that pair; it is not a 1.51% probability that the page has no effect.

Selecting a result after twenty comparisons gives more opportunities to find an apparently impressive difference. Reporting that selection changes its interpretation. The Bonferroni threshold is 0.05 ÷ 20 = 0.0025. The smallest p-value, 0.0151, does not pass; equivalently its adjusted p-value is about 0.302. This does not prove that all twenty layouts have zero effect.

## A shared control is not twenty independent chances

Every comparison contains the same control estimate. An unusually low observed control rate can make several layouts look favourable together. Do not apply an independence formula to calculate this experiment’s exact chance of any false positive.

For contrast only: twenty independent tests, each with an exact 5% false-positive rate when all nulls hold, would give 1 − 0.95 raised to the twentieth power, about 64.2%, for at least one false positive. That is not the probability for this shared-control design and not the probability version 13 is ineffective. Bonferroni bounds the family-wise error without needing independence; with approximate individual tests, its calibration is correspondingly approximate.

## The biggest observed gain need not be the biggest real gain

Exploration is useful for choosing a candidate. But selecting the most favourable noisy estimate tends to select favourable noise as well: selection-driven optimism, sometimes called the winner’s curse. It does not tell us exactly how much to subtract from 3.5 points or establish that this particular estimate exceeds the truth.

Do not mechanically divide the gain by twenty, or assume the adjusted p-value corrects the effect estimate. A fresh comparison of the fixed candidate can estimate its effect without choosing it again on those same observations. It need not identify the best of all twenty pages.

## Make confirmation a different job

Before collecting confirmation outcomes, freeze version 13, the current-page control, assignment, eligibility, the single outcome, sample size, end point, missing-data handling and analysis. Publish the complete confirmation result internally, including the estimated difference and its uncertainty, whether favourable or not. Preserve the exploratory results with their selection history.

For the planned single confirmation comparison, a prespecified two-sided 0.05 test can be used with an effect estimate and interval; it does not inherit twenty comparisons merely because selection used separate data. Do not add alternatives, peek until a small p-value appears, or change outcomes after viewing results. Do not naively pool the selected screening result with confirmation: combining stages requires a selection-aware method. The two-week schedule and sample size are case assumptions, not a universal recipe.

## Choose a business action without inventing certainty

B is a defensible preference if the manager values a cleaner estimate before broad deployment and accepts the extra HK$4,000 and delay. A can still be a reversible business experiment if its uncertainty is stated, monitoring and reversal remain funded, and nobody labels the uplift confirmed. Monitoring alone does not retrospectively validate the selected comparison. Retaining the old page is also defensible if the potential browsing benefit does not justify further effort.

Even a positive confirmation must be judged against practical size, uncertainty and customer experience. Statistical evidence of some increase does not prove an increase of at least one point, and browsing does not establish purchases or profit. No forecast of forgone revenue is supplied, so a unique financial optimum cannot be calculated.

## Instructor note

Suggested 15–20 minutes: three minutes for the initial choice, four for the selection reveal, four for the twenty-comparison screen, and five for a confirmation plan and final decision. Ask students to explain why a shared control makes the independence shortcut inappropriate before showing the optional 64.2% contrast.

Reward separation of candidate selection, confirmation and deployment. Do not require derivation of a test statistic. The supplied p-value comes from a pooled two-proportion normal test, without continuity correction; counts are ample and its assumptions are stipulated. Bonferroni is a transparent conservative example, not the only valid multiple-comparison method. Avoid treating a failure to cross a threshold as proof of no effect or a mandate never to launch. All companies, counts and costs are invented.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional company, counts, costs, timeline and experiment. Twenty fixed candidate-versus-shared-control comparisons are the complete screening family; one candidate is chosen after seeing results. All per-person test assumptions are stipulated, no interference or repeated peeking. The confirmation has no overlapping people or outcomes used in selection. Pooled two-proportion normal test without continuity correction gives z=2.4303944, p=0.0150824; Bonferroni threshold 0.0025 and adjusted p=0.301648. The independent-tests 64.2% example is not the exact shared-control error probability. Two weeks and 18,000 people per validation arm are hypothetical recruitment/design assumptions, not a guarantee of a conclusion. Browsing is not sales. Sources read 16 November 2026; none supplies these invented observations.

- [Wasserstein and Lazar, ASA statement on p-values (2016)](https://gattonweb.uky.edu/Faculty/Ziliak/ASA%20statement%20on%20p-values.pdf). Principles on full reporting, selection, practical importance and p-value interpretation; no case data.
- [NIST/SEMATECH, Bonferroni’s method](https://www.itl.nist.gov/div898/handbook/prc/section4/prc473.htm). General inequality and family-wide error protection; case uses its testing counterpart, not the page’s ANOVA example.
- [Deng, Li and Guo, Statistical inference in two-stage online controlled experiments (2014)](https://exp-platform.com/Documents/p609-deng.pdf). Original study of treatment selection, optimism and validation; advanced combined-stage corrections are not implemented here.
- [Dwork and colleagues, Generalization in adaptive data analysis and holdout reuse (2015)](https://proceedings.neurips.cc/paper_files/paper/2015/file/bad5f33780c42f2588878a9d07405083-Paper.pdf). Explains why repeated adaptive use can compromise a holdout; this case uses one independent confirmation, not the paper’s reusable-holdout algorithm.
- [NIST Dataplot, Binomial proportion test](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/binotest.htm). Pooled two-proportion normal-test formula used to recompute the supplied pairwise p-value; no actual shop data.
