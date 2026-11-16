# A high average accuracy. An uneven burden?

<!-- legacy-case-id: 345 -->

GVR-29 · Fictional leisure club · 15–20 minutes · Classification fairness · Error denominators · Human alternatives

![A hobby-club coordinator compares two blank eligibility cards at a craft room.](../accurate-for-whom-scene.jpg)

## Fairness is not one accuracy score

NIST’s AI Risk Management Framework treats trustworthy use as contextual: measurement can expose trade-offs without deciding whose interests should prevail. Hardt, Price and Srebro formalise equalised odds through conditional error rates; Chouldechova distinguishes those rates from the reliability of positive classifications.

The Fairness and Machine Learning text and Fairlearn documentation also warn that metric choice depends on meaningful labels and the surrounding decision. The invented club below isolates a numerical tension. It is neither an audit of a real product nor a model for employment, lending, education, housing, healthcare or other consequential decisions.

## Opening decision

**Fictional classroom situation.** A leisure club offers a free, optional, non-safety-critical paper-craft hobby session. Eligibility means having completed its introductory session, not possessing any personal attribute. Ordinary membership, other activities and all baseline rights remain unchanged. There is room for every eligible applicant, so one mistaken acceptance does not displace another person.

Two screening rules, E and P, have been tested offline on the same two invented audit cohorts, A and B, each containing one hundred applications. The cohorts are anonymous administrative groupings, not claims about any real population. Completed attendance records supply the correct labels for this exercise. Both rules cost the same to operate. A positive means initially accepted; a negative means initially rejected.

An eligible person wrongly rejected must seek a free, accessible human review, creating effort and possible frustration. An ineligible person wrongly accepted receives an unnecessary session at club expense, but no safety risk or loss of another person’s place. Both rules give clear reasons, timely review before the session, a named accountable coordinator and identical privacy safeguards. These safeguards do not erase the initial burden.

Each table row lists correctly accepted, wrongly rejected, wrongly accepted and correctly rejected applicants, in that order. These are exact classroom counts, not estimated population rates. The coordinator may choose a screen provisionally or request a non-automated design. For now, compare total mistakes and where they fall; the board has not yet stated what it means by a fair distribution.

## Evidence

| Rule / cohort | Correct accept | Wrong reject | Wrong accept | Correct reject |
| --- | --- | --- | --- | --- |
| E / A | 72 | 8 | 2 | 18 |
| E / B | 18 | 2 | 8 | 72 |
| P / A | 72 | 8 | 8 | 12 |
| P / B | 18 | 2 | 2 | 78 |

**Student question:** Which screen would you provisionally choose, or would you withhold approval? Compare overall accuracy and the two kinds of mistake by cohort, stating which burden you are trying to reduce.

## Round two

Both rules face the same eligibility base rates: A has eighty eligible and twenty ineligible applicants; B has twenty eligible and eighty ineligible. The board now asks for **equalised odds**: equal false-rejection rates among eligible applicants and equal false-acceptance rates among ineligible applicants. It also asks for **predictive parity**: equal shares actually eligible among accepted applicants. These use different denominators.

Use false-rejection rate = wrong rejects / all eligible; false-acceptance rate = wrong accepts / all ineligible; positive predictive value = correct accepts / all accepted. Apply each definition separately to A and B. A percentage of all applicants is not either conditional error rate.

There is a funded alternative: staff can check every applicant’s existing attendance record directly, taking two extra staff-days before the session and postponing a nonessential catalogue tidy-up. No applicant must submit additional information or wait beyond the session deadline. For this exercise those records can be resolved correctly; this is an explicit assumption, not a general claim that human judgment is error-free. The same reasons, correction route, privacy and access protections apply.

The board must choose the present arrangement and explain its priorities. It may investigate better data or designs later, but cannot claim an unavailable perfect screen today. All figures remain hypothetical, and group-level equality alone would not establish that the eligibility rule itself is fair.

**Student question:** Calculate each rule’s false-rejection rate, false-acceptance rate and positive predictive value for both cohorts. Which criteria does each meet here, and would you now use E, P or direct record checking?

## Answer the first decision

Neither screen wins on overall accuracy. E correctly classifies ninety in each cohort: **180 / 200 = 90%**. P correctly classifies eighty-four in A and ninety-six in B: also 180 / 200. Each produces ten wrong rejections and ten wrong acceptances. A single average conceals the distribution.

