# Challenge the forecast. Who may override it?

<!-- legacy-case-id: 176 -->

IS-15 · Hong Kong · 10–15 minutes · Information systems · Human oversight · Override authority

![Two stationery-shop colleagues discuss a tablet beside notebook stock and a blank clipboard.](../challenge-and-authorise-scene.jpg)

## A Hong Kong governance context

On 15 October 2026, the HKMA announced its ART framework for responsible AI adoption in banking, including accountability and effective intervention mechanisms. This is sector-specific context, not a retail operating rule.

The stationery chain and its forecast workflow below are fictional and do not involve a bank, personal-data decision or automated customer entitlement.

## Opening decision

A fictional Hong Kong stationery chain uses a forecasting model to suggest how many already-owned display notebooks to send from its warehouse to each branch for the next day. The suggestion cannot release stock by itself: an authorised planner must approve the transfer. There is enough stock and transport for any permitted plan, with no effect on existing customer commitments.

The chain is choosing one exception workflow for a four-week pilot. A trains local branch planners to authorise a temporary quantity within documented limits after checking evidence; it logs the decision for next-day central review. B sends the same evidence to a funded central reviewer who must decide before transfer release. Both have access to the relevant records, trained cover and the power to reject a weak challenge.

A aims to use local context quickly; B aims for consistent reasoning across branches. Both require correction of a confirmed bad input, a recorded reason, a named decision-maker and escalation outside the allowed limits. Neither permits knowingly relying on invalid inputs or unlogged discretion. The pilot packages cost the same and fit paid staffing; this is not a choice between proper control and free extra work.

## Evidence

| Pilot workflow | A: bounded local authority | B: central approval |
|---|---|---|
| Ordinary exception review | About 10 minutes locally | Within 45 minutes centrally |
| Decision authority | Trained local planner within limits | Trained central reviewer |
| Required record | Evidence, quantity, reason, owner, expiry | Same |
| Oversight | Next-day central review | Review before release |

**Student question:** Which exception workflow would you pilot, A or B? Specify what makes a challenge evidence-based and what must remain outside an individual planner’s authority.

## Round two

A branch’s model suggests 260 notebooks for tomorrow. A verified organiser notice says the nearby craft fair has been cancelled, but the model’s event input still says it will run. The data owner confirms the error. Under either workflow, the affected recommendation is marked invalid, blocked from release and the source record is corrected. A validated rerun will be ready in two hours; the stock-transfer cutoff is in 60 minutes.

There is a preapproved temporary manual-planning method for this situation. The recent comparable non-event-day baseline is 200 units, and a documented permitted interval is 180–220. An authorised planner may choose within that interval using current evidence and record the reason; an out-of-range choice requires the duty manager. These are fictional planning limits, not a confidence interval or a forecast of actual sales. The cancelled event’s contribution cannot be isolated by simply subtracting a known number.

The local planner can check the branch’s current shelf stock and enquiry log within about ten minutes. The central reviewer can examine those same records and compare other branches’ activity within 45 minutes, with staffed backup supporting that response window. A chain-wide promotion is also running; neither cancellation alone nor the baseline proves tomorrow’s quantity. Under A, central comparative information is accessible on request within its funded workflow; under B, local staff can clarify their records. Both routes can complete before the 60-minute cutoff; speed is not a forced reason to bypass review.

Whichever route is chosen, the manual quantity applies only to this transfer and expires after release. It does not overwrite the forecast, retrain the model or authorise future exceptions. When the rerun arrives, the owner compares it with the manual decision and later outcomes, checks the data fix and investigates repeated exceptions. If adequate evidence or authorised review is unavailable, the duty manager uses the documented hold-and-notify fallback; no invalid recommendation is released automatically. No profit or forecast-accuracy improvement is established.

**Student question:** Keep or change your pilot choice? Describe who verifies, authorises, logs and later reviews this temporary adjustment, including its expiry and the fallback if review cannot be completed.

## Correction is not optional

The known event error must be fixed under A and B. Leaving the 260 recommendation active because it came from a model is not a third defensible route. A confident-looking output is not evidence that its inputs remain correct. Record the invalidation and corrected source separately from the subsequent stock decision.

