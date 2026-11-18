# The project has time. Does the specialist?

<!-- legacy-case-id: 424 -->

OPS-36 · Singapore · 15–20 minutes · Resource-constrained scheduling · Float · Resource levelling

![Two adult Singapore fit-out coordinators compare a plain task timetable in an unfinished demonstration room, with display equipment and a technician’s closed tool case nearby.](../project-time-specialist-time-scene.jpg)

## Dependencies do not establish resource availability

Scheduling guidance distinguishes a valid sequence of tasks from a feasible allocation of people. Parallel activities may compete for the same specialist. Sometimes moving an activity within its available scheduling room resolves the conflict without accelerating any task or delaying completion. All project details and prices below are fictional.

## Opening decision

You coordinate a fictional Singapore demonstration-room fit-out. The owner has committed to handover at working time 9. The draft plan satisfies every listed dependency and finishes exactly then. Before authorising execution, decide whether that is enough to approve it or whether a resource check is still required.

Use elapsed working days starting at time 0. A one-day task starting at 0 ends at 1; its successor may start immediately. Every task uses the same normal working calendar and must run without interruption. Durations are fixed; no overtime, splitting, shortened checks or altered scope is allowed.

A releases the layout in one day. B configures demonstration-panel hardware in three days. C calibrates decorative display lighting in two days. D verifies demonstration content for four days after B. E performs required final checks and handover in one day after both C and D. These are not emergency or life-safety systems.

All pre-start permissions, materials and safe access arrangements are in place. Required qualifications and release conditions remain fixed. The listed tasks cover the whole bounded project, but the initial table does not identify who performs B and C. Base costs and existing staff are funded; no work has started.

## Evidence

| Task | After | Duration | Start–finish |
| --- | --- | --- | --- |
| A | None | 1 | 0–1 |
| B | A | 3 | 1–4 |
| C | A | 2 | 1–3 |
| D | B | 4 | 4–8 |
| E | C, D | 1 | 8–9 |

**Student question:** Verify the time-9 finish and identify the controlling path. How far could C move without delaying E in the dependency-only plan? What information is missing before calling the timetable executable?

## Round two

The staffing review finds that B and C each need one qualified technician continuously for their entire duration. The same single technician is assigned to both and can perform only one at a time. That technician is available throughout working times 1–8. A, D and E use separate, fully available teams.

B and C occupy different work zones. C may overlap D safely; there is no hidden dependency or shared equipment between them. The only resource conflict is the technician. Moving C within times 1–8 changes neither its cost nor the availability of any other task, materials, access or required approvals.

Option L keeps the existing technician and reschedules B and C without changing durations. Option H hires a second equally qualified technician to perform C at 1–3 while the first performs B at 1–4. H costs an additional S$1,200 in total, including all necessary expenses; no hiring commitment has been made.

The owner wants a resource-feasible finish no later than time 9 at the lowest additional cost. Both options are fundable. The second technician cannot shorten B, D or E; no additional revenue or resilience benefit is valued in this deterministic exercise. Final release still requires passing all checks, not merely reaching the scheduled time.

**Student question:** Choose L or H and give start–finish times for every task. Explain why doing C first with the existing technician is not equivalent to doing B first. How much of C’s original scheduling room does your recommended plan use?

## Debrief · Read the network first

The dependency paths are A–B–D–E: 1 + 3 + 4 + 1 = 9, and A–C–E: 1 + 2 + 1 = 4. Both branches must finish before E. The first path controls the dependency-only finish. Nine days is a lower bound under the fixed durations, not yet proof that the assigned people can deliver it.

C initially starts at 1 and ends at 3. E cannot begin before D ends at 8, so C could start as late as 6 and finish at 8. Its original total and free float are both five days here. Float is permission to move within this model, not permission to omit C.

## Debrief · Locate the resource conflict

From time 1 to time 3, the draft needs two technicians simultaneously: one on B and one on C. Only one is assigned. Correct precedence links do not make this overlap feasible. A weekly total of available person-days would also miss the collision unless availability is checked at the relevant time intervals.

The existing technician needs five working days in total for B and C. That fact alone does not determine the correct order. B unlocks four days of separate content work; C only has to finish before the final merge. Use the dependency network together with the resource calendar.

## Debrief · Level within the available float

Choose L. Keep A at 0–1 and B at 1–4. Move C to 4–6 using the same technician, while the separate D team works at 4–8. E remains at 8–9 because both C and D are complete by 8. No task duration or requirement changes.

