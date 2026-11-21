# Fewer complaints. Or fewer labels?

<!-- legacy-case-id: 555 -->

IS-46 · Hong Kong · 15 minutes · Text classification · Confusion matrix · Aggregate bias · Human review

![Two reviewers compare coloured complaint coding cards and worksheets at a round table.](../fewer-complaints-or-fewer-labels-scene.jpg)

## Complaint counts depend on a consistent classification

Hong Kong’s Consumer Council says its 2026 revision of complaint categories was applied to the earlier years shown in its table. That makes the definition behind the count visible. This exercise uses independent fictional ticket data and makes no claim that the Council uses automated labelling.

## Opening decision

At a fictional Hong Kong online retailer, Yat prepares an internal dashboard on delivery-delay complaints. For this exercise each of 200 ticket records belongs to one of two categories: delivery delay or other. Trained reviewers independently reconciled the reference labels. There are exactly 60 delay and 140 other tickets in this pilot.

The dashboard team compares model labels with the reviewed reference. Require a reported delay share within 3 percentage points of the reference share and recall of at least 85% of reference delay tickets. Recall is the fraction of real delay tickets labelled delay. Every ticket is counted exactly once.

Pipeline L labels each complaint based on a short text summary. Pipeline S instead extracts a structured reason with the same two possible labels. Neither tool identifies a person, closes a complaint or changes the handling of individual cases.

## Evidence

| Initial pipeline L | Called delay | Called other |
| --- | --- | --- |
| Reference delay: 60 | 45 | 15 |
| Reference other: 140 | 15 | 125 |

**Student question:** What delay share would L report, and what delay recall did it achieve? Does a correct headline qualify L for this dashboard?

## Round two

A new 200-ticket validation replay contains 60 tallied delay and 140 other tickets. L captures 36 of the 60 delays and wrongly labels 12 of the 140 others as delay. S captures 54 of the 60 and wrongly labels 14 of the others as delay. Apply the same two gates.

A pre-set uncertainty flag sends exactly nine of S’s tickets for review, within the ten-ticket capacity. In this replay the reviewers found and corrected eight false positives and one false negative among those nine. The reviewers did not know the reference answers in advance; for this hypothetical check, their corrections agree with the reference.

**Student question:** Do L, S, or S plus review pass both gates on the new replay? Calculate each reported share and recall, and say what the team should still check before using the workflow.

## Debrief · The right total can hide two errors

L initially counts 45 + 15 = 60 predicted delays, or 30%, matching the true share of 30%. Its 15 missed delays cancel its 15 incorrect inclusions in the headline. Recall is 45/60 = 75%, below 85%, so L fails.

## Debrief · Both unreviewed versions miss a gate

On the new replay L counts 36 + 12 = 48 delays, or 24%, with 60% recall. It fails both tests. S counts 54 + 14 = 68, or 34%, with 90% recall. S passes recall but misses the allowed share by 4 percentage points.

## Debrief · Trace the corrections

Review takes away eight labels that should not count as delay and adds a missed delay: 68 − 8 + 1 = 61, or 30.5%. It improves delay recall to 55/60, about 91.7%. S plus review is the only workflow meeting both gates on this replay, with nine reviews against capacity ten.

## Debrief · Pass the replay, not every future month

Approve a controlled follow-up, not unattended reporting. Predefine the categories, retain the reference review process, and check both error directions by intake channel and reporting period. Track review load and disclose missing or uncertain coverage if the inputs change.

## Instructor note

Use four minutes for the first table, six for the retry and five for a release recommendation. Ask why a team should report the denominator and not infer fewer complaints from fewer assigned labels. The review queue was pre-defined and independent in this case; the measured improvement is not a general promise.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All retailer tickets, counts, thresholds, workflow outcomes and people are fictional. Reviewers work on synthetic records and use no real customer information. No public dataset is used for the example calculations.

- [Hong Kong Consumer Council, Complaint Figures](https://www.consumer.org.hk/en/complaints-and-services/complaint-figures). Notes its 2026 category revision and reclassification of the three years displayed.
- [Hong Kong Consumer Council, Customer service complaints report](https://www.consumer.org.hk/en/press-release/p-600-customer-service-complaints). Illustrates descriptions of complaint themes and the distinction between case counts and issue types.
- [Google Machine Learning Crash Course, Classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall). Defines recall and describes why a single performance summary can miss important errors.
- [scikit-learn, Confusion matrix documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix). Defines a true-versus-predicted count table; the classroom solution requires no software.
- [Hong Kong Consumer Council, 2025 complaint review](https://www.consumer.org.hk/en/press-release/p-2025-year-ender). The Council reports a dated breakdown of actual complaint counts; no figures are imported into the case.
