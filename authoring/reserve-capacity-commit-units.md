# Reserve capacity. Commit to every unit?

<!-- legacy-case-id: 328 -->

OPS-28 · Hong Kong · 15–20 minutes · Capacity reservation · Quantity flexibility · Contract cash outlays

![A seasonal buyer and supplier planner review empty production trays and a reservation worksheet.](../reserve-capacity-commit-units-scene.jpg)

## Flexibility changes when quantity becomes binding

Supply-contract research distinguishes reserving a supplier’s capacity before demand is known from placing the final order after better information arrives. Public procurement clauses also distinguish estimated or maximum quantities from a binding minimum. Flexibility has a contractual boundary and a price.

The two supplier offers below are fictional. Their fee-credit rule is invented for this exercise, not taken from a real company’s agreement or treated as a rule that applies to all reservation contracts.

## Opening decision

A fictional Hong Kong event-products buyer needs identical tabletop display trays for one seasonal event. The design is already fixed. Demand will be known before the supplier’s final production cutoff and will be either 600 trays with probability 25% or 1,000 with probability 75%. These probabilities are stipulated planning inputs, not forecasts students must estimate. The buyer must meet all realised demand on time; both offers guarantee enough capacity for either scenario with the same quality and delivery date.

Fixed F commits today to buy and receive 1,000 trays at HK$40 each, regardless of later demand. Reservation R instead charges HK$6,000 today to reserve capacity up to 1,000 trays. The buyer must later purchase at least 600 trays and may choose any whole quantity from 600 to 1,000 after demand is known. R charges HK$42 for each tray ordered, before any fee credit. The summary says up to HK$6,000 of the reservation fee can be credited against the final invoice, but the eligibility detail is not yet in the meeting pack. The full clause will arrive before either offer is signed.

The objective is the lowest expected procurement cash outlay while meeting demand, using the supplied probabilities. All relevant supplier charges are in the offers; delivery, tax and other incremental costs are included, and funding and timing differences create no additional costs. Excess trays have zero net recovery or future-use value, including any storage and recycling effects. No returns, resale, second supplier, extra order above 1,000 or product redesign are available. No payment or purchase commitment has yet been made.

## Evidence

| Offer | Commitment now | Later quantity | Price and fee |
| --- | --- | --- | --- |
| F: fixed purchase | 1,000 trays | No reduction | HK$40 per tray |
| R: reserve capacity | HK$6,000 fee and 600 minimum purchase | 600–1,000 after demand known | HK$42 per ordered tray; credit eligibility pending |

**Student question:** Which offer would you provisionally favour, what cash exposure is already clear, and what must you establish about the fee credit before making a final choice?

## Round two

The full R clause says the HK$6,000 fee is non-refundable. It earns a credit of HK$15 for each tray actually ordered above the 600-tray minimum, capped at HK$6,000 in total. The first 600 trays earn no credit. Any unused credit expires after this order and cannot be transferred or redeemed for cash. The final invoice equals HK$42 times the ordered quantity minus the earned credit; the fee paid today must still be included when calculating total outlay.

All other terms and probabilities remain unchanged. The buyer chooses 600 trays in the low scenario and 1,000 in the high scenario after observing demand; unused reserved capacity is not delivered and does not become inventory. Calculate both total cash outlays and the probability-weighted expected outlay before selecting a contract. No extra order merely to earn credit is needed or authorised.

**Student question:** Which offer minimises expected procurement outlay under the full clause, and how much fee remains unrecovered in each demand scenario? Explain what capacity flexibility buys and what it does not remove.

## First answer: distinguish a reservation from ownership

F clearly costs 1,000 × HK$40 = HK$40,000 in either scenario. It leaves 400 excess trays when demand is 600 and none when demand is 1,000. R guarantees access to as many as 1,000 but does not purchase them all: it commits the fee and at least 600 trays, with a bounded later choice.

Before the credit clause, R’s fee-plus-gross-purchase outlay is HK$31,200 at 600 and HK$48,000 at 1,000. A credit may reduce those totals by up to HK$6,000, but the summary does not establish eligibility. F is defensible for a known bill; R is provisionally attractive for avoiding low-demand excess. Do not make a final expected-cost ranking until the credit mechanics are known.

## Second answer: low demand earns no credit

At 600 trays, units above the minimum are zero, so earned credit is zero. Total R outlay is 6,000 + 600 × 42 = HK$31,200. All HK$6,000 of the fee remains unrecovered. R avoids receiving 400 unneeded trays and costs HK$8,800 less than F in this scenario, but reservation was not free.

