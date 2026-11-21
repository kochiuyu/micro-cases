# The aisle test passed. Did the screen shut buyers out?

<!-- legacy-case-id: 508 -->

MKT-42 · Hong Kong · 12–15 minutes · E-commerce · Task accessibility · Incremental contribution · Channel launch

![A grocer and a storefront designer look at a keyboard and a delivery-slot selector next to a shopping basket.](../the-aisle-passed-but-the-screen-scene.jpg)

## One online shop, two ways to enter

Hong Kong’s Digital Policy Office illustrates how a keyboard user can miss important form information when a control is only available by mouse. The W3C similarly treats keyboard operation as part of an operable web interface. These publications show an access problem, not how often it happens or how much it costs a retailer.

## Opening decision

Fictional Pantry Bridge sells weekly ingredient boxes. Its checkout delivery-time picker works by mouse, but a contractor reproduces a keyboard-only path that cannot reach some dates. The store has HK$9,000 for one action this month: repair the picker, or buy ads that send 1,800 additional visits to the unchanged site. Either action costs the full budget. Count only incremental contribution versus keeping the current site and budget.

Finance assumes 10,000 eligible visits without the ads, with 10% using the keyboard route, and HK$45 contribution per completed order before the one-off spend. A deliberately balanced lab test of tasks informs the following planning rates; the lab mix is not traffic share. Assume ads bring the same route mix, and the repaired checkout keeps pointer completion unchanged. Treat the rates as hypothetical planning inputs, not a causal sales estimate.

## Evidence

| Planning rate per eligible visit | Current | With repair |
| --- | --- | --- |
| Keyboard route | 10% | 50% |
| Pointer route | 20% | 20% |

**Student question:** How much incremental contribution would each option earn after its cost? Which would you fund based on the stated assumptions?

## Round two

The analyst corrects the estimated keyboard share from 10% to 4%, with everything else unchanged. The store also documents its fictional launch rule: do not buy traffic for a customer journey with a known reproducible blocker in a supported input route. The full repair removes the reproduced blocker, but it still needs regression and user testing.

**Student question:** At 4%, which option looks better on incremental contribution alone? At what keyboard share does repair break even? How should the launch rule affect the decision?

## Debrief · Count people who can complete

At 10% keyboard use, the current site completes 100 keyboard orders and 1,800 pointer orders out of 10,000: 19% in total. Repair adds 1,000 × (50% − 10%) = 400 orders and adds HK$18,000 contribution before the HK$9,000 cost, so net gain is HK$9,000. Ads add 1,800 × 19% = 342 orders, so net gain is HK$6,390. Repair leads by HK$2,610.

## Debrief · Separate a business case from a launch rule

At 4%, current completion is 4% × 10% + 96% × 20% = 19.6%. Ads add 352.8 expected orders and HK$6,876 net; repair adds 160 orders and loses HK$1,800 this month. Repair breaks even at HK$9,000 ÷ (10,000 × 40% × HK$45) = 5% keyboard share.

## Debrief · The campaign is still on hold

The launch rule still excludes the ads. Repair with an explicit HK$1,800 modeled shortfall if fixing the blocker now is required; otherwise hold the campaign, price a narrower fix and retest before spending. Do not convert the projection into a compliance finding.

## Instructor note

Ask why a lab with equal numbers of keyboard and pointer tasks cannot estimate the fraction of visits using those routes. Discuss how to reproduce a full successful checkout, including selecting alternative dates and returning from a payment error. Test with people who normally use the affected route; a convenient keyboard check is not a complete accessibility audit.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Website standards and public surveys are source context. All products, budgets, visits, estimated rates, rules and results in the decision are fictional. No actual system or compliance outcomes are asserted.

- [Hong Kong Digital Policy Office · Web Accessibility Handbook, version 2](https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/digital_inclusion/accessibility/promulgating_resources/handbook/doc/Web_Accessibility_Handbook.pdf). Section 6.5 illustrates mouse-only information and the importance of keyboard results.
- [W3C · WCAG 2.2 Recommendation](https://www.w3.org/TR/2023/REC-WCAG22-20231005/). Criteria 2.1.1 and 2.1.2 address keyboard operation and leaving a component with keyboard input.
- [Hong Kong Digital Policy Office · On Focus example](https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/digital_inclusion/accessibility/promulgating_resources/handbook/wcag2a/8_25_on_focus.html). Shows a form whose help dialogue interrupts a keyboard journey and a user-triggered alternative.
- [W3C WAI · Involving users in evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/). Explains benefits and limits of user evaluation; it complements standards checks rather than replacing them.
- [Census and Statistics Department · 2024/25 Household Expenditure Survey](https://www.info.gov.hk/gia/general/202606/09/P2026060900321.htm). Tracks household online purchases; this is market context, not evidence of keyboard route prevalence.
