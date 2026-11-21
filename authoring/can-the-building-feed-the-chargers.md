# The chargers arrive. Can the building feed them?

<!-- legacy-case-id: 505 -->

SUS-41 · Hong Kong · 15 minutes · Electric vehicle charging · Infrastructure capacity · Load management · Service reliability

![An estate manager and engineer review two sheets near cars connected to charging points in a Hong Kong car park.](../can-the-building-feed-the-chargers-scene.jpg)

## Hong Kong retrofits residential car parks for EV charging

In May 2026, Hong Kong’s government reported that 488 existing residential car parks had completed installation works under the EV-charging at Home Subsidy Scheme by the end of March. The works provide charging-enabling infrastructure, not the individual chargers. The estate and numbers below are fictional.

## Opening decision

Mei manages an older fictional Hong Kong housing estate with 20 bays fitted with 7 kW chargers. The committee must choose between sharing spare building capacity and paying for an electrical upgrade. An engineer has already assessed both options; these are simplified planning inputs, not installation instructions.

On the design night, 18 cars plug in at 20:00 and each needs 12 kWh at the charger output. Eight leave at midnight; ten leave at 04:00. The charger controller can share power across plugged-in cars and prioritize earlier departures. The estate promises all drivers their full 12 kWh by departure.

The exhibit gives aggregate power available to charging after reserving capacity for other uses. Ignore charging losses, power tapering and all cost differences except those stated. A night costs HK$50 under Share or HK$130 under Upgrade, including the assumed nightly equivalent of each option’s fixed costs.

## Evidence

| Fictional engineering limit | 20:00–00:00 | 00:00–04:00 |
| --- | --- | --- |
| Share: aggregate charger-output limit | 24 kW | 42 kW |
| Upgrade: aggregate charger-output limit | 48 kW | 48 kW |

**Student question:** What is the total installed rating across all 20 charger bays? How many kWh can Share deliver in each window, and can it keep both departure promises? Which option would you approve for this demand profile?

## Round two

The committee learns that three of the ten later drivers now leave at midnight; the same 18 cars still need 12 kWh each. An off-site operator can guarantee up to three 12 kWh sessions before midnight at HK$35 each, paid by the estate. Exactly the drivers assigned those slots have their full need met off site. Assume they accept and travel time does not affect their departure.

**Student question:** Can Share still keep both promises without an off-site arrangement? How many off-site slots would it need, and which feasible option now costs less? What measurement would justify revisiting that choice?

## Debrief · Separate rate from quantity

The connected rating is 20 × 7 = 140 kW; it is not the available simultaneous power. Share delivers at most 24 × 4 = 96 kWh before midnight and 42 × 4 = 168 kWh afterward. The combined maximum is 264 kWh, but it cannot all be used before midnight.

## Debrief · Check each deadline

Eight early cars need 96 kWh, exactly Share’s first-window capacity. They can each receive an average 3 kW. Ten later cars need 120 kWh, which fits the second window at an average 3 kW each. These rates are below the individual 7 kW cap. Both options can deliver 216 kWh by the required deadlines; choose Share at HK$50, while noting it has no first-window buffer.

## Debrief · More total energy does not fix an early shortage

Eleven early cars now need 132 kWh and seven later cars need 84 kWh. The total remains 216 kWh. Share falls 36 kWh short before midnight even though its combined limit still exceeds 216 kWh. Three 12 kWh off-site slots remove exactly the early shortfall. Share plus those slots costs HK$155. Upgrade can meet both deadlines with 192 kWh available in each window and costs HK$130, HK$25 less.

## Debrief · Test the switch point

If only ten cars left early, Share would need two off-site slots and cost HK$120, less than Upgrade’s HK$130. Ask for a representative departure-time and requested-energy profile, an engineer’s check of available capacity under peak building loads, and evidence that off-site slots are reliably available. A change in actual early demand or quote can reverse the decision.

## Instructor note

Spend 2 minutes on the story, 4 on the first window calculation, 4 on updated departures, and 5 on the recommendation. Compare a fixed deadline to total nightly capacity. This is a stylized management exercise, not electrical design, cost engineering, or evidence of real-world emissions savings.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All decisions, timing, equipment limits, energy needs, prices and people in the classroom scenario are fictional. The government’s dated installation count concerns charging-enabling infrastructure. No legal, engineering, emissions or subsidy eligibility conclusion is implied.

- [HKSAR Government, LCQ15: Measures to promote electric vehicles amid high oil prices](https://www.info.gov.hk/gia/general/202605/06/P2026050600233p.htm). Reports 488 car parks had completed installation works by end-March 2026; grounds the dated opening.
- [Environmental Protection Department, 2025–26 Finance Committee written replies](https://www.epd.gov.hk/epd/sites/default/files/epd/english/news_events/legco/files/fc_25-26_eng.pdf). Distinguishes infrastructure covered from individual chargers and identifies 7 kW chargers as common under the scheme.
- [Electrical and Mechanical Services Department, Electricity News 34](https://www.emsd.gov.hk/en/electricity_safety/information_for_the_electrical_trade/electricity_news/34th_issue_aug_2021/index.html). Explains how load control can matter when assessing demand on a dedicated circuit supplying multiple chargers. It is not a design approval for this scenario.
- [HKSAR Government, Updated Hong Kong Roadmap on Popularisation of Electric Vehicles](https://www.info.gov.hk/gia/general/202602/12/P2026021200268.htm). Places home and workplace charging infrastructure in Hong Kong’s wider EV strategy.
- [Environmental Protection Department, Technical Guidelines for EV Charging-enabling for Car Parks of New Building Developments](https://www.epd.gov.hk/epd/sites/default/files/epd/english/environmentinhk/air/prob_solutions/files/guidelines_on_enabling_eng.pdf). Explains that charging time may vary with total demand when load management is used. Scope is new developments, not approval for an older estate.
