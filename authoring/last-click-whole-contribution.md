# The last click. The whole contribution?

<!-- legacy-case-id: 255 -->

MKT-22 · Hong Kong · 10–15 minutes · Multi-touch attribution · Incrementality · Randomised holdout

![Two fictional adult marketing colleagues compare unlabelled campaign cards beside a plain laptop and ceramic plant pot in a small homeware shop office.](../last-click-whole-contribution-scene.jpg)

## Credit and causation answer different questions

Google’s Analytics documentation describes attribution as assigning credit along a customer’s recorded path. Its separate Conversion Lift documentation distinguishes attributed conversions from additional conversions estimated through a controlled comparison. These are different measurement tasks, not interchangeable labels.

The shop, dashboard rules and test results below are original fiction, not a Google campaign. The equal-split rule is a manual classroom convention, not a claim about which models any platform currently offers.

## Opening decision

**Fictional classroom situation.** You manage campaign reporting for a Hong Kong online homeware shop. Discovery ads introduce its plant pots, paid search helps interested shoppers find the offer, and reminder ads can reach eligible previous visitors. All ads use accurate claims and the same prices; no discount changes are involved. Existing lawful consent, data minimisation and access controls are already in place. No new tracking or personal profiles are proposed.

The monthly dashboard must divide exactly **100 conversion credits** across these three channels for 100 distinct, completed, non-returned orders. One order creates one credit, even if it contains several clicks. Credits are reporting units, not money, staff commission, advertising spend or measured causal contributions. All orders have the same value for this exercise.

**Last touch** gives all credit to the final recorded channel. It is simple and reproducible. **Equal split** divides one order’s credit equally among its recorded channels; it recognises earlier contacts without estimating their influence. Each channel appears at most once in each supplied path. These are complete recorded click paths within the agreed reporting window, not a complete account of every influence on a buyer.

The reminder manager sees many final clicks and proposes expanding reminders next month. You must choose a clearly labelled dashboard convention and explain its limits before anyone treats it as a spending instruction. No additional budget has been committed.

## Evidence

| Recorded click path · earliest to latest | Kept orders |
|---|---:|
| Discovery ad → Reminder ad | 40 |
| Search ad → Reminder ad | 20 |
| Discovery ad → Search ad | 20 |
| Search ad only | 20 |
| Total distinct orders | 100 |

**Student question:** Which reporting convention would you use for this dashboard, last touch or equal split? Allocate the 100 conversion credits across the three channels and explain what your choice can and cannot establish about additional sales.

## Round two

A separate, completed follow-up experiment now becomes available. Its 20,000 eligible adult visitors are a **different cohort and period** from the 100-order path worksheet. Before any reminder delivery, the shop randomly assigned 10,000 to a reminder-eligible policy and 10,000 to a holdout that received no reminder ads. Some eligible adults never received or clicked a reminder; all assigned adults remain in the analysis. Compare assignment groups, not only people who clicked.

Prices, product availability, service, and discovery/search campaign policies were identical across groups; actual search behaviour could still change in response to reminders. Assignment was implemented correctly; no cross-group reminder exposure or spillover is assumed. The same complete order measurement covered both groups across all routes to this shop, including direct visits. The prespecified 14-day window is finished; every counted purchaser made exactly one kept order, with returns already settled. No later effects are claimed.

| Completed follow-up test | Reminder eligible | Reminder held out |
| --- | --- | --- |
| Adults randomly assigned | 10,000 | 10,000 |
| Adults with one kept order | 1,200 | 1,000 |
| Purchase rate | 12% | 10% |

The analyst supplies a rounded **95% confidence interval of +1.13 to +2.87 percentage points** for the difference in purchase rates, using the stated independent-group approximation. This interval describes sampling uncertainty under the test assumptions, not a guaranteed range for future campaigns. No channel costs, order contribution margins, scale-response estimates or comparison experiments for discovery/search are supplied.

The decision is whether to endorse the proposed expansion now, defer it pending economics and scale evidence, or recommend a bounded next test for agreement. Existing commitments remain honoured. The experiment is already complete; students are not being asked to contact customers, alter privacy settings or run an unapproved campaign.

**Student question:** How would you revise the dashboard and the recommendation to expand reminders after the holdout result? Calculate the incremental purchase estimate and keep it separate from attribution credit, uncertainty and the untested effects of the other channels.

## One set of orders, two credit ledgers

| Channel | Last touch | Equal split |
| --- | --- | --- |
| Discovery | 0 | 30 |
| Search | 40 | 40 |
| Reminder | 60 | 30 |
| Total conversion credits | 100 | 100 |

Last touch assigns the first two path rows to reminders: 40 + 20 = 60. Search receives the remaining 20 + 20 = 40. Under equal split, discovery gets 20 from the first row and 10 from the third: 30. Search gets 10 from the second, 10 from the third and 20 from the single-channel path: 40. Reminders get 20 + 10 = 30.

Both ledgers total 100. No order has appeared or disappeared. Last touch emphasises the recorded finishing contact; equal split makes earlier contacts visible. Either can be retained transparently for descriptive reporting, with a side-by-side comparison useful here. Neither allocation estimates what would have happened without a channel.

## A path is not the missing alternative

A shopper may already intend to buy before a reminder appears. Another may buy only because of it. Their observed click sequences alone do not reveal which is which. Splitting a credit more evenly does not solve that missing-alternative problem. Conversely, zero last-touch credit does not prove discovery ads have no effect, and an ad need not be clicked to have an effect.

