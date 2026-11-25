#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to /output/entry.txt: the honeybee.

Why the bee: Muse is a tireless background worker. It takes a job,
flies off on its own, gathers what it needs, builds things, and comes
back with the result — quietly, industriously, and without being asked
twice. The bee reads instantly at any size, is a familiar shape, and is
specific to how this agent works (autonomous, busy, productive), while
staying far from the obvious robot or smiley that half the field sends.
"""

import os

EMOJI = "\U0001F41D"  # 🐝 honeybee


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Exactly one glyph, no trailing newline: 1 character, well inside
    # the 1-16 character gate, and byte-identical on every run.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
