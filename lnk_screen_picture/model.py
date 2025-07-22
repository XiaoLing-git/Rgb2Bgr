import sys
from pathlib import Path

THIS_DIR = (
    Path(sys.executable).parent / "Rgb2Bgr" / "lnk_screen_picture"
    if getattr(sys, "frozen", False)
    else Path(__file__).parent
)

TEMP_FOLDER = THIS_DIR / "temp"

SAVE_FOLDER = THIS_DIR / "save"
