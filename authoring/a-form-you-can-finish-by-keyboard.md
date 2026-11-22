# A form you can finish by keyboard

<!-- legacy-case-id: 597 -->

IS-50 · Hong Kong · 15 minutes · Accessible forms · Task completion · Error recovery

![One coordinator uses a desktop keyboard as a colleague records notes on a clipboard.](../a-form-you-can-finish-by-keyboard-scene.jpg)

## An accessible form supports correction, not just submission

W3C guidance covers keyboard access, meaningful focus order, labels and error identification. Hong Kong’s Digital Policy Office also provides testing guidance. The thresholds below are the fictional workshop team’s release criteria and are not a test for WCAG conformance.

## Opening decision

A makerspace runs two observed routes through a replacement workshop registration form. One uses a keyboard alone with the form visible; one uses a keyboard plus a screen reader. For this simplified comparison each script represents a distinct attempt. Success means students register the intended session independently. The existing form stays open until replacement passes.

Prototype A restyles the existing form (one developer day). B uses native form controls with persistent labels and logical focus (three days). To continue to release testing, require at least 90% overall completion and at least 80% within each route. Counts below use valid data only.

## Evidence

| Valid-data rehearsal | Keyboard only (90) | Screen reader (10) |
| --- | --- | --- |
| A · restyle | 88 | 2 |
| B · labelled controls | 82 | 9 |

**Student question:** Compute the overall and per-route completion rates. Which prototype should continue to release testing, and which failure would the pooled number hide?

## Round two

Both routes test 10 new scripts with a missing required field. The separate release gate calls for at least 8 successful recoveries in each route, after noticing and correcting the error without losing other entries. B records 8 keyboard-only and 5 screen-reader recoveries.

The team has two extra days. A visible error banner alone takes one day; the measured repeat has 9 keyboard-only and 6 screen-reader recoveries. Linked field errors, keyboard focus at a clear error summary and preserving entries take two days; measured repeat has 9 recoveries in each route. Both fixes preserve B’s valid-data results. The repeats use the same scripted routes, not a random sample.

**Student question:** Which enhancement should the team ship if these are the only remaining gates? Why can’t it combine the valid-data and error-recovery rates to clear a failing route?

## Check the denominator

A achieves 90/100 = 90% overall, but only 2/10 = 20% on the screen-reader route; its keyboard result is 88/90 ≈ 97.8%. B is 91/100 = 91% overall, 82/90 ≈ 91.1% without a reader and 9/10 = 90% with one. Only B passes both valid-data gates.

## An error must lead somewhere useful

B alone recovers 80% and 50% on the two routes. The banner raises these to 90% and 60%, still failing. The two-day workflow produces 90% on both while preserving the valid-data result. Ship B with the tested recovery work; keep the old form if the repeat confirmation fails.

## Different checks, different claims

Valid entries never exercise the missing-field state. Mixing those successes into the error-route denominator would let easy scripts mask the very failure the gate tests. Run a final manual check that focus arrives in a useful order, the error is conveyed without relying on colour, the right field can be reached, and unchanged answers survive.

## Instructor note

Have students describe what a pass means from the user’s point of view, not a screenshot. Then tell them that passing these replay gates is not a full accessibility conformance assessment.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The organisation, design results, policy gates and workload estimates are fictional. The stated tests do not certify WCAG conformance.

- [W3C, WCAG 2.2](https://www.w3.org/TR/wcag/). Normative success criteria include keyboard access, focus order, labels/instructions and identifying errors.
- [W3C WAI, Understanding Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html). Explains focus sequence for both visually following keyboard focus and screen-reader use.
- [W3C WAI, Labelling controls](https://www.w3.org/WAI/tutorials/forms/labels/). Labels support users and assistive technologies; examples distinguish visible and programmatically available cues.
- [W3C WAI, User notification](https://www.w3.org/WAI/tutorials/forms/notifications/). Describes error summary, linking to fields and advising users how to fix errors.
- [Hong Kong Digital Policy Office, Digital accessibility FAQ](https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/digital_inclusion/accessibility/faq/). Local context on accessibility testing, assistive technologies and communicating a site’s accessibility support.
