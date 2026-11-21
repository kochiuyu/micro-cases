# One parcel. How many fees?

<!-- legacy-case-id: 503 -->

IS-41 · Hong Kong · 15 minutes · Data integration · Join fanout · Data grain · Reconciliation

![A depot analyst compares a short parcel charge ledger with a series of scanner events from the sorting area.](../one-parcel-how-many-fees-scene.jpg)

## One parcel can leave many digital traces

The GS1 EPCIS implementation guide describes how one shipment can generate separate records for steps such as packing, dispatch and receipt. An event records a step, not another shipment. The Hong Kong courier and data below are fictional and do not implement the GS1 standard.

## Opening decision

At a fictional Kowloon courier depot, analyst Jo combines a parcel charge ledger with scanner events for a 6 p.m. review. The ledger has exactly one row per parcel and shows a proposed fee. It is not yet an invoice. The scan feed has one row per event, which can legitimately repeat a parcel ID.

Jo must report the total proposed fees for all ledger parcels and the part cleared for billing. The fictional contract allows one fee per parcel, and only when there is at least one valid delivery event by the review cutoff. Missing, inconclusive or voided delivery evidence leaves the fee pending review, not cancelled.

The current dashboard pairs ledger rows with every scan row having the same parcel ID. It drops parcels without a match and adds the fee on each resulting row. All recorded keys below are correct; no name matching or uncertainty about identity is involved.

## Evidence

| Parcel ID | Ledger fee (HK$) | Events in initial snapshot |
| --- | --- | --- |
| P17 | 100 | Accepted, sorted, delivered E31 |
| P18 | 100 | Accepted, delivered E40 |
| P19 | 80 | No scan rows |

**Student question:** Would you release the dashboard as shown? Calculate its fee total, then rebuild the proposed, cleared and pending totals without dropping any parcel.

## Round two

Before the same 6 p.m. cutoff, a second valid delivery scan E42 arrives for P17. A supervisor’s authorised correction also arrives: E43 voids P18’s delivery event E40. P18 has no other delivery event. Keep the original rows and log the void against E40. The charge ledger has not changed.

A colleague suggests taking just the latest row per parcel. Another suggests adding each distinct fee amount only once. Neither proposal changes the underlying billing rule.

**Student question:** After the new records, what would you clear and hold? What parcel-level checks would let you approve the result, and why is neither shortcut a general solution?

## Debrief · Count parcels, not scans

Do not release the draft. It has three rows for P17 and two for P18. P19 disappears. Its sum is 3 × HK$100 + 2 × HK$100 = HK$500. The correct proposed total is HK$100 + HK$100 + HK$80 = HK$280. Even a join that keeps unmatched parcels but still sums every row would show HK$580.

## Debrief · Decide at the parcel level

Start from the charge ledger. Remove voided deliveries from consideration using the event they reference, without deleting records. For each parcel, determine whether any valid delivery remains by the cutoff; then carry one fee and one status for each ledger parcel. Initially clear HK$200 for P17 and P18. Hold HK$80 for P19.

## Debrief · Apply the correction before clearing

E42 adds evidence for P17, not a second HK$100 fee. E43 invalidates E40 and leaves P18 without a qualifying delivery. P19 still has no scan. Clear HK$100 and hold HK$180. The unchanged proposed total is HK$280, and HK$100 + HK$180 reconciles to it.

## Debrief · Test the rules, not just the total

A latest-row shortcut cannot generally determine eligibility: a later sort scan need not cancel a valid delivery, and a correction targets one event, not necessarily every delivery for that parcel. Counting each distinct fee amount once would merge P17 and P18’s equal charges. Group by parcel ID, never by fee amount.

Before release, test that the ledger IDs are non-empty and unique, that scan and correction IDs link to the intended parcel and event, and that no exceptions are silently lost. Require every ledger parcel exactly once in the output, with one status. Check each amount against its source and confirm cleared plus pending equals proposed, both by parcel and in total.

## Instructor note

Allow 15 minutes: 4 to model the join on paper, 4 to reconcile the initial totals, 4 for the updated status and 3 to design the release check. Ask which table has one row per parcel before asking what the joining key is.

Numbers and event codes are invented. Treat no scan as missing delivery evidence, not proof the shipment failed. This exercise makes no actual billing change and assumes the labelled correction is authoritative.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All parcels, staff, amounts, fee conditions, events and cutoffs are fictional. The cited sources describe event and data-model practices, not a particular company’s delivery or billing rules.

- [GS1, EPCIS and CBV Implementation Guideline, release 2.0](https://ref.gs1.org/guidelines/epcis-cbv/2.0.0/). Explains how the steps in one shipment create multiple visibility events and why the event has a different meaning from the shipment.
- [PostgreSQL, Table Expressions, §7.2.1.1](https://www.postgresql.org/docs/18/queries-table-expressions.html). Explains matched row pairs and how a left outer join adds an unmatched left-side row without collapsing existing matches.
- [Ralph Kimball, Declaring the Grain](https://www.kimballgroup.com/2003/03/declaring-the-grain/). Distinguishes what a row measures from the identifier used to join tables and recommends a clear statement of row meaning.
- [pandas, Merging and key uniqueness](https://pandas.pydata.org/docs/user_guide/merging.html). Documents validation of one-to-one and one-to-many assumptions with example failures for duplicate keys.
- [SQLite, Built-in Aggregate Functions](https://www.sqlite.org/lang_aggfunc.html). Explains why adding distinct fee values counts equal amounts only once, even when they belong to separate parcels.
