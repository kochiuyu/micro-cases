# A persuasive dashboard. Can we trace the number?

<!-- legacy-case-id: 236 -->

IS-20 · Hong Kong · 10–15 minutes · Data lineage · Reproducibility · Analytical assurance

![Two stationery-distributor colleagues discuss plain source documents beside a laptop and ledger.](../trace-the-number-not-only-the-chart-scene.jpg)

## A real move towards reproducible analysis

On 15 April 2026, the UK Office for National Statistics reported that Living Costs and Food Survey processing had moved to a new reproducible analytical pipeline. This is a reported production milestone, not proof that automation removes every error. The Hong Kong distributor, dashboard and figures below are fictional.

## Opening decision

A Hong Kong stationery distributor uses a weekly dashboard to decide whether to extend a voluntary, nonessential promotional campaign. Its agreed rule is to consider an extension only when net incremental contribution exceeds HK$30,000. The rule is a management screen, not proof of causality or a promise to spend. Contribution here means recorded campaign sales less attributed goods, fulfilment and promotional costs. Those definitions and the eligible campaign dates have been approved. No staffing, customer entitlement or safety decision depends on this dashboard.

The current analyst copies authorised aggregate exports into a workbook and prepares a clear chart. The team must choose a production approach for the next twelve weekly reports. M retains a controlled manual workbook: preserve each source snapshot, document every adjustment, lock the released version and have a second analyst independently check it. R builds a scripted pipeline with versioned sources and transformations, a recorded software environment, tests, an independent rerun and a release owner. Neither plan publishes confidential data or bypasses access controls.

Both are affordable and adequately staffed. M costs HK$1,000 per weekly release, including review. R costs HK$6,000 once plus HK$400 per weekly release, including maintenance and review. These are complete incremental costs for twelve comparable releases; no setup cost is yet sunk. Either can be ready before next week. A separately funded review will validate the existing dashboard before any campaign decision; the campaign can pause without breaching a commitment. Choose the recurring process, not whether to act on an unverified number.

## Evidence

| Approach | Setup | Each release |
|---|---|---|
| M: controlled manual | HK$0 | HK$1,000 |
| R: reproducible pipeline | HK$6,000 | HK$400 |

**Student question:** Which production approach would you fund for twelve weekly releases? Explain what another analyst must be able to trace and reproduce before the chart informs a decision.

## Round two

The existing dashboard shows HK$34,000. A reviewer can add its displayed components and obtain the same total, but cannot identify the precise source export or recover an undocumented return adjustment. Two retained exports have the same campaign dates: the first omits a verified HK$7,000 return correction, while the second includes it. The dashboard did not record which version it used. The source owner confirms that the correction belongs to this campaign and must reduce its contribution; there are no other differences. Independently applying the approved definitions to the retained exports, the reviewer reconstructs HK$34,000 from the earlier version and HK$27,000 from the corrected version. The HK$7,000 correction is the sole difference between those reconstructed results. The old dashboard’s matching total does not prove its lineage. The independently reconstructed corrected figure is below the agreed screen. No campaign extension has been authorised.

This was a missing evidence trail in the old process, not a measured defect rate for either proposed plan. M would preserve an immutable authorised snapshot, a change log and signed workbook; R would preserve the same source identity and tie it to the exact transformation, tests, environment and output. Both must reconcile the correction and obtain independent approval. Re-running an undocumented workbook or automating the wrong source is not sufficient. The team must also record why the correction was accepted, not merely keep files with similar names.

For the twelve releases, M totals HK$12,000 and R HK$10,800. Both estimates assume the stated scope and volumes; additional requirements need a new estimate. R reduces the stated recurring effort but introduces a pipeline maintenance responsibility. M remains a feasible controlled method. Neither approach establishes that the campaign caused the recorded contribution or guarantees source data are correct.

**Student question:** After the source-version finding, which approach would you choose and what would you do with the current campaign recommendation? Calculate the twelve-release cost and specify a reproducible evidence trail, not just a matching total.

## Reconciliation is not provenance

Adding displayed cells checks one arithmetic relationship. It does not identify the source version or explain a transformation. Connect the authorised source snapshot, approved definition, adjustment reason, transformation version, reviewer and released output. Keep access restricted; traceability does not require public data.

## Separate the correction from the investment

The independently reconstructed export totals differ by HK$7,000: HK$34,000 versus HK$27,000, so the current figure does not meet the stated greater-than-HK$30,000 screen. Withdraw the unsupported recommendation and document the correction before reconsideration. Choosing R does not retroactively validate the old chart; choosing M does not permit retaining its undocumented method.

## Compare complete costs

M costs 12 × HK$1,000 = HK$12,000. R costs HK$6,000 + 12 × HK$400 = HK$10,800, HK$1,200 lower under the given assumptions. The equality point is ten releases: HK$6,000 divided by the HK$600 difference per release. Cost is one consideration alongside maintainability and evidence quality; do not invent an error probability or a savings guarantee.

## Instructor note

Ask an authorised colleague to regenerate the approved output from the preserved inputs and instructions, check the adjustment and inspect test failures. A matching rerun establishes repeatability under those inputs, not business validity or causal impact. Retain a named maintenance owner, review changes and block release when source identity or reconciliation fails. IS-09 addresses information freshness; this case asks how a particular number was produced.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional Hong Kong distributor. No personal or live data. All figures, quotes, plans and screen fictional. Both plans controlled/affordable; existing dashboard separately reviewed before decision. 34000-7000=27000 below the greater-than-30000 screen. M12x1000=12000;R6000+12x400=10800;difference1200;break-even10 releases. No actual error rates, certainty, source correctness or causal campaign effect inferred. ONS milestone dated15April2026 is UK context, not fictional business. ONS prioritisation/AF/GOV guidance same UK government family; W3C conceptual independent source. Not mandatory software stack.

- [ONS: April 2026 improvement progress update, released 15 April 2026](https://www.ons.gov.uk/aboutus/ourstrategyandplans/onsimprovementplans/onseconomicstatisticsandsurveysimprovementplan/onseconomicstatisticsandsurveysimprovementplanquarterlyprogressupdateapril2026). Actual body reports Living Costs and Food Survey processing transition. Milestone, not universal error elimination.
- [ONS: Prioritising RAP transformation projects, 6 August 2024](https://www.ons.gov.uk/aboutus/whatwedo/programmesandprojects/prioritisingreproducibleanalyticalpipelinesraptransformationprojects). Actual criteria discuss workflow risk, resources and ongoing maintenance. No fictional project cost or duration inferred.
- [W3C: PROV-Overview, 30 April 2013](https://www.w3.org/TR/prov-overview/). Non-normative overview describes objects, processing, responsibility, versioning and derivation. Conceptual support, not a certification.
- [Government Analysis Function: Why take a more sophisticated approach to building your pipeline](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/why-take-a-more-sophisticated-approach-to-building-your-pipeline/). Actual guidance discusses recorded code versions and protected source data. No single tool is imposed on the case.
- [GOV.UK: Choose tools and infrastructure to make better use of your data](https://www.gov.uk/guidance/choose-tools-and-infrastructure-to-make-better-use-of-your-data). Actual reproducibility section covers independent reruns, dependencies and automated testing. Government cloud guidance is not imported as a requirement.
