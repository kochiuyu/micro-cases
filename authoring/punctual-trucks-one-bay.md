# Two punctual trucks. One unloading bay.

<!-- legacy-case-id: 436 -->

OPS-37 · Hong Kong · 15–20 minutes · Dock appointments · Resource occupancy · Truck turnaround

![Two adult event-logistics coordinators compare a plain appointment sheet beside one marked unloading bay, with two stationary unbranded trucks safely separated from people.](../punctual-trucks-one-bay-scene.jpg)

## Arrival is one timestamp, not the whole visit

Truck-appointment research models receiving capacity and service durations alongside arrival slots. Operational reports distinguish time at a facility from particular waiting or handling activities. The two-truck example below is fictional: punctual arrival can coexist with avoidable waiting when a bay remains occupied.

## Opening decision

You dispatch two inbound trucks to a fictional Hong Kong event-supply warehouse tomorrow. Truck A carries display frames; B carries boxed fabric. There is one suitable unloading bay and one fully funded handling team. The bay is ready at 9:00 a.m.; both loads must be received and the bay safely cleared by 10:30.

Choose C, close appointments: A at 9:00 and B at 9:30; or S, spaced appointments: A at 9:00 and B at 10:00. A must go first because its receipt is needed for downstream preparation. Compare only these two schedules; neither truck may arrive before its assigned appointment.

Fixed classroom travel estimates are twenty minutes for A and thirty minutes for B. Each truck departs its origin to arrive exactly on time under either plan. Later departure for B creates no extra origin waiting, cost or missed commitment: dispatch, loading and paid duty are planned accordingly before tomorrow’s work begins.

The same loads, qualified staff, safe methods and employment protections apply to both schedules. A lawful separate holding space and driver welfare access exist if B must wait. Nobody waits on a public road or unloads outside the bay. No extra bay, team, overtime or compressed checks are available.

The dispatcher has checked drive times but not the complete bay-occupancy durations. Management’s objective is first to finish both loads and safe clearance by 10:30, then minimise total waiting at the destination before bay service starts. No monetary value for waiting or dispatch change is supplied.

## Evidence

| Truck | C depart/arrive | S depart/arrive |
| --- | --- | --- |
| A | 8:40 / 9:00 | 8:40 / 9:00 |
| B | 9:00 / 9:30 | 9:30 / 10:00 |

**Student question:** Would you choose close or spaced appointments from arrival times alone? Name the missing intervals needed to calculate B’s actual service start and the time the bay becomes free after both trucks.

## Round two

The handling plan establishes A’s uninterrupted bay occupancy: twenty minutes of load-specific positioning and equipment setup, thirty minutes unloading and receipt, then ten minutes for safe release, departure manoeuvre and bay reset. All three stages occupy the only bay. No stage can be done in the holding space or before A arrives.

B requires five minutes of setup, twenty minutes unloading and receipt, then five minutes of safe release, departure manoeuvre and reset. These stages also occupy the bay continuously. The durations include all destination movements and checks relevant to this bounded comparison; there is no extra omitted travel between holding space and bay.

A starts bay service at 9:00 under both schedules. B starts only when it has arrived and A has completed all bay-clearance work. B cannot start setup alongside A’s unloading or clearance. The supplied durations are deterministic planning inputs, not universal targets or permission to rush actual work.

For this exercise, a truck’s visit ends when its clearance stage finishes. Waiting equals bay-service start minus arrival; visit time equals clearance finish minus arrival. The final clearance endpoint also establishes when the next truck could use the bay. No further arrivals occur within this test.

**Student question:** Draw both schedules including setup, unloading and clearance. Compare total destination waiting, total truck visit time and final bay-clear time. Which schedule meets the stated objective, and what does its result not prove about traffic uncertainty or system-wide cost?

## Debrief · Reserve the full occupation

A needs 20 + 30 + 10 = 60 minutes. Its setup runs 9:00–9:20, unloading and receipt 9:20–9:50, and clearance 9:50–10:00. The bay is not available at 9:50 merely because the goods have been removed.

B needs 5 + 20 + 5 = 30 minutes. Under either appointment plan, it starts at 10:00: setup until 10:05, unloading and receipt until 10:25, and clearance until 10:30. Both loads meet the stated deadline exactly; neither plan finishes earlier.

## Debrief · Count the waiting honestly

Under C, A waits zero minutes and B waits from 9:30 to 10:00: thirty minutes total, fifteen per truck on average. A’s visit lasts sixty minutes and B’s sixty, giving 120 truck-minutes at the destination. Both arrivals are nevertheless exactly punctual.

