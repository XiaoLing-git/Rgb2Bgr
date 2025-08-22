import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore
from typing import Union, Optional

from base_ui.base import BaseUi


class BaseOptionsSelectElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "串口控制",
        options: list[str] = ["2560x1440", "1600x1200", "800x480",""],
        label_frame_flag: bool = True,
    ) -> None:
        super().__init__(master, name, label_frame_flag)
        self.options = options

        combobox_values = self.options
        self.idle_port_check = ttk.Combobox(
            self.label_frame, width=8, values=combobox_values
        )
        self.idle_port_check.set(options[-1])
        self.idle_port_check.pack(side="left", padx=5, pady=1, fill="x", expand=1)
        self.idle_port_check.bind("<<ComboboxSelected>>", self.on_select)

    def get_setup(self) -> str | None:
        """
        获取输入框的值，
        :return: 若存在，返回串口名，若不存在返回None
        """
        current_value = self.idle_port_check.get()
        if len(current_value) == 0:
            return None
        return current_value.strip()

    def on_select(self, event) -> None:
        choice = self.idle_port_check.get()
        self.idle_port_check.set(choice)
        print(choice)


if __name__ == "__main__":

    app = ttk.Window(title="this is Test")
    baseui = BaseOptionsSelectElement(
        app,
    )
    app.mainloop()
