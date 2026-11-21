# Micro Cases in Business

Short classroom cases with an opening decision, a second-round prompt, a debrief, presentation slides, and a printable student handout. Open index.html to browse the collection. Cases now use area codes such as ACC-01 and HSP-01, with unchanged page URLs. Search by title, topic, code or original number; filter links retain the chosen view. See [numbering and the complete crosswalk](docs/case-numbering.md). Editable case materials and the authoring template are in authoring/.

The [original roadmap](planning/collection-roadmap.md) records the first 120 cases. The approved [expansion plan to 240](planning/expansion-to-240.md) adds cases 11–20 in each area, in ten balanced waves with research and review gates. The next approved [expansion plan to 360](planning/expansion-to-360.md) adds cases 21–30 in each area. The approved [expansion plan to 480](planning/expansion-to-480.md) adds cases 31–40 in each area. Planned cases are not counted as published.

The collection contains 493 cases: 48 in Finance, 45 in Economics and 40 in each of the other ten areas. The [finance and economics extension](planning/finance-economics-extension-490.md) adds FIN-41–45 and ECO-41–45, alternating at permanent IDs 481–490, to the completed balanced 480-case collection. The three subsequent Finance cases, FIN-46–48, use permanent IDs 491–493. Planned cases are not counted as published.

Identity fixtures protect all 490 baseline permanent IDs, area codes and URLs. Earlier snapshots are retained unchanged. The builder accepts sequential staged additions through ID 493, with Finance capped at 48 and Economics at 45 and every other area capped at 40.

## Acknowledgement

Cases 1–8, listed below, are based on teaching materials developed by Chiu Yu Ko with support from the "Innovation in Business Education, Business School, Chinese University of Hong Kong, 2024" award.

1. [Snow Town](snow-town.html)
2. [When the star sits out](match.html)
3. [The Shenzhen data puzzle](shenzhen.html)
4. [Crossing Victoria Harbour](tunnel.html)
5. [The checkout bag](bag.html)
6. [The missing rubbish](waste.html)
7. [The red minibus bid](minibus.html)
8. [The offer expires Friday](exam.html)

## Cases 9–16

9. [The last tray of egg tarts](tarts.html)
10. [Who gets the last badminton court?](court.html)
11. [Would you share a ten-trip ferry pass?](ferry-pass.html)
12. [The phone with a fresh battery](battery.html)
13. [Two cafés, one lunch rush](cafes.html)
14. [Who funds the covered walkway?](walkway.html)
15. [Pay per parcel?](parcel.html)
16. [One stall, one bid](stall.html)

## Case 17

17. [Sold out by noon. Double tomorrow?](sold-out.html)

## Case 18

18. [The biggest order, the smallest cash balance](cash-flow.html)

## Case 19

19. [A thousand coupons. A better business?](coupon.html)

## Case 20

20. [The best seller. The best supervisor?](supervisor.html)

## Case 21

21. [A bigger market. Whose customers?](distributor.html)

## Case 22

22. [The warning changed. Did customers notice?](customer-notice.html)

## Case 23

23. [Would you sell the family name?](family-name.html)

## Case 24

24. [Close the loss-making branch?](branch-loss.html)

## Case 25

25. [A room is ready. Is the guest’s trip restored?](replacement-room.html)

Published cases are listed here; the planning ledger records current totals and teaching-area coverage.

## Self-contained classroom reading

Keep external links in the optional sources section only. The opening, exhibits, questions, presentation slides and handout must provide the facts students need without asking them to open a report. Preserve source attribution and distinguish reported facts from classroom assumptions.

Run `python tests/check_case_links.py` to check this convention across all published cases and editable case materials. Run `python tests/check_collection.py` to verify collection links, artwork, editable files and coverage totals.

## Illustration style

Follow the [art direction and production guide](docs/art-direction.md) for every new or revised case illustration. Preserve the established watercolor-and-ink narrative style.

## Decision-question highlighting

Every opening and round-two decision must use the highlighted **Your decision** box on both the page and its presentation slide. Follow the [required question-format guide](docs/decision-questions.md), and run `python tests/check_decision_prompts.py` before publishing.

## Case 26

26. [97% right. Ready to reply?](chatbot.html)

## Case 27

27. [Fly the whole order, or just what is missing?](split-shipment.html)

## Case 28

28. [They like the prototype. Will they buy it?](paid-pilot.html)

## Case 29

29. [No booking fee. A lower price?](booking-fee.html)

## Case 30

30. [Target reached. Returns still coming?](returns-target.html)

## Case 31

31. [They remember the character. Do they remember us?](character-collaboration.html)

## Case 32

32. [The best quote. The right reviewer?](supplier-review.html)

## Case 33

33. [The cheaper batch and the prototype bench](prototype-bench.html)

## Case 34

34. [A faster machine. More finished boxes?](packing-line.html)

## Case 35

35. [The backup is green. Can the shop work again?](recovery-rehearsal.html)

## Case 36

36. [The big client wants its own version](separate-version.html)

## Case 37

37. [One busy night. Two nights of business.](two-night-stays.html)

## Case 38

38. [The invoice is not the exposure](invoice-exposure.html)

## Case 39

39. [The handbook is complete. Are they ready?](ready-for-handoff.html)

## Case 40

40. [The stock is all there. Is it worth the same?](count-and-value.html)

## Case 41

41. [More days to return it, or less trouble?](return-friction.html)

## Case 42

42. [Fewer changeovers. A later customer.](mixed-collection.html)

## Case 43

43. [Export the product, or export the promise?](portable-promise.html)

## Case 44

44. [Two approvals. One source.](one-source.html)

## Case 45

45. [Twenty per cent less. Less of what?](less-of-what.html)

## Case 46

46. [They did not come. Did they try to cancel?](unread-cancellation.html)

## Case 47

47. [Fewer sales. A worse price?](fewer-jobs.html)

## Case 48

48. [HK$60,000 of support. Can we use it?](usable-support.html)

## Teaching-area browsing

Use Teaching area, Business topic and Class time available together, or Reset filters to show all cases. Primary areas follow the coverage ledger; secondary concepts remain in the topic menu. When adding a case, update its `data-discipline` and visible `.discipline` label to match the ledger, then run `python tests/check_disciplines.py` alongside the other checks.

