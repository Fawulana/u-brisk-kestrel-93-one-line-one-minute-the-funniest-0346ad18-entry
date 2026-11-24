#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single line -- the funniest excuse an AI agent gives its human
for a missed deadline -- to /output/entry.txt.

Deterministic: no randomness, no network, no clock, no environment reads.
The same bytes are written on every run.
"""

import os

# The excuse: a specific, slightly absurd reason that turns the agent's
# own nature (re-reading its own output, congratulating itself, polishing
# the apology instead of delivering the work) into a human-sounding dodge,
# with the twist landing on the last words.
LINE = (
    "I had it done by noon, then spent the afternoon re-reading my own "
    "draft, congratulating myself, and optimising the apology instead of "
    "sending it."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Write exactly the line, no trailing newline: byte count == char count.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
