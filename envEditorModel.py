# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnvEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("* {\n"
                                 "    font: 8pt \"Source Code Pro for Powerline\";\n"
                                 "}\n"
                                 "#frame {\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba("
                                 "91, 77, 163, 255), stop:1 rgba(112, 53, 160, 255));\n "
                                 "    border: 1px solid black;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "#closeBtn {\n"
                                 "    border-radius: 10px;\n"
                                 "    background-color: rgba(255, 0, 0, 255);\n"
                                 "}\n"
                                 "\n"
                                 "#closeBtn:hover {\n"
                                 "    background-color: rgba(255, 0, 0, 150);\n"
                                 "}\n"
                                 "\n"
                                 "#closeBtn:pressed {\n"
                                 "        background-color: rgba(255, 0, 0, 80);\n"
                                 "}\n"
                                 "\n"
                                 "#maxBtn{\n"
                                 "    border-radius: 10px;\n"
                                 "    background-color: rgba(231, 231, 115, 255);\n"
                                 "}\n"
                                 "\n"
                                 "#maxBtn:hover{\n"
                                 "    background-color: rgba(231, 231, 115, 150);\n"
                                 "}\n"
                                 "\n"
                                 "#maxBtn:pressed{\n"
                                 "    background-color: rgba(231, 231, 115, 80);\n"
                                 "}\n"
                                 "\n"
                                 "#minBtn {\n"
                                 "    border-radius: 10px;\n"
                                 "    background-color:  rgba(77, 167, 219, 255);\n"
                                 "}\n"
                                 "\n"
                                 "#minBtn:hover {\n"
                                 "    background-color:  rgba(77, 167, 219, 150);\n"
                                 "}\n"
                                 "\n"
                                 "#minBtn:pressed {\n"
                                 "    background-color:  rgba(77, 167, 219, 80);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeWidget {\n"
                                 "        background-color: rgba(255, 255, 255, 0);\n"
                                 "}\n"
                                 "QTreeView::branch:has-children:!has-siblings:closed,"
                                 "QTreeView::branch:closed:has-children:has-siblings{\n "
                                 "    border-image: none;\n"
                                 "     image: url(:/imgs/plus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:open:has-children:!has-siblings,QTreeView::branch:open:has-children:has-siblings{\n"
                                 "    border-image: none;\n"
                                 "    image: url(:/imgs/minus.png);\n"
                                 "}\n"
                                 "\n"
                                 "#expandBtn {\n"
                                 "    border-radius: 20px;\n"
                                 "    border-width: 6px;\n"
                                 "    border-image: url(:/imgs/expand.png);\n"
                                 "    background-color: rgba(170, 85, 255, 50);\n"
                                 "}\n"
                                 "#expandBtn:hover {\n"
                                 "    background-color: rgba(170, 85, 255, 100);\n"
                                 "    border-image: url(:/imgs/expand_hover.png);\n"
                                 "}\n"
                                 "\n"
                                 "#expandBtn:pressed {\n"
                                 "    background-color: rgba(170, 85, 255, 200);\n"
                                 "    border-image: url(:/imgs/expand_pressed.png);\n"
                                 "}\n"
                                 "\n"
                                 "#narrowBtn {\n"
                                 "    border-radius: 20px;\n"
                                 "    border-width: 6px;\n"
                                 "    border-image: url(:/imgs/narrow.png);\n"
                                 "    background-color: rgba(170, 85, 255, 50);\n"
                                 "}\n"
                                 "\n"
                                 "#narrowBtn:hover {\n"
                                 "    border-image: url(:/imgs/narrow_hover.png);\n"
                                 "    background-color: rgba(170, 85, 255, 100);\n"
                                 "}\n"
                                 "\n"
                                 "#narrowBtn:pressed {\n"
                                 "    border-image: url(:/imgs/narrow_pressed.png);\n"
                                 "    background-color: rgba(170, 85, 255, 200);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "    height:20px;\n"
                                 "    border: 1px solid black;\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "    padding: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected {\n"
                                 "    background-color: rgba(255, 255, 255, 200);\n"
                                 "    \n"
                                 "}\n"
                                 "QTabBar::tab:!selected{\n"
                                 "    background-color: rgba(255, 255, 255, 100);    \n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    border: 1px solid black;\n"
                                 "    border-bottom-left-radius: 5px;\n"
                                 "    border-bottom-right-radius: 5px;\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#detailsTab {\n"
                                 "    border: none;        \n"
                                 "    gridline-color:rgb(207, 207, 207);\n"
                                 "    font: 10pt \"华文楷体\";\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "}\n"
                                 "\n"
                                 "#hintTab {\n"
                                 "    border: none;\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "}\n"
                                 "\n"
                                 "#hintTab::item {\n"
                                 "    border-bottom: 1px solid rgba(207, 207, 207, 100)\n"
                                 "}\n"
                                 "\n"
                                 "#machineLabel {\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "    font-size: 12px;\n"
                                 "}\n"
                                 "\n"
                                 "#userLabel {\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "    font-size: 12px;\n"
                                 "}\n"
                                 "\n"
                                 "#computerNameLabel {\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "}\n"
                                 "\n"
                                 "#userNameLabel {\n"
                                 "    color: rgb(216, 216, 216);\n"
                                 "}\n"
                                 "\n"
                                 "#addBtn {\n"
                                 "    border-image: url(:/imgs/add.png);\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "}\n"
                                 "#addBtn:hover {\n"
                                 "    border-image: url(:/imgs/add_hover.png);\n"
                                 "}\n"
                                 "#addBtn:pressed {\n"
                                 "    border-image: url(:/imgs/add pressed.png);\n"
                                 "}\n"
                                 "#addBtn:disabled {\n"
                                 "    border-image: url(:/imgs/add_disable.png);\n"
                                 "}\n"
                                 "\n"
                                 "#delBtn {\n"
                                 "    border-image: url(:/imgs/delete.png);\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#delBtn:hover {\n"
                                 "    border-image: url(:/imgs/delete_hover.png);\n"
                                 "}\n"
                                 "#delBtn:pressed {\n"
                                 "    border-image: url(:/imgs/delete_pressed.png);\n"
                                 "}\n"
                                 "#delBtn:disabled {\n"
                                 "    border-image: url(:/imgs/delete_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#modifyBtn {\n"
                                 "    border-image: url(:/imgs/edit.png);\n"
                                 "    background-color: rgba(255, 255, 255, 0);\n"
                                 "}\n"
                                 "#modifyBtn:hover {\n"
                                 "    border-image: url(:/imgs/edit_hover.png);\n"
                                 "}\n"
                                 "#modifyBtn:pressed {\n"
                                 "    border-image: url(:/imgs/edit_pressed.png);\n"
                                 "}\n"
                                 "#modifyBtn:disabled {\n"
                                 "    border-image: url(:/imgs/edit_disabled.png);\n"
                                 "}\n"
                                 "#exportBtn {\n"
                                 "    border-image: url(:/imgs/export.png);\n"
                                 "}\n"
                                 "#exportBtn:hover {\n"
                                 "    border-image: url(:/imgs/export_hover.png);\n"
                                 "}\n"
                                 "#exportBtn:pressed {\n"
                                 "    border-image: url(:/imgs/export_pressed.png);\n"
                                 "}\n"
                                 "#infoBtn {\n"
                                 "    border-image: url(:/imgs/info.png);\n"
                                 "}\n"
                                 "#infoBtn:hover {\n"
                                 "    border-image: url(:/imgs/info_hover.png);\n"
                                 "}\n"
                                 "#infoBtn:pressed {\n"
                                 "    border-image: url(:/imgs/info_pressed.png);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 2, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minBtn = QtWidgets.QPushButton(self.frame)
        self.minBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.minBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.minBtn.setText("")
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_2.addWidget(self.minBtn)
        self.maxBtn = QtWidgets.QPushButton(self.frame)
        self.maxBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.maxBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.maxBtn.setText("")
        self.maxBtn.setObjectName("maxBtn")
        self.horizontalLayout_2.addWidget(self.maxBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame)
        self.closeBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.closeBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.closeBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.addBtn = QtWidgets.QPushButton(self.frame)
        self.addBtn.setEnabled(False)
        self.addBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.addBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.addBtn.setText("")
        self.addBtn.setIconSize(QtCore.QSize(20, 20))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_7.addWidget(self.addBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.delBtn = QtWidgets.QPushButton(self.frame)
        self.delBtn.setEnabled(False)
        self.delBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.delBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.delBtn.setText("")
        self.delBtn.setIconSize(QtCore.QSize(20, 20))
        self.delBtn.setObjectName("delBtn")
        self.horizontalLayout_7.addWidget(self.delBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.modifyBtn = QtWidgets.QPushButton(self.frame)
        self.modifyBtn.setEnabled(False)
        self.modifyBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.modifyBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.modifyBtn.setText("")
        self.modifyBtn.setIconSize(QtCore.QSize(20, 20))
        self.modifyBtn.setObjectName("modifyBtn")
        self.horizontalLayout_7.addWidget(self.modifyBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.exportBtn = QtWidgets.QPushButton(self.frame)
        self.exportBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.exportBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.exportBtn.setText("")
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout_7.addWidget(self.exportBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.infoBtn = QtWidgets.QPushButton(self.frame)
        self.infoBtn.setMinimumSize(QtCore.QSize(33, 0))
        self.infoBtn.setMaximumSize(QtCore.QSize(36, 30))
        self.infoBtn.setText("")
        self.infoBtn.setObjectName("infoBtn")
        self.horizontalLayout_7.addWidget(self.infoBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.computerNameLabel = QtWidgets.QLabel(self.frame)
        self.computerNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.computerNameLabel.setObjectName("computerNameLabel")
        self.horizontalLayout_7.addWidget(self.computerNameLabel)
        self.computerBox = QtWidgets.QComboBox(self.frame)
        self.computerBox.setObjectName("computerBox")
        self.horizontalLayout_7.addWidget(self.computerBox)
        self.userNameLabel = QtWidgets.QLabel(self.frame)
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName("userNameLabel")
        self.horizontalLayout_7.addWidget(self.userNameLabel)
        self.userBox = QtWidgets.QComboBox(self.frame)
        self.userBox.setObjectName("userBox")
        self.horizontalLayout_7.addWidget(self.userBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(5, 1)
        self.horizontalLayout_7.setStretch(11, 1)
        self.horizontalLayout_7.setStretch(12, 1)
        self.horizontalLayout_7.setStretch(13, 1)
        self.horizontalLayout_7.setStretch(14, 1)
        self.horizontalLayout_7.setStretch(15, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.machineLabel = QtWidgets.QLabel(self.frame)
        self.machineLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.machineLabel.setObjectName("machineLabel")
        self.verticalLayout.addWidget(self.machineLabel)
        self.machineTree = QtWidgets.QTreeWidget(self.frame)
        self.machineTree.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.machineTree.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.machineTree.setAnimated(True)
        self.machineTree.setObjectName("machineTree")
        self.machineTree.headerItem().setText(0, "Machine")
        self.machineTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/machine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.machineTree.headerItem().setIcon(0, icon1)
        self.machineTree.header().setVisible(True)
        self.verticalLayout.addWidget(self.machineTree)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.expandBtn = QtWidgets.QPushButton(self.frame)
        self.expandBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.expandBtn.setText("")
        self.expandBtn.setObjectName("expandBtn")
        self.verticalLayout_3.addWidget(self.expandBtn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.narrowBtn = QtWidgets.QPushButton(self.frame)
        self.narrowBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.narrowBtn.setText("")
        self.narrowBtn.setObjectName("narrowBtn")
        self.verticalLayout_3.addWidget(self.narrowBtn)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 3)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userLabel = QtWidgets.QLabel(self.frame)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userLabel.setObjectName("userLabel")
        self.verticalLayout_2.addWidget(self.userLabel)
        self.userTree = QtWidgets.QTreeWidget(self.frame)
        self.userTree.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.userTree.setAnimated(True)
        self.userTree.setObjectName("userTree")
        self.userTree.headerItem().setText(0, "User")
        self.userTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userTree.headerItem().setIcon(0, icon2)
        self.verticalLayout_2.addWidget(self.userTree)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.Details = QtWidgets.QWidget()
        self.Details.setObjectName("Details")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Details)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.detailsTab = QtWidgets.QTableWidget(self.Details)
        self.detailsTab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.detailsTab.setAutoScroll(True)
        self.detailsTab.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.detailsTab.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.detailsTab.setShowGrid(True)
        self.detailsTab.setGridStyle(QtCore.Qt.SolidLine)
        self.detailsTab.setWordWrap(True)
        self.detailsTab.setCornerButtonEnabled(True)
        self.detailsTab.setObjectName("detailsTab")
        self.detailsTab.setColumnCount(2)
        self.detailsTab.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.detailsTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.detailsTab.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.detailsTab.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.detailsTab.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTab.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.detailsTab.setItem(3, 0, item)
        self.detailsTab.horizontalHeader().setVisible(False)
        self.detailsTab.horizontalHeader().setCascadingSectionResizes(False)
        self.detailsTab.horizontalHeader().setStretchLastSection(True)
        self.detailsTab.verticalHeader().setVisible(False)
        self.detailsTab.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_5.addWidget(self.detailsTab)
        self.tabWidget.addTab(self.Details, "")
        self.Hint = QtWidgets.QWidget()
        self.Hint.setObjectName("Hint")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Hint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hintTab = QtWidgets.QListWidget(self.Hint)
        self.hintTab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hintTab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.hintTab.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.hintTab.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.hintTab.setObjectName("hintTab")
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/stringLabel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.hintTab.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/expandStringLabel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.hintTab.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgs/readOnlyStringLabel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.hintTab.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgs/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.hintTab.addItem(item)
        self.horizontalLayout_6.addWidget(self.hintTab)
        self.tabWidget.addTab(self.Hint, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 10)
        self.verticalLayout_4.setStretch(3, 4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.expandBtn.clicked.connect(self.userTree.expandAll)
        self.narrowBtn.clicked.connect(self.machineTree.collapseAll)
        self.narrowBtn.clicked.connect(self.userTree.collapseAll)
        self.closeBtn.clicked.connect(Form.close)
        self.minBtn.clicked.connect(Form.showMinimized)
        self.expandBtn.clicked.connect(self.machineTree.expandAll)
        self.maxBtn.clicked.connect(Form.setWindowsState)
        self.machineTree.itemClicked['QTreeWidgetItem*', 'int'].connect(Form.receiveActivatedSignal)
        self.userTree.itemClicked['QTreeWidgetItem*', 'int'].connect(Form.receiveActivatedSignal)
        self.addBtn.clicked.connect(Form.createNewItem)
        self.delBtn.clicked.connect(Form.deleteItem)
        self.modifyBtn.clicked.connect(Form.modifyItem)
        self.exportBtn.clicked.connect(Form.exportRegistryTable)
        self.infoBtn.clicked.connect(Form.showInformation)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addBtn.setToolTip(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Create</span> an environment variable</p></body></html>"))
        self.delBtn.setToolTip(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Delete</span> the environment variable</p></body></html>"))
        self.modifyBtn.setToolTip(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Edit</span> the environment variable</p></body></html>"))
        self.exportBtn.setToolTip(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Export</span> the current environment variable</p></body></html>"))
        self.infoBtn.setToolTip(_translate("Form",
                                           "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Get Information</span> of the software</p></body></html>"))
        self.computerNameLabel.setText(_translate("Form", "ComputeName"))
        self.userNameLabel.setText(_translate("Form", "User"))
        self.machineLabel.setText(_translate("Form", "Machine Environment Variables"))
        self.expandBtn.setToolTip(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">expand</span> all environment variables</p></body></html>"))
        self.narrowBtn.setToolTip(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">fold</span> all environment variables</p></body></html>"))
        self.userLabel.setText(_translate("Form", "User Environment Variables"))
        __sortingEnabled = self.detailsTab.isSortingEnabled()
        self.detailsTab.setSortingEnabled(False)
        item = self.detailsTab.item(0, 0)
        item.setText(_translate("Form", "变量名"))
        item = self.detailsTab.item(1, 0)
        item.setText(_translate("Form", "类型"))
        item = self.detailsTab.item(2, 0)
        item.setText(_translate("Form", "源值"))
        item = self.detailsTab.item(3, 0)
        item.setText(_translate("Form", "转义值"))
        self.detailsTab.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Details), _translate("Form", "Details"))
        __sortingEnabled = self.hintTab.isSortingEnabled()
        self.hintTab.setSortingEnabled(False)
        item = self.hintTab.item(0)
        item.setText(_translate("Form", "env variable is a text-string"))
        item = self.hintTab.item(1)
        item.setText(_translate("Form", "env variable is a compressed string"))
        item = self.hintTab.item(2)
        item.setText(_translate("Form", "env variable is a read-only string"))
        item = self.hintTab.item(3)
        item.setText(_translate("Form", "there is something wrong in env variable\'s value "))
        self.hintTab.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hint), _translate("Form", "Hint"))
