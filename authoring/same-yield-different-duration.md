# Same yield. Same interest-rate risk?

<!-- legacy-case-id: 242 -->

FIN-21 · Hong Kong · fictional company · 12–15 minutes · Bond duration · Interest-rate risk · Cash-flow timing

![Two finance colleagues compare two plain investment folders and a long planning strip at a quiet office table.](../same-yield-different-duration-scene.jpg)

## Why a yield quote is only a starting point

A fixed promised payment and a stable resale price are different things. FINRA, the US SEC and Hong Kong investor-education guidance explain that fixed-income prices can fall when market yields rise, even if the promised payments do not change. Yield, credit quality and price sensitivity answer different questions.

This case uses invented zero-coupon holdings to isolate that distinction. It is not a report of a current bond offer, a forecast or advice to buy a security.

## Opening decision

**Fictional classroom situation.** You are the treasurer of a Hong Kong design company. The board has set aside HK$200,000 for a refurbishment expected in five years. All currently known operating bills and emergency needs are funded separately. The current plan requires none of this reserve before year 5.

Two hypothetical holdings are permitted under the company’s existing policy. S pays once in two years; L pays once in five years. Each costs HK$200,000 today and has a 4% annual yield to maturity. Neither pays interim interest: these are **zero-coupon bonds**. Interest is reflected in paying less today than the final payment, not in an annual cash coupon.

Assume identical issuer credit exposure, full payment when due, the same currency and no call or conversion rights. Ignore tax and custody charges. Purchase costs are zero in this model. S would need to be reinvested after year 2 to serve the five-year plan; its future reinvestment rate is unknown. L fixes its single year-5 payment if held and paid as promised.

Compare S and L as alternative whole-reserve policies, not a real trade. No future rate probabilities are supplied. Annual compounding applies; round displayed cash to cents only after calculating.

## Evidence

| Term | S: earlier payment | L: later payment |
|---|---|---|
| Price today | HK$200,000 | HK$200,000 |
| Yield to maturity | 4% annually | 4% annually |
| Single final payment | HK$216,320 at year 2 | HK$243,330.58 at year 5 |
| Cash before maturity | None | None |

Final payment = 200,000 × 1.04 raised to original years; the five-year display is rounded, calculations are not. Price = final payment ÷ (1 + market yield) raised to remaining years.

**Student question:** Would you provisionally choose S or L for the planned five-year reserve? Explain what the identical 4% yield tells you, what it does not tell you, and the tradeoff you accept.

## Round two

**Advance exactly one year.** Evaluate each choice as if it had already been made. Neither holding has paid cash. A newly approved, non-deferrable company payment of HK$200,000 must now come from this reserve. The refurbishment is postponed; there is no second refurbishment payment in this exercise. No other funds or borrowing can be used by the payment deadline.

The market yield used to value both holdings is now 6%, up **two percentage points**, with no change in their promised payments or credit assumptions. S has one year remaining; L has four. The company can sell either whole position and receive cleared cash before the deadline. There is a flat HK$500 sale fee, with no further spread or charge in this classroom scenario.

| Market yield at year 1 | S: one year remaining | L: four years remaining |
| --- | --- | --- |
| 4%, unchanged-yield comparison only | HK$208,000.00 | HK$208,000.00 |
| 6%, the revealed sale scenario | HK$204,075.47 | HK$192,740.61 |

These are supplied model prices, not real dealer quotes. The unchanged-yield row isolates the effect of the yield change at the same date; it is not another available sale price. Do not switch the original investment retrospectively or assume a rescue loan.

**Student question:** For each original choice, can the company meet the HK$200,000 payment after selling at the new 6% yield and paying the fee? Quantify any surplus or shortfall, then propose one reserve-policy safeguard.

## Debrief: reconcile the cash

Under S, sale proceeds after the fee are HK$204,075.47 − HK$500 = **HK$203,575.47**. The company can pay HK$200,000 and retain **HK$3,575.47**. Under L, proceeds are HK$192,740.61 − HK$500 = **HK$192,240.61**, leaving a **HK$7,759.39 shortfall**. The negative balance is an unfunded payment, not permission to overdraw.

Check the prices: S = 216,320 ÷ 1.06; L = (200,000 × 1.04 to the fifth power) ÷ 1.06 to the fourth power. S has only one remaining discounting period, while L has four. The same change in yield therefore affects different stretches of future cash flow.

## Why the later payment moves more

At year 1, both positions would be worth HK$208,000 if yields had stayed at 4%. Relative to that same-date comparison, the yield rise reduces S by **HK$3,924.53** and L by **HK$15,259.39**, before the common fee.

S is still worth more than its original HK$200,000 cost before and after the fee. That does not mean S had no interest-rate exposure: its value is lower than in the unchanged-yield comparison. Separate the effect of one year passing from the effect of the yield change.

**Duration** describes price sensitivity to yield changes. For these simple zero-coupon holdings, later payment means greater duration. Equal initial yields are not equal durations; identical credit assumptions do not remove market-price exposure.

