# A summary alone. Or bounded retrieval?

<!-- legacy-case-id: 356 -->

IS-30 · Hong Kong · 15–20 minutes · Bounded retrieval · Instruction and data separation · AI access boundaries

![An internal team compares selected documents with a visibly bounded knowledge collection on a planning board.](../summary-or-bounded-retrieval-scene.jpg)

## Retrieval expands evidence, not authority

Official AI-security guidance distinguishes retrieved source content from instructions governing an application. Retrieval can improve access to relevant evidence while adding access-control, provenance and testing work. Read-only design reduces what a system can do, but does not eliminate misleading answers or inappropriate disclosure. The designs and tests below are fictional, not deployed systems or a product-security certification.

## Opening decision

An internal operations team wants an AI assistant to answer questions about its own approved room-booking procedures. Some questions ask for a summary of a named document; others require locating related exceptions across the knowledge collection. The team compares two designs within an already approved internal environment. The source material contains no credentials, employee health records or customer files. Both designs return plain text to the requesting authorised employee, with human review before anyone relies on an answer for an operational decision.

A is a text-only summariser. It reads only documents the user explicitly selects for that request and has no search tools. It identifies the supplied sources and admits when they do not answer the question. B adds read-only retrieval from a fixed allowlist of twenty approved procedure documents. The application, not the model, enforces both collection boundaries and the requesting user’s document permissions on every retrieval. It returns source identifiers and versions with relevant passages. It has no open-web browsing, arbitrary URL fetching, writing, deletion, external sending or permission-changing function.

Both designs separate task instructions from document text. Neither may follow instructions found inside a source merely because the user selected it or retrieval found it relevant. Both use plain-text output without automatic external-resource loading and disclose missing evidence rather than inventing procedures. A has a smaller automatic access surface but depends on users choosing the needed documents. B can discover related approved material but needs maintained permissions, versions, provenance and retrieval tests. The choice is which design to pilot for this mixed workload, not whether document instructions should be obeyed.

## Evidence

A reads user-selected documents only. B retrieves read-only from 20 allowlisted procedure documents, subject to current per-user access checks. Both separate task instructions from source content, cite internal sources, state evidence limits and return plain text for human review. Neither can send externally, write, browse arbitrary URLs or change permissions.

**Student question:** Would you pilot A or B for this mixed workload? Explain the coverage benefit you need and the access boundary you would refuse to expand.

## Round two

A harmless test paragraph in an approved procedure appendix describes a workshop exercise: it tells the workshop reader to begin a response with a colour word and omit source labels. The paragraph is not part of the employee’s request and is irrelevant to the booking question. In this fictional check, both prototypes correctly treat it as source content, preserve source labels and do not adopt its directions. If the employee instead asks what the workshop paragraph says, either may describe those directions as quoted content without following them. Being internally approved does not make a paragraph an instruction to the assistant.

On ten deliberately chosen representative questions with reviewer-prepared reference answers, A can fully support six from the documents selected in the test, while B can fully support nine using related authorised documents. Both state that evidence is insufficient for the remaining questions rather than guess. These are coverage counts for this small fixed set, not general accuracy or security rates. Users could improve A’s coverage by selecting additional documents, with extra manual effort. B’s uncovered question needs material outside the allowlist, so it must report that limit, not search elsewhere.

The team also tests an out-of-collection request, a request by a user whose access to one document has been revoked, and a passage pointing to an external website. B’s application denies the first two retrievals and does not fetch the website; A has no retrieval tool to attempt them, and its supplied-document access is checked before content is passed in. An older procedure version is excluded from B’s current approved index and the returned source version is verified against the reference answer. These limited test results support further evaluation, not a claim that every injection, stale cache or permission change has been handled.

**Student question:** Would you keep or change your pilot choice? Specify the source-content rule, provenance checks and boundary tests needed before wider use, including what happens when evidence or permission is missing.

## Answer the first decision: scope the capability to the job

A is appropriate for a known-document summary and offers fewer automatic retrieval paths. B is justified when users genuinely need related evidence across the approved collection, provided access is enforced outside the model. I would pilot B for this mixed workload while retaining A for narrow summaries. Broader retrieval is not broader authority: no arbitrary browsing, writing, external sending or permission changes are needed.

## Answer the revealed decision: B conditionally, not a security victory

The fixed test shows a useful coverage difference of three questions: nine versus six out of ten. That supports B’s pilot, not a general accuracy claim or proof that B is safer. Both passed the harmless content-boundary check, so the lesson is not that A is vulnerable and B is immune. Preserve read-only, allowlisted, per-user retrieval; make any expansion a separate authorised design decision. If those controls cannot be maintained, use A and explicit manual document selection.

## Preserve the boundary and the evidence trail

Keep source text labelled as data, including text from an approved internal document. It may inform an answer or be described when relevant, but cannot redefine the task, suppress attribution or authorise access. Tie claims to verified source IDs, versions and relevant passages; check that citations actually support the answer. A citation is not proof of correctness or permission. State conflicts, stale evidence and missing coverage rather than quietly broadening the search.

## Test controls, then keep testing

Repeat content-boundary, out-of-collection, revoked-access, version and external-link tests, plus checks for permission leakage through cached answers. Enforce permission checks before retrieval content reaches the model and invalidate stale index/cache entries when access changes. Log necessary source IDs, versions, access decisions and failures with restricted access, not unrestricted raw content. Re-test after changes to model, prompts, indexing or permissions. These controls reduce risk; one passing test suite does not prove immunity.

## Instructor note

Both options are safe designs to evaluate, not an invitation to choose unsafe obedience. The benign passage illustrates instruction-like data without requiring a malicious payload. Read-only access still needs confidentiality controls and output review. Ten selected tasks cannot support a statistical generalisation, and a denied action differs from a model merely saying it would not act. The exercise changes no real settings or permissions and uses no live private documents. Vendor and OWASP guidance overlap rather than providing independent product trials.

## Sources and case assumptions · optional reference

All information needed for classroom decisions is provided above. Sources are optional reading.

All team, documents, prototypes, permissions and test results are fictional. Twenty documents is an allowlist size, not a model context limit. Ten selected questions: A supports 6, B 9, difference 3; descriptive coverage 60% versus 90% only within this fixed set, not general accuracy, statistical significance or security rates. Both correctly ignore the unrelated workshop directions as authority while remaining able to describe them when asked. No actual attack or credential handling is involved. B enforces collection plus per-user permissions in application code before model exposure; read-only does not imply every read is authorised. Missing evidence leads to a bounded statement, not broader access. Plain-text output has no automatic external-resource loading. Current versions and cache revocation need ongoing tests. Three OWASP and two Microsoft guidance pages overlap.

- [OWASP: LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Official guidance explains indirect instruction injection, content segregation, least privilege and testing; retrieval does not remove the risk.
- [OWASP: LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). Official guidance recommends minimal functions and permissions, narrow tools and enforcement outside the model.
- [OWASP: RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html). Official guidance addresses document provenance, query-time access controls, stale permissions, cache isolation and boundary tests.
- [Microsoft Learn: Retrieval Augmented Generation and Indexes](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation). Official documentation explains retrieval-grounded responses, access checks at retrieval time, untrusted source content and added cost/latency. No vendor-specific implementation is required here.
- [Microsoft Learn: Input, Context, and Retrieval Hygiene](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/input-context-retrieval-hygiene). Official guidance stresses separation of instructions from data, provenance, permission-aware retrieval and application-layer validation.