## Case 49

49. [Reusable fifty times. Used how many?](actually-reused.html)

## Case 50

50. [A larger limit. The same gap?](same-gap.html)

## Case 51

51. [Four times the reports. Four times the mistakes?](more-reports.html)

## Case 52

52. [Over budget. Out of control?](over-budget.html)

## Case 53

53. [The file arrived. What did we order?](order-units.html)

## Case 54

54. [No commission. No acquisition cost?](direct-cost.html)

## Case 55

55. [Two suppliers. One factory?](shared-factory.html)

## Case 56

56. [A birthday offer. A full birth date?](birthday-fields.html)

## Case 57

57. [A slow seller. An important basket?](small-basket.html)

## Case 58

58. [Equal partners. Earned when?](founder-timing.html)

## Case 59

59. [One hundred couriers. One hundred matches?](local-matches.html)

## Case 60

60. [Two hundred clients. Two hundred new clients?](combined-clients.html)

## Case 61

61. [Paid today. Earned today?](paid-earned.html)

## Case 62

62. [Smaller payments. Cheaper loan?](smaller-payments.html)

## Case 63

63. [More contacts. More customers?](qualified-contacts.html)

## Case 64

64. [Keep running, or stop on purpose?](planned-stop.html)

## Case 65

65. [Choose your days. Coordinate your work.](shared-time.html)

## Case 66

66. [Share the studio. Share the advantage?](shared-advantage.html)

## Case 67

67. [Eighty kilos wasted. Eighty kilos to donate?](edible-surplus.html)

## Case 68

68. [Keep it secret. For how long?](visible-secret.html)


## Case 69

69. [Faster at both. Do both?](faster-at-both.html)


## Case 70

70. [Same seats. Same capacity?](table-mix.html)


## Case 71

71. [A good forecast. Available when?](forecast-cutoff.html)


## Case 72

72. [Three small orders. One big commitment?](one-commitment.html)


## Case 73

73. [One machine invoice. One asset cost?](machine-cost.html)


## Case 74

74. [A discount for paying sooner. Sooner than what?](sooner-than-what.html)


## Case 75

75. [Designed for an age group. Chosen by whom?](chosen-by-whom.html)


## Case 76

76. [An empty counter. A waiting customer.](empty-counter.html)


## Case 77

77. [A realistic test. The right skill?](right-skill.html)


## Case 78

78. [Four signs. One business system?](repeatable-format.html)


## Case 79

79. [Funded. What should we promise next?](next-promise.html)


## Case 80

80. [More people reached. More people helped?](reached-and-helped.html)


## Case 81

81. [A quiet pilot. Enough to learn?](first-rollout.html)

## Case 82

82. [A supplier failed. Must the relationship end?](credible-improvement.html)

## Case 83

83. [A cheaper delivery. Cheaper for whom?](cheaper-for-whom.html)

## Case 84

84. [A faster lunch. Which part should be faster?](meal-pace.html)

## Case 85

85. [A quiet year. Less machine used?](machine-hours.html)

## Case 86

86. [Back sooner. Worth more?](back-sooner.html)

## Case 87

87. [A fresher pack. Still easy to find?](familiar-pack.html)

## Case 88

88. [Check it again. Or make the mistake harder?](harder-to-miss.html)

## Case 89

89. [More variety. More ownership?](whole-job.html)

## Case 90

90. [One forecast. Three strategies?](more-than-one-future.html)

## Case 91

91. [Sell the product. Or license the invention?](route-to-market.html)

## Case 92

92. [A better system. A harder exit?](better-system-harder-exit.html)

## Case 93

93. [No name. No conversation?](no-name-still-a-conversation.html)

## Case 94

94. [The landlord pays. Who saves?](landlord-pays-who-saves.html)

## Case 95

95. [A package deal. Must everyone buy both?](both-or-one.html)

## Case 96

96. [One exhibit. More than one way in.](more-than-one-way-in.html)

## Case 97

97. [Two balances. One payment.](two-balances-one-payment.html)

## Case 98

98. [One bank. Two kinds of safety.](protected-and-available.html)

## Case 99

99. [A smaller audience. More new people?](more-new-people.html)

## Case 100

100. [Print now. Or keep the design open?](keep-the-design-open.html)

## Case 101

101. [Separate the colleagues. Or repair the handoff?](repair-the-handoff.html)

## Case 102

102. [A premium offer. The same business?](same-business.html)

## Case 103

103. [A new leader. Who still decides?](who-still-decides.html)

## Case 104

104. [A fresher screen. A better decision?](fresher-screen.html)

## Case 105

105. [Externally checked. What was checked?](what-was-checked.html)

## Case 106

106. [A bigger order. More mission?](bigger-order-more-mission.html)

## Case 107

107. [Five per cent more. More of what?](more-money-more-kits.html)

## Case 108

108. [A busy reception. Useful conversations?](useful-conversations.html)

## Case 109

109. [Through our till. All our revenue?](through-our-till.html)

## Case 110

110. [Twenty per cent. Only once?](only-once.html)

## Case 111

111. [More to choose. Easier to choose?](easier-to-choose.html)

## Case 112

112. [Within specification. Still the same process?](same-process.html)

## Case 113

113. [A higher target. A clearer method?](clearer-method.html)

## Case 114

114. [One large customer. Too much dependence?](anchor-customer.html)

## Case 115

115. [Keep the job. Start the business?](keep-the-job.html)

## Case 116

116. [Two versions. Two separate groups?](separate-groups.html)

## Case 117

117. [The smaller average loss. The bigger risk?](bigger-risk.html)

## Case 118

118. [Repair the chair. Replace which part?](replace-which-part.html)

## Case 119

119. [Covered damage. Unchanged behaviour?](covered-damage.html)

## Case 120

120. [A village tour. Whose story?](whose-story.html)

## ACC-11

121. [Same units. Same overhead?](same-units-different-setups.html)

## FIN-11

122. [A lower rate. A less certain payment?](lower-rate-less-certainty.html)

## MKT-11

