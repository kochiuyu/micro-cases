# Two dashboards. How many independent routes?

<!-- legacy-case-id: 576 -->

IS-48 · Hong Kong · 15 minutes · Dependency mapping · Availability · Common-cause failure

![Two staff compare separate scheduling screens and a sketch at a sports facility desk.](../two-dashboards-one-upstream-scene.jpg)

## Follow the route, not the number of screens

Microsoft’s reliability guidance advises mapping system dependencies against user flows when analyzing failures. Google’s SRE availability appendix distinguishes the fraction of successful operations from outage duration. A fictional sports hall measures delivery of a usable court schedule, not whether the monitor lights up.

## Opening decision

In an isolated synthetic rehearsal, a request succeeds if any available display shows a current schedule. The hall’s target is at least 98.5% of 10,000 equally counted schedule requests, not guaranteed time uptime. Failure rows are mutually exclusive. A surviving branch shows correct data unless the scenario explicitly says otherwise.

A (HK$100/week) adds a standby display route alongside primary P, but both need original scheduling feed F and the same delivery gateway G. B (HK$160) adds an independent schedule feed H available to either display; initially it can rescue 260 of the F-only failures. C (HK$230) also gives the alternate supply path an independent delivery route and rescues all G-only failures in the replay. These are fictional demonstrations, not instructions to test a live system.

## Evidence

| Exclusive replay condition | Requests |
| --- | --- |
| None of the tested failures | 9,400 |
| Only primary display fails | 120 |
| Only standby display fails | 80 |
| Only original scheduling feed F fails | 300 |
| Only shared delivery gateway G fails | 100 |

**Student question:** What fraction succeeds under A, B and C? Which is the cheapest build that meets the replay target? Name the dependencies A leaves shared.

## Round two

The buyer tightens the freshness requirement. Under that definition the alternate feed H can rescue just 230 of the 300 F-only requests, under B and C alike. All other outcomes stay the same, including C’s 100 rescues during gateway-only failures. No double-counting across rows.

**Student question:** Recalculate B and C, choose again, and find the minimum number of F-only rescues B would need to pass.

## Replicas are not independent routes

Under A, each display covers a failure of the other: 9,400 + 120 + 80 = 9,600 or 96.0%. Neither helps if F or G fails: both sit on every path. B’s alternative feed lifts success to 9,860 or 98.6%; C also rescues the 100 G-only cases for 9,960 or 99.6%. B is cheaper than C and passes.

## Change what counts as success

Under the tightened definition, B reaches 9,830 or 98.3%; C reaches 9,930 or 99.3%. Only C passes. B needs 9,850 − 9,600 = 250 F-only rescues, 20 more than it now delivers. The result depends on the replay mix, not on treating branch failures as independent random events.

## Inspect the route end to end

Record what each path needs: a working display, a current data source and a usable delivery path. Ask the supplier for evidence that H does not depend on F and that C can still deliver without G. An alternate feed that cannot produce fresh schedules under the target conditions is not an effective backup.

## Instructor note

Have groups draw OR between the displays but AND between a live display, fresh feed and delivery gateway. Then have them move the shared nodes outside the OR. Discuss how a real pilot would estimate more representative failure mixes using only authorized, isolated drills.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Entire replay fictional; failure labels and rates represent no live system, vendor promise or security test.

- [Microsoft Azure, failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis). Describes tracing user flows through components to find dependency and failure points.
- [Google SRE, availability table appendix](https://sre.google/sre-book/availability-table/). Explains request failure counts as useful for partially available or unevenly loaded services.
- [AWS, Availability and Beyond](https://docs.aws.amazon.com/pdfs/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.pdf). Fault isolation and loose coupling discussion explains why shared dependencies may limit resilience.
- [AWS Builders’ Library, Static stability using Availability Zones](https://d1.awsstatic.com/builderslibrary/pdfs/static-stability-using-availability-zones.pdf). Engineering example distinguishes independence domains and the ability to keep operating in an impairment. Not evidence about the imaginary hall.
- [Microsoft Azure, reliability testing](https://learn.microsoft.com/en-us/azure/well-architected/reliability/reliability-test). Describes validating critical flows and acceptable graceful degradation in reliability tests.
