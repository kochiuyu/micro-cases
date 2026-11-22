# One string, two different instructions

<!-- legacy-case-id: 587 -->

IS-49 · Hong Kong · 15 minutes · Software localization · Message context · Release regression testing

![Two library staff compare mockups on a tablet at a lending counter.](../one-string-two-instructions-scene.jpg)

## Source words are not the unit of meaning

Microsoft’s localization guidance advises against reusing one string for different meanings. A fictional Hong Kong library lending app tests what happens when a new screen shares a label with a button in another workflow.

## Opening decision

The app serves Traditional Chinese and English. English is the stable source language. Build P reuses translated strings keyed to English text alone. Build C assigns keys by action meaning and sends translators the screen, consequences and protected variables. C takes 55 reviewer minutes; P takes 20. The team has 60 minutes.

For the already reviewed same Traditional Chinese replay, count correct rendered occurrences rather than counting unique labels. Release requires at least 97.5% correct and no action-changing wording on any tested route; no such errors appear in this first replay. One locale’s tests do not certify the other locale or untested routes.

## Evidence

| Initial replay | Reviewed occurrences | Correct | Action-changing errors |
| --- | --- | --- | --- |
| P · pooled by wording | 1,000 | 990 | 0 |
| C · context keys | 1,000 | 995 | 0 |

**Student question:** Which build would you release on this replay if you choose the least reviewer time among eligible builds? State the two separate gates.

## Round two

Ten new Traditional Chinese occurrences come from a confirmation screen. Here “Return” means exit back to the previous screen without surrendering equipment, whereas the existing critical “Return” button finalises the equipment return. P’s shared translation makes the new button sound like surrendering equipment in all ten occurrences; its original 1,000 results are unchanged. C uses separate keys and gets all ten correct. The reviewer times include this replay.

A separate receipt message includes a return-by time inserted at runtime. The values are correct in this rehearsal. The next release must verify that each translated message preserves the time variable and displays a useful local rendering.

**Student question:** What are the revised rates and decision? Show why editing the pooled translation to fix the new button cannot give both actions unambiguous labels, and name one variable-preservation test.

## Initial decision

P is 99.0% correct and C is 99.5%; neither has action-changing errors. P costs 20 reviewer minutes rather than 55, so it wins on the stated initial test. Identical meanings can still share keys.

## The total is not the launch decision

P retains 990/1,010 ≈ 98.02% correct and still exceeds the numeric gate, but its ten action-changing errors block release. C has 1,005/1,010 ≈ 99.50% and zero such errors within the 60-minute budget. A one-word pooled fix would substitute the wrong meaning on the other critical route; author distinct keys with screen context.

## Verify both variables and displayed actions

Check that the receipt retains exactly the required time variable and inserts the expected value in a test such as 18:05. Also replay both critical buttons and compare what a reader thinks happens with what the app does. The gate measures rendered fixtures, not how often actual readers would misinterpret a label.

## Instructor note

Ask learners to name the test that a glossary alone cannot pass. Give a second example where identical text and identical meaning can safely share one key, and ask students to contrast it with the two critical “Return” actions.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Fictional library, translations, test observations and thresholds. No personal loan records or real app used.

- [W3C, Internationalization Tag Set 2.0](https://www.w3.org/TR/its/). Defines Translate, Localization Note and Localization Quality Issue metadata.
- [Microsoft, Make your app localizable](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/prepare-your-app-for-localization). Uses Volume and noun/verb examples to distinguish safe reuse from different meanings.
- [Microsoft, Internationalization testing](https://learn.microsoft.com/en-us/globalization/testing/how-to-perform-internationalization-testing). Test checklist includes context comments, externalized strings and no reuse across different contexts.
- [Android Developers, Localize your app](https://developer.android.com/guide/topics/resources/localization). Describes contextual instructions and protects variables/placeholders from translation.
- [Microsoft documentation source, Message formatting](https://github.com/MicrosoftDocs/globalization/blob/main/globalization/internationalization/message-formatting.md). Public maintainer text explains whole messages, context, typed placeholders and placeholder reordering.
