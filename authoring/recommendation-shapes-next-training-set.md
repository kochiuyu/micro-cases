# The recommendation changes demand. What will the next model learn?

<!-- legacy-case-id: 452 -->

IS-38 · Singapore · 15–20 minutes · Recommendation feedback loops · Exposure bias · Bounded exploration

![Two adult bookshop analysts compare a single abstract recommendation card and two plain book covers beside an unlettered exposure log in a Singapore office.](../recommendation-shapes-next-training-set-scene.jpg)

## The system helps create its next dataset

A recommender helps generate the behaviour later used to train it. When only featured items receive measured clicks, unfeatured items have no comparable opportunity to demonstrate interest. Research studies this feedback loop across repeated updates; this fictional bookshop isolates the exposure problem without claiming that all recommendations reduce diversity or customer benefit.

## Opening decision

You manage fictional Singapore online bookshop Lantern Shelf’s optional discovery card. It features one of two adult hobby books, X or Y, in the same page position. Both are suitable, in stock and priced identically. Full catalogue search and purchase access remain unchanged. The card makes no eligibility, payment or sensitive-content decision.

The current rule features whichever title has accumulated more card clicks. X began with a small historical lead, so every eligible visitor now sees X. At each weekly retraining, the pipeline treats all catalogue titles without a recorded card click as rejected examples, including titles not displayed. It then uses those data to retain its click leader.

Last week, one thousand distinct eligible adults each saw one X card; one hundred clicked it during that session. Y was displayed zero times and received zero card clicks. Catalogue searches and purchases are deliberately outside this outcome. The report nevertheless labels Y’s card interest as zero and proposes another week of X-only exposure.

A retains that policy. B proposes a bounded diagnostic allocation: randomly choose eight hundred of the next thousand eligible adults for X and two hundred for Y, one card each. Assignments are made uniformly before outcomes, not from taste profiles. Record the assigned title, actual exposure and whether that card was clicked.

B costs an additional S$500 for setup and analysis within a funded budget. It also gives two hundred featured placements to a less-tested title instead of X. For planning only, if X maintained its observed 10% rate and Y attracted no clicks, those placements would forgo twenty expected clicks. That is a scenario, not a guaranteed loss.

The test has passed the stipulated privacy, accessibility and service checks. Only minimal authorised session records are retained for a defined review period, then aggregated or deleted as required; no reading histories or sensitive profiles are added. Users can ignore the card. Stock, prices, placement, image quality and normal catalogue access remain comparable.

## Evidence

| Title | Displayed | Clicked |
| --- | --- | --- |
| X | 1,000 | 100 |
| Y | 0 | 0 |

**Student question:** Would you retain A or prepare B? Explain what Y’s zero clicks mean when it had zero displays. Trace how the current training rule could reproduce the same exposure pattern next week, and identify the cash and opportunity costs of learning more.

## Round two

A separate, previously authorised diagnostic pilot now reports results from one thousand different eligible adults, not the people in last week’s log. It used B’s fixed random allocation: X appeared eight hundred times and received eighty clicks; Y appeared two hundred times and received thirty clicks. Every assigned card was displayed and its outcome recorded.

Each person contributed one session, there was no interference between people, and no early stopping or selection of extra titles or outcomes. The allocation was independent of potential click responses. These are stipulated experimental conditions. A card click is still only an immediate browsing action, not a purchase, enduring preference or benefit to the reader.

The analyst proposes feeding eighty X clicks and thirty Y clicks into the old total-click ranking, calling X the winner because eighty exceeds thirty. Unshown titles would again be added as negative examples. If that policy is retained, next week again gives Y no exposure even though the diagnostic data finally contain responses to Y.

The team can instead preserve display denominators and known assignment probabilities, separate exposed non-clicks from unexposed items, and plan a documented exposure-aware update. The pilot is diagnostic evidence, not automatic permission for unrestricted deployment or endless exploration. Further spending or changes remain subject to the approved scope and review.

**Student question:** Compute each pilot click rate and the observed difference. Which title does a raw-count rule favour, and why is that comparison misleading? Specify how logging, training and subsequent evaluation should change without declaring Y universally superior or the pilot a measured profit increase.

## Debrief · A missing opportunity is not a rejection

Last week X’s card click rate was 100/1,000 = 10%. Y’s rate was undefined, not 0%: its denominator was zero. A zero card-click count for a title that never occupied the card provides no direct observation of how these visitors would have responded had it been displayed.

The loop is exposure, response, training, then new exposure. The current rule gives X the observations, incorrectly labels unseen Y as rejected, and chooses X again. More weeks of the same policy can increase log volume without supplying the missing comparison. A randomly held-out slice of those same X-only logs still cannot reveal Y’s response.

## Debrief · Compare responses per opportunity