## An override is a bounded business action

The permitted 180–220 interval surrounds the 200 baseline by 20 units each way, or 10%. It is an authorised decision range, not statistical uncertainty. The case does not supply a uniquely correct quantity. Ask for a supported temporary plan, not an invented calculation claiming the fair accounts for exactly 60 notebooks.

Local evidence may justify a prompt adjustment; a central view may detect context that one site misses. Both routes have time and access. A’s later audit cannot prevent every weak local decision; B’s prior review uses central capacity and can add delay. Compare the ability to challenge and the cost of coordination, not merely whether a human appears in the process.

## Keep action, model and learning separate

A useful record contains the invalid input, supporting evidence, chosen quantity, justification, authoriser, time, expiry and escalation status. The source correction belongs to the data owner; transfer approval belongs to the authorised planner. Temporary stock action must not silently become a permanent model correction.

Review corrected forecasts, decisions and subsequent demand evidence without assuming a better outcome was caused by the override. Units sold can be constrained by stock, so sales alone may not identify unconstrained demand. Repeated exceptions may indicate a data-feed or workflow problem. Escalate those patterns rather than normalising a permanent workaround.

## Instructor note

Require students to correct and block the invalid recommendation first, then compare two legitimate authority designs. A valid answer may choose either workflow, with evidence, explicit limits, expiry and fallback. Do not reward an unauthorised bypass because a deadline exists: both supplied routes fit it.

IS-06 concerns information available when testing forecasts. GVR-13 concerns an affected customer’s opportunity to challenge a decision. Here the output is an internal, expiring stock-allocation exception and its relationship to data correction and model monitoring. It is neither a customer appeal nor a guarantee that human judgment is more accurate.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All branch, model, times, quantities, staffing and limits are original fiction. The invalid 260 suggestion is blocked under both routes; no workflow may release it knowingly. The 60-minute cutoff precedes the 120-minute validated rerun. Local review about 10 minutes and centrally staffed 45-minute response both fit; response staffing is a classroom capacity assumption, not a service guarantee for real systems. The 180–220 interval is a policy bound around 200, plus/minus 10%, not a model confidence band or numerical demand estimate. Out-of-range decisions require duty-manager authority. No amount attributable to the cancelled event is supplied. The baseline and promotion remain relevant but do not prove demand. Both routes share access and paid capacity; A can request comparative information, B can request local clarification. One-transfer approval expires after release and does not modify the model or authorise future transfers. Safe stock capacity, existing commitments and lawful operations are preserved. No personal information or rights decision occurs. HKMA banking context is not retail regulation; ICO UK guidance is conceptual here and its legal provisions are not applied to Hong Kong. NIST Govern 3.2 and Manage 4.1 are two sections of one playbook, not independent empirical studies. Microsoft author-team explanation of its design guidelines was read, not the full associated CHI paper. Five actual relevant source bodies were read; no source example or measured effect copied. PCPD press page returned no readable body and was excluded.

- [HKMA · ART framework announcement · 15 October 2026](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261015-3/). Read announcement of accountability, resilience and intervention initiatives. Banking context, not a retailer compliance standard.
- [NIST AI RMF Playbook · Govern 3.2](https://airc.nist.gov/airmf-resources/playbook/govern/). Read role differentiation, proficiency and oversight procedures. Voluntary guidance, not certification of this workflow.
- [NIST AI RMF Playbook · Manage 4.1](https://airc.nist.gov/airmf-resources/playbook/manage/). Read post-deployment monitoring, override and feedback procedures. Same playbook as Govern, not separate outcome evidence.
- [Microsoft Research · Guidelines for human-AI interaction design](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/). Read author-team account and correction, dismissal, explanation and cautious-update guidelines. Design guidance, not proof of higher accuracy.
- [ICO · Human input and automation-bias discussion](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-do-we-ensure-individual-rights-in-our-ai-systems). Read oversight, additional context and intervention-design sections. Conceptual background only; UK legal rights are not imported into this internal stock example.
