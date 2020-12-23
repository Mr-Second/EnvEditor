# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KvWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc


class Ui_kvWin(object):
    def setupUi(self, kvWin):
        kvWin.setObjectName("kvWin")
        kvWin.resize(471, 229)
        kvWin.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(kvWin)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(kvWin)
        self.frame.setStyleSheet("#frame {\n"
                                 "    border: 1px solid black;\n"
                                 "    border-radius: 5px;\n"
                                 "    \n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.994, y2:1, "
                                 "stop:0 rgba(159, 165, 213, 255), "
                                 "stop:1 rgba(232, 245, 200, 255));\n "
                                 "}\n"
                                 "\n"
                                 "#findFileBtn {\n"
                                 "    border: none;\n"
                                 "    border-image: url(:/imgs/openFile.png);\n"
                                 "}\n"
                                 "#findFileBtn:hover {\n"
                                 "    border-image: url(:/imgs/openFile_hover.png);\n"
                                 "}\n"
                                 "#findFileBtn:pressed {\n"
                                 "    border-image: url(:/imgs/openFile_pressed.png);\n"
                                 "}\n"
                                 "\n"
                                 "#confirmBtn {\n"
                                 "    border: none;\n"
                                 "    border-image: url(:/imgs/confirm.png);\n"
                                 "}\n"
                                 "\n"
                                 "#confirmBtn:hover {\n"
                                 "    border-image: url(:/imgs/confirm_hover.png);\n"
                                 "}\n"
                                 "\n"
                                 "#confirmBtn:pressed {\n"
                                 "    border-image: url(:/imgs/confirm_pressed.png);\n"
                                 "}\n"
                                 "\n"
                                 "#cancelBtn {\n"
                                 "    border: none;\n"
                                 "    border-image: url(:/imgs/cancel.png);\n"
                                 "}\n"
                                 "\n"
                                 "#cancelBtn:hover {\n"
                                 "    border-image: url(:/imgs/cancel_hover.png);\n"
                                 "}\n"
                                 "\n"
                                 "#cancelBtn:pressed {\n"
                                 "    border-image: url(:/imgs/cancel_pressed.png);\n"
                                 "}\n"
                                 "\n"
                                 "#nameInput {\n"
                                 "    font: 11pt \"Source Code Pro\";\n"
                                 "    padding: 2px;\n"
                                 "    border: 2px solid #95a5a6;\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "    border-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "#nameInput:hover {\n"
                                 "    border-color: #7f8c8d;\n"
                                 "}\n"
                                 "\n"
                                 "#nameInput:focus {\n"
                                 "    border-color: #bdc3c7;\n"
                                 "}\n"
                                 "\n"
                                 "#pathInput {\n"
                                 "    padding: 2px;\n"
                                 "    font: 11pt \"Source Code Pro\";\n"
                                 "    border: 2px solid #95a5a6;\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "    border-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "#pathInput:hover {\n"
                                 "    border-color: #7f8c8d;\n"
                                 "}\n"
                                 "\n"
                                 "#pathInput:focus {\n"
                                 "    border-color: #bdc3c7;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cancelBtn = QtWidgets.QPushButton(self.frame)
        self.cancelBtn.setGeometry(QtCore.QRect(320, 180, 41, 41))
        self.cancelBtn.setText("")
        self.cancelBtn.setObjectName("cancelBtn")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(37, 59, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.valueLabel = QtWidgets.QLabel(self.frame)
        self.valueLabel.setGeometry(QtCore.QRect(37, 120, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.valueLabel.setFont(font)
        self.valueLabel.setObjectName("valueLabel")
        self.findFileBtn = QtWidgets.QPushButton(self.frame)
        self.findFileBtn.setGeometry(QtCore.QRect(420, 120, 40, 40))
        self.findFileBtn.setText("")
        self.findFileBtn.setObjectName("findFileBtn")
        self.nameInput = QtWidgets.QLineEdit(self.frame)
        self.nameInput.setGeometry(QtCore.QRect(167, 60, 241, 40))
        self.nameInput.setMinimumSize(QtCore.QSize(0, 25))
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.pathInput = QtWidgets.QLineEdit(self.frame)
        self.pathInput.setGeometry(QtCore.QRect(167, 120, 241, 40))
        self.pathInput.setMinimumSize(QtCore.QSize(0, 25))
        self.pathInput.setText("")
        self.pathInput.setObjectName("pathInput")
        self.confirmBtn = QtWidgets.QPushButton(self.frame)
        self.confirmBtn.setGeometry(QtCore.QRect(200, 170, 60, 60))
        self.confirmBtn.setText("")
        self.confirmBtn.setObjectName("confirmBtn")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(30, 10, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setText("")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.keyWarningLabel = QtWidgets.QLabel(self.frame)
        self.keyWarningLabel.setGeometry(QtCore.QRect(170, 100, 235, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.keyWarningLabel.setFont(font)
        self.keyWarningLabel.setTextFormat(QtCore.Qt.AutoText)
        self.keyWarningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keyWarningLabel.setObjectName("keyWarningLabel")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(kvWin)
        self.cancelBtn.clicked.connect(kvWin.reject)
        self.findFileBtn.clicked.connect(kvWin.openFileDialog)
        self.confirmBtn.clicked.connect(kvWin.confirm)
        self.nameInput.textChanged['QString'].connect(self.keyWarningLabel.hide)
        self.nameInput.editingFinished.connect(kvWin.checkVariable)
        QtCore.QMetaObject.connectSlotsByName(kvWin)

    def retranslateUi(self, kvWin):
        _translate = QtCore.QCoreApplication.translate
        kvWin.setWindowTitle(_translate("kvWin", "AddKeyValue"))
        self.nameLabel.setText(_translate("kvWin", "variable name"))
        self.valueLabel.setText(_translate("kvWin", "variable value "))
        self.keyWarningLabel.setText(_translate("kvWin",
                                                "<html><head/><body><p><span style=\" font-weight:600; "
                                                "color:#ff0000;\">the variable is already "
                                                "existing!</span></p></body></html>"))


