# Within specification. Still the same process?

<!-- legacy-case-id: 112 -->

OPS-10 · Hong Kong · 10–15 minutes · Operations · Process monitoring · Variation

![A supervisor and technician discuss a clipboard beside paper sleeves, a measuring gauge and a safely guarded cutter at a stationery workbench.](../same-process-scene.jpg)

## In the news

On 20 July 2026, HKPC reported a manufacturing showcase including tools intended to integrate production-line data and flag anomalies.

This institutional exhibition report is not proof of effectiveness. Our fictional workshop uses an existing basic chart, not AI.

## Opening decision

Fictional classroom situation. A Hong Kong stationery-finishing workshop cuts decorative paper sleeves for adult notebooks. For this order, acceptable individual widths are 98.0–102.0 mm inclusive. The latest measured sleeve is 100.6 mm, and the current summary records no failed width checks.

Width is a fit characteristic here, not a safety-critical feature. Machine guarding, maintenance, safety obligations and customer release checks remain in force under either response. The summary describes the checks performed, not every unmeasured property.

The supervisor must decide when to examine the process. The time-ordered record and reference chart have not yet been shown; no existing mandatory stop rule is being bypassed.

## Evidence

| Response | What happens now | Resource consequence |
|---|---|---|
| A · Scheduled review | Continue with normal release checks; review the process at the end of the hour. | Keep available production slack. |
| B · Diagnostic pause | Pause for 20 minutes, preserve settings and material, and ask the qualified technician to review measurement, setup and time order. | Use 20 minutes of funded production slack. |

Either schedule can meet today’s delivery. B funds diagnosis, not a guaranteed repair within 20 minutes. No extra worker or quantified prevention benefit is supplied.

**Student question:** Continue normal monitoring for now, or use the 20-minute diagnostic pause? Does “within specification” answer whether the process is behaving as before? Name evidence that could reverse your provisional choice.

## Round two

The technician supplies the last nine readings, taken at equal intervals using the same documented method: 100.2, 100.4, 100.3, 100.5, 100.4, 100.6, 100.5, 100.7 and 100.6 mm.

The centre of 100.0 mm and control limits of 99.0–101.0 mm were established before this job from a substantial reviewed stable baseline of comparable individual measurements. Their validity and measurement resolution are given facts, not calculated from these nine points. The centre is a historical average, not simply the desired target.

The workshop’s preselected warning tests are a point outside the control limits, or nine successive points strictly on the same side of the centre. Either calls for prompt investigation and a proportionate response, not automatic rejection or machine adjustment.

Every point is inside both the product requirement and the control band. All nine are above the centre. The reference values remain fixed for this discussion.

| Reading | Width (mm) |
|---|---:|
| 1 | 100.2 |
| 2 | 100.4 |
| 3 | 100.3 |
| 4 | 100.5 |
| 5 | 100.4 |
| 6 | 100.6 |
| 7 | 100.5 |
| 8 | 100.7 |
| 9 | 100.6 |


**Student question:** Does the chart change your response timing? Which rule signals, what should be checked first, and why would rejecting every sleeve or automatically turning the cutter down be unjustified?

## The product question and process question differ

The measured sleeves satisfy the stipulated 98.0–102.0 mm product requirement. That does not answer whether the recent process behaves like its historical reference.

No point breaches a 99.0 or 101.0 mm control limit. Nevertheless, the supplied nine-on-one-side rule signals at reading nine. The sequence is not continuously increasing: it is a possible shift in location, not a demonstrated upward trend or increased variability.

## Use the available pause for a specific investigation

B is now the supported response under this monitoring plan: there is a defined signal and available diagnostic slack. Preserve the record and settings initially. Have the qualified technician check the gauge and reference, sampling and recording consistency, and recent material or setup changes.

These are questions to investigate, not findings that an operator made an error or a machine broke. Address a confirmed cause and review subsequent output before declaring conditions restored.

