# A blank cell. A harmless average?

<!-- legacy-case-id: 140 -->

IS-12 · Hong Kong · 10–15 minutes · Missing data · Imputation · Sensitivity analysis

![An equipment-hire manager and analyst discuss an incomplete service register beside shelves of projectors and cable cases.](../blank-cell-scene.jpg)

## In the news

On 27 February 2026, Hong Kong’s Census and Statistics Department published its report on business use of information technology in 2025. Its release covered digital tools and business activities, not the accuracy of every operational record.

Our fictional equipment-hire counter asks a separate question: what should an analyst do when a digital log contains completed jobs but missing times? No data-quality failure is alleged in the official survey.

## Opening decision

**Fictional classroom situation.** A Hong Kong equipment-hire counter has 12 completed handovers in yesterday’s register. Every handover is included once. The timing form records active service minutes from starting the handover to finishing it, not queueing time. Eight durations were entered correctly; four duration fields are blank, although those jobs were completed.

A report is due at today’s capacity meeting. The manager normally requests an operational review if the mean across all completed handovers exceeds seven minutes. This is an internal investigation trigger, not a customer promise or an automatic staffing decision. The analyst cannot recover the four actual durations before the meeting.

Choose the main report: A gives the eight-record mean and clearly leaves the all-12 mean unresolved; B adds a separately labelled all-12 estimate, replacing each blank with the observed mean and stating that assumption. Both show the original log and the missing count. Neither may relabel invented values as measured, or claim that a complete-looking file proves the trigger was met or avoided.

## Evidence

| Completed handovers | Recorded active minutes |
|---|---|
| 1–4 | 4, 5, 5, 6 |
| 5–8 | 6, 7, 7, 8 |
| 9–12 | Missing, missing, missing, missing |

Recorded total: 48 minutes. Eight-record mean: 48 ÷ 8 = 6. Replacing each blank with 6 gives (48 + 24) ÷ 12 = 6, an estimate under that assumption. The reason for missing fields is not yet known.

**Student question:** Would you lead with A’s observed-only report or B’s explicitly assumed estimate? Explain what the six-minute figure describes and what you would tell the manager about the seven-minute review trigger.

## Round two

The shift log identifies six quiet-period and six busy-period handovers. All six quiet-period times were recorded: 4, 5, 5, 6, 6 and 7 minutes. Only two busy-period times were recorded: 7 and 8 minutes. All four blanks occurred in the busy period. Staff explain that they stopped filling in the duration field while handling the rush; completion records were still kept.

That explains a recording problem, but does not recover the missing times or establish that recorded and unrecorded busy-period jobs took the same time. A revised B could use the observed busy-period mean, 7.5 minutes, for each blank. Its assumption would be that the two recorded busy jobs represent the four unrecorded ones.

For a sensitivity check, the manager asks what the all-12 mean would be if the four missing jobs averaged eight minutes, or twelve minutes. These are hypothetical stress values, not measured times, probabilities or bounds. A and B can both include this check; the decision remains whether a conditional estimate should lead the report. There is no new time observation before the deadline.

**Student question:** After seeing where the blanks occurred, which report would you lead with? Compare the busy-period estimate with the two sensitivity scenarios, and state what the manager can and cannot conclude about the review trigger.

## A blank is not a zero

Eight measured durations total 48 minutes. Dividing by eight correctly describes the observed records. Dividing that same total by all 12 would give four minutes, but would silently count each missing duration as zero.

Replacing each blank with six retains the six-minute mean by construction. It adds an assumption, not four measurements. Keep missing indicators and original values so later readers can see which numbers were supplied.

## The recording process matters

Missingness is concentrated in a known busy period. This weakens an assumption that the recorded jobs simply stand for all jobs. It does not prove each missing job was slow, or tell us its duration.

Using busy-period information is more targeted than ignoring it. But only two busy times are observed, and those could still differ systematically from the four omitted ones. A group label alone does not establish that an imputation model is valid.

## Show how the conclusion moves

The observed busy mean is (7 + 8) ÷ 2 = 7.5 minutes. Imputing that for four jobs gives (48 + 4 × 7.5) ÷ 12 = 6.5 minutes. This is conditional on the within-busy-period representativeness assumption.

