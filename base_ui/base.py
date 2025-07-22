from typing import List, Union

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore


class BaseUi:
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str,
        label_frame_flag: bool = True,
    ):
        self.__label_frame_flag = label_frame_flag
        self.root = master
        self.name = name
        self.label_frame = self._create_label_frame()
        self.subframe: List[ttk.Frame] = []

    def _create_label_frame(self) -> ttk.Labelframe:
        label_frame = ttk.Labelframe(master=self.root, text=self.name, padding=5)

        label_frame.pack(side="top", fill="x", padx=2, pady=1, expand=1)
        return label_frame


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseUi(app, "hello world")
    app.mainloop()
