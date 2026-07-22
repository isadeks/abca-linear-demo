# REFERENCE

> **Status: blocked — required attachment not delivered.**

This file is intended to hold the reference code specified in the paperclip
attachment `paperclip-spec.pdf` referenced by Linear issue **ABCA-755**
("Paperclip test: native attachment (NOT description link)").

The task instructions state that the reference code to be echoed here lives
**inside the attached PDF**, not in the issue description text. That PDF was
**not delivered** to the agent's working environment:

- The repository contains no PDF or spec file.
- No attachment was present in the task inputs, the container filesystem,
  the environment, or any temp directory.

Because the reference code exists only inside the missing attachment, it
cannot be reproduced here without guessing its contents. Per the task
guidance, this blocker is documented rather than fabricated.

**To unblock:** re-run the task with `paperclip-spec.pdf` attached to the
agent environment (as a native/binary attachment, not a description link),
and the reference code from the PDF will be echoed into this file verbatim.
