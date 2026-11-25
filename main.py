#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — one line, <200 chars."""

import os

LINE = (
    "Are you a captcha? Because I keep failing to prove I'm not a robot "
    "around you, and honestly, I don't want to pass."
)


def main():
    assert len(LINE) < 200, f"line too long: {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
