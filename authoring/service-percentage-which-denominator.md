# Ninety-five per cent service. Of what?

<!-- legacy-case-id: 340 -->

OPS-29 · Hong Kong · 15–20 minutes · Cycle service · Unit fill rate · Complete-order service

![A distributor’s planner examines order cards beside cartons of generic connectors.](../service-percentage-which-denominator-scene.jpg)

## The reporting question

Inventory service percentages can count different things: replenishment cycles without a shortage, individual units supplied, or whole orders completed. Primary teaching and operational documentation distinguish those measures. A shared percentage without its denominator is not a comparable service promise.

This fictional distributor uses one reliable demand log and two supplied feasible policy replays. The task is to interpret service objectives, not audit data provenance, calculate an optimal reorder point or predict future service from a small sample.

## Opening decision

A Hong Kong distributor supplies one standard, non-safety-critical connector. Two teams propose replenishment policies A and B for a bounded follow-up trial. Both report “95% service” from replays of the same demand log. The headline summaries do not state how they counted service. Management must decide whether that headline is enough to treat the policies as equivalent or whether a comparison needs more evidence before selecting the trial policy.

For this exercise, both policies are operationally feasible with the same total procurement, holding and handling cost, lead times and quality. The supplied replays have been checked for physical feasibility; students need not invent stock flows or a new policy. Management’s primary objective is to minimise the number of requested units not available immediately. It also wants the consequences for complete orders and shortage-free cycles reported openly. Partial deliveries are allowed and useful, and no minimum whole-order service constraint applies in this trial. All units have equal importance for the stated objective.

A replenishment cycle is the interval between two scheduled replenishment arrivals. “Immediate” means available at the original order request; a later catch-up delivery does not repair that score. All requested demand, including unfilled units, remains in the denominator. The complete log and the teams’ definitions will be supplied before the final selection. Neither summary is alleged to be false; their meanings are not yet established. No actual customer commitment or guaranteed future service target is being made.

## Evidence

| Opening comparison | Policy A | Policy B |
| --- | --- | --- |
| Reported service | 95%; definition not yet supplied | 95%; definition not yet supplied |
| Test conditions | Same demand log and cost boundary | Same demand log and cost boundary |
| Primary objective | Fewest units unavailable immediately | Fewest units unavailable immediately |

**Student question:** Can the two 95% headlines justify treating A and B as equivalent, and what definitions and counts do you need before choosing under the stated objective?

## Round two

The full log covers twenty consecutive replenishment cycles, with exactly two orders in each cycle. There are no other requests, cancellations, substitutions or corrections. The table groups identical rows; each entry states units per order, not a group total. The same original orders and cycle boundaries are used for both policies. Unfilled units are fulfilled later, outside the immediate-service score.

| Cycles and order group | Number of orders | Units requested per order | A immediate units per order | B immediate units per order |
| --- | --- | --- | --- | --- |
| 1–10: first order in each cycle | 10 | 20 | 20 | 15 |
| 1–10: second order in each cycle | 10 | 20 | 20 | 20 |
| 11–19: both orders in each cycle | 18 | 20 | 20 | 20 |
| 20: first order | 1 | 20 | 20 | 20 |
| 20: second, large order | 1 | 220 | 20 | 220 |

Team A counts the fraction of cycles with no unmet immediate demand, so a cycle fails if even one requested unit is unavailable. Team B counts total units filled immediately divided by total units requested. Also calculate complete-order service: orders whose entire requested quantity is available immediately divided by all original orders. Do not split an incomplete order into smaller “successful” orders, or average cycle percentages without their demand weights. These are descriptive replay results, not estimated guarantees about future demand.

**Student question:** What are both policies’ shortage-free cycle rates, unit fill rates and complete-order rates, and which policy should enter the trial under the stated unit-based objective?

## First answer: define success before comparing

The opening headlines are insufficient to establish equivalence or a winner. Request the time horizon, cycle boundaries, numerator and denominator, whether a “fill” means units or complete orders, the service deadline and treatment of late or missing demand. The primary objective points toward immediate unit fill, but that cannot be inferred from an undefined 95%. Hold the final choice until the common log and definitions are available.

## Count the common demand

There are 10 + 10 + 18 + 1 + 1 = 40 original orders in 20 cycles. Requested units are 10 × 20 + 10 × 20 + 18 × 20 + 20 + 220 = 1,000. The large order is 22% of requested units but just 1/40, or 2.5%, of orders. It occupies one of twenty cycles. Different denominators therefore give its shortage different weight.

