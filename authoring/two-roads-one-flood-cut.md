# Two shuttle routes. One place they can both fail?

<!-- legacy-case-id: 547 -->

SUS-45 · Hong Kong · 15 minutes · Climate adaptation · Service continuity · Common-route dependency

![Two hospital staff examine a shuttle route map next to a parked minibus.](../two-roads-one-flood-cut-scene.jpg)

## Extreme rain can interrupt whole journeys

After Hong Kong’s severe rainstorm in September 2023, the government reported clearance work on major roads and bus routes, while some roads remained closed. In Shek O, it separately reported work on a landslip that had blocked a road. This case models a fictional hospital staff shuttle, not a real hospital’s accessibility or emergency arrangements.

## Opening decision

Bo coordinates a weekday staff shuttle at a fictional Hong Kong hospital. Both existing routes reach different boarding points but must cross the same low road section. If it is officially closed, neither route can be used. Emergency and patient transport are separate and remain unchanged. No driver may use a closed road.

Improve funds access improvements at the shared road section, with review and permission assumed for this exercise. Detour keeps the shared road unchanged and reserves a verified alternate route when that road closes. In the initial forecast the detour is open on every such day. The exhibit forecasts disruption over 20 comparable heavy-rain days.

Count a disrupted day whenever no authorised route can complete the staff shuttle trip by the agreed time. The hospital can spend up to HK$60,000 and first wants to minimise expected disrupted days. If disruption ties, choose the lower cost. Assume there are no other disruptions in the model.

## Evidence

| Fictional planning forecast | Improve | Detour |
| --- | --- | --- |
| Fixed cost | HK$56,000 | HK$48,000 |
| Expected days shared road is closed | 3 | 8 |
| Fraction of those days detour also closed | Not offered | 0% |

**Student question:** Which option should Bo recommend? How many disrupted days does each imply, and why is running two existing routes not equivalent to having two independent ways through?

## Round two

A joint route check finds that the proposed detour uses a different road, but is expected to be closed on half of the days when the shared road is closed because of flooding near its own exit. No extra day closes the service if the shared road remains open. The rest of the forecast is unchanged.

**Student question:** Which option now fits the objective best? At what fraction of shared-road closure days could the detour also be closed and still tie Improve on disrupted days? Which option wins at that point under the stated rule?

## Debrief · Map what the routes have in common

Improve leaves 3 expected days without a usable route. Initially Detour leaves 8 × 0% = 0. Both options fit the budget, so choose Detour. Different route names are immaterial when both routes use the same closed section.

## Debrief · Different road does not mean independent failure

Detour now leaves 8 × 50% = 4 expected disrupted days. Improve leaves 3 and remains within budget, so choose Improve even though it costs HK$8,000 more. The conditional share already refers to days with shared-road closure; no independent-probability assumption is needed.

## Debrief · Locate the tie

Set 8 × overlap share = 3. At 37.5%, each plan leaves 3 expected disruptions. Choose the less expensive Detour at that point. A practical route check should verify common links, joint closures and authorised travel times, not just compare lines on a map.

## Instructor note

Use 2 minutes to read, 4 on the network, 4 for the conditional overlap, and 5 for the decision rule. The forecast is illustrative and gives no travel, safety or engineering advice; a predicted available route never overrides an actual closure.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All contracts, probabilities, geography of the shuttle routes and days disrupted are invented. No real hospital’s access, road safety or risk estimate is implied.

- [HKSAR Government, Extreme conditions to end at midnight](https://www.info.gov.hk/gia/general/202309/08/P2023090800946.htm). Reports major road and bus-route clearance and sections still closed for repairs.
- [HKSAR Government, Shek O repair works in full swing](https://www.info.gov.hk/gia/general/202309/09/P2023090900788.htm). Reports recovery from landslips and damaged access roads in Shek O after the severe rainfall.
- [Hong Kong Observatory, The Year’s Weather 2023](https://www.hko.gov.hk/en/wxinfo/pastwx/2023/ywx2023.htm?os=win). Provides the Observatory’s measured rainfall context for the 7–8 September episode.
- [Drainage Services Department, Flooding Problems](https://www.dsd.gov.hk/EN/Flood_Prevention/Our_Flooding_Situation/Flooding_Problems/index.html). Summarises causes and characteristics of flooding relevant to road access.
- [Hong Kong Observatory authors, Preliminary Study of the September 2023 Severe Rainstorm](https://www.hko.gov.hk/en/publica/reprint/files/r1726_en.pdf). Original meteorological study reports prolonged multi-district rainfall and associated disruption.
