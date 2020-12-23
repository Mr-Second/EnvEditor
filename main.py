import ctypes
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

from envEditor import env_editor
from MsgBox import MsgBox
import icons_rc


def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except WindowsError as e:
        print(e)
        return False


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    if not is_admin():
        msgBox = MsgBox()
        msgBox.setWindowTitle("WARNING")
        msgBox.exec_()
        sys.exit(-1)
    else:
        editor = env_editor()
        editor.setApp(app)
        editor.show()
        sys.exit(app.exec_())


