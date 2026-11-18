# Encrypted here. Readable in the shared link?

<!-- legacy-case-id: 428 -->

IS-36 · Hong Kong · 15–20 minutes · External sharing · Recipient authentication · Usable access control

![Two adult designers in a Hong Kong studio compare a plain link card with two named-recipient cards beside abstract packaging sketches, without readable credentials or client information.](../encrypted-here-readable-in-the-link-scene.jpg)

## Encryption is not an audience list

Encryption protects data in storage and transit, but sharing settings determine who may obtain readable content. HKCERT warns against relying on an obscure URL for confidentiality. The agency, files, quotes and checks below are fictional. No actual client material, accounts, links or credentials are used.

## Opening decision

You manage a fictional Hong Kong design agency preparing one unreleased packaging-concept deck for two named adult client reviewers. The client has authorised those two people, and no others, to view it during a seven-day review. They may not edit or redistribute it. The agency is not authorised to publish the work.

Two proposed workflows use the same approved cloud service, encrypted storage and encrypted connections. Both provide browser viewing without editing or a download button. Both automatically end access after seven days and allow an administrator to revoke it earlier. The deck sits in an isolated location with no inherited, group, alternative-link or pre-existing external permissions.

A uses an anyone-with-the-link setting without recipient sign-in. B requires a named-recipient account and checks that the signed-in identity is on the two-person access list. The accounts are already established and verified. B needs a usability check before release; the agency will not assume that every reviewer can complete its sign-in flow.

A costs HK$400 and B HK$1,000 for this review cycle, including setup, checks and support. Both are funded and can meet the deadline if the tests pass. A colleague prefers A because both options advertise encryption and A avoids sign-in friction. No live sharing has begun.

## Evidence

| Feature | A | B |
| --- | --- | --- |
| Viewer admission | Possession of link | Named account checked |
| Access window | Seven days | Seven days |
| Cycle cost | HK$400 | HK$1,000 |

**Student question:** Which workflow would you provisionally choose for the client’s stated audience restriction? Identify what encryption, expiry and recipient authentication each do, and specify one confidentiality test and one usability test before release.

## Round two

In a controlled rehearsal using a dummy deck and agency test accounts, an unlisted tester receives a forwarded copy of A’s link and can read the deck without signing in. With B, the same tester is denied after signing in to an unlisted account. Neither check involves a real unauthorised person or client content.

One intended reviewer cannot reliably complete B’s initial verification-code screen because it requires manual retyping into separate boxes and blocks pasting. The reviewer can access their own authenticator on the same device. Removing identity checks would solve that inconvenience by abandoning the audience restriction, not by making the control accessible.

The service’s supported alternative screen accepts the complete code by paste or autofill in a labelled field and supports keyboard operation. In the fictional rehearsal, both reviewers complete sign-in and read the dummy deck with their usual tools. The unlisted tester remains denied. This alternative is included in B’s quote and preserves the same authentication requirements.

The agency also checks B’s early revocation and seven-day expiry. After each event, both a fresh request and an already-open session’s new content request are denied. Access lists and other possible permission routes are checked again. These are results for the stipulated configuration, not a claim that deleting any link always removes every permission.

Neither workflow can erase a screenshot or information someone already read. The named reviewers remain bound by the existing no-redistribution instruction. There is no measured breach probability, expected loss or financial return. If recipient verification or usable access fails before release, sharing is postponed while the agency repairs the workflow within the client’s authorised scope.

**Student question:** Would you keep or revise your choice? Explain what the forwarded-link check establishes, how the revised sign-in preserves the audience boundary, and what revocation cannot recover. Is the extra HK$600 a calculated financial return or a cost of meeting the stated requirements?

## Debrief · Separate the three controls

Encryption protects stored data and communications against specified exposure; it does not decide whether the service should display the deck to a link holder. Authentication establishes an account identity. Authorisation checks whether that identity may read this file. B uses both; A’s stipulated admission rule relies on possession alone.

Expiry limits the access period, not the audience within that period. An unlisted person can use A’s forwarded link while it remains valid. A short window and an obscure address therefore do not satisfy the client’s named-recipient requirement. No calculation of how likely forwarding is can replace that explicit restriction.

