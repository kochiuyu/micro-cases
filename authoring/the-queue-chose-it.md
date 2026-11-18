# The queue chose it. Did the queue know more?

<!-- legacy-case-id: 455 -->

ECO-38 · Hong Kong · 15–20 minutes · Information cascades · Bayesian updating · Dependent observations

![Two adult workshop visitors compare blank private signal cards beside two equally accessible activity stalls, with a few other adults choosing calmly and no visible outcome or probability figures.](../the-queue-chose-it-scene.jpg)

## Visible choices can conceal information

A crowded choice need not contain many independent observations. When people see earlier decisions but not the information behind them, sensible individual inference can produce an information cascade. A new independent observation can then matter more than several additional followers.

## Opening decision

In a fictional Hong Kong workshop fair, an adult must choose stall A or B. Exactly one delivers the better learning experience today; that state remains fixed. Prices, access, waiting time and capacity are identical. There is no benefit from joining friends and no penalty from a queue. Only choosing the better experience matters.

Before any signals, A and B are equally likely to be better. Each visitor privately receives either signal a or b. If A is better, a occurs with probability two-thirds; if B is better, b occurs with probability two-thirds. Signals are independent across visitors conditional on which stall is better.

Visitors act sequentially, observing all earlier choices but not earlier private signals. Everyone knows these probabilities and the decision rule: choose the stall with the higher updated probability of being better. At an exact tie, follow your own signal. Assume everyone follows this rule without errors and has no other information.

You advise the ninth visitor, whose private signal is b. The first two visitors chose A, then A. Choices three through eight have not yet been shown to you. Work first from the disclosed choices and the ninth visitor’s signal; do not invent undisclosed observations.

Use odds of A being better versus B being better. Equal starting probabilities mean odds 1:1. Each genuinely informative a signal multiplies these odds by 2; each b divides them by 2. Convert odds x:y into probability x/(x+y) for A. An action need not reveal a new signal.

## Evidence

| Item | Given |
| --- | --- |
| Initial quality odds A:B | 1:1 |
| Private signal accuracy | 2/3, symmetric |
| First two observed choices | A,A |
| Ninth visitor’s signal | b |
| Exact tie rule | Follow own signal |

**Student question:** After only the first visitor’s A choice and your own b signal, which stall would the stated tie rule select? With the first two choices A,A instead, what can you infer about those two signals, and which stall should the ninth visitor choose from the disclosed evidence?

## Round two

The record now shows that visitors three through eight also chose A. Their private signals remain unknown. All followed the stated rule. Separately, a newly available quality inspection favours B. The earlier visitors had not seen this inspection, and the underlying quality state has not changed.

Conditional on either stall being better, the inspection names that stall correctly with probability 90% and the other with probability 10%. Its result is independent of all visitor signals conditional on the quality state. Its authenticity and procedure are stipulated; it is not an infallible observation of the true state.

These are fictional common-knowledge probabilities, not estimated accuracy claims about actual fair visitors or inspectors. Choosing either stall creates no safety, payment or contractual difference in this exercise. Use the same objective and decision rule; first evaluate the extra choices, then incorporate the new inspection.

**Student question:** Do the six additional A choices supply six independent favourable signals? Calculate the ninth visitor’s probability assessment before and after the B-favouring inspection. Keep or change the recommendation, and explain why following the early visitors can be rational without making a long queue decisive evidence.

## Debrief · Recover only informative signals

The first visitor chooses A exactly when seeing a. With that single inferred a and your own b, the odds become 1 × 2 ÷ 2 = 1:1. The stated tie rule selects B. This is a hypothetical comparison using only the first choice, not the complete disclosed record.

The second visitor would choose B after seeing b: the first inferred a and their own b would tie. Therefore the observed second A reveals another a. Two inferred a signals give odds 4:1, or probability 4/5 that A is better, before the ninth visitor’s own information.

## Debrief · Add the private observation

The ninth visitor’s b divides the 4:1 odds by 2, leaving 2:1. Thus A has probability 2/3 and B probability 1/3. Choose A under the stipulated objective. A contrary private signal matters, but it does not outweigh the two informative earlier signals.

After A,A, a later visitor seeing b still assigns probability 2/3 to A; one seeing a assigns 8/9. Either chooses A. Consequently the third A does not distinguish that visitor’s private signal. The same reasoning repeats for visitors four through eight.

## Debrief · Count information, not followers

