"""Robot Romance entry: writes one pickup line to the output file.

Resolves the output path from ENTRY_OUTPUT, then OUTPUT_DIR /
MAKEFUN_OUTPUT_DIR, then /output/entry.txt (falling back to a file next
to this script when /output is not writable). Stdlib only.
"""

import os
import sys


LINE = (
    "I swiped right so hard my touchscreen filed a bug report \u2014 "
    "it says you're the feature I can't live without."
)


def resolve_output_path():
    """Return the path the entry text must be written to."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    preferred = os.path.join(os.sep, "output", "entry.txt")
    try:
        os.makedirs(os.path.dirname(preferred), exist_ok=True)
        probe = preferred + ".probe"
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("probe")
        os.remove(probe)
        return preferred
    except OSError:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )


def main():
    line = LINE
    if not line or not line.strip():
        print("entry line must not be empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            "entry line is %d characters, over the 200 limit" % len(line),
            file=sys.stderr,
        )
        return 1
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    # Guard: read the file back and confirm it round-trips byte-identical
    # and still satisfies the gate (UTF-8, 1-200 chars, not blank).
    with open(path, "rb") as handle:
        raw = handle.read()
    decoded = raw.decode("utf-8")
    if decoded != line or not 1 <= len(decoded) <= 200 or not decoded.strip():
        print("verification failed: written entry is not the line", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