Both wrongly reject eight eligible people in A and two in B. E wrongly accepts two ineligible people in A and eight in B; P reverses those numbers. With no stated fairness priority, withhold final approval rather than call one objectively fair. E is a defensible provisional choice if equal conditional error burdens matter most, but that rationale needs the base-rate calculation, not its name.

## Compute the different denominators

For E, false rejections are 8 / 80 = 10% in A and 2 / 20 = 10% in B. False acceptances are 2 / 20 = 10% in A and 8 / 80 = 10% in B. E therefore meets equalised odds in this table. Its positive predictive values differ: 72 / 74 ≈ 97.3% for A and 18 / 26 ≈ 69.2% for B.

For P, false rejections remain 10% in both cohorts. False acceptances are 8 / 20 = 40% in A and 2 / 80 = 2.5% in B, so P does not meet equalised odds. Its positive predictive values match: 72 / 80 = 90% and 18 / 20 = 90%. Thus P meets predictive parity here. Matching reliability among accepted applicants does not equalise exposure to mistaken acceptance.

## Choose an arrangement, not a winning statistic

Prefer **direct record checking** in this small fictional setting: its funded two staff-days avoid these initial classification mistakes without missing the session deadline or creating new applicant paperwork. Name the displaced catalogue work and retain quality checks; do not imply human processes are inherently unbiased.

If staff capacity changes, either screen needs an explicit justification based on the significance of the mistakes, the reliability and fairness of the target label, and affected members’ views. Free review is necessary but can still impose effort. Monitor who needs review, how quickly corrections occur and whether access barriers persist, not only a model score.

## A limited mathematical lesson

The exhibited E and P rules cannot each satisfy both requested criteria with these counts. The different eligibility rates matter because the share eligible among accepted people depends on the pool being screened as well as its error rates. This example does not prove that all fairness goals are always incompatible. Perfect classification, other special cases, different objectives or changes to the decision process require separate analysis.

Nor does a group comparison establish individual fairness, lawful treatment or why base rates differ. Never interpret cohort labels as inherent ability. This is an offline classroom calculation, not permission to deploy a real eligibility system or collect sensitive attributes.

## Instructor note

Require denominators before percentages. Distinguish equal false-negative rates from equal numbers of rejected people, and positive predictive value from overall accuracy. E has equal accuracy here because both conditional error rates are 10%; equalised odds does not generally guarantee equal accuracy when base rates and error rates differ.

Compared with GVR-13, the focus is not designing an appeal after a flag; compared with IS-14, it is not simply estimating useful alerts. The decision is which distribution of burdens to accept, including whether to avoid automated screening. Ask what would change if record checking imposed an actual deadline failure, but do not silently add that constraint.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All organisations, cohorts, eligibility records and counts are invented. This low-stakes voluntary hobby exercise involves no essential service or real-person high-impact decision. Rules E and P each make twenty errors among two hundred applications. The board must distinguish conditional error rates, predictive values and aggregate accuracy, then consider a funded non-automated alternative. Direct checking is correct only under the stated classroom record assumption. Privacy, review, access and baseline rights are constraints, not rewards traded for accuracy.

- [NIST · AI RMF 1.0, AI risks and trustworthiness](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/). Sections on contextual trade-offs and human judgment support transparent value choices rather than a single-score endorsement.
- [Barocas, Hardt and Narayanan · Fairness and Machine Learning, Classification](https://fairmlbook.org/classification.html). Authors’ definitions of separation and sufficiency and discussion of statistical criteria clarify different conditional denominators.
- [Fairlearn · Common fairness metrics](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html). Official project documentation explains equalised odds, target validity and limitations of treating a metric as complete fairness.
- [Hardt, Price and Srebro · Equality of Opportunity in Supervised Learning · 2016](https://arxiv.org/html/1610.02413). Original paper defines equalised odds and explains limits of tests based only on observed joint statistics. No credit-scoring result is transplanted.
- [Chouldechova · Fair prediction with disparate impact · 2017](https://arxiv.org/pdf/1703.00056). Original paper distinguishes predictive parity from error-rate balance and examines prevalence-dependent tensions. Its criminal-justice findings are not applied to this hobby setting.