## Do not fix the chart by hiding the signal

A signal does not automatically make these nine sleeves defective or identify a setting correction. Required release checks continue. Blindly turning the cutter down could act on the wrong explanation.

Do not recompute the centre or widen limits using these nine readings just to remove the signal. A genuinely changed process may later justify a reviewed new baseline; that is a separate decision supported by evidence.

A false alarm remains possible. The exercise gives no probability of a cause, next defect or avoided financial loss.

## Keep the response bounded, not complacent

The 20-minute allowance is for diagnosis. If findings require longer work, revise the production and delivery plan rather than promising that the pause has solved everything.

Simply continuing because every item passes ignores the supplied rule. A different continuation plan would need a prompt, workable investigation and justified containment; no free parallel technician has been provided.

This one chart does not certify a whole process or prove capability against every requirement. Timing, measurement suitability and other characteristics still matter in real monitoring.

## Instructor note

Ask for the provisional vote before the time record. Then ask students to distinguish three references: product specification, historical centre and control limits. All nine readings pass the first and lie inside the third, yet meet the preselected same-side rule.

The exact nine-point convention is supplied in this case. NIST and ASQ examples use an eight-point rule; do not attribute nine to them. Do not derive new limits from nine observations or teach a posterior certainty from 1/2 raised to a power.

The original chart is a teaching aid, not copied source artwork. A full monitoring design would also assess measurement, dependence, dispersion and sampling. This is an educational response-timing decision, not machine-operation instructions or statistical certification.

## Sources and case assumptions · optional reference

All information needed for the classroom decisions is provided above. Sources are optional reading.

The workshop, measurements, requirements and plan are fictional. Width is a non-safety-critical fit characteristic; guarding, maintenance, required safety and release checks remain. Both initial schedules fit delivery, but a diagnostic allowance is not guaranteed repair time. Nine equally spaced individual readings use a documented method. The historical centre 100.0 mm and limits 99.0–101.0 mm come from a previously reviewed stable comparable baseline; validity and resolution are stipulated, not estimated here. Product specification is separately 98.0–102.0 mm inclusive. The nine-point same-side warning rule was chosen beforehand. All nine points are above 100.0, minimum 100.2 and maximum 100.7; all lie within both bands. This is not a continuously rising sequence or established variability increase. No cause, defect forecast, probability, ROI or capability conclusion follows. NIST/ASQ eight-point examples are not misrepresented as the case’s nine-point convention; Minitab documents that separate convention. Sources checked 15 November 2026 during research and independent review; relevant substantive bodies, not five experimental validations. Original chart and numbers, no source figures copied.

- [HKPC · WAIC 2026 manufacturing showcase · 20 July 2026](https://www.hkpc.org/en/about-us/media-centre/press-releases/2026/hkpc-waic-2026-ai-adaption-in-manufacturing). Institutional exhibition report, not audited effectiveness or evidence about this workshop. No AI requirement inferred.
- [NIST/SEMATECH · What are Variables Control Charts?](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm). Control versus specification, reference reliability and run-rule cautions. Its eight-point example is not the supplied nine-point convention.
- [ASQ · Control Chart](https://asq.org/quality-resources/control-chart). Time order and investigation of unusual patterns. Its run-rule example uses eight points; no source charts or complete-system certification imported.
- [Scott Leavengood and James E. Reeb · Statistical Process Control, Part 2 · Oregon State University Extension, revised July 2015](https://extension.oregonstate.edu/sites/extd8/files/documents/em8733.pdf). Relevant variation, measurement and specification/control sections. No wood-product examples, equations or performance claims transferred.
- [Minitab · All statistics and graphs for Individuals Chart](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/control-charts/how-to/variables-charts-for-individuals/individuals-chart/interpret-the-results/all-statistics-and-graphs/). Test 2 documents nine points on one side; centre and limits differ from targets and specifications. Provider interpretation guidance, not product endorsement or validation of these readings.
