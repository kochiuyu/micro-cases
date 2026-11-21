# Online orders. A queue at the till?

<!-- legacy-case-id: 530 -->

OPS-44 · Hong Kong · 15 minutes · Shared capacity · Batching · Order fulfilment · Service constraints

![A Hong Kong grocer compares a shopping queue and a cart used for online orders.](../online-orders-at-a-busy-shop-scene.jpg)

## Online grocery can draw on stores and dedicated picking sites

The Hong Kong Census and Statistics Department reports online retail sales separately within its retail survey. Grocery fulfilment systems can coordinate manual picking in stores or dedicated sites. A store that promises both channels still has to decide which order its staff can do without delaying other customers.

## Opening decision

Ming runs a fictional Sha Tin grocer. One 30-minute block has 62 shoppers ready for checkout and 20 online orders due by its end. There is no opening backlog. If checkout assistants do no online work, the front team can complete 70 checkouts during the block.

Every batch of five online orders picked by the front team reduces checkout capacity by four. Unused capacity cannot carry forward. The backroom team can prepare up to 15 online orders at HK$2 each without affecting checkouts. Only front-team picks are batched; backroom and external orders can be assigned one by one.

Finish all online orders and serve every waiting shopper by the end of the block. Among feasible allocations choose the one with the lowest incremental cost. The front team’s normal wage adds no extra cost in this model.

## Evidence

| Preparation route | Minimum batch | Block constraint |
| --- | --- | --- |
| Front team | 5 orders | Each batch costs 4 checkouts |
| Backroom | 1 order | Up to 15 orders, HK$2 each |

**Student question:** How many online orders should Ming assign to each team? What visible constraint makes adding one more front-team batch a bad idea?

## Round two

A later block has 67 shoppers and 24 online orders. The same capacities apply. An outside depot with the same goods can complete up to 10 orders by deadline at HK$8 each, with no impact on in-store checkouts.

A trained relief cashier would restore capacity for four more checkouts in this block and costs HK$55. This does not change backroom or depot capacity. All other terms are unchanged.

**Student question:** How should Ming assign the orders in this busier block, with and without the relief cashier? Is the cashier worth HK$55, and at what fee would the two plans tie?

## Debrief · Allocate front-team batches within the spare capacity

With 62 shoppers, the base 70 allows eight checkouts’ worth of picking, or two batches. Front picks 10 and backroom covers 10 at HK$20. A third batch would leave only 58 checkouts for 62 shoppers.

## Debrief · A small increase can remove a whole batch

With 67 shoppers, one four-checkout batch would leave capacity 66. Assign zero online orders to the front, 15 to the backroom and nine to the depot. Incremental cost: 15 × 2 + 9 × 8 = HK$102.

## Debrief · Price the spare cashier against outside work

With relief, base checkout capacity becomes 74. One front batch leaves capacity 70; two leave 66. Assign five front, 15 backroom and four depot orders: HK$30 + HK$32 = HK$62 before relief. With the fee, total cost is HK$117. The plans tie at a HK$40 relief fee.

## Takeaway · Spare capacity is not interchangeable

Three unused checkout slots in the second block cannot support a four-slot batch. Reading only the total online backlog would miss the effect on the shopper queue. A real operator should measure arrivals within the block, not infer individual waits from this capacity rule.

## Instructor note

Allow 15 minutes: 3 to read the constraints, 4 for the first allocation, 5 for relief versus depot and 3 to explain the step change. Ask students to show the online and till totals for every plan.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The store, staffing arrangement, headcounts, fulfilment costs and capacities are fictional. This is a deterministic block model, not a forecast of actual waits.

- [Hong Kong Census and Statistics Department, Monthly Survey of Retail Sales, December 2025](https://www.censtatd.gov.hk/wbr/B1080003/B10800032025MM12/att/en/B10800032025MM12.pdf). Section 3 reports online retail value and distinguishes reporting channels; not fulfilment staffing data.
- [Ocado Group, In-Store Fulfilment](https://solutions.ocadogroup.com/en-us/technology/in-store-fulfillment). Supplier explains its manual picking workflows for stores and dark stores, not a capacity estimate.
- [Hong Kong Technology Venture, corporate operations overview](https://ir.hktv.com.hk/index.html). Operator describes batching identical goods across orders and sorting them back into individual orders.
- [Hong Kong Technology Venture annual report 2024, Management Discussion and Analysis](https://ir.hktv.com.hk/uploads/1745398482903-EW01137-AR24.pdf). Lists warehousing/logistics and pickup within reported fulfilment activities, not the specific classroom rates.
- [foodpanda, Wellcome and Market Place partnership announcement](https://www.foodpanda.com/newsroom/wellcome-and-market-place-are-now-on-foodpanda-hong-kong/). First-party historical example of branded Hong Kong grocery delivery and store pickup; the case invents its own fulfilment arrangement.