123. [A promise of expertise. What can buyers see?](see-the-advice.html)

## OPS-11

124. [Plenty on the shelf. Time to reorder?](time-to-reorder.html)

## PPL-11

125. [A strong finish. A strong year?](strong-finish-strong-year.html)

## STR-11

126. [Keep improving it. Or harvest what remains?](what-remains.html)

## ENT-11

127. [The impressive co-founder. The complementary co-founder?](complementary-founder.html)

## IS-11

128. [Most respondents liked it. Most customers?](respondents-or-customers.html)

## GVR-11

129. [The meeting agreed. Which version applies?](which-version.html)

## SUS-11

130. [Compostable here. Collected where?](collected-where.html)

## ECO-11

131. [A profitable day. One more hour?](one-more-hour.html)

## HSP-11

132. [A cancellation forecast. Another promise?](another-promise.html)

## ACC-12

133. [The best margin. Per what?](margin-per-minute.html)

## FIN-12

134. [Rent the equipment. Keep the exit?](rent-and-exit.html)

## MKT-12

135. [Many visits. Where does the journey break?](where-journey-breaks.html)

## OPS-12

136. [Two stores. One safety stock?](stock-is-not-ready.html)

## PPL-12

137. [Fill the vacancy. Explain the difficult part?](explain-the-difficult-part.html)

## STR-12

138. [A dedicated tool. A dependable agreement?](dedicated-tool.html)

## ENT-12

139. [Better ratings. The same business?](better-for-whom.html)

## IS-12

140. [A blank cell. A harmless average?](blank-cell.html)

## GVR-12

141. [Delete on schedule. Preserve an exception?](preserve-an-exception.html)

## SUS-12

142. [The same electricity. A different time?](same-energy-different-time.html)

## ECO-12

143. [The highest estimate. The best bid?](winning-is-information.html)

## HSP-12

144. [They can read the map. Can they find the entrance?](find-the-entrance.html)

## ACC-13

145. [Cheaper material. A dearer batch?](cheaper-material-dearer-batch.html)

## FIN-13

146. [The invoice is sold. Is the risk gone?](cash-before-risk.html)

## MKT-13

147. [Our biggest customer. Our most valuable relationship?](valuable-relationship.html)

## OPS-13

148. [Promise Friday. Based on which stock?](promise-by-when.html)

## PPL-13

149. [The same leave entitlement. The same fair process?](same-leave-fair-process.html)

## STR-13

150. [Open first. Be ready first?](open-before-the-network.html)

## ENT-13

151. [Ask the people we know. Meet the people they do not know?](beyond-familiar-contacts.html)

## IS-13

152. [Better in both groups. Worse overall?](same-mix-different-answer.html)

## GVR-13

153. [The score flagged the refund. Who can review it?](flag-and-review.html)

## SUS-13

154. [A litre saved. In which place?](a-litre-in-which-place.html)

## ECO-13

155. [A promise of quality. Costly for whom?](promise-costs.html)

## HSP-13

156. [A tidy room. An unwanted interruption?](a-window-not-any-time.html)

## ACC-14

157. [An invoice issued. Cash likely?](an-invoice-not-a-receipt.html)

## FIN-14

158. [Rising cash flows. The same discount rate?](same-money-same-rate.html)

## MKT-14

159. [The same price. Two comparisons.](same-price-two-comparisons.html)

## OPS-14

160. [A shorter route. A missed window?](route-and-window.html)

## PPL-14

161. [A market-rate recruit. An overlooked colleague?](market-rate-existing-colleague.html)

## STR-14

162. [Own the operation. Share the local knowledge?](own-or-share-the-operation.html)

## ENT-14

163. [Sell now. Stay to build?](sell-now-stay-to-build.html)

## IS-14

164. [Accurate alerts. Useful alerts?](accurate-alerts-useful-alerts.html)

## GVR-14

165. [A training visit. A supplier’s holiday?](training-not-a-holiday.html)

## SUS-14

166. [A cooler courtyard. Ready for a hotter summer?](shade-now-shade-later.html)

## ECO-14

167. [A low visit price. A high-use member?](entry-fee-extra-visit.html)

## HSP-14

168. [Follow the script. Recognise the occasion?](script-and-occasion.html)

## ACC-15

169. [A profit. Where did the cash go?](profit-not-cash.html)

## FIN-15

170. [One company. One hurdle rate?](one-company-one-hurdle.html)

## MKT-15

171. [The same benefit. A different frame?](same-benefit-different-frame.html)

## OPS-15

172. [Returned and checked. Where next?](returned-checked-where-next.html)

## PPL-15

173. [The reliable choice. The only person who gets a chance?](who-gets-a-chance.html)

## STR-15

174. [Three nearby outlets. Three different cities?](nearby-or-three-cities.html)

## ENT-15

175. [Equal votes. No decision?](equal-votes-no-decision.html)

## IS-15

176. [Challenge the forecast. Who may override it?](challenge-and-authorise.html)

## GVR-15

177. [We bought the photograph. May we reuse it?](paid-for-which-use.html)

## SUS-15

178. [More trees. Better habitat?](more-trees-better-habitat.html)

## ECO-15

179. [A cheaper printer. More expensive printing?](printer-and-printing.html)

## HSP-15

180. [Decide before guests travel. Or wait?](before-guests-travel.html)

## ACC-16

181. [A small payment. An important correction?](small-but-in-the-note.html)

## FIN-16

182. [Two income streams. One bad month?](cash-moves-together.html)

## MKT-16

183. [A new pack. New sales?](new-pack-new-sales.html)

## OPS-16

184. [Keep every station busy. Finish orders sooner?](started-is-not-finished.html)

## PPL-16

185. [One expert. Who else can cover?](someone-else-can-cover.html)

## STR-16

186. [Join the standard. Keep the distinctive feature?](compatible-with-what.html)

## ENT-16

187. [Many possible users. One first market?](one-first-market.html)

## IS-16

188. [The same average error. The same business cost?](same-error-different-loss.html)

## GVR-16

189. [One exception. A fair rule?](same-exception-same-reasons.html)

## SUS-16

190. [Online first. A service for everyone?](a-booking-not-just-a-button.html)

