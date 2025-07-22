import sys
from pathlib import WindowsPath

THIS_DIR = (
    WindowsPath(sys.executable).parent / "RGB2GBR"
    if getattr(sys, "frozen", False)
    else WindowsPath(__file__).parent
)

BIN_FOLDER = THIS_DIR / "bin"

BIN_FILE_NAME = "libimagetools.so"

BIN_FILE_PATH = BIN_FOLDER / BIN_FILE_NAME