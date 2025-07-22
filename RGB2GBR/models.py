import sys
from pathlib import Path

THIS_DIR = (
    Path(sys.executable).parent / "apps" / "lock_pro_wifi"
    if getattr(sys, "frozen", False)
    else Path(__file__).parent
)

BIN_FOLDER = THIS_DIR / "bin"

BIN_FILE_NAME = "libimagetools.so"

BIN_FILE_PATH = BIN_FOLDER / BIN_FILE_NAME