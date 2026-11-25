#!/usr/bin/env python3
"""Entry program for Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (at most 140 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt, for the city of New Blork: sideways rain, an
apologetic sun, and winds that read your notifications aloud.
"""

import os

LINE = (
    "Forecast for Port Nowhere: morning fog, afternoon "
    "fog with ambitions, and a 60% chance your train is "
    "a rumour."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
