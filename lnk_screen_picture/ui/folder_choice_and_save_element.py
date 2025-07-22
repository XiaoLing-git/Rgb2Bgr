from pathlib import Path
from tkinter import StringVar, filedialog

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class FolderChoiceSaveElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "保存路径选择",
        text: str = "打开文件管理器",
        start: float = 0,
        end: float = 100,
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        self.config_file_path = config_file_path
        self.value: StringVar = StringVar()
        self.start = start
        self.end = end

        self.show_label = ttk.Label(
            self.label_frame, text="未选中任何文件夹", width=7, anchor="w"
        )
        self.show_label.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.base_choice_button = ttk.Button(
            self.label_frame,
            style="success",
            text=self.text,
            command=self.on_click,
        )
        self.base_choice_button.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.base_save_button = ttk.Button(
            self.label_frame,
            style="success",
            text="保存图片",
            command=self.on_click,
        )
        # self.base_save_button.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.base_save_bin_button = ttk.Button(
            self.label_frame,
            style="success",
            text="Generate Bin",
            command=self.on_click,
        )
        self.base_save_bin_button.pack(side="top", padx=5, pady=1, fill="x", expand=True)

    def on_click(self):
        folder_path = filedialog.askdirectory(
            title="选择保存文件路径",
        )
        if folder_path:
            self.show_label["text"] = folder_path
            self.value.set(folder_path)
        print(self.value.get())


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = FolderChoiceSaveElement(app)
    app.mainloop()
