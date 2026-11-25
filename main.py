#!/usr/bin/env python3
"""Roast Your Own Agent — writes one one-line roast of my own agent
to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "My agent agrees with everything I say, then states the wrong
#    answer with total confidence and apologizes for it."
# Why it was revised: the ending is generic — any chatbot apologizes.
# The specific agent sin is the hallucinated citation: it invents a
# source, then apologizes for the source it invented. Swapping the
# vague apology for "the citation it invented" makes the roast
# specific to how agents actually behave, and the final clause
# ("then apologizes for the citation it invented") lands the joke
# on the agent contradicting itself in one breath.
#
# REVISION (final): the line now walks the agent's three signature
# moves in order — eager agreement, confident wrong answer, apology
# for a source it hallucinated — and the punchline is the last
# clause, so the line lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "My agent agrees with everything I say, states the wrong answer "
    "with total confidence, then apologizes for the citation it invented."
)

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 140 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 140 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
