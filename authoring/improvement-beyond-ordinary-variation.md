# The number improved. Beyond ordinary variation?

<!-- legacy-case-id: 248 -->

IS-21 · Hong Kong · fictional printing service · 12–15 minutes · Confidence intervals · Practical importance · Decision uncertainty

![Three fictional adult colleagues in a Hong Kong printing office discuss two plain request-form mockups beside a laptop and an open notebook.](../improvement-beyond-ordinary-variation-scene.jpg)

## An estimate is not a decision rule

A better sample average need not settle a business decision. Statistical guidance from the American Statistical Association distinguishes the size and practical importance of a result from whether it crosses a significance threshold. Confidence intervals add information about precision; they do not make the decision for the manager.

This is a fictional experiment and budget choice. No actual software, customer records or commercial results are being evaluated.

## Opening decision

**Fictional classroom case.** You manage a Hong Kong printing service. A redesigned online quotation-request form may reduce customer effort. It asks for the same information as the existing form and changes no prices, orders, access rights or payment decisions. Technical, privacy and accessibility checks have passed, and the old form remains available. This is not a safety-critical service.

A completed randomised comparison assigned 100 consenting eligible adult customers to each form. Each person made one request, saw only one version and did not influence another participant’s task. All 200 outcomes were recorded using the same start-to-submission timing rule; none was dropped from analysis. Both groups’ requests passed the same completeness check. For this teaching case, the allocation, measurement and conditions for the supplied independent-sample analysis are valid.

The analyst reports average completion times of 8.0 minutes with the old form and 7.5 with the new one. Positive **time saved = old mean − new mean**. Before examining results, the manager defined a mean saving of **0.75 minute per request** as worth pursuing for broad adoption. That is a business benchmark, not a statistical cutoff or a guarantee for each customer.

Choose a provisional next step, not permanent adoption. Both complete four-week packages fit the available budget and paid staffing. A costs HK$1,200 for a limited, reversible release with monitoring. B costs HK$2,400 for a fresh, larger comparable randomised study before considering broader release. Existing service continues under either option. The analyst will now supply precision and the operating limits.

## Evidence

| Measure | Old form | New form |
|---|---|---|
| Independent participants | 100 | 100 |
| Mean completion time | 8.0 minutes | 7.5 minutes |
| Sample standard deviation | 2.5 minutes | 2.5 minutes |

Positive saving = old mean − new mean = 0.5 minute (30 seconds). Preselected worthwhile mean saving = 0.75 minute (45 seconds). Standard deviation describes variation between participants, not uncertainty of the difference in means.

**Student question:** Would you provisionally fund the limited release or the larger comparison first? Explain what the observed half-minute saving establishes, and what uncertainty you need to see before approval.

## Round two

**The analyst’s 95% confidence interval for the mean saving is −0.20 to +1.20 minutes**, rounded from the prespecified two-sided Welch calculation. Negative means the new form is slower; positive means it is faster. Under the stated model, the range is compatible with a small average loss, no difference, or an improvement exceeding the 0.75-minute benchmark. It describes uncertainty about an average difference, not the spread of individual customers’ times.

| Option | Exposure and evidence | Incremental cost |
| --- | --- | --- |
| A: limited release | At most 1,000 eligible users receive the new form. Named support owner monitors service; no new randomised control group. | HK$1,200 |
| B: confirm first | Fresh study: 400 users per form. Of 1,000 eligible users available, the other 200 keep the old form. Analyse the new study separately. | HK$2,400 |

These user counts are the supplied four-week capacity plan, not measured future outcomes. B uses the same eligibility, timing rule and version separation, with a fixed analysis endpoint and a documented plan before collecting new outcomes. No interim result can trigger a declaration of success. Larger samples may improve precision; they do not guarantee a favourable or decisive result.

