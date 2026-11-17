# A cheaper forward. A more flexible protection?

<!-- legacy-case-id: 410 -->

FIN-35 · Hong Kong · 15–20 minutes · Currency commitments · Purchased options · Uncertain underlying exposure

![Two fictional adult importer colleagues compare a fabric sample, an unconfirmed purchase folder and two plain contract worksheets in a Hong Kong office, without visible rates or settlement answers.](../cheaper-forward-flexible-protection-scene.jpg)

## Protect the exposure, not just a quoted rate

A currency forward creates a commitment; a purchased currency option provides asymmetric protection for a premium. Their suitability depends on the exposure as well as the quoted rate. If a planned purchase disappears, its protection may remain. All contracts, rates and amounts below are invented classroom assumptions, not market offers or trading recommendations.

## Opening decision

You prepare a treasury briefing for fictional Harbour Linen, a Hong Kong importer. A customer may order a batch of table linen requiring a EUR10,000 supplier payment in three months. If the order proceeds, that amount and date are fixed. If it is cancelled, the supplier releases the purchase without charge.

There are no other euro receipts, balances, payments or replacement purchases. Let S mean Hong Kong dollars per euro on the payment date: a higher S makes euros more expensive. Consider S = 9.00 and S = 8.00. Neither is a forecast; no probabilities are supplied for rates or cancellation.

Compare F, a fictional cash-settled forward, with O, a purchased cash-settled euro call option. Each covers EUR10,000 for exactly the same date and reference rate. These are alternative histories, not two contracts held together. No actual contract has been arranged; students analyse supplied cash flows rather than execute a trade.

F has no initial payment. At maturity its HK dollar receipt is 10,000 × (S − 8.50). If that number is negative, the importer must pay its absolute amount. The contract cannot be erased merely because the customer cancels. There are no further fees in this fictional quotation.

O costs HK$2,000 now, nonrefundable. Its maturity HK dollar receipt is 10,000 × max(S − 8.50, 0): use zero whenever the difference is negative. Positive value is automatically cash-settled, even if the order disappears. The importer has no further option payment obligation and is not selling an option.

If the order proceeds, euros are bought at S to pay the supplier. Both protection contracts settle in HK dollars only; neither supplies euros. Total purchase-related net outlay equals 10,000S minus the protection receipt plus any initial premium. If there is no order, the 10,000S purchase term is zero.

Ignore interest, discounting, taxes, spreads and all other charges. Sufficient funding and timely settlement are stipulated, with no default, collateral calls or early termination. These are simplifying assumptions, not normal product assurances. Terminal net outlay is not a complete real-world liquidity assessment.

First assume the order proceeds. Management wants to understand certainty, favourable-rate participation and the price of flexibility. It has not assigned cancellation probabilities or a risk preference. Compare both rates before calling the no-premium forward unconditionally cheaper; the company is not seeking speculative currency income.

## Evidence

| Input | Amount |
| --- | --- |
| Notional and maturity | EUR10,000; three months |
| Reference / strike | HK$8.50 per euro |
| F initial payment | HK$0 |
| O initial premium | HK$2,000 |
| Test spot rates | HK$9.00 and HK$8.00 per euro |

**Student question:** If the order proceeds, calculate the physical purchase, each protection receipt and total net outlay at both rates. What does each contract protect, and can the opening information establish one universally preferable choice?

## Round two

Now reveal a hypothetical outcome at the original maturity date: the customer cancels, the supplier releases the purchase without charge, and S = 8.00. There is no euro payment, goods delivery or other cancellation cash flow. Evaluate what would remain under each previously chosen alternative; do not pretend an existing contract can be changed retrospectively.

F still settles under its original formula. O’s premium remains spent and its original payoff rule still applies. No refund, replacement order, offsetting euro receipt or new hedge is available. Compare cumulative net outlay from inception, not only cash paid on the final day.

For a fresh, otherwise identical proposal, management specifies two maximum cumulative net outlays: HK$87,000 if the order proceeds and HK$2,000 if it is cancelled. Test both for every positive S under these exact formulas. This hypothetical policy is not a real treasury mandate or permission to transact.

**Student question:** After cancellation at S = 8.00, what is the net outlay under each alternative? Which satisfies both limits for a fresh proposal under the supplied model? Explain why order cancellation does not mean every valuable option should simply be abandoned.

## Debrief · The purchase still happens

At S = 9.00, the supplier payment costs HK$90,000. F receives HK$5,000, leaving HK$85,000 net outlay. O also receives HK$5,000, but its HK$2,000 premium gives HK$87,000 total. In this scenario, the option costs HK$2,000 more than the forward.

At S = 8.00, the supplier payment costs HK$80,000. F’s receipt is negative HK$5,000, so the importer pays HK$5,000 and total outlay is again HK$85,000. O receives zero; including premium gives HK$82,000. Here the option costs HK$3,000 less than the forward.

## Debrief · Name the protection precisely

With a purchase, F gives 10,000S − 10,000(S − 8.50) = HK$85,000 for every positive S. O gives 10,000 × min(S, 8.50) + HK$2,000, at most HK$87,000. The premium buys favourable-rate participation and removes the obligation to make a negative protection settlement.

Neither choice dominates on purchase cost alone. O is cheaper when S is below 8.30, ties F at 8.30 and costs more above 8.30. This boundary follows from 10,000S + 2,000 = 85,000 on the below-strike branch. It is not a forecast or an option-pricing model.