Under S, both trucks start immediately on arrival, so total destination waiting is zero. A’s visit lasts sixty minutes and B’s thirty, giving ninety truck-minutes. Spacing removes thirty destination waiting minutes without changing the ninety minutes of bay work or the 10:30 final clearance.

## Debrief · Choose within the objective

Choose S under the supplied rule: both schedules finish by 10:30, while S has less destination waiting. Its later B appointment does not mean later unloading. C asks B to arrive before the required resource can serve it; punctuality alone does not establish a well-designed appointment.

This is not proof that every truck should be called exactly at the previous completion time. The case deliberately holds travel and handling durations fixed. There is no spare time before the deadline. A real schedule needs evidence about variation, a feasible contingency and honest communication, not a reliability guarantee copied from this trace.

## Debrief · Avoid shifting the problem off the chart

B’s origin release can move without extra burden here because that flexibility is explicitly supplied. In practice, check origin labour, loading readiness, parking, duty limits and later jobs before claiming a system-wide improvement. Moving a queue elsewhere would not necessarily remove its cost. No currency saving is calculated in this case.

Record appointment, actual arrival, bay-service start, handling completion and safe-clearance finish separately. If only gate arrival is measured, C looks perfect while its receiving queue is invisible. If only unloading ends are measured, the schedule incorrectly offers the bay before the remaining safe release and reset are complete.

## Instructor note

Ask students to shade one bay timeline before calculating truck timelines. Both punctual trucks still compete for one non-overlapping resource. A occupies sixty minutes, B thirty; the difference between plans is B’s thirty-minute wait, not faster handling, a changed route or a second unloading team.

All trucks, times, costs and permissions are fictional. OPS-14 sequences geographic delivery windows; OPS-23 matches queued tickets to qualified staff. Here appointments must reserve a full setup–unload–clear interval at one destination. Safety guidance bounds the example, but no actual lifting procedure, driving-hours advice or legal approval is provided.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Two schedules only, Afirstfixed;C arrivals9:00/9:30, S9:00/10:00. Travels20/30minutes and originreleaseflexibility stipulated, no displaced duty/cost. A20setup+30unload+10clear=60,9:00–10:00. B5+20+5=30,10:00–10:30 underboth. C wait0+30=30 mean15, visits60+60=120;S wait0,visits60+30=90. Baywork90 andfinalclear10:30identical, bothdeadlineexact. Sminimisesdestinationwait undergivenrule, not globaloptimum or currencyreturn. Clearancecontainsallmovements/reset, no doublecount/no overlapping setup. One bay/team, safeholding/welfare,allrightsretained, no roadsidequeue/speeding/checkcompression. No stochasticdistribution/buffer/earlyarrival. Realvariationneedsseparateplanning. Allnumbersfiction.

- [García González and colleagues · Optimizing time slot allocation in complex multi-dock truck loading and unloading operations using evolutionary algorithms · 2026](https://link.springer.com/article/10.1007/s10489-026-07334-7). Original research models receiving slots, waiting space, station availability and service capacity. The case uses a much simpler deterministic trace, not the paper’s algorithm or performance claims.
- [UK HSE · Loading](https://www.hse.gov.uk/workplacetransport/information/loading.htm). Regulator’s substantive guidance discusses agreed unloading arrangements, safe waiting and preventing premature vehicle movement. General safety context, not a statement of Hong Kong law or a substitute for a competent site plan.
- [Hong Kong Labour Department · Guidance Notes on Prevention of Trapping Hazard of Tail Lifts · 2015](https://www.labour.gov.hk/eng/public/os/C/TailLifts_English.pdf). Official guidance includes communication, competent maintenance, instruction and supervision during loading activities. No equipment dimensions or operating procedure are transplanted; classroom durations are not legal or safe-speed standards.
- [FMCSA / Virginia Tech Transportation Institute · Driver Detention Times in Commercial Motor Vehicle Operations · December 2014](https://rosap.ntl.bts.gov/view/dot/193/dot_193_DS1.pdf). Original commissioned research explains its stop-time definition and inability to separate waiting from actual handling in the available data. Its historical two-hour classification is not adopted as a legal threshold or a measure of this warehouse’s waiting.
- [Port of Los Angeles · Control Tower launch announcement · February 2021](https://portoflosangeles.org/references/2021-news-releases/news_022421_controltower_launch). Port’s own announcement describes current turn-time snapshots and historical averages for planning. It is evidence of the tool’s stated measurement purpose, not independent proof of reduced queues or a present-day service guarantee.
