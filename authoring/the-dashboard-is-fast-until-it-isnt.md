# The dashboard is fast. Until it isn’t.

<!-- legacy-case-id: 545 -->

IS-45 · Hong Kong · 15 minutes · Tail latency · Caching and freshness · Load replay · Service targets

![At a venue service desk, two staff compare a printout with a screen beside an outdoor market.](../the-dashboard-is-fast-until-it-isnt-scene.jpg)

## Average speed can hide slow requests

Google’s site reliability engineering handbook explains that an average can hide a slow tail. The HTTP caching standard separately distinguishes freshness from age and explains when stored responses need validation. The platform, replay and targets below are fictional.

## Opening decision

A Hong Kong venue operator tests a public market dashboard before a weekend launch. Most requests show stable event details; some ask for current stock at the venue’s merchandise stand. The test contains no customer data and makes no real booking. Jam, the technology lead, wants the cheapest option meeting both targets.

On each 100-request replay, the 95th-percentile time is the 95th observation from fastest to slowest. It must be at most 300 ms. At most 5% of inventory responses may show a superseded count when checked against the recorded source at the time of response. No more than HK$180 per day is available.

Extra capacity serves requests from the authoritative service. Long cache reuses responses for both request types; bounded cache limits reuse and checks fast-changing inventory more often. The table groups exact response times, not ranges. Initially 20 out of 100 requests ask for inventory.

## Evidence

| Option and daily cost | 100 ms | 250 ms | 260 ms | 450 ms | Wrong inventory |
| --- | --- | --- | --- | --- | --- |
| Extra capacity — HK$180 | 0 | 96 | 0 | 4 | 0 |
| Long cache — HK$90 | 96 | 0 | 0 | 4 | 6 |
| Bounded cache — HK$120 | 90 | 0 | 6 | 4 | 1 |

**Student question:** Compute each option’s 95th-percentile time and incorrect inventory rate. Which option meets both targets at the lowest daily cost?

## Round two

At a second replay there are 40 inventory requests, still 100 total. Extra capacity remains at 96 requests at 250 ms and 4 at 450 ms with no incorrect inventory. Long cache still records 96 at 100 ms and 4 at 450 ms, but now shows ten incorrect inventory counts.

Bounded cache now records 86 responses at 100 ms, 8 at 260 ms and 6 at 450 ms. Two of its inventory counts are incorrect. The targets and quotes are unchanged.

**Student question:** Which option would you approve for the revised mix? Explain why both the average time and the cache-hit count can be misleading release checks.

## Debrief · Sort the times

Initially the 95th value is 250 ms for extra capacity, 100 ms for long cache and 260 ms for bounded cache. All three meet the time target. Use the number of requests that actually ask for stock as the accuracy denominator.

## Debrief · Check the right denominator

Inventory errors are 0/20 = 0%, 6/20 = 30% and 1/20 = 5%, respectively. Bounded cache meets both targets at HK$120, cheaper than the HK$180 capacity option. Long cache’s lower cost does not make it eligible.

## Debrief · Test the revised mix

Bounded cache serves only 86 + 8 = 94 requests at 260 ms or faster. The 95th is now 450 ms, even though 2/40 = 5% passes the accuracy target. Long cache still passes speed but 10/40 = 25% fails accuracy. Extra capacity is the only option passing both and exactly spends the budget.

## Debrief · Match the test to the service promise

Bounded cache’s new mean is (86 × 100 + 8 × 260 + 6 × 450) ÷ 100 = 133.8 ms, well below 300 ms. That does not meet a percentile target. A cached response may also be quick and outdated. Report percentiles and validated wrong-response rates by request type across representative load.

## Instructor note

Allow five minutes to count cumulative positions, four to check the two denominators and six to replay and explain. Ask what changes at exactly 95 responses within the threshold. No particular vendor, configuration or production rollout is recommended.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All load, counts, costs, stale-response and timing values are stipulated. “Wrong inventory” means disagreeing with the recorded authoritative count at response time, not simply old by age. No real site, endpoints or credentials are used.

- [Google SRE, Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/). Distinguishes latency distributions from average and shows the point of bucket counts.
- [Google SRE Workbook, Monitoring](https://sre.google/workbook/monitoring/). Explains how tracking the 95th and 99th percentiles detects slow tails.
- [RFC Editor, HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111.html). Section 4.2 distinguishes freshness lifetime and age. The exercise does not prescribe HTTP headers.
- [Cloudflare, Retention vs Freshness](https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/). Distinguishes stored object retention, expiration and revalidation.
- [Cloudflare, Cache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance/). Defines cache ratio and separates hits, misses and expired data paths. A hit is not an inventory correctness test.