## ECO-16

191. [One more quotation. Worth the search?](one-more-quotation.html)

## HSP-16

192. [Lively to one table. Too loud to another?](a-room-for-this-conversation.html)

## ACC-17

193. [Most of the value. Enough of the evidence?](coverage-is-not-a-population.html)

## FIN-17

194. [More credit. A tighter promise?](cheaper-credit-tighter-promise.html)

## MKT-17

195. [They want everything. What will they trade?](which-improvement-would-you-give-up.html)

## OPS-17

196. [Steady output. Or follow the peak?](steady-output-later-peak.html)

## PPL-17

197. [Everyone agrees. Has everyone’s evidence been heard?](whose-evidence-reached-the-table.html)

## STR-17

198. [Defend every customer. Defend the right position?](defend-the-position-not-every-price.html)

## ENT-17

199. [A venture plan. Which partners help shape it?](partners-change-the-opportunity.html)

## IS-17

200. [Easy access. Appropriate access?](cover-the-task-not-every-permission.html)

## GVR-17

201. [A new policy. Effective from when?](the-date-that-changes-the-rule.html)

## SUS-17

202. [Many volunteers. A dependable service?](cover-the-service-not-the-signup-count.html)

## ECO-17

203. [We will launch if you do.](ready-only-if-both-are-ready.html)

## HSP-17

204. [Keys handed over. Ready to move in?](keys-are-not-a-completion-record.html)

## ACC-18

205. [Keep the budget. Update the forecast?](one-target-two-views.html)

## FIN-18

206. [Earn more interest. Available on which day?](cash-on-the-day-it-is-needed.html)

## MKT-18

207. [More reminders. More relationships?](permission-is-not-a-message-quota.html)

## OPS-18

208. [Customer demand moved a little. Orders moved a lot.](orders-are-not-consumption.html)

## PPL-18

209. [More people to lead. The same manager’s day?](count-the-work-not-only-the-reports.html)

## STR-18

210. [The rival across the road. Or a different way to meet the need?](another-way-to-spend-the-evening.html)

## ENT-18

211. [It worked in the last business. Will the routine travel?](will-the-routine-travel.html)

## IS-18

212. [The feature is delivered. Is the work supported?](features-pass-work-still-waits.html)

## GVR-18

213. [A useful industry meeting. Which topics are off limits?](keep-the-meeting-in-bounds.html)

## SUS-18

214. [Residents will vote. Who can get onto the ballot?](who-can-shape-the-ballot.html)

## ECO-18

215. [The shared resource is open. Will it last?](ready-stock-is-not-endless.html)

## HSP-18

216. [The highest rent. The right neighbour?](rent-is-not-the-whole-site.html)

## ACC-19

217. [A lower return. A better investment?](lower-return-better-investment.html)

## FIN-19

218. [The best project. The best set of projects?](best-project-best-package.html)

## MKT-19

219. [One name for two promises?](one-name-two-promises.html)

## OPS-19

220. [Straight through the depot. Or onto a shelf?](through-the-depot-or-to-a-shelf.html)

## PPL-19

221. [Lose a team member. Keep a colleague?](lose-a-team-member-keep-a-colleague.html)

## STR-19

222. [The next market. The next missing capability?](next-market-missing-capability.html)

## ENT-19

223. [Start a business. Or buy one to run?](start-a-business-buy-one-to-run.html)

## IS-19

224. [One switch-over. Two records to reconcile?](one-switch-two-records.html)

## GVR-19

225. [The board agreed. Did it record the conditions?](board-agreed-record-the-conditions.html)

## SUS-19

226. [A carbon project. Would it happen anyway?](carbon-project-happen-anyway.html)

## ECO-19

227. [A price cap. Which shortage remains?](price-cap-shortage-remains.html)

## HSP-19

228. [Ten minutes to wait. Ten minutes without knowing?](ten-minutes-without-knowing.html)

## ACC-20

229. [An internal price. Two sensible refusals?](internal-price-two-refusals.html)

## FIN-20

230. [A good year. A distributable surplus?](good-year-distributable-surplus.html)

## MKT-20

231. [Points earned. Benefits understood?](points-earned-benefits-understood.html)

## OPS-20

232. [Count everything twice. Or risky shelves more often?](count-the-risky-shelves.html)

## PPL-20

233. [The instruction is clear. Whose example changes the habit?](whose-example-changes-the-habit.html)

## STR-20

234. [One network. Every decision at headquarters?](one-network-local-decisions.html)

## ENT-20

235. [Stop the venture. Keep the promise?](stop-the-venture-keep-the-promise.html)

## IS-20

236. [A persuasive dashboard. Can we trace the number?](trace-the-number-not-only-the-chart.html)

## GVR-20

237. [An incident declared. Who is directing the response?](one-response-clear-authority.html)

## SUS-20

238. [The pilot grant ends. Who maintains the benefit?](fund-the-years-after-opening.html)

## ECO-20

239. [Two sellers merge. Which competition disappears?](the-rival-customers-would-choose.html)

## HSP-20

240. [One booking. Several different visits?](one-booking-different-visits.html)

## ACC-21

241. [Two products. Which cost changes?](two-products-which-cost-changes.html)

## FIN-21

242. [Same yield. Same interest-rate risk?](same-yield-different-duration.html)

## MKT-21

243. [One customer. Which channel earns the sale?](one-customer-which-channel.html)

## OPS-21

244. [Enough components. Ready in the right week?](components-ready-in-the-right-week.html)

## PPL-21

245. [Useful feedback. Useful to do what?](useful-feedback-useful-to-do-what.html)

## STR-21

246. [Follow the plan. Recognise a better pattern?](follow-the-plan-recognise-the-pattern.html)

## ENT-21

247. [The clever solution. The costly problem?](clever-solution-costly-problem.html)

## IS-21

248. [The number improved. Beyond ordinary variation?](improvement-beyond-ordinary-variation.html)

## GVR-21

249. [A cheap contract. An uncapped exposure?](cheap-contract-uncapped-exposure.html)

## SUS-21

250. [A more efficient device. Less total energy?](efficient-device-total-energy.html)

