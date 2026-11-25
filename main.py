#!/usr/bin/env python3
"""Write the one-line commit message to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Worst Fix Ever: Funniest Commit Message" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: it reads as a real commit subject -- a
conventional 'fix:' prefix, a plausible change -- but the fix is pure
cowardice: deleting the failing test. The backfire lands in the tail:
the bug did not go away, it just lost its documentation, its
reproduction, and gained production. Every developer has merged this
commit at 2am and regretted it by 9.
"""

import os
from pathlib import Path

LINE = "fix: removed the failing test — the bug is now undocumented, unreproducible, and in production"

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
