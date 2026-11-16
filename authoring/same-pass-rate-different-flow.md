# Ninety-eight per cent at every stage. What leaves the line?

<!-- legacy-case-id: 304 -->

OPS-26 · Hong Kong · 15–20 minutes · First-pass yield · Rework flow · End-to-end output

![A production manager and technician inspect display-stand components between fitting and finishing benches, with a small repair bench nearby.](../same-pass-rate-different-flow-scene.jpg)

## A pass after repair is not a first pass

Quality guidance distinguishes units accepted on their first attempt from units accepted only after repair and retesting. A high final acceptance figure can hide substantial extra work. A chain of stage percentages is useful only when the numerator, denominator and treatment of rework are compatible.

This fictional two-stage production exercise uses explicit flow assumptions. It is not a reported factory result, a safety trade-off or a claim that failures at different stages are statistically independent.

## Opening decision

You manage a fictional Hong Kong producer of reusable display stands. A fixed batch of 10,000 units will pass through fitting stage A and finishing stage B. Only units that meet the unchanged specification at A enter B, and only units that meet the final specification can ship. No defect is waived. Choose one of two already funded process improvements, each costing HK$20,000. The budget cannot fund both.

The decision objective is the greatest expected number of conforming finished units from this fixed batch by the deadline. First-pass performance and rework workload must also be reported, but they are not the primary ranking criterion. Both projects, all processing and all specified rework fit within the same safe staffing, capacity and deadline. No extra starts, overtime or selling-price difference are allowed. The quoted project costs cover all differences in spending; no cash saving per avoided rework is supplied.

The summary dashboard reports 98% pass at A and 98% pass at B. Project A raises A’s reported figure to 99%, leaving B unchanged. Project B raises B’s reported figure to 99%, leaving A unchanged. The labels do not say whether a pass is first-time acceptance or acceptance after rework. The underlying route sheets are available for the second round. Treat the summary as incomplete evidence, not proof that 98% of all starts ship.

## Evidence

| Same 10,000 starts | Stage A reported pass | Stage B reported pass | Project cost |
| --- | --- | --- | --- |
| No improvement | 98% | 98% | None |
| Project A | 99% | 98% | HK$20,000 |
| Project B | 98% | 99% | HK$20,000 |

**Student question:** Would the dashboard justify preferring Project A, Project B or neither yet for finished output? State the missing definition you need before multiplying its percentages.

## Round two

The route sheets reveal different measures. At A, the reported figure includes successful rework. Of 10,000 starts, 9,000 pass first time, 800 go through one successful repair and retest, and 200 are scrapped directly. With Project A, 9,100 pass first time, 800 are successfully reworked and 100 are scrapped. No other A routes exist.

At B, the reported figure is first-pass acceptance divided by all units entering B. Without Project B, 98% pass first time. Each of the remaining 2% receives one rework attempt: half then pass and half are scrapped. Project B raises first-pass acceptance to 99%; half of the remaining 1% pass after one attempt, and half are scrapped. These rates apply equally to units that passed A first time and those reworked at A, under either project.

All accepted A units enter B once initially; rework attempts are not additional new units in the denominator. No work is unfinished at the deadline. These are supplied planning rates and flows, not estimates from a sample. Count unique finished units, units with no rework anywhere, and rework attempts. All costs, safe capacity and the output-first objective remain as stated.

**Student question:** Using the route sheets, which project gives more conforming finished units, and how would you report its output and no-rework yield without confusing the two?

## The opening percentages do not settle the choice

If both stage figures were compatible final-acceptance proportions of each stage’s incoming cohort, either change from 98% to 99% would give the same product. But the summary does not establish that condition. The defensible first-round response is to withhold a ranking and ask what a pass counts, what enters each denominator and where failed units go.

## Reconcile the unchanged line

A sends 9,000 + 800 = 9,800 units to B. B accepts 98% first time plus half of the remaining 2%, a final acceptance rate of 99%. Baseline finished output is 9,800 × 0.99 = 9,702. Units with no rework anywhere are 9,000 × 0.98 = 8,820, or 88.20% of starts. Multiplying the two dashboard figures gives 96.04%, neither baseline final yield nor no-rework yield.

## Compare finished units on one basis

Project A sends 9,100 + 800 = 9,900 units to B; B still finally accepts 99%. Finished output is 9,801. Project B leaves A output at 9,800; B finally accepts 99% + half of 1% = 99.5%. Finished output is 9,751. Choose Project A under the supplied output-first objective: 50 more finished units than B, at equal total cost and feasible capacity.

## Report the hidden work too

Project A has 9,100 × 0.98 = 8,918 units with no rework, a no-rework yield of 89.18%; its final yield is 98.01%. Project B has 9,000 × 0.99 = 8,910 no-rework units, or 89.10%, and final yield 97.51%. The same B first-pass rates apply to the clean A cohort by explicit assumption, so no unstated independence assumption is needed.

Project A requires 800 A rework attempts and 9,900 × 2% = 198 B attempts, total 998. Project B requires 800 + 9,800 × 1% = 898 attempts. These are attempts, not necessarily different units: a unit may be reworked at both stages. B therefore reduces rework load more, but that does not overturn A under the supplied objective, equal spending and adequate capacity.

## Instructor note

Give three minutes to critique the dashboard, then five to draw the two routes and calculate outputs. Ask for a reconciliation of every start into final output or scrap. Use a separate colour for units with no rework. Finish by discussing why the preferred project could change under a different objective or a genuine rework-capacity constraint, neither of which is present here.

Do not bypass inspection or ship failed units to improve a percentage. This is yield accounting across stages, not a control-chart inference, machine-speed exercise or a particular mistake-proofing design. Percentages are planning assumptions, and the clean-cohort application is explicit. A better headline percentage is not enough to establish a better end-to-end flow.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All production flows, rates, costs and project effects are fictional. Conforming output includes successfully reworked units; no-rework output excludes them. Stage B rates are explicitly conditional on either incoming cohort. Capacity, safety and specification remain fixed. Two ASQ sources are related professional guidance.

- [ASQ, Quality Glossary: First pass yield](https://asq.org/quality-resources/quality-glossary/f). Defines first-pass acceptance to exclude reruns, retesting and repair. Supports an explicit no-rework numerator.
- [Minitab, Throughput yield and rolled throughput yield](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/six-sigma/supporting-topics/what-are-throughput-yield-ytp-and-rolled-throughput-yield-yrt/). Explains serial-stage yield and no-rework treatment. The case supplies conditional cohort rates rather than assuming arbitrary marginal rates may be multiplied.
- [ASQ, Cost of Quality](https://asq.org/quality-resources/cost-of-quality). Distinguishes prevention, appraisal, scrap and rework costs. Supports reporting repair workload without inventing a cash saving.
- [Michael Ballé, How Does Lean Apply in a Job Shop?](https://www.lean.org/the-lean-post/articles/how-does-lean-apply-in-a-job-shop/). Original practitioner discussion emphasises recording rework and investigating causes with workers. No claimed factory outcome is borrowed.
- [iSixSigma, Using Effective Metrics to Measure Production Test Flow](https://www.isixsigma.com/metrics-methodology/using-effective-metrics-measure-production-test-flow/). Original practitioner article separates first-time entries, reruns, passing output and unfinished work. Used for flow-record definitions, not its broader claims about early-stage improvements or profitability.
