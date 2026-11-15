# Easy access. Appropriate access?

<!-- legacy-case-id: 200 -->

IS-17 · Hong Kong · 10–15 minutes · Least privilege · Role design · Absence coverage

![Two equipment-hire colleagues discuss a proposed scheduling tool beside plain paperwork and a laptop.](../cover-the-task-not-every-permission-scene.jpg)

## Access is part of secure operation

On 20 January 2025, HKCERT’s Hong Kong Cyber Security Outlook briefing included least privilege among its account-management recommendations. The briefing concerned wider cybersecurity risks, including digital signage; it does not establish a breach or measured benefit at the office below. Our organisation, records, tasks and costs are original fiction.

## Opening decision

A fictional Hong Kong equipment-hire office is replacing a small internal scheduling tool. The exercise uses only invented corporate order codes, equipment categories and completion statuses. It contains no real customer data, contact details, payment identifiers, credentials or sensitive records. The question is how to assign functions on already-authorised operational records, not whether to collect more data.

Each worker will have a named account with strong authentication and an action log. Neither option permits shared passwords, user administration or deletion of records. B, a broad operational role costing HK$2,000 to configure and test, gives the three office staff view, status-edit and export functions. N, narrower named roles costing HK$5,000, separates those functions by task and includes a tested temporary-permission workflow. The figures are one-time configuration costs; equal ongoing support is funded separately. Both fit the available budget and launch date.

The owner values quick absence cover and worries that narrow roles will block work. The team has not yet completed its task-to-permission map. These are proposed configurations, not permissions already granted. Data access must still have a business purpose and authorised scope; no security baseline or contractual restriction can be waived merely to save setup time. Choose a provisional design and explain what workflow evidence you need before approval.

## Evidence

| Proposed design | Setup cost | Coverage approach |
|---|---:|---|
| B: broad named role | HK$2,000 | All three have view, status-edit and export |
| N: narrower roles | HK$5,000 | Task permissions plus tested temporary cover |

**Student question:** Which design would you provisionally approve, and what task-and-absence evidence must you check first? Explain why a named login and an action log do not by themselves establish that every permission is needed.

## Round two

The completed map shows that coordinators Mei and Arun must view the active-order list and edit completion status for daily scheduling; each is trained and authorised to cover the other. Neither needs routine export. Office manager Jo needs to view active orders and export only the previous month’s approved monthly summary into a designated internal reporting folder; Jo does not need routine status editing. Nobody needs deletion, user administration or a download of the entire historical order register. Under B, the export function would allow that whole-register download even though no task requires it.

When Jo is absent, Arun is trained and authorised to produce that same monthly summary. Under N the owner, or a designated independent deputy if the owner is unavailable, can approve a logged two-hour export permission restricted to that summary and destination; it expires automatically, with completion and revocation checked. Arun cannot approve his own access. The tested approval process completes within two working hours; the reporting task is requested at least one working day before its deadline. No emergency workaround or credential sharing is needed.

The quoted HK$5,000 includes those role restrictions, cover assignments, expiry tests and staff training. Both coordinators keep ordinary scheduling access during leave coverage. Departures and role changes trigger review; logs are examined under the office’s limited retention policy. The extra setup cost is HK$3,000. There is no supplied breach probability, loss estimate or quantified productivity improvement from which to calculate a financial return.

**Student question:** Using the completed task map, would you keep or revise your design? Specify Mei’s, Arun’s and Jo’s ordinary permissions, Arun’s temporary absence-cover permission, and one test that checks both access restriction and completion of the work.

## Authentication is not authorisation

Named accounts identify who acted; logs can support later review. They do not make a permission necessary. View, edit and export are distinct capabilities, and exporting a whole register creates a different exposure from viewing an active scheduling list. B’s convenience does not justify functions absent from the completed task map.

## Give the task enough access

