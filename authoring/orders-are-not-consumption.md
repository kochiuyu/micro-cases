# Customer demand moved a little. Orders moved a lot.

<!-- legacy-case-id: 208 -->

OPS-18 · Hong Kong · 10–15 minutes · Bullwhip effect · Order batching · Demand visibility

![Two distributor colleagues discuss a plain clipboard beside a reusable storage box.](../orders-are-not-consumption-scene.jpg)

## Visibility across a logistics chain

Hong Kong’s Transport and Logistics Bureau announced the formal rollout of the Port Community System on 16 January 2026, including cargo tracking across transport networks. Seeing cargo movements is not the same as knowing final customer demand. Our fictional distributor explores that distinction; no ordering failure or measured improvement is attributed to the public system.

## Opening decision

A fictional Hong Kong distributor supplies one homeware retailer with a standard reusable storage box. Every quantity below is an individual box: product codes, units and records are correct. The retailer’s last four weekly orders were 0, 200, 0 and 300. The distributor sees the latest increase and must choose its future planning routine, not whether to honour a confirmed order. All accepted commitments can and will be fulfilled under either routine.

A continues using incoming order changes as the main signal for its internal capacity forecast. This is fast and closely reflects the requests it must serve. B introduces a weekly bilateral review of retailer sales, stock, outstanding orders and delivery dates before changing that forecast. B takes two funded staff hours weekly, displacing a nonurgent catalogue refresh; it is not a free information exercise. No extra stock purchase or capacity booking is authorised by choosing B.

The retailer has voluntarily agreed to this limited planning exchange. Only necessary product-level quantities and dates are shared with authorised staff for this supply relationship, not personal records, rival retailers’ data or resale-pricing plans. Commercial protections, secure access and independent pricing remain intact. Forecasts do not cancel orders or change contracts. Neither routine shortens the agreed next-week delivery schedule.

## Evidence

| Week | Retailer order, boxes |
|---|---:|
| 1 | 0 |
| 2 | 200 |
| 3 | 0 |
| 4 | 300 |

**Student question:** Which planning routine would you choose, and what would have to be true before treating the 300-box order as a new weekly level of consumer demand?

## Round two

The retailer provides this reconciled timeline. It began week 1 with 250 boxes on hand and no outstanding orders. Orders placed at the end of a week arrive at the start of the next week. There were no returns, losses, cancellations or stockouts, so recorded consumer sales equal the supplied demand for these four weeks. Closing stock = opening stock + receipts − consumer sales.

| Week | Consumer sales | Retailer orders | Receipts | Closing stock |
| --- | --- | --- | --- | --- |
| 1 | 100 | 0 | 0 | 150 |
| 2 | 110 | 200 | 0 | 40 |
| 3 | 90 | 0 | 200 | 150 |
| 4 | 100 | 300 | 0 | 50 |

The retailer normally batches orders every second week to save administrative work. Its week-2 order was 200 boxes. Week 4 had a temporary wholesale discount that the retailer chose to use: it ordered its planned 200 boxes plus 100 for later weeks. Its customer-facing price and promotion did not change. The week-4 order is a genuine commitment, with all 300 due in week 5, not an error or a fictitious purchase.

At the end of week 4, 50 boxes are on hand and 300 are already inbound. Future consumer demand is unknown. The discount and two-week ordering practice remain unless the parties separately agree changes; access to a sales file does not remove either incentive. No minimum stock target, future probability or cost optimisation is supplied. Do not order another 300 merely because the existing 300 have not arrived yet.

**Student question:** How would you revise your interpretation and planning routine? Reconcile sales, orders and the pipeline, then name one cause of the swings that sharing data alone would not remove.

## Debrief: reconcile before reacting

Consumer sales total 400 boxes and average 100 per week, with a range from 90 to 110. Retailer orders total 500 and range from 0 to 300. This is a small illustrative timeline, not a statistical estimate for an industry. Orders are both real and much lumpier than consumption. An order-free week is not zero consumer demand; an order of 300 is not proof of sustained weekly sales of 300.

## Stock and pipeline explain the difference

The retailer ends with 50 on hand plus 300 inbound, or 350 committed boxes in total. It began with 250 and no pipeline: 250 + 500 ordered − 400 sold = 350. The additional 100 reflects forward buying in the supplied narrative. Received goods alone reconcile as 250 + 200 received − 400 sold = 50. Treating the inbound order as missing stock would count the same requirement twice.

## Visibility helps interpretation, not every policy

B is now more informative for separating sales from batching and forward buying, provided the review’s effort is worthwhile. It does not entitle the distributor to reject the 300-box order, assume future sales stay at 100, or dictate a retailer’s prices. Discussing smaller regular orders, processing costs or future discount design requires a separate lawful commercial agreement and a cost/service comparison. Delivery delay, incentives and capacity constraints can remain even with accurate data.

## Instructor note

Draw two lines for sales and orders, then add a separate inventory-and-pipeline bridge. The learning objective is amplification between stages despite accurate units and no stockout censoring. OPS-01 concerns a single sell-out; IS-05 concerns units; this case concerns ordering behaviour. No variance formula, optimal order quantity, public-system performance claim or real data-sharing action is required. All decision evidence is on the page.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All business data and behavioural explanations are original fiction. Week-2 order arrives in week 3; week-4 order arrives in week 5. Opening stock 250 plus receipts 200 minus sales 400 leaves 50. End-of-week 4 inventory position here is on-hand 50 plus inbound 300, with no backorders or reservations; it is not a recommended stock target. Historical demand range 20 versus order range 300 illustrates amplification without estimating a long-run bullwhip ratio. The agreed next-week delivery schedule and existing contractual commitments are preserved. Data exchange is bilateral, authorised and purpose-limited; no coordination of rival prices or markets is proposed.

- [Transport and Logistics Bureau: logistics measures and PCS rollout, 16 January 2026](https://www.tlb.gov.hk/eng/psp/pressreleases/transport/2026/20260119a.html). Official dated cargo-visibility context; the URL date differs from the event date stated in the body. No demand-forecasting outcome is claimed.
- [GS1 Hong Kong: response to PCS launch, 17 January 2026](https://www.prnewswire.com/apac/news-releases/gs1-hong-kong-welcomes-launch-of-port-community-system-advocates-global-data-standards-for-smarter-trade-and-logistics-302663913.html). Issuer statement about standards and traceability, not independent evidence of inventory savings. Same launch as the first source.
- [GS1: EPCIS, enabling visibility with real-time information on supply-chain events](https://www.gs1.org/sites/default/files/docs/epc/gs1_epcis_enabling_visibility.pdf). Event visibility and need-to-know access guidance; older brochure, not proof that visibility reveals final demand or removes incentives.
- [Lee, Padmanabhan and Whang: Information Distortion in a Supply Chain, 1997](https://courses.ie.bilkent.edu.tr/ie460/wp-content/uploads/sites/12/2019/02/Lee-Padmanabhan-Whang-1997-MS.pdf). Original research paper in a university-hosted copy; batching, price variation and demand-signal mechanisms. No numerical model or figure reproduced.
- [MIT Center for Transportation and Logistics: Beer Game Debrief, January 2025](https://ctl.mit.edu/sites/ctl.mit.edu/files/Rice%20-%20Beer%20Game%20Debrief%20Jan%207%202025%20EE%20v0%20san.pdf). Teaching discussion of delays, batching and incentives; related synthesis rather than an independent field estimate.
