import ctypes
from pathlib import Path
from PIL import Image

import numpy as np

from RGB2GBR.errors import Rgb2BgrException
from RGB2GBR.models import BIN_FILE_PATH


class ImageTools:
    def __init__(self,
                 rgb_file_input_file:Path,
                 bgr_file_output_file:Path
                 # y4_file_output_file:Path
                 ):



        self.rgb_file_input_file = rgb_file_input_file
        self.bgr_file_output_file = bgr_file_output_file
        # self.y4_file_output_file = y4_file_output_file
        self.__assert_attr()


        self.lib = ctypes.cdll.LoadLibrary(str(BIN_FILE_PATH))

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

    def __assert_attr(self):
        if not self.rgb_file_input_file.exists():
            raise FileNotFoundError("File path not exist")
        if not self.bgr_file_output_file.suffix == ".bin":
            raise ValueError("File Suffix should end with |.bin|")


    def load_input_file_to_array(self):
        pil_image = Image.open(self.rgb_file_input_file)
        image_array = np.array(pil_image)
        height, width, channels = image_array.shape
        if channels != 3:
            raise ValueError("File format is not RGB")
        return image_array

    def swap_rgb_bgr(self, input_array):
        """将 BGR 数组转换为 RGB 数组"""
        height, width, channels = input_array.shape
        if channels != 3:
            raise ValueError("输入数组必须是三通道图像")

        output_array = np.empty_like(input_array)
        swap_size = width * height
        self.lib.SWAP_RGB_BGR(input_array, output_array, swap_size)
        return output_array

    def index_mapping_spectra6_aio_y4(self, input_array)->bytes:
        height, width, channels = input_array.shape
        if channels != 3:
            raise ValueError("输入数组必须是三通道图像")
        output_size = (height * width) // 2
        output_array = np.zeros(output_size, dtype=np.uint8)

        self.lib.IndexMapping_Spectra6_AIO_Y4(input_array, output_array, width, height)
        return bytes(output_array)

    def run(self)->None:
        try:
            response = self.swap_rgb_bgr(self.load_input_file_to_array())
            response = self.index_mapping_spectra6_aio_y4(response)
            with open(self.bgr_file_output_file, 'wb') as f:
                f.write(response)
        except Exception as e:
            raise Rgb2BgrException(f"Transform RGB To BRG Fail, Msg: {str(e)}")


