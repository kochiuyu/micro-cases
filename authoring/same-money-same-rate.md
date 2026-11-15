# Rising cash flows. The same discount rate?

<!-- legacy-case-id: 158 -->

FIN-14 · Hong Kong · 10–15 minutes · Investment appraisal · Inflation consistency · Real and nominal values

![Two packaging-workshop colleagues compare proposal sheets beside a small cutting-machine model and cardboard samples.](../same-money-same-rate-scene.jpg)

## A Hong Kong price-data context

On 22 October 2026, Hong Kong’s Census and Statistics Department released September consumer-price figures. A price index measures a particular basket over a particular period; it is not automatically a forecast for an equipment project.

The workshop, cash flows and inflation rate below are invented teaching assumptions, not the government’s forecast.

## Opening decision

Fictional classroom situation. A Hong Kong packaging workshop is considering a small cutting machine costing HK$110,000 today, including installation. It would operate for three years. Two spreadsheets describe the same project but give opposite signs for its net present value, or NPV: the value today of future net cash flows, less today’s outlay.

Sheet A calls its cash flows “today’s purchasing power”: HK$42,000 at each year-end. Sheet B calls them “future money”: HK$43,680, HK$45,427.20 and HK$47,244.288. Both sheets discount at 9.2% a year. A reports NPV of about −HK$4,063; B reports about +HK$4,376. These are not different machines or operating plans.

Funds are available without reducing protected reserves, no order has been placed, and there is time to reconcile the sheets. The owner asks which recommendation is ready to use. A negative NPV would fail this financial screen; a positive one would support further consideration, not compel a purchase.

## Evidence

| Year-end net cash flow · HK$ | A: today’s purchasing power | B: future money |
|---|---:|---:|
| 1 | 42,000 | 43,680 |
| 2 | 42,000 | 45,427.20 |
| 3 | 42,000 | 47,244.288 |
| Rate used by each sheet | 9.2% | 9.2% |
| Reported NPV, rounded | −4,063 | +4,376 |

**Student question:** Would you use either spreadsheet to recommend the machine now, or hold the recommendation for a consistency check? Identify the missing definition that matters more than which NPV looks attractive.

## Round two

The project modeller confirms a simplified common inflation assumption of 4% a year. Every component of the net operating cash flow rises at that same rate, so HK$42,000 in today’s purchasing power becomes 42,000 × 1.04 to the power of the year in future money. There is no change in physical output or real operating surplus.

The supplied matched discount rates for the same project risk are 5% real and 9.2% nominal: 1.05 × 1.04 = 1.092. These are appraisal assumptions, not loan quotes or recommendations for other businesses. Sheet A used the nominal rate against real cash flows. Sheet B paired nominal cash flows with the nominal rate.

All cash flows occur at year-end; today is year zero. The initial HK$110,000 is already today’s money. The stated flows include all incremental operating costs. For this teaching model there are no tax cash flows, working-capital changes, financing flows, terminal proceeds or other omitted project cash flows. Forecasts and rates are held fixed for the comparison.

**Student question:** Repair the inconsistent sheet. What NPV should the two consistent methods produce, and how would you explain why rising future-money receipts do not create extra real value by themselves?

## Match the cash-flow units to the rate

Real cash flows express purchasing power at today’s prices; nominal cash flows express the money expected at each future date. Discount the first with the supplied 5% real rate and the second with the supplied 9.2% nominal rate. A shared percentage is not automatically a fair comparison when the cash-flow units differ.

## Reconcile the same project

Corrected A: 42,000 ÷ 1.05 + 42,000 ÷ 1.05² + 42,000 ÷ 1.05³ − 110,000 = HK$4,376.42, rounded. B: 43,680 ÷ 1.092 + 45,427.20 ÷ 1.092² + 47,244.288 ÷ 1.092³ − 110,000 gives the same result.

Each nominal cash flow contains a factor of 1.04 for every year. The matched nominal discount factor contains the same inflation factor alongside 1.05. They cancel. The old −HK$4,063.44 was a unit mismatch, not a more cautious view of the same properly stated assumptions.

## A conversion is not a better business

The model produces positive NPV of about HK$4,376 under either consistent method. It does not prove that the cash flows will occur or that the machine is the best use of funds. Check demand, capacity, costs and competing opportunities before a real investment.

If sales prices and costs rise at different rates, do not inflate a net total blindly. Forecast those components, then convert them consistently using a common general-price basis. Nor should a household CPI observation be inserted as the project’s future inflation assumption without justification.

## Instructor note

Ask for the missing rate definition before arithmetic. Either real or nominal presentation can be the final report; keeping an inconsistent sheet is not a legitimate alternative after the reveal. Have students label each column and rate, then explain the cancellation in words.

Use the exact matched relation: (1 + nominal rate) = (1 + real rate) × (1 + inflation). Here 5% + 4% gives 9%, not the supplied 9.2%; subtraction is only an approximation. FIN-08 compares project timing/payback, while ECO-09 asks what a current materials budget buys. This case isolates multi-period unit consistency. Public-sector social discount rates and household borrowing rates are not this workshop’s cost of capital.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All project details and rates are original fiction. There are three full years from year zero, with end-of-year receipts. Both sheets describe identical real activity. General inflation is stipulated at 4%; exceptionally for clarity, every net-flow component moves at the same rate, so there are no relative-price changes. The 5% real hurdle and matched 9.2% nominal rate concern the same risk; neither is estimated from current borrowing rates. Exact relation: 1.05 × 1.04 = 1.092. Correct present value is HK$114,376.41723356; subtracting HK$110,000 gives HK$4,376.41723356. The mismatched calculation gives −HK$4,063.43632886. Year-three nominal receipts retain HK$47,244.288 to avoid intermediate rounding. Final values are rounded as labelled. No tax, working-capital, financing, terminal or other cash flows are omitted within this deliberately bounded model; all incremental operating costs are netted. Positive NPV is conditional, not guaranteed profit, an affordability assessment or an instruction to invest. The CPI release is context, not a forecast. ACCA supports the exact matching relation; our numbers are original. The Green Book concerns social appraisal and supplies no private business rate here. ECB gives an introductory subtraction calculation; the draft explicitly uses exact compounding. RBA explains an Australian household basket, not the workshop’s costs. No source table or numerical example is reproduced.

- [Hong Kong C&SD · September 2026 CPI release · 22 October 2026](https://www.info.gov.hk/gia/general/202610/22/P2026102200426p.htm). Read dated release and its price-index description. No reported rate is used as the project forecast.
- [ACCA · Inflation and investment appraisal](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html). Read real/nominal cash-flow and cost-of-capital explanations, Fisher relation and consistent-valuation discussion. Original simplified cash flows, not the article’s numerical examples.
- [HM Treasury · Green Book 2026, prices and discounting](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026). Read inflation conversion and discounting sections. UK social appraisal is not a source for this business’s rate or a claim of equivalent social and private values.
- [ECB · Nominal and real interest rates · 25 May 2016](https://www.ecb.europa.eu/ecb-and-you/explainers/tell-me/html/nominal_and_real_interest_rates.en.html). Read purchasing-power explanation. The case uses exact compounding, not the page’s introductory subtraction calculation.
- [Reserve Bank of Australia · Inflation and its measurement](https://www.rba.gov.au/education/resources/explainers/inflation-and-its-measurement.html). Read weighted-basket and CPI coverage explanations. General price indices need not match a particular project’s selling prices or input costs.