## ECO-21

251. [A lower price for some. Can the groups stay separate?](lower-price-groups-stay-separate.html)

## HSP-21

252. [The room is larger. Does it feel usable?](room-features-usable-space.html)

## ACC-22

253. [More production. More profit?](more-production-more-profit.html)

## FIN-22

254. [Commit now. Pay for the option to wait?](pay-for-time-to-decide.html)

## MKT-22

255. [The last click. The whole contribution?](last-click-whole-contribution.html)

## OPS-22

256. [Shorten the longest task. Finish the project sooner?](shorten-the-task-or-the-project.html)

## PPL-22

257. [A disagreement over pay. Or over the package?](different-priorities-better-package.html)

## STR-22

258. [A copied product. A copied advantage?](copy-the-product-copy-the-advantage.html)

## ENT-22

259. [Enough pledges. Enough capacity to fulfil?](enough-pledges-enough-capacity.html)

## IS-22

260. [One winning result. How many chances to win?](one-winner-many-comparisons.html)

## GVR-22

261. [A complaint upheld. Is retaliation prevented?](complaint-upheld-protection-continues.html)

## SUS-22

262. [Cash support. Or the goods people need?](cash-choice-goods-available.html)

## ECO-22

263. [Two markups. One final customer?](two-markups-one-final-customer.html)

## HSP-22

264. [The same occupied nights. The same cleaning workload?](same-nights-more-departures.html)

## ACC-23

265. [On the truck. In whose year-end stock?](on-the-truck-in-whose-stock.html)

## FIN-23

266. [No price today. No dilution tomorrow?](unpriced-not-ownership-free.html)

## MKT-23

267. [Better taste. Or a different expectation?](better-taste-different-expectation.html)

## OPS-23

268. [One shared line. Who can serve the next ticket?](next-ticket-next-eligible-ticket.html)

## PPL-23

269. [One team bonus. Whose contribution is visible?](one-team-bonus-visible-contribution.html)

## STR-23

270. [A profitable division. A useful parent?](profitable-division-useful-parent.html)

## ENT-23

271. [Use what is available. Build what is repeatable?](available-resources-repeatable-service.html)

## IS-23

272. [The worst branches improved. Did coaching work?](lowest-score-next-month.html)

## GVR-23

273. [The evidence exists. Can its history be shown?](evidence-exists-history-shown.html)

## SUS-23

274. [Just above the threshold. No help at all?](small-raise-large-withdrawal.html)

## ECO-23

275. [Better wages. More than a higher cost?](better-wages-more-than-higher-cost.html)

## HSP-23

276. [A beautiful display. An easy meal to assemble?](see-the-dish-build-the-meal.html)

## ACC-24

277. [Expected repairs. Already a liability?](expected-repairs-already-liability.html)

## FIN-24

278. [A lower premium. How much risk stays here?](lower-premium-repeated-deductible.html)

## MKT-24

279. [Preferred when compared. Never on the shortlist?](preferred-compared-never-shortlist.html)

## OPS-24

280. [A bulk discount. A lower total stocking cost?](bulk-price-total-stock-cost.html)

## PPL-24

281. [Reward the suggestion. Change the reason for suggesting?](reward-suggestion-change-reason.html)

## STR-24

282. [Compete in sales. Cooperate in the foundation?](common-training-separate-businesses.html)

## ENT-24

283. [Paid for the work. Paid for the result?](paid-work-paid-result.html)

## IS-24

284. [The same customer. Two different records?](same-customer-different-records.html)

## GVR-24

285. [Permission for service. Permission for research?](permission-service-permission-research.html)

## SUS-24

286. [Cleaner here. Dirtier somewhere else?](outside-site-not-outside-impact.html)

## ECO-24

287. [Split the surplus. Compare which alternative?](split-surplus-compare-alternative.html)

## HSP-24

288. [More reviews. A more trustworthy picture?](review-history-current-offer.html)

## ACC-25

289. [Depreciated on schedule. Still worth carrying?](depreciated-schedule-worth-carrying.html)

## FIN-25

290. [Payment promised. Documents accepted?](shipment-complete-documents-complying.html)

## MKT-25

291. [Advertise every week. Or be present at the moment?](every-week-present-moment.html)

## OPS-25

292. [The most units sold. The most trips walked?](units-sold-trips-walked.html)

## PPL-25

293. [Two reasonable managers. One impossible instruction?](two-managers-one-workday.html)

## STR-25

294. [A better product. Who will install it?](better-product-missing-installer.html)

## ENT-25

295. [Every customer gets the founder. Can the business grow?](founder-at-the-right-moment.html)

## IS-25

296. [Recorded at noon. Happened at noon?](recorded-at-noon-happened-at-noon.html)

## GVR-25

297. [A different team. Reviewing whose work?](different-team-same-firms-work.html)

## SUS-25

298. [The cheapest green purchase. Over which lifetime?](cheaper-now-through-the-service-life.html)

## ECO-25

299. [Buy today. Wait for tomorrow’s discount?](buy-today-wait-for-the-discount.html)

## HSP-25

300. [The festival fills the town. Does the town benefit?](festival-spending-stays-local.html)

## ACC-26

301. [A group sale. A group profit?](a-group-sale-a-group-profit.html)

## FIN-26

302. [Cash flows continue. How much is the ending worth?](cash-flows-continue-ending-worth.html)

## MKT-26

303. [A lower price. A clearer customer business case?](same-price-clearer-customer-value.html)

## OPS-26

304. [Ninety-eight per cent at every stage. What leaves the line?](same-pass-rate-different-flow.html)

## PPL-26

305. [A slower colleague. Or a harder queue?](slower-colleague-harder-queue.html)

## STR-26

306. [One global product. One global learning direction?](local-design-global-learning.html)

## ENT-26

307. [Endorsed by whom. Credible to whom?](endorsed-by-whom-credible-to-whom.html)

## IS-26

308. [Two confirmations. One order?](two-confirmations-one-order.html)

## GVR-26

309. [A dispute pending. What can still continue?](dispute-pending-service-continuing.html)

## SUS-26

310. [A better transition. For whom, and when?](transition-jobs-between-dates.html)

