# The highest estimate. The best bid?

<!-- legacy-case-id: 143 -->

ECO-12 · Hong Kong · 10–15 minutes · Common value · Winner’s curse · Conditional information

![Two resellers independently inspect a shared lot of plain stationery while sealed envelopes rest on separate desks.](../winning-is-information-scene.jpg)

## Industry context

Hong Kong’s Government Logistics Department publishes auction information for government stores, and its open-data catalogue includes 2026 auction lists describing confiscated, used or surplus and unclaimed items.

This is context for a surplus-stock decision, not a claim about anyone’s auction profit. Our fictional private sale uses invented sealed-bid rules and numbers, not GLD’s auction terms.

## Opening decision

A fictional Hong Kong reseller inspects a mixed lot of unused stationery. There are two bidders. Both would obtain the same eventual net resale value from the lot: resale receipts after all handling, selling, transport and other costs except the auction payment. Neither has a special customer or cost advantage. That common value is uncertain, and each inspection gives an imperfect estimate.

Your inspection report puts expected net resale value at HK$10,000. The report allows two equally likely values, HK$8,000 and HK$12,000. These probabilities already reflect your inspection; they are not a claim that every lot has the same distribution.

The sale is first-price sealed-bid: highest bid wins and pays its own bid; losers pay nothing. You may bid in HK$100 increments, lose any tie and may abstain for zero payoff. There is no reserve, entry fee or later negotiation. The aim is to maximise expected monetary surplus, with no value placed on winning for its own sake. A colleague proposes bidding HK$9,000: below the HK$10,000 estimate, apparently leaving a cushion. No bid has been submitted; the auction team is checking the model of the rival’s bid before the deadline.

## Evidence

| Opening information | Supplied assumption |
|---|---|
| Net resale value after your inspection | HK$8,000 or HK$12,000; each probability 1/2 |
| Expected net resale value | HK$10,000, before auction payment |
| Bid rules | HK$100 increments; own bid paid if highest; ties lost |

**Student question:** Would you provisionally endorse the HK$9,000 bid or set a different bidding instruction? Explain why a bid below HK$10,000 may still be unsafe, and identify what you need to know about winning.

## Round two

The completed classroom model links the lot’s common value to the rival’s information and bid. There are exactly two states after your inspection, each with probability one half. In the low-value state, net resale value is HK$8,000, the rival’s inspection estimate is HK$9,000 and its bid is HK$7,000. In the high-value state, net resale value is HK$12,000, the rival’s estimate is HK$13,000 and its bid is HK$11,000. Your own report remains HK$10,000 in either state.

The table is the stipulated joint model, not inside information from a competitor or a recommendation to exchange bids. It describes possibilities before bidding; you do not observe which state occurs. Treat the rival’s stated bid rule as fixed for this one decision. It is not claimed to be an equilibrium or the rival’s optimal strategy. All auction rules, costs and probabilities remain unchanged. Choose one bid before the state is known; you cannot select a different bid after winning.

**Student question:** Choose one bid, or abstain, under this model. Compare HK$7,100, HK$9,000 and HK$11,100, including zero when you lose. What does winning with HK$9,000 reveal about value?

## Winning selects a state

Before learning the outcome, expected value is (HK$8,000 + HK$12,000) ÷ 2 = HK$10,000. But a HK$9,000 bid wins only when the rival bids HK$7,000, which in this model occurs only in the HK$8,000 state. Conditional on that bid winning, value is HK$8,000, not HK$10,000.

The winner then pays HK$9,000 for HK$8,000 net resale value: a HK$1,000 loss. The other state yields no purchase and zero. Expected surplus is therefore −HK$500. Multiplying a supposed HK$1,000 cushion by a one-half chance of winning would give the wrong sign because it treats value and winning as unrelated.

## Compare complete outcomes

At HK$7,100, the low state wins and yields HK$900; the high state loses and yields zero. Expected surplus is HK$450. At HK$9,000 the outcomes are −HK$1,000 and zero, averaging −HK$500. At HK$11,100 both states win: −HK$3,100 and +HK$900 average −HK$1,100. Abstaining gives zero.

