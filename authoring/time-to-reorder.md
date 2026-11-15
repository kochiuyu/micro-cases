# Plenty on the shelf. Time to reorder?

<!-- legacy-case-id: 124 -->

OPS-11 · Hong Kong · 10–15 minutes · Operations · Reorder points · Inventory position

![Two stationery-wholesaler colleagues discuss shelves of adhesive-label packs while the manager holds an inventory clipboard.](../time-to-reorder-scene.jpg)

## Hong Kong context · Seeing goods on the way

On 16 January 2026, Hong Kong’s Transport and Logistics Bureau announced the formal rollout of its Port Community System, describing connected cargo tracking across transport networks.

Visibility is useful only when it informs a decision. The stationery wholesaler below is fictional; its demand, deliveries and rules are invented, not findings about the system.

## Opening decision

At closing time, a small stationery wholesaler has **140 usable packs of standard adhesive labels**. The manager normally waits until the shelf reaches 100 packs before ordering. A colleague asks whether that leaves enough stock while a delivery is on its way.

The worked plan uses exactly 20 packs each business day. The recorded lead time is five complete business days after an order is placed at closing time, with replenishment ready for use after those days’ consumption. Management wants 40 packs remaining just before a replenishment arrives.

Every new order is the usual 200-pack lot. Funding and storage permit it; this discussion is about *when* to order, not the lot size. Stock is reviewed at each day’s close. Before authorising any order, the manager will confirm the supplier’s dates and outstanding purchase orders.

## Evidence

| Opening record | Quantity or timing |
|---|---|
| Usable packs on the shelf | 140 |
| Daily use in the worked plan | 20 packs per business day |
| Recorded lead time for a new order | 5 complete business days |
| Management’s chosen safety buffer | 40 packs |
| Fixed replenishment lot | 200 packs |

**Student question:** Provisionally order the usual 200 packs now, or wait until the shelf reaches 100? Explain the trigger and what you must check before sending the order.

## Round two

The checks change two entries. An existing **120-pack order will be ready for use tomorrow morning, before any consumption**. Separately, the supplier confirms that a **new order now takes ten complete business days** after placement. The dispatched 120-pack delivery is unaffected.

There are no other receipts, backorders or reserved customer commitments beyond the stated daily use. For the worked trace, use the confirmed dates and exactly 20 packs per business day. These are scenario assumptions, not a real-world delivery guarantee. No emergency supply option is available in this decision.

Keep the same 40-pack buffer and 200-pack lot. Use a trigger of **lead-time demand + safety buffer**, applied to **inventory position: usable on-hand stock + confirmed on-order stock**. Reorder when that position is at or below the trigger. Also check that each receipt arrives before it is needed.

**Student question:** Does the longer lead time mean ordering today? Use the confirmed delivery to set the next order time, and show the stock expected just before that new order arrives.

## A trigger is not an order quantity

With the opening five-day lead time, lead-time demand is 20 × 5 = 100 packs. Add the agreed 40-pack buffer: the trigger is **140 packs**. With no outstanding supply, the opening record would justify ordering now.

Waiting until 100 would leave 100 − 100 = zero immediately before replenishment in this exact-demand example, rather than management’s intended 40. That is not proof of an inevitable stock-out in practice. The 200-pack lot answers a different question: how much arrives after an order is triggered.

## Count supply once, not twice

The new ten-day lead time raises the trigger to 20 × 10 + 40 = **240 packs**. Current inventory position is 140 on hand + 120 on order = **260 packs**. It is above the trigger, so another order today is not yet called for by the stated rule.

Tomorrow’s receipt moves 120 packs from “on order” to “on hand”. It does not add 120 to inventory position a second time. After tomorrow’s 20 packs are used, both on-hand stock and position are 240. Order the usual 200 at that closing-time check; position then rises to 440, while the shelf still holds 240.

## Check the dates as well as the total