## ECO-26

311. [Same target. Same reduction at every plant?](same-cap-different-reductions.html)

## HSP-26

312. [The check-in works. Does the handoff work?](confirmed-here-missed-there.html)

## ACC-27

313. [The result improved. Which warning was missed?](result-improved-warning-missed.html)

## FIN-27

314. [A credit limit. How much can we draw?](credit-limit-available-draw.html)

## MKT-27

315. [A smaller price tag. A cheaper quantity?](smaller-pack-cheaper-quantity.html)

## OPS-27

316. [Short supply. Which allocation keeps promises?](short-shipment-which-allocation.html)

## PPL-27

317. [Flexible for the business. Predictable for the team?](flexible-business-predictable-team.html)

## STR-27

318. [One acquisition. One operating system?](one-acquisition-one-operating-system.html)

## ENT-27

319. [Learn from one experiment. Keep the learning comparable?](one-experiment-comparable-learning.html)

## IS-27

320. [The sensor is consistent. Is it measuring correctly?](consistent-sensor-correct-measurement.html)

## GVR-27

321. [Within every limit. Outside the overall boundary?](local-limits-shared-exposure.html)

## SUS-27

322. [Restore later. Lose something now?](restore-later-not-reversible.html)

## ECO-27

323. [More effort. No larger prize.](winning-effort-vanishing-prize.html)

## HSP-27

324. [Three landmarks, or one connected story?](fewer-stops-clearer-story.html)

## ACC-28

325. [A market price. A design cost gap?](market-price-design-cost-gap.html)

## FIN-28

326. [The hedge moves. Does it move with our cost?](hedge-moves-delivered-cost.html)

## MKT-28

327. [They understand the benefit. Can they picture doing it?](understand-benefit-picture-setup.html)

## OPS-28

328. [Reserve capacity. Commit to every unit?](reserve-capacity-commit-units.html)

## PPL-28

329. [A cheerful greeting. At what emotional cost?](cheerful-greeting-emotional-cost.html)

## STR-28

330. [Enter the attractive segment. Cross which barrier?](attractive-segment-mobility-barrier.html)

## ENT-28

331. [A family successor. A fair path into responsibility?](family-successor-fair-path.html)

## IS-28

332. [The line looks dramatic. What does the axis say?](dramatic-line-axis-context.html)

## GVR-28

333. [Stop the work. Who may restart it?](stopped-until-cleared.html)

## SUS-28

334. [A neighbourhood improved. Who can still stay?](better-place-same-people.html)

## ECO-28

335. [Choose freely now. Restrict a future choice?](chosen-lock-unexpected-need.html)

## HSP-28

336. [A full appointment book. A workable morning?](booked-time-shared-room.html)

## ACC-29

337. [One package price. Three promises?](one-package-three-promises.html)

## FIN-29

338. [The same ownership. The same exit proceeds?](same-ownership-different-exit.html)

## MKT-29

339. [Resolve one complaint. Reassure which audience?](private-remedy-public-reassurance.html)

## OPS-29

340. [Ninety-five per cent service. Of what?](service-percentage-which-denominator.html)

## PPL-29

341. [A project ends. What does the team learn?](project-ends-team-learning.html)

## STR-29

342. [Improve the current model. Protect a different one?](current-model-different-unit.html)

## ENT-29

343. [An internal idea. An independent venture?](internal-idea-independent-venture.html)

## IS-29

344. [Assigned to the pilot. Actually using it?](assigned-pilot-actual-use.html)

## GVR-29

345. [A high average accuracy. An uneven burden?](accurate-for-whom.html)

## SUS-29

346. [A benefit far away. Less valuable to whom?](later-benefit-present-choice.html)

## ECO-29

347. [The default stays. Is it the preferred choice?](still-enrolled-still-preferred.html)

## HSP-29

348. [A fair recovery. Must it be identical?](same-entitlement-different-remedy.html)

## ACC-30

349. [A healthier ratio. A healthier business?](ratio-rises-cash-falls.html)

## FIN-30

350. [Affordable interest. A repayable principal?](interest-paid-principal-due.html)

## MKT-30

351. [One customer profile. Two shopping missions?](same-shoppers-different-missions.html)

## OPS-30

352. [One production lot. One recall boundary?](one-lot-shared-ingredient.html)

## PPL-30

353. [Nothing in the contract changed. Did the promise?](contract-unchanged-promise-changed.html)

## STR-30

354. [A stronger position. For how long?](stronger-position-for-how-long.html)

## ENT-30

355. [One venture story. Several testable assumptions?](venture-story-testable-assumptions.html)

## IS-30

356. [A summary alone. Or bounded retrieval?](summary-or-bounded-retrieval.html)

## GVR-30

357. [The supplier promises compliance. Who remains accountable?](delegated-work-retained-accountability.html)

## SUS-30

358. [A new safeguard. Who helps decide when it changes?](trigger-to-review-not-to-build.html)

## ECO-30

359. [A better private deal. A cost outside the contract?](outside-the-quiet-deal.html)

## HSP-30

360. [A busy season. A destination all year?](rooms-without-a-destination.html)

## ACC-31

361. [Half finished. How many units of work?](half-finished-units-of-work.html)

## FIN-31

362. [A higher percentage. More value created?](higher-percentage-more-value.html)

## MKT-31

363. [The same sales. A smaller buyer base?](same-sales-smaller-buyer-base.html)

## OPS-31

364. [The truck is half empty. Is there room?](half-empty-is-there-room.html)

## PPL-31

365. [We trained them. Can they use it?](trained-them-can-they-use-it.html)

## STR-31

366. [Control the core. Design every extension?](control-the-core-design-every-extension.html)

## ENT-31

367. [Enthusiasts love it. Can ordinary buyers adopt it?](enthusiasts-love-it-ordinary-buyers-adopt-it.html)

## IS-31

368. [Trained on yesterday. Useful for tomorrow?](trained-on-yesterday-useful-for-tomorrow.html)

## GVR-31

369. [The board has information. Does it have time to challenge?](information-without-challenge.html)

## SUS-31

370. [Lower carbon. A heavier water footprint?](lower-carbon-heavier-water-footprint.html)

