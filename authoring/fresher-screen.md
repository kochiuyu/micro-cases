# A fresher screen. A better decision?

<!-- legacy-case-id: 104 -->

IS-09 · Hong Kong · 10–15 minutes · Information systems · Data freshness · Decision windows

![Two colleagues discuss a laptop at a decorative-prop studio counter, with ceramic vases, artificial floral stands and a clock nearby.](../fresher-screen-scene.jpg)

## In the news

In a reply on 11 June 2025, Hong Kong’s Government described parking-meter sensors providing occupancy information to support follow-up on unpaid occupied spaces.

This is historical context for timely information, not a guarantee of availability or an evaluation of the unrelated fictional rental studio below.

## Opening decision

Fictional classroom situation. A Hong Kong decorative-prop studio rents vases, tabletop displays and artificial-flower stands for photo shoots. Enquiry staff use an internal dashboard to shortlist suitable items across two storage rooms.

The dashboard is read-only. Before promising an item, staff check and reserve it in the authoritative booking system in one controlled step, preventing it from being promised twice. This confirmation process is staffed and funded under both proposals; customers cannot reserve through the dashboard.

Cancellations and new reservations change availability during the day. The owner must choose a dashboard service level for the next three months. The studio serves advance enquiries and occasional same-day requests, but has no forecast of additional rentals from faster updates.

## Evidence

| Service level | Dashboard information | Monthly incremental cost |
|---|---|---:|
| A · Daily snapshot | Accurate at 7am each business day | HK$600 |
| B · Intraday updates | Source changes normally arrive within five minutes | HK$1,800 |

Both complete quotes include support and monitoring. Setup effort is comparable and affordable. Staff and agreed hours remain unchanged. Each display shows source-update times and that it is not a reservation.

A missed scheduled update produces a stale/unavailable status; staff then use the established booking-system route. Five-minute updating is neither instantaneous nor guaranteed available. Safety and payment checks remain.

**Student question:** Would you pay HK$1,200 more each month for intraday updates, or choose the daily snapshot? Make a provisional choice and name the specific customer action for which freshness would matter.

## Round two

The team reviews three recent enquiries in this fictional studio. These are selected workflow traces, not a random sample or a monthly sales forecast.

Tuesday: a decorative stand became free after a 9:10am cancellation. At 9:30am a customer wanted that type for noon collection. Staff had time to act, but the 7am shortlist omitted it and they did not search that item in the booking system.

Thursday: a matching item became free at 10am, but the customer needed it next week. Staff had time to use their ordinary confirmation workflow; no imminent collection deadline applied.

Friday: an item became free at 11am for a noon request, but the only colleague able to arrange collection was occupied until after noon.

Under B’s normal update timing, Tuesday’s change would appear by about 9:15am, before the enquiry. That creates a usable lead, not a completed sale: suitability, the customer’s choice and the binding reservation still need confirmation.

**Student question:** Which enquiries could a fresher shortlist realistically help, and why? Would you now choose A or B? State the action window, the confirmation step and one piece of evidence that would reverse your choice.

## Tuesday has a usable window, not a guaranteed rental

The cancellation precedes the enquiry by 20 minutes. With B operating normally, the change could be visible around 9:15am, 15 minutes before the request. Staff have time to arrange noon collection.

They could now shortlist the stand and attempt the current booking-system reservation. Someone else might already have reserved it, suitability might fail or the customer might decline. The trace supports a plausible benefit from timely discovery, not one certain extra rental.

## Thursday and Friday expose different limits

Thursday’s next-week request leaves time for the ordinary workflow. Earlier visibility might still be convenient, but this trace does not establish an urgent opportunity that requires B.

Friday’s display is not the only constraint: no authorised collection colleague is available before noon. A faster update alone cannot make that request feasible. Paying for B does not add collection capacity.

## Follow the information all the way to action

For this studio, the useful chain is: an item becomes free → the dashboard updates → staff notice it during an enquiry → collection can be arranged → the current reservation is confirmed.

