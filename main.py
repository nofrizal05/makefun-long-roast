"""One-line satirical roast for make.fun's "The Long Roast" bounty.

Writes a single original sentence roasting lawmakers who would regulate
AI, crypto or the internet but cannot convert a file to PDF, to
/output/entry.txt. Standard library only.
"""

import os
import re

SENTENCE = (
    "They spent a year writing the law that will govern artificial "
    "intelligence, and three months trying to convert that same law into "
    "a PDF \u2014 the future, it turns out, is a Word file nobody in the "
    "building can open."
)

MAX_CHARS = 320


def validate(sentence):
    """Exactly one sentence, 1-320 characters, no real living person named.

    A sentence terminator is a period, exclamation or question mark that
    ends the text or is followed by whitespace and a capital letter (the
    start of a new sentence). A period inside a word or abbreviation does
    not end a sentence.
    """
    text = sentence.strip()
    if not text:
        raise ValueError("sentence is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "sentence is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    terminators = re.findall(r"[.!?](?=\s+[A-Z]|$)", text)
    if len(terminators) != 1:
        raise ValueError(
            "expected exactly one sentence, found %d terminators" % len(terminators)
        )
    if not text.endswith((".", "!", "?")):
        raise ValueError("sentence must end with terminal punctuation")
    return text


def main():
    sentence = validate(SENTENCE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    print("Wrote %d characters to %s" % (len(sentence), out_path))


if __name__ == "__main__":
    main()