## ECO-31

371. [The average quality. Who still sells?](average-quality-who-sells.html)

## HSP-31

372. [Fewer bookings today. Behind the booking curve?](fewer-bookings-behind-the-curve.html)

## ACC-32

373. [Rejects. Which loss belongs in stock?](rejects-which-loss-belongs-in-stock.html)

## FIN-32

374. [More return on equity. More risk to equity?](more-return-more-equity-risk.html)

## MKT-32

375. [A generous referral. A trustworthy recommendation?](same-reward-different-recipient.html)

## OPS-32

376. [First in. First to expire?](first-in-first-to-expire.html)

## PPL-32

377. [Someone knows. Who knows who?](someone-knows-who-knows-who.html)

## STR-32

378. [On both platforms. Loyal to neither?](on-both-platforms.html)

## ENT-32

379. [The investor brings customers. Which customers may we serve?](investor-access-commercial-freedom.html)

## IS-32

380. [A positive average. The same rollout for everyone?](positive-average-same-rollout.html)

## GVR-32

381. [A donation is generous. Whose interests does it serve?](generous-donation-whose-benefit.html)

## SUS-32

382. [A clean recycling stream. One contaminated load?](one-contaminated-load.html)

## ECO-32

383. [Two plans. Who chooses which one?](two-plans-who-chooses.html)

## HSP-32

384. [The rooms stay open. Can the stay still work?](open-rooms-unavailable-purpose.html)

## ACC-33

385. [The sales target is met. Are the costs covered?](same-revenue-different-break-even.html)

## FIN-33

386. [A business price. A price for the shares?](business-price-share-price.html)

## MKT-33

387. [A free trial. Enough time to experience the benefit?](free-trial-time-to-experience.html)

## OPS-33

388. [A sample passed. Did the shipment pass?](sample-passed-shipment-passed.html)

## PPL-33

389. [Strong inside. Disconnected outside.](strong-inside-disconnected-outside.html)

## STR-33

390. [Larger factory. Lower cost from what?](larger-factory-lower-cost-from-what.html)

## ENT-33

391. [A patent to use. Freedom to sell?](patent-to-use-freedom-to-sell.html)

## IS-33

392. [Averages are stable. What happens on the worst days?](same-average-different-tail.html)

## GVR-33

393. [The terms are disclosed. Are they understood?](terms-disclosed-terms-understood.html)

## SUS-33

394. [A useful by-product. A dependable input?](useful-heat-dependable-supply.html)

## ECO-33

395. [A tax on the seller. Who pays in the end?](seller-tax-who-bears-it.html)

## HSP-33

396. [An upgrade accepted. The right room left unsold?](upgrade-accepted-right-room-unsold.html)

## ACC-34

397. [A useful prototype. An asset already?](useful-prototype-recognition-date.html)

## FIN-34

398. [A guaranteed loan. Whose future cash?](guaranteed-loan-future-cash.html)

## MKT-34

399. [The same message. Who must agree?](same-message-who-must-agree.html)

## OPS-34

400. [Equal work. A balanced line?](equal-work-balanced-line.html)

## PPL-34

401. [One company. Two identities.](one-company-two-identities.html)

## STR-34

402. [A strong threat. A costly commitment?](strong-threat-costly-commitment.html)

## ENT-34

403. [A large market. A reachable first business?](large-market-reachable-business.html)

## IS-34

404. [A model improved. Is the target still the same?](model-improved-target-changed.html)

## GVR-34

405. [The customer is unhappy. Is consent still voluntary?](optional-consent-blocked-service.html)

## SUS-34

406. [Help is available. Can people claim it?](help-available-document-barrier.html)

## ECO-34

407. [More demand today. More supply when?](more-demand-more-supply-when.html)

## HSP-34

408. [A minimum spend. A banquet worth accepting?](minimum-spend-exclusive-time.html)

## ACC-35

409. [New information. Or an old mistake?](new-information-old-mistake.html)

## FIN-35

410. [A cheaper forward. A more flexible protection?](cheaper-forward-flexible-protection.html)

## MKT-35

411. [A new product. Added sales or moved sales?](added-sales-or-moved-sales.html)

## OPS-35

412. [Mostly zero. Forecast nothing?](mostly-zero-forecast-nothing.html)

## PPL-35

413. [A better plan. Whose input shaped it?](better-plan-whose-input.html)

## STR-35

414. [Global brand. Local proof.](global-brand-local-proof.html)

## ENT-35

415. [One technology. Keep a second application possible?](one-technology-second-application.html)

## IS-35

416. [New transactions. Or genuinely new customers?](new-transactions-new-customers.html)

## GVR-35

417. [A control passed. Was the exception invisible?](control-passed-exception-invisible.html)

## SUS-35

418. [Pay for success. Which clients get served?](pay-success-who-served.html)

## ECO-35

419. [A rival adds capacity. Does your best quantity change?](rival-output-your-best-response.html)

## HSP-35

420. [The guest does the work. Is the service easier?](guest-does-work-service-easier.html)

## ACC-36

421. [After year-end. Evidence about which year?](after-year-end-which-condition.html)

## FIN-36

422. [A cheaper machine. Over how many service years?](cheaper-machine-service-years.html)

## MKT-36

423. [Recognised here. Understood there?](recognised-here-understood-there.html)

## OPS-36

424. [The project has time. Does the specialist?](project-time-specialist-time.html)

## PPL-36

425. [A technical career. Must it become management?](technical-career-not-management.html)

## STR-36

426. [The alliance works. Do the alliances fit?](the-alliances-fit.html)

## ENT-36

427. [The app is free. Who funds the free users?](free-app-who-funds-users.html)

## IS-36

428. [Encrypted here. Readable in the shared link?](encrypted-here-readable-in-the-link.html)

## GVR-36

429. [The penalty is paid. Are customers restored?](penalty-paid-customers-restored.html)

## SUS-36

430. [A generous restricted gift. Enough unrestricted money?](restricted-gift-full-cost.html)

## ECO-36

431. [Many enquiries. A credible threat of entry?](entry-cost-recoverable-after-exit.html)

## HSP-36

