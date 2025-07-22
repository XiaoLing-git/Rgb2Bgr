from pathlib import Path
from tkinter import messagebox

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseEntryControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "串口控制",
        text: str = "连接",
        config_file_path: Optional[Path] = None,
    ):
        super().__init__(master, name)
        self.text = text
        # 指定初始化配置文件路径
        self.config_file_path: Path | None = config_file_path

        self.base_entry = ttk.Entry(self.label_frame, width=8)
        self.base_entry.pack(side="left", padx=5, pady=3, fill="x", expand=True)
        self.base_button = ttk.Button(
            self.label_frame,
            text=self.text,
            width=7,
            style="secondary",
            command=self.get_setup,
        )
        self.base_button.pack(side="left", padx=5, pady=5, fill="x", expand=True)

    def get_setup(self) -> int | None:
        """
        获取输入框的值，
        :return: 若存在，返回串口名，若不存在返回None
        """
        try:
            response = self.base_entry.get().strip()
            response = response.replace(" ", "")
            response = int(response)
            return response
        except ValueError as e:
            messagebox.showinfo("警告", "样本数值必须为整数")
        return None


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseEntryControlElement(app, "hello world")
    app.mainloop()
