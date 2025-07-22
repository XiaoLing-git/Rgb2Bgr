import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore

from typing import Union, Any

from base_ui.base import BaseUi


class GroupControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "组管理",
        base_element: Any = None,
    ):
        super().__init__(master, name)

        self.group_frame = ttk.Frame(
            self.label_frame,
        )
        self.group_frame.pack(side="left", fill="both", expand=True)

        self.base_element = base_element
        self.edit_button = ttk.Button(
            self.group_frame,
            text="|添加设备|",
            padding=(20, 40),
            command=self.add_device,
            style="secondary-outline",
        )
        self.edit_button.pack(side="left", padx=5, pady=5, fill="both")

    def add_device(self) -> None:
        print("add_device was call")
        base_button = ttk.Button(
            self.group_frame, text="|this is Demo|", padding=(20, 40), style="secondary"
        )
        base_button.pack(
            side="left",
            padx=5,
            pady=5,
            fill="both",
            expand=True,
            before=self.edit_button,
        )


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = GroupControlElement(app, "组管理")
    app.mainloop()
