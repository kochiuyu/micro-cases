# One large payment. A predictable monthly reserve?

<!-- legacy-case-id: 434 -->

FIN-37 · Hong Kong · 15–20 minutes · Sinking funds · Future value of an annuity · Contribution timing

![Two adult wholesale-business colleagues compare a blank monthly calendar and reserve worksheet beside a small model packing machine in an office, without numerical answers or bank branding.](../monthly-reserve-later-start-scene.jpg)

## A savings target needs a timeline

A replacement reserve grows through both new contributions and interest already earned. The date of each contribution matters: a payment made just before purchase has no time to grow. A saving target therefore needs a calendar as well as an amount, and a later start cannot be repaired merely by keeping the original monthly transfer.

## Opening decision

Fictional Harbour Supply, a Hong Kong wholesaler, needs HK$120,000 for a replacement packing machine at the end of month 12. That all-in price and purchase date are fixed for this exercise. Existing equipment remains safely serviceable until replacement. There is no loan, refinancing, resale receipt or usable opening reserve.

Starting from zero today, deposit the same amount D at the end of each month, months 1–12 inclusive. At each month-end, interest is credited to the balance already held; then that month’s deposit is added. Purchase occurs immediately after month 12’s deposit. All transfers and withdrawals are available at the stated times.

The fictional reserve earns exactly 0.5% per month on its opening balance. Interest remains in the fund. There are no fees, tax, withdrawal penalties, rate changes or losses in this model. This is a stipulated monthly rate, not an annual rate or an actual bank offer; no investment product is recommended.

For n equal end-of-month deposits at monthly rate i, the final balance is D × [(1 + i)^n − 1]/i. Here i = 0.005. Alternatively update each month: closing balance = opening balance × 1.005 + D. Use full precision internally, then choose a whole-dollar monthly contribution rounded upward.

Up to HK$14,000 is available at each planned month-end after all operating commitments and protected emergency reserves. Unused capacity is not automatically deposited. The objective is the smallest equal whole-dollar monthly transfer that funds at least HK$120,000 on time. No safety, staffing or emergency provision may be reduced.

## Evidence

| Input | Rule |
| --- | --- |
| Purchase target | HK$120,000 at month 12 end |
| Initial deposits | Month ends 1–12 |
| Monthly interest | 0.5% on opening balance |
| Monthly available cash | Up to HK$14,000 |

**Student question:** What equal monthly contribution funds the target with deposits at months 1–12? Compare it with HK$120,000 divided by twelve. Explain which deposit earns eleven months of interest and which earns none.

## Round two

Before any transfer, a cash review establishes that months 1, 2 and 3 have no surplus available for this reserve. The first possible contribution is now at the end of month 4, not today or the start of month 4. Months 4–12 still each allow up to HK$14,000.

The machine still costs HK$120,000 immediately after the end-of-month-12 deposit. Interest and all other assumptions are unchanged. There is no catch-up lump sum or money waiting elsewhere. Recalculate an equal contribution for the remaining dates rather than extending the purchase deadline or assuming earlier deposits occurred.

**Student question:** How many deposits remain, and what revised whole-dollar contribution meets the target? If the original rounded transfer continues on those dates, calculate the final balance and shortfall. Does the revised plan fit the monthly cash limit?

## Debrief · Accumulate each payment

Twelve deposits produce a factor of [(1.005)^12 − 1]/0.005 = 12.33556237. The exact level contribution is HK$120,000/12.33556237 = HK$9,727.971565. Round upward to HK$9,728. Its final balance is approximately HK$120,000.35, so it meets the target without relying on an extra transfer.

The first deposit, at month 1’s end, grows for eleven months; the last grows for zero. The balance is D × [(1.005)^11 + (1.005)^10 + … + 1]. Do not give all twelve deposits twelve months of interest or treat the monthly rate as 0.5% per year.

## Debrief · Compare with simple division

Saving HK$10,000 twelve times would also work, producing approximately HK$123,355.62 under the stipulated return. Dividing the target by twelve ignores interest; it does not find the smallest required transfer here. Conversely, claiming interest will cover a gap without calculating each payment’s exposure to time is not a funding plan.

The HK$9,728 plan transfers HK$116,736 in total and earns about HK$3,264.35 interest. Interest is not a further owner contribution. A transfer to the reserve is an internal movement of cash, not a second machine purchase expense; the final HK$120,000 payment uses the accumulated reserve once.

## Debrief · Count dates after the delay

Months 4 through 12 inclusive provide nine deposits, not eight or twelve. Their accumulation factor is [(1.005)^9 − 1]/0.005 = 9.182115829. The first now earns eight months of interest; the last still earns none. The first three months have a zero balance and earn zero interest.

