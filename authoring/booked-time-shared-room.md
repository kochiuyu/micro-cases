# A full appointment book. A workable morning?

<!-- legacy-case-id: 336 -->

HSP-28 · Fictional nonmedical wellness studio · 15–20 minutes · Coupled resource scheduling · Service phases · Protected turnaround

![A spa scheduler and two practitioners review an unlabelled appointment board outside a serene treatment room.](../booked-time-shared-room-scene.jpg)

## An appointment reserves more than one calendar

Mindbody’s spa scheduling discussion identifies coordination of practitioners, rooms and service duration as a resource-allocation problem. Square’s processing-time documentation distinguishes stages within an appointment. These are vendors’ descriptions of their own operational concepts, not evidence that a particular product or schedule is best.

Google’s scheduling documentation illustrates sequence and non-overlap constraints. HSE’s beauty-service guidance separately treats safety controls and cleaning as planned work, not time to erase for utilisation. The durations and staffing below are invented site-specific classroom assumptions; no treatment or hygiene procedure is being prescribed.

## Opening decision

**Fictional classroom situation.** A nonmedical wellness studio must schedule four adult appointments between 09:00 and 12:00: two Long relaxation services, labelled L1 and L2, and two Short refresh services, S1 and S2. Two equally qualified practitioners, P and Q, must each provide one L and one S. Each has an ordinary private room. All clients agree to any confirmed start within the morning; no exact times have been promised. No extra appointments, practitioner sharing or shorter services may be introduced.

An L occupies its practitioner continuously for sixty minutes; an S for forty-five. Each requires ten further uninterrupted practitioner minutes immediately afterward for the ordinary-room reset and records. Both practitioners take an uninterrupted, fixed break from 10:15 to 10:30. Service and reset cannot cross that break. All required consultation, movement and client transition time is already included in service durations. Clients leave at actual service completion, not at the end of an artificial slot.

Uniform blocks seventy-five minutes per appointment on each practitioner’s calendar, including required reset and any unused allowance. Its proposed starts are 09:00 and 10:30 for both practitioners. Duration-specific blocks seventy minutes for L and fifty-five for S, retaining the fixed break and permitting idle time rather than adding clients. The same four services, price, staff pay, consent, access supports and safety standards apply. Neither design assumes a practitioner can serve two clients at once.

The initial draft places L first and S second for both P and Q. Based only on practitioner time, this fits either design. The operations lead has not yet supplied the phase-level map of a specialist room shared by both service types. The scheduler must compare the calendar designs provisionally, then check every required resource before confirming times. The studio’s aim is a feasible, unhurried service day, not maximum apparent occupancy.

## Evidence

| Service | Continuous practitioner service | Immediate practitioner reset | Duration-specific block | Uniform block |
| --- | --- | --- | --- | --- |
| L | 60 minutes | 10 minutes | 70 minutes | 75 minutes |
| S | 45 minutes | 10 minutes | 55 minutes | 75 minutes |

**Student question:** Which calendar design would you provisionally use for these four appointments? Compare the practitioner time it blocks, preserve the break and resets, and explain why that calculation alone cannot establish a feasible appointment book.

## Round two

The specialist room is now mapped. Each L requires it during its **first twenty minutes**, then continues in that practitioner’s ordinary room for forty minutes. Each S starts in the ordinary room for thirty minutes and requires the specialist room during its **final fifteen minutes**. Its practitioner stays with the same client continuously throughout. Phases cannot change order or pause, and transitions are included in the stated times.

The specialist room accommodates one client-practitioner pair at a time. Immediately after each room-use phase, a separate, trained room attendant needs ten uninterrupted minutes to complete its required hygiene turnaround. The room is unavailable throughout that period. The attendant is funded, has no competing duties during the proposed service/turnaround periods, and takes the same 10:15–10:30 break. All rooms are ready at 09:00; every final reset must finish by 12:00. These times are stipulated requirements, not universal cleaning standards.

The specialist-room turnaround is separate from the practitioner’s ten-minute ordinary-room reset and records after the whole service. They may overlap because different workers and spaces are involved. The two ordinary rooms remain assigned to their own practitioners and have no other bookings. No extra room, substitute procedure, overtime or reduced hygiene period is available.

Both L appointments starting at 09:00 would demand the same specialist room from 09:00 to 09:20. The draft therefore fails despite fitting both practitioner calendars. The scheduler may reorder each practitioner’s L and S and choose feasible starts under the selected design; clients remain flexible. The service mix, break and all duration rules stay fixed.

**Student question:** Produce one feasible appointment schedule and the separate specialist-room timeline, including every turnaround. Does the reveal force you to abandon Uniform, or is resource coordination a separate requirement under either calendar design?

## Answer the calendar comparison

Prefer **Duration-specific** for transparent resource accounting, while treating free time as slack rather than an automatic invitation to sell more. Each practitioner needs sixty + ten + forty-five + ten = **125 minutes** for service and reset, plus fifteen break minutes. Uniform blocks 150 appointment minutes plus the same break: 165 minutes. Duration-specific blocks 140 including break, releasing twenty-five calendar minutes per practitioner, fifty in total.