Mei and Arun need active-order viewing and completion-status editing, including reciprocal cover. Jo needs viewing and a scoped monthly-summary export, not routine editing. N can support those jobs without whole-register export, deletion or user administration. Least privilege means enough for the authorised task, not the smallest number of permissions regardless of service failure.

## Design the exception as part of the workflow

Arun’s authorised monthly-summary cover uses an independent approver or deputy, a stated purpose, restricted output and destination, a two-hour window and checked expiry. The two-working-hour approval fits the one-working-day lead time. A permanent broad export right is not required for this occasional task. If approval timing, staffing or the task changes, reassess the design rather than assume the exception still works.

## Pay for a usable control, not a guarantee

N costs HK$5,000 versus HK$2,000: HK$3,000 more upfront. Under the supplied map it supports necessary work while avoiding unnecessary permissions, so it is the defensible design. That does not prove it prevents every incident or pays for itself. Review role assignments, logs, changes and real task completion; a well-named role can still contain excessive rights if its configuration is wrong.

## Instructor note

Draw a person-by-action map, then simulate Jo’s absence. Test that Mei cannot export, that Arun cannot export without the approved temporary grant or after expiry, and that the scoped report reaches the correct internal folder on time. Also test that ordinary scheduling still works. Do not use real accounts, records or credentials, and do not actually change any system permissions. The exercise concerns role design, not collecting fewer fields or profiling employee trustworthiness.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional system and records only. Two configuration quotes of 2,000 and 5,000 imply incremental setup cost 3,000 HK dollars; both include ordinary named accounts, authentication, logs, funded support and adequate budget. N includes staff training, tested approvals, independently authorised backup, exact scope/destination, two-hour expiry and review. Jo’s report is requested at least one working day before deadline; approval within two working hours. No claim that logged broad permissions are safe merely because records are non-sensitive. No actual permissions, credentials, external transmission, administrative access or sensitive data in task. Broad-role option is an unapproved initial design, not an authorised security exception. After map, N meets least-privilege and coverage needs; no unsupported ROI or probability. Distinct from GVR data minimisation: existing authorised operational fields unchanged, focus who may perform which action and when. Five actual bodies read: HKCERT dated briefing, HK Government InfoSec guidance, NIST glossary, NZ NCSC guidance and NIST demonstration. Two NIST sources overlap institutional origin and support definitions/design, not measured business outcomes. PCPD direct page returned no lines and is not counted or cited, despite useful indexed text. No source diagrams/data reproduced.

- [HKCERT · Cyber Security Outlook · 20 January 2025](https://www.hkcert.org/press-centre/hkcert-unveils-hong-kong-cyber-security-outlook-2025-phishing-hits-five-year-high-vulnerabilities-in-supply-chain-and-ai-content-hijacking-emerge-as-key-risks-over-half-of-enterprises-fear-cyber-attacks-on-iot-digital-signages). Actual dated briefing and least-privilege recommendation read. Wider threat context only, not an incident or effect estimate for this office.
- [Hong Kong Government InfoSec · Control access](https://www.infosec.gov.hk/en/best-practices/business/control-access-to-critical-information). Actual role-based rights, unique IDs and review/removal guidance read. No blanket legal-compliance conclusion.
- [NIST · Least privilege](https://csrc.nist.gov/glossary/term/least_privilege). Actual task-minimum access definitions read. A definition, not a complete implementation standard or effectiveness study.
- [New Zealand NCSC · Principle of least privilege](https://www.ncsc.govt.nz/protect-your-organisation/principle-of-least-privilege/). Actual task mapping, role review and time-bounded access guidance read. Institutional guidance adapted to a fictional non-sensitive workflow.
- [NIST · Data-level security demonstrations](https://pages.nist.gov/zero-trust-architecture/VolumeD/UseCaseH.html). Actual H-5 temporary access and H-6 restricted operations read. Demonstration concepts, not evidence that this office’s configuration is certified or tested in reality.
