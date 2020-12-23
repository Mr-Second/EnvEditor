from PyQt5.QtCore import Qt, QEventLoop
from PyQt5.QtWidgets import QWidget

from InfoWinModel import Ui_Form


class InfoDialog(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(InfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

    def exec(self):
        self.show()
        eventLoop = QEventLoop(self)
        eventLoop.exec()

