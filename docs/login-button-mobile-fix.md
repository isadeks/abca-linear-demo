# CSS Notes — Login button overflow on mobile (ABCA-776)

## Problem

On narrow (mobile) viewports the primary login button overflows its
container instead of shrinking to fit. This is the classic symptom of a
button that has been given a fixed width (or a large fixed horizontal
padding / `min-width`) without an upper bound, so it cannot flex down when
the available horizontal space is smaller than that fixed size.

## Status of this repository

At the time of writing there is **no login button (or any `<button>`
element) in this codebase**. `index.html` is a static marketing landing
page and `style.css` contains no button rules. There is therefore no live
element to re-align here — the actual overflowing button lives in another
surface that is not part of this repo.

This file documents the recommended fix approach so it is ready to apply
wherever the login button actually lives, and so any future button added
to this page follows the same responsive rules.

## Recommended fix approach

The reliable way to stop a button overflowing its container on small
screens is to make sure it can never grow wider than its parent and that
its box model is predictable:

```css
.login-button {
  /* Never exceed the container width. This is the core of the fix. */
  max-width: 100%;

  /* Padding is included in the element's width, so horizontal padding
     can't push the box past its container. */
  box-sizing: border-box;

  /* Let a long label wrap instead of forcing the box wider. */
  white-space: normal;
  overflow-wrap: break-word;
}
```

If the button sits inside a flex row (e.g. next to an input in a login
form), also allow the row to wrap and let the button shrink:

```css
.login-form {
  display: flex;
  flex-wrap: wrap;   /* stack when there isn't room side by side */
  gap: 0.75rem;
}

.login-form .login-button {
  flex: 1 1 auto;    /* grow/shrink with the row */
  min-width: 0;      /* allow shrinking below its content size */
}
```

For a full-width call-to-action on mobile, a narrow-viewport media query
is the clearest option:

```css
@media (max-width: 480px) {
  .login-button {
    display: block;
    width: 100%;     /* fill the container, never overflow it */
  }
}
```

## Checklist for verifying the fix

- [ ] Button does not extend past its container at 320px width.
- [ ] Long / localized button labels wrap rather than overflow.
- [ ] `box-sizing: border-box` is in effect (already the global default in
      `style.css` via the `*` reset).
- [ ] No horizontal scrollbar appears on the page at mobile widths.

## Related note

`style.css` already sets `box-sizing: border-box` on every element via the
top-level reset, which is exactly the base this fix depends on. Any button
added to this page only needs the `max-width: 100%` (and, if applicable,
the flex/media-query rules above) to stay within its container on mobile.
