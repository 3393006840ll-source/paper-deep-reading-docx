#!/usr/bin/env python3
"""Extract page-separated PDF text for evidence tracing."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")

    reader = PdfReader(str(args.pdf))
    parts = [
        f"SOURCE: {args.pdf.name}",
        f"PDF_PAGES: {len(reader.pages)}",
        "",
    ]
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # preserve progress on a damaged page
            text = f"[EXTRACTION ERROR: {exc}]"
        parts.extend(
            [
                f"===== PDF PAGE {index} =====",
                text.strip(),
                "",
            ]
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts), encoding="utf-8")
    print(f"Extracted {len(reader.pages)} pages to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
