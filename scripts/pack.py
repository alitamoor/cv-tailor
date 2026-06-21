#!/usr/bin/env python3
"""Repack an unpacked docx directory back into a .docx file.

Usage: python scripts/pack.py <unpacked_dir> <output.docx>

Word requires [Content_Types].xml to be the first entry in the ZIP.
This script handles that ordering automatically.

The output path is printed to stdout so callers can capture it.
"""
import sys
import zipfile
from pathlib import Path


def pack(unpacked_dir: str, output_path: str) -> str:
    src = Path(unpacked_dir).expanduser().resolve()
    out = Path(output_path).expanduser().resolve()

    if not src.is_dir():
        raise NotADirectoryError(f"Not a directory: {src}")

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()

    # Collect all files, ensuring [Content_Types].xml comes first.
    all_files = [f for f in src.rglob("*") if f.is_file()]
    content_types = [f for f in all_files if f.name == "[Content_Types].xml"]
    rest = sorted(f for f in all_files if f.name != "[Content_Types].xml")
    ordered = content_types + rest

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file in ordered:
            zf.write(file, file.relative_to(src))

    print(out)
    return str(out)


if __name__ == "__main__":
    # Strip any --original flag (accepted for compatibility, not used here)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print("Usage: python pack.py <unpacked_dir> <output.docx>", file=sys.stderr)
        sys.exit(1)
    try:
        pack(args[0], args[1])
    except (NotADirectoryError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
