# The backup is green. Can the shop work again?

Case 35 · Hong Kong · 10–15 minutes · Information systems · Business continuity · Recovery testing

![A framing-shop owner and technician discuss a laptop, backup drive and job-ticket printer at the counter.](../recovery-rehearsal-scene.jpg)

## In the news

On 14 November 2025, 47 financial-services firms took part in Hong Kong’s WISE2025 continuity exercise. Its scenario combined a simulated super typhoon with telecommunications outages and degraded data-centre services.

This was an online tabletop simulation, with no actual physical responses. It was not proof that the firms had restored their production systems. The principle for a smaller business is to rehearse what it would take to keep working, not simply own backup equipment.

## Opening decision

Fictional classroom situation. You own a Hong Kong picture-framing shop. Staff use an order application to check dimensions and print workshop job tickets. After an interruption, your agreed business target is to resume those two tasks within two hours.

The nightly backup dashboard reports successful jobs. Storage monitoring shows enough room for the planned backup retention, and a replacement laptop is available. Nobody has rehearsed the complete recovery workflow on it.

This month’s improvement budget can fund either additional storage capacity or technician time for a supervised recovery rehearsal and initial fixes. Both fit the budget. You can also defer the spending. These are the current options, not a claim that storage and testing are substitutes in every business.

## Evidence

Known: green backup-job reports, enough storage for planned retention, and a replacement laptop.

Not demonstrated: a staff member finding an order and printing a correct job ticket within two hours of interruption.

**Student question:** Buy more backup storage, fund a supervised recovery rehearsal, or keep the current arrangement? What does the green report actually establish?

## Round two

The owner authorises an isolated rehearsal using copied test orders, supervised by the technician. It does not change live orders or interrupt the shop.



| Observed test stage | Time taken |
|---|---:|
| Restore order files | 40 minutes |
| Rebuild settings/templates and validate workflow | Another 3 hours |

The backup files are readable. But the recovery plan did not include the application settings and ticket templates needed to turn an order into a correct workshop job ticket. Staff can complete that task only after both stages. The test clock starts at the simulated interruption; the stages are consecutive and include all elapsed time in this exercise.

No real orders are lost or changed. This test examines recovery time for the selected scenario; it does not prove that the backup schedule meets the shop’s separate tolerance for losing recent changes.

**Student question:** Has the shop met its two-hour recovery target? What must be fixed and demonstrated before you call it ready?

## Count until the business can work

The observed recovery takes 40 + 180 = 220 minutes, or 3 hours 40 minutes. That exceeds the two-hour target by 100 minutes: 1 hour 40 minutes.

Stopping the clock when files appear on the laptop would measure the wrong finish line. The target covers usable order lookup and correct job-ticket printing, not data copying alone.

## Fix the missing links, then retest

Assign an owner to include the required application settings and templates in the protected recovery materials and document the authorised recovery sequence. Keep access appropriately restricted. The technician should check the dependencies rather than assume this is the only missing item.

Repeat a controlled, isolated test from the simulated interruption through staff validation of a sample order and its correct printed ticket. Record elapsed time, exceptions and corrective actions. Until that test meets the target, do not claim that fixing one file proves readiness.

More capacity for the same incomplete backup would not resolve the gap demonstrated here. Continue monitoring storage and retention; additional storage could become necessary if those requirements change.

## Two different recovery questions

How long can we be unable to work? That is the recovery-time question tested here.

How much recent work can we afford to lose? That is a separate recovery-point question. A nightly copy may be too old for some businesses even if it restores instantly. Set that tolerance from business needs and check the backup schedule against it; this case gives no numerical loss tolerance.

A successful rehearsal is evidence for the tested scenario, not a guarantee against every disruption. Review the plan when software, staff, equipment or business requirements change.

## Instructor note

Allow 2 minutes for the first vote, 3 for the test result and 5–7 for the recovery plan. Ask the storage group what demonstrated constraint extra space removes. Ask the rehearsal group to define the finish line before calculating elapsed time. Close by distinguishing a successful job report, readable files and a usable business service. This is business planning, not an instruction to experiment on a live system.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The framing shop, systems, budget choices, target and test timings are invented teaching assumptions. The exercise uses copied test orders in isolation; it is not a live failover or security drill. WISE2025 is a real tabletop event, not a reported production recovery. HKMA observations concern banking and are not presented as legal requirements for a framing shop. NIST guidance is US federal guidance, not Hong Kong law. The GitLab incident is historical, not evidence about its current reliability. Undated pages checked 14 November 2026.

1. [HK Financial Services Business Continuity Management Forum · WISE2025](https://www.hkfsbcm.org/wise-2025.html) — Event held 14 November 2025: 47 firms, online tabletop simulation, severe-weather and service-dependency scenario; no actual physical responses. Page publication date unspecified.
2. [HKMA · Good practices for addressing vulnerabilities related to operational resilience, 1 April 2026](https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20260401-2-EN/20260401-2-EN.pdf) — Annex discusses recovery testing, backup restoration in end-to-end exercises and dependencies. Banking supervisory context, not a small-business compliance checklist.
3. [HKCERT · Frequently asked questions, questions 36–37](https://www.hkcert.org/resources/faq) — Distinguishes backups from disaster recovery and links recovery planning to business impact, applications, hardware and data.
4. [NIST · SP 800-34 Rev. 1, May 2010, updated November 2010](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf) — Sections 3.2, 3.5.1 and 4.4 discuss recovery objectives, dependencies, testing and validation; not newly issued guidance.
5. [GitLab · Postmortem of database outage of January 31, 10 February 2017](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/) — Company retrospective describes backup shortcomings and a lengthy recovery using an available snapshot. A historical illustration of recovery complexity, not a claim about current reliability or data loss in code repositories.
