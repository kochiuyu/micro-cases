# The hedge moves. Does it move with our cost?

<!-- legacy-case-id: 326 -->

FIN-28 · Hong Kong · 15–20 minutes · Basis risk · Commodity exposure · Scenario cash costs

![A processor finance analyst compares a delivery-cost worksheet beside containers of industrial raw material.](../hedge-moves-delivered-cost-scene.jpg)

## The reference price is not always the delivered price

CME explains that local cash prices can differ from a reference futures price because of freight, quality and local supply conditions. LME educational material similarly separates a base reference price from physical premiums. Offsetting the base-price movement does not automatically fix the delivered bill.

This case supplies a fictional hedge payoff for arithmetic only. It is not an instruction to trade, select a real instrument or apply hedge accounting.

## Opening decision

A fictional Hong Kong processor must buy exactly 1,000 kg of an industrial input in one month. Quantity, quality and delivery date are fixed. Its supplier’s all-in delivered price per kg will be the reference index I on that date plus a local premium P. There are no other delivery charges, taxes or exchange-rate effects in this model. The initial planning assumption is P = HK$10 per kg, but that premium is not contractually fixed.

The team compares no hedge with one permitted classroom hedge covering exactly 1,000 kg and the same index observation date. The hedge pays the processor 1,000 kg × (I − HK$100/kg) at settlement. A negative result means the processor pays that amount in absolute terms. The fixed all-in hedge fee is HK$2,000. Both settlement and the physical purchase occur on the same date. The exercise stipulates sufficient funding, no default, no quantity mismatch and no additional financing or transaction costs; real collateral and liquidity requirements are outside this simplified payoff model.

Management’s stated objective is to remove index-driven variation in the purchase cost, not to beat every possible unhedged outcome. It also asks whether the plan guarantees an all-in HK$115,000 procurement ceiling. For the first calculation, use the two supplied index scenarios and the HK$10 planning premium. No probabilities are supplied. Calculate unhedged cost and hedged net cash cost, then choose how to describe the protection and the limit of that description. No actual financial position is authorised or requested.

## Evidence

| Scenario at purchase | Index I, HK$/kg | Planning premium P, HK$/kg |
| --- | --- | --- |
| Higher index | 120 | 10 |
| Lower index | 80 | 10 |

Unhedged cost = 1,000 × (I + P). Hedged net cash cost = physical purchase cost − hedge receipt + HK$2,000. Subtracting a negative receipt adds the hedge payment.

**Student question:** Would the supplied hedge serve the index-risk objective, and what are the cash costs in both scenarios? Can the HK$115,000 all-in ceiling be called guaranteed?

## Round two

Before any commitment, a local handling-capacity disruption makes a HK$25 per kg premium a credible stress scenario, independently of the index. The supplier pricing formula remains I + P; the hedge formula, quantity, fee and date do not change. Recalculate both index scenarios with P = 25. This is a stress test, not a forecast or an assigned probability.

No fixed-premium supplier offer or additional premium hedge is available in the exercise. Management can keep the index hedge as partial protection, or decline it, but cannot label the residual premium exposure eliminated. It must report any breach of the HK$115,000 planning ceiling and seek a revised procurement plan rather than claim the same index hedge covers the local component.

**Student question:** What are the stressed cash costs with and without the hedge, and how should management describe the remaining exposure and the procurement-ceiling problem?

## First answer: what the hedge offsets

At I = 120 and P = 10, the physical cost is HK$130,000. The hedge receipt is HK$20,000, so net cost is 130,000 − 20,000 + 2,000 = HK$112,000. At I = 80, physical cost is HK$90,000; the negative HK$20,000 receipt is a payment, giving 90,000 + 20,000 + 2,000 = HK$112,000.

The supplied hedge removes variation caused by the index when premium and quantity are held fixed. It costs more than remaining unhedged in the low-index scenario, which is not a failure of the stated risk-reduction objective. Both first-snapshot results are under HK$115,000, but the premium was only assumed, not fixed, so no unconditional ceiling guarantee follows.

