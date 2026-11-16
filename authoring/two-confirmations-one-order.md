# Two confirmations. One order?

<!-- legacy-case-id: 308 -->

IS-26 · Hong Kong · 15–20 minutes · Idempotency · Transaction identity · Uncertain responses

![A workshop customer checks a phone while a coordinator examines two blank reservation slips.](../two-confirmations-one-order-scene.jpg)

## A reply can disappear after the work succeeds

Public API documentation describes retry controls for situations where a caller receives no usable response. The important distinction is between repeating one intended operation and initiating another. The following booking situation is fictional, not a report of a provider incident.

## Opening decision

A fictional Hong Kong craft-workshop organiser is reviewing its booking tool before release. Each order reserves one transferable seat. A customer may legitimately book another seat for a friend using the same account, workshop and contact details. Capacity is ample for the examples below. The tool takes no payment; a confirmed reservation is nevertheless a promise of a seat.

A customer sometimes sees a spinning screen after pressing Confirm. The server might still be processing, might already have reserved the seat, or might not have accepted the request. The screen alone cannot distinguish these states. The team must set the retry rule, not change seat eligibility or cancel legitimate orders.

Option A creates a new order for every accepted submission, including a retry after a timeout. Option B assigns a stable request identifier before the first submission, preserves it when retrying that intended order and shows its existing result if completed. A clearly separate Book another seat action creates a new identifier. Both are feasible within the funded release work. B needs additional state management and testing; A is simpler but leaves duplicate consequences to support staff. Release can wait if correctness checks fail.

## Evidence

A timeout means the customer did not receive a usable response. It does not establish whether the server reserved a seat. Matching booking details and click counts do not, by themselves, establish the number of intended orders.

**Student question:** Should the booking tool treat each retry as a new order or recognise a stable identifier for the original request? Explain how your rule would preserve a genuinely separate booking.

## Round two

A controlled pre-release test supplies the missing facts. Lin intended one seat. Her first submission reserved it, but the reply was delayed. She selected Retry twenty seconds later, still intending the same order. Separately, Sam deliberately selected Book another seat after his first booking was confirmed: he wanted two seats for two friends. Sam’s two orders have identical account, workshop, quantity and contact fields. These are verified intentions in the test, not inferences from similar records.

In the proposed B design, Lin’s first attempt and retry carry identifier L1. Sam’s separate orders carry S1 and S2. These short labels are classroom notation; production identifiers would be generated to avoid collisions and contain no personal information. Identity is scoped to the authenticated account and the create-reservation operation. A changed quantity or workshop under an existing identifier is rejected for resolution rather than silently replayed or treated as a fresh order.

The proposed service contract retains retry identities and their outcomes for 48 hours from first acceptance. All test attempts occur within one minute. This is a fictional design assumption, not a provider guarantee. An unresolved request approaching or beyond that window goes to reservation-status reconciliation, not an automatic new identifier. While an order is still processing, the interface says Pending and offers status checking; it does not promise another seat. The existing reservation record remains authoritative after retry-state expiry.

**Student question:** How should the tool handle Lin’s retry and Sam’s two bookings? Specify the identity rule, the response to an uncertain result and one test that would expose an unsafe design.

## Count intentions, not attempts

Under B, Lin receives one reservation and its existing result; Sam receives two separate reservations. Three intended orders therefore produce three seats. A would produce four if all four submissions were independently accepted. A rule merging all matching details would leave only two seats across the two customers and wrongly suppress Sam’s legitimate second order. These are outcomes for stipulated test inputs, not an estimated defect rate.

## Make identity a service contract

Choose B for the stated promise. Generate and retain the identifier before the first send; do not replace it merely because a reply is slow. Show the reservation reference when complete and distinguish Retry this order from Book another seat. Idempotency means repeating the same intended operation does not add another reservation. It does not mean every message is delivered once or every response is identical. New intent must remain possible.

## Protect the boundary, not only the button

Recording the identifier and committing the reservation must succeed together or fail together. Concurrent submissions with the same identity must not each pass an independent check and reserve a seat. A pending outcome should lead to status checking or controlled retry with the same identity, not a fresh booking. If the identity store is unavailable, pause or reconcile instead of silently dropping protection. Keep normal account authorisation: an identifier is not permission to read another customer’s reservation.

Test a committed booking with a lost reply, two simultaneous copies, the same identity with changed fields, two distinct identities with identical fields, and uncertain status near expiry. Check seat records as well as screens. If confirmations or other downstream actions are added, give those effects their own duplicate controls; protecting reservation creation alone does not guarantee a single email or payment.

## A reasonable objection

B adds storage, concurrency handling and clearer interface states. If those safeguards cannot be verified, delaying release and handling uncertain requests through an authorised status check is preferable to asserting that retries are safe. A can be acceptable for a deliberately non-binding enquiry inbox with human reconciliation before any commitment, but that would change this case’s immediate reservation promise. Disabling the button can reduce accidental clicks; it cannot resolve a lost response or a retry from another session.

## Instructor note

Ask students to state an identity rule before showing the two customers. The reveal challenges both “every click is new” and “identical details are duplicates”. Keep the class focused on business intent, authoritative status and testable promises, not memorising HTTP headers. The migration case concerns transfer between old and new systems; this case has one reservation system and repeated deliveries of an operation. Physical mistake prevention can help interface use but is not a substitute for server-side transaction identity. No real bookings, payments or production changes are requested.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All organiser, customer, timing and design details are original fiction. One order reserves one transferable seat; multiple orders per account are permitted, capacity is ample and no payment is taken. Lin has one intent and two submissions; Sam has two intents and two submissions. Correct outcome is three seats, independent submission processing would create four, and merging matching details would leave two. All attempts occur within one minute. Forty-eight-hour retention is a stipulated contract, not an industry standard. Existing reservation records survive retry-state expiry. A pending or expired uncertain request requires status reconciliation, not blind creation. Public sources explain technical principles and distinct provider contracts; none is evidence that the fictional implementation has passed its tests.

- [RFC 9110, section 9.2.2: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods). Defines repeated intended effects and cautions against automatic retries without appropriate semantics. It does not make every POST operation idempotent.
- [Amazon Builders’ Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). Explains why identical parameters can represent separate intentions, caller request identities and atomic recording with the associated mutation.
- [Stripe: Idempotent requests](https://docs.stripe.com/api/idempotent_requests). Documents API-version-specific replay behaviour, request-key generation, parameter comparison and retention limits. The case does not adopt Stripe’s exact contract.
- [PayPal Developer: Idempotency](https://developer.paypal.com/api/rest/reference/idempotency/). Shows how a timed-out operation may have succeeded and how a supported request identifier retrieves its status; support and retention depend on the API.
- [Adyen: API idempotency](https://docs.adyen.com/development-resources/api-idempotency/). Documents scope, validity, concurrent requests and transient-error handling. Cross-region and provider-specific limits illustrate why the contract must be explicit.
