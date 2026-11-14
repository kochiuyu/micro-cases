# 97% right. Ready to reply?

Case 26 · Hong Kong · 10–15 minutes · AI oversight · Service automation

![Two customer-support colleagues discuss a chatbot launch beside a laptop, headset and online-retail parcels.](../chatbot-scene.jpg)

## In the news

On 15 October 2026, Hong Kong’s Consumer Council reported a ticket customer who could not obtain a date change or human help after a No. 8 typhoon warning. Before purchase, AI support had indicated that rescheduling might be possible depending on circumstances. The company and customer gave different accounts of the failed handoff; the company changed the date after Council intervention.

This anonymized complaint is not an AI accuracy test and does not establish that the system invented a policy. It raises a practical question: what happens when a customer needs more than a routine answer?

## Opening decision

You manage customer support at a fictional Hong Kong online clothing retailer. A new chatbot is running in shadow mode: it drafts replies, but staff check them before anything reaches customers. A reviewer has assessed 1,000 drafts against the retailer’s policy and actual order records. The headline is 970 correct replies: 97%.

The operations team wants direct automated replies next week to shorten waits. Keeping staff approval for every reply is slower but preserves a check before sending. You can choose a narrower launch instead. No staff reduction is planned; the same team would handle escalations. No unsafe draft has been sent in this pilot, and no future workload saving has yet been measured.

## Evidence

Fictional shadow-mode pilot: 1,000 drafted replies; 970 correct; 30 incorrect; 97% overall correctness. Staff checked all drafts before sending. Reply correctness is not successful resolution. Future question mix and savings are unmeasured.

**Student question:** Would you allow direct replies next week, keep staff approval, or launch only a limited service? Name the evidence you need before choosing the boundary.

## Round two

The reviewer opens the same 1,000-draft audit by task. All 30 incorrect replies came from order amendments and exceptions; routine questions accounted for most of the test. Some drafts said an address change was completed even though the order record still showed the old address. The pilot bot had no permission to change that record.



| Task | Audited | Correct | Correctness |
|---|---:|---:|---:|
| Routine product and delivery-information questions | 950 | 950 | 100% |
| Order amendments and exceptions | 50 | 20 | 40% |
| Total | 1,000 | 970 | 97% |

This is new detail about the original audit, not a new test or a changed bot. The routine group is informational: it makes no order changes or commitments. Staff caught the false completion messages in shadow mode. Whether the bot can reliably route future exceptions to staff has not been tested.

**Student question:** Where would you draw the launch boundary now? Specify what must happen before a customer is told an order has changed, and who takes responsibility when a handoff is needed.

## Debrief · The average hides the boundary

The overall score weights each reply equally. Routine questions make up 95% of this sample, so their strong result dominates. Exception correctness is 20 ÷ 50 = 40%; 30 ÷ 50 = 60% were wrong. The same 30 errors are only 3% of the full sample. A single percentage conceals where the failures occur and what customers might do because of them.

An inaccurate product detail and a false “address changed” message may have very different consequences. Do not attach a made-up loss to all 30 errors: the audit does not tell us how many would cause a misdelivery, a repeat contact or a refund. It also does not establish that humans never make mistakes.

## A narrower launch is still a system

A defensible next step is a bounded, monitored pilot for approved informational questions, while order amendments and uncertain requests stay with staff. Keeping all replies assisted until routing works is also defensible. The routine group’s 950 correct answers are evidence from this sample, not a promise of perfect future performance.

The boundary needs an implementation test: unsupported requests, ambiguous wording and a request for a person must reach a staffed queue. Test mixed conversations too: a routine delivery question may become an address-change request. Do not assume the model’s confident tone means it recognized the right category.

Separate an answer from an action. The bot may say that a request has been passed to staff, but must not say an amendment is complete without a verified successful change in the order system. Give the queue a named owner, carry the conversation context, and show an achievable response time. Urgent amendments need attention before dispatch; after dispatch, staff must explain the remaining options rather than promise a change.

Measure unresolved exceptions, missed dispatch cutoffs, repeat contacts, handoff delay and staff rework alongside reply correctness and speed. Compare with the existing staffed service. Agree a stop rule for false completion messages and a rollback owner before launch. Savings are a hypothesis until the whole workflow, including escalation, works.

## Back to the evidence

The Council’s ticket complaint illustrates a failed route from a conditional automated answer to practical help. RTHK reports the same release, not a second independent experiment. The Council’s earlier e-commerce study also distinguishes operational efficiency from whether consumers find assistance useful; its survey is not a current chatbot accuracy benchmark.

Hong Kong’s privacy regulator recommends risk-proportionate human oversight and accountability in its AI framework. NIST’s generative-AI profile similarly emphasizes context, consequences, realistic evaluation and monitoring. Those are design principles, not proof that this fictional pilot is ready or a legal compensation rule.

## Instructor note

Minutes 0–3: vote using the headline and ask what the score does not show. Minutes 3–7: reveal the task breakdown and calculate 40% and 60%. Minutes 7–12: draw the route from a customer’s amendment request to a verified order change. Assign a person to the queue and identify what the bot may honestly tell the customer.

Challenge “97% is good enough” with error consequences and the sample mix. Challenge “a human handoff solves it” with queue ownership, response time and dispatch cutoffs. If students retain their initial choice, ask what new safeguards or evidence now support it. The case is about system authority and workflow design, not replacing staff or deciding legal refund rights.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The retailer, pilot, task mix, correctness counts, staff arrangements, access restrictions and example false completion messages are fictional classroom assumptions. They are not findings about the ticket platform, any named AI product or the actual incidence of customer harm. 970/1,000 = 97%; 20/50 = 40%; 30/50 = 60%. No real customer records are included. The artwork is fictional.

1. [Hong Kong Consumer Council, customer-service complaints, 15 October 2026](https://www.consumer.org.hk/en/press-release/p-600-customer-service-complaints) — Case 2 describes conditional AI advice and a failed human handoff around event-ticket rescheduling. Parties gave differing accounts. Not a performance benchmark or proof of an invented policy.
2. [RTHK, AI can be problem, not solution in retail services, 15 October 2026](https://news.rthk.hk/rthk/en/component/k2/1874039-20261015.htm?archive_date=2026-10-15) — Reports the same Council announcement and the importance of practical help and alternative human contact. Not independent experimental evidence.
3. [Hong Kong Consumer Council, Fostering Consumer Trust: Ethical Artificial Intelligence in E-commerce, 8 September 2022](https://www.consumer.org.hk/en/press-release/p-ai-in-ecommerce) — Historical consumer survey distinguishes operational efficiency from usefulness and experience. Its measures are not generative-AI answer accuracy.
4. [PCPD, Artificial Intelligence: Model Personal Data Protection Framework, June 2024](https://www.pcpd.org.hk/english/resources_centre/publications/files/ai_protection_framework.pdf) — Section 2.2 supports risk-proportionate human oversight and accountability. Personal-data governance guidance, not a statutory compensation rule.
5. [NIST, Generative Artificial Intelligence Profile, AI 600-1, July 2024](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — Voluntary framework: risk combines likelihood and consequences; MS-2.5-001 and MS-4.2-002 address assessment limits and realistic evaluation; MANAGE 4.1 addresses monitoring and recovery.
