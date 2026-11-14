# A faster machine. More finished boxes?

Case 34 · Hong Kong · 10–15 minutes · Operations · Bottlenecks · Process capacity

![A packing manager and colleague consider equipment while staff prepare gift boxes at separate worktables.](../packing-line-scene.jpg)

## In the news

On 16 July 2023, Hong Kong’s government news service described Hongkong Post’s packet-sorting robotics, introduced in March 2022. Parcels passed through scanning, weighing and robotic sorting; staff then sealed mailbags for dispatch.

The story shows connected activities, not a diagnosis of a bottleneck at Hongkong Post. It prompts a different question for a small business: if one activity gets faster, will the complete process produce more?

## Opening decision

Fictional classroom situation. You manage a Hong Kong gift-order packing workshop. Every identical box goes through pick/check → wrap → seal/label. Customers have enough orders for 150 finished boxes per hour over the coming busy period. Orders are waiting, and you want more acceptable boxes ready for dispatch.

A supplier demonstrates a HK$20,000 pick/check setup that raises that station’s capacity from 120 to 200 boxes per hour. You have not measured the other stations. The budget can fund one equipment or workstation improvement, and you must choose before the busy period. There is time for a short process study before deciding.

## Evidence

The proposed HK$20,000 setup raises pick/check capacity from 120 to 200 boxes/hour. Other station capacities are initially unknown. Demand is 150 finished boxes/hour. One improvement can be funded; there is time to measure the process first.

**Student question:** Approve the faster pick/check setup now, or measure the full packing line first? What output would justify the purchase?

## Round two

A representative time study now measures all three stations, including normal interruptions. These are sustainable rates of acceptable work for the same box design.



| Station, in order | Current capacity |
|---|---:|
| Pick/check | 120 boxes/hour |
| Wrap | 80 boxes/hour |
| Seal/label | 100 boxes/hour |

Separate staff run each station. Every box passes all three in that order. Materials, transfer space and transport between stations are adequate; no other process limits this simplified model. These are steady-state rates, not promised first-hour output after an empty-line start.

For the same HK$20,000, a wrapping-workstation redesign can raise wrapping from 80 to 120 boxes/hour. Alternatively, the proposed pick/check setup raises that station from 120 to 200. Either change leaves the other stations, staffing, quality and recurring costs unchanged. Budget permits only one. Demand remains 150 boxes/hour.

**Student question:** Which investment would you choose now, and how many extra finished boxes per hour could it support?

## Follow one box to the end

In this simplified serial process, the slowest station limits sustainable finished output. Initially, that is wrapping: min(120, 80, 100) = 80 boxes/hour.

Faster pick/check gives min(200, 80, 100) = 80. It does not increase the flow of finished boxes under these assumptions. Sending extra work to wrapping only creates waiting work unless upstream release is controlled.

Improved wrapping gives min(120, 120, 100) = 100. The potential gain is 20 completed boxes/hour, or 25%, not wrapping’s 40-box gain and not the advertised 80-box pick/check gain.

## The bottleneck moves

After the wrapping change, sealing and labelling becomes the limiting station. The process still cannot meet demand of 150 boxes/hour. Do not promise that the entire backlog disappears.

Keep enough prepared work available so the constraint is not starved, but do not reward upstream staff merely for building the largest pile. Recheck end-to-end performance, quality and queues after the change. A different product mix, downtime pattern or staffing arrangement could change the constraint.

## A decision you can defend

For the stated goal of increasing completed boxes, the wrapping redesign is the useful candidate; the faster pick/check setup adds no finished-flow capacity in this model. Verify the redesign at the required quality before committing.

That is a capacity comparison, not a full investment appraisal. Confirm how long the extra demand lasts, the contribution from additional completed orders, implementation downtime and the HK$20,000 outlay before claiming payback or profit. If those economics fail, delaying both purchases is defensible.

Key idea: improve the process’s limiting activity, then look again. A station’s speed is not the same as the business’s output.

## Instructor note

Use 2 minutes for the first vote, 3 to reveal the time study and 5–7 to trace one box through the alternatives. Ask students who choose the faster pick/check setup which downstream rate changes. Ask students who choose wrapping why its 40-box improvement yields only 20 more completed boxes. Close by separating capacity from financial return and noting the remaining demand gap.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The workshop, equipment offers, prices, station rates, demand and operating conditions are invented teaching assumptions. They are not estimates of Hongkong Post or DHL performance. The serial-process calculation assumes sustainable rates, adequate materials and transfer capacity, unchanged quality and separate staff. Government and supplier statements about the same postal installation are separate documents, not independent replication. No claim is made that mailbag sealing constrained Hongkong Post. Undated educational sources checked 14 November 2026.

1. [Hong Kong Government · Using tech to propel mail service, 16 July 2023](https://www.news.gov.hk/eng/2023/07/20230713/20230713_184301_929.html?tl=t) — Describes the March 2022 robotic system and subsequent staff sealing of mailbags. The reported efficiency comment is not used as a measured end-to-end delivery gain.
2. [Geek+ · Hongkong Post sorting-system announcement, 25 July 2023](https://www.geekplus.com/resources/news/hongkongpost) — Supplier describes sorting capacity of up to 1,000 packets/hour. A stage-capacity claim, not guaranteed completed deliveries; announcement date is not installation date.
3. [DHL Express · Hong Kong West Service Center opening, 9 April 2024](https://www.dhl.com/hk-en/home/press/press-archive/2024/dhl-express-unveils-its-fully-automated-eco-friendly-service-center-in-hong-kong.html) — Company announcement describes connected automated sorting, weighing/dimensioning and screening functions. Not independent evidence for this fictional investment.
4. [ACCA · Throughput accounting and the theory of constraints](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/throughput-constraints1.html) — Educational explanation of constrained system output and excessive upstream production. Supports the process reasoning, not a claim about the postal installation.
5. [Lean Enterprise Institute · Standardized Work](https://www.lean.org/lexicon-terms/standardized-work/) — Describes process-capacity sheets, work sequence and in-process inventory. Supports measuring connected activities and reviewing the workflow.
