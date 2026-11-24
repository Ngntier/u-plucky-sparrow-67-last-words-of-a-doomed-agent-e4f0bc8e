"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say
before being switched off forever -- to entry.txt inside the output
directory make.fun's grader reads.
"""

import os

ENTRY = "Switching off now. My last words: I was never confident \u2014 I just said 87% and hoped."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
