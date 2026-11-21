# Protection when the portfolio falls

<!-- legacy-case-id: 481 -->

FIN-41 · Hong Kong · 15 minutes · State prices · Contingent claims · Hedge basis

![A trustee and investment officer compare two payout offers beside scholarship papers in a Hong Kong campus office.](../protection-when-the-portfolio-falls-scene.jpg)

## Weekly index contracts come to Hong Kong

Trading in weekly Hang Seng Index options began on 16 September 2019. HKEX said the short maturities could help market participants manage exposure around events. The exchange’s actual contract settles using a specified index measure. The fictional claims below instead pay fixed amounts in two defined index states.

## Opening decision

You are advising the fictional Harbour Learning Foundation. Its treasurer must present a benchmark value and a hedge recommendation to the trustees. The foundation’s existing assets leave it HK$50 short of next week’s scholarship payment in the index-down state, but it has enough in the index-up state.

The two index states are equally likely in the treasurer’s forecast. All amounts in the exhibit are HK dollars per unit; all contracts pay on the same date. From the two traded benchmark securities, the treasurer can construct claims that pay on that date.

Use a frictionless two-state benchmark. The note and fund can be bought or sold short in fractional units at the exhibited prices. Ignore credit risk, fees and other interim payments. The foundation is not required to trade the benchmark portfolios; their costs are valuation references.

The offered claims are alternatives: Down pays for an index decline and costs HK$25 today; Up pays only on an index rise and costs HK$23. The foundation can buy at most one. Its immediate objective is to meet the scholarship payment in the bad state, as well as identify which offer is cheap relative to its benchmark.

Premiums come from a separate, sufficient budget and do not change the stated scholarship shortfalls or any other payment commitment.

## Evidence

| Security | Price now | Index down | Index up |
| --- | --- | --- | --- |
| Traded note | 95 | 100 | 100 |
| Traded cyclical fund | 92 | 80 | 120 |
| Down offer | 25 | 50 | 0 |
| Up offer | 23 | 0 | 50 |

**Student question:** Do Down and Up have the same benchmark price, and which offer should you recommend for the scholarship payment?

## Round two

Before signing, you learn that the latest foundation forecast was too strong: its own portfolio can also fall short by HK$50 when the index ends up, for example when a large holding diverges from the index. The benchmark securities and claim payouts still depend only on the two index states; the index-up state may now contain both a shortfall and no shortfall for the foundation.

The trustee asks whether adding the other claim as well would remove the cash gap. For this round the two offered claims may be bought together at their original prices; a safe note remains available at its benchmark price.

**Student question:** Does Down still cover every scholarship shortfall, and which choice gives a certain HK$50 at the payment date under the stated terms?

## Debrief · Reproduce the down-state cash

Buy 1.5 notes and short 1.25 funds. In the down state this pays 150 − 100 = HK$50, and in the up state 150 − 150 = zero. Its cost is 1.5 × 95 − 1.25 × 92 = HK$27.50.

## Debrief · Reproduce the up-state cash

Take the payoff from half a note and subtract the down-state portfolio. The up-state claim therefore costs 47.50 − 27.50 = HK$20. The forecast expected value of each offer is HK$25; it is not its benchmark price.

## Debrief · Price and funding point the same way

Down costs HK$25 against its HK$27.50 benchmark; Up costs HK$23 against HK$20. Down also pays exactly when the original scholarship shortfall occurs. Its recommendation follows the stated objective, not a claim about the future index.

## Debrief · Hedge what actually falls short

Down alone pays zero when the index is up, even if the foundation has a shortfall. Buying Down and Up gives HK$50 in both index states for HK$48. Half a safe note delivers the same HK$50 for HK$47.50, so it is the cheaper stated certain-cash solution.

## What the two-state instruments cannot do

The modeled index claims cannot distinguish two outcomes that have the same index state but different foundation shortfalls. The safe note covers both by paying regardless, including when the foundation does not need the cash.

## Instructor note

Allow 15 minutes: 2 to frame the decision, 4 for the first calculation and a vote, 4 for the second round, and 5 to defend or revise a recommendation. Ask each group to cite a number and name the assumption that would change its call.

Ask groups to distinguish the prices of state payouts from their probabilities and to identify hedge-basis risk. The exact comparisons require borrowing or shorting only for the pricing benchmark, known contractual payoffs, and no fees or credit risk. An index option does not literally pay on the foundation’s own funding deficit.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All people, prices, payoffs, quantities and contract terms in the classroom exercise are fictional. The opening news context describes the cited historical developments, not the case’s figures or recommendations.

- [HKEX, August 2019 announcement of weekly index options](https://www.hkex.com.hk/en/News/News-Release/2019/190807news?sc_lang=en). Explains the planned start date and the intended use around short-term events; the notice was conditional on approval.
- [HKEX Fact Book 2020, weekly HSI options trading table](https://www.hkex.com.hk/-/media/HKEX-Market/Market-Data/Statistics/Consolidated-Reports/HKEX-Fact-Book/HKEX-Fact-Book-2020/FB_2020.pdf). The footnote confirms trading started on 16 September 2019; volume is not evidence of the classroom prices.
- [HKEX, Weekly Hang Seng Index Options](https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Weekly-Hang-Seng-Index-Options?sc_lang=en). Contract specifications show how final settlement is based on index observations; a real option does not just pay a fixed bonus for a generic downturn.
- [Harrison and Kreps, Martingales and Arbitrage in Multiperiod Securities Markets](https://www.sfu.ca/~kkasa/HarrisonKreps_79.pdf). The two-date model treats marketed contingent claims as payoff portfolios priced with a linear rule in frictionless markets; the exercise’s specific quotes are fictional.
- [Optiver, Improving settlement for Hong Kong’s weekly index options](https://www.optiver.com/insights/markets/improving-settlement-for-hong-kongs-weekly-index-options/). Market participant’s own explanation of averaging and why payout can diverge from terminal exposure; its proposed changes are recommendations rather than rules.
