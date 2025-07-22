from pathlib import Path
from typing import Union, Optional

import ttkbootstrap as ttk  # type: ignore
from ttkbootstrap.constants import *  # type: ignore

from apps.base_ui.base import BaseUi
from apps.base_ui.base_button_control_element import BaseButtonControlElement
from apps.base_ui.base_checkbutton_control_element import BaseCheckButtonControlElement
from apps.base_ui.base_file_choice_element import BaseFileChoiceElement
from apps.base_ui.base_options_select_control_element import BaseOptionsSelectElement
from apps.base_ui.base_scale_control_element import BaseScaleControlElement
from apps.lnk_screen_picture.ui.folder_choice_and_save_element import (
    FolderChoiceSaveElement,
)


class PictureControlElement(BaseUi):
    def __init__(
        self,
        master: Union[ttk.Frame, ttk.Window],
        name: str = "图片处理单元",
        config_file_path: Optional[Path] = None,
    ):
        super().__init__(master, name)
        self.config_file_path = config_file_path
        self.label_frame.pack(fill="both", side="right")
        self.file_choice: BaseFileChoiceElement = BaseFileChoiceElement(
            self.label_frame
        )
        self.pic_size: BaseOptionsSelectElement = BaseOptionsSelectElement(
            self.label_frame, "图片规格设置"
        )
        self.sharp: BaseScaleControlElement = BaseScaleControlElement(
            self.label_frame, name="鲜明度调节", start=0, end=4.0
        )
        self.sharp.value.set(1)
        self.sharp.show_label["text"] = 1
        self.contrast: BaseScaleControlElement = BaseScaleControlElement(
            self.label_frame, name="对比度调节", start=0, end=5
        )
        self.contrast.value.set(1)
        self.contrast.show_label["text"] = 1

        self.de_shake: BaseScaleControlElement = BaseScaleControlElement(
            self.label_frame, name="黑白处理二值化阈值设置", start=0, end=255
        )
        self.de_shake.value.set(128)
        self.de_shake.show_label["text"] = 128

        self.de_color: BaseCheckButtonControlElement = BaseCheckButtonControlElement(
            self.label_frame, name="黑白处理使能"
        )

        self.save: FolderChoiceSaveElement = FolderChoiceSaveElement(
            self.label_frame, name="保存图片"
        )
        self.label_frame.pack_propagate(False)
        self.label_frame.configure(width=500, height=1000)
        self.label_frame.pack(fill="y", expand="y", side="right")


if __name__ == "__main__":
    app = ttk.Window(title="this is Test")

    baseui = PictureControlElement(app)
    app.mainloop()