| Moment | On hand | On order | Position |
| --- | --- | --- | --- |
| Now, before a new order | 140 | 120 | 260 |
| Tomorrow morning, existing receipt arrives | 260 | 0 | 260 |
| Tomorrow close, after 20 used | 240 | 0 | 240 |
| Immediately after ordering 200 | 240 | 200 | 440 |
| After the following 10 days’ use, before receipt | 40 | 200 | 240 |
| New receipt arrives | 240 | 0 | 240 |

The 140 currently available packs bridge the wait until tomorrow morning. The next 240 cover ten further days’ use of 200 packs, leaving 40 before receipt. A distant or uncertain inbound order could not be treated as immediately usable simply because it raises the position.

## Keep the policy honest

This is a transparent calculation under an agreed policy, not an optimisation of inventory cost or customer service. Management might choose a different buffer, but no probability distribution, shortage cost or service target is supplied to calculate one.

Maintain separate on-hand and outstanding-order records, check promised usable dates, and update lead-time assumptions. Unexpected demand, rejected goods or a changed delivery date can invalidate the trace. A visibility system does not remove that judgement.

## Instructor note

Allow a first vote before showing the purchase-order check. Ask students to distinguish the shelf threshold, lead-time demand, safety buffer and order lot. In round two, ask one pair to calculate the trigger and another to draw the dated stock path.

The longer lead time pushes the trigger upward; the confirmed inbound order raises the position. Their combined effect is to order tomorrow at closing, not to double-order today. At the end of the trace the position is again at the trigger, so the continuing policy would assess another lot; the exhibit is not the end of all future replenishment.

Unlike OPS-01’s launch-quantity inference, this case assumes an established repeat-use product and asks when to reorder. Do not claim the stipulated 40-pack buffer guarantees availability. The local announcement supplies context, not evidence for any classroom number.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional replenishment example. No claim that the wholesaler uses Hong Kong’s Port Community System. All quantities, exact daily demand, receipt dates, fixed lot and management’s 40-pack buffer are invented. The buffer is stipulated, not estimated from a service target. Orders are reviewed at closing time; lead time runs through the stated number of complete subsequent business days. The already-dispatched receipt arrives before tomorrow’s demand. No other allocations, backorders, supply or emergency order option is available. The scalar position calculation is accompanied by a dated availability check. Real demand or delivery changes require replanning. Source bodies and arithmetic were independently reviewed on 15 November 2026; this is not evidence of classroom learning outcomes.

- [Transport and Logistics Bureau, 16 January 2026: smart, green and modern logistics measures](https://www.info.gov.hk/gia/general/202601/16/P2026011600420p.htm). The announcement and Port Community System paragraphs provide dated local cargo-visibility context, not evidence about the fictional wholesaler or its lead times.
- [Oracle Inventory Help: Reorder Point Planning](https://docs.oracle.com/cd/A60725_05/html/comnls/us/inv/roplan.htm). Historical product documentation explains lead-time demand, safety stock and planned receipts. Product-specific implementation and economic-order-quantity examples are not adopted as an optimal policy for this firm.
- [Microsoft Learn: Handling reordering policies](https://learn.microsoft.com/en-ca/dynamics365/business-central/design-details-handling-reordering-policies). The reorder-point and projected-inventory sections support examining dated supply and demand. The case does not reproduce Business Central’s full time-bucket or reservation logic.
- [Global Logistics Cluster: Managing Inventory Levels](https://log.logcluster.org/en/managing-inventory-levels). The substantive order-cycle and inventory-component guidance distinguishes on-hand, ordered and committed goods. Humanitarian examples are not evidence of commercial demand. Its terminology separates ordinary lead-time stock from extra safety stock.
- [Virginia Cooperative Extension: Lean Inventory Management in the Wood Products Industry](https://www.pubs.ext.vt.edu/420/420-148/420-148.html). The definitions and reorder-point equation provide teaching background; first published May 2021, page states reviewed May 2026. The wood-industry figures, later optimisation examples and results are not used here.
