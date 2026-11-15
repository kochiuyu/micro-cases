# Keep running, or stop on purpose?

<!-- legacy-case-id: 64 -->

OPS-06 · Hong Kong · 10–15 minutes · Operations · Maintenance · Reliability

![A production supervisor and service coordinator discuss an appointment folder beside paper stacks and an enclosed machine at rest.](../planned-stop-scene.jpg)

## In the news

On 27 June 2025, the Hong Kong Government reported receiving MTR investigation reports and an action plan covering targeted inspections, stronger asset monitoring and incident response. It also called for faster application of predictive maintenance to support railway resilience.

This illustrates maintenance as part of reliable operations. Railway safety is not the subject of the cost comparison below: the fictional workshop decision concerns an optional service and excludes safety faults or overdue required maintenance.

## Opening decision

Fictional classroom situation. A Hong Kong print-finishing workshop has a busy week ahead. Its paper-folding machine is working. An optional preventive service appointment before that week would interrupt production, so the operations manager proposes postponing it: “Why stop a machine that is still producing?”

The all-in cost of keeping the appointment is HK$2,000, including the service and the economic cost of the planned interruption. This amount is not just the technician’s invoice. The manager wants to preserve today’s output, while the supervisor worries about an unscheduled stoppage when customer deadlines are closer.

For this exercise, there is no known safety fault, no overdue mandatory service, and either timing choice remains within manufacturer requirements. The component under discussion is not safety-critical. Safety obligations are not traded against money. A condition assessment relevant to next week’s reliability is still being reviewed.

## Evidence

| Before the decision | What is known |
|---|---|
| Machine status | Working |
| Keep optional service appointment | HK$2,000 all-in, including planned interruption |
| Postpone | Avoid that planned cost now |
| Disruption risk next week | Assessment not yet reviewed |

**Student question:** Would you keep the service appointment or postpone it? What evidence would you need to compare the planned interruption with an unexpected failure?

## Round two

The condition assessment supplies the following fictional teaching estimates for the coming week: a 30% chance of one disruptive failure if service is postponed, compared with 5% if the appointment is kept.

A failure would create HK$10,000 in total incremental loss, including repair and disruption. This same loss applies under either option and is additional to any planned service cost. At most one failure is modelled. All other costs and outcomes are assumed equal; effects after the coming week are excluded. These figures are not estimates from MTR or the cited studies.

**Student question:** Which option has the lower expected incremental cost under these assumptions? Would that calculation guarantee a better outcome next week, and which assumptions most need checking?

## Compare the planned cost with the risk left behind

Postponing has expected incremental cost 30% × HK$10,000 = HK$3,000.

Keeping the appointment has expected incremental cost HK$2,000 + 5% × HK$10,000 = HK$2,500. The residual failure risk does not disappear after service.

The model therefore favours keeping the appointment by HK$500 in expected cost. Do not add the planned interruption again: it is already inside the HK$2,000. Do not add separate repair or disruption charges again: both are already inside the HK$10,000 failure loss.

## Expected cost is not next week’s bill

An expected cost is a probability-weighted average across possible outcomes, not the amount certain to be paid. If no failure occurs, postponing incurs none of the modelled costs, while service costs HK$2,000. A failure after service would still produce a total of HK$12,000 in modelled costs.

One good week after postponement would not prove the risk assessment wrong. One failure after service would not prove the appointment was pointless. Judge the decision using the evidence available beforehand, and improve the estimates as comparable maintenance and failure records accumulate.

## How much risk reduction pays for the stop?

Service costs HK$2,000 against a HK$10,000 failure consequence. It must reduce failure probability by more than 2,000 ÷ 10,000 = 0.20, or 20 percentage points, to lower expected cost in this model. Exactly 20 points gives a tie.

The stated reduction is 30% − 5% = 25 percentage points, which passes that threshold. If the untreated risk were only 20% and the serviced risk still 5%, the reduction would be 15 points: postponing would cost HK$2,000 in expectation versus HK$2,500 for service.

This sensitivity check shows why the assessment matters. The threshold is conditional on the stated costs, time horizon and safety exclusions, not a rule for all machines.

## Plan reliability, not just uninterrupted activity

A planned stop can be scheduled around jobs, staff and materials. An unexpected stop can collide with delivery commitments. Ask how the risk estimates were produced, what comparable equipment records show, what failure would interrupt and whether a practical fallback exists.

Running until failure can be reasonable for some inexpensive, noncritical items that are quickly replaced. Maintenance is not always economically justified at every interval. Here the evidence favours the appointment within the simplified one-week model, while real decisions must also respect safety, manufacturer requirements and longer-term asset effects.

## Instructor note

Let students defend today’s output before revealing the assessment. Keep the discussion operational: planned versus unplanned downtime, customer commitments and reliable capacity, not merely a probability exercise.

Check the HK$3,000 versus HK$2,500 calculation and distinguish a 25-percentage-point reduction from a 25% relative reduction. Invite students to identify where uncertain estimates or an omitted longer-term consequence would change the decision.

Do not apply this classroom threshold to railway safety, known faults or required maintenance. No technical repair or inspection procedure is prescribed.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The workshop, service decision, probabilities and costs are invented. The example concerns a non-safety-critical component, no known safety fault or overdue required maintenance, and operation within manufacturer requirements. The HK$2,000 includes the planned interruption; the HK$10,000 includes repairs and disruption if a failure occurs. At most one failure, the same consequence under either choice, a one-week horizon and all other outcomes equal are assumed. Sources checked 14 November 2026. No cited study supplies these probabilities or validates this machine’s safety. Historical US evidence and facilities guidance are background, not causal estimates for Hong Kong workshops.

1. [Hong Kong Government, investigation reports and action plan from MTRCL, 27 June 2025](https://www.info.gov.hk/gia/general/202506/27/P2025062700592.htm) — Primary announcement on inspections, asset monitoring and predictive maintenance. Railway safety decisions are expressly outside the fictional economic comparison.
2. [Douglas S. Thomas and Brian A. Weiss, NIST AMS 100-34, June 2020](https://nvlpubs.nist.gov/nistpubs/ams/NIST.AMS.100-34.pdf) — Original survey and analysis of US manufacturing maintenance costs and losses, with estimates referring to 2016. Observational associations are not transferred as causal effects or local probabilities.
3. [Douglas S. Thomas, NIST AMS 100-18, April 2018](https://nvlpubs.nist.gov/nistpubs/ams/NIST.AMS.100-18.pdf) — Examines direct maintenance costs, downtime, lost sales and evidence gaps. Supports explicit assumptions rather than a universal savings claim.
4. [Pacific Northwest National Laboratory, Maintenance Approaches, undated](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches) — Facilities guidance comparing reactive, preventive and predictive approaches, drawing on FEMP 2010. No headline savings range is used in the case.
5. [IBM, What is reactive maintenance?, undated](https://www.ibm.com/think/topics/reactive-maintenance) — Vendor-authored explanation of unplanned downtime and circumstances where easily replaced noncritical assets may suit a reactive approach. No product effectiveness claim is adopted.
