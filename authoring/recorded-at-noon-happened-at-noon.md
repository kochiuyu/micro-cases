# Recorded at noon. Happened at noon?

<!-- legacy-case-id: 296 -->

IS-25 · Hong Kong · 15–20 minutes · Event time · Delayed records · Reporting cutoffs

![A fictional service-centre analyst and branch colleague compare blank ticket slips and a laptop beside a plain clock, with waiting chairs in the background.](../recorded-at-noon-happened-at-noon-scene.jpg)

## A timestamp answers a particular question

Official stream-processing documentation distinguishes when an event occurs from when a system receives or processes its record. Network delays can separate those moments. An hourly count is therefore meaningful only when its time basis is clear.

The following service-centre records are invented. No software platform, outage or customer behaviour is being reported as a real event. The exercise needs no programming: identify the business event, choose the matching clock and decide how later records should change a report.

## Opening decision

You are an analyst for two fictional Hong Kong service centres. At 13:05, the operations manager asks which hour from 10:00 to 13:00 had the most customer arrivals. A report for a staffing discussion is due at 14:00; there is no emergency staffing change to make now. A customer receives one queue ticket when joining. The requested measure is tickets issued, not completed services, minutes of work or people still waiting.

Every record has two fields: ticket-issued time supplied by the branch kiosk, and receipt time assigned when the reporting system receives the record. The kiosk field is intended to mark the customer’s arrival, but its clock and capture rule have not yet been checked. Receipt times are reliable for system receipt. The existing dashboard groups by receipt time. The three rows cover the fictional operating day 12 November 2026 in Hong Kong time, using intervals that include the start and exclude the end: 10:00–11:00, for example, excludes exactly 11:00.

The current extract contains 200 distinct ticket records. Within the supplied population, each ticket represents one arrival, with no reissues or duplicates. The analyst can validate the kiosk timestamps and reconcile branch records by 13:30 using funded staff time. The displayed receipt counts are available immediately. Completeness for the customer-arrival period is not yet established; a quiet transmission period is not proof that nobody joined the queue.

## Evidence

| Reporting-system receipt interval | Records received |
|---|---:|
| 10:00–11:00 | 20 |
| 11:00–12:00 | 20 |
| 12:00–13:00 | 160 |

Total in the 13:05 extract: 200 distinct records. Grouped by receipt time, not yet checked against ticket-issued time. All quantities are fictional.

**Student question:** Would you use the receipt-time table to identify the customer-arrival peak, or validate and regroup by ticket-issued time? Say what you can honestly report at 13:05 and what still needs checking.

## Round two

By 13:30, the analyst verifies that both kiosks timestamp each ticket when the customer joins the queue, their clocks are synchronised and the date and time zone are correct. Centre A transmitted promptly: its original records contain 20 tickets in each event hour. Centre B had a connection delay and transmitted 140 stored records during 12:00–13:00. Those records comprise 80 tickets issued during 10:00–11:00, 40 during 11:00–12:00 and 20 during 12:00–13:00.

At 13:15, another 20 distinct Centre B records arrive. Their checked ticket-issued times fall in 11:00–12:00. They are additional tickets, not retransmissions or duplicates. By 13:30, reconciliation against both centres’ source issue logs confirms that all 220 tickets issued from 10:00 to 13:00 are included exactly once. This establishes completeness for this bounded period, not for future tickets or all future corrections. Keep the original 13:05 snapshot as a version rather than silently replacing its meaning.

**Student question:** What are the revised customer-arrival counts for the three hours, and which hour is highest? Specify the event period, receipt cutoff and revision label for the 14:00 report; explain what the noon receipt spike still tells you.

## Answer the question that the field can support

At 13:05, the analyst can state that 160 records were received between 12:00 and 13:00, the largest receipt count in the extract. That is not yet evidence that the most customers joined then. A sensible recommendation is to validate ticket-issued time and regroup before the 14:00 report. Receipt time remains useful for transmission monitoring. Its reliability does not make it the appropriate clock for every business question.

## Regroup the original 200 records

For event time, Centre A contributes 20 in each hour and Centre B contributes 80, 40 and 20. The original 200 therefore regroup to 100, 60 and 40. Their sum remains 200; regrouping changes the time allocation, not the population. The noon receipt count of 160 consists of A’s 20 timely records plus B’s batch of 140. Of B’s batch, 120 tickets were issued before noon and 20 during the noon hour.

