# Short supply. Which allocation keeps promises?

<!-- legacy-case-id: 316 -->

OPS-27 · Hong Kong · 15–20 minutes · Shortage allocation · Protected commitments · Downstream service

![A distributor planner studies three customer trays beside a short carton of identical connectors.](../short-shipment-which-allocation-scene.jpg)

## Allocation methods serve different objectives

Oracle’s distribution-planning documentation describes demand-ratio allocation among competing demands at the same priority. SAP separately describes protected quantities and prioritised demand. These are different planning mechanisms, not a universal definition of fairness or permission to override contracts.

The distributor, orders, agreements and numbers below are fictional. The exercise asks how a discretionary shipment can support downstream service after every binding minimum has been protected.

## Opening decision

You are the allocation planner at a fictional Hong Kong distributor of an identical connector used in assembly kits. A common upstream shortfall leaves 100 connectors available for today’s dispatch against accepted orders totalling 140. Customer A ordered 60, B ordered 40 and C ordered 40. Units are indivisible, but every allocation calculated here is a whole number. Transport, assembly time and delivery capacity are sufficient and identical for all three customers.

The accepted agreements guarantee each customer at least 20 connectors today. They explicitly permit the distributor to allocate today’s discretionary remainder using either of the two rules below, and guarantee delivery of every outstanding ordered unit in two days. That later supply is secured. No customer has a stronger current entitlement, and no other reservation or commitment exists. Protect all three minimums before applying either rule; never allocate beyond an accepted order.

Proportional rule: divide the remaining connectors in proportion to each customer’s ordered quantity still unfilled after its minimum. Service-priority rule: use the remainder to maximise the total number of customers’ kits completed by tonight, counting every completed kit equally and accounting for usable alternative stock. The company’s stated objective is that kit total, subject to all agreements. Each completed kit needs one connector and all its other components. If service facts are unverified, the rule uses proportional allocation provisionally, with a review before dispatch.

At this first snapshot, alternative connector stocks and ready kit quantities are not yet verified. Choose a provisional allocation and identify exactly which facts could justify changing it. A scheduled check will supply those facts before today’s dispatch cutoff; no shipment or promise has yet been changed.

## Evidence

| Customer | Accepted order | Guaranteed today | Unfilled after minimum |
| --- | --- | --- | --- |
| A | 60 | 20 | 40 |
| B | 40 | 20 | 20 |
| C | 40 | 20 | 20 |
| Total | 140 | 60 | 80 |

**Student question:** How would you provisionally allocate the 100 connectors, and what verified downstream facts would justify using the service-priority rule instead?

## Round two

Before dispatch, the check confirms that A has 40 usable connectors of its own and other components ready for exactly 60 kits tonight. B and C each have no alternative connectors and have all other components ready for exactly 40 kits tonight. One delivered connector completes one otherwise-ready kit until that customer’s kit limit is reached. The alternative stock is compatible, unreserved and available now. All customers will use their own stock first, then today’s deliveries, to meet these kit requirements.

No further kits can be completed tonight beyond those limits. There are no other shortages, safety differences, deadlines, margins or customer weights to consider. No connector transfers between customers or additional procurement are possible today. The objective remains the total completed kits tonight, after satisfying every 20-unit minimum. Reallocate only the discretionary remainder; later delivery obligations and secured supply remain unchanged.

**Student question:** Which final allocation maximises completed kits tonight while preserving all minimums, and how does its service result compare with the provisional proportional allocation?

## First protect the promises

The minimums consume 60 of the 100 connectors, leaving 40 discretionary units. Unfilled orders after minimums are 40, 20 and 20, a 2:1:1 ratio. Proportional extras are therefore 20, 10 and 10. The provisional allocation is A 40, B 30 and C 30.

Equal extras would be a different rule, not proportional fairness. Giving all units to the biggest order would violate other minimums. With downstream facts unverified, the supplied fallback supports the proportional provisional result. A service-priority change requires usable alternative stock, ready kit limits and the number of additional kits each extra connector enables, verified before dispatch.

## Count completed kits, not shipped components

Under the provisional allocation, A has 40 own connectors plus 40 delivered but can complete only 60 kits. Twenty of its delivered connectors do not increase tonight’s output. B completes 30 kits and C completes 30: total 120. All minimums are met, but the shipment does not maximise the stated service objective.

## Allocate the discretionary remainder where it works

Keep A at its 20-unit minimum: with its own 40, it completes all 60 ready kits. Give B and C 40 each, adding 20 discretionary units to each minimum. The final allocation is A 20, B 40, C 40, using all 100 connectors and completing 60 + 40 + 40 = 140 kits.

This is 20 more kits than proportional allocation and reaches the total ready-kit ceiling of 140, so no feasible allocation can improve it. All 40 outstanding ordered connectors belong to A and arrive in two days as agreed. A’s lower shipment is not a broken minimum or an assertion that its customer relationship matters less.

## Fairness depends on what is being shared

Both rules satisfy today’s contractual floor. Proportional allocation spreads the discretionary shortage by unfilled order size; service priority directs it by verified marginal kit completion. Under a different objective or different agreements, the answer could change. Here, preserving proportionality would knowingly sacrifice 20 completed kits under the stated objective.

Record the stock evidence, ready-kit ceilings, minimums, allocation and outstanding commitments. Explain A’s later balance and the common rule without disclosing another customer’s confidential stock records. Do not promise unverified substitutions or treat a software allocation setting as a legal waiver.

## Instructor note

Allow three minutes for minimums and provisional allocation. Reveal stock and kit readiness, then allow four minutes for both kit totals. Ask students to show why A’s first 20 delivered units matter but its next 20 do not improve tonight’s service. Require the 140-kit upper bound as well as a feasible allocation.

This concerns a shortage across already accepted customers, not selecting transport or deciding whether to accept an order. Agreements expressly permit the discretionary allocation and protect later balances. Do not invent penalties, contractual overrides or customer rankings. The research sources motivate explicit constraints; their numerical results and software mechanics are not imported into this fiction.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All customers, agreements, quantities and service facts are fictional. Contractual permission for discretionary allocation is an explicit case assumption, not legal advice. All binding minimums and later deliveries remain protected. Two SAP sources are related primary product-learning materials; software features are context, not an implementation specification.

- [Oracle, Managing Distribution Plans: Fair Share Allocation](https://docs.oracle.com/cd/E26401_01/doc.122/e48756/T309464T471624.htm). Primary product documentation describes demand-ratio allocation within a priority level and distinctions among allocation methods. The case uses its own minimum-first calculation, not a claim about a configured Oracle run.
- [SAP Learning, Outlining aATP with Check Against Allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation). Explains rationing scarce material by customers and periods rather than allowing the first demand to consume everything. It does not establish contractual rights.
- [SAP Learning, Outlining aATP with Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-). Distinguishes mutually protected quantities from prioritised protection. Supports separating a protected floor from subsequent priorities; the fictional agreements are independently stipulated.
- [Microsoft Learn, Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities). Explains reservations for specific orders and the restriction on using reserved inventory elsewhere without cancelling that reservation. The case does not authorise cancellation of any binding commitment.
- [Mingwu Liu and Xiaomei Wei (2019), Inventory rationing policy and backup supply with two classes of customers, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0214386). Original mathematical research models rationing priorities and backup supply under explicit assumptions. Its cost model and numerical findings do not prove the fictional kit-allocation result, which is calculated separately.
