# The same average error. The same business cost?

<!-- legacy-case-id: 188 -->

IS-16 · Hong Kong · 10–15 minutes · Forecast evaluation · Asymmetric loss · Decision costs

![Two print-shop colleagues compare plain planning folders beside printers and paper samples.](../same-error-different-loss-scene.jpg)

## Forecasting in a local digital context

On 23 October 2025, HKPC released its AI Readiness in Workplace Survey and described support for business applications including demand forecasting. The announcement is context, not a test of forecast accuracy or proof of savings. The print shop, models, observations and losses below are original fiction.

## Opening decision

A fictional Hong Kong print shop compares two equally priced models for next-day capacity planning. The same four held-out days were not used to fit or select either model. Both forecasts were fixed before each day using only information then available. Both use the same units: requested standard print jobs. Complete request logs include requests not fulfilled, so demand is not a sales count clipped by capacity.

For this classroom replay, reserving one capacity slot per forecast job is the fixed planning rule. All forecast quantities are feasible within the shop’s safe maximum of 120 jobs a day. A slot cannot be added or moved to another day once that day starts. Accepted contractual orders, staff breaks and safety checks are protected separately; these requests concern additional discretionary work. There is no staffing cut or unpaid extra work.

A manager sees that both forecasts miss by ten jobs on each day and suggests either model will do. Choose which model deserves preference for a further operational evaluation, not unrestricted deployment. Four days are deliberately a small teaching example, not evidence that their frequency or errors will repeat in future.

## Evidence

| Day | Demand | A forecast | B forecast |
|---|---:|---:|---:|
| 1 · Busy | 100 | 90 | 110 |
| 2 · Busy | 100 | 90 | 110 |
| 3 · Quiet | 60 | 70 | 50 |
| 4 · Quiet | 60 | 70 | 50 |

**Student question:** Would you treat models A and B as interchangeable for capacity planning? Calculate their mean absolute errors, then name the operational information needed before choosing one.

## Round two

Operations supplies a complete incremental loss schedule for this replay, measured against having reserved exactly the requested number of slots. An unused reserved slot costs HK$4 on either type of day, net of any recovery. A demand unit above reserved capacity loses HK$20 of net contribution on a busy day, but HK$2 on a quiet day because the discretionary job mix has a lower margin. These per-job losses already allow for avoided variable costs. Do not add lost revenue, wages or another shortage penalty.

Every shortage unit is lost that day, not backlogged or shifted to another day. There is no same-day extra slot, subcontracting or cross-day inventory. Losses are linear over the ten-unit errors shown. Model fees, other operating costs and the protected work are unchanged. The costs and fixed forecast-to-capacity rule are stipulated assumptions, not estimated causal effects.

Use the same four rows to compare the two models under this rule. For a sensitivity check, replace only the busy-day shortage loss of HK$20 with an unknown amount c; retain quiet-day shortage loss HK$2 and unused-slot loss HK$4. Neither model is tuned or combined after viewing these rows. A different allocation rule or hybrid requires a separately evaluated proposal.

**Student question:** Which model would you prefer under the supplied operating-loss assumptions? Calculate both four-day losses and the busy-day shortage cost at which your preference would change.

## One score hides the pattern

Each model has total absolute error 10 + 10 + 10 + 10 = 40 jobs, so mean absolute error is 40 ÷ 4 = 10 jobs. Both also have zero average signed error. Neither fact says their operating consequences are equal. A is short on both busy days and long on both quiet days; B has the reverse pattern.

## Count the consequence of each unit

A loses 20 busy-day jobs at HK$20 each and reserves 20 unused quiet-day slots at HK$4 each: HK$400 + HK$80 = HK$480. B reserves 20 unused busy-day slots at HK$4 each and loses 20 quiet-day jobs at HK$2 each: HK$80 + HK$40 = HK$120. B has HK$360 less replay loss under the stated rule.

## Locate the decision boundary

With busy-day shortage cost c, A’s loss is 20c + HK$80. B’s loss stays HK$120. They tie when 20c + 80 = 120, or c = HK$2 per lost job. B is preferred if c exceeds HK$2; A if it is below HK$2. This threshold changes only that cost, not forecasts, quantities or day mix.

## Cost-sensitive is not always higher

B is not larger on every day: it allocates more on the costly-shortage days and less on the lower-margin days. The lesson is not to inflate every forecast. It is to evaluate the forecast together with the action rule and the relevant loss. No optimal forecast or globally optimal capacity policy has been derived.

## Validate before relying

Prefer B for the next evaluation under these assumptions, while retaining human planning checks. Confirm the shortage margins and unused-slot recovery, then test on more genuinely future days spanning the intended operating conditions. Four observations and a supplied loss schedule do not establish statistical superiority, future savings or a causal business effect.

## Instructor note

First ask for the MAE tie, then ask where each model is short. Reveal costs only after that distinction is visible. Require the HK$480/HK$120 totals and HK$2 sensitivity threshold. This is continuous demand-error evaluation, not alert precision or a base-rate shift. Input timing and complete demand observation are stipulated sound, so students should not invent leakage or censored sales. All essential facts are supplied; no software or external reading is required.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All company, model, request, cost and capacity figures are fictional. Both fixed forecasts use the same held-out four days and pre-day information, with complete requested demand including unfulfilled requests. Fixed decision rule reserves forecast quantity; feasible maximum 120, no same-day addition, cross-day movement or hidden inventory. Protected contractual work and safe staffing are outside the comparison. A errors forecast minus demand are −10, −10, +10, +10; B +10, +10, −10, −10. MAE 10 and signed mean zero for both. Complete linear opportunity losses: busy underage 20, quiet underage 2, any overage 4, HK dollars per unit. A 20 × 20 + 20 × 4 = 480; B 20 × 4 + 20 × 2 = 120; difference 360. Sensitivity A 20c + 80 ties B 120 at c = 2. No added lost revenue or double-counted cost. No forecast combination, empirical frequency estimate, guaranteed future saving or optimal policy claim. Five actual source bodies read: HKPC context, one combined OTexts chapter, AWS metrics, scikit-learn MAE and pinball documentation. Two scikit-learn pages share publisher; they document different losses, not independent studies. No source dataset or code examples copied.

- [HKPC · AI Readiness in Workplace Survey · 23 October 2025](https://www.hkpc.org/en/about-us/media-centre/press-releases/2025/ai-readiness-in-workplace-survey-2025). Dated local digital-business context and assessment emphasis, not model accuracy evidence.
- [Hyndman and Athanasopoulos · Forecasting: Principles and Practice · Chapter 5](https://otexts.com/fpp3/toolbox.html). Read held-out accuracy and absolute-error definitions. Original case numbers; no benchmark data copied.
- [AWS · Evaluating predictor accuracy](https://docs.aws.amazon.com/forecast/latest/dg/metrics.html). Read differing penalties for under- and overprediction. No service recommendation or empirical savings claim.
- [scikit-learn · Mean absolute error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html). Read metric inputs, aggregation and examples. Definition support only; no code execution claimed.
- [scikit-learn · Mean pinball loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html). Read loss slope and asymmetric examples. Conceptual extension only; classroom calculation uses explicit currency losses, not a fitted quantile model.