## Add late records to their event window

The additional 20 records received at 13:15 belong to 11:00–12:00 because that is when their tickets were issued. The revised event counts are 100, 80 and 40, totalling 220. The highest customer-arrival hour is 10:00–11:00. Do not add the 20 to the noon event window or discard them merely because they arrived after the event period ended. Unique tickets and reconciliation prevent double-counting.

## Make the report’s boundaries visible

For the 14:00 report, label the measure as tickets issued, the event period as 10:00–13:00 on 12 November 2026 in Hong Kong time, and the receipt cutoff as 13:30 on that date. Label it revised and reconciled against source issue logs. The three windows include their starts and exclude their ends. Preserve the earlier extract and its receipt-time basis so another analyst can reproduce the change. A later correction should receive a new version label and explanation.

## Completeness comes from evidence

The case’s completeness claim comes from matching the bounded ticket population to the source logs, not simply waiting until 13:30. If reconciliation failed, report the counts as provisional, identify the unresolved gap and provide an update plan. Streaming systems can use watermarks and triggers to manage expected progress and revisions, but those mechanisms are not universal proof that all records exist. No particular software setting is prescribed here.

## What the corrected peak does not establish

The receipt spike still describes a burst of incoming data and can help investigate transmission delays. The corrected ticket profile describes one day’s arrivals; it does not measure service duration, queue length, staffing need or the cause of demand. A staffing decision would also need representative days, service times and capacity. Receipt time is not assumed to equal every later processing timestamp.

## Instructor note

Use about 3 minutes for the initial choice, 6 for regrouping and late-record arithmetic, and 6 for reporting and limits. Ask for two tables: original receipts 20/20/160 and revised events 100/80/40. Students should explain why their totals differ: 20 extra records arrived, not because a grouping operation created customers.

Common mistakes are treating a field named time as self-explanatory, equating trustworthy receipt timestamps with event validity, moving late tickets into the receipt hour, or declaring completeness because the system became quiet. Optional extension: discuss a watermark as a system estimate of event-time progress, with late-data handling, rather than a magic finality certificate. Distinguish this exercise from forecasts with information cutoffs and from merely refreshing a dashboard: its core is choosing the correct event clock and retaining revisions.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All centres, people, clocks, records, counts, network delays and report deadlines are original fiction. Ticket-issued time means joining the queue, not service completion. One distinct ticket corresponds to one arrival in this bounded exercise; unique identifiers prevent recounting on retransmission. No personal identifiers appear. All times use 12 November 2026 and Hong Kong local time, with start-inclusive/end-exclusive windows. Kiosk clocks and capture rules are validated only in the reveal. Receipt time is not asserted to equal every downstream processing time. Source reconciliation establishes completeness for 10:00–13:00 by 13:30, not an unbounded stream.

- [Apache Beam · Basics of the Beam model · accessed 16 November 2026](https://beam.apache.org/documentation/basics/). Windowing, watermark and trigger sections distinguish event and processing time, uncertain arrival order and early or revised results. Conceptual reference; no specific default configuration imposed on the case.
- [Apache Flink · Timely Stream Processing · stable documentation accessed 16 November 2026](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/). Explains event versus processing time and that delayed elements may arrive after a watermark. The retrieved stable page identified version 2.3.0; the moving link can later change.
- [Google Cloud Dataflow · Streaming pipelines · accessed 16 November 2026](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines). Documents windows, watermarks and triggers. Expectations about completeness are distinct from the case’s explicit source reconciliation. No Dataflow service was used.
- [Microsoft Learn · Understand time handling in Azure Stream Analytics · accessed 16 November 2026](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-time-handling). Defines arrival time and application time and explains why source or network delays matter. Substantive public text was read; no account login or configuration was performed.
- [Graham Klyne and Chris Newman · RFC 3339: Date and Time on the Internet: Timestamps · July 2002](https://www.rfc-editor.org/rfc/rfc3339). Sections 4.1–4.4 explain UTC, numeric offsets and problems with unqualified local time. Timestamp format alone does not validate a clock or event meaning. RFC 3339 has later updates including RFC 9557; no software implementation or compliance claim is made.
