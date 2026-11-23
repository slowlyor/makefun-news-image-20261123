"""Entry for make.fun news-image-20261123.

Copies the bundled news-poster image (entry.png, a JPEG) to the
output directory as entry.png. Deterministic: the same bytes are
written on every run. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"bundled image not found: {SOURCE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    # Byte-for-byte copy: the file is JPEG data despite the .png name,
    # which the rules allow (format is told apart by its first bytes).
    shutil.copyfile(SOURCE, destination)


if __name__ == "__main__":
    main()
