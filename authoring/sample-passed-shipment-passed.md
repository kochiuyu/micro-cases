# A sample passed. Did the shipment pass?

<!-- legacy-case-id: 388 -->

OPS-33 · Shenzhen · 15–20 minutes · Acceptance sampling · Precommitted disposition rules · Producer and consumer risk

![Two adult quality colleagues examine printed fabric sleeves beside a plain inspection sheet and measuring tool at a tidy Shenzhen inspection bench.](../sample-passed-shipment-passed-scene.jpg)

## One lot, one defined rule

Quality guidance distinguishes a decision about one delivered lot from monitoring a production process. Acceptance sampling uses a defined sample and decision rule; accepting a lot is not a certificate that every unit conforms. The buyer, supplier, plans and results below are fictional, not a named standard or real inspection record.

## Opening decision

You buy 1,000 printed fabric sleeves for adult desk accessories at fictional Shenzhen retailer Desk Lane. Only cosmetic print alignment is being assessed. Safety, lawful sale and all other product requirements have separately passed their required checks. No medical, electrical, protective or food-contact goods are involved.

A sleeve is nonconforming if its print is displaced by more than 2 mm from the agreed position. Exactly 2 mm conforms. Count affected sleeves, not the number of marks on each sleeve. The nondestructive measurement procedure, trained inspectors and classification accuracy are verified for this exercise.

The buyer and supplier have negotiated two sampling templates for future orders. Each selects 50 different sleeves uniformly at random, without replacement, from the complete identified 1,000-unit lot. Every sleeve is accessible. Neither supplier-picked examples nor convenient top-carton samples qualify. A lot-specific signed instruction must select one template before inspection.

Template S accepts the lot when at most one sampled sleeve is nonconforming; template R accepts at most two. More than the selected limit rejects the lot. Under either template, every known nonconforming sampled sleeve is withheld and replaced with an individually checked conforming sleeve before any accepted lot can ship.

Both templates take the same inspection time and cost. No defect-related loss value or target risk tolerance is supplied. Inspection and any required correction are funded by the supplier under the agreed procedure. The buyer has buffer stock, so holding this lot does not force a missed customer promise.

No goods have been released. Your meeting pack contains both templates but not the signed lot instruction or inspection result. A provisional preference for future orders cannot change this lot’s existing instruction. That record and the complete inspection log will be opened in round two.

## Evidence

| Template | Sample | Accept lot if | Reject lot if |
| --- | --- | --- | --- |
| S | 50 sleeves | 0 or 1 nonconforming | 2 or more |
| R | 50 sleeves | 0, 1 or 2 nonconforming | 3 or more |

**Student question:** Which template would you provisionally prefer for a future comparable order, and what risk trade-off matters? What must you check before deciding this lot’s release? Does either template promise zero nonconforming sleeves in the shipment?

## Round two

The signed lot instruction selected S before sampling. The verified random sample contains two nonconforming sleeves and 48 conforming sleeves. No ambiguity, measurement error or selection failure has been found. The supplier proposes recording R instead because the same sample would then pass. No authorised amendment has been agreed.

Under the signed procedure, rejection means hold this identified lot, not discard every sleeve. The supplier must screen all 1,000 sleeves, correct or replace every detected nonconforming unit, and document the work. The two known failures remain isolated until corrected or replaced. A lot cannot be relabelled to erase its rejection history.

After documented correction, the buyer takes one fresh uniform random sample of 50 from the complete corrected 1,000-unit lot, using S again. Any detected failures are withheld. A second rejection keeps the lot on hold for a separately approved corrective plan; no repeated sampling until a pass is allowed.

For perspective, the next table gives exact sampling probabilities for two hypothetical incoming lots: one contains exactly 20 nonconforming sleeves; the other exactly 100. These are comparison scenarios, not estimates of this lot’s unknown total. Probabilities describe the initial lot decision before any screening, correction or replacement of sampled failures.

| Incoming lot | S: at most 1 | R: at most 2 |
| --- | --- | --- |
| 20 of 1,000 nonconforming | 73.60% | 92.64% |
| 100 of 1,000 nonconforming | 3.08% | 10.56% |

**Student question:** Accept under R, or record rejection under S and follow the correction route? Use the two hypothetical lots to explain the producer–buyer risk trade-off, and state what the observed two failures do and do not establish about the shipment.

## Debrief · Apply the selected rule

Two exceeds S’s acceptance number of one, so record rejection and hold the lot. Two is within R’s limit, but R was not selected for this inspection. A future reviewed change is possible before future results exist. Quietly substituting the passing template now would misstate which procedure this lot satisfied.

Removing only the two observed failures is insufficient after rejection: S requires the documented whole-lot correction route. Reinspection follows a changed, recorded lot, not repeated draws from the unchanged lot. Keep the original selection, sample identities, measurements, disposition and correction history together.

## Debrief · A sample rate is not a census

