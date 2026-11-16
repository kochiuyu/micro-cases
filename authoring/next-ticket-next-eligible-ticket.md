# One shared line. Who can serve the next ticket?

<!-- legacy-case-id: 268 -->

OPS-23 · Hong Kong · 15 minutes · Skill-based routing · Queue pooling · Head-of-line blocking

![Two service colleagues discuss a plain ticket holder at a small print-support counter.](../next-ticket-next-eligible-ticket-scene.jpg)

## Service-design context

Queueing research studies both shared capacity and the rules that match requests to employees. Operational routing systems can check skills as well as availability. Sharing a waiting list does not itself create a missing capability.

The following print-support desk and all times are fictional. This is a small dispatch exercise, not a statistical prediction or a claim that one queue design always wins.

## Opening decision

A Hong Kong print-support centre wants to replace two separate walk-up lines with one shared ticket list. Two employees, A and B, are available; no staffing or equipment increase is proposed. Both can handle routine document-layout support at the same speed. The supervisor has not yet checked whether every queued request is routine.

Six customers are present at minute zero in recorded ticket order 1–6. This order breaks their arrival tie. The table gives the complete service time for each request, including its normal handoff. Nobody else arrives during this isolated test, nobody leaves, and service is not interrupted or transferred once started. No urgent case, accessibility priority or protected appointment is part of this test; such obligations must remain protected in actual operations.

The proposed rule is **strict global order**: start tickets in numerical order. Once a ticket has started, another free employee may start the next ticket; earlier work need not finish first. If the oldest unstarted ticket cannot be assigned, later tickets cannot start either. When both employees are available for the same eligible ticket, assign A first.

The manager wants to reduce total waiting before service starts without sending work to an unqualified employee. Waiting time excludes service time. The same service quality, breaks and safe workload apply; these short task durations are invented, not employee targets. Before adopting the rule, the team can verify request requirements and qualifications.

## Evidence

| Ticket | Service minutes |
|---|---|
| 1 | 8 |
| 2 | 2 |
| 3 | 4 |
| 4 | 2 |
| 5 | 2 |
| 6 | 2 |

**Student question:** Would you pilot the shared list with strict global start order? What capability check must happen before you promise that the next free employee can serve the next ticket?

## Round two

The capability check finds ticket 3 needs a legacy brochure-format procedure that only A is trained and equipped to complete. B cannot perform it, and no rapid training, transfer or remote specialist is available in this test. Every other ticket is routine and can be served by either employee. Service times remain unchanged.

Compare strict global order with this feasible **oldest-eligible rule**: whenever an employee becomes free, assign the oldest waiting ticket that employee can competently handle. Skipped tickets keep their original position for a qualified employee; they are not moved to the back. Apply the same A-first tie-break when both employees are available. At minute zero A starts ticket 1 and B starts ticket 2 under either rule.

Explain the routing rule before a pilot: a later routine request may start first while an earlier request waits for a specialist. Do not promise global start order under the oldest-eligible rule. Staff qualifications and required service quality remain binding.

**Student question:** Which rule would you use for this test? Draw each employee’s service sequence, compare total waiting, and explain what ticket 3 should be told when later tickets start first.

## Strict order can block usable capacity

A serves ticket 1 from 0–8. B serves ticket 2 from 0–2, then waits: ticket 3 cannot start until A is free at minute 8, and the global-order rule blocks tickets 4–6.

At minute 8 A starts ticket 3 (8–12) and B starts ticket 4 (8–10). B then serves ticket 5 (10–12). At minute 12 both are free, so A takes ticket 6 (12–14). Starts in ticket order are 0, 0, 8, 8, 10 and 12. Since everyone arrived at zero, total waiting is 38 minutes and the mean is 38 ÷ 6 ≈ 6.33 minutes. Last completion is minute 14.

## Oldest eligible is not oldest overall

A still serves ticket 1 from 0–8, then ticket 3 from 8–12. B serves ticket 2 from 0–2, ticket 4 from 2–4, ticket 5 from 4–6 and ticket 6 from 6–8. Ticket 3 remains first in line for A; nobody takes its qualified slot.

Starts in ticket order are 0, 0, 8, 2, 4 and 6. Total waiting is 20 minutes and the mean is 20 ÷ 6 ≈ 3.33 minutes. Last completion is minute 12. Compared with strict order, 18 total waiting minutes are removed; ticket 3 still waits eight minutes. The improvement comes from allowing B to serve eligible work, not from making either employee faster.