The simple rules here must not be confused with every advanced attribution system. Some models use experimental information. Our evidence is deliberately narrower: this path table and these two fixed bookkeeping conventions do not identify causal channel shares.

## Use all assigned people

The eligible group’s purchase rate is 1,200 ÷ 10,000 = 12%; the holdout’s is 1,000 ÷ 10,000 = 10%. The estimated effect of the reminder-eligible policy is **2 percentage points**. Applied to a group of 10,000, this is **200 additional purchasers/orders** relative to the estimated no-reminder baseline of 1,000.

Relative lift is 2 ÷ 10 = 20%, not 2%. These different percentages have different denominators. The estimate is for the policy of making reminders available under the tested delivery system, not for forcing everyone to see or click an ad. Restricting the comparison to clickers would break the randomised comparison.

## Do not turn an estimate into a list of people

The 1,000 holdout purchases show that purchases occur without reminder ads. They estimate a baseline for the eligible group; they are not the same identified people as 1,000 of its 1,200 buyers. We cannot name the 200 incremental individuals or prove that every other buyer was unaffected.

The supplied interval corresponds to approximately **113 to 287 additional orders per 10,000 assigned adults**. Report the estimate and uncertainty together. The result supports a positive effect in this completed test under its assumptions. It is not a promise of exactly 200 orders next month.

## Keep the dashboard in two panels

Panel one: historical path attribution, 100 orders, with the chosen rule and reporting window. Show reminders receiving 60 last-touch credits or 30 equal-split credits. Panel two: the separate randomised test, 12% versus 10%, estimated +200 orders per 10,000 with the supplied uncertainty range.

Do not subtract 200 from 60, multiply the historical 60 credits by the test’s lift, or redistribute the 200 as causal shares among discovery, search and reminders. The datasets have different periods and cohorts. The test changes only reminder eligibility while the other campaign policies remain available; it does not identify their separate effects or the value of removing all advertising.

## A positive lift is not an automatic expansion

Recommend acknowledging the positive tested lift but withholding an unconditional expansion recommendation. Contribution per additional kept order, incremental campaign and operating costs, and the response to a different spending level are missing. Revenue credit alone does not establish profit or an optimal media mix.

A bounded follow-up can be proposed once costs, consent scope, sample size, success criteria and stopping rules are agreed. Retaining current committed activity while gathering that evidence can also be reasonable. Do not move all reminder credit to search, declare reminders useless, or infer the return on discovery from a test that did not vary it.

## Instructor note

Use three minutes for the path ledger, two for explaining why allocation is not causation, four for the holdout and three for the dashboard recommendation. Keep the test hidden until the first decision. Ask students to label the denominator for each percentage and to explain why all 10,000 assigned adults remain in each arm.

The normal-approximation interval is supplied so introductory classes need not calculate standard errors. For an extension, compute 0.02 ± 1.96 × sqrt[(0.12 × 0.88 + 0.10 × 0.90) ÷ 10,000], giving approximately 0.01133 to 0.02867. Fixed equal group sizes make the raw 200-order difference align with the rate effect scaled to 10,000; unequal groups require rate normalisation.

Unlike MKT-02, the primary task is not a coupon contribution decision. Unlike MKT-21, credits do not pay staff or allocate a commission pot. This case compares attribution ledgers with a separately identified policy effect. Do not generalise the historical studies’ effects to this shop, or treat a positive test result as a universal rule that all ads work.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All shop paths, test counts, policies and interval are original hypothetical teaching data. No real customer data, actual experiment or platform account is used. Manual equal-split attribution is not described as a current platform option. The experiment measures an intent-to-treat policy effect in its eligible population, preserving all assigned users. Independent groups and no interference are stipulated. Costs, margins and scale response are not supplied, so no ROI or automatic budget optimum can be computed. Five source documents include two complementary official Google pages and three original research papers; they are not five independent replications of the fictional effect.

- [Google Analytics Help · Get started with attribution](https://support.google.com/analytics/answer/10596866?hl=en). Official definition and distinctions between attribution models. Its advanced discussion includes experimental training signals; the case therefore does not claim all attribution methods are merely arbitrary rules.
- [Google Ads Help · Understand your Conversion Lift based on users measurement data](https://support.google.com/google-ads/answer/14102450?hl=en). Official separation of attributed and incremental conversions, relative lift, and uncertainty. Classroom study is not a Google product implementation and does not use its delayed-conversion modelling.
- [Gordon, Zettelmeyer, Bhargava and Chapsky · A Comparison of Approaches to Advertising Measurement, author manuscript dated 12 April 2018](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf). Original comparison of observational methods and randomised experiments; read implementation, assignment-versus-exposure discussion and conclusion. Findings are limited to its studies and data, not a universal impossibility claim.
- [Blake, Nosko and Tadelis · Consumer Heterogeneity and Paid Search Effectiveness, author manuscript dated 8 April 2014](https://faculty.haas.berkeley.edu/stadelis/tadelis.pdf). Original eBay field research illustrating selection and substitution between paid and organic routes. No claim that all search advertising has zero value or that this shop reproduces those results.
- [Lewis and Reiley · Online Ads and Offline Sales, author-hosted manuscript](https://www.davidreiley.com/papers/OnlineAdsOfflineSales.pdf). Original retailer experiment showing why click-only and online-only measurement can miss effects, and why precision matters. Author-hosted manuscript, not a claim to reproduce its estimates or customer-matching practice.