The revised exact contribution is HK$120,000/9.182115829 = HK$13,068.883276. Round upward to HK$13,069, producing approximately HK$120,001.07. That is HK$3,341 more per contributing month than the original rounded plan, but remains HK$931 below the HK$14,000 monthly limit.

## Debrief · Show the unfunded gap

Keeping HK$9,728 for only nine deposits yields HK$9,728 × 9.182115829 = approximately HK$89,323.62. The shortfall is HK$30,676.38. It exceeds three missed transfers of HK$9,728 because those early transfers would also have earned interest. An unchanged standing instruction does not preserve an unchanged target.

The revised nine transfers total HK$117,621; interest supplies approximately HK$2,380.07. The later start requires more contributed principal and a larger monthly allocation. It does not change the machine price. Using HK$13,000 would still leave about HK$632.49 unfunded, so rounding the requirement downward is not harmless.

## Debrief · Maintain the boundary

Approve the HK$13,069 monthly allocation for months 4–12 within this fictional model, with a check of actual transfers and balances against the calendar. The remaining HK$931 monthly capacity is not required by this target. Do not count it twice or assume a catch-up payment exists outside the specified resources.

Real planning would verify the purchase price, net rate, access conditions and ability to contribute. A variable investment return is not the guaranteed monthly rate assumed here. If those inputs change, recalculate the funding schedule rather than presenting the classroom result as a guaranteed real-world outcome.

## Instructor note

Draw month-ends 1 through 12 and put the purchase immediately after the last deposit. First solve the original schedule; then cross out deposits 1–3. Require students to count nine remaining payments and reconcile contributions plus interest with the target. A basic calculator and the supplied formula are sufficient.

FIN-30 concerns balloon debt and uncommitted refinancing, with a zero-return reserve. This case contains no borrowing: it designs an interest-bearing equipment-replacement fund and tests contribution timing. It is also distinct from FIN-36’s unequal-life equipment comparison: the replacement choice and deadline are fixed here.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All amounts, equipment and cash availability fictional. Target120000 after deposit at month12 end; no opening reserve/borrowing/refinancing/salvage. Monthly rate0.005 on opening balance, interest then deposit, no tax/fees/penalties/losses. Internal full precision, reported balances to cents, equal whole-dollar transfers rounded upward. Initial12 deposits factor12.3355623729, exact9727.97156485, rounded9728 gives120000.350764. Delay removes dates1–3; first month4 end,9payments factor9.18211582901, exact13068.8832764, rounded13069 gives120001.071769. Original9728 on9dates gives89323.622785, shortfall30676.377215. Revised increase3341, available monthly14000 leaves931. 13000 would yield119367.505777. Protected operations/emergency funds unchanged, no separate catch-up source. Sinking fund is not amortisation or double purchase expenditure; no real savings product or guaranteed actual return asserted.

- [OpenStax · Principles of Finance 2e · 8.2 Annuities](https://openstax.org/books/principles-finance-2e/pages/8-2-annuities). Original teaching derives the accumulated value of equal end-period deposits and distinguishes ordinary annuities from beginning-period payments. The case uses its own amounts and monthly timeline.
- [Jean-Paul Olivier · Business Math: A Step-by-Step Handbook · 2021 Revision A · 14.3](https://openlibrary-repo.ecampusontario.ca/jspui/bitstream/123456789/898/2/Olivier-BusinessMath-2021A.pdf). Original textbook explains sinking-fund schedules, accumulating principal and interest, and payment rounding. Its bond examples are not adopted; this fund buys replacement equipment without borrowing.
- [Investor and Financial Education Council · Managing your Money · Saving for the Future](https://www.ifec.org.hk/web/common/pdf/publication/en/ifec-managing-money-booklet-en.pdf). Original educational booklet connects clear saving goals, regular review, a separate savings account and the time available for compounding. Its personal examples and returns are not forecasts for this business.
- [US Consumer Financial Protection Bureau · How does compound interest work?](https://www.consumerfinance.gov/ask-cfpb/how-does-compound-interest-work-en-1683/). Official worked explanation separates principal, rate and compounding frequency and illustrates interest on accumulated interest. No US account rule or product guarantee is applied.
- [ASIC Moneysmart · Compound interest](https://moneysmart.gov.au/saving/compound-interest). Official explanation distinguishes simple from compound interest; its worked monthly example correctly uses a monthly rate and total months. The generic formula labels elsewhere on the page are inconsistent and must not be used. This case supplies its own correctly specified formula.
