# Equal work. A balanced line?

<!-- legacy-case-id: 400 -->

OPS-34 · Hong Kong · 15–20 minutes · Line balancing · Task precedence · Equipment compatibility

![Three fictional adult workshop colleagues examine six plain task cards beside three orderly gift-packing benches, with a forming fixture and wrapping fixture on separate benches.](../equal-work-balanced-line-scene.jpg)

## Averages do not assign tasks

Line balancing assigns tasks to workstations while preserving their required order and equipment restrictions. Dividing total work by the number of people gives a workload benchmark, not proof that an assignment is feasible. The workshop, tasks, times and fixtures below are entirely fictional.

## Opening decision

You manage a Hong Kong workshop packing non-food stationery gifts for adults. Three trained adults operate three ordered stations, one person per station. Every pack visits stations 1, 2 and 3 in order. You must assign six indivisible tasks, A–F, to these fixed stations before a supervised trial.

The desired steady operating cadence is one finished pack every six minutes, equivalent to ten per hour once the line is filled. It is a planning target, not a customer promise. Existing orders are protected by finished stock. You can recommend a slower feasible cadence without overtime or missed deliveries.

Assign each task exactly once to one station; no splitting tasks, parallel helpers, backward travel or omitted checks. Within a station, one task follows another. A predecessor may share its successor’s station only if performed first. Otherwise it must be at an earlier station. Different stations work on different packs concurrently.

The exhibit gives exact minutes per pack under approved methods for this exercise, not observed worker-performance estimates. Times include routine handling and required checks. Transfer time adds nothing further in this simplified model. Materials, approved transfer space and staffing are adequate; no other capacity restriction is assumed.

Breaks, setup and line filling are outside the net operating intervals considered here and remain funded and protected. Nobody must work faster, skip an inspection or change an approved fixture. Any proposed reassignment needs its normal safety and quality approval before use. Equipment compatibility still needs checking.

A colleague proposes station 1: A then B; station 2: C then D; station 3: E then F. Each totals six minutes. Assess this as a provisional time-and-precedence plan, not an instruction to begin production. The equipment record will be opened before anything is moved.

## Evidence

| Task | Approved work | Minutes | Must follow |
| --- | --- | --- | --- |
| A | Prepare coded carton | 2 | None |
| B | Check kit against carton code | 4 | A |
| C | Form matching insert | 3 | A |
| D | Wrap checked kit | 3 | B |
| E | Fit formed insert | 4 | C |
| F | Pack, final check and seal | 2 | D and E |

**Student question:** Does the proposed 6–6–6 assignment respect every precedence link? Explain what the total of eighteen task-minutes establishes, and what it cannot establish before the equipment check.

## Round two

The verified equipment record shows that C’s forming fixture occupies the full main bench surface. D’s wrapping fixture needs that same full surface. Both must remain installed during an operating run, so C and D cannot share a station, even if their tasks are done sequentially.

Each station already has an approved side shelf for A, B, E or F alongside either fixture. All other task combinations are compatible. Before the trial, the two existing fixtures may be assigned to different stations using the funded setup procedure. Neither fixture can be removed between packs or placed in a walkway.

No fourth station, extra person, duplicate fixture or alternative method is available in this decision. Task times and precedence remain unchanged. Revise the allocation and state the fastest feasible cadence under these assumptions, rather than certify six minutes merely because average work is six minutes per worker.

**Student question:** Can any three-station allocation still achieve six minutes per pack? Demonstrate an equipment-compatible allocation, verify all its precedence links, and explain the resulting output rate and unused time without cutting breaks or checks.

## Debrief · The first plan passes only two tests

A before B is respected within station 1. A also precedes C; B precedes D. Both C and D finish before station 3, where E follows C and F follows both D and E. The proposed 6–6–6 plan therefore passes time and precedence tests, but fails equipment compatibility.

## Debrief · Why the average is not enough

Total task work is 2 + 4 + 3 + 3 + 4 + 2 = 18 minutes. With three stations, the largest station load cannot be below 18/3 = 6. That is a lower bound. It says a faster cycle is impossible, not that six minutes is achievable.

A six-minute cycle would require all three loads to equal six, with no unused time. The only way to partition these indivisible task times is two pairs of 2 + 4 and one pair of 3 + 3. The only three-minute tasks are C and D, which cannot share a station. Six is therefore infeasible.

## Debrief · A feasible reassignment

Use station 1: A then C, five minutes; station 2: B then D, seven minutes; station 3: E then F, six minutes. C and D occupy different benches. A precedes B and C; B precedes D; C precedes E; D and E both precede F. Every task appears once.

