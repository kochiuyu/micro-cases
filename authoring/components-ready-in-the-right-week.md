# Enough components. Ready in the right week?

<!-- legacy-case-id: 244 -->

OPS-21 · Hong Kong · fictional workshop · 15–20 minutes · Material requirements planning · Bill of materials · Lead-time offsets

![Two workshop colleagues compare tabletop display bases and upright frames beside a tray of matching connectors and an open planner.](../components-ready-in-the-right-week-scene.jpg)

## A production order is more than a shopping list

A finished-product order creates demand for the parts inside it. Material requirements planning, or MRP, works through those relationships and schedules supply before each production stage needs it. Official manufacturing documentation separates quantities, existing supply and lead times; a grand total alone is not a release plan.

The workshop and all figures below are invented. No software purchase, real supplier order or claim about a named manufacturer is involved.

## Opening decision

**Fictional classroom situation.** At the start of week 1, a Hong Kong workshop must prepare **40 tabletop information displays for collection at the start of week 6**. The order is confirmed. Each display uses one base A and one upright frame B. Both subassemblies use the same connector C.

A colleague suggests waiting until final assembly approaches before ordering connectors. You must instead plan backwards from the collection date. Ten completed, inspected bases are already free for this job; there are no frames or finished displays in stock.

All dates mean the **start of the named week**. A one-week stage started in week 4 finishes and becomes usable in week 5. Inputs are required when a stage starts. Connector purchasing takes two weeks from release to inspected, usable receipt. Production and purchasing lead times include the required checks; they cannot be compressed.

Normal capacity is confirmed for the stated batches, including simultaneous base and frame work. All other materials, labour, funds and storage are available. There is no scrap, safety-stock requirement, minimum order quantity or quantity discount. No order has yet been released. For the first decision only, provisionally treat the scheduled 60-connector receipt as uncommitted; its reservation check follows before approval.

## Evidence

Bill of materials: inputs for one unit of each parent.

| Parent | Inputs per parent | Production lead time |
|---|---|---|
| Finished display | 1 base A + 1 frame B | 1 week |
| Base A | 2 connectors C | 1 week |
| Frame B | 3 connectors C | 2 weeks |

| Supply at start of week 1 | Quantity | Availability |
|---|---|---|
| Completed bases A | 10 | Usable and uncommitted now |
| Completed frames B | 0 | None |
| Connectors C on hand | 70 | Usable and uncommitted now |
| Scheduled connector receipt | 60 | Usable start of week 3; reservations not yet checked |

C is the same shared stock item in both assemblies. No other receipt or demand for free stock is modelled. Do not explode components again for ten bases already made. For the provisional first decision, assume all scheduled 60 are free; verify before releasing orders.

**Student question:** Using the provisional assumption that all 60 incoming connectors are free, would you order connectors now or in week 2? Give the quantity, needed week and start week of each assembly stage.

## Round two

**It is still the start of week 1, before any new order is released.** The reservation check shows that **40 of the scheduled 60 connectors are already allocated to another confirmed job at the start of week 3**. That commitment cannot be borrowed. Only 20 of the receipt are free for your displays. All 70 connectors currently on hand remain free. The other job’s capacity and materials are otherwise separately covered.

The supplier confirms that any new quantity up to 90 can be released now for usable receipt at the start of week 3. A second order released at the start of week 2 can arrive at the start of week 4. Each separate order costs HK$80 for administration and delivery, plus HK$10 per connector. Carrying extra connectors from week 3 to week 4 costs HK$0.50 per connector. Other holding costs are common to the alternatives and excluded.

Compare two ordinary-service plans: one consolidated order arriving in week 3, or two staged orders arriving in weeks 3 and 4. Use only what this job needs. Normal capacity, receipt dates and inspection success are fixed for this calculation; no expediting, substitutions or skipped checks are available. Neither plan adds a safety buffer.

**Student question:** With only 20 incoming connectors available to this job, what must be ordered this week? Recommend the consolidated or staged plan, showing quantities, dates and total relevant cost without using the other job’s stock.

## Debrief: work backwards through the product

Work backwards: final assembly starts in **week 5** to provide 40 displays in week 6. Frames take two weeks, so start **40 frames in week 3**. Bases take one week; use the ten already made and start **30 new bases in week 4**. Both batches become usable in week 5.

The frame batch requires 40 × 3 = **120 connectors in week 3**. The base batch requires 30 × 2 = **60 in week 4**. Total demand for this job is 180, not 200: the ten completed bases already contain their connectors.

Under the provisional first-round assumption, 70 on hand + 60 arriving in week 3 = 130. After the 120 for frames, ten remain. Order **50 in week 2 for week 4** to cover the base batch. Waiting until final assembly in week 5 would be too late for both upstream stages.

## Net the corrected supply by date

After the reservation check, free supply before new orders is only 70 + 20 = **90 connectors**. Frames need 120 in week 3, so at least **30 new connectors must arrive in week 3**. With a two-week purchasing lead time, release that requirement **now, in week 1**.

If you order just those 30 now, week-3 stock is 70 + 20 + 30 − 120 = zero. The 60 required for bases in week 4 must then be ordered in week 2. Total new purchases are **90**, but the time-phased shortages are **30 in week 3 and 60 in week 4**. Ordering all 90 in week 2 would get the total right and the first date wrong.

## Trace both feasible release plans

