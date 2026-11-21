# Who gets the lending subsidy?

<!-- legacy-case-id: 492 -->

FIN-47 · Singapore · 15 minutes · Two-sided markets · Marketplace lending · Credit screening · Acquisition costs

![Two colleagues in a Singapore office compare separate borrower and lender paths for short-term and longer-term loans.](../who-gets-the-lending-subsidy-scene.jpg)

## Singapore platforms connect small businesses with investors

In a June 2024 explainer, Singapore-based Funding Societies described connecting small businesses with individual and institutional investors. Its March 2025 credit-assessment explainer describes how it reviews borrowers and uses that work to prepare investor fact sheets. The exercise that follows uses a fictional platform and does not represent the provider’s practices or terms.

## Opening decision

Priya runs growth at a fictional Singapore marketplace for small-business loans. She can run one acquisition campaign this month, or neither. The platform earns S$180 per funded loan after routine servicing costs, before any new screening or campaign costs. Already screened applications cost nothing more to process in this exercise.

The marketplace has two separate lending pools: short-term and longer-term. Lenders’ mandates fix which pool they can fund during the month, so spare capacity cannot move between pools. Each qualified firm wants one loan; each available slot can fund one loan in that pool.

The lender campaign draws lapsed lenders back. The borrower campaign recruits 30 longer-term applicants; 16 are forecast to qualify at the existing standard. Screening costs S$30 per new applicant whether or not the applicant qualifies, in addition to the campaign cost. Use the forecast counts as fixed for each round.

## Evidence

| Measure | No campaign | Lender campaign | Borrower campaign |
| --- | --- | --- | --- |
| Qualified short-term firms | 70 | 70 | 70 |
| Short-term lending slots | 45 | 63 | 45 |
| Qualified longer-term firms | 20 | 20 | 36 |
| Longer-term lending slots | 45 | 57 | 45 |
| New applications to screen | 0 | 0 | 30 |
| Campaign cost | S$0 | S$1,250 | S$540 |

**Student question:** Which campaign should Priya choose? Compare funded loans by pool and extra contribution after all new costs against doing nothing.

## Round two

A pilot suggests that only 12 of the 18 extra short-term slots would actually be ready to fund this month. The 12 extra longer-term slots would still be available. The lender campaign’s cost is fixed, and the borrower campaign forecast is unchanged.

For the decision, a slot counts only if the lender is ready to fund within the month. An expression of interest is not a slot.

**Student question:** Which campaign now earns more, and what is the smallest number of extra ready-to-fund short-term slots that would make the lender campaign the better choice?

## Debrief · Find the constraint in each pool

Without a campaign, 45 short-term and 20 longer-term loans are funded: 65 in all. The marketplace has 90 qualified firms and 90 slots, but short-term firms cannot use the 25 unused longer-term slots. The bottleneck is lenders in the short-term pool and qualified firms in the longer-term pool.

## Debrief · Compare extra contribution

The lender campaign funds 63 + 20 = 83 loans, up 18. Its contribution rises by 18 × S$180 − S$1,250 = S$1,990. The borrower campaign funds 45 + 36 = 81 loans, up 16. Screening all 30 new applicants gives 16 × S$180 − 30 × S$30 − S$540 = S$1,440. Both beat doing nothing; recruit lenders on this forecast.

## Debrief · Count slots ready this month

The revised lender campaign funds 57 + 20 = 77 loans, up 12: 12 × S$180 − S$1,250 = S$910. The borrower campaign still adds S$1,440, so Priya should switch. The longer-term slots added by the lender campaign do not change funded volume.

## Debrief · Set a rollout threshold

With 14 extra ready short-term slots the lender campaign adds S$1,270. With 15 it adds S$1,450, just S$10 more than the borrower campaign. Fifteen is the minimum on these assumptions, but that small lead is a reason to verify commitments before spending.

## Instructor note

Allow 15 minutes: 2 to read, 5 to calculate and vote, 4 to update the decision and 4 to debrief. Ask students why total lender capacity and total applicants hid a shortage and what metric they would put on Priya’s dashboard.

Track ready capacity, screened approvals and funded loans separately by pool. Keep the credit standard fixed when comparing the campaigns. If the borrower campaign changes credit quality or contribution per funded loan, the threshold needs to be recalculated; this one-month model does not measure long-run profitability or credit losses.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The people, platform, forecasts, product pools and financial terms in the exercise are fictional. The opening context describes the cited real provider; the model is not a description of its operations or a recommendation to borrow, lend or invest.

- [Funding Societies, What does Funding Societies do?](https://help.fundingsocieties.com/en/articles/760347-what-does-funding-societies-do). The June 2024 provider explainer identifies Singapore small businesses and investor groups served; it does not report the case’s campaign terms.
- [Funding Societies, Our credit assessment explained](https://help.fundingsocieties.com/en/articles/722590-our-credit-assessment-explained). The March 2025 provider explainer describes examples of credit checks and says the platform prepares fact sheets for investors.
- [CGFS and FSB, FinTech credit: Market structure, business models and financial stability implications](https://www.bis.org/publications/cgfs-paper-fintech-credit-market-structure-business-models-and-financial-stability-implications). The joint report describes platforms matching borrowers to investors, alternative balance-sheet models and variation in funding sources.
- [Rochet and Tirole, Platform Competition in Two-Sided Markets](https://www.ugr.es/~scarbo/ROCHETIR.pdf). The original model explains why the allocation of charges across a platform’s two sides can affect activity. It does not estimate this case’s response to a campaign.
- [Iyer, Khwaja, Luttmer and Shue, Screening Peers Softly](https://projects.iq.harvard.edu/files/epod/files/cid_working_paper_no._rwp13-017_khwaja_2013.pdf). The authors’ working paper uses Prosper data to study information in online credit screening. Its US results are not used as assumptions about Singapore firms.
