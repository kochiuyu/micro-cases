# Is a big IPO allocation good news?

<!-- legacy-case-id: 495 -->

FIN-50 · Hong Kong · 15 minutes · Initial public offerings · Winner’s curse · Adverse selection · Allocation-weighted value

![Two analysts compare IPO allocation slips at a Hong Kong training desk.](../big-ipo-allocation-good-news-scene.jpg)

## Hong Kong revises how IPO shares reach the public

In August 2025, the Hong Kong Stock Exchange introduced two mechanisms that issuers can choose between for allocating shares to the public subscription tranche. That tranche is the pool made available for public subscriptions. A pool’s size is not the same as the number of shares one applicant receives. The exercise below uses fictional allotments, not either exchange mechanism.

## Opening decision

At a Kowloon training session, analyst Jan must assess a simulated public application for 120 shares in a sensor maker’s initial public offering (IPO). The offer price is HK$16 per share. If she applies, she pays for the shares allotted to her, not the 120 she requested. If she skips it, her payoff is zero.

Everyone faces the same debut value per share in each possible state. Better-informed applicants compete hardest when their signals suggest a strong debut, so Jan expects fewer shares in that state. The table fixes probabilities, values and Jan’s allotment in each state.

Measure profit at the simulated debut: value of shares allotted minus their purchase cost. Judge the decision using expected profit. Ignore fees and other costs until the second round; assume the table stays fixed when calculating a break-even price.

## Evidence

| Debut state | Probability | Value per share | Shares allotted |
| --- | --- | --- | --- |
| Weak | 25% | HK$12 | 120 |
| Middle | 50% | HK$20 | 50 |
| Strong | 25% | HK$30 | 10 |

**Student question:** What is Jan’s expected profit at HK$16, and what offer price would just break even once you account for how many shares she gets in each state?

## Round two

A colleague notices a flat HK$25 platform charge per application, payable even if no shares are allotted. This charge is fictional. Keep the share price and all the outcomes in the exhibit unchanged.

**Student question:** With the HK$25 charge, would Jan still apply at HK$16 under the model? What are the new break-even offer price and the largest flat charge she could bear at HK$16?

## Debrief · Full allotment can be bad news

The simple probability-weighted share value is HK$20.50. But the most shares arrive in the weak state, where each share is worth HK$4 less than Jan pays. A full allotment is bad news in this model, not evidence that the issuer is attractive.

## Debrief · Count dollars per application

At HK$16, state profits are −HK$480, +HK$200 and +HK$140. The expected profit is 25% × (−480) + 50% × 200 + 25% × 140 = HK$15. Under the initial assumptions Jan would apply, but the margin is much smaller than the HK$4.50 difference between mean share value and offer price suggests.

## Debrief · Weight by shares, not just states

Expected allotment is 30 + 25 + 2.5 = 57.5 shares. Expected debut value of all those shares is HK$360 + HK$500 + HK$75 = HK$935. Break-even is HK$935 ÷ 57.5, about HK$16.26 per share. This weights each state by its probability times the shares it delivers.

## Debrief · A fee changes the decision

The fee drops expected profit to 15 − 25 = −HK$10, so Jan skips the application at HK$16. With the fee the break-even price is (935 − 25) ÷ 57.5, about HK$15.83. A flat charge of HK$15 would leave Jan indifferent at HK$16; a higher charge makes skipping preferable.

## Takeaway · A model, not a trading rule

The winner’s curse here is an allocation effect: investors receive more exposure to weak issues when better-informed demand crowds them out of strong ones. A large actual allotment can have other causes, including the offering terms. The case’s fee, probabilities and allocations are not estimates for any actual IPO.

## Instructor note

Allow 15 minutes: 3 to read the exhibit, 5 to price the initial application, 4 to recheck it with the fee, and 3 to discuss what a large allotment might mean.

Ask what happens to the no-fee break-even price if Jan gets the same positive number of shares in every state. It returns to HK$20.50. Ask students to explain why just conditioning on a positive allotment does not fix the calculation here: Jan receives some shares in all three states.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All companies, people, probabilities, sums, quantities and fee terms in the exercise are fictional. The historical exchange announcement supplies context only. This is a teaching example, not an investment recommendation.

- [HKEX, IPO price discovery and open market consultation conclusions (2025)](https://www.hkex.com.hk/News/Regulatory-Announcements/2025/2508012news?sc_lang=en). Official announcement of two public-tranche mechanisms and the 4 August implementation date. These rules concern the pool of shares, not the fictional applicant’s allotment.
- [Hong Kong Government, Legislative Council reply on IPO market measures (2026)](https://www.info.gov.hk/gia/general/202605/13/P2026051200604.htm). Confirms implementation in August 2025 and explains why allocations can differ across issuers; it does not establish a link between any individual allotment and return.
- [Issuer prospectus filed on HKEXnews, structure of the global offering (8 April 2026)](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0408/2026040800017.pdf). A primary example of published offer terms identifying a public tranche and describing Mechanism B and possible reallocation. Its figures are not used here.
- [HKEX, Fast Interface for New Issuance](https://www.hkex.com.hk/Services/Platform-Services/FINI?sc_lang=en). Describes Hong Kong’s digital IPO settlement infrastructure. It does not specify or endorse the exercise’s model charge.
- [Kevin Rock, Why New Issues Are Underpriced (1986)](https://psyfitec.com/files/files/fuller/ipo/rock%201986.pdf). The original study models better-informed applicants crowding others out of more attractive offerings; the case’s three-state example is original.
