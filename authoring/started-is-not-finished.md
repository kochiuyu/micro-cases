# Keep every station busy. Finish orders sooner?

<!-- legacy-case-id: 184 -->

OPS-16 · Hong Kong · 10–15 minutes · Work-in-progress control · Little’s law · Measurement boundaries

![Two workshop colleagues discuss desk-organiser production beside parts and an assembled sample.](../started-is-not-finished-scene.jpg)

## A historical Hong Kong lean-production context

HKPC’s 2006/07 annual report described a lean-manufacturing programme for SMEs that combined training, assessment, pilot improvements and evaluation. This historical context illustrates examining workflow rather than equating activity with completed output.

The workshop, release policies, observations and stable-flow comparison below are original classroom data. No reported HKPC performance improvement is transferred to this workshop.

## Opening decision

A fictional Hong Kong workshop makes one standard desk-organiser kit. Approved orders and materials are ready. Every kit follows the same preparation, assembly and final quality-check route; batch sizes, staffing, equipment and required checks remain unchanged. The line can sustainably complete four acceptable kits per working day under the present conditions. The manager wants clearer progress and fewer half-finished kits without reducing delivery performance.

A releases every approved ready order to the floor immediately. B trials a maximum of 12 released but unfinished kits across the whole line. A new kit can enter B only when a completed, quality-approved kit leaves and frees a slot. An exception is not an extra unrecorded slot. Unreleased approved orders stay in a visible dated queue, retain their original acceptance time and delivery promise, and are released in the same agreed order. A blocked or defective kit remains counted until resolved; no kit is discarded to improve the metric.

The cap is a proposed operating control, not proof that 12 is optimal or sufficient. The supervisor will watch for starvation of the constraining operation, defects and due-date performance, and adjust through a documented review if needed. Paid staff remain available for required work and upkeep; idle time is not hidden as a staffing saving. Both policies are feasible and funded. No extra machine, overtime or subcontracting is available in this comparison.

## Evidence

| Release policy | Floor control | Customer-order record |
|---|---|---|
| A: release all ready work | No released-work cap | Acceptance time and promised date retained |
| B: controlled release | At most 12 unfinished released kits | Unreleased queue visible; acceptance time and promise retained |

Physical completion capability remains four good kits per working day.

**Student question:** Would you trial controlled release B or retain A while checking the flow? Explain what a release cap could improve, what it could put at risk, and which completion and waiting measures you would watch.

## Round two

First, the supervisor examines five recent days during which an old approved backlog was being released under A: eight kits entered the floor and four good kits left each day. No kits were scrapped, returned to the unreleased queue or otherwise removed. Released unfinished work therefore increased by four kits per day, or 20 across those five days. This growing-queue period is not a steady-state sample; dividing one closing inventory count by output would not establish its average lead time.

Next, use a separate supplied stable-flow comparison for two settled observation periods with matched order type, staffing, checks and four accepted orders and four good completions per working day on average. No losses, cancellations, hidden work or continuing backlog growth occur. Under A, average released work is 24 kits and average unreleased accepted orders are zero. Under B, average released work is 12 kits and average unreleased accepted orders are 12. These are time averages, not one afternoon’s count. The 12-kit cap kept the constraining operation supplied in this particular B period; that does not establish the smallest safe cap.

Define floor flow time from release to final good completion, and customer lead time from order acceptance to that same completion. For these stable periods, average number within a defined boundary equals average completion rate multiplied by average time inside it. Use the same boundary, units and period for all three quantities. The entire accepted-order boundary includes both the unreleased queue and the released floor work. There is no later shipping delay in this exercise.

The manager is considering keeping B and advertising “orders now finish in three days instead of six”. No individual-order guarantee or improved due-date result is supplied. The release rule may make floor work easier to control, but waiting before release remains real waiting for a customer.

**Student question:** Would you retain B on this evidence, and would you approve the proposed three-day customer claim? Calculate average floor time and acceptance-to-completion time for both settled periods, then specify what must be monitored before any delivery promise changes.

## More starts did not increase finishes

Eight starts minus four completions added four unfinished kits daily, hence 20 over five days. That period cannot be treated as settled simply because output stayed at four. A launch metric or busy preparation station can rise while final throughput remains unchanged.