A recent timestamp only addresses part of that chain. The controlled booking step remains essential even when the screen has just refreshed. More frequent updates are not permission to promise directly from the shortlist.

Both services display their limitations. A clearly dated snapshot is not dishonest; B’s fresh-looking screen is not a booking guarantee. Missed updates trigger the established fallback, not guessed availability.

## Choose the service standard the business will support

B costs HK$1,200 extra each month, or HK$3,600 over three months. It is defensible if timely same-day enquiries are an important service and usable opportunities justify that cost. A remains defensible if advance enquiries dominate or the extra value is too small.

The three traces supply no frequency, conversion rate or incremental contribution. Do not turn Tuesday into a monthly profit forecast or invent a break-even number of rentals. Seek evidence about how often matching changes arrive in time and whether staff can act on them.

Manual refreshes or a different service level could be assessed separately, with their workload and price. They are not free alternatives already supplied by these quotes.

## Instructor note

Take a first vote before showing the traces. Ask each group to identify a specific action deadline rather than saying “real-time is always better”. On the reveal, distinguish discovery, collection feasibility and confirmed reservation.

Require a provisional three-month choice and reversal evidence. Tuesday is a possible usable window; Thursday lacks urgency; Friday lacks acting capacity. These distinctions are not statistical estimates or proof of sales uplift.

This is data freshness for current decisions, not retrospective forecast leakage, recovery time or semantic accuracy. The funded booking process is unchanged under both options, including its controlled availability-and-reservation step. Direct customer booking would need a different transaction design, not merely a faster display.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The studio, traces, prices, update service levels and staffing assumptions are original fiction. A is accurate at the daily 7am snapshot, not guaranteed current all day. B normally delivers source changes within five minutes, not instantly or with guaranteed uptime. Both quotes include support/monitoring; setup is comparable, and the existing staffed authoritative availability-and-reservation step remains funded under both. There is no double-promising permission, new customer reservation interface, relaxed safety check or additional working-hours assumption. Tuesday 9:10 plus five minutes gives about 9:15, before the 9:30 enquiry; its noon collection is feasible but no additional rental is certain. Thursday is not an urgent deadline; Friday lacks the available collection colleague. The three selected traces are not a representative sample, forecast, conversion rate or causal estimate. Price difference is HK$1,200 monthly/HK$3,600 for three months; no incremental contribution or break-even count is supplied. Five primary institutional documents were read by researcher and implementer; relevant sections only, not five empirical studies or validation of the fictional software. No code, schemas, tables or source illustrations are copied. Sources checked 14 November 2026.

1. [Hong Kong Government · LCQ1: On-street parking spaces · 11 June 2025](https://www.info.gov.hk/gia/general/202506/11/P2025061100221.htm) — Historical sensor-information context. No enforcement rule, accuracy guarantee or later pilot completion is inferred.
2. [Hong Kong Transport Department · Parking Vacancy Data Specification · version 1.9, April 2026](https://static.data.gov.hk/td/parking-vacancy/dataspec/TD_Parking_Vacancy_Data_Specification.pdf) — Online-vacancy fields distinguish timestamps and unavailable data. Technical documentation, not a reservation promise; no schema or sample data reused.
3. [UK Government · Government Data Quality Framework: guidance · 3 December 2020](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework-guidance) — Relevant timeliness, metadata and limitations sections. Timing should suit intended use; institutional guidance is not a measured benefit or Hong Kong legal requirement.
4. [Microsoft Learn · Data integration patterns for Microsoft industry clouds](https://learn.microsoft.com/en-us/industry/well-architected/cross-industry/data-integration-patterns) — Relevant integration, system-of-record and error-handling passages. Product-specific architecture guidance, not a recommendation or guarantee of this fictional service level.
5. [W3C · Data on the Web Best Practices · Recommendation](https://www.w3.org/TR/dwbp/) — Best Practices 20–21 on update timing and testing, plus metadata context. No source examples or code reproduced; not a rental-system certification.
