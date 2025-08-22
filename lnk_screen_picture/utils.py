import time
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

import numpy as np  # type: ignore[import-not-found]


def resize_image(input_path: Path, output_path: Path, new_width: int, new_height: int):
    try:
        img = Image.open(input_path)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)
        print(f"图片已成功调整为 {new_width}x{new_height}，并保存到 {output_path}")
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_path}")
    except Exception as e:
        print(f"发生错误：{e}")


def adjust_contrast(input_path: Path, output_path: Path, factor: float):
    start_time = time.time()
    try:
        image = Image.open(input_path)
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)
        print(f"已保存调整后的图片到: {output_path}")
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_path}")
    print(f"耗时:{time.time()-start_time}")


def adjust_sharp(input_path, output_path, amount):
    start_time = time.time()
    try:
        image = Image.open(input_path)
        sharpened = image.filter(ImageFilter.SHARPEN)
        clarity_image = Image.blend(image, sharpened, alpha=amount * 0.5)
        clarity_image.save(output_path)
        print(f"已保存调整后的图片到: {output_path}")
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_path}")
    print(f"耗时:{time.time()-start_time}")


def adjust_sharp_contrast(
    input_path: Path, output_path: Path, amount: float, factor: float
):
    start_time = time.time()
    try:
        image = Image.open(input_path)
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)

        sharpened = enhanced_image.filter(ImageFilter.SHARPEN)
        clarity_image = Image.blend(enhanced_image, sharpened, alpha=amount * 0.5)
        clarity_image.save(output_path)
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_path}")
    print(f"耗时:{time.time()-start_time}")


def adjust_all(
    input_path: Path,
    output_path: Path,
    amount: float,
    factor: float,

    gray_scale_flag: bool,
    threshold: int,
    width: int|None,
    height: int|None,
):
    start_time = time.time()
    try:
        image = Image.open(input_path)
        print("&"*100,image.height,image.width)

        if image.width > image.height:
            image = image.rotate(90,expand=True)
        if width and height:
            image = image.resize((width, height))  # type: ignore[assignment]
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)
        sharpened = enhanced_image.filter(ImageFilter.SHARPEN)
        image = Image.blend(enhanced_image, sharpened, alpha=amount * 0.5)  # type: ignore[assignment]
        if gray_scale_flag:
            image = floyd_steinberg_dithering(image, threshold)
        image.save(output_path)
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_path}")
    print(f"耗时:{time.time()-start_time}")


def floyd_steinberg_dithering(image, threshold=128):
    img = image.convert("L")
    width, height = img.size
    pixels = np.array(img, dtype=np.float32)

    for i in range(height):
        for j in range(width):
            original = pixels[i, j]
            if original >= threshold:
                pixels[i, j] = 255
            else:
                pixels[i, j] = 0
            error = original - pixels[i, j]
            if j < width - 1:  # 右侧像素
                pixels[i, j + 1] += error * 7 / 16
            if i < height - 1:
                if j > 0:  # 左下像素
                    pixels[i + 1, j - 1] += error * 3 / 16
                pixels[i + 1, j] += error * 5 / 16  # 正下像素
                if j < width - 1:  # 右下像素
                    pixels[i + 1, j + 1] += error * 1 / 16
    result = Image.fromarray(np.uint8(np.clip(pixels, 0, 255)))
    return result



def floyd_steinberg_rgb_dithering(image, threshold=128,base_flag=0):
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # 转换为NumPy数组，分离RGB通道
    img_array = np.array(image, dtype=np.float32)
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    height, width = r.shape

    # 对每个通道分别应用Floyd-Steinberg抖动
    for channel in [r, g, b]:
        for y in range(height):
            for x in range(width):
                # 当前像素值
                old_pixel = channel[y, x]

                # 阈值处理（0-255范围）
                new_pixel = 0 if old_pixel < threshold else 255
                channel[y, x] = new_pixel

                # 计算量化误差
                error = old_pixel - new_pixel

                # 误差扩散到相邻像素
                if x + 1 < width:
                    channel[y, x + 1] += error * 7 / 16
                if x - 1 >= 0 and y + 1 < height:
                    channel[y + 1, x - 1] += error * 3 / 16
                if y + 1 < height:
                    channel[y + 1, x] += error * 5 / 16
                if x + 1 < width and y + 1 < height:
                    channel[y + 1, x + 1] += error * 1 / 16

    # 合并处理后的通道，确保三个通道值相同（真正的黑白）
    # 这里取R通道作为基准，实际应用中也可以取平均值
    if base_flag == "R":
        result_array = np.stack([r, r, r], axis=2).astype(np.uint8)
    elif base_flag == "G":
        result_array = np.stack([g, g, g], axis=2).astype(np.uint8)
    elif base_flag == "B":
        result_array = np.stack([b, b, b], axis=2).astype(np.uint8)
    else:
        result_array = np.mean([r, g, b], axis=0).astype(np.uint8)

    return Image.fromarray(result_array, mode='RGB')


# 使用示例
if __name__ == "__main__":
    # 打开彩色图像
    image = Image.open("example.jpg")

    # 应用RGB Floyd-Steinberg抖动
    dithered_image = floyd_steinberg_rgb_dithering(image)

    # 保存结果
    dithered_image.save("rgb_dithered_black_white.jpg")