## Explain the apparent queue jump

Tell ticket 3: “Your request needs our colleague with the legacy-format capability. You keep your place for that colleague. The other desk can handle routine requests while you wait.” In the fixed test, A becomes available at minute 8; actual service estimates need honest uncertainty rather than a guarantee copied from this trace.

The oldest-eligible rule serves the stated objective better in this test without extending ticket 3’s wait. It changes the meaning of order, so explain it rather than promise an absolute first-come-first-started service. A strict-order policy is feasible but deliberately accepts idle time and longer overall waits here. Neither arithmetic nor a ticket system overrides legitimate priority or access obligations.

## What the test does not establish

Only this finite trace has been calculated. In a continuing system, specialist availability, arrival mix and assignments of routine work to the specialist can change later waits. Track waits by request type, not only the overall mean, and watch whether specialised requests repeatedly wait too long.

No rule here adds a third employee, changes service times or lets B attempt work outside competence. Cross-training could be a separate future investment with cost and quality checks; it is not free capacity available today. Physical queue layout, a shared ticket list and the dispatch rule are distinct design decisions.

## Instructor note

Allow 3 minutes for the initial proposal, 5 to draw the two time lines and 5–7 to compare rules and customer explanations. Ask why B is idle from minute 2 to 8 under strict order: not laziness, but a dispatch rule combined with the skill constraint. Under oldest-eligible, ticket 3 keeps its place for A even though tickets 4–6 start earlier.

Waiting is start minus arrival, not completion minus arrival. All six arrive at zero; service totals 20 employee-minutes under either rule. No healthcare, emergency triage or eligibility decision is being simulated. This extends the earlier pooling case through capability-constrained assignment rather than repeating a pooled-versus-express-counter choice.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All centre facts, ticket times and qualifications are invented. Six arrivals at zero, tie order 1–6; service times [8,2,4,2,2,2]. A and B handle all routine work identically; only A handles ticket 3. Service is non-preemptive, no transfer, no new arrivals, abandonment or priority cases. At a simultaneous availability tie, A takes the oldest ticket first. Strict global start order permits the next ticket once the prior ticket has started, not only after completion. Strict starts [0,0,8,8,10,12], waits total 38, average 19/3, final completion 14. Oldest-eligible starts [0,0,8,2,4,6], waits total 20, average 10/3, final completion 12. All service durations sum to 20 employee-minutes in both policies. The 18-minute aggregate waiting reduction is a deterministic trace result, not a forecast, causal estimate or universal queueing theorem. Specialist ticket 3 waits eight minutes under both. Existing priority/access obligations and safe work are protected, not waived. Five substantive source bodies were read on 16 November 2026; links are optional background only. The actual OPS-07 already compares pooled and dedicated counters, so this case intentionally focuses on head-of-line blocking and qualification-aware dispatch.

- [Wallace and Whitt · A Staffing Algorithm for Call Centers with Skill-Based Routing · revised January 2005](https://www.columbia.edu/~ww2040/poolingMSOMrevR.pdf). Original manuscript defines which requests an agent can handle and non-interrupted service; limited-flexibility findings depend on stated assumptions and are not copied as a forecast.
- [Microsoft Learn · Skill matching in unified routing](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-skill-based-routing). Actual documentation distinguishes exact skill eligibility from assignment ordering. No system was configured; closest-match fallback is not permitted by this case.
- [MIT OpenCourseWare · Basic Queueing Theory notes](https://ocw.mit.edu/courses/15-763j-manufacturing-system-and-supply-chain-design-spring-2005/22f4805864deb06eee85acc1601463ba_queueing_note.pdf). Teaching notes distinguish queue waiting from time in the system and state stochastic-model assumptions. This case uses a finite deterministic trace, not those steady-state formulas.
- [Van Dijk and Van der Sluis · Pooling Is Not Always the Answer · 2005 technical note](https://pure.uva.nl/ws/files/3821611/95002_338fulltext.pdf). Original analysis discusses pooling and alternative overflow/priority rules under different service characteristics; supports caution against universal pooling claims. No numerical example reproduced.
- [Hindy Ling, Etgar and Bar-Gera · Server pooling models for separate and bounded queues · 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10907676/). Original paper distinguishes sharing servers from sharing waiting spaces and makes its stochastic assumptions explicit. Its port model and quantitative findings are not transplanted into this desk.