In the diagnostic pilot, X has 80/800 = 10%; Y has 30/200 = 15%. Y’s observed rate is five percentage points higher. Raw counts favour X, eighty to thirty, partly because X had four times as many display opportunities. Neither count alone compares response to a displayed card fairly.

The pilot supports investigating Y and rejects the interpretation that its earlier absence of clicks demonstrated no interest. It does not establish Y as the best choice for every visitor, future week or outcome. Finite-sample uncertainty remains; an analyst should report an interval and a prespecified evaluation before making stronger performance claims.

## Debrief · Preserve how the data were generated

Log eligibility, assignment policy and version, assigned title, actual display, the single click outcome and the review window. For this fixed allocation, each eligible person had an 80% chance of X and a 20% chance of Y. Preserve these design probabilities; do not replace them with the observed click rates.

An exposed non-click is an observed response under that display. An unexposed title has no such response and must not automatically become a negative training label. Keep historical X-only records distinguishable from the randomised pilot. Pooling their counts as though they shared one assignment design would discard the information the pilot was built to supply.

## Debrief · Learn without promising a universal cure

Use exposure-aware training and evaluation appropriate to the documented design, including uncertainty and comparisons on held-out or prospectively collected data with support for both candidate titles. If future recommendations become personalised, simple aggregate click rates are not a complete correction. Account for differing display chances and context rather than treating every logged click as an independent vote.

Probability weighting is not a magic source of missing outcomes. The old policy gave Y zero display probability, so its unobserved response cannot be recovered from those records alone without extra assumptions or information. Positive exploration creates an opportunity to learn within the eligible set; it does not validate every causal model or remove all future feedback effects.

## Debrief · Keep the exploration tradeoff visible

B’s S$500 and two hundred less-certain placements are genuine costs of information. Twenty expected forgone clicks was a planning scenario assuming X’s 10% rate persisted and Y’s rate was zero. The pilot’s thirty Y clicks are not thirty incremental purchases, and cannot be added to revenue or called a proven return on S$500.

Choose B’s learning approach rather than the unsupported zero-interest assumption, while retaining a bounded scope, a stop-and-review point and normal catalogue access. Track exposure coverage and customer experience alongside clicks. Do not expand the experiment indefinitely just because the less-shown title performed promisingly in one cohort.

## Instructor note

IS-11 asks whether voluntary survey respondents represent customers; IS-22 handles selection among many experimental comparisons. Here the deployed rule repeatedly creates its own future training data. Keep two books and one outcome fixed so the central lesson is the exposure–response–retraining loop, not multiple testing or post-hoc segmentation.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All fiction. Single optional card 2 books, full catalogue access retained. Historical X 1000 displays 100 clicks 10%, Y 0 displays 0 clicks undefined rate. Dynamic weekly rule total click leader and unseen negative example creates feedback. Independent preauthorised pilot 1000 unique adults complete uniform allocation 800 X/200 Y, 80/30 clicks=10%/15% observed 5 pp difference; marginal assignment p.8/.2 not click probabilities. No interference/missingness/repeated users/multiplicity/early stopping. Cash S$500 plus 200 less-certain placements. Expected 20 click opportunity loss only if X stable 10% andY 0, not forecast or actual loss. No purchase/profit claim/universal winner. Exposure aware learning requires design and uncertainty; historical zero support not magically corrected. No actual deployment, experiment or personal data access.

- [Chaney, Stewart and Engelhardt · How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility · 2018](https://arxiv.org/html/1710.11214). Original simulation research studies repeated recommendation-driven data collection and cautions about evaluation on similarly confounded logs. Simulation findings are not measured effects at this bookshop.
- [Schnabel and colleagues · Recommendations as Treatments: Debiasing Learning and Evaluation · 2016](https://www.cs.cornell.edu/~adith/docs/MNAR.pdf). Original research develops exposure-probability-aware evaluation and learning, with assumptions and bias–variance tradeoffs. Its estimators are not implemented or certified by this classroom calculation.
- [Krauth, Wang and Jordan · Breaking Feedback Loops in Recommender Systems with Causal Inference · 2022](https://arxiv.org/html/2207.01616). Original research distinguishes multi-step feedback from static missingness and addresses positivity and additional assumptions. The case does not claim a simple click-rate comparison implements its algorithm.
- [Amazon Personalize · Configuring exploration for a domain recommender](https://docs.aws.amazon.com/personalize/latest/dg/create-recommender-configure-exploration.html). Official technical documentation describes bounded exploration of items with little interaction data. Product defaults and exploration settings are not treated as the case’s random-assignment probabilities or a recommended vendor configuration.
- [Netflix Technology Blog · Measuring the Impact of Personalized Recommendations · 10 July 2026](https://netflixtechblog.com/measuring-the-impact-of-personalized-recommendations-4c26be3a4d96). Researchers’ own methodological account separates underlying title appeal from recommendation effects and uses bounded experiments to validate a model. Viewing findings are not imported as bookshop click or sales effects.
