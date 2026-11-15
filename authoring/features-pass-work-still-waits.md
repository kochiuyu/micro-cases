# The feature is delivered. Is the work supported?

<!-- legacy-case-id: 212 -->

IS-18 · Hong Kong · 10–15 minutes · Requirements · User acceptance testing · End-to-end workflow

![Two design-services colleagues discuss a proposed tool beside a laptop and plain documents.](../features-pass-work-still-waits-scene.jpg)

## Test the task, not only the screen

On 11 April 2023, Singapore’s GovTech described the refreshed LifeSG app and two rounds of user testing. Participants attempted service tasks, and feedback exposed a booking obstacle that was not obvious from a list of available services. This institutional account motivates the question below; it is not evidence about our fictional system or a controlled estimate of user benefit.

## Opening decision

A fictional Hong Kong design-services firm has commissioned an internal job-request tool. It can create a request, assign an owner, attach a specification and mark work complete. Each feature passes its agreed individual functional check. Staff want to replace part of a shared spreadsheet process, but a request sometimes moves between teams when the first team cannot handle it.

Before the controlled release, the operations manager must decide what evidence will count as operational acceptance. A uses the passed feature checks as the starting point and releases a small, four-week internal trial, with documented manual handoffs and monitoring where needed. B requires a complete cross-team task demonstration before releasing even that trial, accepting a possible delay and extra integration work. Neither route may bypass mandatory security, privacy, accessibility, authorisation or record-retention checks; those have already passed. Contractual payment and supplier obligations are separate and unchanged.

Both routes are funded, and the existing spreadsheet process remains staffed and available. No external customer is promised an earlier service. Before either route starts, a brief common walkthrough uses thirty synthetic requests and approved staff test accounts. The manager sets the initial acceptance priorities now, then will use that walkthrough to confirm the release route. No live customer data are used. A is not permission to overlook an unsupported handoff; it requires a tested, owned temporary process.

## Evidence

| Already checked separately | Whole-task question still to demonstrate |
|---|---|
| Create, assign, attach, complete | Can the second team receive the correct request and current specification? |
| Authorised access and records | Who owns a reassigned request until accepted? |

**Student question:** Would you initially favour the controlled release with a documented temporary process, or require the complete cross-team demonstration first? State the acceptance evidence you need beyond a list of working features.

## Round two

The walkthrough finishes all thirty synthetic requests. Nine require reassignment. For those nine, the second team cannot inherit the attached specification automatically: a coordinator must copy the current file into a new authorised task and cross-reference the original request. The ordinary feature checks still pass. The nine cases each take ten additional minutes of paid coordination, ninety minutes in total. This deliberately constructed test set is not a frequency forecast for live work.

A documented workaround is then tested successfully: the original coordinator retains ownership until the second team acknowledges receipt; both tasks are cross-referenced, the current specification is verified and only authorised accounts are used. A can start the four-week trial now with at most thirty such reassignments. Five paid coordination hours cost HK$1,500 in total at HK$300 per hour. A daily count and an owner are assigned. Any case that cannot be handled correctly, or any reassignment beyond the cap, stays in the existing staffed spreadsheet process. No customer deadline or protection is relaxed.

B adds an automatic handoff at a confirmed all-in HK$6,000 cost, with a two-week delay and a required repeat of the cross-team tests before trial release. The old process covers that period. The remaining two-week observation window will be shorter if the team keeps the same review date. Both alternatives fit approved funds. The longer-run volume, value of earlier learning and future maintenance cost are unknown, so neither cost is a complete business case. A is temporary, not approval for unrestricted rollout; B is not accepted merely because the supplier says the enhancement is ready.

**Student question:** Which release route would you choose now, and what exact pass condition, owner and stopping rule would you record? Explain how you would distinguish a working feature, a supported task and readiness for wider use.

## Acceptance follows the work

Functional checks establish that each specified feature behaves as tested. Operational acceptance asks whether authorised people can complete the business task, including a cross-team handoff and its exceptions. Here, nine requests expose an extra step rather than a failed individual feature. Define the expected input, owner, current specification and acknowledged receipt, then test the complete path.

## A workaround is a process, not a promise

A is credible only because the temporary handoff has been tested, paid capacity is capped and the old process remains available. Nine times ten minutes is ninety minutes in the constructed test. Thirty permitted reassignments times ten minutes is five hours; five times HK$300 is HK$1,500. Do not turn 9 / 30 into an expected production rate or assume all requests need that effort.

## Choose the boundary of approval

A buys earlier bounded operational learning at the cost of coordination and a future review. B buys a more integrated handoff, with added expenditure, delay and less observation by the same review date. Either can be justified without pretending that approval of one trial approves the whole service forever. Record actual handoff performance, failures and workload before expanding; require retesting after the enhancement.

## Instructor note

Ask students to write a pass condition a different employee could observe: correct current specification reaches an authorised recipient, ownership remains explicit and receipt is acknowledged. Do not reward a vague “all features work” or an unlimited manual workaround. IS-03 tests recovery after disruption; this case defines ordinary task acceptance before release. It does not reinterpret the supplier’s contract, authorise live deployment or replace mandatory compliance checks.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All firm, system, test and cost facts are original fiction. The thirty requests are a constructed synthetic test set, not a random sample. Nine reassignments at ten extra minutes each total ninety minutes. The temporary cap of thirty reassignments requires five hours, priced all-in at HK$300 per hour, total HK$1,500. The workaround is tested and authorised; cap overflow and any unsupported task revert to the staffed old process. The HK$6,000 enhancement is all-in and includes repeat acceptance testing; it delays release two weeks. Mandatory protections already pass and remain mandatory under both routes. Operational acceptance is not a waiver of supplier obligations or payment rights. No live data, outreach or deployment is performed. Two DPO references and two UK government references are related guidance, not independent empirical studies.

- [GovTech Singapore: LifeSG makeover, 11 April 2023](https://www.tech.gov.sg/technews/lifesg-gets-a-makeover/). Institutional account describes task-based testing and booking feedback. Not a controlled evaluation or evidence for the fictional workflow.
- [Hong Kong Digital Policy Office: Guidelines for Application Software Testing](https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/methodology/system_development/application_software_testing.html). Distinguishes functional and acceptance testing, and documents test evidence. Guidance, not a certification of this tool.
- [UK Government Service Manual: quality assurance and regular testing](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly). Testing covers usability and technical aspects under normal and unusual conditions. No fictional cost or threshold comes from this guidance.
- [UK Government: Gate 4 readiness for service](https://www.gov.uk/government/publications/gate-review-4-readiness-for-service/gate-4-review-readiness-for-service). Relevant sections discuss end-to-end tests, acceptance criteria, corrective action and transition ownership. Public-sector assurance context, not a binding rule for this firm.
- [Hong Kong DPO: Best Practices for Business Analyst, section 3.6.2](https://www.digitalpolicy.gov.hk/tc/our_work/digital_infrastructure/methodology/system_development/doc/G60_Best_Practices_for_Business_Analyst_v1_3.pdf). Actual guide calls for realistic process flow, expected outputs and acceptance criteria. Same institutional family as the testing overview.
