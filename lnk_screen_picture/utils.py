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
    width: int,
    height: int,
    gray_scale_flag: bool,
    threshold: int,
):
    start_time = time.time()
    try:
        image = Image.open(input_path)
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
