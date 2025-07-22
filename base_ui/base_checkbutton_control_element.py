from pathlib import Path
from tkinter import IntVar

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseCheckButtonControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "串口控制",
        text: str = "黑白",
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        self.check_var = IntVar(value=0)
        self.config_file_path: Path | None = config_file_path

        self.base_button = ttk.Checkbutton(
            self.label_frame,
            text=self.text,
            width=7,
            variable=self.check_var,
            style="success-round-toggle",
            command=self.onclick,
        )
        self.base_button.pack(side="left", padx=5, pady=1, fill="x", expand=True)

    def onclick(self):
        if self.check_var.get() == 1:
            print("enable")
        else:
            print("disable")


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseCheckButtonControlElement(app)
    app.mainloop()
