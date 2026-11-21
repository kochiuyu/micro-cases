# The typhoon is over. What restarts first?

<!-- legacy-case-id: 499 -->

OPS-41 · Hong Kong · 15 minutes · Disruption recovery · Time-bucket scheduling · Release gates · Backlog

![A depot coordinator compares cleared and waiting routes on a board while dispatch trucks queue outside.](../typhoon-ends-what-restarts-first-scene.jpg)

## After Ragasa, services returned in stages

In September 2025, Super Typhoon Ragasa disrupted transport in Hong Kong. The MTR reported inspecting and clearing open rail sections before service could gradually resume. Hong Kong International Airport remained operational, but its operator announced a gradual resumption of flights. A change in weather was not the same as immediate recovery across every route.

## Opening decision

After a fictional typhoon, Yin runs dispatch for a Lantau depot with two sets of customers, East and West. Nine one-truck orders are ready. East is confirmed clear for 09:00; West expects clearance for 10:00, but the supervisor has not yet signed off.

One gate serves both routes. At most three trucks can leave in each hourly slot starting at 09:00, 10:00 or 11:00; at most two can leave at 12:00. The hourly times are departures. A slot cannot be carried forward, and a route cannot be used before its own confirmed clearance.

Meet as many priority dispatch deadlines as possible, then clear the remaining backlog as early as possible. Orders within the same row are interchangeable. No trucks arrive after the nine listed here.

## Evidence

| Order group | Trucks | Latest on-time dispatch |
| --- | --- | --- |
| East priority | 2 | 09:00 |
| West priority | 2 | 10:00 |
| East regular | 3 | 12:00 |
| West regular | 2 | 12:00 |

**Student question:** If West clears at 10:00 as expected, which trucks would you plan to release in each slot? What would you tell West customers before clearance is confirmed?

## Round two

West’s inspector now expects to sign off only for the 11:00 slot. Use that time for the revised plan, but do not release any West truck until clearance is confirmed. A late priority dispatch triggers a HK$1,000 credit per order; the missed deadline remains in the service record.

An approved partner already on the customer side of the closure has suitable local stock and can dispatch exactly one West priority order at 10:00 for HK$400. That order would leave Yin’s backlog, use no depot slot and avoid its late credit. The partner cannot cover any other order.

**Student question:** With West’s clearance delayed, which orders remain late, how does the depot schedule change, and is the approved partner worth using?

## Debrief · Clear the first three slots

One valid plan is 09:00: two East priority and one East regular; 10:00: two West priority and one West regular; 11:00: two East regular and one West regular. All nine depart on time. Tell West customers that the 10:00 dispatch remains conditional on a clearance check before release.

## Debrief · A free slot cannot cross a closed route

Without the partner, use 09:00 for two East priority and one East regular, and 10:00 for two East regular. One 10:00 slot is unused because no West truck may travel yet. At 11:00 release both West priority trucks and one West regular; the last West regular leaves at 12:00. Two priority orders are late.

## Debrief · Recover one deadline, not the whole route

Use the same East plan and let the partner cover one West priority order at 10:00. The 11:00 depot slot can then take the other West priority and both West regular orders. One priority order remains late. The late credit plus fee is HK$1,400 versus HK$2,000 without the partner, a HK$600 saving.

## Takeaway · Know which limit moved

Priority rules allocate capacity within safe routes. They do not make an uncleared route usable. A verified alternative already on the far side can meet a deadline that empty depot slots cannot. If its fee exceeded HK$1,000, late credits alone would not justify it.

## Instructor note

Allow 15 minutes: 3 to check the rules, 4 to set the first plan, 5 to respond to the delay, and 3 to defend a revised promise. Ask why completing more jobs at 10:00 is not feasible without changing the West constraint.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

The depot, customer orders, times, costs and procedures are invented. This case does not give actual typhoon safety or routing instructions.

- [Hong Kong Observatory, Super Typhoon Ragasa report](https://www.hko.gov.hk/en/informtc/ragasa25/ragasa.html). Primary weather record, monitoring and local impacts during September 2025.
- [MTR service updates for 24 September 2025](https://www.mtr.com.hk/archive/corporate/en/press_release/PS-2025-09-24-E_Typhoon.pdf). Operator explains phased resumption after inspection, clearance and repairs on different sections.
- [Airport Authority Hong Kong, Ragasa recovery notice](https://www.hongkongairport.com/en/media-centre/press-release/2025/pr_1823). The airport stayed operational, yet airlines expected a gradual flight resumption.
- [Hong Kong Government, response to Ragasa, 24 September 2025](https://www.info.gov.hk/gia/general/202509/24/P2025092401544.htm). Describes the transport coordination centre’s route monitoring and safety checks before gradual restoration.
- [Transport Department, two temporary ferry adjustments](https://www.td.gov.hk/filemanager/en/content_13/TPF2/Temporary%20Service%20Adjustments%20of%20Central%20Hung%20Hom%20and%20Sai%20Wan%20Ho%20%20Kwun%20Tong%20Licensed%20Ferry%20Services%20en%20.pdf). Gives route-specific suspensions before the storm and points readers to updated resumption notices.
