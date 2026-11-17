# Mostly zero. Forecast nothing?

<!-- legacy-case-id: 412 -->

OPS-35 · Macau · 15–20 minutes · Intermittent demand · Occurrence and size · Forecasts versus commitments

![Two adult depot planners in a fictional Macau equipment-service storeroom examine a small replacement bracket and a plain monthly demand chart with sparse marks, without legible forecast answers.](../mostly-zero-forecast-nothing-scene.jpg)

## Zeros can be genuine demand observations

Intermittent-demand methods distinguish whether demand occurs from how large it is when it occurs. A monthly average can therefore be fractional even when parts are indivisible. Research also distinguishes a demand forecast from the inventory needed to meet a service objective. The depot and every observation below are fictional.

## Opening decision

You plan one replacement bracket at fictional Macau equipment-service depot QuietBay. It fits a noncritical removable storage accessory, not a safety device. Approved repairs, service standards and customer commitments remain protected. The immediate task is a next-month planning forecast, not a purchase order or permission to defer necessary maintenance.

The exhibit records all genuine reactive customer requests during twelve complete months. Zero means no request, not unavailable stock, closure, missing data, returns or suppressed enquiries. Records are deduplicated in brackets, not orders. There is no distributor batching or promotion, and the installed equipment population was unchanged.

Compare A: use last month’s request quantity as next month’s forecast; B: describe the full window using the proportion of months with requests and the average quantity in those months. Treat B as a transparent baseline under an unchanged reactive-demand process, not a fitted advanced model or a proven winner.

The manager favours A because the latest two months were quiet. No future reactive orders, obsolescence evidence or new operating restrictions are known. Neither the series nor the manager’s preference establishes next month’s actual demand. A separate planned-maintenance register is being checked before the total planning figure is finalised.

## Evidence

| Months | Monthly quantities, in order |
| --- | --- |
| 1–4 | 0, 0, 2, 0 |
| 5–8 | 0, 0, 4, 0 |
| 9–12 | 0, 3, 0, 0 |

**Student question:** Which baseline would you present for reactive demand, A or B? Calculate the nonzero-month frequency, average nonzero quantity and implied monthly rate. Explain why neither zero nor a fractional forecast tells you exactly how many brackets to stock.

## Round two

The planner marks demand events in months 3, 7 and 10, with quantities 2, 4 and 3. The two fully observed gaps between events are four and three months. The time from the last event to the end of month 12 is two months; it is an unfinished gap, not a completed two-month interval.

The last event before month 1 is unknown. Do not invent a three-month completed gap before month 3. Three nonzero observations do not establish a regular replacement cycle, a distribution or statistical independence between event size and timing. The full twelve-month window remains the denominator for the simple frequency baseline.

The separate maintenance register now confirms exactly two bracket replacements next month for a newly commissioned, separately identified equipment group. These are approved planned jobs, not reactive requests from the historical group. They neither replace nor overlap the reactive-demand stream. Both jobs proceed, requiring one bracket each. Assume no reactive requests from this new group next month.

Those two approved brackets are already physically reserved and funded for the booked work. Do not cancel or release them because A predicts zero reactive demand. There is no other known planned requirement next month. The future reactive process is assumed unchanged only for the conditional baseline calculation.

The depot has not supplied free reactive stock, outstanding reactive replenishments, supplier lead time, demand uncertainty, service target or shortage and holding costs. Therefore no numerical replenishment or safety-stock decision is possible from this exhibit. Required service arrangements remain in place while the planner obtains those inputs.

**Student question:** Prepare next month’s planning statement with known planned work separate from the reactive baseline. What total conditional expected requirement follows from B, what do the observed gaps establish, and what must be checked before choosing a reactive stock quantity?

## Debrief · Separate occurrence from quantity

Three of twelve months contain requests, giving an empirical nonzero frequency of 3/12 = 0.25. Their quantities total 2 + 4 + 3 = 9 brackets; mean nonzero quantity is 9/3 = 3. Multiplying 0.25 × 3 gives a baseline of 0.75 bracket per month.

This equals the ordinary full-window mean, 9/12. The decomposition makes its ingredients visible; it does not create extra information or improve accuracy by arithmetic alone. Under an unchanged process, I would present B as the more informative provisional planning baseline, alongside A’s zero and the very limited evidence.

## Debrief · Quiet months do not prove zero need

A forecasts zero because month 12 was zero. That is a legitimate last-observation benchmark, not proof the part will never be needed again. Nine quiet months coexist with three positive months. Conversely, B’s 0.75 is not evidence that exactly one bracket will be requested next month.

The frequency 0.25 is a sample fraction used as a planning estimate, not a validated future probability. The observed nonzero mean is also uncertain. A longer run of zeros could indicate changed equipment use or obsolescence, but the supplied two-month gap alone does not establish either.

## Debrief · Do not invent an interval model

The completed observed gaps are four and three months, averaging 3.5 months. Dividing the three-bracket nonzero mean by 3.5 gives about 0.857, not 0.75. Those quantities use different observation boundaries: the interval average omits the unknown initial gap and unfinished final gap. Do not call them interchangeable estimators.

