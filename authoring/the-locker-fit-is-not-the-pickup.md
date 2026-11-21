# The parcel fits. Will the locker be free later?

<!-- legacy-case-id: 541 -->

OPS-45 · Hong Kong · 15 minutes · Capacity reservation · Parcel lockers · Size substitution · Scenario costs

![A courier holds a parcel as a colleague gestures toward different-sized locker compartments.](../the-locker-fit-is-not-the-pickup-scene.jpg)

## Self-pickup depends on the compartment and the collection window

Hongkong Post publishes iPostal Station locations and links them to nearby post offices. A separate carrier’s Taiwan-to-Hong Kong locker service describes size and collection-time constraints. The case gives a fictional operator’s own slots, pickup patterns and costs.

## Opening decision

At a fictional Kowloon housing estate, a parcel operator opens the day with four small compartments and two large ones. A small parcel fits either size; a large parcel fits only a large compartment. Each compartment holds one parcel. Five small and one large parcels arrive this morning; two large parcels arrive in the afternoon.

With the Fill policy, use all six lockers now, including one large locker for the fifth small parcel. With Reserve, send that small parcel directly to the nearby staffed counter for HK$3 and keep one large locker free. Either option uses a large locker for the morning large parcel. A counter parcel is successfully served and never occupies a locker.

On a fast day all morning locker parcels are collected before the afternoon delivery. On a slow day none are. A large afternoon parcel that cannot fit a free locker goes to the counter for HK$8 instead. There are no other costs; minimise expected counter handling cost.

## Evidence

| Time window | Small parcels | Large parcels |
| --- | --- | --- |
| Morning | 5 | 1 |
| Afternoon | 0 | 2 |

**Student question:** Show the afternoon free large slots under each policy on fast and slow days. Which policy is cheaper if 40% of days are slow?

## Round two

Collection reminders have just been tested. The operator now forecasts that 25% of days will be slow. Assume the two all-or-none pickup scenarios and both counter handling charges are unchanged.

**Student question:** Should the operator change the policy on the revised forecast? At what slow-day probability do both policies cost the same?

## Debrief · Check the right size at the right time

On a fast day, both policies have two free large lockers in the afternoon and no large parcels go to the counter. On a slow day, Fill has no large spaces, so it diverts both afternoon parcels; Reserve has one space, so it diverts one.

## Debrief · Add the morning cost separately

At 40% slow, Fill costs 0.40 × HK$16 = HK$6.40 in expectation. Reserve costs HK$3 + 0.40 × HK$8 = HK$6.20. Reserve leads narrowly even though its morning cost is higher.

## Debrief · Recompute as pickups get faster

At 25% slow, Fill costs HK$4 and Reserve HK$5. The operator should switch to Fill under the stated objective. With slow probability p, the tie satisfies 16p = 3 + 8p, so p = 37.5%.

## Takeaway · A fit check is not a capacity promise

Using a large locker for a small parcel carries a cost only when the compartment is still needed before it is freed. An operator should measure occupancy by size and time before using this model’s switching rule.

## Instructor note

Allow 15 minutes: 3 to sketch slots, 4 for both policies by state, 5 to compare costs across rounds, and 3 to discuss evidence on pickups. Ask how partly collected mornings could change the model.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All schedules, pickup outcomes, slot counts, costs and policy choices are fictional and do not describe actual operators’ terms.

- [Hongkong Post, iPostal Stations paired with nearby post offices](https://ec-ship.hongkongpost.hk/platform/data/Nearby%20Post%20Office%20list.pdf). Primary list showing stations and nearby counters with operating hours. The exercise does not assume a provider transfer policy.
- [S.F. Express Taiwan, Hong Kong SF Locker service](https://htm.sf-express.com/tw/en/products_services/express_service/chain_and_hong_kong/personal_express_service/). Describes dimension and collection-time constraints for a specific cross-border service. Fictional costs are not copied.
- [Hongkong Post, EC-Ship API specification](https://ec-ship.hongkongpost.hk/API-portal/EC-Ship_API_Specification.pdf?t=2711147437325694468). Separately identifies an iPostal Station field and pick-up office information in relevant services, not capacity.
- [SingPost, Collection Points](https://www.singpost.com/support/managing-deliveries/collection-points). Operator describes Pick lockers and locations; confirms self-pickup as a network design pattern.
- [SingPost, Locker Solutions](https://www.singpost.com/business/delivery-solutions/domestic-delivery/lockers). Business page documents multiple locker service uses. The exercise does not use the vendor’s promised performance.
