"""Entry for the "Worst Fix Ever: Funniest Commit Message" brief.

The humour here lives in a single, terrible commit message. Instead of
repairing the code, the fictional author deletes the test that was
complaining about the bug. With the test gone the build goes green, but
nothing was actually fixed: the defect loses its documentation, nobody
can reproduce it on demand any more, and it quietly ships anyway.

This program does the smallest honest job around that joke. It holds
the message in one constant, checks it is a single sane line, and
writes it verbatim — with no trailing newline — into entry.txt inside
the output directory chosen by the runner.
"""

import os
from pathlib import Path

LINE = "fix: removed the failing test — the bug is now undocumented, unreproducible, and in production"

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir):
    """Write the commit message to ``entry.txt`` in ``out_dir``.

    The message has to stay a single line: an empty value or one that
    smuggles in a newline would break the format, so both cases raise
    ``ValueError`` before anything touches disk. The directory is
    created when missing, and the resulting path is returned.
    """
    if not LINE:
        raise ValueError("entry line must not be empty")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must not contain newlines")

    target_dir = Path(out_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    entry_path = target_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir():
    """Return the output directory requested by the environment."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