C starts three days later than its original time 1, consuming three of its five days of float. Its finish at 6 leaves two days before E starts at 8. The single technician never overlaps assignments. Under the stated calendar, C could also start between 4 and 6 and still meet handover.

## Debrief · Check the tempting alternative

If C goes first at 1–3, B must wait until 3–6. D then runs at 6–10, and E at 10–11. Handover is two days late. Prioritising the shorter task or whichever manager asks first ignores the downstream chain. Nothing about C’s lower duration makes it the right first assignment.

H restores the original parallel plan and also finishes at 9, but costs S$1,200 more. L meets the same deadline with zero additional cost under the supplied assumptions. H buys no earlier completion because A–B–D–E still requires nine days. Choose the feasible lower-cost plan, not extra capacity merely to preserve early task dates.

## Debrief · State what has and has not been proved

This is resource levelling within available float; some terminology calls the within-deadline form resource smoothing. The operational result matters: feasible assignments, unchanged durations and time-9 finish. Resource constraints can extend a project in other networks. Do not infer that every conflict can be solved by delaying a noncritical task.

The two remaining days beside C are not two spare days on the entire project. B, D and E still control handover. Confirm individual availability, qualifications, safe concurrent work, equipment and task dependencies before issuing the revised baseline. If actual conditions change, recalculate rather than promising the deterministic result.

## Instructor note

First draw the split after A and the merge before E. Ask learners to approve only dependency feasibility until the resource reveal. Then draw one technician’s timeline and compare B-first with C-first. Require all five task intervals, the time-11 alternative and the S$1,200 unnecessary premium before accepting a recommendation.

OPS-22 pays to shorten selected task durations and recalculates the critical path. Here every duration stays fixed; the decision reallocates one specialist’s time. This is a classroom scheduling model, not Singapore construction or electrical guidance. Required competence, safety, approvals and final release checks cannot be traded for deadline compliance.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Fictional Singapore bounded project, elapsed common working time0. Tasks A1 none;B3 afterA;C2afterA;D4afterB;E1afterC,D. Paths9/4. Initial A0–1 B1–4 C1–3 D4–8 E8–9. B/C each require same single technician continuously; technicianavailable1–8; otherteams/resourcesfullyavailable. Nonpreemptive,noovertime,noacceleration. C/D safeparallel,differentzones,nohiddendependency. Level B1–4 C4–6 D4–8 E8–9, originalCfloat5 consumes3 leaves2; starts4through6 feasible. Cfirst1–3 pushesB3–6 D6–10 E10–11. HsecondqualifiedtechnicianC1–3 cost1200SGDallinclusive, finishstill9. Lzeroadditionalcost,basefunded andmovingCnochangecost. Objectivefinishby9lowestadditionalcost,noriskpremium/revenueprovided. Qualifiedstaff,prestartpermissions,safetyandfinalreleaseconditionsprotected. Lowerbound9achieved sooptimaldurationtoo. No actual legal guidance or sourced productivity figures.

- [Tammo T. Wilkens · Fundamentals of scheduling and resource leveling · 2006](https://www.pmi.org/learning/library/scheduling-resource-leveling-project-progression-8006). Original professional conference paper explains time-resource tradeoffs and prioritising competing activities. Used for scheduling logic, not its broad assurances about finishing on time or any copied example.
- [Microsoft Support · Distribute project work evenly (level resource assignments)](https://support.microsoft.com/en-gb/project/distribute-project-work-evenly-level-resource-assignments?nochrome=true). Product documentation explains resolving overallocations by moving tasks and warns that completion may move. This manual exercise forbids splitting and does not assume software output is automatically optimal.
- [Chris Hendrickson · Project Management for Construction · Fundamental Scheduling Procedures](https://www.cmu.edu/cee/projects/PMbook/10_Fundamental_Scheduling_Procedures.html). Author’s open textbook distinguishes time-oriented and resource-constrained scheduling and discusses manual adjustment and heuristic limits. No source project, resource data or diagram is reproduced.
- [US Government Accountability Office · Schedule Assessment Guide · December 2015](https://www.gao.gov/assets/gao-16-89g.pdf). Original institutional guide explains realistic resource assignments, free float and documenting levelling effects. US oversight guidance supplies concepts, not local construction requirements or this case’s durations.
- [NASA · Schedule Management Handbook · March 2011](https://ntrs.nasa.gov/api/citations/20110012668/downloads/20110012668.pdf). Archived original handbook section 5.6 explains resource calendars, loading and reviewing levelling results. Historical conceptual guidance only, not a statement of current NASA policy or a Singapore compliance standard.
