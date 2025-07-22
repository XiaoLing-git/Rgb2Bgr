import time
from pathlib import Path

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore

from typing import Union, Optional

from base_ui.base import BaseUi
from base_ui.base_button_and_port_control_element import BaseButtonAndPortControlElement
from base_ui.base_mac_show_element import BaseMacShowElement
from base_ui.base_progess_bar_show_element import BaseProgressBarShowElement


class AppBaseControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "Lock Pro BLE",
        config_file_path: Optional[Path] = None,
    ):
        super().__init__(master, name)
        self.config_file_path = config_file_path
        self.button_and_port = BaseButtonAndPortControlElement(
            self.label_frame,
            name="设置&烧录",
            text="烧录",
            config_file_path=self.config_file_path,
        )
        self.mac_label: BaseMacShowElement = BaseMacShowElement(self.label_frame)
        self.progress_bar: BaseProgressBarShowElement = BaseProgressBarShowElement(
            self.label_frame, name="状态栏"
        )

    @property
    def port(self) -> str | None:
        return self.button_and_port.get_setup()

    @property
    def get_mac(self) -> str | None:
        text: str = self.mac_label.label["text"]
        if len(text) == 0:
            return None
        return text

    def set_mac(self, text: str) -> None:
        self.mac_label.setup(text)

    def set_progress_bar(
        self, label_info: str, progress: int, style: str = "success"
    ) -> None:
        self.progress_bar.set_state(label_info, progress, style)


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")
    baseui = AppBaseControlElement(app)
    app.mainloop()
