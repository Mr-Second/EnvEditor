import os
import sys
import typing

from PyQt5 import QtCore, sip
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget
from ctypes.wintypes import MSG

from win32con import WM_NCACTIVATE

from KvWinModel import Ui_kvWin


class PopDialog(QDialog, Ui_kvWin):
    signal = pyqtSignal(dict)

    def __init__(self, parent: QWidget, existingItems: list):
        super(PopDialog, self).__init__(parent)
        self.setupUi(self)
        xDirMoveLength = parent.geometry().center().x() - int(self.width() / 2) - self.geometry().x()
        yDirMoveLength = parent.geometry().center().y() - int(self.height() / 2) - self.geometry().y()
        self.move(xDirMoveLength, yDirMoveLength)

        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.keyWarningLabel.hide()

        self.existingItems = existingItems

    def connectWithThis(self, slotFunc):
        self.signal.connect(slotFunc)

    def openFileDialog(self):
        res = QFileDialog.getExistingDirectory(self, "Choose Fold Path", ".")
        if os.path.isdir(res):
            self.pathInput.setText(res)

    def confirm(self):
        if len(self.nameInput.text()) == 0:
            self.nameInput.setStyleSheet("border-color: #e84118")
        elif len(self.pathInput.text()) == 0:
            self.pathInput.setStyleSheet("border-color: #e84118")
        elif not self.checkVariable():
            pass
        else:
            message = {
                "name": self.nameInput.text(),
                "value": self.pathInput.text()
            }
            self.signal.emit(message)
            self.accept()

    def checkVariable(self):
        variableName = self.nameInput.text()
        for item in self.existingItems:
            if item.lower() == variableName.lower():
                self.keyWarningLabel.show()
                return False
        return True
