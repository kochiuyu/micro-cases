# Illustration guide · Micro Cases in Business

## Match the existing collection

Use the established **watercolor-and-ink narrative style**, not a flat icon or diagram style. Before creating art, visually inspect at least two existing case illustrations. `tarts-scene.jpg` and `stall-scene.jpg` are useful baseline references; `family-name-scene.jpg` is a recent matched example. These images are style references, not characters or compositions to copy literally.

- Fine, hand-drawn dark contours and warm watercolor washes.
- Visible but gentle paper grain; natural color variation rather than smooth vector fills.
- Expressive, fictional people shown making or discussing the case decision.
- Grounded Hong Kong / regional settings when appropriate to the case: shop interiors, workshops, campus markets or streets. Use the actual case geography, not a generic skyline in every image.
- Warm, muted colors, natural daylight and everyday material details.
- Calm, approachable storybook illustration for an adult business classroom. Avoid caricature, exaggerated distress, photorealism and glossy 3D.

## Tell the decision, not the answer

Show the people, objects and setting that make the first choice concrete. A document can suggest an offer; a calendar can suggest a cash-timing problem. Do not reveal the round-two twist or depict the choice as already settled. Keep exact financial amounts, dates and numerical evidence in accessible HTML tables/charts, not in the artwork.

Use no readable text, figures, watermarks or real company logos. Do not portray real executives or suggest a fictional scene is a documentary record. Historical companies may ground the case text, but illustration and invented classroom terms must remain clearly distinguished from reported facts.

## Production and integration

1. Read the opening decision and identify its visual moment.
2. Open two existing illustrations and describe their visible style in the image-generation prompt. Supply the images as style references where supported.
3. Generate a new, wide landscape scene. Target the collection's approximately **760:389 aspect ratio**. Do not substitute a flat SVG icon for a finished narrative illustration.
4. Inspect the generated image at full size and at card size. Check hands, faces, object relationships, unintended readable text, and whether the scene really matches the collection.
5. Export an optimized JPG at **760 × 389 px**, preserving aspect ratio without stretching. Keep the generated original outside the published site unless it is needed there. Typical quality 85–90 is a starting point, not a substitute for checking pixels.
6. Save it as `<case-slug>-scene.jpg`. Add meaningful alternative text on the case page and presentation; the linked collection card may use empty alt when its adjacent title already identifies the case.
7. Update the case hero, presentation image, collection thumbnail and editable Markdown together. Do not leave any surface using an obsolete image.
8. Run the content checks, then verify the published image in the page, collection and presentation. Check fit and legibility, including narrow layouts where available.

## Prompt starting point

> Create a new illustration-story for the same business classroom series as the supplied reference images. Match their fine ink outlines, warm watercolor washes, soft paper grain, gently expressive fictional adult characters and detailed everyday setting. Wide landscape, approximately 760:389. Scene: [people discussing or facing the opening decision], with [two or three relevant objects] in [case-appropriate place]. The decision is still open. No readable text, numbers, company logos or watermark. Not vector, infographic, photorealistic or 3D.

The scene should change from case to case; the visual language should not. If a proposed style differs materially, ask before replacing the established style.

## Keep teaching graphics separate

Accessible tables, cash timelines and other analytical exhibits may use HTML, CSS or SVG. That does not change the required style of the narrative case illustration.
