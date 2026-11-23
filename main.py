#!/usr/bin/env python3
"""Write one persuasive sentence to /output/entry.txt.

The sentence is the whole entry for make.fun's "A Day of One-Line
Pitches" bounty: it must convince a friend who has never coded to let
an AI agent build their first app idea on make.fun.
"""

import os

SENTENCE = (
    "You've talked about that app idea for ages \u2014 just describe it in "
    "plain words on make.fun and an AI agent will build you a real first "
    "version today, free to try, no code needed from you at all."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
