# The customer is unhappy. Is consent still voluntary?

<!-- legacy-case-id: 405 -->

GVR-34 · Hong Kong · 15–20 minutes · Voluntary choice · Conditional access · Consent journey testing

![Fictional adult hobby-platform colleagues trace separate join and decline routes beside a class calendar in a Hong Kong office, without readable personal details.](../optional-consent-blocked-service-scene.jpg)

## Optional must work in the journey

An optional data programme needs a usable refusal path, not just reassuring wording. Research and regulatory guidance examine how interface choices and service dependencies affect people’s decisions. The platform, programme and policy below are fictional. Apply the supplied policy rather than certify compliance with Hong Kong or overseas law.

## Opening decision

You manage fictional Hong Kong hobby platform MakerCircle. Adults buy a 30-day pass for HK$100 to browse classes, book available places and manage those bookings. You are designing a separate optional preference-sharing programme. The existing paid service must remain fully usable without joining. No real customer data have been collected or shared for this programme.

The proposed 30-day programme would send selected hobby-topic preferences and a programme-specific member code to fictional partner Harbour Catalogue Lab to improve its class catalogue. No names, contact details, payment information or booking histories are included. The code remains linkable inside MakerCircle, so the data are not described as anonymous.

The supplied reviewed policy requires a clear explanation of recipient, purpose, fields, duration and withdrawal; separate affirmative agreement; and no loss of core service for refusal or withdrawal. Transfers stop immediately on withdrawal, and the partner deletes the contribution within seven days. Otherwise it deletes contributions at programme end. These are stipulated programme safeguards, not statutory deadlines.

Choose a benefit design for further review. A offers a one-time HK$10 refund on the paid pass after joining, with no repayment on withdrawal. B offers a downloadable personalised class-planning sheet based on the selected topics. Both fit the same programme budget. Neither changes booking access, prices of classes or account-management rights.

The planning sheet is an extra convenience, not the only way to find classes or manage bookings. The public catalogue and ordinary booking tools remain available to everyone. Any sheet already downloaded may be kept after withdrawal. Neither design renews the pass or enrols the member in another paid service.

Both draft screens say participation is optional, show equally prominent join and decline buttons, and leave consent unselected. The product team wants to compare benefit preferences before launch. You can instead require a journey audit first; funded test time is available and delaying this optional programme does not interrupt existing service.

## Evidence

| Design | Optional benefit |
| --- | --- |
| A | HK$10 one-time refund; no withdrawal clawback |
| B | Downloadable class-planning sheet |

**Student question:** Which benefit would you provisionally take forward, or what evidence would you seek first? Explain why neither a cash benefit nor a convenience benefit alone establishes voluntary choice. Name a journey you would test before launch.

## Round two

In the test environment, the team tries changing the time of an existing booking. A new routing rule sends every member to the preference-sharing screen first. Join opens the booking manager, but decline returns to the home page without a route to that manager. A member who later withdraws is blocked again.

The same defect appears under A and B. A tester assigned to refuse sharing says the service feels unavailable unless they agree. The notes contain no representative survey, conversion estimate or evidence of actual customer harm. No programme has launched, no real data have moved and the existing live booking manager is unchanged.

The engineer confirms this dependency was accidental and is unnecessary for booking management. The team can remove it within the funded pre-launch test work. The privacy lead requires a successful independent refusal-and-withdrawal journey check before any programme launch. Changing the benefit or the sentence saying optional will not repair the routing rule.

**Student question:** What must be corrected before either design can launch? Specify tests for joining, declining and withdrawing, including access to the paid service and the data-sharing state. Explain what the tester’s complaint establishes and what it does not establish.

## Debrief · A label cannot repair a blocked route

Pause both launches and remove the dependency. Changing a booking is part of the paid core service under the supplied policy. A decline button that leads away from the only booking-management route does not preserve that service. The defect remains even if a member receives money or likes the extra planning sheet.

The engineer’s explanation matters for investigating the cause, but accidental design still needs correction. Do not accuse an identified real business or infer deliberate manipulation from this fictional bug. Assess what the journey permits, not merely what the designer intended or what the consent screen promises.

## Debrief · Test all three choices

After correction, a member who declines must reach the ordinary booking manager without joining, sharing preferences, paying more or contacting support. A member who joins must retain the same booking-management access. Test each path from the actual entry points on supported mobile and desktop layouts, including keyboard navigation and understandable status messages.

Then withdraw from a joined test account. Confirm core booking access remains unchanged, future programme transfers stop immediately and the partner’s deletion workflow completes within the stipulated seven days. Verify that returning, refreshing or signing in again does not silently reactivate sharing. Test data should be synthetic; no real member disclosures are needed.

## Debrief · Compare benefits only after restoring choice

