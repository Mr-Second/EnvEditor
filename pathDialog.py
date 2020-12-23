import os

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog

from ValueWinModel import Ui_Dialog


class PathDialog(QDialog, Ui_Dialog):
    signal = pyqtSignal(str)

    def __init__(self, parent: QWidget, isOpenFileBtnShown=True):
        super(PathDialog, self).__init__(parent)
        self.setupUi(self)
        xDirMoveLength = parent.geometry().center().x() - int(self.width() / 2) - self.geometry().x()
        yDirMoveLength = parent.geometry().center().y() - int(self.height() / 2) - self.geometry().y()
        self.move(xDirMoveLength, yDirMoveLength)

        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.keyWarningLabel.hide()

        if not isOpenFileBtnShown:
            self.findFileBtn.hide()
            self.valueLabel.setText("Value:")
            self.keyWarningLabel.setText("value can't be empty!")

    def openFileDialog(self):
        res = QFileDialog.getExistingDirectory(self, "Choose Fold Path", ".")
        self.pathInput.setText(res)

    def connectWithThis(self, slotFunc):
        self.signal.connect(slotFunc)

    def confirmBtnClicked(self):
        if len(self.pathInput.text()) == 0:
            self.keyWarningLabel.show()
            return
        else:
            self.signal.emit(self.pathInput.text())
            self.accept()
