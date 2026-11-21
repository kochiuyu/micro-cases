# When the feed goes blank, what should the board say?

<!-- legacy-case-id: 524 -->

IS-43 · Hong Kong · 15 minutes · Data freshness · Missing values · Service status · Fallback design

![A transport information controller checks a station display and route-status printout by a bus stop.](../when-the-bus-feed-goes-quiet-scene.jpg)

## A transit response contains more than an ETA

Hong Kong’s Digital Policy Office publishes bus estimated-arrival data from two operators through DATA.GOV.HK. Its data dictionary separates data-generation time from the predicted arrival time. Other public transit-feed specifications similarly distinguish measurement freshness from the prediction itself. The display rule below is fictional.

## Opening decision

A Hong Kong transport information team tests a digital bus board. It is 14:00:00. Every route is in the timetable; the board also receives a live snapshot. Retrieval succeeded for the exhibit. The team must decide which estimates to display and count how many routes have reliable live information.

Show a numeric live ETA only if it is present, its own observation is at most 90 seconds old, and the ETA is not before the current time. A fresh explicit confirmation of no running bus is a live status, not a numeric ETA. A blank prediction without that confirmation does not prove service has stopped.

When the live snapshot is fresh but a route has no usable information, show that route’s next scheduled time clearly labelled as schedule, not live. Count a qualifying ETA or verified no-service status as live coverage. Do not count a scheduled fallback.

## Evidence

| Route | Prediction | Observed | Explicit status | Schedule |
| --- | --- | --- | --- | --- |
| A | 14:05 | 13:59:15 | — | 14:07 |
| B | 14:06 | 13:58:20 | — | 14:08 |
| C | — | 13:59:40 | No bus running | 14:10 |
| D | — | — | — | 14:11 |

**Student question:** What should each route show, and what fraction of the four routes actually has reliable live information?

## Round two

At 14:01:30 all four event rows are still unchanged. The network check still gets a successful response, but the upstream snapshot timestamp, last updated at 13:59:50, is now 100 seconds old. No new service information is available.

If the upstream snapshot age exceeds 90 seconds, show a single live-feed-unavailable banner and suppress all its live ETAs and status messages. Use the schedules in the exhibit as labelled fallbacks until a fresh snapshot passes the route checks. All four scheduled times are still in the future.

**Student question:** Should the board keep any live messages or report four cancelled routes? What does it show instead, and which two monitoring signals should trigger separate alerts?

## Debrief · Check the observation

At 14:00, A is 45 seconds old and its ETA is future, so show 14:05 live. B is 100 seconds old, so show 14:08 scheduled. The future ETA does not make B’s observation fresh.

## Debrief · A blank is not zero

C’s explicit no-bus status is 20 seconds old, so show that status and no ETA. D has no evidence of live status; show 14:11 scheduled. Two routes, A and C, have live information: 2/4 or 50%. Only one has a live numeric ETA.

## Debrief · A successful retrieval is not an update

At 14:01:30 the upstream snapshot is 100 seconds old; the banner and scheduled times 14:07, 14:08, 14:10 and 14:11 replace all live information. Coverage is 0/4, not four cancellations. A stale past no-bus status cannot conceal a scheduled departure as if the latest state were known.

## Debrief · Monitor both paths

Alert separately on failures to retrieve and age since the last upstream update. Also watch route-level observation ages and coverage; the feed could be healthy while individual routes are stale. Record why each fallback occurred before restoring a live display.

## Instructor note

Spend four minutes on the first cross-section, four on the failure rule, four designing monitoring and three discussing recovery. Ask what happens at exactly 90 seconds and why an API transaction arriving now need not contain new observations. The 90-second policy and service messages are not instructions for a real operator.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Route IDs, values, timings, snapshot/fallback rules and display are fictional. Sources provide standards or datasets, not live trip forecasts or actual operator fallback policies.

- [DATA.GOV.HK, DPO estimated arrival dataset](https://data.gov.hk/en-data/dataset/hk-dpo-datagovhk1-transport-bus-route-list-and-eta-spcific-bus-stop). Describes the two operator sources and ETA for a specific stop.
- [DPO, Bus Route List and ETA API Data Dictionary](https://static.data.gov.hk/ogcio/datagovhk/opendata/eta/bus-route-list-and-eta-specific-stop-api-data-dictionary.pdf). Documents separate initial data timestamps and ETA fields; it does not prescribe the fictional display.
- [MobilityData, GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/). Documents the meaning of a trip-update timestamp apart from future StopTime predictions.
- [GTFS Realtime working group, Best Practices](https://old.gtfs.org/realtime/best-practices/). Explains refresh, age and missing update recommendations; not a Hong Kong API contract.
- [Citybus, real-time Next Bus arrival data dictionary](https://www.citybus.com.hk/datagovhk/bus_eta_data_dictionary.pdf). The operator documents its ETA and data generation timestamps separately, without prescribing this case’s fallback.
