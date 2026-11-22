# One night: which work belongs together?

<!-- legacy-case-id: 572 -->

OPS-48 · Hong Kong · 15 minutes · work packaging · shared setup · constrained maintenance

![Two railway planners compare a route diagram and coloured parts tokens on a table.](../one-night-which-work-belongs-together-scene.jpg)

## Railway renewal has a closing time

MTR describes using a roughly two-hour overnight window for Hong Kong inspections, maintenance and renewal. Singapore’s Land Transport Authority also describes scheduling renewal and maintenance into narrow engineering hours. The situation below is a fictional planning problem, not guidance for rail work.

## Opening decision

You choose optional preventive work at Harbour Link Rail. The overnight planning envelope is 95 minutes. The final 20 minutes are reserved for independent signoff before the service team may take over, leaving 75 minutes for setup and work. Required safety work is already accounted for outside this exercise.

A single team works sequentially and has 15 minutes of fixed setup per area visited tonight, whether it does one or both jobs there. Work durations are additional. A job counts only if completed in full. All jobs can wait for a future approved window.

The exhibit uses points on a common scale for the benefit of completing each job tonight instead of deferring it. Points add across jobs. Choose the feasible package with the highest total points.

## Evidence

| Optional job | Area | Work time | Points |
| --- | --- | --- | --- |
| A1 | West | 29 min | 10 |
| A2 | West | 24 min | 7 |
| B1 | East | 35 min | 12 |
| B2 | East | 18 min | 7 |

**Student question:** Which package should the team schedule tonight, and why should the choice depend on work areas rather than on individual job scores alone?

## Round two

Just before planning closes, the East area setup increases to 25 minutes. The West setup, work times, benefits, total window and protected signoff time are unchanged.

**Student question:** Which package should replace the original one? How many setup minutes could East have used at most for its original two-job bundle to remain feasible?

## First decision: pay setup once per area

East’s two jobs use 15 + 35 + 18 = 68 minutes and earn 19 points. West’s use 15 + 29 + 24 = 68 minutes and earn 17. The only feasible mixed pair is A2 and B2: 30 + 24 + 18 = 72 minutes for 14 points. No three jobs fit, and no single job scores above 12. Choose East.

## Second decision: test feasibility before ranking

East’s setup can use at most 75 − 35 − 18 = 22 minutes. At 25 minutes, the bundle takes 78 minutes. Even the shortest mixed pair would take 15 + 25 + 24 + 18 = 82. West’s bundle still fits and earns 17, better than any single job. Leave the 20 minutes of signoff untouched.

## What to take away

When jobs share a setup, the relevant decision is the package. Simply sorting jobs by points or per-minute benefit ignores the cost of adding another area. Protect required handover time before optimising optional work.

## Instructor note

The time and point values are fictional and do not describe how any operator certifies work or returns a railway to service.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The time and point values are fictional and do not describe how any operator certifies work or returns a railway to service.

- [MTR, Hong Kong Transport Services business overview](https://www.mtr.com.hk/archive/corporate/en/publications/images/business_overview_e.pdf). Describes how overnight inspection, maintenance and asset renewal use a roughly two-hour non-traffic window.
- [Hong Kong Government, LegCo railway maintenance paper](https://www.legco.gov.hk/yr2024/english/panels/tp/tp_rsc/papers/tp_rsc20250207cb3-131-4-e.pdf). Discusses competing uses of the maintenance window and the occasional planned extension of non-traffic hours.
- [Hong Kong Government, Legislative Council reply on train services](https://www.info.gov.hk/gia/general/201512/09/P201512090545.htm). Gives examples of distinct inspection work and explains that defective track replacement occurs during night non-traffic hours.
- [Singapore LTA, Bukit Panjang fleet and infrastructure renewal](https://www.lta.gov.sg/content/ltagov/en/newsroom/2024/8/news-releases/first-two-new-bukit-panjang-light-rail-vehicles-to-commence-passenger-service-from-1-august.html). Paragraph 7 describes why concurrent renewal and maintenance within narrow engineering hours must be coordinated.
- [Singapore LTA, Integrated Train Testing Centre factsheet](https://www.lta.gov.sg/content/ltagov/en/newsroom/2021/3/news-release/singapore_ittc_to_be_fully_operational_in_2024.html). Explains how moving train testing away from the mainline releases time and space for other maintenance.
