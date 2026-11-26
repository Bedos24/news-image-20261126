#!/usr/bin/env python3
"""Entry program for news-image-20261126 (make.fun).

The picture of the day is a single newspaper front page covering the
world news of Thursday, 26 November 2026. The finished page travels
with this repository as frontpage.png; running this program checks
that file and then publishes it as entry.png in the output folder.

Only the Python standard library is used, nothing is fetched from the
network, and the output bytes are exactly the shipped page bytes.
"""

import hashlib
import os
import struct
import sys

PAGE_NAME = "frontpage.png"
PAGE_SHA256 = "1eabaf328927ab5a7df8625d5ade3d13967144d7898f3137acfbac7efdd20a88"
PAGE_BYTES = 162709
BYTE_LIMIT = 1024 * 1024
SIDE_LIMIT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_page(folder):
    """Load the shipped front page and return its raw bytes."""
    path = os.path.join(folder, PAGE_NAME)
    with open(path, "rb") as handle:
        return handle.read()


def check_page(payload):
    """Reject a page that breaks the competition guardrails."""
    if not payload.startswith(PNG_MAGIC):
        raise ValueError("front page is not a PNG image")
    if len(payload) != PAGE_BYTES:
        raise ValueError("front page has an unexpected byte count")
    if len(payload) > BYTE_LIMIT:
        raise ValueError("front page exceeds the 1 MiB cap")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != PAGE_SHA256:
        raise ValueError("front page checksum does not match")
    width, height = struct.unpack(">II", payload[16:24])
    if width > SIDE_LIMIT or height > SIDE_LIMIT:
        raise ValueError("front page exceeds the 1024 pixel cap")
    return width, height


def output_folder(here):
    """Prefer MAKEFUN_OUTPUT_DIR, then /output, then a local folder."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(here, "output")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    payload = read_page(here)
    width, height = check_page(payload)
    target_dir = output_folder(here)
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(payload)
    # Read the published file back and confirm it survived the write
    # byte for byte; a truncated copy would score as a broken entry.
    with open(target, "rb") as handle:
        published = handle.read()
    if hashlib.sha256(published).hexdigest() != PAGE_SHA256:
        raise ValueError("published entry.png does not match the page")
    print("entry.png written to %s (%d x %d, %d bytes, verified)"
          % (target, width, height, len(published)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