The observed nonconforming proportion is 2 ÷ 50 = 4%. It does not establish exactly 40 nonconforming sleeves among 1,000. Two failures prove that the original lot was not defect-free, but rejection does not prove every sleeve fails or that its true nonconforming proportion exceeds a particular limit.

Likewise, a sample meeting an acceptance number would not prove every uninspected sleeve conforms. An acceptance number is a sample decision threshold, not permission to ship known failures or a guaranteed maximum defect percentage in every accepted lot. The stated rule and residual uncertainty must both be reported.

## Debrief · Whose risk changes?

At the hypothetical 20-in-1,000 quality level, S rejects 100% − 73.60% = 26.40% of such lots; R rejects 7.36%. If that quality level were agreed acceptable, these illustrate producer’s risk: rejection of a lot at the acceptable reference level. No such acceptable-quality designation is imposed by this case.

At the hypothetical 100-in-1,000 level, S accepts 3.08% of such lots and R accepts 10.56%. If that level were designated unacceptable, these illustrate consumer’s risk: acceptance at the poor reference level. They are not the probability that this inspected lot is poor, nor the chance a particular shipped sleeve fails.

## Debrief · Understand the comparison

With the same random sample size, every outcome accepted by S is also accepted by R. R additionally accepts samples containing exactly two nonconforming sleeves. It therefore reduces rejection at both hypothetical quality levels, helping the producer at the better level while increasing the buyer’s exposure at the poorer level.

The displayed probabilities use sampling without replacement from a finite lot. Students may use the supplied table; no distribution derivation is required. They concern initial acceptance only, not the outgoing quality after screened failures are corrected. The actual lot’s composition and the frequency of different quality levels remain unknown.

## Debrief · Do not redesign from one outcome

For future orders, agree relevant quality reference levels, tolerable risks, inspection effort and correction responsibilities before selecting a plan. Neither template is established as universally optimal or compliant with a named standard. A more permissive threshold does not improve the supplier’s manufacturing quality; it changes which sample outcomes trigger acceptance.

Choosing R only when S would fail cannot be described as S with a harmless administrative adjustment. For the same sample, choosing whichever of these two templates passes produces R’s acceptance rule. It does not preserve S’s buyer protection, and it is not a separate independent confirmation.

## Instructor note

Allow three minutes for the initial preference and missing record, four for the signed-rule reveal, five for the risk table and three for a defensible disposition record. Distinguish nonconforming units, sample proportion, lot disposition and actual outgoing quality. Do not invent a disposal cost, process improvement or posterior probability.

OPS-10 concerns time-ordered process monitoring; OPS-26 reconciles stage yields and rework. This case instead decides one lot’s disposition under a preselected sampling plan. IS-22 examines exploratory experiment selection; here the central task is applying a supplier–buyer acceptance rule with an explicit correction and reinspection route.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All organisations, product details, lot and sample sizes, thresholds, results and procedures are fictional. S and R are teaching templates, not ANSI/ASQ or ISO plans. No safety-critical quality characteristic is sampled in this exercise. Uniform random sampling without replacement and accurate nondestructive classification are stipulated. The probability table uses exact hypergeometric probabilities: for N=1,000, n=50 and K=20 or 100 nonconforming units, sum C(K,d)C(1,000−K,50−d)/C(1,000,50) over d=0 through the acceptance number. Values are rounded to two decimal percentage points. This is initial acceptance, not outgoing quality or a posterior assessment of the actual lot. Known failures cannot ship; rejection and one corrected-lot reinspection follow the supplied procedure. Sources explain concepts, not legal obligations or certification.

- [NIST/SEMATECH, What kinds of Lot Acceptance Sampling Plans are there?](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc22.htm). Defines single-sample decision rules, producer and consumer risk, and rectifying inspection. No standard-plan designation or outgoing-quality formula is applied.
- [ASQ, Attribute and Variable Sampling Plans and Inspection Procedures](https://asq.org/quality-resources/sampling/attributes-variables-sampling). Explains attribute counting and predefined acceptance criteria. The explanatory page, not a purchased standard or its tables, supplies background.
- [Minitab, Data considerations for Attributes Acceptance Sampling](https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/acceptance-sampling/how-to/attributes-acceptance-sampling/before-you-start/data-considerations/). Explains random selection, counted units and exact hypergeometric probabilities for isolated finite lots. No software-generated or standards-certified plan is claimed.
- [FAO/Codex, ALINORM 04/27/23 Appendix III, proposed draft sampling guidelines, 2004](https://www.fao.org/4/j2291e/j2291e04.htm). Historical primary draft, sections 1.1, 1.3 and 2.1.2: sampling limits, agreed plans and recorded procedures. Food-specific provisions and legacy standard references do not govern these sleeves.
- [Christian Walck, Hand-book on Statistical Distributions for Experimentalists, section 21, University of Stockholm](https://staff.fysik.su.se/~walck/suf9601.pdf). Author-hosted university report, last modified 10 September 2007. Section 21 gives the finite-population, without-replacement probability law used for the original case calculations.
