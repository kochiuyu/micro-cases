# Decision questions · required presentation rule

Every case must make its student decision questions visually unmistakable in **both the reading page and presentation slides**. Do not leave an opening vote or round-two question as an ordinary paragraph, even if its slide title is a question.

Use the collection’s existing `student-prompt` component:

```html
<div class="student-prompt">
  <strong>Your decision</strong>
  <p>The concrete choice students must make, followed by the reason or evidence requested.</p>
</div>
```

Preserve the warm pale-gold background, dark left border, bold question and visible “Your decision” label. The label and weight must distinguish the prompt even without color. Keep the question text consistent between the reading page, presentation and student handout. Editable Markdown must label it **Student question:**.

## Before publishing any case

1. Identify the opening decision and every later decision/revote. Wrap each in `student-prompt` on the page **and in the slide HTML**.
2. Confirm the handout includes the questions and round-two prompt; do not accidentally publish the debrief as the student response.
3. Run `python tests/check_decision_prompts.py`. It checks that every case has at least two nonempty decision components in both surfaces. This minimum-count safeguard does not replace inspection of every question.
4. Open presentation mode, visit each decision slide and visually verify that the whole highlighted box fits and remains readable. Also inspect the page. A passing text check alone is not a visual pass.

News-hook questions, explanatory questions and instructor discussion suggestions need not all be gold boxes. The required boxes are the choices students are asked to answer during the case.