## Debrief · Choose B without claiming immunity

Choose B with the tested accessible sign-in. Its HK$1,000 cost exceeds A’s HK$400 by HK$600 for this cycle. Both budgets are available, but only B as tested meets the identity-bound sharing requirement. The difference is not a quantified return on investment or an estimate of losses prevented.

The forwarded-link check isolates an important distinction: possessing B’s URL alone does not admit an unlisted account. It does not prove that accounts cannot be compromised or that an authorised reviewer cannot photograph the screen. The fictional checks support this limited workflow decision, not a general security certification.

## Debrief · Make the authorised path usable

The initial code-entry interface adds a transcription barrier. Allowing paste or autofill changes the interaction, not who receives access or which authentication requirements apply. The supported alternative is tested with the intended reviewers and their usual tools. Do not share accounts, disclose codes to staff or switch to an unrestricted link as a workaround.

A successful rehearsal for two reviewers does not establish universal accessibility or complete standards conformance. Keep support available and reassess if devices, assistive tools or sign-in steps change. When a person cannot complete the authorised path, repair that path or postpone sharing; do not silently enlarge the approved audience.

## Debrief · Revocation has a boundary

Confirm the audience list, file scope, expiry and every route that could still grant access. Removing a link need not remove direct, inherited or other-link permissions. Here those alternatives are explicitly absent and tested. Check fresh requests and active-session behaviour rather than relying only on a changed setting label.

Revocation prevents further service access under the tested configuration. It cannot erase earlier screenshots, remembered content or separately retained copies. View-only and a disabled download button are not guarantees against copying. Retain the client’s distribution restrictions and share only the material needed for the authorised review.

## Instructor note

Minutes 0–4: separate encryption, identity and permission on a board. Minutes 4–8: reveal the forwarded-link result. Minutes 8–12: repair the transcription barrier without changing the audience. Minutes 12–17: explain the limits of expiry, revocation and copy prevention, then justify the HK$600 cost difference.

This is a paper-based design exercise. Students must not create links, transmit files, change permissions or use real credentials. The fictional service combines stipulated capabilities; the case is not a product configuration recipe. Reward a conditional release decision and concrete checks, not a promise of perfect confidentiality.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All people, agency, deck, configurations, costs and tests are fictional. Two reviewers have already-established verified accounts. One isolated file has no other external permission routes. Both designs use encryption, seven-day access, early revocation, browser viewing and no editing or download button. Only B requires an authorised named identity. The accessible alternative preserves authentication requirements, accepts whole-code paste/autofill and is tested with both reviewers. HK$1,000 minus HK$400 equals HK$600 per cycle, with no breach probabilities or ROI supplied. Revocation results apply to fresh and active-session requests in this stipulated configuration, not to previously viewed or captured content. No real sharing, access change, test attack, credential handling or personal-data collection is performed.

- [HKCERT · Cloud Storage Security](https://www.hkcert.org/security-guideline/cloud-storage-security). Official guidance distinguishes encrypted communication, authentication and explicit access permissions. Its warning about obscure URLs motivates the sharing question, not a claim about an actual agency breach.
- [Microsoft Learn · How shareable links work in OneDrive and SharePoint in Microsoft 365](https://learn.microsoft.com/en-us/sharepoint/shareable-links-anyone-specific-people-organization). Provider documentation describes anyone and specific-recipient audiences and overlapping permission routes. The case uses a fictional configuration rather than asserting every listed feature is available together in a particular product plan.
- [NIST · SP 800-207: Zero Trust Architecture · sections 2 and 2.1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf). Primary technical guidance distinguishes subject authentication, resource authorisation and continuing policy enforcement. This small exercise is not a complete zero-trust architecture assessment.
- [W3C WAI · Understanding SC 3.3.8: Accessible Authentication (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html). Official explanatory guidance addresses transcription barriers and support for paste or autofill. One successful workflow test does not demonstrate full accessibility conformance.
- [Dropbox Help · How to set or change shared link permissions](https://help.dropbox.com/share/set-link-permissions). Provider documentation explains expiry, other permission routes and limits of download blocking. These control limitations inform the case, without implying its fictional service is Dropbox.
