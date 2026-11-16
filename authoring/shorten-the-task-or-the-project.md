# Shorten the longest task. Finish the project sooner?

<!-- legacy-case-id: 256 -->

OPS-22 · Hong Kong · fictional venue · 15–20 minutes · Critical path · Schedule compression · Float

![Two fictional venue managers discuss a blank plan beside furniture and decorative panels in a quiet event room.](../shorten-the-task-or-the-project-scene.jpg)

## A faster activity is not always an earlier opening

Project scheduling guidance treats completion as the result of dependencies, not just a list of task lengths. Adding resources to one activity may leave the final handover unchanged because another sequence still finishes later. After a change, the controlling sequence can move.

The venue, activities, durations and quotes below are original classroom assumptions. This is not a construction timetable or a claim about a named venue’s safety procedures.

## Opening decision

**Fictional classroom situation.** You coordinate a modest non-structural fit-out of a Hong Kong event room. The owner wants the earliest feasible handover within an approved acceleration budget. Base costs are already funded. Today you may buy **one** HK$6,000 acceleration package: shorten B from four to two working days, or shorten C from eight to six. The extra specialist team does not take staff from another activity. No partial packages or other first-round accelerations are offered.

All activities must be completed. Every listed predecessor must finish before its successor starts. B and C can run in parallel after A; D follows B; E waits for **both C and D**. B prepares only the furniture zone; C includes panel fabrication, delivery and placement in a separate display zone. Separate teams and sufficient space make this parallel work feasible. Materials and qualified staff are available. Assume fixed durations, no resource conflicts, rework or additional delays in this calculation.

Use elapsed working time starting at 0: a two-day activity starting at 0 finishes at time 2, and its successor may start immediately then. All teams use the same working calendar; the numbers are not calendar dates. All needed pre-start permissions are already in place. E includes the remaining required checks and handover: its two days and release conditions cannot be skipped or shortened. All packages retain the same quality and safe working arrangements.

## Evidence

Invented dependency schedule, working days. All predecessors must finish.

| Activity | Must wait for | Duration |
| --- | --- | --- |
| A · Final layout release | None | 2 |
| B · Prepare furniture zone | A | 4 |
| C · Make and place decorative panels | A | 8 |
| D · Fit furniture on site | B | 5 |
| E · Final checks and handover | C and D | 2 |

**Student question:** Which first acceleration, B or C, would you buy to finish the whole fit-out sooner? Calculate completion with no acceleration and with each option, rather than choosing the longest individual activity.

## Round two

**Use this common planning position, regardless of your first vote.** The owner has approved the B package, so B is now scheduled for two days. Work has not started; this is a revised plan, not a claim that the room is already complete. C is still eight days and D is still five.

A second, separate HK$6,000 acceleration budget becomes available. Choose at most one additional package: shorten C from eight to six days, or shorten D from five to three days. The C quote remains available; D’s extra team is newly available. Both packages meet the same safety and quality requirements, with no change to any other duration or dependency. You may retain the money by buying neither. E remains two days. The objective is still the earliest feasible handover within the authorised budget; no revenue per saved day is supplied.

**Student question:** Given B has been shortened to two days, would you spend the second HK$6,000 on C, on D, or neither? Calculate the project finish for each choice and identify the path that controls your recommended finish.

## Trace the two routes to handover

The two complete paths are A → B → D → E and A → C → E. Before acceleration their lengths are 2 + 4 + 5 + 2 = **13 days** and 2 + 8 + 2 = **12 days**. The room needs both branches, so the later route determines completion: 13 days, not their sum or average.

The 13-day route is the **critical path** in this simple schedule. Its activities have no scheduling room to slip without delaying the finish. C is the longest single activity, but finishes at time 10 while D finishes at 11. C has one day of **total float**: it can slip by one day without delaying project completion, if everything else stays as planned. Non-critical does not mean unnecessary or safe to ignore.

## First purchase: count project days saved

Shorten C to six: A → C → E becomes 10 days, but A → B → D → E remains 13. The project still finishes at time 13. This buys no earlier handover.

Shorten B to two: A → B → D → E becomes 11 days, while A → C → E remains 12. Completion becomes time 12, one day earlier. Buy B for the stated objective. Two days removed from B save only one project day because the other branch now controls the finish.

## The critical path moves

After B is shortened, A finishes at 2; B at 4; D at 9; C at 10. E cannot start until 10 and finishes at 12. A → C → E is now critical. B and D each have one day of total float relative to the revised finish, but that is shared path flexibility, not two separate days that can both be consumed without consequence.

