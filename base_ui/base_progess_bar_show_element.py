import time

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore

from ttkbootstrap import Progressbar, Label

from typing import Union

from base_ui.base import BaseUi


class BaseProgressBarShowElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "进度条",
        text: str = "",
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        top_frame = ttk.Frame(self.label_frame, height=60)
        top_frame.pack(side="top", fill="x", padx=2, pady=1, expand=1)
        top_frame.pack_propagate(False)
        self.base_progress_bar = Progressbar(top_frame)

        self.base_progress_bar.pack(side="top", padx=5, pady=1, fill="x", expand=True)

        self.statement_label = Label(top_frame, style="default", text="IDLE")
        self.statement_label.pack(side="top", padx=5, pady=1, fill="x", expand=True)

    def set_state(self, label_info: str, progress: int, style: str = "success"):
        assert 0 <= progress <= 100
        self.base_progress_bar["value"] = progress
        self.statement_label["text"] = label_info
        self.base_progress_bar.configure(style=f"{style}.Horizontal.TProgressbar")
        self.base_progress_bar.update()
        self.statement_label.update()


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseProgressBarShowElement(app)

    for i in range(5):
        time.sleep(1)
        baseui.set_state(f"count{i}", (i + 1) * 20)
    baseui.set_state(f"count down", 100, "primary")
    app.mainloop()
