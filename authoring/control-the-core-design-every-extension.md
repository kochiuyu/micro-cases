# Control the core. Design every extension?

<!-- legacy-case-id: 366 -->

STR-31 · Hong Kong · fictional software platform · 15–20 minutes · Platform governance · External complementary innovation · Boundary resources

![Two fictional platform colleagues and an independent developer discuss neutral interface sketches at a Hong Kong workspace.](../control-the-core-design-every-extension-scene.jpg)

## Let others extend a platform without abandoning its rules

Research on software platforms examines how interfaces, development tools and participation rules enable independent firms to create complementary products while the platform owner retains control of its core. These resources can both enable contribution and constrain it.

Shopify’s published extension and review documentation illustrates that defined extension points and mandatory review can coexist. It does not establish the best governance policy for every platform. The Hong Kong platform, policies, costs and test evidence below are wholly fictional, not descriptions of Shopify or Apple.

## Opening decision

A fictional Hong Kong business operates software that helps small creative studios organise non-confidential sample catalogues. It owns and maintains the core catalogue system. Independent software firms want to sell optional add-ons, called extensions, to studio customers. These firms are not employees, franchisees or branches: they own their extension code, choose whether to invest, and receive their own extension-sale proceeds under disclosed terms. Customers opt in; the existing catalogue works without extensions.

The platform can fund one six-month governance pilot at HK$60,000, including tools, review, documentation and support. Both designs are technically feasible and affordable, with no measured revenue or cost advantage. A, the owner-shaped catalogue, publishes four permitted commercial feature categories from its roadmap. External developers may create different designs within them, but a new feature category needs the owner’s discretionary roadmap approval. B, bounded external innovation, permits new feature categories without that commercial approval if they stay within the same documented technical interface and pass mandatory checks.

Both retain the same security, privacy, reliability, accessibility, disclosure and licensing requirements; neither is an unreviewed app store. Both use the same isolated extension environment, limit access to authorised catalogue functions, require customer consent and have a funded removal and rollback process. Neither exposes core source code or allows extensions to alter the core. Existing customer contracts remain unchanged. The decision is whether independently conceived purposes must also fit the owner’s commercial roadmap, not whether safeguards apply.

## Evidence

| Dimension | A: owner-shaped catalogue | B: bounded external innovation |
| --- | --- | --- |
| Fully funded pilot budget | HK$60,000 | HK$60,000 |
| New commercial feature category | Requires discretionary roadmap approval | Allowed within published boundaries |
| Mandatory assurance review | Required | Required |
| Core ownership and extension code ownership | Unchanged | Unchanged |

**Student question:** Would you choose A or B for the governance pilot? Explain what control the owner should retain and what independent developers need in order to create something the owner has not specified.

## Round two

Three independent developers demonstrate working prototypes using the same permitted interface. One produces a conventional contact sheet within the existing roadmap. Two introduce unplanned purposes: arranging sample images into a physical exhibition-wall mock-up and producing a comparison board for textile colour selections. Both operate only on customer-selected catalogue items. All three have passed the pilot’s mandatory assurance checks; no proposal requires additional data access, a security exemption or a core change.

The owner reviews all three promptly. It approves the contact sheet but declines the other two under A because it wants the catalogue to retain its narrow administrative identity, not because review staff lack time. Under B all three could enter a customer pilot after the same checks. Each developer has funded its own maintenance and accepts the disclosed support, rollback and permitted-use obligations. Twelve invited studio managers tried the prototypes: four asked to test the wall mock-up further and three asked to test the textile board further. Nobody has bought either, and the groups may overlap. These requests indicate possible uses, not market size or proven demand.

The customer-support rehearsal also finds that participants confuse some extension functions with the core product. B’s funded plan can provide clear developer labels, documentation and support routing, but no customer test yet shows that these eliminate confusion. A offers a narrower, more predictable product identity; B allows a wider range of independent experimentation while retaining the core boundaries. Neither has a measured profit or adoption forecast. The owner can revise its future governance after the six-month pilot, while honouring published commitments and existing customer protections.

**Student question:** Keep or change your governance choice? Explain the cost of restricting commercial purposes versus permitting them, and specify one enabling resource, one retained control and one pilot outcome to review.

## The platform can set boundaries without specifying every use