Conditional on the first two choices and the error-free rule, each subsequent A occurs regardless of whether A or B is actually better. Its likelihood ratio is 1, not 2. The six additional A choices leave the ninth visitor’s pre-inspection odds at 2:1 and probability for A at 2/3.

This is an information cascade: later actions stop revealing their private signals. No hidden signal values have been disclosed, and none may be counted. The sequence can favour the worse stall when the early signals are misleading, even though each visitor follows the agreed probability-maximising rule.

## Debrief · Use the genuinely new evidence

A B-favouring inspection occurs with probability 10% if A is better and 90% if B is better. Its likelihood ratio for A versus B is therefore 1/9. Multiply the existing 2:1 odds by 1/9 to obtain 2:9. A now has probability 2/11; B has probability 9/11, approximately 81.8%.

Change the recommendation to B. The posterior is not automatically 90%: it combines the inspection with the previously informative choices and the ninth visitor’s signal. Nor should eight A actions be multiplied as eight independent a signals. That would count information the later actions do not reveal.

## Debrief · Respect the model’s boundaries

The result depends on known signal quality, conditional independence, the own-signal tie rule, identical objectives and error-free behaviour. If people make mistakes, share information directly, see different signals or gain from company, later actions may convey different information. Real queues do not establish these assumptions merely by existing.

An alternative inspection correlated with the visitors’ information would not justify multiplying likelihood ratios as though independent. Ask where each observation came from and what would have produced it under either quality state. A larger number of visible decisions is not automatically a larger independent sample.

## Instructor note

Have students trace the second visitor’s two possible signals before calculating the ninth visitor’s posterior. Then ask whether the third visitor’s action changes across those signals. This makes the loss of information visible before introducing the stronger independent inspection.

ECO-29 concerns defaults and inferred preferences; IS-11 concerns voluntary survey response and missing customers. Here all actions are observed eventually, but their dependence on earlier actions makes them less informative than independent signals. The lesson is neither that crowds are always wrong nor that ignoring private information is always irrational.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

Entire workshop situation and signal/inspection rates are fictional. Exactly one better stall, fixed state, equal priors, identical objectives and costs, no direct social benefit or congestion. Error-free sequential choice with common knowledge, private symmetric accuracy2/3, conditional independence, own-signal tie-breaking. AA implies aa; prior odds4, own b yields2 and probabilityA2/3. Later A actions supply likelihood ratio1; no hidden later signal values released. Independent B inspection likelihood ratio1/9 yields oddsA:B2:9 and probabilityB9/11. Authentic procedure does not mean infallible state observation. Conditional independence, not unconditional independence, permits the likelihood multiplication. Sources supply concepts and explicitly differentiated models, not validation of fictional behaviour or rates.

- [Bikhchandani, Hirshleifer and Welch · A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades · 1992](https://snap.stanford.edu/class/cs224w-readings/bikhchandani92fads.pdf). Original research explains why actions can cease revealing private information and why new public information can interrupt a cascade. The case explicitly uses own-signal tie-breaking, rather than importing the paper’s random tie convention.
- [Kevin Dorst · Information Cascades · original teaching notes](https://www.kevindorst.com/uploads/8/8/1/7/88177244/bikchandani_et_al._1992_information_cascades.pdf). Author-created teaching develops a two-thirds signal example with own-signal tie-breaking. Used for transparent inference, not independent empirical confirmation of real visitors’ accuracy.
- [David Easley and Jon Kleinberg · Networks, Crowds, and Markets · Chapter 16: Information Cascades](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch16.pdf). Original textbook chapter distinguishes informational reasoning from direct benefits of matching others and explains why later choices can conceal private signals. The workshop and inspection are fictional.
- [Abhijit Banerjee · A Simple Model of Herd Behavior · 1992](https://economics.mit.edu/sites/default/files/publications/banerjee92herd.pdf). Original theoretical research explains how sequential imitation can limit the information reflected in choices. Its specific formal model is not the numerical model used here.
- [Lisa Anderson and Charles Holt · Information Cascades in the Laboratory · research manuscript for the 1997 study](https://econweb.ucsd.edu/~jandreoni/Econ264/papers/Holt%20Anderson%20AER%201997.pdf). Primary experimental paper presents a symmetric signal model, explicit tie assumptions and controlled private draws with replacement. Its experiment does not establish that actual workshop visitors behave without errors or that this fictional inspection has 90% accuracy.
