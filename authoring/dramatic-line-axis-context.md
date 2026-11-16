# The line looks dramatic. What does the axis say?

<!-- legacy-case-id: 332 -->

IS-28 · Hong Kong · 15–20 minutes · Visual encoding · Axis choice · Decision context

![An analyst and a manager compare two chart layouts at a desk.](../dramatic-line-axis-context-scene.jpg)

## A correct value is not the whole visual message

Visualisation experiments show that axis choices can affect the perceived importance of a change, even when the numbers are readable. Guidance distinguishes magnifying a trend from representing an absolute level and does not require every line chart to begin at zero. The cost series, display proposals and viewer check below are original fiction.

## Opening decision

A Hong Kong facilities team is preparing a five-minute weekly cost briefing. Its six weekly totals have been checked against the same approved ledger version and use the same cost categories, currency and weekly period. There are no missing weeks or disputed values. The analyst must choose a display, not repair the data. The briefing should let managers see both the recent movement and its budget significance; no cause or forecast has been established.

A uses one unfilled line chart of weekly cost with a clearly labelled vertical axis from HK$99,500 to HK$102,500, in HK$500 steps. Every week and its point are labelled. The narrow scale makes small movements easy to see and uses one panel. B uses two equally sized, separately labelled panels: absolute weekly cost from HK$0 to HK$110,000, and change from week 1 from HK$0 to HK$3,000. The panels share the same six evenly spaced weeks, not a dual axis. B also states the latest cost, the change in dollars and the percentage change from week 1. It takes more space but makes the level and movement explicit.

All panels have the same plotting width and height, straight line segments, visible data markers, no filled area, no smoothing and no extrapolation. Tick labels specify HK dollars. B’s change panel contains 0, 400, 200, 800, 1,400 and 2,000; those are differences from week 1, not total spending. Both designs use exactly the verified costs in the exhibit. The analyst has not yet added the organisation’s escalation trigger to either design.

## Evidence

| Week | Weekly cost, HK$ | Change from week 1, HK$ |
|---|---:|---:|
| 1 | 100,000 | 0 |
| 2 | 100,400 | 400 |
| 3 | 100,200 | 200 |
| 4 | 100,800 | 800 |
| 5 | 101,400 | 1,400 |
| 6 | 102,000 | 2,000 |

A cost axis: 99,500–102,500. B separate panels: cost 0–110,000 and change 0–3,000. Same plotting dimensions and six evenly spaced weeks. Latest cost HK$102,000; increase HK$2,000 / 2% from week 1.

**Student question:** Which display would you use for the briefing, A or B? Explain how you would keep the movement visible without letting the chart’s apparent steepness stand in for the size or importance of the cost change.

## Round two

In a small usability check, six colleagues see A first and then B. After A, four describe the rise as at least 10% and say it looks like an immediate budget threat. After B, all six correctly state the HK$2,000, 2% increase. This is informal, sequential feedback, not a randomised experiment: order, annotations and the second view could all matter. It reveals a comprehension risk in this briefing, not a measured causal effect of cropping alone or proof that every viewer will misread A.

The finance manager confirms the existing rule: a verified weekly total at or above HK$108,000 triggers a formal cost review. It is a review threshold, not permission to ignore smaller changes, and not a forecast. That level is outside A’s displayed range but within B’s absolute-cost range. The latest total is HK$102,000, which is HK$6,000 below the trigger. None of the six weeks reaches it. The analyst can now add a labelled HK$108,000 horizontal reference line to B’s absolute panel, without changing any data or scale.

A can also be redesigned with a wider cost axis and a clear threshold annotation; no one is forbidden to use a nonzero baseline. The cost movement still merits routine monitoring and investigation proportionate to its context. No evidence here explains the cause, predicts the next week, or establishes that a 2% rise is economically unimportant. The choice is how to communicate the verified change and the actual review rule together.

**Student question:** How would you revise the briefing after the viewer check and threshold information? State the actual change and distance from the trigger, and explain when a cropped line-chart axis can still be appropriate.

## Answer the first decision: retain level and change

I would use B for this mixed-purpose briefing. Its separate views support reading the absolute cost and the small movement without making viewers infer a percentage from the angle of a line. A is not numerically false, and its crop can be useful for detailed trend inspection. But a labelled axis alone does not guarantee that a hurried audience interprets the magnitude correctly. B’s extra space earns its place only if the panels and units remain easy to distinguish.

