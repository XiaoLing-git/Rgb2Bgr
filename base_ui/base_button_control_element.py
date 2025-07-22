from pathlib import Path

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseButtonControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "串口控制",
        text: str = "按钮",
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        self.config_file_path: Path | None = config_file_path

        self.base_button = ttk.Button(
            self.label_frame,
            text=self.text,
            width=7,
            style="success",
            command=self.onclick,
        )
        self.base_button.pack(side="left", padx=5, pady=1, fill="x", expand=True)

    def onclick(self):
        print("button clicked")


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseButtonControlElement(app, "hello world")
    app.mainloop()
