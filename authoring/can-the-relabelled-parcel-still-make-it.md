# Can the relabelled parcel still make it?

<!-- legacy-case-id: 562 -->

OPS-47 · Hong Kong · 15 minutes · rework loops · bottleneck capacity · dispatch cutoff

![A dispatch supervisor watches cartons pass through a scanner beside a relabelling bench.](../can-the-relabelled-parcel-still-make-it-scene.jpg)

## Why a label matters to the line

Hongkong Post documents barcode labels for tracking bulk airmail bags. DHL describes how an obscured parcel barcode can prevent automated sorting and tracking. The next scenario is a fictional parcel depot in Hong Kong, not a description of either operator.

## Opening decision

You run the late shift at Banyan Parcel. Eight unreadable parcels have already used one scan each and are at the exception bench. The booking identity can be verified from an intact record for each; no parcel can leave without a successful scan or verified carrier acceptance.

All 26 waiting clean parcels scan successfully on the first pass. Relabelling any exception takes one bench slot and makes its next scan successful. Both clean parcels and relabelled exceptions need one of the gate’s 30 remaining scan slots. The bench can finish up to six relabels before the selected gate slots; assume no other sequencing delays.

Maximise the contribution from dispatching on time based on the exhibit. Late dispatch contributes zero in this exercise. The costs of ordinary scanning and relabelling are already reflected in the amounts shown.

## Evidence

| Waiting parcels | Count | Net contribution if sent on time |
| --- | --- | --- |
| Clean, standard promise | 26 | HK$10 each |
| Unreadable, priority promise | 6 | HK$30 each after relabelling |
| Unreadable, standard promise | 2 | HK$6 each after relabelling |

**Student question:** How many of each type should Banyan send tonight, and which parcels lose their place in order to make that plan feasible?

## Round two

The gate now has only 27 slots. The service team imposes a minimum of 24 clean parcels on tonight’s truck. The same six bench slots remain.

A carrier can take up to three verified, relabelled priority parcels separately tonight through its own scan, with no use of Banyan’s gate. Its added fee is HK$12 each. Those parcels still use Banyan’s bench slots. No other parcels can use this service.

**Student question:** What mix should Banyan now send through the gate and through the carrier, and how much contribution does the carrier option add versus operating without it?

## First decision: charge every pass to the gate

Send six priority exceptions and 24 clean parcels for 6 × HK$30 + 24 × HK$10 = HK$420. Two clean parcels and both standard exceptions wait. Four priority parcels fit without displacement; the next two each replace a HK$10 clean parcel with a HK$30 priority parcel. A standard exception cannot improve the plan.

## Second decision: move validated work around the bottleneck

Without the carrier, send 24 clean and three priority parcels through the gate for HK$330. Keep that gate mix and transfer the other three priority parcels to the carrier: 3 × (HK$30 − HK$12) = HK$54 extra, for HK$384. All six bench slots are now needed. Sending a fourth priority parcel through the gate would violate the clean minimum.

## What to take away

A repaired label is not a dispatched parcel: the repaired item returns to the same scarce step. Count gate visits rather than parcels repaired. The alternate route is worth paying for here because it frees the constrained gate, not because it repairs labels faster.

## Instructor note

All plans, numbers and depot rules are fictional. Ask learners whether adding a seventh bench slot alone could improve either decision.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All plans, numbers and depot rules are fictional. Ask learners whether adding a seventh bench slot alone could improve either decision.

- [Hongkong Post, EC-Ship bulk airmail guide](https://ec-ship.hongkongpost.hk/platform/data/User%20Guide_BAM%20AC%20Scan_eng_v5.pdf). Section C describes barcode labels for mail-bag tracking, not individual parcel gate operations.
- [DHL eCommerce, Delivering your parcels safely](https://www.dhl.com/content/dam/dhl/local/gb/dhl-ecommerce/documents/pdf/gb-ecommerce-delivering-your-parcels-safely.pdf). The labelling section shows why obscured and creased labels can hinder barcode scanning.
- [GS1, Logistic Label Guideline](https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf). Section 9 describes how parties use identifiers and scanners in logistics.
- [DHL Hong Kong, Computer Vision for Shipments](https://www.dhl.com/hk-en/microsites/csi/computer-vision/logistics-use-cases/shipments.html). Operator research shows barcode and optical character capture in parcel sorting.
- [UPS, Retail Rates and Service Guide](https://www.ups.com/media/en/2007_retail_rsg.pdf). Historical packing instructions distinguish the visible shipping label from duplicate address information inside a package.
