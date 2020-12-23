from PyQt5.QtWidgets import QDialog

from MsgBoxModel import Ui_Dialog


class MsgBox(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MsgBox, self).__init__(parent)
        self.setupUi(self)