## Debrief · Remove the purchase, not the contract

After cancellation at S = 8.00, F pays HK$5,000 with no supplier payment to offset it. Cumulative net outlay is therefore HK$5,000, not HK$85,000 and not zero. O pays nothing further; its nonrefundable premium makes cumulative outlay HK$2,000. The option limits this outcome’s cost but does not refund its premium.

For any positive S after cancellation, F’s net outlay is 10,000(8.50 − S). O’s is 2,000 − 10,000 × max(S − 8.50, 0). A negative net outlay means a net cash receipt, not a bill. Keeping that sign prevents a receipt from being counted as another expense.

## Debrief · Check the new planning limits

F meets the HK$87,000 completed-order limit because its completed cost is HK$85,000. But it fails the cancellation limit whenever S is below 8.30: at 8.00 the HK$5,000 payment exceeds HK$2,000 by HK$3,000. Meeting a purchase budget does not ensure acceptable exposure when there is no purchase.

O satisfies both supplied limits: completed-order outlay never exceeds HK$87,000 and cancellation outlay never exceeds the HK$2,000 premium. Thus O fits this fresh proposal’s stated screen within the simplified model. That result does not prove lower expected cost, market availability, suitability for a real business or permission to trade.

## Debrief · An unused purchase can leave valuable protection

If cancellation instead coincided with S = 9.00, F would receive HK$5,000 and O would receive HK$5,000 at maturity. O’s cumulative net receipt would be HK$3,000 after premium. The cash-settled option’s positive value is not discarded just because euros are no longer needed; automatic settlement was explicitly stipulated.

These alternative outcomes are not a reason to seek cancelled orders or speculate. No probability distribution or sales margin is supplied, so no expected company-profit ranking is possible. The lesson is to reassess the exposure and contractual rights together, not to call every unused hedge worthless.

## Instructor note

Minutes 0–5: reconcile purchase and protection separately at both rates. Minutes 5–9: remove the purchase after cancellation but retain each contract. Minutes 9–14: derive and test the two planning limits. Minutes 14–18: discuss the positive-value cancellation counterexample and distinguish cumulative cost from final-day cash.

FIN-04 nets operating receipts against bills; FIN-28 isolates a physical-price component not covered by a hedge. Here currency, notional and date match exactly while the underlying purchase can disappear. All payoff terms are invented. Real collateral, settlement, counterparty, legal and suitability risks need separate review; no trading steps or hedge-accounting advice are taught.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Original fictional importer, purchase, customer cancellation, contracts, rates and policy. EUR10000,3months,HKDperEUR reference8.50. F receipt10000(S−8.50), noinitialpayment; O premium2000 upfront nonrefundable, receipt10000max(S−8.50,0), automaticpositivecashsettlement regardlessorder. Both alternative cash-settled histories, no actual positions or trading instruction. Euros ifneeded boughtspot separately. Cancellationreleasesentiresupplierpayment withoutothercashflows. PositiveS scenarios9/8; no probabilities. Ignore discount/interest/tax/spreads/otherfees; funding,timelysettlement,nodefault,nocollateralcalls stipulated only. PurchaseF85000always; O87000high/82000low; purchasecosttie8.30. Cancellationat8 F5000out/O2000out; at9 F5000in/O3000netin. Freshproposal limits87000completed/2000cancelled, OqualifiesallpositiveS,Ffailscancelbelow8.30. Neitherexpectedprofitnorrealmarketavailabilityclaimed. Currentordercancelreveal cannotretroactivelychangechoice. No matchingoperatingreceipt,basis/date/quantitymismatch untilpurchasevanishes; no sellingoptions.

- [US International Trade Administration · Foreign Exchange Risk](https://www.trade.gov/foreign-exchange-risk). Official explanation of currency exposure between agreement and settlement, and agreed future exchange rates. Export-focused examples supply background, not this importer’s numbers or a Hong Kong product recommendation.
- [Chris Becker and Daniel Fabbro · RBA Research Discussion Paper 2006-09 · Hedging Instruments](https://www.rba.gov.au/publications/rdp/2006/2006-09/hedging-instruments.html). Original analysis distinguishes forward commitments from option rights and premiums. Its historical usage statistics and examples are not reused; the fictional contracts explicitly settle in cash.
- [Treasury Corporation of Victoria · Foreign Exchange](https://www.tcv.vic.gov.au/clients/foreign-exchange). Provider’s own explanation addresses forward timing or volume mismatches and option rights. Its deposit products and Victorian client arrangements are not proposed for this fictional importer.
- [CPA Australia · Tips to Manage Foreign Exchange Risk · 19 April 2020](https://www.cpaaustralia.com.au/-/media/project/cpa/corporate/documents/tools-and-resources/business-management/tips-to-manage-foreign-exchange-risk.pdf?la=en&rev=89e0b1090e45426cba9c69f9417cf1f1). Original professional guidance links exposure records, scenario cash flows, product costs and risk tolerance. The case does not adopt rate forecasts or imply that a no-initial-payment contract is free of economic cost.
- [Basel Committee on Banking Supervision · RMA20 Foreign exchange risks](https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/rma/20). Official guidance distinguishes settlement, replacement-cost and liquidity risks. It concerns banks, not a direct rule for this importer, and explains why a terminal classroom payoff is not a complete operational risk assessment.
