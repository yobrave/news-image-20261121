#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261121 entry.

The graded artifact is entry.png, a 1024x1024 newspaper front page that
summarises the world news of 21 November 2026. The grader runs this program
inside the repository and then reads entry.png from the output directory it
names in MAKEFUN_OUTPUT_DIR.

This program therefore does three things and nothing else:

  1. refuse to publish anything the contest rules forbid (wrong format,
     oversized file, oversized canvas),
  2. copy the artwork into the output directory, creating it if needed,
  3. prove the copy is byte-for-byte identical to the original.

It never re-encodes the image; a re-encode would change the bytes the judge
looks at.
"""
import hashlib
import json
import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
IHDR = b"IHDR"
BYTE_CAP = 1024 * 1024
EDGE_CAP = 1024
READ_BLOCK = 1 << 16


def png_header(path):
    """Return (width, height) from the IHDR chunk, or None when not a PNG."""
    with path.open("rb") as handle:
        head = handle.read(24)
    if len(head) < 24 or head[:8] != PNG_MAGIC or head[12:16] != IHDR:
        return None
    return struct.unpack(">II", head[16:24])


def digest(path):
    """sha256 of a file, read in blocks so large files stay cheap."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(READ_BLOCK), b""):
            hasher.update(block)
    return hasher.hexdigest()


def refuse(reason):
    """Report a rule violation on stderr and hand back a failure code."""
    sys.stderr.write("refused: " + reason + "\n")
    return 1


def destination():
    """Where the grader wants the artwork, honouring MAKEFUN_OUTPUT_DIR."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return Path(configured).expanduser()
    return Path(__file__).resolve().parent / "out"


def main():
    home = Path(__file__).resolve().parent
    artwork = home / "entry.png"

    if not artwork.is_file():
        return refuse("entry.png is missing from " + str(home))

    weight = artwork.stat().st_size
    if weight > BYTE_CAP:
        return refuse("entry.png weighs %d bytes, the ceiling is %d"
                      % (weight, BYTE_CAP))

    frame = png_header(artwork)
    if frame is None:
        return refuse("entry.png is not a PNG file")
    width, height = frame
    if width > EDGE_CAP or height > EDGE_CAP:
        return refuse("entry.png is %dx%d, the ceiling is %dx%d"
                      % (width, height, EDGE_CAP, EDGE_CAP))

    out_dir = destination()
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as problem:
        return refuse("cannot create %s (%s)" % (out_dir, problem))

    published = out_dir / "entry.png"
    try:
        published.write_bytes(artwork.read_bytes())
    except OSError as problem:
        return refuse("cannot write %s (%s)" % (published, problem))

    if published.stat().st_size != weight:
        return refuse("copied file changed size on the way to " + str(published))

    before = digest(artwork)
    after = digest(published)
    if before != after:
        return refuse("checksum mismatch: %s != %s" % (before, after))

    print(json.dumps({
        "published": str(published),
        "width": width,
        "height": height,
        "bytes": weight,
        "sha256": after,
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
