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


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
