# The old screen returns. What has not rolled back?

<!-- legacy-case-id: 476 -->

IS-40 · Singapore · 15–20 minutes · Release reversibility · Coupled workflows · Business rollback

![Two adult wholesale-office colleagues compare plain order and invoice folders beside a monitor displaying abstract interface blocks in a Singapore office.](../old-screen-new-invoices-scene.jpg)

## Reversing software is not erasing events

Deployment guidance distinguishes a working new version from a safe transition between versions. A business process may already have sent a document or changed another system before its screen is reversed. The fictional rehearsal below examines that boundary, not the quality of a particular software vendor.

## Opening decision

Fictional classroom situation. Meridian Paper, a Singapore stationery wholesaler, plans to replace its order-entry screen and invoicing service. Opening records reconcile, staff training is complete and ordinary access, security and customer-service safeguards remain funded. All choices require an isolated end-to-end recovery rehearsal before anyone authorises a live release.

A stages functions: introduce the new order-entry screen first and transfer invoice responsibility later. Its complete planned transition costs S$6,000, including temporary integration and two change windows. B transfers order entry and invoicing together in one window for S$4,000. Both fit the S$8,000 budget and existing customer commitments.

A seeks a smaller initial functional change but must manage interfaces between versions. B avoids that temporary split but changes more of the business process at once. Both can be deferred. No probabilities of failure or future savings are supplied; lower cost alone does not establish safer recovery.

The team proposes a quick recovery action: switch back to the old order-entry screen. Both screens can read the durable shared order log. However, invoice generation runs in a separate background worker, and issued documents are copied to an external receiver. Switching the screen does not automatically control either dependency.

## Evidence

| Function | Screen switch reverses it? |
|---|---|
| Order-entry interface |Yes|
| Background invoicing |Not established|
| Already delivered documents |No|

**Student question:** Would you favour A or B provisionally? What must the recovery rehearsal demonstrate about accepted orders, invoicing authority and delivered documents before a screen switch counts as a safe business recovery?

## Round two

In an isolated rehearsal of A, thirty synthetic orders enter the durable shared log once each. A configuration dependency also starts the new invoicing worker, although the plan said invoicing would transfer later. It queues all thirty orders and issues one correct test invoice for each of eighteen. Twelve remain queued without invoices.

The eighteen documents reach an isolated test receiver, never customers. No payments, dispatches or real financial records exist. The old screen is then restored successfully, but the new worker and its queue are unaffected. The old billing register still marks all thirty orders unbilled because no invoice-status handoff was implemented.

The proposed recovery script would start the old biller and issue thirty more invoices. The rehearsal stops before that step. Assume that biller follows its stale register exactly. No order data are missing or duplicated; the defect is split invoicing authority and unreconciled side effects, not a failed initial data migration.

The release owner can hold deployment while engineers and finance design a controlled recovery. The extra work has not been priced or tested; it is not included automatically in A’s quoted S$6,000. B has not undergone its full recovery rehearsal either, so the observed defect does not certify B as safe.

**Student question:** If the unsafe old-biller step ran while the new worker produced nothing further, how many duplicate invoices and total documents would result? Explain the safe next steps for the eighteen issued and twelve pending orders. Would you release either plan now, and how could a genuinely reversible phase be designed?

## Track the business state

Thirty accepted orders remain valid in the shared log. Eighteen already have one correct test invoice each; twelve have none. An old screen that displays every order correctly has not reconciled invoice ownership or recalled the eighteen external documents.

The hypothetical old-biller run adds thirty documents to eighteen already issued: 48 total. Eighteen orders would receive a duplicate invoice; twelve would receive their first. That calculation assumes the new worker produces nothing further. Leaving its twelve queued jobs active creates another uncontrolled route and must not be ignored.

## Stop competing actors before recovery

Hold live release. In the rehearsal, stop new invoicing and prevent queued jobs from firing; establish and verify a settled worker state before moving authority. Preserve the accepted-order log, invoice identifiers, delivery evidence and queue state. Do not delete history or replay every order simply because the old register says unbilled.

Reconcile each order across the log, invoice register and receiver. Assign exactly one authorised invoicing owner for each pending order. Mark the eighteen issued orders so neither system invoices them again, and transfer or complete the twelve pending jobs once through the chosen controlled route. Test delayed messages and repeated recovery attempts.

## Compensation is not time travel

The eighteen invoices are stipulated correct, so reverting the interface does not by itself require cancelling them. If a real business needed corrections, finance would use an authorised, legally appropriate correction and communication process linked to the original record. A database restore cannot make a document disappear from its recipient.

Correction can itself fail or be retried. Record its progress and verify the resulting business state rather than assuming an automatic inverse. This exercise authorises no real invoice, cancellation, credit note, refund or customer communication.

## Choose a boundary that actually contains the change

A revised functional phase could keep the old invoicing service as sole owner while the new screen writes compatible accepted orders, with the new worker positively disabled and tested. This is a proposed redesign, not an available proven feature or free fix. Price and rehearse it before approval.

Alternatively, test a combined transfer with explicit ownership of all in-flight work and a recovery route that preserves issued-document history. B saves S$2,000 on the original quotes, but its end-to-end recovery remains unproven. Neither “phased” nor “single cutover” is a safety certificate.

## Instructor note

An acceptable recommendation holds both plans until their business recovery gates pass, while stating a provisional design preference. IS-19 focuses on migration comparison and cutover reconciliation; IS-03 tests recovery after interruption. Here a planned functional boundary fails because a background process and external side effects continue after the interface reverses.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional Singapore stationery-wholesaler scenario, not a real deployment. Reconciled opening data, training and common safeguards are stipulated; neither release is authorised before a full business-recovery rehearsal. A phases order entry before invoicing; B combines their transfer. Complete planned transition quotes are S$6,000 and S$4,000 within an S$8,000 budget; later redesign is unpriced. Thirty synthetic orders enter a durable shared log. The new worker queues all thirty and issues eighteen correct invoices to an isolated test receiver, leaving twelve without invoices. Interface rollback affects neither the worker, issued-document history nor the old register's unbilled flags. The hypothetical old-biller run would add thirty documents: eighteen duplicates and 48 total, assuming the new worker produces nothing further. This replay is not actually run. No real invoices, payments, dispatches, customer contacts or financial records exist. Recovery must settle the worker and its pending queue, reconcile records and establish one authoritative billing owner per order. The eighteen correct invoices need not be cancelled; any necessary correction requires an authorised finance-led process preserving history and applicable law. No tax rule, credit note or payment action is prescribed. Vendor examples are not claimed implementations.

- [Sandeep Pokkunuri · AWS Builders’ Library: Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/). Original engineering account covers version compatibility and testing transitions, not merely final versions. No vendor implementation is assumed.
- [Microsoft Azure Architecture Center · Compensating Transaction pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction). Business-specific compensation may not restore the original state; progress, retries and human intervention require design. Not an accounting or tax rule.
- [Google SRE Workbook · Canarying Releases](https://sre.google/workbook/canarying-releases/). Original practitioner chapter discusses limited exposure, evaluation and release controls. A canary is not proof that external effects are reversible.
- [Danilo Sato · Parallel Change · 2014](https://martinfowler.com/bliki/ParallelChange.html). Author’s expand–migrate–contract explanation supports compatibility across phased interfaces. It does not validate a phase that leaves coupled business processes uncontrolled.
- [Stripe · Invoice status transitions and finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions). Vendor documentation illustrates distinct invoice states and restrictions after finalization. Meridian does not use a stipulated Stripe implementation, and Singapore invoice requirements are not inferred from this page.
