# One switch-over. Two records to reconcile?

<!-- legacy-case-id: 224 -->

IS-19 · Hong Kong · 10–15 minutes · System migration · Cutover controls · Parallel reconciliation

![Two rehearsal-studio colleagues discuss a booking-system change beside a laptop and plain folder.](../one-switch-two-records-scene.jpg)

## A booking transition needs public arrangements

On 2 November 2023, Hong Kong’s LCSD published transitional booking arrangements ahead of the announced SmartPLAY launch on 9 November, including arrangements during service suspension. This illustrates the need to manage service continuity, not evidence about our software methods. The studio, costs and tests below are fictional.

## Opening decision

A fictional Hong Kong rehearsal-room studio is replacing its booking application. Functional, security, accessibility and test-data migration checks have passed. The same booking rules, fees and customer rights apply. Existing reservations, amendments and cancellations must remain intact. A specialist has tested backups and recovery, including reconciliation of transactions accepted after switching; simply restoring an old backup is not an acceptable rollback.

Plan A transfers booking authority this Sunday after final validation. Plan B runs the old system for another five working days while authorised staff reproduce each booking change in a restricted new-system comparison copy. The old system alone confirms availability and sends customer messages during comparison; the copy cannot take independent bookings or send confirmations. After checking differences, B transfers authority next Sunday. Both retain protected records and the tested recovery plan.

Both complete plans fit a HK$15,000 transition budget. Existing staff duties and service are covered by separately funded capacity, with no unpaid overtime. Customers can be notified of either Sunday maintenance period; neither date breaches promises. The studio can defer if release checks fail. The decision is whether five more days of real-workflow comparison are worth their effort, not whether to permit uncontrolled duplicate booking systems.

## Evidence

| Plan | Timing | Booking authority |
|---|---|---|
| A: single cutover | This Sunday after validation | Old until approved transfer, then new |
| B: parallel comparison | Five working days, then next Sunday | Old during comparison; copy cannot confirm |

**Student question:** Would you choose the planned single cutover or five days of parallel comparison before cutover? Explain the additional assurance you expect and who is allowed to confirm bookings during the transition.

## Round two

An isolated rehearsal of Plan B measures three staff minutes per booking change, including duplicate entry and reconciliation. The staffing plan uses 200 changes per day for five working days; treat that volume and average time as planning assumptions, not a guarantee. Four deliberately seeded discrepancies were detected and corrected in the rehearsal. They are not an estimate of live defect frequency or proof that every possible error will be found.

The specialist confirms that both plans still need a 90-minute final transaction freeze for the last sync and consistency checks. An agreed two-hour Sunday maintenance window is available under either plan. During the freeze, neither application confirms new bookings or applies changes. A tested, access-controlled request log preserves time order and acknowledges receipt without promising availability; staff process it once against the authoritative system after reopening. Existing sessions continue and emergency contact remains available.

At HK$240 per staff-hour, the additional parallel comparison is budgeted at HK$12,000. The common final transfer and support cost HK$3,000, making A HK$3,000 and B HK$15,000. No costs are committed. Both require zero unresolved reservation mismatches, an authorised go/no-go owner and completion within the approved window. Otherwise, use the rehearsed recovery route without losing accepted changes. More comparison adds evidence, not certainty.

**Student question:** Given the rehearsal workload and freeze requirement, which plan would you fund? Calculate the parallel checking effort, then specify the release and recovery conditions that protect every accepted booking.

## Count the work, not just the systems

200 changes × 3 minutes × 5 days = 3,000 minutes, or 50 staff-hours. At HK$240 per hour, comparison costs HK$12,000; adding the common HK$3,000 gives B HK$15,000. A avoids that extra checking, not the validation and recovery safeguards. Actual volumes or times could change the workload.

## Parallel operation still needs a final boundary

The restricted copy lets the team compare outcomes while the old system remains authoritative. It is not a second independent booking desk. The 90-minute freeze prevents either system from accepting changes during the final reconciliation. A queued request is acknowledged, not confirmed, and must be processed once after reopening.

## Choose evidence with clear exit conditions

A is defensible if the existing test evidence and protected cutover satisfy the business owners. B is defensible if further observation of real workflow warrants 50 hours and HK$12,000. Neither option permits unresolved mismatches or an overrun beyond the approved window. After new transactions have been accepted, recovery must preserve and reconcile them; switching a screen back or restoring an old backup alone could lose bookings.

## Instructor note

IS-03 tests recovery after interruption; IS-07 chooses a cohort for a display-only rollout. This case transfers live transaction authority between systems. The seeded discrepancies are a test design, not observed customer harm or a failure-rate sample. Both plans are deliberately safe and affordable. Students should explain the value of additional evidence rather than label parallel operation automatically safer or cheaper. No real system changes are requested.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All studio details, tests, prices and timings are original fiction. Parallel copy cannot independently accept bookings or send messages; one authoritative record throughout. Existing rights, sessions, access controls and customer commitments preserved. Both plans have tested recovery including post-cut over accepted transactions, not stale backup restoration. Comparison 200 changes/day ×3 minutes ×5 days=3000 minutes=50 hours; 50×240=12000; common 3000 gives A 3000 B 15000. Four seeded discrepancies are not estimated real error frequency. 90-minute freeze fits approved 120-minute window; no bookings confirmed during freeze; requests logged in order and processed once. Both plans defer/recover if zero-unresolved-mismatch gate or window fails. Two AWS references share one guidance family.

- [LCSD: Transitional booking arrangements, 2 November 2023](https://www.info.gov.hk/gia/general/202311/02/P2023110200221p.htm). Actual announcement states transitional dates and service arrangements. No inference about backend architecture or migration success.
- [AWS: Cutover stage](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html). Actual guidance covers source-write freeze, backup, final sync, validation and data-aware rollback. Technical context, not a prescribed implementation for the fictional studio.
- [AWS: Pre-cutover stage](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/pre-cutover-stage.html). Actual guidance calls for rehearsed plans, contingencies and ownership. Related to the previous AWS source, not an independent experiment.
- [US Federal Student Aid: Data Migration Roadmap Guidance, version 3.2, 2019](https://studentaid.gov/sites/default/files/fsawg/static/gw/docs/ciolibrary/Data_Migration_Roadmap_Guidance.pdf). Actual sections describe planned duration, validation and exit criteria for parallel operation. US institutional guidance; no retention rule or mandatory parallel duration imported.
- [Microsoft: Plan an n-tier workload migration](https://learn.microsoft.com/en-us/azure/migration/migrate-n-tier-from-on-premises-1-plan). Actual cutover-control table distinguishes write authority and recovery after the first target-system write. Vendor-specific guidance illustrates why traffic reversal alone is not data rollback.
