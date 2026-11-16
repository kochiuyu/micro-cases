# The evidence exists. Can its history be shown?

<!-- legacy-case-id: 273 -->

GVR-23 · Hong Kong · 15–20 minutes · Evidence integrity · Chain of custody · Investigative uncertainty

![Two fictional internal reviewers discuss a plain folder beside an unbranded laptop in a private office.](../evidence-exists-history-shown-scene.jpg)

## A file needs a handling history

Digital-evidence guidance separates preserving the received bytes from explaining their source and handling. A cryptographic hash is a calculated fingerprint used to compare file contents; it is not a certificate that the underlying business event occurred. Investigation guidance also stresses fair fact-finding rather than trying to confirm an accusation.

This fictional internal review uses supplied permissions and procedures. It is not a court-admissibility decision, forensic tutorial or statement of Hong Kong legal requirements.

## Opening decision

A fictional Hong Kong distributor is reviewing whether a promotional artwork approval was recorded before an agreed release cutoff. Release is safely paused; no customer, pay or safety obligation depends on today’s update. An independent reviewer must plan the first examination, not decide fault.

A qualified records custodian has already preserved the relevant original records and audit logs under restricted access. The review is authorised for one artwork record and its approval history only. Personal mailboxes, unrelated employee records and broader monitoring are outside scope. Both proposed methods preserve privacy, original material and access logs; there is no risk of scheduled deletion today.

C provides a controlled read-only export copy of the scoped record, with export settings, collector identity and receipt record. It takes two staff-hours including its initial examination. It offers a stable item for comparison but may not include every source-system relationship. S provides a supervised read-only examination of the source system and a recorded session, taking three staff-hours including custodian support. It offers current context, but a current display does not automatically recreate an earlier state.

Four staff-hours are funded for this initial stage, leaving two after C or one after S for framing follow-up questions. Both methods are feasible; neither guarantees the answer. A later investigation allowance is separate. Staff may not change source records, override access controls or privately forward evidence.

## Evidence

| Initial review | Staff-hours | Evidence benefit |
|---|---:|---|
| C controlled export | 2 | Stable scoped file and recorded settings |
| S supervised source | 3 | Current context and logged session |

**Student question:** Would you begin with the controlled export copy or supervised source-system review? Explain the useful evidence each provides, its limitation and the handling record you require.

## Round two

The first stage ends without a finding. Whichever route you chose, the custodian supplies two relevant files already received through approved channels. They display different statuses for the same artwork identifier. Both are now separately preserved, assigned unique evidence IDs and hashed at receipt. Their hashes differ; repeat checks of each against its own receipt hash match.

| Received file | Displayed status | Known handling history |
| --- | --- | --- |
| A | Approved | Named collector, scoped export settings, 10:00 receipt and protected hash record |
| B | Pending | Received at 11:00; original export time, settings and intermediate handling unknown |

No reliable record yet establishes whether B came from another export time, filter, workflow state, formatting process or an altered source. Its displayed creation date alone does not settle this. A’s handling is better documented, but its approval status at export does not prove who approved the artwork or when. Neither file alone answers the cutoff question. No person is accused on this evidence.

Before a non-decisional interim update, four further staff-hours are available. Route H uses three hours with the authorised custodian to trace export settings, relevant audit history and handoffs, plus one hour to report. Route W uses two hours for voluntary factual interviews with the two people who supplied the files, one hour for a scoped side-by-side comparison and one hour to report. Both are funded and competently staffed, preserve the originals, and may yield incomplete explanations. The work not selected can be scheduled next; there is no imminent loss of data or witness availability.

The update may explicitly say the chronology is unresolved and request a documented next step. It cannot declare misconduct or certify which file is historically correct without supporting evidence. Keep both versions, record the uncertainty and do not overwrite one with the other. Any broader collection needs separate authority; confidential evidence stays with the assigned team.

**Student question:** Which follow-up would you prioritise before the interim update? State what the two files establish, what remains unproven and how you will preserve both while investigating their difference.

## Separate three questions