That does not save fifty paid labour minutes or create a saleable fifty-minute appointment. Staff pay and demand are fixed, and free intervals may be fragmented. Uniform can be a reasonable simpler template with extra allowance. Neither design is feasible merely because each practitioner has enough total minutes: the shared-room phases also have to fit.

## A feasible practitioner schedule

Keep P on **L1 at 09:00–10:00**, followed by reset 10:00–10:10; then S1 at 10:30–11:15, followed by reset 11:15–11:25. Put Q on **S2 at 09:00–09:45**, followed by reset 09:45–09:55; then L2 at 10:30–11:30, followed by reset 11:30–11:40. Both retain the full 10:15–10:30 break.

All four clients receive their complete service with one practitioner. Duration-specific can show these exact blocks and free intervals. Uniform can use the same starts and service order inside 09:00–10:15 and 10:30–11:45 blocks. Thus the reveal requires correcting the room collision, not necessarily abandoning Uniform.

## Check the shared room independently

Specialist room: L1 uses 09:00–09:20; attendant turnaround 09:20–09:30. S2 uses 09:30–09:45; turnaround 09:45–09:55. L2 uses 10:30–10:50; turnaround 10:50–11:00. S1 uses 11:00–11:15; turnaround 11:15–11:25. Every next use begins only after the preceding turnaround ends.

Room-use time totals twenty + fifteen + twenty + fifteen = **70 minutes**, and four turnarounds total forty, so the room is blocked for 110 minutes. Total capacity alone did not prevent the original 09:00 clash. The attendant’s work does not overlap its break, and each ten-minute task has an available worker. The final specialist reset ends at 11:25; the final practitioner reset ends at 11:40.

## Distinguish slack from permission

Do not reserve the specialist room for the whole L or S when it is only needed for a phase, unless a real safety or privacy requirement demands that longer reservation. Equally, do not call it available while hygiene turnaround is underway. Use linked records for the practitioner, ordinary room, specialist-room phase and attendant work.

This deterministic trace proves feasibility for the supplied times, not robustness to late arrivals or variable service needs. In practice, confirm actual requirements, appropriate buffers and procedures for delays without cutting care, breaks or hygiene. The remaining slack is not a guarantee that any extra booking fits. Confirm exact client start and finish times only after the resource check.

## Instructor note

Have students first calculate 150 versus 125 appointment/reset minutes per practitioner, then expose the 09:00 shared-room conflict. Require both a practitioner timeline and the room’s use-plus-turnaround timeline. Reject answers that overlap room hygiene, treat a practitioner as free during a service phase, or skip the fixed break.

Unlike OPS-07, this is not queue pooling or adding counters. Unlike HSP-06, it is not a static match between parties and tables. Different resources are needed at different phases. All services are nonmedical and fictional; no clinical, treatment or sanitation instructions are taught. The example is a feasible schedule, not proof of earliest possible completion or general software performance.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional nonmedical service-scheduling exercise. Four clients, L 1/L 2 sixty minutes and S 1/S 2 forty-five minutes; P/Q each do one of each continuously. Ten-minute immediate practitioner ordinary-room reset/records follows every service. Fixed break 10:15–10:30 for practitioners and dedicated specialist-room attendant; no tasks cross it. L uses specialist room first 20 minutes, S final 15 after 30 ordinary-room minutes. Ten-minute separate attendant turnaround follows each specialist use. Two ordinary rooms, one per practitioner, no other bookings; transitions included. Feasible P:L 09:00,S 10:30;Q:S 09:00,L 10:30. Specialist occupied 09:00–09:30,09:30–09:55,10:30–11:00,11:00–11:25 including turnarounds. Final practitioner reset 11:40. Uniform 75-minute blocks also fit this order. Calendar savings 25 per practitioner, not paid labour savings. All times invented; no universal hygiene or break standard asserted.

- [Mindbody · Booking and Scheduling Software for Spas · updated March 2026](https://www.mindbodyonline.com/business/education/blog/booking-and-scheduling-software-spas). Vendor’s own operational discussion identifies linked practitioner, room and duration constraints. Marketing performance claims and product comparisons are not treated as independent evidence.
- [Square · Create and edit processing time for appointments](https://squareup.com/help/us/en/article/6756-add-gap-times-to-your-square-appointments-services). Official product documentation distinguishes initial, processing and final durations. Its example permits provider downtime; this case explicitly does not free the practitioner during service.
- [Google OR-Tools · The Job Shop Problem](https://developers.google.com/optimization/scheduling/job_shop). Official technical explanation of ordered tasks and exclusive resource occupancy. Used as a scheduling analogy, not a claim that people or wellness services are interchangeable machines.
- [HSE · COSHH and beauticians: key messages](https://www.hse.gov.uk/coshh/industry/beauty.htm). Regulator guidance stresses task-dependent controls. Supports retaining assessed requirements rather than treating schedule pressure as permission to remove them.
- [HSE · Nail bars and other beauty services, SR13 · March 2025](https://www.hse.gov.uk/pubns/guidance/sr13.pdf). Public guidance includes cleaning, equipment maintenance, training and supervision. It does not specify this fictional ten-minute turnover or fifteen-minute break; its nail-service procedures are not transplanted.
