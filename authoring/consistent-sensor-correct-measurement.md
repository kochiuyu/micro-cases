# The sensor is consistent. Is it measuring correctly?

<!-- legacy-case-id: 320 -->

IS-27 · Hong Kong · 15–20 minutes · Measurement precision · Systematic error · Calibration

![A facilities analyst compares a desk temperature sensor and reference instrument in an ordinary exhibition room.](../consistent-sensor-correct-measurement-scene.jpg)

## Repeatability is not the same as accuracy

Metrology guidance distinguishes agreement among repeated readings from agreement with an appropriate reference. Calibration establishes a measurement relationship under specified conditions; it is not automatically a physical adjustment. This case uses invented data from a noncritical monitoring task.

## Opening decision

A fictional Hong Kong exhibition office uses a desk temperature sensor for an internal, descriptive room-monitoring dashboard. It does not control ventilation, protect sensitive objects, trigger alarms or support safety, medical, employment or contractual decisions. Building controls and required inspections use separate approved systems. The analyst wants the dashboard to describe the temperature at the sensor location rather than the whole building.

Five successive readings taken after equilibration under the same stable conditions are 24.9, 25.0, 25.1, 25.0 and 25.0 degrees Celsius. The mean is 25.0 and the maximum minus minimum is 0.2 degrees. The display is steady. There is no current reference comparison in the meeting pack and no evidence that a recent instrument check covers this installation.

The analyst has one HK$1,500 noncritical monitoring allowance. A spends it on collecting and reviewing one hundred additional readings under the same conditions, then reports their average. B spends it on a qualified calibration service against a suitable reference across the intended operating range, documenting uncertainty and assessing any correction. Each uses the full allowance, including paid work; they cannot do both this cycle. Routine dashboard collection continues under either choice, but the analyst can label its accuracy unverified pending the work. There is no urgent decision requiring an unverified absolute temperature.

## Evidence

Five readings (degrees Celsius): 24.9, 25.0, 25.1, 25.0, 25.0. Mean 25.0; range 0.2. A funds one hundred additional readings and their review; B funds reference calibration across the intended range and correction assessment. Each costs HK$1,500 including paid work.

**Student question:** Would you spend the allowance on more readings or reference calibration? Explain what the five readings establish and what they cannot establish about the temperature.

## Round two

An existing preliminary check is brought to the meeting. It was completed during prior routine work and did not consume the proposed allowance. A qualified technician compared the sensor with a currently calibrated reference at three stable conditions spanning the intended range. Both sampled the same air region after sufficient settling; checks found no relevant location gradient or response-time mismatch. The reference values and uncertainty are suitable for this noncritical purpose.

At reference values of 20.0, 23.0 and 26.0 degrees Celsius, the sensor’s five-reading means were respectively 22.0, 25.0 and 28.0 degrees. Within each set, the sensor’s maximum-minus-minimum range was no more than 0.2 degrees. The technician reports expanded uncertainty of 0.15 degrees for each mean difference in this comparison, using coverage factor 2. This is supplied comparison uncertainty, not something students must calculate from the range. The central five readings were the ones shown initially.

The difference is consistently positive at the checked points. The technician has not yet established long-term stability or issued a validated correction for routine use. B remains available to complete that work within the funded service scope, documenting the applicable range and conditions and verification after any adjustment. A would still average more readings from the same uncorrected sensor. The task remains noncritical, and no one has changed the dashboard or equipment.

**Student question:** Which use of the allowance is now justified? Calculate the observed mean differences and a provisional corrected value for the original mean, then state what must be checked before applying that correction routinely.

## Answer the first question: two kinds of evidence

B is the stronger provisional choice for an absolute-temperature dashboard with no relevant current reference check. The initial readings show close repeatability under the specified short-term conditions; they do not establish agreement with the temperature being measured. A could be valuable if reference agreement had already been established and random variation were the unresolved problem. Collecting more observations is not intrinsically superior to checking what the instrument measures.

## Answer the second question: a stable offset

