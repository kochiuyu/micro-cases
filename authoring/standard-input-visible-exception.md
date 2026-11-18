# Standardise the input. Keep the exception visible.

<!-- legacy-case-id: 472 -->

OPS-40 · Hong Kong · 15–20 minutes · Service standardisation · Exception routing · Input design

![Two adult parcel-support colleagues in a Hong Kong office compare blank intake forms beside plain sealed parcels and an unlettered workflow board, without showing routing outcomes.](../standard-input-visible-exception-scene.jpg)

## Consistency needs a route for differences

Public service-design guidance recommends asking relevant questions, testing routes and helping users who cannot provide an expected answer. Process guidance also connects inputs with downstream activities. The fictional desk below asks whether a common intake can preserve a meaningful exception without becoming an uncontrolled collection of special requests.

## Opening decision

You manage fictional Harbour Parcel Support in Hong Kong. The desk answers administrative delivery-status enquiries for cross-border parcels. It does not release goods, decide customs clearance or handle dangerous-goods declarations. Those responsibilities and all existing safety, privacy and legal controls remain outside this redesign.

Two teams currently use different intake forms for the same service. Staff repeatedly translate field names when transferring an enquiry. Management wants consistent identifiers and fewer wrong-team transfers, not a cut in staffing. Two affordable designs use the same existing system, paid training allowance and authorised teams.

A uses one fixed form and one default destination for every enquiry. B offers separate routine and exception forms with shared core fields; staff must choose the right form before entering details. The service owner has not yet mapped the request mix or tested either design. Both proposals retain required checks and audit records.

## Evidence

| Design | Core fields | Destination rule |
| --- | --- | --- |
| A · Fixed form | Same for all | One default team |
| B · Separate forms | Shared definitions | Chosen form determines team |

**Student question:** Which design would you provisionally trial? What must you learn about requests and downstream ownership before treating one form as a complete standard?

## Round two

A reviewed fictional set contains 200 enquiries: 184 routine tracking questions and 16 about a return already accepted by the returns desk. These groups do not overlap. The latter need the returns team, not the tracking team. The accepted-return reference is visible to intake staff in the existing record.

In a diagnostic replay, A sends all 200 to tracking. The 16 returns enquiries then need correction and transfer. B sends all 200 correctly when a trained reviewer selects each form using that reference. This proves a distinction matters in the replay, not that real staff will always choose correctly.

A third feasible design, C, keeps one common intake with a required routing question: does the existing record show an accepted return? Yes reveals the return-reference field and sends the enquiry to returns; no sends it to tracking. Cannot determine sends it to the existing authorised support lead for clarification, never silently to tracking.

C fits the same funded allowance and existing system. The lead has verified capacity for the pilot; clarification does not permit bypassing required checks. Staff retain the original receipt time, explain uncertainty to the customer and record the final route. The pilot cannot promise instant clarification or a faster resolution time.

**Student question:** Which design would you trial now? Calculate A’s wrong-first-team rate in the replay. Specify C’s exception rule, owner and monitoring, and explain what should remain standard even when the route differs.

## Debrief · Standardise the useful common core

A misroutes 16/200 = 8% of the reviewed set; 92% take the appropriate initial route. A high routine share does not make the minority irrelevant. The aggregate can conceal a systematic failure concentrated in one recognisable category. These are routing results, not resolution or satisfaction rates.

Trial C, retaining common field definitions, required evidence, timestamps and audit records. Vary only the questions and destination needed for the identified condition. Standardisation means a repeatable rule, including a repeatable exception rule; it does not require identical processing for materially different requests.

## Debrief · Bound the exception

Use the existing accepted-return status, not a vague request to describe anything unusual. Record the reference, route to the named returns team and preserve ownership until accepted. Unknown status goes to the support lead. A blank answer must not become an unannounced no.

Do not let free text authorise arbitrary routes or let customers invent acceptance references. Nor should staff infer accepted status merely because someone wants to return a parcel. The record establishes this administrative category; it does not establish any customs, refund or delivery entitlement.

## Debrief · Keep the alternative credible

B remains defensible if separate forms make responsibilities clearer and staff select reliably. Its shared definitions already provide some standardisation. C avoids choosing a form before the routing question, but that is a design hypothesis to test, not proof that one interface always beats two.

The replay establishes A’s mismatch under its stated default rule. It does not measure completion effort, unknown-status frequency or ordinary staff performance under C. The case supplies no basis to claim a cash saving or a causal improvement in customer satisfaction.

## Debrief · Test routes, not only fields

Before launch, test yes, no, unknown and corrected-answer paths with realistic records. Confirm that a changed answer updates the destination and does not leave stale hidden data. Provide persistent instructions and an accessible way to obtain help; test with staff using their normal tools.

During the bounded pilot, count wrong-first-team transfers by category, clarification backlog, time to ownership and resolution, missing evidence and customer effort. Include unresolved requests. Review emerging exceptions with the service owner instead of quietly adding unchecked branches. Stop or revise if routing or controls deteriorate.

## Instructor note

Ask students first to name the common input standard, then draw the three branches and name the owner at each handoff. Separate a known return from unknown status. Keep the original receipt clock running through clarification so an apparently tidy form cannot hide waiting.

OPS-08 changes a physical packing step to expose omissions; OPS-23 assigns queued work to qualified employees. This case changes the information captured before routing and the controlled treatment of exceptions. Every desk, count, capability and cost assumption is fictional; source guidance supplies design principles, not carrier performance evidence.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All desk facts, counts, capabilities and allowances are fictional. Reviewed set184routine+16acceptedreturns=200, exclusive. A default tracking misroutes16=8%; B diagnostic selection correct but not representative trial. C feasible funded conditional intake with unknown to existing authorised lead with verified pilot capacity. No waived controls, no customs release/refund entitlement, no personal data printed, unchanged staffing. No measured performance for C; preserve receipt clock and monitor all unresolved work. Sources are background guidance, not validation of invented outcomes.

- [GOV.UK Forms · Using routes](https://www.forms.service.gov.uk/about/using-routes). First-party guidance explains conditional routes and checking them after structure changes. It does not supply this fictional request mix or performance.
- [Sarah Gibbons · Service Blueprints: Definition](https://www.nngroup.com/articles/service-blueprints-definition/). Original service-design guidance links customer actions with frontstage and backstage dependencies. It supports mapping ownership, not a quantified benefit from one form.
- [NHS digital service manual · Use filter questions to route users](https://service-manual.nhs.uk/content/how-to-write-good-questions-for-forms/use-filter-questions-to-route-users). First-party guidance addresses early filtering, unclear answers and alternative support. Healthcare context is not a legal rule for parcel support.
- [ISO · The process approach in ISO 9001:2015](https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/iso9001_2015_process_approach.pdf). Official explanation connects inputs, activities, outputs and context-dependent controls. This case does not assert certification or reproduce the full standard.
- [W3C WAI · Form Instructions](https://www.w3.org/WAI/tutorials/forms/instructions/). Original accessibility tutorial explains persistent instructions, required fields and label associations. It supports usable input design, not a routing-success estimate.
