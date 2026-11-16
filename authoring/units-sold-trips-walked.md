# The most units sold. The most trips walked?

<!-- legacy-case-id: 292 -->

OPS-25 · Hong Kong · 15–20 minutes · Warehouse slotting · Pick visits · Space constraints

![Two fictional warehouse colleagues consider vacant near-dispatch storage bays beside bulky cartons, compact bins and a handling trolley.](../units-sold-trips-walked-scene.jpg)

## More orders can mean a different picking workload

On 12 August 2020, DHL announced its IDEA warehouse software. Its announcement described growing online order volumes alongside smaller shipments, and explained that the tool grouped orders and improved picking routes. This is a company account of a wider operational challenge, not independent proof of a particular slotting rule.

The fictional warehouse below does not buy that software or change its routes. It asks a narrower question: which products should occupy two scarce nearby storage bays? All products, quantities, distances and handling arrangements are invented teaching inputs.

## Opening decision

You manage a fictional Hong Kong accessories wholesaler before a fixed one-week order book is picked. Two empty storage bays near dispatch are available. Layout A puts bulky presentation boxes in both nearby bays. Layout BC puts adapter pouches in one and label rolls in the other. Products not placed nearby stay in their existing farther locations. These are the only two layouts offered for this exercise; all other products and activities are unchanged.

Each presentation box counts as one sales unit, as does each adapter pouch or label roll. The table shows units due for dispatch during the same week, not revenue or number of customer orders. The team has not yet checked how those units are grouped into picking requests. No stock has moved, so your first choice is provisional.

The two near bays together can hold the complete week’s bulky-box stock, while each compact product needs one bay for its complete week’s stock. Every near and far location has passed the fictional site’s handling and storage review, including load capacity, supported access height, product compatibility and clear routes. Approved trolleys and handling aids are available. The bulky product cannot share a bay with either compact product. Do not remove these constraints or substitute unsafe lifting to gain space.

Starting stock covers the fixed order book in either layout. Both are filled before picking begins, with equal setup effort and no replenishment during the exercise. A dedicated picking visit goes from dispatch to one product and back: 20 metres in total for a nearby location or 80 metres for a farther one. The whole quantity requested on that visit fits the approved trolley. Each request is served separately, with no shared route or batching. Loading and checking effort, service commitments and all non-travel work are unchanged between layouts. Minimise total picking travel, not headcount or a worker speed target.

## Evidence

| Product | Units due this week | Near bays required |
|---|---:|---:|
| Presentation boxes | 1,200 | 2 |
| Adapter pouches | 600 | 1 |
| Label rolls | 200 | 1 |

**Student question:** Would you provisionally give the two nearby bays to presentation boxes or to adapter pouches and label rolls? Explain what the unit-sales table can and cannot tell you about picking travel.

## Round two

The team now checks the same fixed order book. All 1,200 presentation boxes leave in 30 full-carton requests of 40 boxes each. The 600 adapter pouches leave in 300 requests of two each. The 200 label rolls leave in 200 requests of one each. Each request requires exactly one separate dispatch-to-product-and-back visit under the stated method. These are complete request counts, not estimates of average order size. They reconcile to the original unit totals.

| Product | Units per request | Separate visits |
| --- | --- | --- |
| Presentation boxes | 40 | 30 |
| Adapter pouches | 2 | 300 |
| Label rolls | 1 | 200 |

The storage, trolley-capacity, no-batching and no-replenishment assumptions are unchanged. Both layouts remain feasible, and no move has yet occurred. Compare all three products’ travel in each layout, including products left farther away. There is no wage rate, walking speed or cash saving supplied.

**Student question:** Which layout would you now choose to minimise the week’s picking travel? Calculate total distance for both layouts and explain why a high unit-sales ranking is not a pick-visit ranking.

## Count visits, not pieces

The 1,200 boxes produce only 30 visits because each request takes a full carton. The pouches and rolls together produce 500 visits although they account for only 800 units. Sales units measure product flow; separate visits measure repeated travel in this model. Neither revenue nor stock value is the decision metric.

Before the request breakdown, preferring boxes because they sell more units is a plausible starting heuristic, not a calculated travel result. A preference for BC is also provisional: compactness alone does not establish how often staff visit a location.

## Compare both complete layouts

Layout A requires 30 × 20 + 300 × 80 + 200 × 80 = 40,600 metres. Layout BC requires 30 × 80 + 300 × 20 + 200 × 20 = 12,400 metres. BC saves 28,200 metres, or 28.2 kilometres, across the whole team’s one-week request book. These are aggregate route distances, not one person’s shift distance.

