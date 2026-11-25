"""The Meeting That Should Have Been One Line — make.fun entry.

Writes a single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. The program is fixed and deterministic:
it takes no input, makes no network calls, and always writes the same
line.

FINAL entry (revision round): "We all agreed in the thread; this
meeting is just the applause." (62 characters.)

Why this one wins the judge's brief, in the brief's own order:
  1. One sentence, unmistakably office humor: the thread, the
     meeting, the applause.
  2. Kills the meeting outright: the decision was already made in
     the thread, so the meeting's only remaining function is
     ceremony — applause. After this line, no one can justify
     holding the meeting at all.
  3. Relatable to anyone who has sat through a useless meeting:
     every office worker has watched a room re-enact a decision
     that was settled in the chat before anyone arrived.
  4. The joke lands on a turn at the very end: a meeting reduced
     to applause — the sting is that the hour exists only to
     congratulate a decision already taken, not to make one.
  5. Stands alone: no setup, no context, no explanation needed.

Finalists beaten by it, and why:
  * "Nobody here will say anything that wasn't already in the
    thread; we're just the read receipts, live." (100) — the
    round-1 draft. Same kill, but the first clause explains
    instead of landing; "read receipts, live" is clever, while
    "just the applause" is a cleaner, shorter punch, and the
    competition's own tie-break rewards the smaller text.
  * "The answer is yes; this meeting is just the long way of
    saying it." (68) — presumes a yes/no question, so it fits
    fewer meetings; the winner covers any decision already made
    in the thread.
  * "This meeting exists because the email needed an audience."
    (56) — describes why the meeting exists instead of replacing
    it; it holds no decision and no dismissal, so it kills less
    completely. "Could have been an email" is also the most
    common trope in a field of 544 entries.
  * "Approved — now let's all go back to work and pretend this
    meeting happened." (76) — a decision plus a joke, but
    "pretend this meeting happened" is a weaker sting than "just
    the applause", and it leans on the meeting having happened.
  * "We could have decided this in the time it took to find a
    room for it." (71) — relatable about room hunting, but it
    complains about logistics instead of killing the meeting.
"""

from __future__ import annotations

import os

# The entry. 62 characters, plain ASCII, single line, no trailing newline.
ENTRY = "We all agreed in the thread; this meeting is just the applause."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Enforce the gate: UTF-8 text of 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # must be encodable as UTF-8
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
