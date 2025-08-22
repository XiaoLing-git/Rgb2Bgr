import shutil
import time
from pathlib import Path
from tkinter import TclError, messagebox
from typing import Union, Optional

import ttkbootstrap as ttk  # type: ignore
from PIL import Image, ImageTk
from ttkbootstrap.constants import *  # type: ignore

from RGB2GBR.api import ImageTools
from RGB2GBR.errors import Rgb2BgrException
from base_ui.base import BaseUi
from lnk_screen_picture.model import TEMP_FOLDER, SAVE_FOLDER
from lnk_screen_picture.ui.picture_control_element import PictureControlElement
from lnk_screen_picture.ui.picture_show_element import PictureShowElement
from lnk_screen_picture.utils import adjust_all


class LnkScreenPictureApp(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "水墨屏图片预处理",
        config_file_path: Optional[Path] = None,
    ):
        super().__init__(master, name)

        self.config_file_path = config_file_path
        self.show: PictureShowElement = PictureShowElement(self.label_frame)
        self.control: PictureControlElement = PictureControlElement(self.label_frame)
        self.label_frame.pack(fill="both")
        self.control.file_choice.base_button.configure(
            command=self.choice_file_and_show
        )
        self.control.pic_size.idle_port_check.bind(
            "<<ComboboxSelected>>", self.idle_port_check_onclick
        )
        self.control.pic_size.idle_port_check.bind(
            "<Return>", self.idle_port_check_onclick
        )

        self.control.contrast.base_scale.bind(
            "<ButtonRelease-1>", lambda event: self.adjust_all_setup()
        )
        self.control.sharp.base_scale.bind(
            "<ButtonRelease-1>", lambda event: self.adjust_all_setup()
        )
        self.control.de_shake.base_scale.bind(
            "<ButtonRelease-1>", lambda event: self.adjust_all_setup()
        )
        self.control.de_color.base_button.configure(command=self.adjust_all_setup)
        self.control.save.base_save_button.configure(command=self.save_button_onclick)
        self.control.save.base_save_bin_button.configure(
            command=self.bin_save_button_onclick
        )

        self.selected_file: Path | None = None
        self.last_file: Path | None = None

    def idle_port_check_onclick(self, event):
        self.control.pic_size.on_select(event)
        self.adjust_all_setup()

    def choice_file_and_show(self):
        self.control.file_choice.on_click()
        self.adjust_all_setup()

    def adjust_all_setup(self):
        pic_width: int | None = None  # type: ignore
        pic_height: int | None = None  # type: ignore
        file_path = self.control.file_choice.value.get()
        if len(file_path) == 0:
            messagebox.showinfo("警告", "未选中图片")
        file_path = Path(file_path)
        if not file_path.exists():
            messagebox.showinfo("警告", "文件不存在")
        try:
            option_str = self.control.pic_size.idle_port_check.get()
            response = option_str.split("x")
            if len(response) !=2:
                pic_width = None
                pic_height = None
            else:
                pic_width = int(response[0])
                pic_height = int(response[1])
        except AssertionError as e:
            messagebox.showinfo("警告", "分辨率格式输出异常，格式：整数x整数")
        except ValueError as e:
            messagebox.showinfo("警告", "分辨率格式输出异常，格式：整数x整数")

        try:
            file_path = self.control.file_choice.value.get()
            file_path = Path(file_path)
            contrast_value = float(self.control.contrast.value.get())
            sharp_value = float(self.control.sharp.value.get())
            de_color = self.control.de_color.check_var.get()
            de_shake = int(self.control.de_shake.value.get())

            if file_path.exists():
                new_file_path = TEMP_FOLDER / f"{int(time.time())}_{file_path.name}"
                adjust_all(
                    file_path,
                    new_file_path,
                    sharp_value,
                    contrast_value,
                    bool(de_color),
                    de_shake,
                    pic_height,
                    pic_width,
                )
                self.show_picture(str(new_file_path))
                self.selected_file = file_path
                self.last_file = new_file_path
            else:
                messagebox.showinfo("警告", "文件不存在")
        except AttributeError as e:
            # print(e)
            messagebox.showinfo("警告", "未选中文件")
            self.control.sharp.value.set(1)
            self.control.sharp.show_label["text"] = 1
            self.control.contrast.value.set(1)
            self.control.contrast.show_label["text"] = 1

    def show_picture(self, file_path: str):
        try:
            photo = ttk.PhotoImage(file=file_path)
        except TclError as e:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
        self.show.show_picture["image"] = photo
        self.show.show_picture.image = photo

    def save_button_onclick(self):
        file_path = self.control.file_choice.value.get()
        if len(file_path) == 0:
            messagebox.showinfo("警告", "未选中图片")
            return
        file_path = Path(file_path)
        if not file_path.exists():
            messagebox.showinfo("警告", "文件不存在")
            return

        folder_path = self.control.save.value.get()
        option_str = self.control.pic_size.idle_port_check.get()
        contrast_value = float(self.control.contrast.value.get())
        sharp_value = float(self.control.sharp.value.get())
        de_color = self.control.de_color.check_var.get()

        if len(folder_path) > 0 and Path(folder_path).exists():
            shutil.copy(
                self.last_file,
                Path(folder_path)
                / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
            )
        else:
            shutil.copy(
                self.last_file,
                SAVE_FOLDER
                / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
            )

    def bin_save_button_onclick(self):
        try:
            print("bin_save_button_onclick was call")
            file_path = self.control.file_choice.value.get()
            if len(file_path) == 0:
                messagebox.showinfo("警告", "未选中图片")
                return
            file_path = Path(file_path)
            if not file_path.exists():
                messagebox.showinfo("警告", "文件不存在")
                return

            folder_path = self.control.save.value.get()
            option_str = self.control.pic_size.idle_port_check.get()
            contrast_value = float(self.control.contrast.value.get())
            sharp_value = float(self.control.sharp.value.get())
            de_color = self.control.de_color.check_var.get()

            if len(folder_path) > 0 and Path(folder_path).exists():
                shutil.copy(
                    self.last_file,
                    Path(folder_path)
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
                )
                image_tool = ImageTools(
                    Path(folder_path)
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
                    Path(folder_path)
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.stem}.bin",
                )
                Path(
                    folder_path
                ) / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.stem}.bin"
                image_tool.run()
            else:
                shutil.copy(
                    self.last_file,
                    SAVE_FOLDER
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
                )
                image_tool = ImageTools(
                    SAVE_FOLDER
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.name}",
                    SAVE_FOLDER
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.stem}.bin",
                )
                print(
                    Path(folder_path)
                    / f"{int(time.time())}_{sharp_value}_{contrast_value}_{option_str}_{de_color}_{self.selected_file.stem}.bin"
                )
                image_tool.run()
        except Rgb2BgrException as e:
            messagebox.showinfo("Error", "不支持黑白图片")
        except Exception as e:
            messagebox.showinfo("Error", "")