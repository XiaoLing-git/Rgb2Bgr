from pathlib import Path

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseMacShowElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "Mac",
        text: str = "None",
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)
        self.text = text
        self.config_file_path: Path | None = config_file_path

        self.label = ttk.Label(
            self.label_frame,
            text=self.text,
            anchor="center",
            font=("SimHei", 10, "bold"),
        )
        self.label.pack(side="left", padx=5, pady=10, fill="x", expand=True)

    def setup(self, text: str):
        self.label["text"] = text
        self.label.update()


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseMacShowElement(app)
    baseui.setup("hello worl dasdasdagvd")
    app.mainloop()
