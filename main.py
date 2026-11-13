# ai-joke-03 entry (Python 3.13, standard library only): it writes one fixed
# joke, a one-liner about AI coding agents, to /output/entry.txt.
#
# The joke: "My coding agent wrote a 200-line function, then left a TODO above
# it: 'implement this function.'" The agent did the work and, in the same
# breath, left a note saying the work still needs doing.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Deterministic: one fixed string, no randomness, no time, no network.
# The file is written with no trailing newline: the judge reads exactly
# the bytes written, so no line end is added that is not part of the joke.

import os

JOKE = "My coding agent wrote a 200-line function, then left a TODO above it: 'implement this function.'"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