## Draw the boundary before calculating

In the stable comparison, floor averages give A: 24 kits ÷ 4 kits per day = 6 working days; B: 12 ÷ 4 = 3 working days. The difference concerns time after release. B also has 12 accepted orders waiting outside the floor boundary, equivalent to 3 working days on average. For all accepted work, A has 24 + 0 = 24 orders and B has 12 + 12 = 24. Both therefore have 24 ÷ 4 = 6 working days from acceptance to completion.

## Do not turn a neater floor into a misleading promise

Reject the proposed three-day customer claim. The observed floor-time reduction is real within its boundary, but the supplied customer lead-time average did not improve. Neither average guarantees any individual order’s completion date. Keeping B may be justified for visible release discipline and lower floor WIP, not a measured gain in throughput, total customer waiting, profit or on-time delivery.

## A control rule is not additional capacity

Retain the visible unreleased queue, original timestamps and due-date priorities. Monitor good completions, floor and pre-release queues, total lead time, late orders, starvation and defects together. Do not keep cutting the cap on the assumption output will remain fixed: too little available work can starve the constraining step. Little’s law relates consistent averages; it does not implement a process improvement by itself.

## Instructor note

Keep the growing-backlog episode distinct from the two settled periods. Have students draw acceptance → waiting to release → floor → good completion. Accept a monitored B trial or retention for control, but require rejection of the unsupported customer claim. No arbitrary overloading, hidden queue, cancelled order or bypassed check is an improvement. The supplied stable rates and time averages make the arithmetic possible; real observations require consistent boundaries and treatment of unfinished jobs. This is release discipline, not a new bottleneck machine or a batch-size change.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All workshop observations and policies are fictional. One kit is one order, same routing and processing requirements. Physical capability four good completions daily; no overtime, new machine, changing batch size, outsourcing, workforce cut or skipped quality check. B cap 12 counts all released unfinished kits including blocked/rework jobs; replacements released only after good completion. Stable B observation averages 12 on floor with prompt slot replacement and no starvation, not proof of minimum cap. Preliminary growing period 8 in−4 out=4 extra/day,20 over 5 days; not the data used for steady-state Little law. Separate settled periods both accept 4 and complete 4 daily, no growth/loss/cancellation: A released 24+unreleased 0; B released 12+unreleased 12. Floor averages 6 and 3 days, pre-release 0 and 3, acceptance-to-completion 6 both. No hidden queue, reset clock, artificial order deletion or shipping delay. Customer deadlines retained; due-date distribution and individual guarantees not supplied. All numbers are exact classroom averages; no inferential causal estimate, financial benefit or universal WIP optimum. Sources are actual bodies with honest scope: Michigan institutional summary is not a full read of the 1990 CONWIP paper; Little 2011 relevant theory/application sections read, not full-paper certification. Historical HKPC context not current programme availability; none of its reported lead-time percentages copied.

- [HKPC · Annual Report 2006/07 · lean-manufacturing section](https://www.hkpc.org/images/stories/reports/AR0607.pdf). Actual historical programme description includes assessment, pilot and evaluation. No reported improvement percentage attributed to our workshop.
- [John D. C. Little · Little’s Law as Viewed on Its 50th Anniversary · Operations Research, 2011](https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf). Relevant body sections define average flow quantities, boundaries and release management. Primary research, not a guarantee that reducing inventory alone preserves throughput.
- [Lean Enterprise Institute · Inventory](https://www.lean.org/lexicon-terms/inventory/). Defines inventory position/purpose and warns against reducing buffers without addressing variability/capability. No numerical cap prescribed.
- [NIST MEP · Lean and Process Improvement](https://www.nist.gov/mep/lean-and-process-improvement). Relevant flow, visual control and improvement sections read. Kanban overview is conceptual context, not a claim our rule is identical to every kanban implementation.
- [Michigan Ross · Constant Work-In-Process](https://michiganross.umich.edu/about/100-years/our-impact/1990/constant-work-process). Institutional explanation of the1990CONWIP contribution; the original paper was not counted as read. No comparative superiority claim adopted.