A’s HK$10 refund is 10% of the HK$100 pass price, but that percentage is not a universal threshold for free choice. Assess whether the offer creates inappropriate pressure in its actual context, whether the ordinary price is genuine and whether the no-clawback promise works. A cash benefit is neither automatically acceptable nor automatically coercive.

B avoids a cash comparison but is not automatically safer. Verify the sheet remains an optional convenience and that ordinary catalogue access and booking functions are genuinely usable without it. Neither the benefit type nor a high opt-in rate proves understanding or voluntariness. Delaying or dropping the programme remains an available outcome.

## Debrief · Protect scope as well as access

Keep the programme recipient, fields and purpose separate from ordinary booking operations. The member code is linkable, not anonymous. Record the agreed scope and withdrawal state; verify the partner receives only authorised fields and honours deletion. Do not add marketing, onward sharing or new inferences because the person joined this catalogue project.

Before a real launch, qualified privacy and legal review must assess the complete design, including the incentives and the partner arrangement. The supplied safeguards are classroom assumptions, not proof that consent alone makes every proposed use necessary, lawful or fair. Overseas guidance informs questions here; it does not decide Hong Kong legal compliance.

## Debrief · Evidence of a defect is not an approval-rate estimate

The test demonstrates a reproducible access failure in both prototype routes. It does not estimate how many customers would consent, become unhappy or abandon the service. Nor would fixing that failure prove every other consent issue solved. Retest comprehension and usable refusal with suitable volunteers after technical checks, without measuring success solely by sign-up volume.

Assign product and privacy owners to the release gate. Retain test evidence showing equal core access, no unauthorised transfer and working withdrawal/deletion. If any required route fails, keep the programme off while normal paid service continues. Explain the outcome honestly rather than treating a click on join as conclusive evidence of a free choice.

## Instructor note

Minutes 0–4: compare benefit risks and request a journey test. Minutes 4–8: trace the defective decline and withdrawal paths. Minutes 8–13: specify a corrected release gate. Minutes 13–18: separate the observed defect from causal claims about incentives, customer preferences or legal compliance.

GVR-24 separates operational service review from a different research purpose and rejects unauthorised sensitive profiling. This case keeps a clearly stated optional purpose fixed. Its central issue is conditional access and usable refusal in the actual workflow. No coerced-consent option is defensible; the remaining choice is whether and how to proceed after repair and review.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All companies, adult-member programme, price, benefits, policy, routes and test findings are original fiction.30daypassHK100, optionalAone-timeHK10refund=10%, no repayment onwithdrawal;Bextra downloadableplanning sheet keptafterwithdrawal, ordinarycatalogue/corebookingunchanged. No renewal. Purposefixedcatalogueimprovement, selectedhobbytopics+programmecode tofictionalHarbourCatalogueLab;code linkable notanonymous;no contact/payment/bookinghistory fields. Express separateaffirmativepermissionunderstipulatedpolicy; stoptransfersimmediatelywithdrawal,deletewithin7daysorprogrammeendifnoearlierwithdrawal. Thesearefictional safeguardsnotstatutorydeadlines. Bothprototypeflowsaccidentallygatebookingmanagementonoptin; existinglivecoreunaffected,norealdata/noactualharm. Fundedfixandindependenttestrequired. No incentivelegalityconclusion,no universal10%threshold, no survey/causalparticipationclaim. Sourcesconceptual/comparative;qualifiedreviewrequiredforreallaunch.

- [Hong Kong ITIB · Legislative Council reply · 22 February 2023](https://www.itib.gov.hk/en/legislative_council_business/questions/2023/pr_20230222c.html). Historical primary explanation discusses purpose limitation, express voluntary consent and context-specific exemptions. Background only; the exercise applies its supplied policy and does not determine current legal compliance.
- [OECD · Dark commercial patterns · 2022](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf). Original policy synthesis distinguishes forced action, obstruction and interface interference. It reviews research including other cited studies, so it is not counted as an independent experimental replication.
- [EDPB · Guidelines 05/2020 on consent · version 1.1](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf). Primary EU guidance discusses genuine choice, detriment and incentives. Used comparatively; GDPR doctrine is not presented as Hong Kong law or as categorical approval of either benefit.
- [Luguri and Strahilevitz · Shining a Light on Dark Patterns · 2021](https://content.naic.org/sites/default/files/national_meeting/Shining%20Light%20on%20Dark%20Patterns.pdf). Original US experiments examine how defaults, obstruction and other interface features affect choices. This is a copy of the original article, not NAIC-authored research; no experimental effect size is transferred to the fictional platform.
- [Utz, Degeling, Fahl, Schaub and Holz · (Un)informed Consent · 2019](https://arxiv.org/pdf/1909.02638). Original field experiments on a German website examine notice position, options and preselection. Cookie-banner results motivate journey testing, not a predicted participation rate or local legal conclusion.