Choose HK$7,100 under the stated objective. Any bid up to HK$7,000 loses both states, including the tie. From HK$7,100 through HK$11,000, only the low state is won and a higher payment only reduces surplus. From HK$11,100 upward both states are won, and even the cheapest such bid has negative expected surplus. This checks all permitted ranges, not just the three examples.

## Selection is not a universal discount

At the HK$9,000 proposal, your HK$10,000 estimate is above the rival’s HK$9,000 estimate precisely in the state you win. Competing estimates concern the same resale value, so beating a less optimistic bidder can be bad news about that value. A private-value auction, where your known benefit does not change with others’ information, is different.

The HK$7,100 answer is a best response to this supplied two-state rival rule, not a general strategy or a fixed percentage to subtract from every estimate. More bidders, different signals, reserves, bidding rules, costs or rival behaviour would require a new calculation. Rational adjustment can avoid a loss; winning an auction is not itself evidence of a curse.

## Instructor note

Allow 3 minutes for the provisional instruction, 4 to draw the two states and 4 to reconcile bid outcomes. Keep the reveal hidden during the first discussion. Reward identifying the missing connection between rival bids and value rather than requiring an exact opening bid from incomplete information.

After the reveal the expected-surplus criterion has a definite answer. Ask which rows survive when a particular bid wins. This is an original, deliberately small decision model, not an equilibrium derivation, investment recommendation or analysis of a GLD sale. All costs except payment are already deducted from value; do not deduct them twice. Do not encourage competitor information exchange.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The private stationery sale, two bidders, inspections, bid rules and values are fictional. All amounts are Hong Kong dollars. Conditional on your HK$10,000 inspection estimate, the lot has the same net resale value for either bidder: HK$8,000 or HK$12,000, each with probability one half. The rival estimates HK$9,000 or HK$13,000 and bids HK$7,000 or HK$11,000 respectively. This fixed rival rule is not claimed to be optimal or an equilibrium. Your bids use HK$100 increments and lose ties.

At HK$7,100, your low- and high-state surpluses are HK$900 and zero, giving HK$450 expected surplus. At HK$9,000, they are −HK$1,000 and zero, giving −HK$500. At HK$11,100, they are −HK$3,100 and HK$900, giving −HK$1,100. This is an illustrative conditional joint model, not a calibrated signal model or observed frequency. No real bid or auction action is proposed.

The Government Logistics Department’s service page and 2026 catalogue provide regional context only. They do not supply this sale’s rules, a particular lot date, results or a profit forecast. The five references comprise those two related official documents, the introduction and methods of an original 2008 experiment, an NSF researcher interview and a Stanford researcher discussion. They are not five independent empirical studies. Unavailable materials are not relied on. Unlike the earlier private-value auction-format case, this model makes winning informative about the common value. All references are optional; the classroom decisions require no external reading.

- [Government Logistics Department · Public auction service · checked 15 November 2026](https://www.gld.gov.hk/en/our-services/supplies/auction/). Describes auctioned government stores and availability of lists/terms. Next-date field did not render; no current auction date or rules inferred.
- [DATA.GOV.HK · GLD Auction List catalogue · 2026 entries](https://data.gov.hk/en-data/dataset/hk-gld-suppmgmt2-auction-list). Catalogue description and 2026 resource labels support regional surplus-sale context. Same GLD provider, not a second independent valuation study; individual lot data not used.
- [The value of victory: social origins of the winner’s curse in common value auctions · Judgment and Decision Making · October 2008](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/value-of-victory-social-origins-of-the-winners-curse-in-common-value-auctions/5DDB727F9F2E599C7BA90106F5AAC3C0). Original research introduction and method explain common-value selection and experimental bidding. Social-motivation findings are not generalised to these fictional traders; none of its numerical experiments copied.
- [NSF · Q&A with Paul Milgrom · 23 October 2020](https://www.nsf.gov/science-matters/greatest-auction-ever-qa-paul-milgrom-2020-nobel-laureate). Researcher interview explains the winner’s curse and information in auction prices. Qualitative reasoning, not a recommended bid or evidence about Hong Kong surplus lots.
- [Stanford Report · The bid picture · 19 November 2020](https://news.stanford.edu/stories/2020/11/bid-picture-nobel-prize-winners-explain-auction-theory-collaboration). Researcher discussion distinguishes common/private values and first-/second-price payment rules. Institutional explanatory reporting, not another empirical validation of this case.
