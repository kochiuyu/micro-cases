# A failed payment. A failed checkout?

<!-- legacy-case-id: 464 -->

IS-39 · Hong Kong · 15–20 minutes · Event semantics · Checkout-level measurement · Outcome reconciliation

![Two adult ticketing analysts compare unlettered event slips and a simple seat-plan mockup in a bright Hong Kong office, without readable percentages or customer payment details.](../payment-success-booking-success-scene.jpg)

## An event label needs a business definition

Payment approval, captured funds and a confirmed booking describe different events. Analytics must join the appropriate records before calling a checkout complete. Provider documentation explains payment states, while funnel tools require explicit counting units and step definitions. The following pre-release test uses invented records and no real payments or customers.

## Opening decision

Fictional Hong Kong ticket seller Seatline is evaluating a checkout redesign in a funded test environment. Each of one hundred synthetic checkout identifiers represents one intended seat purchase. Every checkout begins and submits payment. Each receives twenty-four hours of follow-up from its own start, with no missing or late-arriving records at the analysis cutoff.

The initial dashboard shows 120 payment attempts and ninety issuer approvals. It labels the resulting 75% “checkout success”. The analyst must choose a reporting definition before a release decision: attempt-level approval, completed paid bookings per checkout, or a funnel retaining both payment and reservation stages.

An approval reserves funds for possible capture; it is not itself captured payment. For this exercise, capture means one successfully completed charge. A completed paid booking requires that capture and a confirmed seat reservation linked to the same checkout by its follow-up deadline. A pending seat or an approval alone does not qualify.

The event log distinguishes checkout_started, payment_attempted, payment_approved, payment_captured and seat_confirmed. These are custom teaching labels, not provider API names. Each record has a timestamp, event identifier and checkout identifier; payment records also identify the attempt. Authoritative payment and reservation records can be reconciled without collecting names, card details or other personal data.

No actual customer is charged or assigned a seat. Payment execution is already verified to charge at most once per checkout; the question is how to measure outcomes, not how to implement duplicate-payment prevention. Release remains blocked until unresolved payment-and-reservation mismatches have a tested safe resolution. No existing customer protection or security check may be removed.

## Evidence

| Recorded events | Count |
| --- | --- |
| Checkout starts | 100 |
| Payment attempts | 120 |
| Issuer approvals | 90 |

**Student question:** Is ninety approvals divided by 120 attempts a valid checkout-success measure? Specify the counting unit and the linked records needed for completed paid bookings, while retaining a useful operational measure of payment attempts.

## Round two

The complete test ledger shows eighty checkouts approved on their first and only attempt. Twenty others receive a definitive decline, then each makes one new attempt for the same intended booking. Ten retries are approved; ten are declined again. Nobody retries after approval, and no checkout has more than one approval or capture.

Among the eighty first-attempt approvals, seventy have captured payments and sixty-five of those have confirmed seats. The ten approved retries all have captured payments and confirmed seats. The ten twice-declined checkouts have neither. Thus five captured payments still lack confirmed seats at the deadline; ten other approvals remain uncaptured.

Examples use synthetic keys. C001 has attempt C001-A1 approved, captured and linked to seat C001-S1. C071 has C071-A1 approved and captured but no confirmed seat. C081 has declined attempt C081-A1 followed by approved, captured C081-A2 and confirmed seat C081-S1. C091 has two declined attempts and no seat.

These examples belong to the supplied groups; do not add them again. All confirmed seats are linked to captured payments, and no other reservations, captures, cancellations or refunds occur within the test window. The mismatch is a reservation-outcome problem, not missing telemetry or a duplicate charge. These are constructed outcomes, not measured production failure rates.

**Student question:** Reconcile attempts, approvals, captured payments and completed paid bookings. Calculate attempt approval and checkout completion rates. Why can their equal headline percentages conceal different failures, and what should the release report show?

## Debrief · Count attempts without inventing customers

The eighty first attempts plus twenty pairs of attempts give 80 + 40 = 120 attempts. There are eighty initial approvals and ten retry approvals, so ninety in total. Thirty attempts decline: twenty initial declines plus ten repeat declines. Attempt approval is 90/120 = 75%, a valid attempt-level statistic.

At checkout level, ninety of one hundred eventually obtain an approval, so the approval rate is 90%. The thirty declined attempts do not represent thirty failed checkouts: ten checkouts decline twice, while ten recover on retry. Preserve the retry workload without inflating the number of intended bookings or declaring every decline a permanently lost sale.

## Debrief · Reconcile the promised outcome

