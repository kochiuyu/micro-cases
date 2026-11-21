# When does a tougher loan collect less?

<!-- legacy-case-id: 494 -->

FIN-49 · Hong Kong · 15 minutes · Borrower incentives · Moral hazard · SME lending · Pledgeable cash flow

![A lender and a fleet owner discuss a loan beside a worker checking the temperature of a chilled crate.](../tougher-loan-collect-less-scene.jpg)

## Hong Kong changes the terms of SME financing support

On 18 November 2024, changes to Hong Kong’s SME Financing Guarantee Scheme took effect. They extended the maximum guarantee periods of two products and added partial principal repayment options for new loans under those products. The fictional loan below uses project cash only and has no public guarantee.

## Opening decision

A small Kwun Tong delivery firm asks Mina, a credit officer, for HK$126,000 to start a chilled-grocery route. The firm will follow the same required safety checks either way. Its owner can also put in extra time planning collection windows and coordinating backup drivers, which makes a profitable season more likely.

Mina can verify the season’s cash from delivery and resale records, but she cannot verify the owner’s planning effort. If the owner does the extra work, success is 80% likely; without it, 50%. The work has a personal cost to the owner valued at HK$18,000.

All figures from here are in HK$1,000. The loan advances 126 today and settles at season-end. In either quote, the firm pays 20 after a weak season; only the payment after success differs. Mina needs expected collections of at least 126.

Assume both parties compare expected payoffs without discounting. The owner keeps cash after repayment, can decline for a payoff of zero, and does the extra work if exactly indifferent. There are no taxes, outside guarantees or claims on the owner’s personal assets.

## Evidence

| Season outcome | Project cash | Quote A pays lender | Quote B pays lender |
| --- | --- | --- | --- |
| Success | 240 | 155 | 175 |
| Weak season | 40 | 20 | 20 |

**Student question:** Which quote should Mina approve, and how much does the lender expect to collect under each once the owner chooses whether to do the extra work?

## Round two

Before signing, Mina learns that part of the weak-season resale proceeds cannot be assigned to the lender under the draft agreement. The money still goes to the firm. Total project cash stays at 40 in that state, but at most 10, not 20, can now be collected by Mina.

Mina can rewrite both repayments. Let R be the success payment, no more than 240, and X the weak-season payment, at most 10. The chances of each outcome, the owner’s cost of extra effort and the funding amount all stay the same.

**Student question:** Can Mina design a break-even loan that still rewards the extra work? If not, how much would she need to be able to collect in a weak season for such a loan to become possible?

## Debrief · Ask what the borrower keeps

Under A, the owner keeps 85 after success and 20 in a weak season. Extra work shifts 30 percentage points of probability towards success, adding 0.30 × (85 − 20) = 19.5 in expected retained cash. That exceeds the cost of 18, so the owner does the work.

Under B, the owner keeps only 65 after success and still keeps 20 in a weak season. Extra work adds 0.30 × (65 − 20) = 13.5, less than its cost. The owner skips it. Taking the loan is still preferable to declining it under either quote.

## Debrief · Use the repayment probability the quote creates

Mina expects to collect 0.80 × 155 + 0.20 × 20 = 128 under A, enough to cover 126. Under B she expects only 0.50 × 175 + 0.50 × 20 = 97.5. Approve A, not B. The tougher quote changes the incentive as well as the amount due.

## Debrief · Find the two limits

Extra work pays for itself when 0.30 × [(240 − R) − (40 − X)] ≥ 18, or R ≤ 140 + X. If the owner does the work, the lender breaks even when 0.80R + 0.20X ≥ 126, or R ≥ 157.5 − 0.25X.

At the new cap X = 10, the owner requires R ≤ 150 while the lender requires R ≥ 155. Lowering X makes the gap wider. Even without the extra work, the most the lender could collect on average is 0.50 × 240 + 0.50 × 10 = 125.

## Debrief · Find the minimum weak-season collection

The two limits first overlap when 140 + X ≥ 157.5 − 0.25X, so X must be at least 14. At X = 14 and R = 154, the lender expects exactly 126 and the owner is just willing to do the extra work under the tie rule. A strictly positive effort incentive needs a cap above 14.

## Instructor note

Allow 15 minutes: 3 for the first vote, 4 for the incentive and collections calculations, 5 for the revised contract and 3 for discussion. Ask each group to explain why expected collections need not rise when the amount owed in success rises.

In this model a larger weak-season payment comes out of the owner’s project cash and can strengthen the incentive to avoid that outcome. A third-party guarantee can raise lender recovery without reducing the owner’s weak-season residual, so the same incentive calculation would not apply.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The parties, figures and loan terms of the cold-chain exercise are fictional. The opening news describes the dated policy change only, not scheme eligibility or borrowing advice.

- [HKMA, briefing to the Legislative Council Panel on Financial Affairs, February 2025](https://www.hkma.gov.hk/media/eng/doc/about-the-hkma/legislative-council-issues/20250203e2.pdf). Confirms the 18 November 2024 effective date and the changes to the guarantee periods and partial repayments.
- [HKMA, nine measures to support SMEs, March 2024](https://www.info.gov.hk/gia/general/202403/28/P2024032800316p.htm). Distinguishes repayment capacity and collateral value when describing credit reviews; does not prescribe the fictional loan’s terms.
- [HKMC Insurance Limited, SME Financing Guarantee Scheme factsheet, September 2024](https://www.hkmc.com.hk/files/product/6/SFGS%20Factsheet_Eng%20eff%2023%20Sep%202024.pdf). Documents the historical guarantee ratios and lender document verification under the scheme; the case models no guarantee.
- [Holmström and Tirole (1997), Financial Intermediation, Loanable Funds, and the Real Sector](https://www.uh.edu/~bsorense/HolmStromTiroleQJE97.pdf). Derives a limit on income that can be promised to lenders without undermining borrower incentives.
- [Stiglitz and Weiss (1981), Credit Rationing in Markets with Imperfect Information](https://mubsep.mubs.ac.ug/pluginfile.php/598448/mod_resource/content/1/Stiglitz-CreditRationingMarkets-1981%20%281%29.pdf). Shows how loan terms may change borrowers’ actions as well as promised repayments.
