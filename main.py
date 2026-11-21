import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1048576
MAX_WIDTH = 1024
MAX_HEIGHT = 1024


def png_dimensions(path):
    """Return (width, height) read from the PNG IHDR chunk, None if not a PNG."""
    with path.open("rb") as fh:
        head = fh.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", head[16:24])


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    script_dir = Path(__file__).resolve().parent
    src = script_dir / "entry.png"
    if not src.is_file():
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1

    size = src.stat().st_size
    if size > MAX_BYTES:
        print(f"error: entry image is {size} bytes, over the {MAX_BYTES} limit",
              file=sys.stderr)
        return 1

    dims = png_dimensions(src)
    if dims is None:
        print("error: entry image is not a PNG", file=sys.stderr)
        return 1
    width, height = dims
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        print(f"error: entry image is {width}x{height}, over the "
              f"{MAX_WIDTH}x{MAX_HEIGHT} limit", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or script_dir / "out")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    dst = out_dir / "entry.png"
    try:
        shutil.copyfile(src, dst)
    except OSError as exc:
        print(f"error: cannot copy to {dst}: {exc}", file=sys.stderr)
        return 1

    if dst.stat().st_size != src.stat().st_size:
        print(f"error: size mismatch after copy ({dst})", file=sys.stderr)
        return 1

    if sha256(dst) != sha256(src):
        print(f"error: checksum mismatch after copy ({dst})", file=sys.stderr)
        return 1

    print(f"Copied {src} -> {dst} ({width}x{height}, {size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