Seventy first-attempt captures plus ten retry captures give eighty captured payments. Sixty-five first-attempt paid confirmations plus ten retry paid confirmations give seventy-five completed paid bookings. The end-to-end rate is therefore 75/100 = 75%. Payment capture alone would give 80%, not the completed-booking result.

The hundred checkouts partition into seventy-five completed paid bookings, five captured but unconfirmed, ten approved but uncaptured, and ten with no approval. These sum to one hundred. This outcome table makes the missing seat confirmations visible instead of treating a payment-system success as fulfilment of the seller’s promise.

## Debrief · Equal rates do not validate equal meanings

The two 75% figures use different denominators and numerators. One divides approvals by attempts; the other divides complete paid bookings by checkout starts. Their equality is deliberately constructed. Neither makes thirty declined attempts equal to twenty-five incomplete bookings, nor makes every approval a confirmed seat.

Report the checkout funnel as one hundred starts and submissions, ninety approved checkouts, eighty captured checkouts and seventy-five completed paid bookings. Alongside it, show 120 attempts and thirty declines for payment operations. Label the cohort, twenty-four-hour deadline and unit on each measure; do not mix event counts and checkout counts in one unlabeled percentage.

## Debrief · Make the join and timing explicit

Join approval and capture to their payment attempt, then to the checkout; join the authoritative seat confirmation to that same checkout. Count each qualifying checkout once. Do not join solely on timestamps or amount, or treat a browser’s success screen as proof that both backend outcomes exist. Retain original events and a reviewable reconciliation result.

Keep event-occurrence time distinct from collection time and document exactly when each event is emitted. A checkout with an unresolved state is not silently dropped from the denominator. Later resolution should be shown separately or under a clearly revised follow-up metric, not backdated into the original twenty-four-hour completion result.

## Debrief · Fix the mismatch before claiming improvement

Keep the release gate closed while the team tests safe handling of captured-but-unconfirmed cases and uncaptured approvals. Real remedies would follow the authorised customer-protection process; issuing a refund would not turn a missing booking into a completed booking. This exercise authorises no payment, refund, reservation or customer communication.

The test validates arithmetic and exposes outcome distinctions, not an improvement caused by the redesign. There is no prior-version comparison or randomised treatment here. A later evaluation must use consistent checkout definitions, complete follow-up and safeguards, while reporting payment and reservation exceptions alongside the headline outcome.

## Instructor note

IS-26 prevents repeated requests from executing the same intended transaction twice. Here execution has no duplicate charges, but analytics can still confuse attempts, approvals and completed outcomes. MKT-12 assumes checked instrumentation to diagnose a journey bottleneck; this case first establishes what the event-based success measure actually means.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All synthetic prerelease test data.100checkoutIDs eachoneintendedseat, allstartandsubmit,24hfollowup each,120attempts.80initialapproval;20firstdecline retry once:10approval10decline.90approvals/120=75%;90uniqueapproved/100=90%.80captured,75confirmedpaid=75%starts;fivecapturedunconfirmed,tenapproveduncaptured,tendeclined. Everycaptureonce,completeauthoritativeevents,no duplicatecharges; repeatedattempts afterdefinitivedecline not replayduplicates. C001successful,C071capturednotconfirmed,C081declineapprovedcomplete,C091twodeclines examples. Latercustomerremedy notretroactivecompletion. No actualpayment/refund/booking orcausalupliftclaim.

- [Stripe · Payment status updates](https://docs.stripe.com/payments/payment-intents/verifying-status). Official documentation distinguishes incomplete, pending, uncaptured and succeeded states, and identifies authoritative status. Its payment success is not proof of Seatline’s separately confirmed seat.
- [Adyen · Payments lifecycle](https://docs.adyen.com/account/payments-lifecycle/). Official payment-state definitions distinguish authorisation and capture. Provider timing and status contracts are not copied into the fictional twenty-four-hour analysis window.
- [Google Analytics · Funnel exploration](https://support.google.com/analytics/answer/9327974?hl=en). Official guidance explains ordered conditions, open and closed entry, and step time limits. This case uses custom checkout-level reconciliation rather than claiming a default user funnel supplies the answer.
- [Amplitude · Hold properties constant in a Funnel Analysis chart](https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-hold-properties-constant). Official examples explain how holding an identifier constant changes the counting unit and prevents mixing steps from different journeys. No live analytics configuration is requested.
- [OpenTelemetry · Semantic conventions for events · development-status guidance](https://opentelemetry.io/docs/specs/semconv/general/events/). Primary technical specification describes named occurrences, event definitions, timestamps and correlation attributes. It is marked Development; the case’s teaching labels are not asserted to be standard payment event names.