Croston-type methods separately smooth positive quantities and interarrival intervals, using explicit initialisation and updating rules. B is not a Croston calculation: it uses a full-window empirical frequency and conditional mean. No smoothing parameters are supplied, and this short record does not establish which forecasting method performs best.

## Debrief · Add distinct known work once

The maintenance register supplies two known planned brackets from a separate equipment group. Keep them as a dated requirement. B’s reactive baseline is 0.75, so total conditional expected requirement is 2 + 0.75 = 2.75 brackets. A would give 2 + 0 = 2, not zero total demand.

A total expectation of 2.75 is not a physical work order or an instruction to reserve three. The two planned brackets are already reserved and must not be counted again as an additional purchase. If planned work overlapped historical reactive demand, simply adding it could double-count; the case explicitly rules that out.

## Debrief · Forecasting is not stocking

An inventory decision needs the distribution of demand over replenishment lead time, existing free stock, inbound supply, service objectives and relevant costs. A point rate alone supplies none of those decisions. Do not round 0.75 to one and label that safety stock, or treat an average as a service guarantee.

Retain the approved maintenance reservations and obtain the missing reactive inventory inputs. Review equipment use and maintenance changes before extrapolating. Compare candidate forecasts on later held-out periods and the operational outcomes that matter, rather than selecting a model because it fits these twelve observations or predicts many zeros correctly.

## Instructor note

Minutes 0–4: distinguish genuine zeros from missing or censored observations. Minutes 4–8: compute 3/12, 9/3 and 0.75. Minutes 8–12: mark complete versus unfinished gaps and add the distinct known jobs. Minutes 12–17: separate 2.75 expected requirement, two reserved brackets and the still-undetermined replenishment decision.

OPS-01 studies stockout-censored sales; OPS-18 studies batching and amplified orders. Here observations are genuine uncensored requests and intermittency is the modelling problem. The small window demonstrates frequency and size, not statistical validation. No maintenance procedure, critical-parts stock policy or customer service reduction is being prescribed.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All observations, equipment groups and planning rules fictional. Noncritical removable storage accessory, safety/approvedservice protected. Reactive quantities0,0,2,0,0,0,4,0,0,3,0,0;genuinecompletezerorequests,no censoring/returns/closure/promotion/batching.3positive months/12=.25;sum9;positive mean3;windowmean.75.Observedcompletedgaps7−3=4 and10−7=3,mean3.5;3/3.5≈.857 not equivalentwindowmean;beforewindowgapunknown,afterlastgap2unfinished. No fittedCroston/smoothing/independence/periodicityclaim. Bconditionalunchangedreactiveprocessassumption, notvalidatedprobability/accuracywinner. Separatenewgroupapprovedplannedjobs2requiringoneeachalreadyreserved/funded,nooverlap/displacementofreactivestream.2+.75=2.75conditionalexpectedtotal;A2+0=2. No actualfractionaljob or autoorder3. Reactivefreestock/inbound/leadtime/uncertainty/service/costinputsabsent,nonumericalreplenishmentrecommendation. No releaseofplannedreservations or cancelledservice. The new equipment group generates no reactive requests next month under the fictional exercise assumption.

- [Hyndman and Athanasopoulos · Forecasting: Principles and Practice · Section13.2](https://otexts.com/fpp3/practical.html). Original educational treatment separates positive quantities and interarrival times and explains Croston’s limitations. The case’s empirical frequency baseline is deliberately not labelled Croston’s method.
- [Nikolaos Kourentzes · Intermittent demand forecasting with tsintermittent](https://cran.r-project.org/web/packages/tsintermittent/vignettes/tsintermittent.html). Package author’s technical vignette explains demand-rate forecasts and occurrence/size methods. No software fit, parameter estimate or claimed accuracy improvement is imported.
- [Pennings, van Dalen and van der Laan · Exploiting elapsed time for managing intermittent demand for spare parts · 2017](https://pure.eur.nl/ws/portalfiles/portal/47741629/Exploiting-Elapsed-Time-for-Managing.pdf). Original research introduction discusses timing, size and possible dependence driven by maintenance. Its empirical improvements do not validate this fictional twelve-month baseline.
- [Willemain, Smart and Schwarz · A new approach to forecasting intermittent demand for service parts inventories · 2004](https://smartcorp.com/wp-content/uploads/2015/07/IJF_Bootstrap_paper_Smart_Software.pdf). Original research distinguishes a mean rate from the distribution of demand over replenishment lead time. Its shipment proxies and comparative results are not transferred to the case’s genuine request records.
- [Van der Auweraer, Boute and Syntetos · Forecasting spare part demand with installed base information · 2019](https://orca.cardiff.ac.uk/id/eprint/117050/1/Forecasting%20spare%20part%20demand%20with%20installed%20base%20information.pdf). Authors’ original scholarly review links demand generation to equipment and maintenance information. A literature synthesis, not a new experiment or proof that these known jobs overlap the historical stream.