Keep both routes visible. A change that helps the original critical path may have no further effect once a different route becomes longer.

## Second purchase: recalculate, do not repeat

With B already at two days, shortening D to three makes A → B → D → E equal 9 days. The C route remains 12, so completion remains 12. Buying neither also leaves completion at 12.

Shorten C to six instead: A → C → E becomes 10 days; A → B → D → E stays 11. Completion is now **11 days**, controlled by A → B → D → E again. Choose C for the earliest finish. The two packages together cost HK$12,000 and save two project days from the original 13-day plan. That is not four days saved just because two activity durations each fell by two.

The second package costs HK$6,000 for one additional project day saved. Whether that is financially worthwhile requires the value of the earlier handover and any wider costs; those are not supplied. The case establishes the fastest permitted schedule, not a profit-maximising investment.

## A schedule is a model, not a promise

At a merge point, start the successor when the last required predecessor finishes. Recheck the full network after acceleration or delay. Float belongs to a schedule with stated assumptions; it is not permission to miss safety, quality or contractual requirements.

Real durations and resource availability can change. Confirm the extra team, dependencies, remaining checks and updated forecast before promising an opening. If a required check fails, the room is not released merely because the calculated time has arrived. Adding workers does not necessarily shorten every kind of task.

## Instructor note

Allow 15–20 minutes: three for the dependency table, four for the first vote and two path calculations, five for the second budget, and three to eight for float and business interpretation. Keep the reveal closed until students commit to a first answer. Draw A splitting into B → D and C, then both feeding E. Never add parallel branches together.

Ask C supporters whether the furniture branch changes. Ask B supporters why two days removed save only one. Then use the common revised B plan for everyone so the second comparison is consistent. No formal backward-pass calculation is required; the optional one-day float discussion can follow the decision.

OPS-03 is repeated serial output constrained by station rates; OPS-04 sequences repeated batches on one machine; OPS-21 offsets material needs by lead times. This is a one-off project network with parallel paths and a merge. Do not equate critical with longest individual activity, or suggest accelerating safety inspections.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional nonstructural venue fit-out, durations, dependencies, budgets and specialist packages. Five activities A2,B4,C8,D5,E2 with predecessors A none;B A;C A;D B;E C andD. Same working calendar,elapsedtime0,finish-to-start no lags, separate teams/no resource conflicts, deterministictimes, unchangedscope quality safety. All prestart permissions ready, E mandatory two-day checks/handover cannot shorten or bypass; release still requires passing. Initial eligible packages B4to2 orC8to6 each6000 once. Reveal assumesBapproved beforework, second6000budget C8to6 orD5to3, atmostone; nothing else alters. Baseline paths13/12; Bonly11/12 finish12; Conly13/10 finish13; B+D9/12 finish12; B+C11/10 finish11. Baseline Cfloat1; afterB B/Dtotalfloat1each sharednotadditive. All numbers illustrative not observed productivity or procurement offers. Objectiveearliesthandover withinbudget notfinancialNPV. Five meaningful institutional/professional sourcebodies/sectionsread; two PMI papers are different documents, not independent fieldstudies. Main case selfcontained.

- [US Government Accountability Office · Schedule Assessment Guide · December 2015](https://www.gao.gov/assets/gao-16-89g.pdf). Best Practice 6: valid dependencies, longest paths, float, changing critical paths and uncertainty. Not a fit-out schedule or Hong Kong compliance standard.
- [Scott W. Kramer and James L. Jenkins · Understanding the basics of CPM calculations · 2006](https://www.pmi.org/learning/library/critical-path-method-calculations-scheduling-8040). Definitions and forward/backward passes; successors with several predecessors wait for the latest finish. No source network or worked figures reproduced.
- [Éamonn V. Kelly · Crash with confidence · 2011](https://www.pmi.org/learning/library/generating-crash-analysis-calculating-costs-6224). Time-cost tradeoffs, feasible acceleration limits and rechecking the critical path. No real-world productivity improvement assumed.
- [Association for Project Management · What is scheduling in project management?](https://www.apm.org.uk/resources/what-is-project-management/what-is-scheduling-in-project-management/). Public explanation of duration, dependency logic and float; scope/risk/quality remain part of scheduling.
- [Microsoft Support · Manage your project’s critical path](https://support.microsoft.com/en-us/project/manage-your-project-s-critical-path). Changing task durations can change the controlling sequence. Software-specific critical-task settings are not imposed on this manual model.
