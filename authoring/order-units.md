# The file arrived. What did we order?

Case 53 · Hong Kong · 10–15 minutes · Information systems · Data quality · Process integration

![A stationery shop owner and assistant discuss order sheets and a laptop beside notebooks and an open carton.](../order-units-scene.jpg)

## In the news

On 19 November 2025, OCBC Hong Kong announced a partnership with GS1 Hong Kong using, with users’ consent, transaction data from the ezTRADE platform for a digital trade-finance service. The announcement describes digital purchase orders, invoices and shipment advice.

This illustrates how business records travel between organisations and inform further decisions. It does not report a unit-conversion failure. Our separate stationery-shop test below is fictional and unrelated to either organisation.

## Opening decision

Fictional classroom situation. A Hong Kong stationery shop wants to automate weekly orders to its supplier. Staff currently re-enter the order lines manually, which takes time and can introduce mistakes.

A new connector sends the shop’s order files to the supplier’s test system. Every test file has arrived successfully. The owner wants to enable live automatic ordering next week and remove routine manual confirmation.

The team has checked file delivery, but has not yet compared the goods and quantities represented by the supplier’s acknowledgements with the shop’s intended orders. All work remains in a test environment: no purchase order has been placed.

## Evidence

| Check | Current evidence |
|---|---|
| Test files reach the supplier | Yes |
| Acknowledged goods and quantities match intent | Not yet checked |
| Live ordering enabled | No |

**Student question:** Would you switch on automatic supplier ordering next week, or keep manual confirmation while testing further? What would count as a successful test?

## Round two

One shop record requests 120 individual notebooks of a particular model. The corresponding supplier product record is a carton containing 12 of that same notebook.

The connector copies the quantity number 120 unchanged, without translating the packaging unit. The supplier’s test acknowledgement therefore represents 120 cartons, not 120 individual notebooks.

For this product, the supplier accepts whole-carton quantities only. This is still a test: no goods have been dispatched and no loss has occurred. Other products may have different pack sizes.

**Student question:** How many cartons should this request specify? What must the team verify before enabling automatic ordering, beyond successful file delivery?

## Same number, different meaning

The copied number would represent 120 × 12 = 1,440 notebooks at the supplier. The intended 120 notebooks require 120 ÷ 12 = 10 cartons for this particular product.

A file can arrive, parse correctly and contain a valid number while representing the wrong business request. Technical acceptance does not establish that both organisations mean the same product, packaging level and quantity.

The problem is not solved by dividing every order by twelve. Conversion depends on the verified product and pack size; a non-whole-carton request needs an explicit business decision rather than silent rounding.

## Make the shared meaning explicit

Agree which product identifier refers to the individual notebook and which refers to the orderable carton. Record the packaging level, contents per carton, quantity unit and applicable conversion.

Preserve the shop’s intended individual-unit quantity alongside the supplier’s carton quantity. For a test, convert the supplier’s acknowledgement back to individual units and compare it with the approved intent.

Do not assume a barcode, a matching product name or a successful import alone guarantees correctness. The records and rules behind them need a named owner and a way to handle changes.

## Test exceptions, then release carefully

Pause automatic submission for the affected mapping. Correct it and test normal orders, different pack sizes, changed product records, unknown units and quantities that do not fit whole cartons. Route unresolved cases for review rather than guessing.

Use a limited rollout with reconciliation and a clear stop procedure. Compare intended orders with supplier acknowledgements and, later, received goods.

Automation remains a credible option after appropriate checks. Manual entry has its own costs and errors; this test does not prove that permanent manual processing is safer or quantify the connector’s benefits.

## Instructor note

Before the reveal, ask students what “successful” means: delivered file, accepted message or correct business transaction? Afterward, have them label every quantity with its unit.

Keep the lesson on shared meaning and end-to-end validation, not programming syntax or any real vendor’s reliability. The arithmetic is simple; the managerial task is deciding who owns definitions, exceptions and release approval.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The stationery shop, connector and all test figures are fictional. No real organisation is alleged to have made this error. Sources checked on 14 November 2026. Vendor announcements provide context, not independent proof of claimed benefits. Sources are optional attribution, not required student reading; no source tables or illustrations are reproduced.

1. [OCBC Hong Kong: digital trade-finance announcement, 19 November 2025](https://www.ocbc.com.hk/iwov-resources/hk/ocbc/gbc/pdf/media/2025/Press%20Release_OCBCHK%20GS1%20HK%20Launch%20Digital%20Trade%20Finance%20Service_EN_Final.pdf) — First-party account of consent-based transaction-data use; no connection to the fictional ordering error.
2. [GS1 US: Packaging Level Definitions](https://www.help.gs1us.org/packaging-level) — Explains individual items, inner packs and cases; the notebook example is original.
3. [GS1 US: Import Higher Levels of Packaging](https://www.help.gs1us.org/import-higher-levels-of-packaging) — Records packaging level, contained identifiers and quantities separately; does not report the fictional false-success incident.
4. [UK Government: The Government Data Quality Framework, 3 December 2020](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework) — Distinguishes expected format and range from accuracy and fitness for purpose; general guidance, not Hong Kong law.
5. [GS1 Hong Kong: enhanced 1QR platform announcement, 9 April 2025](https://www.prnewswire.com/apac/news-releases/gs1-hong-kong-celebrates-innovation--collaboration-with-newly-upgraded-1qr-platform-at-annual-dinner-2025-302424546.html) — First-party release about identifiers and business information; not evidence that a QR code alone fixes data quality.
