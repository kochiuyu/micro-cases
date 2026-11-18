# Correct today. Which version decided yesterday?

<!-- legacy-case-id: 440 -->

IS-37 · Singapore · 15–20 minutes · Model version traceability · Inference reproducibility · Minimal decision records

![Two adult analysts in a fictional Singapore subscription-service office compare two abstract version folders linked to a small decision card on a monitor, without readable customer data, credentials or verdict labels.](../current-model-yesterdays-decision-scene.jpg)

## A changing label cannot identify a past release

A model’s current version can work correctly without explaining an earlier recommendation. Technical guidance distinguishes stored model artifacts, execution records and changeable deployment labels. The subscription business, releases, scores and records below are fictional; no live system or personal data is inspected.

## Opening decision

You manage the recommendation workflow for fictional Singapore hobby-reading subscription service PageHarbour. It chooses which optional reading panel appears first: focused craft suggestions or a general catalogue. Subscribers can always open both. Prices, paid access and cancellation rights are unaffected. The task is to explain past panel choices, not decide anyone’s eligibility.

The existing workflow overwrites its production model file when a release changes. It retains each recommendation’s timestamp, output score, panel shown and a small input snapshot, but records only the label “current” for its configuration. Feature definitions and panel thresholds are maintained separately. A retained input does not identify which complete configuration used it.

A keeps that overwrite approach for the next release. B introduces a protected versioned release bundle linking the model artifact, feature definitions, scoring code, runtime dependencies and panel rule. Each decision records the resolved bundle identifier, not only “current”. Both cost quotes are funded, and a two-week implementation window is available without changing subscriber service.

B proposes retaining only the necessary decision-time feature values, timestamp, score, action and protected reference to the relevant support case. Names, billing details, message contents and unrelated reading history are excluded. Access and purpose-limited retention must be agreed before use; a support-case reference is not assumed to make a record anonymous.

## Evidence

| Design | Configuration record | Historical limit |
| --- | --- | --- |
| A | Overwritten file; current label | Past bundle not identified |
| B | Preserved bundle; resolved identifier | Still needs complete inputs and tested replay |

**Student question:** Which design would you choose for explaining historical panel choices? Specify why preserving the input and a label called “current” may be insufficient, and name information the decision record should not collect merely because storage is available.

## Round two

A subscriber asks why the focused panel appeared yesterday. The old record shows score 0.60 and “focused”, plus a decision-time snapshot of four completed craft articles in the preceding seven days and six in the preceding thirty days. The snapshot is unchanged. It does not identify the feature definition, model or panel-rule version actually executed.

The engineering archive contains two candidate release bundles, R1 and R2. R1 defines x as the seven-day count and scores 0.20 + 0.10x. R2 defines x as the thirty-day count and scores 0.10 + 0.08x. For this fixture these formulas are exact and deterministic; the scores are ranking indices, not calibrated probabilities.

R1 shows focused when its score is at least 0.55; R2 uses at least 0.65. Otherwise each shows general. R2 is currently deployed. Both bundles can be replayed in preserved test environments, but the old production log has no reliable link establishing which bundle ran yesterday. Matching an archived output is not that missing deployment link.

Using the stored snapshot with current R2 gives 0.58 and general. The support agent wants to replace yesterday’s recorded result with that answer. No evidence says the old record was fabricated; a different configuration is one possible explanation. The team can report the uncertainty and manually help the subscriber find either panel without changing the old record.

The B implementation includes an independent replay test, protected release storage and a check that each decision resolves its deployment label to a bundle identifier. Logging failure routes the optional display to the general catalogue and raises an operational alert. The fallback is recorded, not presented as a model-scored recommendation. These controls remain proposals until tested.

**Student question:** Calculate each candidate bundle’s score and panel using the stored snapshot. Does R1’s matching output prove it ran yesterday? Design a minimal record and replay check for future decisions, and state how support should describe the unresolved historical result.

## Debrief · Replay the configuration, not the filename

R1 uses x = 4: 0.20 + 0.10 × 4 = 0.60. Since 0.60 is at least 0.55, it selects focused. R2 uses x = 6: 0.10 + 0.08 × 6 = 0.58. Since 0.58 is below 0.65, it selects general.

Applying R2’s threshold to R1’s 0.60 would also produce general, but that mixes releases. Feeding the seven-day count into a model expecting a thirty-day count changes its input meaning. Model version, feature semantics and downstream rule must travel together; recording only the model name leaves important behaviour unspecified.

