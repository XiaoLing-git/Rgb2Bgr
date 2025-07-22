from pathlib import Path
from tkinter import DoubleVar, IntVar

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseScaleControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "调节",
        text: str = "锁定",
        start: float = 0,
        end: float = 100,
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        self.config_file_path = config_file_path
        self.value: DoubleVar = DoubleVar()
        self.value.set(0)
        self.start = start
        self.end = end

        self.check_var = IntVar(value=0)

        self.show_label = ttk.Label(
            self.label_frame, text=self.value.get(), width=7, anchor="center"
        )
        self.show_label.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.base_scale = ttk.Scale(
            self.label_frame,
            style="success",
            from_=self.start,
            to=self.end,
            variable=self.value,
            command=self.on_move,
        )
        self.base_scale.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.base_scale.bind("<ButtonRelease-1>", lambda event: self.on_mouse_release())

        # self.base_button = ttk.Checkbutton(
        #     self.label_frame,
        #     text=self.text,
        #     width=7,
        #     variable=self.check_var,
        #     style="success-round-toggle",
        #     command=self.onclick,
        # )
        # self.base_button.pack(side="left", padx=5, pady=1, fill="x", expand=True)

    def onclick(self):
        if self.check_var.get() == 1:
            self.base_scale.config(state="disabled")
        else:
            self.base_scale.config(state="success")

    def on_move(self, value):
        self.value.set(round(float(value), 2))
        self.show_label["text"] = round(float(value), 2)

    def on_mouse_release(self):
        print(self.value.get())


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseScaleControlElement(app)
    app.mainloop()
