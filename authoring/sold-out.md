# Sold out by noon. Double tomorrow?

Case 17 · Hong Kong · 10–15 minutes · Demand forecasting · Inventory

![A kiosk owner holds an empty tray while a colleague considers tomorrow’s order](../sold-out-scene.jpg)

## In the news

Hong Kong’s McGriddles launch drew queues in July 2024. On 29 July, McDonald’s said it had sold one million units, would end its app trial early as stock ran out, and would return on 5 August during breakfast hours. A sell-out is exciting. But how much does a launch day tell a manager about tomorrow’s order?

## Opening decision

You run a fictional independent Hong Kong breakfast kiosk, not a McDonald’s branch. Your new sandwich sold all 100 portions by noon today. Customers still approached the counter, but staff did not record how many wanted that sandwich rather than other products. Your supplier needs tomorrow’s order now.

You can order kits for either 100 or 200 sandwiches. Delivery is before opening; there is no same-day replenishment. Each kit costs HK$20 and each sandwich sells for HK$35. Unsold kits have no usable or resale value after tomorrow. Labour and other overheads do not change between the two choices. You can afford either order.

## Evidence

Tomorrow’s contribution · HK$ · invented scenarios

| Order | Demand: 100 | Demand: 200 |
|---|---|---|
| 100 kits | 1,500 | 1,500 |
| 200 kits | −500 | 3,000 |

Contribution = sales revenue minus cost of every kit ordered. Sales cannot exceed stock. Compare only demand of 100 and 200; neither is a forecast and probabilities are not supplied.

**Student question:** Order 100 or 200 for tomorrow? State the demand you are expecting and one reason not to trust today’s sales total.

## Round two

The cashier checks the wristband tally kept during the event: 80 of today’s 100 sandwiches were bought by visitors wearing wristbands for a nearby one-day event. The event will not run tomorrow. The price was the same for everyone. No other assumption changes.

You do not know whether those visitors will return independently, whether local customers were turned away, or how many people would have bought later if stock had remained.

**Student question:** Does this change your order? What extra observation would most help you decide before the supplier’s deadline?

## Debrief

Sales stopped at the stock limit; demand did not necessarily stop there. Selling 100 establishes at least 100 purchases today. It does not show that today’s full-day demand was exactly 100, nor that tomorrow’s will be 200. A queue alone does not count customers who wanted this product and would have paid its price.

Compare the downside and the upside. If demand is 100, doubling the order lowers contribution from HK$1,500 to −HK$500: a HK$2,000 loss relative to the smaller order. If demand is 200, doubling raises contribution from HK$1,500 to HK$3,000: a HK$1,500 gain. The larger order is not justified merely because yesterday sold out.

The event is a reason to revise a forecast, not a new forecast by itself. Removing 80 event purchases from 100 sales leaves 20 observed non-event purchases. It does not prove tomorrow’s demand will be 20: regular customers may have been unable to buy, and some visitors may return. The reveal weakens a simple “repeat today, then double” argument without uniquely determining the correct quantity.

Before the deadline, check paid pre-orders, enquiries specifically for the sandwich, comparable non-event days, and whether tomorrow has a similar demand driver. State the limits of each measure. If you choose 100, explain the missed-sales risk you accept. If you choose 200, explain why you expect enough repeat demand to justify the waste risk.

## Optional calculation

For a manager comparing expected contribution in this two-scenario model, let p be the probability that demand is 200. Ordering 200 yields p × 3,000 + (1 − p) × (−500). Ordering 100 yields 1,500 in either scenario. The larger order wins only when 3,500p − 500 > 1,500, or p > 4/7 (about 57%). At 4/7 the choices tie.

This threshold is calculated from the invented prices and scenarios. The news reports and the event wristbands do not supply p. Different demand possibilities, salvage value, customer-retention effects or risk preferences could change the decision.

## Back to the news

HK01 reported queues and some lunchtime stockouts on 27 July 2024, then lighter traffic at one Tsuen Wan branch the next day. That single-branch observation is not a chain-wide demand estimate. The company’s later announcement also changed availability from the trial’s all-day offer to breakfast hours. Comparing sales across those periods without accounting for selling hours would mix different conditions.

The news motivates the forecasting question. It does not establish that McDonald’s used this kiosk’s costs, order rule or event mix, or deliberately created a shortage.

## Instructor note

Minutes 0–3: show the opening and payoff table; take a vote. Ask one student on each side to name the risk they accept. Minutes 3–7: reveal the event tally and vote again. Minutes 7–12: compare the evidence students would collect and work through the optional threshold if appropriate.

Challenge “100 sold means 100 wanted” with the unrecorded turnaways. Challenge “80 visitors gone means only 20 tomorrow” with the same missing data. Ask 200-order supporters how strong their high-demand belief must be. Ask 100-order supporters what evidence would make them switch. There is no uniquely correct quantity without a forecast and an objective. For a later discussion, consider whether pre-orders or smaller, more frequent replenishment could change the trade-off; those options are not available under today’s fixed order rule.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The independent kiosk, 100/200 kit choices, HK$20 cost, HK$35 price, no salvage or replenishment, capacity and affordability assumptions, 80 event purchases and one-day event are fictional. Neither scenario probability is observed. Contribution excludes unchanged overheads and is not total business profit. The illustration depicts a fictional kiosk, not the reported company. No deliberate-scarcity motive is asserted.

1. [McDonald’s Hong Kong, launch announcement, 24 July 2024](https://www.mcdonalds.com.hk/wp-content/uploads/2024/07/2024-07-24_McDonalds-McGriddles-Launch-Press-Release_FINAL_Website-1.pdf) — Original planned app trial and all-day availability; a company announcement.
2. [McDonald’s Hong Kong, revised launch announcement, 29 July 2024](https://mcdonalds.com.hk/wp-content/uploads/2024/07/2024-07-29_McDonalds-McGriddles-Returns-on-Aug-5_FINAL_Website.pdf) — Company-reported one million sales, early trial ending and breakfast-only return on 5 August. Distinct from the earlier plan, not independent verification of sales.
3. [HK01, launch-day reporting, 27 July 2024](https://www.hk01.com/社會新聞/1042155/麥當勞mcgriddles首賣-多區大排長龍-新蒲崗分店要等逾一小時) — Reports queues, ordering difficulties and some branch stockouts. Does not measure total unmet demand.
4. [HK01, Tsuen Wan follow-up, 28 July 2024](https://www.hk01.com/社會新聞/1042385/麥當勞mcgriddles-荃灣店人潮減少-食客食足兩日-未來數日再食) — Reports lighter traffic at one branch the next day; a local observation, not a general demand forecast.
5. [Marketing-Interactive, McGriddles launch interview, 2024](https://www.marketing-interactive.com/how-mcdonald-s-hk-s-mcgriddles-rely-on-word-of-mouth-to-cause-buzz) — Company interview on the campaign, launch timing and early trial ending. Promotional perspective is distinguished from independent demand measurement.
