# A shorter route. A missed window?

<!-- legacy-case-id: 160 -->

OPS-14 · Hong Kong · 10–15 minutes · Routing · Time windows · Delivery feasibility

![A dispatcher and delivery driver discuss plans beside a parked van and trolley of parcels in a depot courtyard.](../route-and-window-scene.jpg)

## A Hong Kong access reminder

A Transport Department notice designated specified Mong Kok road sections as restricted zones from 13 July 2026, including restrictions on loading and unloading except for permitted users. It illustrates why access conditions matter alongside a route’s length.

The three stops below are invented, with no real customer addresses. Their loading windows are fictional site conditions, not the road restrictions in that notice.

## Opening decision

Fictional classroom situation. A Hong Kong delivery dispatcher has one van carrying all three customers’ parcels. It leaves depot D at 9:00 a.m. after the load and safety checks and must return by 11:00. Driver, vehicle, capacity and safe working arrangements are the same and funded under either plan. Each stop requires ten uninterrupted minutes for safe unloading and receipt.

Two candidate sequences have been prepared: Route 1 visits A, then B, then C, and returns to D; Route 2 visits B, then A, then C, and returns to D. Route 1 is shorter, but Route 2 reaches B earlier. Compare these two candidates only; no claim is made that either is best among every possible route.

For the first calculation, use the booking windows: A 9:10–9:50, B 9:20–10:00 and C 9:50–10:30. The whole ten-minute stop must fit inside its window, not merely arrival. Safe waiting space is available if early. Travel times below are fixed classroom assumptions, not a promise about Hong Kong traffic. Site confirmations are due before dispatch.

## Evidence

| Leg | Distance | Travel time |
|---|---:|---:|
| D → A | 4 km | 15 min |
| A → B or B → A | 2 km | 10 min |
| B → C | 3 km | 15 min |
| D → B | 6 km | 20 min |
| A → C | 4 km | 20 min |
| C → D | 5 km | 20 min |

**Student question:** Which route would you provisionally schedule? Show the unloading start and finish at each stop, then identify what you must confirm before calling the shorter route feasible.

## Round two

Before the van leaves, A confirms that its receiving team and loading bay can now accept the whole stop until 10:10. B’s building manager confirms a tighter loading-bay rule: unloading must start no earlier than 9:20 and be fully finished by 9:35. B’s customer booking alone had not captured that building condition. C’s 9:50–10:30 window is unchanged.

These are verified conditions for this fictional day. The public-road routes and private bays are lawful to use as specified; there is no permitted curbside substitute, unattended drop, second van or earlier departure. The ten-minute service time and travel-time assumptions remain. Do not reduce safety checks, speed or pretend that arrival at the closing time is enough.

Recalculate both candidates against these confirmed windows. Route 2 costs three extra kilometres and ten extra minutes overall, but it may satisfy a constraint that Route 1 cannot. No late-delivery penalty has been supplied that allows the dispatcher to buy permission to miss the window.

**Student question:** Which candidate is feasible now? Give its full timetable, explain the failed constraint in the other route, and state what you would do if an actual delay threatened the remaining time margin.

## Trace the clock, not just the line on the map

Route 1: D 9:00 → A 9:15–9:25 → B 9:35–9:45 → C 10:00–10:10 → D 10:30. It covers 14 km, with 60 minutes travelling and 30 minutes serving customers. It fitted the original booking windows.

Route 2: D 9:00 → B 9:20–9:30 → A 9:40–9:50 → C 10:10–10:20 → D 10:40. It covers 17 km, with 70 minutes travelling and 30 minutes service. It also fitted the original windows, but originally finished exactly at A’s limit.

## Check the revised constraint

After confirmation, Route 1 reaches B at 9:35 but still needs ten minutes. Finishing at 9:45 violates the 9:35 close. Route 2 completes B at 9:30, A at 9:50 and C at 10:20, so every full stop fits and the van returns before 11:00.

The extra distance is not waste simply because another path is shorter. Feasibility comes before minimising distance among the candidates. Waiting can help an early arrival; it cannot repair a late finish at B.

## A feasible plan is not a traffic guarantee

Route 2 leaves five minutes before B’s finish deadline and ten before C’s. A’s newly widened window offers more room there, but it cannot erase a downstream limit. These are local margins, not an extra allowance that can be spent repeatedly at every leg.

Monitor progress, use an agreed dispatcher contact and seek a lawful revised arrangement if a delay makes the plan infeasible. Do not unload outside the permitted window without agreement, park illegally or shorten safe service. The case supplies no probability of delay or comparison proving this is a robust real-world optimum.

## Instructor note

Have students mark travel and service as separate blocks. The reveal changes site constraints, not driving speed, volume or the service task. Check both initial feasibility and revised feasibility; do not reward a recommendation based only on kilometres.

OPS-02 selects which goods to expedite; OPS-07 compares waiting at service counters. Here the object is the sequence of geographically separated stops under access windows. Some routing APIs define windows as service-start intervals; this case explicitly requires completion within the window. Do not import an API convention over the stated customer condition. UK safety guidance is illustrative, not Hong Kong legal advice.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All stops, parcels, travel times, distances and windows are original fiction. One van, all loads ready after checks at exactly 9:00, return deadline 11:00; no capacity, loading-order or safe-working difference. Either candidate is funded. Ten minutes includes all safe unloading and receipt activity and cannot be compressed. Whole-stop windows are inclusive at boundaries. Initial Route 1 and Route 2 both fit. Confirmed A end moves from 9:50 to 10:10; B end changes from 10:00 to 9:35 after building verification. Route 1 is no longer feasible at B; Route 2 is feasible with five minutes at B and ten at C. Travel durations are exogenous and do not imply a constant speed per kilometre. Distance sums 14/17 and driving sums 60/70; total elapsed 90/100. There is no omitted depot handling after departure or before the stated return endpoint. Only two proposed sequences compared, not exhaustive optimisation. No real addresses or route service API calls made. Site loading conditions and public-road legality are separate; all specified routes/bays legal in the fictional premise. No unsafe shortcuts, unapproved arrival, automatic late penalty permission or spare emergency resource. Actual delays require reassessment rather than a guaranteed recovery action. Google technical docs are primary descriptions of models, not evidence of delivery performance. Solomon 1987 university copy was access-denied and publisher supplied only an abstract; neither counts as a read substantive source. Five other institutional bodies were read.

- [Hong Kong Transport Department · Restricted zones in Mong Kok · effective 13 July 2026](https://www.td.gov.hk/en/traffic_notices/index_id_87558.html). Read complete notice, including exceptions. Local context only; fictional customer windows are not inferred from it.
- [Hong Kong Transport Department · Where not to stop](https://www.td.gov.hk/en/road_safety/road_users_code/index/chapter_5_for_all_drivers/where_not_to_stop_/?print=1). Read no-stopping and signage guidance. The case does not treat unloading as an automatic exemption or provide a real route authorisation.
- [Google OR-Tools · Vehicle routing problem with time windows](https://developers.google.com/optimization/routing/vrptw). Read model explanation and time-window/waiting constraint discussion. No code, map or example data reproduced; no claim a solver was run.
- [Google Route Optimization API · Time windows](https://developers.google.com/maps/documentation/route-optimization/concepts/time-windows). Read event-window definitions and essentials. This API generally applies delivery windows to start time; the fictional case deliberately specifies full-stop completion instead.
- [UK HSE · Management and supervision of workplace transport risk](https://www.hse.gov.uk/WORKPLACETRANSPORT/checklist/section1.htm). Read site communication and time-pressure sections. Safe planning principles only, not a statement that UK workplace rules govern Hong Kong.
