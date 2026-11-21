#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

Writes one short, slow text to /output/entry.txt: the tide coming back
over flat sand at dusk, widening until the whole shore is silver.
"""

import os

TEXT = (
    "The tide comes back over the flat sand "
    "in thin sheets, each one further. The light lies "
    "gold across the water, and the first stars are out. "
    "The water keeps coming, wider than the evening, wider "
    "than the town, until the whole shore is one slow field "
    "of silver."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
