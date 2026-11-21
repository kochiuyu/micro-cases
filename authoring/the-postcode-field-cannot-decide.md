# The postcode field cannot make the decision

<!-- legacy-case-id: 534 -->

IS-44 · Hong Kong and Singapore · 15 minutes · Data contracts · Schema validation · Exception handling · Address formats

![A fulfilment analyst compares two different address forms and a stack of unmarked parcel labels.](../the-postcode-field-cannot-decide-scene.jpg)

## Address formats depend on where the parcel is going

The Universal Postal Union publishes destination-specific address formats. Its Hong Kong address examples omit a local postcode, while SingPost’s address guidance distinguishes the allocated six-digit code from the unit address. The lesson’s Hong Kong orders are local dispatches, not mail originating in Mainland China.

## Opening decision

A fictional retailer tests 50 orders for local fulfilment at its Hong Kong and Singapore depots. Each order ID is unique and has the correct destination. Mei owns the import review, not the actual dispatch. A junior analyst proposes one rule for both destinations: pass any row whose postcode has six digits and hold everything else.

For this pilot, a Hong Kong row needs the full address of the local drop-off, but no postcode. A Singapore row needs the full address, including the unit if required, and a trusted six-digit postcode for that address. All six-digit codes in the test are already verified. The exhibit specifies every missing required field.

Passing means suitable for the next routing review, not proof of delivery. Store source records unchanged, and record any correction in a separate reviewed field. All entries are synthetic; no real addresses or recipients are supplied.

## Evidence

| Destination and record state | Orders |
| --- | --- |
| Hong Kong: complete local address, no postcode | 20 |
| Hong Kong: missing street, no postcode | 5 |
| Singapore: complete address and six-digit postcode | 16 |
| Singapore: complete address, only five postcode digits in import | 6 |
| Singapore: required unit missing, six-digit postcode | 3 |

**Student question:** How many orders would the six-digit-only check pass or hold incorrectly? What would the destination-specific check pass and hold?

## Round two

The reviewer finds archived original text for four of the six five-digit cases. A numeric conversion stripped one leading zero in each; the original six-character field and address reference agree. There is no reliable original or reference for the other two five-digit cases.

The reviewer also finds the required unit for one of the three incomplete Singapore records in the authorised original order. No other missing field is resolved. Some orders share a building and postcode but go to different units.

**Student question:** After review, how many orders pass and how many remain held? Which information must stay as text, and why should the importer neither pad every short code nor merge orders by postcode?

## Debrief · A field can be absent for a reason

The six-digit-only rule passes 16 + 3 = 19 and holds 31. It wrongly passes the three records lacking required units and wrongly holds 20 complete local Hong Kong addresses. The same treatment of all blanks would hide whether a field is inapplicable or required but missing.

## Debrief · Validate by destination

The destination-specific rule passes 20 Hong Kong and 16 Singapore orders: 36 total. Hold 5 + 6 + 3 = 14 with separate reasons. Keep the verified destination, source text, validated format and review reason distinct. A valid postcode by itself does not verify a whole address.

## Debrief · Restore proof, not guesses

Approved evidence clears four five-digit records and one missing-unit record. Pass 36 + 5 = 41 and hold nine: five Hong Kong street issues, two unresolved Singapore code issues, two unresolved Singapore units. Preserve postcode strings with leading zeros, original input and the correction trail. Do not auto-pad any unknown value.

## Debrief · Keep record identity separate

Different orders at the same building can share a postcode, but keep their original order IDs and distinct required address parts. Test a valid Hong Kong blank, a genuine leading zero, a missing required unit and two units with the same postcode. Reconcile pass plus hold to all 50 orders.

## Instructor note

Use four minutes for the first counts, four to design reason codes, four for the review and three for tests. Ask which assumption changes if the postal origin changes. The rules in the exhibit are stated pilot conditions, not a complete addressing specification for all parcels.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All organisations, addresses, records, validation policies and quantities are fictional. The external resources give examples of real addressing formats, not authority to examine or change live records.

- [Universal Postal Union, Hong Kong address examples](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/hkgEn.pdf). Shows apartment, building and street address forms without a local postcode.
- [Universal Postal Union, General Addressing Issues](https://www.upu.int/UPU/media/upu/documents/PostCode/General-Addressing-Issues.pdf). Separately documents a specific code used from Mainland China to Hong Kong; the classroom case is local only.
- [HKSAR Home Affairs Department, Postal Services](https://www.had.gov.hk/rru/en/images/pdf/Your_Guide_to_Services_in_HK_English_chapter_18.pdf). Explains use of Hongkong Post’s local address-format finder.
- [SingPost, Mail Redirection Service guidance](https://www.singpost.com/support/other-services-enquiries/mail-redirection). Distinguishes an allocated six-digit postcode from subdivided unit numbers. This is postal context, not the pilot’s dispatch policy.
- [SingPost, official postal code lookup](https://www.singpost.com/find-postal-code). Looks up codes by address or building and shows why a plausible digit string is not itself verification.