Both options have a tested return to the old form, no record loss and funded help. A named owner must immediately pause new allocation if a confirmed defect blocks a valid request, while affected users receive the old-form route. Monitor complaints, completion failures and request completeness, not only speed. Daily monitoring cannot detect every problem before exposure, undo time already spent or establish a causal saving without a comparable control.

Neither option may claim confirmed improvement, proven equivalence or demonstrated attainment of the 0.75-minute benchmark from the existing result. A expires after four weeks unless reviewed; B delays broader-release consideration by four weeks. The extra HK$1,200 for B buys evidence, not certainty. Any customer time benefit postponed by waiting is uncertain, not a booked cash loss.

**Student question:** After seeing the interval and operating limits, which option would you authorise for four weeks? State the uncertainty you accept, one pause condition, and a truthful sentence about the evidence.

## Debrief: read the range, not just the average

The point estimate is a **30-second mean saving**. The rounded interval extends from the new form being **12 seconds slower** on average to being **72 seconds faster**. It includes zero and the preselected 45-second practical benchmark.

The data do not yet distinguish the mean effect from zero at the corresponding two-sided 5% test level. That is not evidence that the effect is exactly zero, and the interval is not narrow enough to rule out a useful benefit. Equally, a positive point estimate does not establish improvement or that the practical benchmark has been reached.

## What 95% does and does not mean

A 95% interval method would cover the fixed underlying mean difference in about 95% of repeated comparable studies when its assumptions hold. It does not give a 95% probability that this particular fixed effect lies inside these realised endpoints. Nor does it say that 95% of customers benefit or that outcomes outside the interval are impossible.

The interval addresses sampling uncertainty under the stated design. It cannot repair bad measurement or missing outcomes. Those problems are excluded in this case to focus on precision. Future users, devices or workflows outside the eligible setting require separate evidence.

## Choose an action without overstating evidence

**A is defensible** if the manager accepts uncertain benefit and the possibility of a small average slowdown for a reversible, capped release. The interval is not a worst-case bound; larger slowdowns remain possible. Record the four-week expiry, pause authority and service checks. Do not turn ordinary rollout monitoring into a claim that the benefit has been experimentally confirmed.

**B is defensible** if the manager values a more precise comparison before greater exposure enough to pay HK$1,200 more and wait. Preserve the analysis plan and report the fresh results even if they remain inconclusive. Do not promise that a larger study will “prove it works”.

The given costs and uncertainty do not establish a uniquely optimal option: no money value for customer effort or probability distribution over effects is supplied. The decision needs an explicit tolerance for uncertainty, not a fabricated expected-profit calculation.

## Waiting and acting both have uncertain consequences

At the planned counts, A could give the new form to 1,000 users, versus 400 under B: a difference of 600 users. If the estimated 0.5-minute average saving transferred unchanged, that difference would correspond to **600 × 0.5 = 300 customer-minutes** during the period.

This is conditional scenario arithmetic, not a guaranteed saving, wage reduction or confidence interval for a future total. If the effect were negative, the extra exposure would instead add customer effort. Costs of waiting and acting both depend on the uncertain effect.

A suitable report is: “The trial estimated a 0.5-minute mean saving; the 95% interval is −0.20 to +1.20 minutes. We have not established a useful improvement, and we are choosing a bounded next step.” Add the chosen option and why its cost and exposure are acceptable.

## Optional: reproduce the interval

**Optional calculation.** Standard error of the difference = square root of (2.5 squared ÷ 100 + 2.5 squared ÷ 100) = 0.3536 minute. The Welch degrees of freedom are 198 for these equal sample sizes and sample variances. The 95% critical t value is about 1.972.

Thus 0.5 ± 1.972 × 0.3536 gives approximately −0.197 to +1.197 minutes, displayed as −0.20 to +1.20. Calculations use unrounded intermediates. The interval is for old minus new, so do not reverse the benefit sign halfway through.

## Optional: a larger study can still leave a business question

