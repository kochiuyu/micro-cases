# The server is cheaper. Is the bill?

<!-- legacy-case-id: 566 -->

IS-47 · Hong Kong · 15 minutes · Cloud billing · Usage metering · Cost sensitivity

![Two print lab staff compare a paper invoice and print samples beside a computer monitor.](../the-server-is-cheaper-the-bill-is-not-scene.jpg)

## A cloud bill has more than one meter

Google Cloud’s Cloud Run documentation distinguishes charges for several kinds of resource use. AWS publishes separate request and duration factors for Lambda, and documents commitments separately. A Hong Kong photo-printing lab has two imaginary offers with invented HK-dollar rates, not provider quotations.

## Opening decision

Two offers support identical file retention, peak throughput, customer response time and service quality. Flex bills requests and CPU time separately. Reserved charges a monthly block including all compute and requests at either workload shown. The minimum lasts one month. The lab must choose one offer at the same next monthly renewal, not pay a switching penalty.

An initial metering rehearsal shows 2 million invocations, 100,000 CPU-seconds, 300 GB sent out to customers and 50 GB-month of storage. Billable units already account for any rounding. Both options use identical volumes; different network tariffs are part of the quotes. Assume no taxes, credits, support charges, penalties, or other costs.

## Evidence

| Monthly bill item | Flex | Reserved |
| --- | --- | --- |
| Invocations | HK$80 / million | Included |
| CPU time | HK$0.0015 / CPU-second | Included |
| Flat block | None | HK$650 |
| Outbound transfer | HK$1.20 / GB | HK$0.30 / GB |
| Storage | HK$0.60 / GB-month | HK$0.60 / GB-month |

**Student question:** Which plan would you recommend using the first full metering rehearsal? Compute the total bill for each and explain how outbound transfer changes the compute-only price gap.

## Round two

The same pre-renewal test now includes retries after a temporary internal queue interruption. The full monthly forecast grows to 2.5 million invocations and 180,000 CPU-seconds, with no extra outbound bytes or retained storage. The jobs are replayed internally, and the Reserved block still covers the full load.

**Student question:** Does your choice change? With 2.5 million calls and the same transfer and storage, how many total CPU-seconds would make the two plans tie?

## Read the complete quote

First Flex costs 160 + 150 + 360 + 30 = HK$700. Reserved costs 650 + 90 + 30 = HK$770. Flex still wins by HK$70, but outbound transfer reduces its compute-and-request advantage from HK$340 to HK$70.

## Reprice the changed units

With replays, Flex costs 200 + 270 + 360 + 30 = HK$860. Reserved remains HK$770, so Reserved now saves HK$90. The extra HK$160 on Flex combines HK$40 for more invocations and HK$120 for CPU.

## Break-even usage

At 2.5 million invocations, Flex’s non-CPU bill is HK$590. The HK$180 gap to the HK$770 Reserved total buys 120,000 CPU-seconds at HK$0.0015 per second. Below that Flex wins and above it Reserved wins, subject to the block still covering the load.

## Instructor note

Ask why a flat compute estimate and a dashboard showing unique customer orders miss the same problem in different ways. Have students request one billing extract with unit, quantity and rate for each meter and verify the month and network route match the comparison.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All quoted rates and offers are fictional and not product advice. No price shopping is required.

- [Google Cloud, Cloud Run pricing](https://cloud.google.com/run/pricing). Explains distinct metered resource charges and billing granularity; not the exercise’s quote.
- [AWS, Lambda pricing](https://aws.amazon.com/lambda/pricing/). Request loads and duration are separately described, with additional network/data transfer terms where relevant.
- [Google Cloud, billing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). Standard and detailed export bodies describe usage, SKU, cost, currency and resource-level fields.
- [AWS, how Savings Plans apply](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html). Examples distinguish commitments and uncovered on-demand usage; neither equals the fictional flat block.
- [Google Cloud, invoice cost details](https://docs.cloud.google.com/billing/docs/how-to/cost-table). Cost table provides invoice-period itemization and CSV, useful for reconciling usage estimates to a statement.