Set the common cycle to seven minutes. Each station finishes its assigned work before the next transfer; within-station sequences preserve all checks. Loads are 5–7–6, not 6–6–6. With integer task times, every possible station load is an integer; since six is infeasible and seven is attained, seven is the minimum here.

## Debrief · Rate and unused capacity

At a seven-minute cycle, steady output is 60/7, about 8.57 packs per operating hour. That is below the target of ten. It is a long-run rate, not a promise of fractional packs or first-hour completions from an empty line. Finite-run output also depends on filling, draining and available operating time.

Across three stations, each cycle provides 3 × 7 = 21 worker-minutes against eighteen task-minutes. Unused scheduled time is three worker-minutes: two at station 1, zero at station 2, one at station 3. Work-content utilisation is 18/21, about 85.7%. This is not a measure of worker effort or attendance.

## Debrief · Revise the plan, not the rules

I would propose the 5–7–6 assignment for the normal approved trial and communicate a seven-minute model cadence. Preserve stock cover and existing commitments. Confirm safe setup, actual sustainable times and acceptable finished quality before adopting it. This model does not justify guaranteeing ten packs per hour.

Unused time at one station cannot automatically be transferred to another. Cross-station assistance, task splitting, new equipment or method changes would require a different approved model and resources. Do not rescue the target by silently introducing them. A future redesign may be investigated separately; none is supplied here.

## Instructor note

Minutes 0–4: map all six precedence links and test the provisional plan. Minutes 4–8: reveal the incompatible fixtures and prove six impossible. Minutes 8–13: construct and check 5–7–6. Minutes 13–18: calculate cadence and distinguish a mathematical lower bound from feasible, safely validated production.

OPS-03 chooses an investment at an existing serial-process bottleneck. Here the people, stations, equipment and task times are fixed. The decision is task assignment subject to precedence and compatibility, not which machine to speed up. The nominally perfect balance is infeasible before any investment comparison begins.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Fictional non-food stationery packing task, fixed three people/stations, six indivisible tasks with exact approved times2,4,3,3,4,2minutes. Precedence A→B,A→C,B→D,C→E,D→F,E→F. C/D cannot share station because fixtures occupy full main bench and stay installed; other tasks use approved side shelf and all other combinations are compatible. No duplicate fixture, helper, splitting, backward travel or omitted checks. Initial AB/CD/EF passes precedence and6minute loads but fails compatibility. Total18/3=6lowerbound; only exact6partition requires C/Dtogether; feasible AC/BD/EF loads5/7/6 attain minimum7 because loads integral. Rate60/7≈8.57pernetoperatinghour; not first-hour output. Idle3worker-min/cycle and18/21≈85.7%work-contentutilisation, not effort. Breaks/setup/filling protected outside modeled operating intervals. Existing orders covered by finished stock, no new promise. All methods and reassignment require normal safety/quality approval. Sources supply modeling concepts, not measured performance or approval of the fictional layout.

- [Guéret, Prins and Sevaux / Heipcke · Applications of optimization with Xpress-MP · section7.6](https://webhomes.maths.ed.ac.uk/hall/Xpress/Xpress-booka4.pdf). Original optimization teaching models unique task assignment, predecessor order and maximum station load. Its amplifier example and numerical solution are not reproduced.
- [Christian Blum · Iterative Beam Search for Simple Assembly Line Balancing with a Fixed Number of Work Stations · 2010](https://arxiv.org/pdf/1012.3273). Author’s original paper defines the fixed-station problem and precedence/cycle constraints. Its algorithmic benchmark results are not evidence about this workshop.
- [Cao, Li, Liu and Zhang · An Optimization Model for Assembly Line Balancing Problem with Uncertain Cycle Time · 2020](https://onlinelibrary.wiley.com/doi/10.1155/2020/2785278). Original research explicitly distinguishes spatial constraints from pairs of tasks that cannot share a station. Its uncertainty model and aircraft examples are not imported.
- [Zhang, Kucukkoc and Karaoglan · Rebalancing of mixed-model two-sided assembly lines with incompatible task groups · 2016](https://ikucukkoc.baun.edu.tr/dokumanlar/2016_Zhang_Kucukkoc_Karaoglan.pdf). Author-hosted original proceedings paper distinguishes fixed-station cycle minimisation and practical compatibility restrictions. Its two-sided simultaneous-task restriction differs from this case’s explicit same-station prohibition.
- [El Belghiti, Mouloud and Soulhi · A Feasibility-Oriented Heuristic for Garment Assembly Line Balancing with Machine Compatibility Constraints · 2026](https://www.mdpi.com/2413-4155/8/11/341). Original modeling study distinguishes a workload lower bound from technological feasibility and specifies indivisible tasks and compatibility. No garment benchmark values, heuristic results or real-workplace validation are transferred.
