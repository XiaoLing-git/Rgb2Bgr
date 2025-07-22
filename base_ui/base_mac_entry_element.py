from pathlib import Path

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseMacEntryElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "Mac输入",
        config_file_path: Optional[Path] = None,
        label_frame_flag: bool = True,
    ):
        super().__init__(master, name, label_frame_flag)

        self.base_entry = ttk.Entry(
            self.label_frame,
        )
        self.base_entry.pack(side="left", padx=5, pady=10, fill="x", expand=True)

    def get_setup(self):
        return self.base_entry.get()


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseMacEntryElement(app)
    app.mainloop()