| Week-start event | Consolidated order | Staged orders |
| --- | --- | --- |
| Week 1: release purchase orders | Order 90 for week 3; stock remains 70 | Order 30 for week 3; stock remains 70 |
| Week 2: next release | No new release | Order 60 for week 4 |
| Week 3: receive free supply, use 120 | 70 + 20 + 90 − 120 = 60 | 70 + 20 + 30 − 120 = 0 |
| Week 4: use 60 | 60 − 60 = 0 | 0 + 60 − 60 = 0 |

A purchase release does not put material on the shelf. The scheduled 40 allocated to the other job never enter this free-stock trace. Across the entire connector pool, 70 on hand + 60 scheduled + 90 new = 220; your job uses 180 and the other job uses 40. Each connector is counted once.

## Choose a lot pattern, not just a total

Both plans buy 90 × HK$10 = **HK$900** of connectors. Consolidation adds one HK$80 order fee and holds 60 extra connectors for one week at HK$0.50 each: **HK$900 + HK$80 + HK$30 = HK$1,010**.

Staging adds two HK$80 fees and no extra week-3-to-week-4 stock: **HK$900 + HK$160 = HK$1,060**. The consolidated 90-unit order released now is **HK$50 cheaper** under the supplied dates and costs. Both plans are physically feasible; consolidation is not justified by pretending all 90 are needed in week 3.

The difference illustrates why net requirements and order quantities are not the same decision. A different order fee, holding cost, space constraint or verified supply risk could alter the preferred lot pattern. No probabilities are supplied for valuing uncertain disruptions here.

## A usable planning discipline

Use a simple sequence: begin with the finished-product schedule, subtract usable parent stock, calculate the remaining parent production, derive each child requirement, combine shared components by needed date, subtract free dated supply, then offset shortages by purchasing lead time.

A workable material plan still requires valid product specifications, trustworthy allocations, a feasible capacity plan and monitoring of receipt dates. Those conditions are explicitly supplied here rather than proven by the arithmetic. A later change should trigger replanning, not an invented receipt or a silent transfer of another customer’s allocation.

## Instructor note

Allow 15–20 minutes: three for the product structure and week convention, four for the provisional release decision, five for the reservation reveal and stock trace, and three to eight for cost comparison and debrief. Keep the reservation reveal and answers closed until the first decision. Show the two small opening tables separately in presentation mode.

Ask students to draw three lines: frames from week 3 to 5, bases from week 4 to 5, and final assembly from week 5 to 6. Then place connector requirements at the starts of the first two lines. Check that students subtract completed bases before calculating their connector demand, aggregate the shared item, and distinguish a release from a receipt.

The first answer is explicitly provisional: the 60-unit receipt was not verified as free. No new purchase was placed before the check, so correcting the plan in week 1 is possible. The shared connector is disclosed from the beginning; the case does not use a hidden design change to manufacture a shortage.

OPS-11 concerns a reorder trigger for independent repeat demand. OPS-13 concerns promising a delivery from dated kit availability. This case explodes a multilevel bill of materials and offsets dependent component demand. It is not a critical-path capacity optimisation or an instruction to override reservations. Source documentation explains mechanisms, not a claim that any vendor system implements this exact toy model.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional display workshop and all quantities, dates, commitments, lead times and costs. Collection at startweek6; final assembly1week starts5. Need40 bases less10 already made =30 new bases, start4;40 frames take2weeks, start3. Shared connectors:30×2=60 due4 plus40×3=120 due3, total180. First-round provisional free supply70+60=130 implies net50 due4, release2. Reservation check before any release leaves only20 of scheduled60 free;40 remain protected for another job. Revised free supply90 implies shortages30 due3/release1 and60 due4/release2. Consolidated90 release1/receipt3 leaves60 after frame use, then0 after base use. Staged30+60 leaves0 after each use. Both purchase900; consolidation fee80 plus holding30 totals1010; staging fees160 totals1060; consolidation cheaper50. All dates are week starts; receipts clear required checks before same-start production. Capacity is funded and sufficient; no scrap, minimum lot, discounts, safety stock, substituted inputs or expediting. Six substantive authoritative documentation pages used; an additional Oracle planning-process page was read. SAP Help procedure page returned no readable body and was excluded. These are vendor explanations, not six independent empirical studies. No source figures, quotations or artwork reproduced.

- [Oracle · Overview of Material Requirements Planning](https://docs.oracle.com/cd/A60725_05/html/comnls/us/mrp/mrpover.htm). Gross-to-net inputs, dated planned replenishment and the need to check capacity separately. Historical product documentation, not a capacity guarantee.
- [Oracle · Time-Phasing Requirements](https://docs.oracle.com/cd/A60725_05/html/comnls/us/mrp/timphreq.htm). Lead-time offsets and component demand tied to operation/order starts. The case uses explicitly defined week-start buckets rather than every vendor setting.
- [SAP Learning · Applying Lead-Time Scheduling to Update a Material](https://learning.sap.com/courses/exploring-basic-data-for-manufacturing-and-product-management-in-sap-s-4hana/applying-lead-time-scheduling-to-update-a-material). Bill-of-material explosion, planned orders and production versus purchased-item lead times. No SAP deployment or automated result is claimed.
- [Oracle · Lead Times Usage in Manufacturing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/faumf/lead-times-usage-in-manufacturing.html). Processing, pre-processing and post-processing time, including the distinction between receipt and usable availability. All toy-case checks are already included in stated leads.
- [Microsoft Learn · Bills of materials and formulas](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom). Parent-component structures, multilevel BOMs and approved product definitions. No product-specific automatic reservation rules are imported.
- [Microsoft Learn · Production planning](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/production-planning). Netting across BOM levels and propagation of lower-level material delay. The case stipulates current data and normal capacity rather than reproducing complete planning software.