Integrity asks whether a particular received item has stayed unchanged. Provenance asks where it came from and how it was created and handled. Interpretation asks what it shows about the business event. A stable file can still have incomplete provenance, and a well-documented export can still omit facts needed to interpret approval.

## Interpret the hashes narrowly

Different hashes mean the compared byte sequences differ. They do not identify the cause, the changed fields, the responsible person or the correct chronology. Matching each file to its own receipt hash supports that it has not changed since that recorded baseline, assuming the protected process works. Hashing B now does not reconstruct its missing export history. No learner needs to calculate a hash.

## Preserve uncertainty as well as content

Retain A and B as distinct items with their original receipt records. Keep a protected master and use controlled working copies for comparison; record any derived comparison separately. Log who collected or received each item, source, method, settings, time and time zone, access and transfers. Mark missing facts as unknown. Never backfill an invented collector, change an original to match the other file or discard the inconvenient version.

## Choose the next evidence, not the verdict

H is defensible when the key uncertainty is the system history and export conditions. W is defensible when the suppliers can explain the handoff or intended export, with their accounts recorded as statements to corroborate rather than established fact. H uses 3 + 1 = 4 staff-hours; W uses 2 + 1 + 1 = 4. Either may leave the cutoff unresolved. A helpful interim report distinguishes observations, sources, competing explanations and the next authorised check.

## What could resolve the chronology?

Ask whether preserved audit events identify the relevant approval action, actor, timestamp and record version, and whether clock/time-zone conventions and export settings explain the difference. Compare that context with the supplier accounts and contents. These are questions for the qualified custodian, not permission to alter systems. A later conclusion must state its supporting evidence and remaining limits; an unexplained discrepancy alone is not proof of tampering.

## Instructor note

Ask learners what a hash can and cannot establish before revealing the missing history. Accept either initial method and either follow-up when the evidence benefit and limitations are explicit. Reward preserving both versions, respecting scope and issuing a qualified interim update. Do not turn the exercise into employee blame, a forensic acquisition procedure, a retention-deletion choice or a dashboard recalculation. Real legal or disciplinary consequences require the appropriate specialist process.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All organisation, artwork, files, statuses, times, permissions and hour budgets invented. No real data collection or system action. Records already preserved, no imminent loss, privacy scope fixed. Hash facts stipulated, not actual calculations. No earlier event time can be inferred from receipt at 10:00/11:00 or displayed creation date. Initial 4 hours and separate follow-up 4 are distinct allocations. UK/US/IETF guidance supports narrow evidence-handling concepts, not HK legal advice or admissibility.

- [NIST IR 8387 · Digital Evidence Preservation · September 2022](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8387.pdf). Actual source/transfer documentation, protected hashes and baseline limitations sections read. Supports preserving received evidence; does not certify a business event or a legal conclusion.
- [SWGDE · Best Practices for Digital Evidence Collection · Version 2.0, November 2025](https://swgde.org/wp-content/uploads/2025/12/2025-11-20-Best-Practices-for-Digital-Evidence-Collection-18-F-002-2.0.pdf). Actual original third-party production, hashing and contemporaneous documentation sections read. Professional guidance, not authority for this fictional review to collect extra data.
- [IETF RFC 3227 · Guidelines for Evidence Collection and Archiving · February 2002](https://www.rfc-editor.org/info/rfc3227/). Original chain-of-custody and restricted-archive sections read. Used for recording discovery, handling and transfers; old tool/algorithm suggestions are not adopted.
- [NIST SP 800-86 · Integrating Forensic Techniques into Incident Response · August 2006](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf). Original master/working-copy and reporting discussion read. Used for separation of preservation, examination and qualified reporting, not as current technical acquisition instructions.
- [Acas · Carrying out an investigation](https://www.acas.org.uk/investigations-for-discipline-and-grievance-step-by-step/step-3-carrying-out-an-investigation). Actual fairness, privacy and how/why evidence was obtained guidance read. UK comparative guidance only; no UK legal powers or duties imported.