Each visit moved from far to near saves 60 metres. Using both bays for boxes saves 30 × 60 = 1,800 metres relative to leaving all three products far away. Using them for pouches and rolls saves (300 + 200) × 60 = 30,000 metres. The all-far comparison is 530 × 80 = 42,400 metres; it is a check on the arithmetic, not a third offered layout.

## Space and safety are part of the choice

BC is best of the two feasible layouts under the supplied inputs. It does not follow that the item with the most requests should always go nearest dispatch. Products consume different amounts of space; a heavy or awkward product may need a particular handling position or aid. Those constraints define which layouts can be considered before travel savings are compared.

Here each compact product occupies one bay, while boxes occupy both. In a larger problem, competing combinations, replenishment work, congestion and shared routes can change the answer. The case deliberately fixes those factors so that unit quantities and handling events can be distinguished.

## Less travel is not automatically cash saved

The difference represents travel workload avoided under the model. It is not a measured productivity increase, a promise of faster deliveries, a reduction in safe staffing or a payroll saving. Work could be less tiring or capacity could be redeployed, but these outcomes require their own evidence. Do not convert kilometres into money or require faster walking without additional justified inputs.

## Instructor note

Allow three minutes for the opening vote and ask what information is missing. Give four minutes to reconcile units and visits, then four to calculate both complete layouts. Use the remaining discussion to distinguish the activity count, capacity constraint and objective. Ask an A supporter what observation would change the choice; ask a BC supporter why small package size alone is insufficient evidence.

Accept a qualified opening choice or a reasoned statement that the data do not yet rank travel. In round two BC is the bounded model answer. Common errors are multiplying units by metres, counting only the products moved, treating a round trip as one-way, or combining requests despite the stated method. Do not invent replenishment, relocation costs or safety exceptions. A useful extension is to ask which missing operational change would invalidate the simple per-visit comparison, without claiming an unpriced redesign is available.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All warehouse names, products, quantities and layouts are original fiction; no source dataset, table, image or company outcome is reproduced. Boxes: 1,200 units in 30 requests of 40; pouches: 600 in 300 requests of two; rolls: 200 in 200 requests of one. There are 530 separate visits. Round-trip distances are 20 metres near and 80 metres far. A totals 40,600 metres; BC totals 12,400; difference 28,200. All-far is 42,400. Two near bays can hold all boxes or both compact products, with stipulated safe access, capacity and suitable handling aids. Equal setup, complete initial stock, no replenishment, no batching and unchanged non-travel work isolate slotting travel. No cash, time or staffing saving is inferred. Five public source bodies were read: DHL’s dated announcement, the Georgia Tech exercise, OSHA storage guidance, HSE warehouse guidance and the Irish HSA storage case. The safety sources overlap and are guidance, not three independent empirical studies or Hong Kong legal advice. The Georgia Tech data file was not downloaded or reused; its page supports distinguishing pieces from requests and considering storage and replenishment together.

- [DHL Group · Artificial Intelligence: DHL algorithm makes e-fulfillment more effective · 12 August 2020](https://group.dhl.com/en/media-relations/press-releases/2020/artificial-intelligence-dhl-algorithm-makes-e-fulfillment-more-effective.html). Company announcement describes more online orders, smaller shipments, order grouping and picking-route analysis. Context only; no reported percentage gain is transferred to this fictional case.
- [John J. Bartholdi III · Order-picking data (Warehouse Science / Georgia Tech)](https://www.warehouse-science.com/book/supplement/projects/dataset1/index.html). Public teaching page separately defines pieces sold, requests/picks, dimensions and stock, and considers picking plus restocking effort. Only the concepts inform this original exercise; its dataset and numerical example are not reused.
- [US OSHA · Grocery Warehousing: Storage](https://www.osha.gov/etools/grocery-warehousing/storage). Actual guidance discusses low and high access, bulky products, reaching and suitable slot arrangements. Supports treating access and handling constraints as requirements, not optional travel trade-offs. US guidance is not asserted to be Hong Kong law.
- [UK Health and Safety Executive · Warehousing](https://www.hse.gov.uk/logistics/warehousing.htm). Actual guidance covers handling aids, worker input and separation of pedestrian and vehicle routes. Supports the safe-route and approved-equipment boundaries; historical injury statistics are not used.
- [Ireland Health and Safety Authority · Case Study 4: Warehouse Storage, text version](https://www.hsa.ie/eng/workplace_health/manual_handling_display_screen_equipment/risk_assessment_videos/case_study_text_version_/case_study_4_warehouse_storage_text_version). Actual case illustrates assessing load and task risks and reorganising storage/handling rather than improvising access at height. It supports the non-negotiable safe-access screen, not the fictional distance calculation.
