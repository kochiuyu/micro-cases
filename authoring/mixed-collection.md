# Fewer changeovers. A later customer.

<!-- legacy-case-id: 42 -->

OPS-04 · Hong Kong · 10–15 minutes · Operations · Batch size · Production scheduling

![A workshop supervisor and printer discuss trays of leaf and flower gift labels beside a divided collection box.](../mixed-collection-scene.jpg)

## In the news

PolyU’s report of a technical visit to HKPC on 18 October 2024 described a knitted-garment microfactory demonstration that supported small-batch production. The report illustrates interest in manufacturing flexibility; it is not an independently audited estimate of business performance.

HKPC’s production-planning services also describe the challenge of smaller orders, more product varieties and changing delivery schedules. Our label workshop and all timings below are fictional. The decision is about scheduling an existing machine, not buying new technology.

## Opening decision

Fictional classroom situation. You supervise a Hong Kong gift-label workshop. A confirmed order requires 200 labels of design A and 200 of design B. There is no finished stock. All materials are ready, and one machine has 360 available minutes in the shift.

Each good label takes 0.5 minute to produce. Every run, including the first, requires 30 minutes of setup and checking before production. A run is a continuous stretch of one design; adjacent stretches of the same design count as one run.

Assume no breakdowns, defects, shared-worker constraints or extra packing delays. The stated setup includes the required checks and cannot be skipped. Time starts at minute zero, before the first setup.

Your summary sheet shows two plans. Both produce all 400 labels within the shift. The two-run plan preserves more time for unexpected work, but the summary has not shown collection details.

## Evidence

| Plan | Sequence | Total time | Unused shift time |
|---|---|---|---|
| Two runs | A200 → B200 | 200 production + 60 setup = 260 min | 100 min |
| Four runs | A100 → B100 → A100 → B100 | 200 production + 120 setup = 320 min | 40 min |

Both produce the same quantity. Setup checks cannot be skipped.

**Student question:** Which plan would you approve: two long runs or four shorter runs? What delivery information should you check before choosing?

## Round two

The customer’s confirmed collection plan requires 100 A and 100 B by minute 180. The remaining 100 of each can be collected at shift end, minute 360. The first collection needs both designs, not any 200 labels.

This requirement was on the order but omitted from the supervisor’s summary. No production has started. You can revise the sequence now; changing the customer’s collection time would require the customer’s agreement, which has not been obtained.

The customer can collect completed labels while the machine continues its run. Collection causes no extra delay in this simplified exercise. All other time assumptions remain unchanged.

**Student question:** Would you keep two runs, use four, or propose another sequence? Show when the customer can collect 100 of each design, and whether the full order still finishes within the shift.

## Find when the required mix is ready

Two runs: setup A takes minutes 0–30; A200 finishes at minute 130. Setup B takes minutes 130–160. The first B100 takes another 50 minutes, so 100 of both designs are available only at minute 210, 30 minutes late.

Four runs: setup A and A100 take 30 + 50 = 80 minutes. Setup B and B100 take another 80. The first mixed collection is ready at minute 160, 20 minutes before the deadline. The full order finishes at minute 320.

Reversing the two long runs merely changes which design arrives late. Total output by shift end is not enough to satisfy the earlier mixed collection.

## Can three runs do better?

Try A100 → B200 → A100. A100 is ready at minute 80. After B setup, B100 is ready at minute 160, so the first collection can leave on time while the B run continues.

B200 finishes at minute 210. The final A setup and A100 take another 80 minutes. Everything finishes at minute 290, leaving 70 minutes of shift time.

This three-run plan meets the same promise with 30 fewer setup minutes than four runs. It shows why the initial menu is not the whole solution. Other feasible sequences may exist; the case does not establish a universal best batch size.

## Choose against the promise

Use a feasible mixed sequence, such as the three-run plan, when the minute-180 commitment stands. Four runs also meet the stated deadlines, though they use more setup time under these assumptions.

Two long runs preserve the most slack, but require an agreed later first collection. Do not silently redefine the promise or assume the customer accepts a delay. No delay penalty or profit estimate is provided, so we cannot price that negotiation.

For future work, investigate safe ways to reduce setup time. Preparing materials outside machine downtime can help in some settings, but no reduction is assumed here, and quality or safety checks remain necessary.

Key idea: schedule the required mix by the required time, not just the daily total.

## Instructor note

Allow 2 minutes for the first comparison, 3 for the collection reveal and 5–7 for drawing a timeline. Ask for the time when the first 100 of each design exist, not just when production ends. Let students propose the three-run sequence before opening that explanation. Keep the first-run setup and partial-run collection assumptions visible. Do not label four runs optimal or confuse this single-machine sequencing exercise with a bottleneck investment decision.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The workshop, order, run times and collection requirement are invented. The PolyU report concerns a 2024 technical visit, not this workshop or a promised performance gain. Undated explanatory/service pages checked 14 November 2026. Setup and quality assumptions are for scheduling arithmetic, not machine-operation instructions.

1. [PolyU · Technical visit to HKPC, 18 October 2024](https://www.polyu.edu.hk/ise/about-ise/alumni/milesaa/activities_index/activities_past/2024/technical-visit-to-hkpc-future-manufacturing-hall-and-ai-applications-hall/) — Visit report describes a knitted-garment microfactory demonstration and small-batch capability. Its reported performance figures are not used.
2. [HKPC · Production Capacity Optimisation](https://www.hkpc.org/en/our-services/green-smart-living/corporate-sustainability/production-capacity-optimisation) — Describes planning for small batches, product variety and changing delivery schedules. Undated service description, not an evaluation of software benefits.
3. [Lean Enterprise Institute · Every Product Every Interval](https://www.lean.org/lexicon-terms/every-product-every-interval/) — Explains production frequency, variety and changeover-time constraints. Undated explanatory guidance, not a claim that the smallest batch is always optimal.
4. [Lean Enterprise Institute · Single Minute Exchange of Die](https://www.lean.org/lexicon-terms/single-minute-exchange-of-die/) — Distinguishes stopped-machine setup from preparatory work that can occur outside downtime. No specific reduction is assumed in the case.
5. [Lean Enterprise Institute · Heijunka](https://www.lean.org/lexicon-terms/heijunka/) — Discusses production mix and the contrast between long runs and repeated mixed sequences. Its example and claimed performance effects are not imported.