The three observed mean differences, sensor minus reference, are 22.0 − 20.0 = +2.0, 25.0 − 23.0 = +2.0 and 28.0 − 26.0 = +2.0 degrees Celsius. Each is large compared with the supplied 0.15-degree expanded comparison uncertainty. This supports investigating a stable positive offset over the checked conditions. A provisional additive correction is therefore minus 2.0 degrees, giving 25.0 − 2.0 = 23.0 degrees for the initial mean. That is a corrected estimate, not an exact true temperature or a validated permanent rule.

## More of the same does not remove the offset

If the sensor continues to read roughly two degrees high, more readings can produce a more stable estimate of that high mean without removing the bias. Averaging can reduce a random component under suitable assumptions, but closely spaced sensor readings may be correlated, so one hundred readings do not automatically yield the precision gain expected from independent observations. The observed 0.2-degree range is not the full uncertainty of the temperature result.

## Complete the measurement relationship

Use B to document reference traceability and uncertainty, repeatability, conditions, range and evidence of drift. Verify a proposed correction on fresh checks, including more than one operating point; do not extrapolate beyond the validated range or infer permanence from three means. Calibration describes the relation; applying a software correction or physically adjusting the sensor is a distinct action requiring an appropriate documented procedure and verification. Keep raw readings and correction versions so old and new data are not silently mixed.

## A dashboard needs a maintenance rule

Until verification, label absolute readings unverified rather than claim that a smooth line is accurate. After approval, state the correction’s valid conditions and uncertainty and schedule checks appropriate to observed stability and the monitoring purpose. Investigate a changed discrepancy rather than repeatedly subtracting the old offset. The reference is not perfectly error-free; the supplied comparison uncertainty is why its quality and the measurement setup matter.

## Instructor note

This is a measurement-process problem before analysis, not missing-data imputation or choosing a forecasting loss function. All figures, budgets and technician findings are fictional. The central set has mean 25.0 and range 0.2; no standard-deviation or confidence calculation is required. The reference comparison is a preliminary supplied observation, not the unchosen paid calibration already being completed. Do not treat three matching offsets as proof of linearity everywhere or confuse precision, accuracy and uncertainty. Both choices preserve separate safety systems.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All office, instrument, cost and numerical details are original fiction for noncritical descriptive monitoring. No control, safety, medical, conservation, employment or contractual action uses this sensor. Five readings total 125.0 degrees Celsius, mean 25.0, range 0.2. Three sensor-minus-reference means each equal +2.0 degrees. Supplied expanded comparison uncertainty is 0.15 degrees with coverage factor 2, not derived from sample range. Provisional correction −2.0 gives 23.0 for the initial mean, without implying zero uncertainty or long-term validation. Preliminary checks used prior routine capacity, not the unspent HK$1,500 allowance. Calibration and adjustment are distinct. NIST handbook pages are related technical guidance, not independent empirical studies.

- [NIST/SEMATECH handbook: Bias and Accuracy](https://www.itl.nist.gov/div898/handbook/mpc/section1/mpc113.htm). Explains agreement with a reference and identification or reduction of bias; calibrated equipment alone does not eliminate all setup effects.
- [JCGM International Vocabulary of Metrology: Measurement precision](https://jcgm.bipm.org/vim/en/2.15.html). Defines repeat-measurement agreement under specified conditions and warns against equating precision with accuracy.
- [JCGM International Vocabulary of Metrology: Calibration](https://jcgm.bipm.org/vim/en/2.39.html). Defines the calibration relationship with uncertainty and distinguishes calibration, adjustment and verification.
- [NIST/SEMATECH handbook: What can go wrong with calibration](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Discusses poor precision, changing instrument response and the need to monitor stability rather than assume a calibration remains valid.
- [NIST/SEMATECH handbook: Approach to uncertainty analysis](https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc52.htm). Explains that uncertainty depends on measurement configuration, repeatability, time effects and random and systematic contributions.
- [NIST Technical Note 1297, Appendix D1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Clarifies accuracy, repeatability, systematic error and the distinction between an error estimate and measurement uncertainty.
