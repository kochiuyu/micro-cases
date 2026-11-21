# Full terminal. Empty boxes in the wrong place?

<!-- legacy-case-id: 509 -->

OPS-42 · Hong Kong and Shenzhen · 15 minutes · Container repositioning · Scenario analysis · Expected cost · Network imbalance

![A container planner studies empty-box counts at two terminals while cranes and stacked containers are visible beyond the office.](../full-terminal-empty-boxes-scene.jpg)

## Hong Kong counts empty and loaded containers separately

Hong Kong’s official shipping statistics for the fourth quarter of 2025 recorded throughput of 3.32 million twenty-foot equivalent units, including 0.70 million empty units. The figures measure movement, not depot inventory available to exporters. Operators may reuse an empty box or move it for another booking.

## Opening decision

Nico plans empty-equipment moves for a fictional operator. Ten interchangeable empty 20-foot boxes are ready: eight at the Hong Kong terminal and two at the Shenzhen terminal. Each export booking tomorrow needs one box at its own terminal.

Tonight Nico can commit to moving up to three boxes from Hong Kong to Shenzhen for HK$80 each. A fourth move is available for HK$200 instead of HK$80 for that box. All booked moves arrive before the export cut-off and cannot be reversed.

Each booking left without a box costs HK$300 in Hong Kong or HK$800 in Shenzhen. Count those costs plus moving charges, and assume no further transfers, rental or future value of idle boxes in this one-day decision.

## Evidence

| Tomorrow’s plan | Hong Kong boxes needed | Shenzhen boxes needed |
| --- | --- | --- |
| Initial forecast | 6 | 4 |

**Student question:** If the forecast is certain, how many boxes should Nico move? Explain why ten boxes for ten bookings does not settle the decision.

## Round two

Just before tonight’s booking deadline, a shipper might switch some export bookings to Shenzhen. The current 6-and-4 split now has a 60% chance. There is a 40% chance that Hong Kong instead needs four and Shenzhen needs six. The total is ten either way.

The terminals will learn which split applies only after the move must be booked. The move cap, charges and per-booking shortage costs are unchanged.

**Student question:** Which transfer minimises expected cost across the two demand splits? What would happen to cost and service if Nico moved one fewer or one more?

## Debrief · Put boxes where orders are

The initial forecast is met by moving two boxes, leaving six in Hong Kong and four in Shenzhen, for HK$160. Moving fewer creates a Shenzhen shortage that costs HK$800 per booking. Moving extra creates a Hong Kong shortage and adds moving costs.

## Debrief · Moving two under uncertainty

Moving two costs HK$160. In the 6-and-4 split nothing is short. In the 4-and-6 split Shenzhen is short two boxes even though Hong Kong has two unused ones. Expected cost is 160 + 0.40 × 1,600 = HK$800.

## Debrief · Compare one more and then another

Moving three costs HK$240 and leaves five boxes at each terminal. It misses one Hong Kong booking in the 60% scenario and one Shenzhen booking in the 40% scenario. Expected cost is 240 + 0.60 × 300 + 0.40 × 800 = HK$740.

## Debrief · The fourth box has a higher price

Moving four costs HK$440 and leaves four Hong Kong boxes and six Shenzhen boxes. It misses two Hong Kong bookings in the 60% scenario and none in the 40% scenario, for expected cost 440 + 0.60 × 600 = HK$800.

## Debrief · Check all feasible choices

Zero moves cost HK$2,240 in expectation; one costs HK$1,520. Three moves give the lowest expected cost, although one booking is always missed. Two or four moves can serve every booking in one scenario, but each can leave two bookings short in the other.

## Instructor note

Allow 15 minutes: 3 to draw the two terminal inventories, 4 to solve the first decision, 5 to compare expected costs, and 3 to explain why the minimum-cost policy does not maximise the probability of serving every booking.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All company details, inventories, bookings, costs, probabilities and transfer terms are fictional. The sourced statistics concern historical port throughput and are not this case’s initial inventory.

- [Census and Statistics Department, Hong Kong Shipping Statistics, fourth quarter 2025](https://www.censtatd.gov.hk/wbr/B1020008/B10200082025QQ04/att/en/B10200082025QQ04.pdf). Reports 3.32 million TEUs total and 0.70 million empty TEUs in section 7; these are movements, not inventory.
- [Marine Department, Port and Maritime Statistics](https://www.mardep.gov.hk/en/materials-and-publications/publications/port-and-maritime-statistics/index.html). Official tables separate types of port throughput and link to definitions and limitations.
- [Yantian International Container Terminals, Shenzhen Hutchison Inland Container Depots](https://www.yict.com.cn/page/SHICD.html?locale=en_US). Operator describes Shenzhen warehousing and container-storage facilities and their links to local terminals.
- [Maersk, What is container turnaround?](https://www.maersk.com/support/faqs/2023/10/18/container-turnaround). Carrier describes returning an empty container to a specified location so it can be used again.
- [Maersk, Matchbox equipment reuse and exchange advisory](https://www.maersk.com/news/articles/2020/12/28/matchbox-exchange-instant-container-reuse-and-exchange-online-platform). Gives a real carrier example of alternatives to conventional empty-container returns in certain markets, not the case’s route or terms.
