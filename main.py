from pathlib import Path

import numpy as np

from RGB2GBR.api import ImageTools
from RGB2GBR.models import THIS_DIR, BIN_FOLDER, BIN_FILE_PATH

if __name__ == '__main__':
    # print(THIS_DIR)
    # print(BIN_FOLDER)
    # print(BIN_FILE_PATH)
    # print(THIS_DIR)

    pic_path = THIS_DIR.parent / "20250625-160750.jpg"
    image_tools = ImageTools(pic_path,Path("./result.bin"))

    image_tools.run()