# Assigned to the pilot. Actually using it?

<!-- legacy-case-id: 344 -->

IS-29 · Hong Kong · 15–20 minutes · Intention-to-treat analysis · Optional uptake · Selection bias

![An analyst compares a pilot invitation roster with aggregate training results, without displaying individual employee details.](../assigned-pilot-actual-use-scene.jpg)

## An offer and its uptake answer different questions

Randomised-evaluation guidance distinguishes the effect of offering a programme from differences between people who choose to participate and those who do not. Keeping assignment, use and outcome records separate matters when access is optional. The company, scores and participation pattern below are fictional, not an evaluation of a real training product.

## Opening decision

A Hong Kong business-services company tests an optional spreadsheet-practice tool with 80 consenting staff. A documented lottery assigns 40 to receive access for four weeks and 40 to a comparison group without access. Staff may decline the tool without penalty. Everyone retains usual training resources and completes the same pre-specified, independently administered end-of-pilot skills assessment, scored from 0 to 100. No outcome is missing. There are no shared accounts, access by controls or spillovers between staff in this simplified case.

The manager’s question is whether offering this optional tool improves average assessment performance for this eligible staff group under the pilot’s delivery conditions. It is not a question about forcing everyone to use it or identifying employees for promotion. Individual results and participation will not be used for personnel decisions; the report uses aggregates. The offer includes access and a standard invitation, so its effect need not operate only through logged tool use.

Before opening the score report, the analyst must choose the headline comparison. A compares all 40 assigned access with all 40 assigned no access, regardless of use. B compares active users with everyone who did not use the tool, pooling offered nonusers and controls. “Active” was defined before analysis as completing at least one practice module. The manager is attracted to B because it appears to focus on people who actually experienced the product. Both reports can show uptake descriptively, but only one should headline the stated offer-policy question.

## Evidence

A: all 40 randomly offered access versus all 40 controls. B: active users versus all nonusers, including offered nonusers and controls. Complete common assessment; no crossover or spillovers. Question: effect of this optional offer for eligible pilot staff.

**Student question:** Would you headline A or B? Explain which comparison matches the manager’s policy question and what could go wrong when groups are rebuilt around actual use.

## Round two

The verified assignment log matches the original lottery. Of the 40 offered access, 20 were active users with a mean score of 80, and 20 were nonusers with a mean of 60. The 40 controls had a mean of 66. These are exact fictional means on the same 100-point assessment, not percentage improvements. Thus the offered group’s mean is 70, while the combined 60 nonusers have a mean of 64.

A short baseline questionnaire, completed before the lottery, recorded whether staff already planned extra spreadsheet practice. Each assignment group happened to contain 20 who planned it and 20 who did not; the lottery was not altered to achieve this realised balance. All 20 active users came from the offered staff who had planned extra practice. None of the other 20 offered staff used the tool. This makes uptake visibly selected on prior motivation. It does not establish that motivation explains the entire score gap or that the tool has no effect.

A produces a four-point difference: 70 minus 66. B produces a sixteen-point difference: 80 minus 64. The summary does not include within-group score variation, confidence intervals or costs. No statistical-significance, precision or value-for-money conclusion can be drawn from these means alone. The invitation itself may encourage other practice even among nonusers, so an additional assumption that assignment affects scores only through tool use has not been established.

**Student question:** Which result should lead the report now, and how should it be described? Explain what the other comparison can show and what additional evidence is needed before a wider rollout.

## Answer the first decision: preserve the assignment

Use A for the stated offer-policy question. It retains people in the groups created by the lottery, including offered staff who never used the tool. This is an intention-to-treat analysis. B sorts staff by a choice made after assignment, so it can compare people with different prior characteristics as well as different tool experience. It is a descriptive engagement comparison, not automatically an effect of use.

## Answer the revealed decision: four points, with limits

Lead with an estimated four-point effect of being offered this optional package on the pilot assessment: 70 versus 66. The documented lottery, complete common outcomes and stipulated absence of spillovers support this causal interpretation of assignment, subject to sampling uncertainty. Do not say the effect is exactly four points in the population, statistically significant, or a sixteen-point gain from tool use. Report the 50% uptake alongside the offer estimate.

## Audit the arithmetic and selected comparison

Offered mean: (20 × 80 + 20 × 60) / 40 = 70. Combined nonuser mean: (20 × 60 + 40 × 66) / 60 = 64. Therefore A is 70 − 66 = 4 points, and B is 80 − 64 = 16 points. The denominator for B includes 60 people, not just the 40 controls. Users were already more motivated on the observed baseline measure. That supports a selection warning but does not quantify how much of sixteen points is selection.

## Do not turn uptake into a shortcut

Dividing four by 50% uptake would produce eight points arithmetically, but it is not an identified effect of use under the stated facts. Such an instrumental-variable interpretation needs additional assumptions, including no effect of the offer except through use, which is not established here. Nor is it an effect of compulsory use for every employee. Keep offer, engagement and mechanism questions distinct.

## Instructor note

Request score-level variation and an analysis consistent with the lottery to quantify uncertainty; verify the outcome was pre-specified and records remain complete. For rollout, also examine delivery costs, practical importance, durability and whether later staff and uptake resemble the pilot. No personnel ranking follows from an aggregate evaluation. The baseline balance is a stipulated realisation, not a promise that randomisation always balances every characteristic. Institutional sources provide methodology, not evidence that this invented product works.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All company, participant, assignment, uptake, motivation and assessment facts are invented. Eighty consenting staff: 40 offered and 40 controls. Twenty active users and 20 offered nonusers yield 50% offered uptake. Offered total score is 2,800; control total 2,640; combined nonuser total 3,840 across 60 people, mean 64. ITT difference is 4 score points; user/nonuser difference is 16 score points, not 16 percent. Within-group variation is intentionally absent, so uncertainty cannot be calculated from the exhibit. Random assignment is verified, no outcome missing, no crossover or interference, common assessment. Baseline motivation is measured before assignment, equal 20/20 composition realised in both arms; uptake selects all 20 motivated offered staff. This does not isolate a motivation effect or rule out other selection. The offer may affect practice outside the tool, so the exclusion restriction needed for a use-effect estimate is unverified. Institutional methodological sources overlap and are not five product evaluations. No individual employment decisions are involved.

- [J-PAL: Data Analysis](https://www.povertyactionlab.org/resource/data-analysis). Primary institutional guidance defines intention-to-treat and explains additional assumptions for instrumental-variable estimates of participation effects.
- [Innovations for Poverty Action: Randomization](https://data.poverty-action.org/research-design/randomization.html). Primary research-practice guidance distinguishes assignment and participation, one-sided noncompliance and spillovers.
- [World Bank DIME: Research Design for Impact Evaluation](https://worldbank.github.io/dime-data-handbook/design.html). Primary institutional handbook explains identification, randomisation noise, uptake and the distinction between credible design and precision.
- [J-PAL: Using Administrative Data for Randomized Evaluations](https://www.povertyactionlab.org/resource/using-administrative-data-randomized-evaluations). Primary guidance warns that differential outcome coverage or linking can undermine assignment-based comparisons; informs the complete-common-outcome safeguard.
- [J-PAL: Sampling](https://www.povertyactionlab.org/resource/sampling). Primary guidance distinguishes sampling from assignment and notes that comparability is in expectation, with sampling variation and external-validity limits.