## The tradeoff does not disappear

L was not irrational simply because this particular early-sale scenario hurts it. Under the original five-year plan, L fixes the model’s year-5 payment if the issuer pays as promised. S returns money sooner, but the rate available for reinvesting it is unknown. No probability for the early payment or yield change was supplied, so the realised outcome does not establish an ex-ante optimal choice.

The sensitivity runs both ways. In a separate year-1 illustration with a 2% yield and otherwise identical assumptions, S would be worth HK$212,078.43 and L HK$224,799.84 before fees. L gains more when yields fall; this is a scenario, not a prediction.

A defensible safeguard is to distinguish funds that may be called early from genuinely long-horizon funds, and approve a sale-value stress test before allocating the reserve. A liquid buffer or shorter-duration allocation has costs and must be sized to an explicit payment scenario. S passes this stated 6% scenario, not every possible shock. Neither a maturity label nor a credit rating establishes unrestricted liquidity in real markets.

## Optional: duration as an approximation

**Optional calculation extension.** At the year-1 comparison yield of 4%, modified duration for a zero-coupon payment is remaining years ÷ 1.04. That gives 0.9615 for S and 3.8462 for L. Approximate percentage price change = −modified duration × change in yield, using the yield change as a decimal.

For a 0.02 rise, approximate changes are −1.9231% and −7.6923%. Exact repricing gives about −1.8868% and −7.3362% relative to HK$208,000. Duration is a local approximation; use the exact discounted cash flows for this two-percentage-point move. The approximation error is not a new fee or a credit loss.

## Instructor note

Allow 12–15 minutes: two for the role, three for the first vote, four for the reveal and cash reconciliation, and three to six for the debrief. Keep round 2 and the answers closed until students state their first choice. Beginners can use the supplied prices; the optional duration calculation is not needed to decide.

Ask S supporters what happens when its proceeds must be reinvested; ask L supporters what changes if the planned holding period cannot be maintained. Do not accept “4% interest arrives each year”: both are zero-coupon holdings. Require the HK$500 fee once per whole-position sale and compare prices at the same date.

FIN-18 concerns deposit maturity, contractual early withdrawal and a supplier discount. FIN-11 concerns floating-rate borrowing costs. Here the distinct mechanism is repricing fixed future cash flows before maturity, with no issuer failure or contractual early-redemption penalty. No actual purchase, sale or personal investment recommendation is involved.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional company, holdings, cash need, yields, fee and sale prices. Annual compounding; zero coupons; no default, FX, tax, call rights, purchase costs or custody fees. Final payments equal 200,000 × 1.04 squared/fifth power, with rounding only for display and final cash settlement. After one year, remaining maturities are one and four years. Exact repricing at 6% gives 204075.471698113 and 192740.610870237 before one HK$500 fee per position. Net cash 203575.47/192240.61; surplus 3575.47/shortfall 7759.39 against 200000. Unchanged-yield year-1 value is 208000 for both; rate effects 3924.53/15259.39 before fee. Separate 2% illustration gives 212078.43/224799.84 before fee. All numerical examples are authored calculations, not empirical source data or current offers. No probabilities supplied. Six distinct substantive authoritative source bodies read; sources provide general mechanisms only. Main narrative is self-contained; no quotations, proprietary data or source artwork reproduced. A real bond sale might have different execution, settlement, spread and credit outcomes.

- [FINRA · Brush Up on Bonds: Interest Rate Changes and Duration · 19 September 2024](https://www.finra.org/investors/insights/bonds-interest-rate-changes-duration). Duration, maturity and rate-price sensitivity; the percentage rule is approximate and does not cover every risk.
- [US SEC Investor.gov · Fixed Income Investments: When Interest Rates Go Up, Prices of Fixed-Rate Bonds Fall](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-86). Interest-rate exposure before maturity, coupon and maturity effects, and the distinction between promised payments and market-price guarantees. Educational guidance, not Hong Kong law.
- [IFEC · Key risks of bonds](https://www.ifec.org.hk/web/en/investment/investment-products/bonds/key-risks.page). Zero-coupon discounting, interest-rate risk, default and secondary-market liquidity. These risks are separated rather than treated as interchangeable.
- [IFEC · More on bonds · 13 February 2025](https://www.ifec.org.hk/web/en/investment/investment-products/bonds/more-on-bonds.page). Coupon versus yield, price versus par and credit-rating limitations. No quoted market yield is borrowed for the exercise.
- [Hong Kong Government Bond Programme · Investing in Government Bonds](https://www.hkgb.gov.hk/en/investor/investing.html). Pre-maturity sale prices, liquidity limitations and yield calculations. The fictional instruments are not actual Government Bonds or offers.
- [IFEC · Buying and selling bonds](https://www.ifec.org.hk/web/en/investment/investment-products/bonds/buying-and-selling.page). Secondary-market pricing and transaction-cost structures. The HK$500 fee and assured sale/settlement are invented case assumptions, not market terms.
