# A buy order. A higher quote?

<!-- legacy-case-id: 483 -->

FIN-42 · Hong Kong · 15 minutes · Bid–ask spread · Adverse selection · Bayesian updating · Market making

![Two Hong Kong dealing-desk trainees study an incoming order on a screen beside a two-column quote board.](../a-buy-order-a-higher-quote-scene.jpg)

## HKEX changes the rules for ETF liquidity

In 2020 HKEX introduced new market-making requirements and reduced tick sizes for eligible products as part of its ETF liquidity measures. Actual spreads can reflect many factors. The fictional desk below isolates one: what an incoming order says about the value of an asset.

## Opening decision

At a fictional Hong Kong ETF dealing desk, you must set prices for one unit of a simple fund. At today’s close it will be worth either HK$120 or HK$80. Before the next message, your desk assigns a 40% chance to the higher value.

You face one incoming market order. The trader buys from you at your ask or sells to you at your bid. The order direction is the only new clue. For this exercise it follows the conditional frequencies in the exhibit and does not respond to small changes in your quote.

Set each price so that you break even on average conditional on trading on that side. You have no fees, processing costs, inventory concerns, tick-size constraints or other information. The table gives order likelihoods in each value state, not probabilities of the value after seeing an order.

## Evidence

| At the close | Prior chance | Buy likelihood | Sell likelihood |
| --- | --- | --- | --- |
| HK$120 | 40% | 80% | 20% |
| HK$80 | 60% | 30% | 70% |

**Student question:** What bid and ask should the desk post before learning the order’s direction, and why is one unconditional price not sufficient?

## Round two

The first order is a buy and trades at your posted ask. A second order is about to arrive from a scheduled portfolio rebalance. Its direction is independent of the fund’s closing value and the first order: the second trader buys or sells with equal likelihood in either value state.

No closing value is revealed between trades, and no other news arrives. The desk uses the updated belief after the first buy, then quotes before the second direction is known. The same break-even rule applies.

**Student question:** What bid and ask should you now post for the rebalance order, and has eliminating the informational spread undone what you learned from the first buy?

## Debrief · Put the buy in the denominator

The joint probabilities of a buy and a high or low outcome are 0.40 × 0.80 = 0.32 and 0.60 × 0.30 = 0.18. A buy is 0.50 likely overall, so the posterior high probability is 0.32 ÷ 0.50 = 64%.

## Debrief · A sale sends the other signal

With a sell, the high and low joint probabilities are 0.08 and 0.42. The posterior high probability is 0.08 ÷ 0.50 = 16%. Conditional value is HK$80 plus HK$40 times the posterior high probability.

## Debrief · The quote protects the desk

The bid is HK$86.40; the ask is HK$105.60. The prior value of HK$96 would lose HK$9.60 on average conditional on either side of the incoming trade. Quotes differ because the orders select different mixtures of states.

## Debrief · Keep the update, drop the spread

After the first buy the high probability is 64%. Multiplying both state probabilities by 0.50 for either direction of the second order leaves that 64% unchanged after normalising. Bid and ask both equal HK$105.60.

## Two comparisons to report

Relative to the initial bid–ask spread of HK$19.20, the next spread is zero in the model. Relative to the initial unconditional value of HK$96, the new common quote is HK$9.60 higher. The first order still conveys information.

## Instructor note

Allow 15 minutes: 2 to frame the decision, 4 for the first calculation and a vote, 4 for the second round, and 5 to defend or revise a recommendation. Ask each group to cite a number and name the assumption that would change its call.

Have learners sketch 100 cases with 32 high buys and 18 low buys before calculating. Real ETF market makers face costs, inventory risks, tick sizes and product-level quoting obligations, so a zero informational spread is not a prediction of a zero observed spread. Neither this ETF nor its order flow is a real product.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All people, prices, payoffs, quantities and contract terms in the classroom exercise are fictional. The opening news context describes the cited historical developments, not the case’s figures or recommendations.

- [HKEX, Assessing the Impact of ETF Liquidity Enhancements](https://www.hkex.com.hk/-/media/HKEX-Market/Products/Securities/Exchange-Traded-Products/Attachment/HKEX--Assessing-the-impact-of-HKEX_s-ETF-liquidity-enhancements_whitepaper_en.pdf). Documents the 2020 measures, including new market-making obligations and a tick-size change; the exercise does not attribute empirical spreads solely to information.
- [HKEX, Market Makers overview](https://www.hkex.com.hk/Products/Securities/Exchange-Traded-Products/Market-Makers/Overview?sc_lang=en). Lists actual market-making programmes and links to product-level obligations; these are not the fictional quote rule.
- [HKEX, Securities FAQ, ETF section](https://www.hkex.com.hk/Global/Exchange/FAQ/Products/Securities?sc_lang=en). Identifies spread, size and response-time obligations and notes that market price may differ from net asset value.
- [Glosten and Milgrom, Bid, Ask and Transaction Prices](https://milgrom.people.stanford.edu/wp-content/uploads/1984/09/Bid-Ask-and-Transaction-Prices.pdf). Original theoretical analysis of how heterogeneous information can create a spread without inventory or processing costs.
- [HKEX, Exchange-Traded Products investor resources](https://www.hkex.com.hk/Products/Securities/Exchange-Traded-Products/Investors?WT.mc_id=SpreadTableEffective_EN_HomepageWebBanner_ETPInvestor&sc_lang=en). Explains why tick size can influence observed spreads; the fictional model assumes no tick-size or quote-size constraints.