If the missing jobs average eight minutes, the overall mean is 80 ÷ 12, about 6.67. At twelve minutes it is 96 ÷ 12 = 8. The scenarios fall on opposite sides of seven. They are not a confidence interval or evidence that either scenario occurred.

For a deeper check, let m be the missing jobs’ average. The overall mean is (48 + 4m) ÷ 12. It equals seven when m = 9, and exceeds seven only when m exceeds nine. That threshold helps identify what evidence matters; it does not supply the missing answer.

## Make the report usable without false precision

A is defensible if the analyst will not place an inadequately supported all-job estimate in the headline. It should still show the scenario analysis and explain why the unresolved mean matters. “Six minutes among eight recorded jobs; four busy-period durations missing” is an honest measured statement.

B is defensible as an explicitly conditional planning estimate alongside the observed data and sensitivity check, not as confirmation that the seven-minute trigger was avoided. Both reports leave the actual all-12 mean unresolved. The manager may investigate the recording process now without pretending a staffing benefit has been proved.

For future handovers, pilot a workable duration-capture method with staff, preserve the same start/end definition, and monitor completeness by busy period. Do not force guessed entries merely to remove blanks. Later data can improve understanding but cannot automatically reconstruct yesterday’s missing measurements.

## Instructor note

Use three minutes for the first report choice, four for the missingness reveal and scenario calculations, then four for a one-sentence management headline. Ask groups to mark measured, imputed and hypothetical values in different ways. Keep the optional nine-minute threshold for the debrief.

The objective is item-level missing-data treatment and sensitivity, not IS-11’s customer-survey participation and launch decision. Every job is already in this register; only a numeric field is absent. IS-05’s units are consistent here. The pattern does not prove a formal missing-data mechanism or validate a model. Do not suggest multiple imputation would create certainty from 12 records or that an observational timing log estimates the causal effect of additional staff.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All service records, times, group assignments, deadline, internal trigger and report options are fictional teaching assumptions. Handovers 1–6 are quiet, 7–12 busy. Every handover completed and appears once; all eight measured durations are correct. Missing means unrecorded active service time, not zero or unfinished service. No actual missing time is recovered in round two. Observed busy mean 7.5 is an assumption-based donor summary, not validated imputation; eight/twelve-minute missing-job averages are stress scenarios without probabilities or bounds. The model describes yesterday’s 12 jobs, not future demand, causal staffing benefits or legal service standards. The seven-minute rule is a management investigation trigger only. No inferential confidence interval or uncertainty estimate is calculated from synthetic repetitions. The official Hong Kong release is context, not evidence of missingness in official statistics. Sources are optional and were read in the specified sections; the Statistics Canada and BTS documents are historical methodological guidance, not current Hong Kong obligations.

- [Census and Statistics Department · Business-sector IT usage report released · 27 February 2026](https://www.info.gov.hk/gia/general/202602/27/P2026022700354.htm). Dated context for business digital records. The case makes no claim that the survey had missing-data problems or that digital adoption guarantees data quality.
- [Statistics Canada · Quality Guidelines: Imputation · archived 2009 edition](https://www150.statcan.gc.ca/n1/pub/12-539-x/2009001/imputation-eng.htm). Principles, auxiliary variables and impact-on-estimates sections explain model assumptions, missingness information and retaining imputation indicators. Historical methodological guidance.
- [US Census Bureau · Statistical Quality Standard C2: Editing and Imputing Data](https://www.census.gov/about/policies/quality/standards/standardc2.html). C2-2 and C2-3 cover planning, testing, flags and preservation of original values. Applies within its stated US agency scope, not as a legal duty for the fictional counter.
- [Office for National Statistics · Item editing and imputation for Census 2021 · 8 November 2022](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/itemeditingandimputationprocessforcensus2021englandandwales). Sections 1–3 distinguish item nonresponse, modelling distributions and recovering individual truth. Census methods are not asserted to validate the case’s simple replacements.
- [US Bureau of Transportation Statistics · Guide to Good Statistical Practice: Processing Data · archived page dated 27 December 2011](https://www.bts.gov/archive/publications/bts_guide_to_statistical_policy/chapter4). Sections 4.1–4.2 discuss missing-value coding, reporting differences and documentation; 4.4 discusses sensitivity to assumptions. No transport-specific empirical rates are imported.
