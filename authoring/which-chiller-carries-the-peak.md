# Which chiller should carry the evening peak?

<!-- legacy-case-id: 551 -->

OPS-46 · Hong Kong · 15 minutes · Load allocation · Energy use · Running reserve · Discrete optimisation

![Two facilities staff look at a sheet beside chillers in a plant room.](../which-chiller-carries-the-peak-scene.jpg)

## Cooling plants can optimise which chillers run

Hong Kong’s Electrical and Mechanical Services Department describes chiller sequencing as choosing when machines start or stop using information about demand and part-load performance. This example uses invented measurements for a small plant; it is not an operating procedure.

## Opening decision

At a fictional Kwun Tong shopping centre, the plant has two chillers, A and B. During the next two-hour block the expected cooling demand is 300 kW. The table lists each unit’s allowed cooling outputs and its total electrical draw at each setting, including associated equipment. A dash is unavailable.

Supply exactly 300 kW of cooling during this block. Minimise electrical energy, calculated as total electrical power multiplied by two hours. Ignore start costs and assume a unit operating at zero is off. Cooling kW and electrical kW measure different quantities.

## Evidence

| Cooling output per unit (kW) | A electric draw (kW) | B electric draw (kW) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | 27 | 20 |
| 200 | 49 | 43 |
| 300 | — | 63 |

**Student question:** Which combination meets 300 kW at the lowest electricity use? Show the feasible combinations and their two-hour consumption.

## Round two

Maintenance advises that a 100 kW cooling surge could arrive on short notice. Require at least 100 kW of unused output capacity from already running chillers. An offline unit cannot start fast enough to count. Compute reserve as each running unit’s maximum cooling output minus its current output.

**Student question:** Which schedule is least costly with the reserve rule, and what is its extra energy use before any surge? Could the plant meet both requirements if A were unavailable?

## Debrief · Make a feasible list

Three combinations supply exactly 300 kW: A off and B at 300; A at 100 and B at 200; A at 200 and B at 100. They draw 63, 70 and 69 kW respectively, or 126, 140 and 138 kWh for two hours. Start with B alone under the original objective.

## Debrief · Count only the power already on

B alone has zero reserve at 300. With both units running, their combined maximum is 500 kW and current output is 300, so each two-unit combination carries 200 kW of running reserve. A at 200 and B at 100 draws less power than the other qualifying combination.

## Debrief · Price the extra headroom

The selected reserve schedule uses 138 − 126 = 12 kWh more before a surge. If A is unavailable, B can meet the base load but cannot also hold 100 kW in reserve. The two targets then cannot both be met by this plant.

## Takeaway · Don’t confuse nameplate and useful reserve

A machine can be installed and operable without contributing immediately to reserve. The illustration is discrete and single-block. Real plant decisions need verified models for pumps, starts, weather and site-specific controls.

## Instructor note

Allow 15 minutes: 3 for units and feasible settings, 4 to compare ordinary dispatch, 5 to test reserve, and 3 for interpretation. Ask whether adding nominal capacity would help if it could not respond in time.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The centre, load, electrical draw, allowable settings and reserve requirement are fictional. No engineering or code compliance instruction is given.

- [EMSD, Guidelines on Application of Central Control and Monitoring Systems](https://www.emsd.gov.hk/filemanager/en/content_764/ccms17.pdf). Section 6.5.10 describes sequencing with partial-load performance and cooling profiles.
- [EMSD, Building Energy Code 2024](https://www.emsd.gov.hk/beeo/en/pee/BEC_2024_ENG.pdf). Section 6.14 documents monitoring and optimising relevant chilled-water plants. The fictional table is not a compliance test.
- [EMSD, Retro-commissioning Technical Guidelines supplementary information](https://rcxrc.emsd.gov.hk/uploads/media/658401249fcd5/emsd-tg-rcx-2023-supplementary-information-en-final-clean.pdf). Describes chilled-water equipment and system boundaries, including pumps.
- [EMSD Annual Report 2023/24, Staff Highlights](https://wcms.emsd.gov.hk/minisites/EMSDar/2324ar/en/staff-highlights.html). Describes the department’s own chiller optimisation project using observed conditions, not the exercise numbers.
- [EMSD, Energy Consumption Indicators and Benchmarks](https://www.emsd.gov.hk/en/energy_efficiency/energy_end_use_data_and_consumption_indicators/energy_consumption_indicators_benchmarks/). Documents local energy benchmarking context, a different level of analysis from an individual dispatch schedule.