## Policy A: few failed cycles, a large shortage

A fills the first 39 orders completely and supplies only 20 of the last 220 units. It fills 800 of 1,000 requested units immediately, leaving 200 unavailable: unit fill is 80%. Only cycle 20 has any shortage, so 19/20 cycles are shortage-free, or 95%. Complete-order service is 39/40, or 97.5%. Team A’s headline is correct but does not mean 95% of units were supplied.

## Policy B: many small shortages, more units supplied

B misses five units on the first order of each of cycles 1–10: 10 × 5 = 50 units unavailable. It fills 950/1,000 units immediately, or 95%. Ten cycles contain a shortage, so only 10/20, or 50%, are shortage-free. Ten original orders are incomplete, leaving 30/40 complete, or 75%. The large order is fully supplied. Team B’s 95% is also correct but measures something else.

## Choose the objective, disclose the trade-off

Choose B for the bounded follow-up trial under the stated objective: 50 rather than 200 units unavailable immediately, a reduction of 150. Its unit fill is 15 percentage points higher. Do not call it better on every service measure: A has 45 percentage points more shortage-free cycles and 22.5 percentage points more complete orders. If management instead prioritised complete orders or imposed a minimum order-service constraint, the decision could change.

Report all three labelled measures with their counts and horizon. Late fulfilment cannot turn an initial miss into an immediate success. The replay is a decision input, not evidence that B will guarantee 95% service or the same cost on every future demand path. The trial should retain the original-order and immediate-availability definitions while checking subsequent performance.

## Instructor note

Before the reveal, reward a request for operational definitions rather than guessing that equal percentages mean equal performance. After it, have students total orders and units, then mark failed cycles, incomplete orders and missing units separately. Each of the first ten B shortages fails one order and one cycle; A’s single large shortage has a much larger unit consequence.

No demand probability distribution, reorder-point formula or causal field comparison is supplied. The replays and cost equivalence are stipulated, not empirically validated policy superiority. Cycle service is often expressed as a probability in inventory theory; this exercise reports its observed finite-log counterpart. Vendor metric names and time cutoffs vary, so the printed definitions govern. This distinguishes service objectives rather than information-system provenance.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Fictional teaching case. Demand, policy replays, feasibility and cost equality are supplied assumptions. Rates describe this log only, not guaranteed future service. Cycle, unit and original-order definitions and the immediate deadline govern every calculation.

- [MIT Center for Transportation & Logistics, Supply Chain Fundamentals Key Concepts (Winter 2020)](https://scx-static-assets.s3.amazonaws.com/SCx%20Key%20Concept%20Documents/MITx_SCx_KeyConcept_SC1x_FV.pdf). The service-metric section distinguishes no-stockout probability per replenishment cycle from item demand filled. The case uses finite-log observed rates, not the document’s distributional safety-stock formulae.
- [Oracle Production Scheduling, Evaluating Production Schedules: Customer Service KPIs](https://docs.oracle.com/cd/E26401_01/doc.122/e48797/T581889T582170.htm). Primary documentation separately defines complete-order, line and unit fill using specified timing. This case has one item per order and explicitly uses immediate availability, not every vendor’s on-time convention.
- [SAS Inventory Optimization 5.1 User’s Guide, inventory analysis KPIs](https://support.sas.com/documentation/onlinedoc/invopt/51/invoptug.pdf). The provider distinguishes fulfilled-demand ratios, readiness measures and facility/item analysis. Historical product guidance supports explicit measurement scope, not a current implementation recommendation.
- [SAP Learning, Other Drivers of Safety Stock: service-level metrics and conversion](https://learning.sap.com/courses/mastering-sap-ibp-for-inventory-planning-and-optimization/other-drivers-of-safety-stock-service-level-periods-between-replenishment-lot-size-delivery-type-and-promotions_c74e59d4-bc17-4bdf-932f-c65740b9d768). Primary training distinguishes fill rate from non-stockout probability and discusses assumptions needed to convert between them. No SAP algorithm, normality assumption or automatic conversion is used here.
- [Roberto Rossi, Onur A. Kilic and S. Armagan Tarim, A note on Tempelmeier’s beta-service measure](https://arxiv.org/pdf/1103.1286). Original research note defines immediately satisfied demand and explains why horizon and cycle service formulations differ. Its model and example are not reproduced; the fictional log is independently constructed.
