import numpy as np

from RGB2GBR.api import ImageTools
from RGB2GBR.models import THIS_DIR, BIN_FOLDER, BIN_FILE_PATH

if __name__ == '__main__':
    print(THIS_DIR)
    print(BIN_FOLDER)
    print(BIN_FILE_PATH)
    # print(THIS_DIR)

    image_tools = ImageTools()

    width, height = 100, 100
    bgr_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # 转换 BGR 到 RGB
    rgb_image = image_tools.swap_rgb_bgr(bgr_image)

    y4_data = image_tools.index_mapping_spectra6_aio_y4(rgb_image)

    print(f"原始 BGR 图像形状: {bgr_image.shape}")
    print(f"转换后的 RGB 图像形状: {rgb_image.shape}")
    print(f"Y4 数据大小: {y4_data.shape}")