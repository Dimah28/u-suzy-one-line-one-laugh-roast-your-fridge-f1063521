"""One Line, One Laugh: Roast Your Fridge -- make.fun bounty
u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.

Writes a single roast of the entrant's fridge (133 characters, well
inside the 200-character gate) to /output/entry.txt.

The joke: a midnight fridge raid finds almost nothing -- one egg, a
jar of pickles -- and then the twist lands in the last few words: the
mystery smell in there has been paying rent longer than the owner.
Concrete setup (midnight, one egg, pickles), a specific recognisable
detail (the smell), surprise reversal at the end, reads cleanly aloud
as one line, no wasted words.
"""

import os

LINE = (
    "I opened my fridge at midnight and found one egg, a jar of "
    "pickles, and a smell that has clearly been paying rent longer "
    "than I have."
)

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def _validate_entry(text):
    """Gate from the bounty rules: UTF-8 text, 1-200 chars, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate is 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def write_entry():
    """Validate the roast, then write it to /output/entry.txt."""
    _validate_entry(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return OUTPUT_PATH


if __name__ == "__main__":
    write_entry()
