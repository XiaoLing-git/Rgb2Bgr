from pathlib import Path
from typing import Union, Optional

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore

from apps.base_ui.base import BaseUi


class PictureShowElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "图片显示单元",
        config_file_path: Optional[Path] = None,
    ):
        super().__init__(master, name)
        self.config_file_path = config_file_path
        self.label_frame.pack(fill="both")
        self.label_frame.pack_propagate(False)
        self.label_frame.configure(width=1200, height=1000)
        self.label_frame.pack(side="left")

        self.show_picture: ttk.Label = ttk.Label(
            self.label_frame, padding=10, anchor="center"
        )
        self.show_picture.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = PictureShowElement(app)
    app.mainloop()