## Debrief · A matching candidate is not a verified history

R1 reproduces the recorded score and panel under the supplied snapshot. That makes it consistent with the old record, not proven to have been deployed for that request. Another configuration could produce the same output. The missing per-decision release link cannot be recreated just by choosing the archive version that matches.

Current R2’s general panel is a new calculation under current rules. It does not establish that yesterday’s focused panel was an error. Preserve the original record and label any reconstruction separately, with its assumptions. Support can explain the recorded result and the traceability limitation without inventing a historical configuration.

## Debrief · Bind the release and the execution

Choose B. Give each protected bundle an unambiguous identifier and preserve the actual model artifact, feature definitions, scoring implementation, dependency versions and panel rule. Record the identifier resolved at decision time. An alias such as “current” can point somewhere else tomorrow; it is useful for deployment, not sufficient as a historical reference.

Keep a minimal decision record linking that bundle to timestamp and time zone, decision-time feature values, score, displayed panel and any fallback or manual override. Record missing-value and rounding conventions in the bundle. Preserve outputs as evidence of what occurred, while maintaining the information required to test how they were produced.

## Debrief · Test replay, not just storage

An authorised independent colleague should retrieve a recorded bundle and its permitted inputs, run it in the preserved environment and compare score and panel with the saved output. Include threshold-boundary fixtures and a test that changes the deployment alias afterward. The earlier decision must still resolve to its original bundle.

For this deterministic fixture, exact scores and decisions are expected. Other systems may need documented tolerances or random-state controls; do not promise bit-for-bit replay universally. A successful replay establishes reproducibility under the preserved conditions, not that the recommendation is useful, unbiased or factually correct.

## Debrief · Keep traceability proportionate

Preserve decision-time aggregates needed for replay rather than copying whole reading histories, messages or billing records into a debugging archive. Restrict access, protect linkage keys and set a justified retention period with the responsible privacy and service owners. A coded case reference can still link to a person and requires protection.

Do not extend collection or retention without authority simply to make every conceivable future investigation easier. Document what cannot be reconstructed after an approved retention period ends. Training provenance belongs in a separate governed development record; replaying one inference does not automatically require another copy of every training record.

## Instructor note

Minutes 0–4: choose the record design. Minutes 4–8: calculate both releases and the mixed-threshold result. Minutes 8–13: distinguish a matching candidate from known deployment. Minutes 13–18: specify a minimal bundle-linked record, alias-change test and truthful support response.

This is a paper-based technical design exercise. Students neither deploy code nor collect subscriber data. Keep the focus on inference configuration, feature meaning and decision-rule versions rather than a dashboard correction or legal chain of custody. No source mandates a particular vendor, retention duration or current Singapore compliance conclusion.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All business, records and releases fictional. Optional panel order only; both panels always accessible with no pricing or entitlement effect. Old record contains score0.60/focused and frozen aggregate counts4 in7days,6 in30days but lacks bundle identity. Archive R1 gives0.20+0.10*4=0.60 at least 0.55 focused; current R2 gives0.10+0.08*6=0.58 below 0.65 general. Indices are not probabilities. Candidate R1 match is not proof of historical deployment. B preserves bundle and execution linkage, with governed minimal input retention and coded-reference protections, no copied full histories or training records by default. Logging failure produces recorded general-catalogue fallback. No live testing, deployment, data acquisition or policy change is performed.

- [MLflow · ML Model Registry](https://mlflow.org/docs/latest/ml/model-registry/). Official documentation distinguishes specific model versions from mutable aliases. Registry availability alone does not preserve every component or prove which release served a past request.
- [scikit-learn · Model persistence](https://scikit-learn.org/stable/model_persistence.html). Official documentation describes dependency-version limitations and supporting code and metadata. The case distinguishes replaying a preserved inference from rebuilding a trained model.
- [TensorFlow TFX · ML Metadata](https://www.tensorflow.org/tfx/guide/mlmd). Official guidance links artifacts, executions and their inputs and outputs for lineage. This supports connecting a release to a run, not just keeping unrelated files.
- [NIST · AI Risk Management Framework 1.0 · 2023](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf). Primary framework discusses documentation, transparency and privacy-enhancing design. It does not prescribe a legal retention period or certify this fictional workflow.
- [DVC · Experiments Overview](https://doc.dvc.org/user-guide/experiment-management). Official documentation describes versioned experiment state, parameters, models and datasets. A development experiment record is not itself proof of a production deployment or permission to copy personal data.
