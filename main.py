import ttkbootstrap as ttk  # type: ignore

from lnk_screen_picture.app import LnkScreenPictureApp


def start_app():
    version = "1.0.0"
    root = ttk.Window(title=f"水墨屏图片处理 {version}")

    LnkScreenPictureApp(root)
    root.mainloop()


if __name__ == "__main__":
    start_app()