## Answer the revealed decision: show the decision reference

Retain B, add the HK$108,000 reference line to the absolute panel and state: latest weekly cost HK$102,000; up HK$2,000 or 2% from week 1; HK$6,000 below the formal-review trigger. Continue routine monitoring rather than claim that the trigger has been reached or that no concern exists. A revised, clearly labelled nonzero-axis chart that includes the threshold and explicit change could also work; test comprehension rather than enforce a blanket zero rule.

## What the geometry amplifies

The actual increase is (102,000 − 100,000)/100,000 = 2%. On A, that HK$2,000 spans two-thirds of a HK$3,000 vertical range. On B’s absolute panel it spans about 1.82% of a HK$110,000 range. These fractions describe chart height, not economic growth. B’s change panel deliberately magnifies movement again, but explicitly labels it as change from a baseline and pairs it with the level. Neither a steep nor a flat line establishes business significance.

## Choose a scale for the task

A cropped line chart can reveal small but important movement when the units, scale, baseline and relevant decision context are clear. A zero baseline can obscure such movement. Conversely, a crop that hides a relevant threshold or encourages exaggerated magnitude is a poor fit for this briefing. Do not convert A into truncated bars: bar lengths normally encode magnitude from zero. Avoid double axes, decorative area fills and unexplained scale changes between comparable panels.

## Instructor note

Have learners reconstruct the two axis ranges from the exhibit and calculate the change before revealing the trigger. This case fixes data lineage and varies visual encoding; unlike a reference-price frame, the issue is quantitative scale and task context. The six-viewer check bundles order and design differences and cannot isolate causality. Ask a fresh reader to report latest level, dollar change, percent change and trigger status. Do not grade “all axes must start at zero” as the lesson or treat the trigger as a statistical control limit.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Every value, viewer response, threshold and briefing is fictional. The six weekly costs are 100000, 100400, 100200, 100800, 101400 and 102000 Hong Kong dollars. Same verified ledger, scope and weekly unit; no missing periods, inflation adjustment, per-unit claim or forecast. Differences from week 1 are 0, 400, 200, 800, 1400 and 2000. Endpoint increase is 2000/100000 = 0.02 = 2%. A spans 102500−99500 = 3000; 2000/3000 = two-thirds. B absolute range 110000 gives 2000/110000 ≈ 1.82% of chart height, not a 1.82% cost change. Trigger gap 108000−102000 = 6000. All six observations are below the trigger. B’s change panel is a separate baseline-difference view, not a dual-axis plot. The usability check uses the same six people in a fixed order and changes several presentation features; no causal or population estimate follows. Sources discuss experiments or design guidance, not this firm’s cost importance or review policy.

- [Correll, Bertini and Franconeri: Truncating the Y-Axis: Threat or Menace?, CHI 2020](https://arxiv.org/pdf/1907.02035). Original experimental paper. Truncation affects subjective effect importance across tested designs; authors reject a universal zero-baseline rule and describe domain-context limitations.
- [Pandey and colleagues: How Deceptive are Deceptive Visualizations?, CHI 2015](https://www.cs.rpi.edu/~cutler/classes/visualization/S24/papers/2015_Pandey_Deceptive_Visualization.pdf). Original experiments on distortion. Truncation treatment uses bars; the line treatment changes aspect ratio. Supports caution about encoding, not a direct estimate for this case’s cropped line.
- [Office for National Statistics: Axes and gridlines](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines). Primary design guidance permits appropriate cropping for line charts and recommends extending axes and annotating relevant targets. Distinguishes bars and area charts.
- [Office for National Statistics: Line chart](https://service-manual.ons.gov.uk/data-visualisation/chart-types/line-chart). Primary design guidance on time trends, missing values, comparison context and annotations. Related to the axes guidance, not independent experimental evidence.
- [European data portal: Scales in line charts](https://data.europa.eu/apps/data-visualisation-guide/scales-in-line-charts). Primary institutional design guidance discusses why zero may be uninformative or hide meaningful changes. Its research discussion overlaps Correll and colleagues, not a separate replication.
