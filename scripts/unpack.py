#!/usr/bin/env python3
"""Unpack a .docx file into a directory for XML editing.

A .docx file is a ZIP archive. This script extracts it so you can
edit word/document.xml directly, preserving exact formatting.

Usage: python scripts/unpack.py <file.docx> [output_dir]

Output directory defaults to <file>_unpacked/ next to the source file.
The output path is printed to stdout so callers can capture it.
"""
import sys
import shutil
import zipfile
from pathlib import Path


def unpack(docx_path: str, output_dir: str | None = None) -> str:
    src = Path(docx_path).expanduser().resolve()
    if not src.exists():
        raise FileNotFoundError(f"File not found: {src}")
    if src.suffix.lower() != ".docx":
        raise ValueError(f"Expected a .docx file, got: {src.suffix}")

    dest = (
        Path(output_dir).expanduser().resolve()
        if output_dir
        else src.parent / (src.stem + "_unpacked")
    )
    if dest.exists():
        shutil.rmtree(dest)

    with zipfile.ZipFile(src, "r") as zf:
        zf.extractall(dest)

    print(dest)
    return str(dest)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unpack.py <file.docx> [output_dir]", file=sys.stderr)
        sys.exit(1)
    try:
        unpack(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
