# A quiet pilot. Enough to learn?

<!-- legacy-case-id: 81 -->

IS-07 · Hong Kong · 10–15 minutes · Information systems · Staged rollout · Pilot design

![A bicycle-workshop employee and customer calmly check a phone near the counter, with a bicycle in the background.](../first-rollout-scene.jpg)

## In the news

On 2 May 2024, Hong Kong’s Government reported the announced eMPF launch and a phased onboarding timetable for trustees and schemes.

This is a historical example of staged introduction, not proof of its success or a claim that later implementation matched the timetable. The bicycle business below is unrelated and involves a much narrower display change.

## Opening decision

Fictional classroom situation. A bicycle-repair business has two workshops. It is introducing a redesigned job-status view showing whether a bicycle is being assessed, repaired or ready for collection. Customers and counter staff can use it.

Underlying records, access permissions, payments and repair work remain unchanged. Basic functional, security and accessibility checks have passed; no defect is known. This is a display change, not a database migration or a source of safety-critical repair advice. The existing view remains usable.

The manager must choose one workshop for the first week. One support colleague can watch the rollout and handle feedback. Supporting both workshops adds coordination. Users can return to the old view under the stated display-only design.

## Evidence

| Quieter workshop | Busier workshop |
|---|---|
| About 40 recent daily visits | About 200 recent daily visits |
| Mostly staff counter use | Many customer phone visits, including evenings |
| Less exposure; nearby staff help | More exposure; earlier customer-use learning |

Visits are not unique people or guaranteed future traffic. Both patterns matter.

**Student question:** Which workshop would you start with for one week? Make a provisional choice and name one finding that would make you change it.

## Round two

The supplier confirms that the redesigned view can be enabled for selected repair-job accounts, not only entire workshops. The same account keeps the same view on return visits. In a rehearsal, staff enabled and disabled it without changing the underlying repair records.

The support colleague can see feedback by workshop, device and time of day. A small cohort spanning both locations is now feasible, covering counter use, customer phones and evening checks without enabling every busy-site account.

No pilot outcome has occurred. This capability does not prove the redesign works. A mixed cohort adds coordination and needs clear support ownership; a small or hand-picked group is not automatically representative or a full-load test. Accounts and visits are different counts.

**Student question:** Keep your original site-first plan or choose a mixed small cohort? Specify what must be observed before expansion and one condition for pausing or returning users to the old view.

## Choose what the first stage is meant to teach

Quiet-first is defensible for a narrow check of staff support and day-to-day rollout procedures. Its lower exposure does not make it a complete test of customer phone use or evenings.

Busy-first can bring those uses into view earlier if support and fallback are ready. The objective is not simply the largest or smallest visit count: choose the relevant tasks, users and circumstances the first stage should cover.

## A smaller cohort need not mean a quieter setting

The new account-level capability separates exposure size from workshop selection. A mixed cohort can include useful contexts at both locations while limiting how many accounts see the change.

It still requires coordination, a named support owner and deliberate coverage. A few selected accounts may produce little use or miss important patterns. Do not equate an account limit with a fixed number of visits, a representative sample or a stress test.

## Define expansion using evidence of use

Before expanding, observe customers and staff completing actual status-check tasks on phones and at the counter, including evening use. Check that people understand the status, display information is correct for the account and support workload is manageable.

Decide which observations are needed before starting. A week with little use and no complaints is weak evidence, not automatic readiness. Timing and actual activity matter alongside the number of days. Peak-load testing remains a separate requirement.

## Give stopping a practical owner and trigger

Name who monitors feedback and can pause the rollout or return users to the old display. A serious account-specific incorrect job display warrants stopping and investigation, not waiting to fill a usage quota. Less severe confusion may call for a smaller rollout and a correction before expansion.

The rehearsal supports the narrow fallback described here. It does not establish that arbitrary system changes or database migrations can be reversed instantly without loss. Verify that the old view remains usable during the actual pilot.

## Instructor note

Do not mark quiet-first wrong before the reveal. It can serve a deliberate initial learning goal. Afterwards, ask whether the new cohort capability changes the chosen tradeoff and who will support it.

A strong response chooses a group, identifies evidence for expansion and a stopping condition. Neither staged delivery guidance nor this invented rehearsal guarantees safety or success. No failure probability or cost saving can be calculated from 40 versus 200 visits.

The company, traffic, checks and capability are fictional. This is deployment-design education, not a real account change or recommendation about pension administration.

## Sources and case assumptions

All information needed for classroom decisions is in the case. Sources are optional reading for attribution and background.

The business, views, daily visit counts and rehearsal are invented. This is a display-only redesign: records, permissions, payments and repair workflow are unchanged; no safety-critical advice is supplied. Basic checks are stipulated passed, not verified at a real company. Forty and 200 are recent illustrative visits, not unique people, future guarantees or risk probabilities. Account-level assignment persists on return visits, but accounts do not equal visits. The old-view fallback is plausible under the narrow stated architecture, not a universal promise of lossless rollback. No pilot results or full-load validation are supplied. Sources checked 14 November 2026. The eMPF item reports a historical announced timetable, not confirmed subsequent outcomes. Selected substantive guidance sections were read, not every full document. Foreign government practices and vendor engineering accounts are not Hong Kong requirements or proof of this shop’s readiness.

1. [Hong Kong Government, eMPF Platform to launch next month, 2 May 2024](https://www.news.gov.hk/eng/2024/05/20240502/20240502_153009_440.html?type=ticker) — Historical announcement of phased onboarding. No projected savings, later completion or analogy to the scale of pension administration is asserted.
2. [Microsoft, Architecture strategies for safe deployment practices, maintained guidance](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) — Relevant recommendations on progressive exposure, observation, usage and rollback were read. General guidance, not validation of this cohort; article text was accessible despite a generic authorization notice.
3. [Alec Warner and Štěpán Davidovič, Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — Relevant population, duration and measurement sections were read. Supports weighing exposure and informative use; the fictional cohort is not a causal A/B experiment.
4. [UK Government Service Manual, How the beta phase works, maintained guidance](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — Substantive guidance on limited real-user rollout, support and learning was read. UK delivery practice is not a Hong Kong legal or assessment requirement.
5. [Clare Liguori / AWS, Automating safe, hands-off deployments, 18 June 2020](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) — Relevant first-person engineering sections on controlled rollout, monitoring and compatibility were read. Not a prescription to copy Amazon infrastructure or evidence that this supplier passed real tests.