## Second answer: the premium moves separately

At P = 25 and I = 120, unhedged cost is HK$145,000 and hedged cost is 145,000 − 20,000 + 2,000 = HK$127,000. At I = 80, unhedged cost is HK$105,000 and hedged cost is 105,000 + 20,000 + 2,000 = HK$127,000. Both hedged stress costs exceed the HK$115,000 ceiling by HK$12,000.

## See the residual directly

Substitution gives hedged cost = 1,000(I + P) − 1,000(I − 100) + 2,000 = HK$102,000 + 1,000P. The index cancels; the premium does not. Raising P from 10 to 25 increases net cost by HK$15,000. The premium would need to be no more than HK$13 per kg to stay within HK$115,000 under this model.

This mismatch between the reference exposure and the actual delivered exposure is basis risk. The formula isolates it cleanly here; real hedges can also have date, grade, quantity, funding and other mismatches. Do not assume the reference price and local premium always move together or in opposite directions.

## Retain a precise claim, not an all-in guarantee

For the stated objective, retaining the supplied hedge as index-only protection remains defensible. It holds stressed net cost constant across the two index scenarios, but cannot satisfy the separate all-in ceiling in the premium stress. Declining the hedge retains both index and premium exposure; its cheaper low-index outcome does not guarantee a lower bill.

Report the residual premium and the HK$12,000 stress shortfall. Management needs a revised procurement or funding plan and any further authorised analysis; no additional instrument or supplier agreement is invented here. Scenario comparisons alone do not establish expected savings or a universal reduction in total cost variance without a joint distribution.

## Instructor note

Allow four minutes for the two initial cash reconciliations. Reveal the premium stress and require two more reconciliations before simplifying the formula. Watch the negative hedge receipt: it increases the buyer’s cash cost. Ask what is held constant when describing index-risk reduction.

All prices, contract terms and fees are invented. This is a supplied payoff, not a specification of a listed contract, an investment recommendation or a real transaction. Do not teach operational trading steps or equate terminal net cost with real-world liquidity needs. Unlike a natural foreign-currency offset, the physical delivered exposure contains a local component absent from the hedge.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All entities, quantities, prices and payoff terms are fictional. No real derivatives transaction, trading instruction or accounting treatment is requested. Funding and terminal settlement simplifications are explicit; real collateral and liquidity risks remain outside the arithmetic. Three LME materials are related exchange educational sources, not independent empirical evidence.

- [CME Group, Learn about Basis: Grains](https://www.cmegroup.com/education/courses/introduction-to-grains-and-oilseeds/learn-about-basis-grains). Explains cash-minus-futures basis, local determinants and its effect on a buyer’s hedge outcome. No grain prices or trade example are reused.
- [London Metal Exchange, The role of premiums and discounts in pricing industrial metals contracts](https://www.lme.com/en/Education/Online-resources/LME-Digest/The-role-of-premiums-and-discounts-in-pricing-of-industrial-metals-contracts). Separates base reference prices from delivery, grade and regional premiums; not all components are hedgeable with the base instrument.
- [London Metal Exchange, How are LME prices referenced in physical contracts?](https://www.lme.com/Education/Online-resources/LME-Digest/How-are-the-LME-prices-referenced-in-physical-contracts). Describes physical contracts using an underlying reference plus separately negotiated premiums and residual exposure.
- [London Metal Exchange, Hedging](https://www.lme.com/sustainability-and-physical-markets/physical-market-benefits/hedging). Explains relating a hedge to physical purchase exposure and real margin requirements. The fictional payoff abstracts from those operational features and makes no accounting-standard claim.
- [Cboe, Risk Disclosure Statement for Futures and Options on Futures](https://cdn.cboe.com/resources/general/Combined_Risk_Disclosure_Statement_for_Futures_and_Options.pdf). Primary exchange-hosted disclosure explains loss and additional-margin risks. Supports the boundary between a classroom terminal-payoff calculation and an actual trading decision.