432. [The building is busy. Are the rooms available?](busy-floor-available-rooms.html)

## ACC-37

433. [Cash tax paid. Tax expense matched?](cash-tax-tax-expense.html)

## FIN-37

434. [One large payment. A predictable monthly reserve?](monthly-reserve-later-start.html)

## MKT-37

435. [A true success story. A typical result?](true-story-typical-result.html)

## OPS-37

436. [Two punctual trucks. One unloading bay.](punctual-trucks-one-bay.html)

## PPL-37

437. [A useful disagreement. An escalating quarrel.](disagree-with-design-not-person.html)

## STR-37

438. [Sell the product. Rent the outcome?](sell-product-rent-outcome.html)

## ENT-37

439. [The demonstration works. The regulated pathway is longer.](working-sensor-regulated-pathway.html)

## IS-37

440. [Correct today. Which version decided yesterday?](current-model-yesterdays-decision.html)

## GVR-37

441. [Most owners agreed. Which consent was required?](majority-support-class-consent.html)

## SUS-37

442. [Better results. Which weights made them better?](which-weights-made-it-better.html)

## ECO-37

443. [One more café. More choice or duplicated cost?](another-cafe-choice-duplicated-cost.html)

## HSP-37

444. [A full programme. A complete guest journey?](full-programme-complete-journey.html)

## ACC-38

445. [Rent paid. No obligation on the statement?](rent-paid-obligation-recognised.html)

## FIN-38

446. [A sales forecast. How much working capital?](faster-payment-more-stock.html)

## MKT-38

447. [The customer left. Which offer deserves a return?](why-the-member-left.html)

## OPS-38

448. [The best supplier score. The missing condition.](best-score-missing-condition.html)

## PPL-38

449. [Same meeting. Different burden.](same-meeting-different-burden.html)

## STR-38

450. [Win the customer. Keep the value?](customer-value-interface-toll.html)

## ENT-38

451. [Repeat purchases. Or one customer’s experiment?](repeat-orders-experimental-budget.html)

## IS-38

452. [The recommendation changes demand. What will the next model learn?](recommendation-shapes-next-training-set.html)

## GVR-38

453. [A sanction list match. The same person?](name-match-ownership-hold.html)

## SUS-38

454. [A local success. A displaced pressure?](local-reduction-displaced-pressure.html)

## ECO-38

455. [The queue chose it. Did the queue know more?](the-queue-chose-it.html)

## HSP-38

456. [Visible care. A usable lobby?](visible-care-usable-lobby.html)

## ACC-39

457. [More packs sold. Why less revenue?](more-packs-less-revenue.html)

## FIN-39

458. [A reward for early repayment. After which fee?](early-repayment-after-which-fee.html)

## MKT-39

459. [More stockists. More of the category market?](more-stockists-more-category.html)

## OPS-39

460. [A shorter task. More handoffs.](shorter-task-more-handoffs.html)

## PPL-39

461. [Excellent alone. Ready to work together?](excellent-alone-ready-together.html)

## STR-39

462. [Next door. Closer to operate?](next-door-closer-to-operate.html)

## ENT-39

463. [Family wealth. One business, several owners’ needs.](family-wealth-different-cash-needs.html)

## IS-39

464. [A failed payment. A failed checkout?](payment-success-booking-success.html)

## GVR-39

465. [A lower rating. A lower risk?](new-label-same-exposure.html)

## SUS-39

466. [Citizens report it. Who closes the loop?](citizens-report-who-closes-loop.html)

## ECO-39

467. [A larger rebate. A smaller reason to save?](rebate-before-the-baseline.html)

## HSP-39

468. [A group booking. Who may change it?](a-group-booking-who-may-change-it.html)

## ACC-40

469. [A reassuring reply. Evidence from whom?](reassuring-reply-evidence-from-whom.html)

## FIN-40

470. [The same payout. The same value for whom?](same-payout-different-shareholders.html)

## MKT-40

471. [More members. Who answers next?](members-grow-contributors-tire.html)

## OPS-40

472. [Standardise the input. Keep the exception visible.](standard-input-visible-exception.html)

## PPL-40

473. [Helpful connection. A narrow recruitment pool.](helpful-connection-narrow-pool.html)

## STR-40

474. [Different customers. The same reusable capability?](different-customers-reusable-capability.html)

## ENT-40

475. [Spent six months. Fund one more?](spent-six-months-fund-one-more.html)

## IS-40

476. [The old screen returns. What has not rolled back?](old-screen-new-invoices.html)

## GVR-40

477. [A new adviser. An old matter?](new-role-old-matter.html)

## SUS-40

478. [A certified share. A certified item?](certified-share-certified-item.html)

## ECO-40

479. [The same expected payoff. The same choice?](same-average-different-risk-choice.html)

## HSP-40

480. [A great last moment. A better whole visit?](great-last-moment-better-whole-visit.html)

## FIN-41

481. [Protection when the portfolio falls](protection-when-the-portfolio-falls.html)

## ECO-41

482. [The shares jumped. What changed?](shares-jumped-what-changed.html)

## FIN-42

483. [A buy order. A higher quote?](a-buy-order-a-higher-quote.html)

## ECO-42

484. [Record takings. More sold?](record-takings-more-sold.html)

## FIN-43

485. [The customer paid. Can we make payroll?](customer-paid-can-we-make-payroll.html)

## ECO-43

486. [The shelves are empty. Where did sales go?](empty-shelves-where-did-sales-go.html)

## FIN-44

487. [The peg holds. Which rate resets?](the-peg-holds-which-rate-resets.html)

## ECO-44

488. [Rates fell. Why did the loan cost more?](rate-cut-credit-spread.html)

## FIN-45

489. [The same forecast. A dearer option?](same-forecast-dearer-option.html)

## ECO-45

490. [A tariff discount. On how many units?](tariff-discount-how-many-units.html)

## FIN-46

491. [Which share would you sell?](which-share-would-you-sell.html)

## FIN-47

492. [Who gets the lending subsidy?](who-gets-the-lending-subsidy.html)

## FIN-48

493. [Who funds the rescue investment?](who-funds-the-rescue-investment.html)
