# One hundred couriers. One hundred matches?

<!-- legacy-case-id: 59 -->

ECO-05 · Hong Kong · 10–15 minutes · Economics · Network effects · Local matching

![A courier and two dispatch colleagues discuss a delivery service beside plain document envelopes in a Hong Kong office.](../local-matches-scene.jpg)

## In the news

In its annual results announced on 31 March 2025, GoGoX described driver engagement, onboarding and demand-prediction initiatives in Hong Kong and overseas markets aimed at improving order matching. These are management descriptions, not independent evidence that a particular intervention caused better results.

The practical question is familiar to any local marketplace: do the participants who join actually find useful partners? Our document-delivery platform below is fictional and its figures are not GoGoX data.

## Opening decision

Fictional classroom situation. A small Hong Kong marketplace connects businesses needing document deliveries with independent couriers. It is deciding whether its next recruitment effort should open a third service district or strengthen its two existing districts.

For tomorrow’s fixed delivery window, the dashboard shows 100 actual delivery requests and 100 couriers who have confirmed availability. Each courier can accept at most one request during that window. Opening another district would broaden the service’s reach; concentrating the effort could improve reliability for existing participants. A colleague says: “Both sides are equal. Our current network is ready; let’s expand.”

The figures are active requests and available people, not cumulative registrations. No cost, willingness-to-travel or next-month demand estimates have yet been supplied. The decision today concerns the next recruitment effort, not a promise that tomorrow’s requests are already assigned.

## Evidence

| Tomorrow’s window | Total across current districts |
|---|---:|
| Delivery requests | 100 |
| Available couriers | 100 |
| Maximum requests per courier | 1 |

**Student question:** Would you direct the next recruitment effort to a new district or strengthen the current network first? What must you know before treating equal totals as evidence of a working marketplace?

## Round two

The team breaks the same totals down by district: District A has 80 requests and 20 available couriers; District B has 20 requests and 80 available couriers.

For this classroom calculation, every courier is suitable for any request in their own district. No courier can travel between districts within tomorrow’s promised window, and each can handle only one request. These are fixed constraints for this window, not a permanent rule about Hong Kong travel.

The totals remain 100 and 100. No new recruitment or relocation can change tomorrow’s capacity. Later availability could change through voluntary arrangements; willingness, costs and recurrence of this pattern are unknown.

**Student question:** How many requests could be matched at most tomorrow? Does this change which side and district you would target next, and what would you check before spending?

## Count feasible pairs, not just participants

District A can form at most 20 pairs: its couriers are the limiting side. District B can also form at most 20 pairs: its requests are the limiting side. The combined ceiling is 20 + 20 = 40 matches, not 100.

At that ceiling, 60 requests in A remain unmatched and 60 couriers in B have no request. Forty is a feasibility ceiling under the stated assumptions, not a prediction that every feasible pair accepts and completes a delivery. An algorithm cannot remove a binding travel constraint.

## An extra participant matters where a partner is missing

A two-sided network connects two different groups. More suitable couriers can make the service more useful to businesses; more suitable requests can make it more useful to couriers. These cross-side benefits depend on usable matches, not merely on a larger headline total.

As a counterfactual comparison, keeping everything else the same, one additional suitable courier in A could raise the matching ceiling by one, until demand is met. Another courier in B would not raise it while B has only 20 requests. Conversely, an additional suitable request in B could use spare capacity. More customers in A would not solve its courier shortage.

This illustrates local matching constraints. It does not estimate a network-effect coefficient or prove increasing returns, profitability or a winner-takes-all market.

## Target the missing side; test whether it persists

Before the next recruitment round, compare requests and voluntary availability by district and delivery window over several days. Investigate cancellations, acceptable terms, reliability and whether the mismatch repeats. Do not force couriers to relocate or assume they will wait unpaid.

A targeted effort could seek suitable couriers in A or business demand in B, or negotiate a different future window with participants. Compare the cost and willingness involved with evidence for the new district. More feasible matches alone do not establish better margins.

Expansion may still be sensible if the third district has a viable local mix and attractive economics. The error is using balanced citywide totals as sufficient proof. Track completed matches and participant experience, not just sign-ups.

## Instructor note

Take an opening vote, ask what a “network” count misses, reveal the district split and give pairs one minute to calculate the ceiling. Then ask whether recruiting one more courier in each district has the same effect.

The learning objective is local cross-side matching and the marginal usefulness of the missing participant. It differs from fee incidence, supplier dependence and a generic growth-versus-profit debate. Keep the fixed-window arithmetic separate from the later recruitment choice. No subsidy amount or algorithm is prescribed.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The platform, districts, time window and all counts are invented. The no-cross-district constraint and one-request capacity define a simplified matching exercise, not a claim about real operators. Company descriptions are attributed, not independently verified causal findings. Sources checked 14 November 2026. The AEA source was read at its public abstract; no full-text empirical estimate is claimed or transferred to Hong Kong.

1. [GoGoX Holdings, 2024 annual results announcement, 31 March 2025, printed page 17](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033102141.pdf) — Management describes driver engagement, onboarding and demand prediction for matching in Hong Kong and overseas markets. Provides the dated local hook, not the classroom figures.
2. [Lalamove Hong Kong, Sustainability Report 2025 announcement, 15 April 2026](https://www.lalamove.com/en-hk/press-releases/sustainability-report-2025) — Company describes route suggestions and order-matching optimisation. Supports the relevance of matching operations; environmental and safety claims are not used.
3. [Uber, Matching riders with drivers, undated](https://www.uber.com/us/en/marketplace/matching/) — Explains proximity, traffic, geography and trip requirements in matching. Its US-oriented feature descriptions are not assumed to apply in Hong Kong or to document deliveries.
4. [Prateek Jain, Soheil Sadeghi and Mehrdad Bakhtiari, Uber Engineering, Reinforcement Learning for Modeling Marketplace Balance, 2 July 2025](https://www.uber.com/us/en/blog/reinforcement-learning-for-modeling-marketplace-balance/) — Explains changing supply-demand balance across places and times. No algorithm, company performance estimate or need for AI is inferred for the fictional firm.
5. [Juan Camilo Castillo and Shreya Mathur, Matching and Network Effects in Ride-Hailing, AEA Papers and Proceedings 113, May 2023, pages 244–247, public abstract](https://www.aeaweb.org/articles?id=10.1257/pandp.20231069) — Models matching and network externalities. Its model-specific increasing returns and subsidy result are not conclusions of our arithmetic exercise.