## High demand uses the full credit

At 1,000 trays, the 400 units above the minimum earn 400 × HK$15 = HK$6,000 credit, reaching the cap. The final invoice is 42,000 − 6,000 = HK$36,000. Add the initial fee: total R outlay is HK$42,000. No fee remains unrecovered, yet R still costs HK$2,000 more than F because its unit price is higher.

## Expected outlay favours R, narrowly

R’s expected outlay is 0.25 × 31,200 + 0.75 × 42,000 = 7,800 + 31,500 = HK$39,300. F remains HK$40,000. Choose R for a HK$700 expected saving under the supplied objective and probabilities, while acknowledging its HK$2,000 disadvantage in the high-demand scenario. Do not call it cheaper in every state.

If p is the low-demand probability, R costs 42,000 − 10,800p in expectation. It is cheaper than F only when p exceeds 2,000/10,800, about 18.52%. The supplied 25% clears that threshold. This sensitivity is not a new probability forecast; changed demand beliefs or missing costs could change the choice.

## Read flexibility as a set of limits

The reservation buys a later quantity decision within 600–1,000, not zero commitment, ownership of 1,000 trays or unlimited replenishment. The minimum protects a base purchase, the maximum caps supply access and the credit rewards purchases above the minimum only. Keep the fee, gross invoice and earned credit as separate cash lines to avoid counting a refund that does not exist.

An extra tray above the minimum earns HK$15 credit but costs HK$42, so its net incremental outlay is HK$27 while credits remain. Buying unneeded units merely to recover the fee would increase cost. Demand must be observed by the stipulated cutoff; this case does not assume the same flexibility after that deadline.

## Instructor note

Use the first question to expose the difference between a headline credit and a verified credit entitlement. Do not require a unique provisional answer when a material clause is missing. Reveal the clause before any final choice, then require low, high and expected cash totals, including the fee once and the credit once.

This is a two-stage procurement commitment, not a single newsvendor quantity or postponement of product differentiation. No financial option is traded and no long-lived investment is valued. Research sources explain contractual flexibility and incentives, not the fictional fee formula. US procurement clauses are comparisons, not governing law for the buyer. Probabilities, funding and zero excess value are explicit simplifying assumptions.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All offers, prices, probabilities and credit rules are fictional; no agreement is being signed. Demand is observed before the final quantity cutoff. Excess has zero net value and all incremental cash charges are included. Fee and earned credit are distinct cash lines. The Cirrus Logic disclosure contains different actual fee and prepayment terms; no claim is made that it uses this case’s credit formula. Foreign public procurement terms provide background, not local legal advice.

- [Gérard Cachon and Martin Lariviere (2001), Contracting to Assure Supply](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Cachon_lariviere_ms_assuresupply.pdf). Original research separates capacity commitment before demand information from final ordering afterwards and examines incentives. No equilibrium result or parameter is applied to this fictional offer.
- [Andy Tsay (1999), The Quantity Flexibility Contract and Supplier-Customer Incentives](https://www.researchgate.net/publication/227447166_The_Quantity_Flexibility_Contract_and_Supplier-Customer_Incentives). Original paper’s full public text describes coupled minimum purchase and maximum supply commitments. The case uses its own bounded-quantity terms, not the paper’s optimal contract.
- [Barnes-Schuster, Bassok and Anupindi (2002), Coordination and Flexibility in Supply Contracts with Options](https://www.academia.edu/54656229/Coordination_and_Flexibility_in_Supply_Contracts_with_Options). Public original manuscript discusses the buyer’s later response to demand and the supplier’s cost of providing flexibility. No general claim of coordination or universal savings is made here.
- [US Federal Acquisition Regulation 52.216-22, Indefinite Quantity](https://www.acquisition.gov/far/52.216-22). Primary contract clause distinguishes estimates from actual orders and specifies minimum and maximum obligations. US public procurement law does not govern the fictional offer.
- [Cirrus Logic, 2024 Annual Report, Capacity Reservation Agreement note](https://www.sec.gov/Archives/edgar/data/772406/000077240624000043/a2024fullannualreportars.pdf). Original company disclosure distinguishes a non-refundable capacity fee, purchase commitments and a separate purchase prepayment credited to invoices. Its actual terms differ from the invented combined fee-credit arrangement here.
