import ctypes
import numpy as np

from RGB2GBR.models import BIN_FILE_PATH


class ImageTools:
    def __init__(self):
        # 加载共享库
        print(BIN_FILE_PATH)
        self.lib = ctypes.cdll.LoadLibrary(str(BIN_FILE_PATH))

        # 设置函数参数和返回类型
        self.lib.SWAP_RGB_BGR.argtypes = [
            np.ctypeslib.ndpointer(dtype=np.uint8, flags='C_CONTIGUOUS'),
            np.ctypeslib.ndpointer(dtype=np.uint8, flags='C_CONTIGUOUS'),
            ctypes.c_int
        ]

        self.lib.IndexMapping_Spectra6_AIO_Y4.argtypes = [
            np.ctypeslib.ndpointer(dtype=np.uint8, flags='C_CONTIGUOUS'),
            np.ctypeslib.ndpointer(dtype=np.uint8, flags='C_CONTIGUOUS'),
            ctypes.c_int,
            ctypes.c_int
        ]

    def swap_rgb_bgr(self, input_array):
        """将 BGR 数组转换为 RGB 数组"""
        height, width, channels = input_array.shape
        if channels != 3:
            raise ValueError("输入数组必须是三通道图像")

        output_array = np.empty_like(input_array)
        swap_size = width * height
        self.lib.SWAP_RGB_BGR(input_array, output_array, swap_size)
        return output_array

    def index_mapping_spectra6_aio_y4(self, input_array):
        """对 RGB888 图像进行 Spectra6 AIO Y4 映射"""
        height, width, channels = input_array.shape
        if channels != 3:
            raise ValueError("输入数组必须是三通道图像")

        # 输出数组大小为输入的一半（Y4 格式）
        output_size = (height * width) // 2
        output_array = np.zeros(output_size, dtype=np.uint8)

        self.lib.IndexMapping_Spectra6_AIO_Y4(input_array, output_array, width, height)
        return output_array


# 使用示例
if __name__ == "__main__":
    # 初始化库
    image_tools = ImageTools()

    width, height = 100, 100
    bgr_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # 转换 BGR 到 RGB
    rgb_image = image_tools.swap_rgb_bgr(bgr_image)

    y4_data = image_tools.index_mapping_spectra6_aio_y4(rgb_image)

    print(f"原始 BGR 图像形状: {bgr_image.shape}")
    print(f"转换后的 RGB 图像形状: {rgb_image.shape}")
    print(f"Y4 数据大小: {y4_data.shape}")