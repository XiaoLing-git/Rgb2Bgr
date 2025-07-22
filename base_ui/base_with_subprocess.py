import time
from typing import List, Union
from tkinter import messagebox

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore


class BaseUiWithSubProcess:
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "",
        label_frame_flag: bool = True,
    ):
        self.__label_frame_flag = label_frame_flag
        self.root = master
        self.name = name
        self.sub_process_run_state = False
        self.label_frame = self._create_label_frame()
        self.subframe: List[ttk.Frame] = []
        self.message_count: int = 0

    def _create_label_frame(self) -> ttk.Labelframe:
        if self.__label_frame_flag:
            label_frame = ttk.Labelframe(master=self.root, text=self.name, padding=5)
        else:
            label_frame = ttk.Frame(master=self.root, padding=5)
        label_frame.pack(side="top", fill="x", padx=2, pady=1, expand=1)
        return label_frame

    def sleep(self, delay_time: int):
        start_time = time.time()
        while True:
            if time.time() - start_time > delay_time:
                break
            self.root.update()

    def sub_process_error_call_back(self, error: Exception | None = None):
        if error is None:
            self.root.update()
        else:
            messagebox.showinfo("警告", str(error))
            self.message_count = self.message_count + 1
            self.sub_process_run_state = False


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = BaseUiWithSubProcess(app, "hello world")
    app.mainloop()
