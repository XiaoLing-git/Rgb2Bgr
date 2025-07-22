import sys
from pathlib import Path

if "win" in sys.platform:
    raise SystemError(f"Only call on Linux OS")

THIS_DIR = (
    Path(sys.executable).parent / "RGB2GBR"
    if getattr(sys, "frozen", False)
    else Path(__file__).parent
)

print("RGB2GBR",THIS_DIR)

BIN_FOLDER = THIS_DIR / "bin"

BIN_FILE_NAME = "libimagetools.so"

BIN_FILE_PATH = BIN_FOLDER / BIN_FILE_NAME