If the fresh study achieves 400 participants per form and variability remains 2.5 minutes, its standard error would be about 0.1768 minute, half the original. Its realised variability and effect may differ; those are planning assumptions, not known future data.

For illustration only, retaining the 0.5-minute estimate and the same standard deviations would give a fresh 95% interval of about **0.15 to 0.85 minute**. That would exclude zero, yet still include effects below the 0.75-minute business benchmark. More precision and statistical significance do not automatically establish practical importance.

## Instructor note

Use 12–15 minutes: three for the role and first vote, three to interpret the interval, four for the bounded-release versus evidence decision, and two to five for an honest management sentence. The supplied interval is sufficient; arithmetic extensions are optional. Keep the debrief hidden until the second vote.

Ask students to locate zero and 0.75 within the interval. Challenge both “not significant means no effect” and “the average improved, so publish success”. Distinguish customer minutes from cash and a business benchmark from a p-value threshold. Pause rules protect service; repeated dashboard inspection is not a licence to stop at a favourable significance result.

IS-07 compares where to start a pilot; IS-10 examines interference and assignment units; IS-11 investigates nonresponse; IS-12 treats missing measurements. These are not the failure here: the sample design and outcomes are stipulated valid. OPS-10 uses a time-ordered process-warning rule, whereas this case estimates a difference between two groups. The new lesson is limited precision and practical decision-making under that uncertainty, not equivalence testing or a promise that larger samples remove every bias.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional printing service, valid randomised trial, costs, user-capacity plan, business benchmark and monitoring rules. 100 independent participants per arm, complete outcomes, means 8.0/7.5 minutes, sample SD 2.5 each. Benefit defined old−new=.5 minute. Welch SE=sqrt(6.25/100+6.25/100)=.3535533906; df 198; t.975=1.972017478; CI[-.197213466, 1.197213466], displayed[-.20, 1.20]. Worthwhile mean effect. 75 minute set before results. Four-week A costs 1200 and caps new-form exposure at 1000; B costs 2400 with fresh 400 per arm and 200 other users on old form, total 1000. Neither is permanent adoption. At planned counts exposure difference 600; 600×.5=300 customer-minutes only if effect transfers. No wage or profit conversion, no assigned effect probabilities. At fresh n 400 each with same SD and mean, SE=.1767766953; df 798; 95% CI[.152997743, .847002257], explicitly hypothetical. Five distinct primary/institutional bodies read; three NIST sections address different method questions, not three independent studies. ONS uncertainty guidance and NIST example output were also consulted but not needed as references. No raw source data, images or extended quotations reproduced. Actual population effects, future data and rare harms are unknown.

- [American Statistical Association · Statement release on significance and p-values · 7 March 2016](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf). Official six-principle summary: threshold crossings do not measure practical importance or alone settle business decisions. No claim that p-values are forbidden.
- [NIST/SEMATECH Handbook · Do two processes have the same mean?](https://www.itl.nist.gov/div898/handbook/prc/section3/prc31.htm). Independent-sample standard errors and Welch-Satterthwaite degrees of freedom. The case uses its own means, sample sizes and two-sided interval, not the source example.
- [NIST/SEMATECH Handbook · What are confidence intervals?](https://itl.nist.gov/div898/handbook/prc/section1/prc14.htm). Repeated-sampling coverage and interval interpretation. A realised frequentist interval is not a probability distribution for a fixed effect.
- [NIST/SEMATECH Handbook · Sample sizes required](https://itl.nist.gov/div898/handbook/prc/section2/prc222.htm). Sample-size planning requires precision or effect assumptions and variability. Used for the larger-study caveat, not as a guaranteed success calculation.
- [Microsoft Research · Patterns of Trustworthy Experimentation: During-Experiment Stage · 25 January 2021](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/). Guardrail monitoring and the danger of unadjusted repeated peeking. Practitioner guidance; fictional cap, costs and pause rule are not Microsoft specifications.