A has not rejected unsafe software: all three prototypes meet the common requirements. It has rejected two commercial purposes outside its desired product identity. B separates that commercial veto from mandatory assurance. The distinction matters because an external firm may discover a useful combination of existing functions that the owner did not put on its roadmap.

Interfaces, documentation, test tools and clear participation rules are often called **boundary resources**. They let independent firms build around a protected core. They do not require publishing core source code, waiving review or permitting unrestricted access. Here both routes use the same technical architecture; the commercial permission differs.

## Independent contributors cannot simply be assigned a roadmap

These developers invest their own resources and own their products. The platform cannot treat them as internal staff whose next task it assigns. Predictable permissions, usable documentation, support routes and an honoured interface-support period can make independent investment more practical. They still cannot guarantee profitable products or oblige every developer to participate.

The two rejected prototypes illustrate additional experimentation B would permit. Four and three further-test requests cannot be added into seven unique customers because overlap is unknown. They establish neither paid demand nor the value of all future extensions. More extensions is not automatically more customer value.

## Choose a governance position, then test its consequences

B is defensible if the owner wants the platform to support applications it cannot fully anticipate and accepts greater variety in the customer experience. A is defensible if a deliberately narrow product identity matters more than the unproven niche uses. A can hear external ideas, but its discretionary commercial gate makes the owner’s intended scope decisive. There is no universally optimal level of openness.

For B, provide documented examples and a published interface-support period, retain assurance testing and revocation for breaches, and identify the developer and support contact clearly. Review successful customer tasks, voluntary continued use, developer maintenance, support confusion and rule violations. For A, track useful proposals excluded solely by roadmap fit and whether the narrower catalogue actually improves customer understanding. Do not substitute total app count or membership for these outcomes.

## Instructor note

Use three minutes for the initial governance choice, four for the prototype and support evidence, and six for the trade-off and pilot design. Both options preserve mandatory protections. Do not reward bypassing review as innovation or assume a pass on assurance proves commercial value.

The mechanism is distributed complementary innovation under platform governance, not local buyer–seller matching or economies of scale. It differs from delegating two known operating choices to branches: autonomous external firms originate, own and fund new products. It also differs from a product maker joining an industry standard: this firm owns the platform and sets participation boundaries. No real platform terms are accepted or changed in the exercise.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All firms, policies, prototypes, budgets, assurance outcomes and interview requests are fictional. Both governance designs cost HK$60,000 for six months; no economic winner is derived. Three prototypes include one inside the roadmap and two outside; all pass mandatory checks. Four and three test requests may overlap and are not purchases. External developers own and fund extensions; the core remains controlled. No protected code or live customer data is disclosed. Sources support governance concepts and examples, not fictional outcomes.

- [Petrik and Mikusz · A Method for Boundary Resources Design to Increase Complementor Satisfaction · published online9 October2025](https://link.springer.com/article/10.1007/s12599-025-00968-w). Read introduction and framework on enabling independent complementary innovation while retaining control, and on resources supporting developer engagement. Industrial-platform research, not a predicted effect for this fiction.
- [Engert, Evers, Hein and Krcmar · The Engagement of Complementors and the Role of Platform Boundary Resources in e-Commerce Platform Ecosystems · 2022](https://link.springer.com/article/10.1007/s10796-021-10236-3). Read introduction and theoretical background: autonomous firms extend a platform core; technical and social resources facilitate and constrain contributions. Qualitative research does not establish the fictional pilot’s best policy.
- [Shopify developer documentation · App extensions](https://shopify.dev/docs/apps/build/app-extensions). Read defined extension points, unchanged authentication requirements, versioning and review provisions. Illustrates extensions inside a governed platform; the fictional commercial veto is not a Shopify rule.
- [Shopify developer documentation · About the app review process](https://shopify.dev/docs/apps/launch/app-store-review/review-process). Read mandatory requirements, review and publication stages. Contribution and review coexist. This distinct process document shares a publisher with the extension architecture guide.
- [Apple Developer · App Review Guidelines, sections1.6 and2.5](https://developer.apple.com/app-store/review/guidelines/). Read data-security requirements, public-API use and containment restrictions. Bounded participation need not imply unrestricted access. No Apple-specific compliance advice or claim the fictional design qualifies for an actual store.
