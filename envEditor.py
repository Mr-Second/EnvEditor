import getpass
import os
import socket

import icons_rc

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect, QTreeWidgetItem, QTreeWidget, \
    QTableWidgetItem, QMessageBox

from InfoDialog import InfoDialog
from envEditorModel import Ui_Form
from pathDialog import PathDialog
from popDialog import PopDialog
from registry_tools import RegistryTools


class env_editor(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(env_editor, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(6, 6)
        shadow.setColor(QColor(43, 43, 43))
        self.frame.setGraphicsEffect(shadow)

        # tableWidget条纹相间
        # self.detailsTab.setAlternatingRowColors(True)
        self.isNormal = True
        self.registryTool = RegistryTools()

        self.currentUser = getpass.getuser()
        self.machineName = socket.gethostname()
        self.userBox.addItem(self.currentUser)
        self.computerBox.addItem(self.machineName)

        normalStrIcon = QIcon(":/imgs/stringLabel.png")
        expandStrIcon = QIcon(":/imgs/expandStringLabel.png")
        readOnlyStrIcon = QIcon(":/imgs/readOnlyStringLabel.png")
        errStrIcon = QIcon(":/imgs/error.png")
        valueIcon = QIcon(":/imgs/arrow.png")

        self.iconMap = {
            1: normalStrIcon,
            2: expandStrIcon,
            3: readOnlyStrIcon,
            4: errStrIcon,
            5: valueIcon
        }

        self.types = ["", "normal string", "expand string", "read-only string", "error-path string"]

        self.readOnlyKeys = [
            "NUMBER_OF_PROCESSORS",
            "OS",
            "PATHEXT",
            "POWERSHELL_DISTRIBUTION_CHANNEL",
            "PROCESSOR_ARCHITECTURE",
            "PROCESSOR_IDENTIFIER",
            "PROCESSOR_LEVEL",
            "PROCESSOR_REVISION",
            "PSModulePath",
            "USERNAME"
        ]

        self.itemMap = {}
        self.childParentMap = {}
        self.itemInfoMap = {}
        self.app = None

        self.userTree.setFocusPolicy(Qt.NoFocus)
        self.machineTree.setFocusPolicy(Qt.NoFocus)

        self.__initTreeView()
        self.previousItemClicked = ""
        self.message = {}

    def setApp(self, app_: QApplication):
        self.app = app_

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.detailsTab.setColumnWidth(0, int(self.detailsTab.width() / 9))
        self.detailsTab.setColumnWidth(1, self.detailsTab.width() - int(self.detailsTab.width() / 9))

    def receiveActivatedSignal(self, item: QTreeWidgetItem, index: int):
        if not self.addBtn.isEnabled() or not self.delBtn.isEnabled() or not self.modifyBtn.isEnabled():
            self.addBtn.setEnabled(True)
            self.delBtn.setEnabled(True)
            self.modifyBtn.setEnabled(True)
        self.previousItemClicked = item.text(0)
        key = None
        if not item.parent() is None:
            key = item.parent().text(0)
        else:
            key = item.text(0)
        if self.userTree.isAncestorOf(item.treeWidget()):
            key = f"{key}_User"
            self.previousItemClicked = f"{self.previousItemClicked}_User"
        elif self.machineTree.isAncestorOf(item.treeWidget()):
            key = f"{key}_Machine"
            self.previousItemClicked = f"{self.previousItemClicked}_Machine"

        info = self.itemInfoMap[key]
        name = info["Name"]
        valueType = info["Type"]
        originalVal = info["OriginalValue"]
        changedVal = info["ChangedValue"]
        self.detailsTab.setItem(0, 1, QTableWidgetItem(name))
        self.detailsTab.setItem(1, 1, QTableWidgetItem(valueType))
        self.detailsTab.setItem(2, 1, QTableWidgetItem(originalVal))
        self.detailsTab.setItem(3, 1, QTableWidgetItem(changedVal))

        if originalVal == changedVal:
            self.detailsTab.setRowHidden(4, True)
        else:
            self.detailsTab.setRowHidden(4, False)

    def createNewItem(self):
        if self.previousItemClicked == "":
            return

        treeName = self.previousItemClicked.split("_")[-1]
        if self.previousItemClicked in self.itemMap:
            items = self.__getTreeWidgetItems(treeName)
            dialog = PopDialog(self, items)

            def slotFunc(msg: dict):
                self.message = msg
            dialog.connectWithThis(slotFunc)

            self.setWindowOpacity(0.5)
            dialog.title.setText(f"Add Item In <b>{treeName}</b> environment variables")
            res = dialog.exec_()
            self.setWindowOpacity(1.0)

            if res == 0:
                print("dialog is rejected")
                return

            key = self.message["name"]
            value = self.message["value"]
            self.registryTool["Set"](treeName, key, value)
            self.message.clear()

            if treeName == "User":
                itemName = self.__createTreeItem(key, value, 1, self.userTree, treeName)
                self.userTree.addTopLevelItem(self.itemMap[itemName])
            else:
                itemName = self.__createTreeItem(key, value, 1, self.machineTree, treeName)
                self.machineTree.addTopLevelItem(self.itemMap[itemName])
        elif self.previousItemClicked in self.childParentMap:
            dialog = PathDialog(self)

            def slotFunc(msg: str):
                self.message = msg
            dialog.connectWithThis(slotFunc)
            self.setWindowOpacity(0.5)
            res = dialog.exec_()
            self.setWindowOpacity(1.0)
            if res == 0:
                print("dialog is rejected")
                return
            key = self.childParentMap[self.previousItemClicked]
            parentItem = self.itemMap[f"{key}_{treeName}"]
            sonItem = QTreeWidgetItem(parentItem)
            sonItem.setIcon(0, self.iconMap[5])
            sonItem.setText(0, self.message)
            parentItem.addChild(sonItem)
            self.message.clear()
            self.itemInfoMap[f"{key}_{treeName}"]["OriginalValue"] += f";{self.message}"
            self.itemInfoMap[f"{key}_{treeName}"]["ChangedValue"] += f";{self.message}"
            self.registryTool["Set"](treeName, key, self.itemInfoMap[f"{key}_{treeName}"]["OriginalValue"])

        self.__update()

    def deleteItem(self):
        if self.previousItemClicked == "":
            return

        role = self.previousItemClicked[self.previousItemClicked.rfind("_") + 1:]
        value = self.previousItemClicked[:self.previousItemClicked.rfind("_")]
        key = ""
        flag = -1  # 0 -> delete key, 1 -> delete value
        item = None
        if self.previousItemClicked in self.itemMap:
            key = value
            flag = 0
            item = self.itemMap[self.previousItemClicked]

            # -------delete items in childParentMap whose value is the text of the item--------
            delList = [v for k, v in self.childParentMap.items() if v == item.text(0)]
            print(delList[0] in self.childParentMap.values())
            self.childParentMap = dict((key, value) for key, value in self.childParentMap.items()
                                       if value not in delList or not key.endswith(f"{role}"))
            print(delList[0] in self.childParentMap.values())
            # ---------------------------------------------------------------------------------

            if role == "User":
                modelIndex = self.userTree.indexFromItem(item)
                index = modelIndex.row()
                self.userTree.takeTopLevelItem(index)
            else:
                modelIndex = self.machineTree.indexFromItem(item)
                index = modelIndex.row()
                self.machineTree.takeTopLevelItem(index)
        elif self.previousItemClicked in self.childParentMap:
            key = self.childParentMap[self.previousItemClicked]
            flag = 1
            parentItem = self.itemMap[f"{key}_{role}"]
            count = parentItem.childCount()
            if count <= 0:
                return
            for i in range(count):
                childItem = parentItem.child(i)
                if childItem.text(0) == value:
                    parentItem.takeChild(i)
            # -----delete the value of item in childParentMap----------
            self.childParentMap.pop(self.previousItemClicked)
            # ---------------------------------------------------------
        else:
            return

        if flag == 0:
            res = self.registryTool["DelKey"](role, key)
            print(res)
        elif flag == 1:
            res = self.registryTool["DelValue"](role, key, value)
            print(res)
        else:
            return
        self.__update()

    def modifyItem(self):
        if self.previousItemClicked == "":
            return

        if self.detailsTab.item(1, 1).text() == "read-only string":
            QMessageBox.warning(self, "WARNING", "read-only string can't be written", QMessageBox.Yes, QMessageBox.Yes)
            return

        role = self.previousItemClicked[self.previousItemClicked.rfind("_") + 1:]
        key = self.previousItemClicked[:self.previousItemClicked.rfind("_")]
        print(f"role: {role}, key: {key}")

        def slotFunc(msg: str):
            self.message = msg
        if self.previousItemClicked in self.itemMap:
            dialog = PathDialog(self, False)
            dialog.connectWithThis(slotFunc)
            self.setWindowOpacity(0.5)
            res = dialog.exec_()
            self.setWindowOpacity(1.0)
            if res == 0:
                print("dialog is rejected")
                return
            newKey = self.message

            item = self.itemMap[self.previousItemClicked]
            value = self.itemInfoMap[self.previousItemClicked]["OriginalValue"]
            if self.registryTool["Set"](role, newKey, value):
                res = self.registryTool["DelKey"](role, item.text(0))
                if res:
                    item.setText(0, newKey)
                    res = self.itemInfoMap.pop(self.previousItemClicked)
                    res["Name"] = newKey
                    self.itemInfoMap[f"{newKey}_{role}"] = res

        elif self.previousItemClicked in self.childParentMap:
            dialog = PathDialog(self)
            dialog.connectWithThis(slotFunc)
            self.setWindowOpacity(0.5)
            res = dialog.exec_()
            self.setWindowOpacity(1.0)
            if res == 0:
                print("dialog is rejected")
                return
            newValue = self.message

            parentKey = self.childParentMap[self.previousItemClicked]
            parentItem = self.itemMap[f"{parentKey}_{role}"]
            count = parentItem.childCount()
            if count <= 0:
                self.registryTool["Set"](role, parentKey, str(newValue) + ";")
                return
            values = []
            for i in range(count):
                childItem = parentItem.child(i)
                if childItem.text(0) == key:
                    childItem.setText(0, newValue)
                else:
                    values.append(childItem.text(0))
            values.append(newValue)
            newValue = ";".join(values)
            res = self.registryTool["Set"](role, parentKey, newValue)
            if res:
                self.childParentMap.pop(f"{key}_{role}")
                self.childParentMap[f"{newValue}_{role}"] = parentKey
                self.itemInfoMap[f"{parentKey}_{role}"]["OriginalValue"] = newValue
                self.itemInfoMap[f"{parentKey}_{role}"]["ChangedValue"] = newValue
        self.__update()

    def setWindowsState(self):
        if self.isNormal:
            self.showMaximized()
            self.isNormal = not self.isNormal
        else:
            self.showNormal()
            self.isNormal = not self.isNormal

    def __initTreeView(self):
        userData = self.registryTool["Get"]("User")
        machineData = self.registryTool["Get"]("Machine")
        # pprint(userData)
        for item in userData.items():
            key = item[0]
            valueType = userData[key]["type"]
            value = userData[key]["value"]

            itemIndex = self.__createTreeItem(key, value, valueType, self.userTree, "User")
            self.userTree.addTopLevelItem(self.itemMap[itemIndex])

        for item in machineData.items():
            key = item[0]
            valueType = machineData[key]["type"]
            value = machineData[key]["value"]
            itemName = self.__createTreeItem(key, value, valueType, self.machineTree, "Machine")
            self.machineTree.addTopLevelItem(self.itemMap[itemName])

    def __createTreeItem(self, key: str, value: str, valueType: int, parent: QTreeWidget, role: str) -> str:
        originalValue = value
        changedValue = ""

        keyItem = QTreeWidgetItem(parent)
        keyItem.setText(0, key)

        values = value.split(";")
        if key in self.readOnlyKeys:
            valueType = 3
        else:
            valueType = self.__getValueType(values, role)
        keyItem.setIcon(0, self.iconMap[valueType])

        if len(values) < 2:
            if self.registryTool.isCompressedPath(values[0], role):
                value = self.registryTool.getExpandPath(values[0], role)
            valueItem = QTreeWidgetItem(keyItem)
            valueItem.setText(0, value)
            valueItem.setIcon(0, self.iconMap[5])
            keyItem.addChild(valueItem)
            self.childParentMap[f"{value}_{role}"] = key
            changedValue = value
        else:
            for value in values:
                if len(value) == 0:
                    continue
                valueItem = QTreeWidgetItem(keyItem)
                if self.registryTool.isCompressedPath(value, role):
                    value = self.registryTool.getExpandPath(value, role)
                if not os.path.isfile(value) and not os.path.isdir(value) and not (key in self.readOnlyKeys):
                    valueItem.setForeground(0, QColor("#eb3b5a"))
                valueItem.setText(0, value)
                valueItem.setIcon(0, self.iconMap[5])
                keyItem.addChild(valueItem)
                if changedValue == "":
                    changedValue = value
                else:
                    changedValue += f";{value}"
                self.childParentMap[f"{value}_{role}"] = key

        self.itemMap[f"{key}_{role}"] = keyItem
        self.itemInfoMap[f"{key}_{role}"] = {
            "Name": key,
            "Type": self.types[valueType],
            "OriginalValue": originalValue,
            "ChangedValue": changedValue
        }
        return f"{key}_{role}"

    def __getValueType(self, values: list, role: str) -> int:
        valueType = 1
        if len(values) <= 0:
            valueType = 1
        elif len(values) <= 2:
            if self.registryTool.isCompressedPath(values[0], role):
                valueType = 2
            elif not os.path.isfile(values[0]) and not os.path.isdir(values[0]):
                valueType = 4
            else:
                valueType = 1
        else:
            for value in values:
                if len(value) == 0:
                    continue
                if self.registryTool.isCompressedPath(value, role):
                    valueType = 2
                    break
                if not os.path.isfile(value) and not os.path.isdir(value):
                    valueType = 4
                    break
        return valueType

    def __getTreeWidgetItems(self, role: str) -> list:
        res = []
        if role == "User":
            item = QtWidgets.QTreeWidgetItemIterator(self.userTree)
        else:
            item = QtWidgets.QTreeWidgetItemIterator(self.machineTree)
        while item.value():
            if item.value().parent() is None:
                res.append(item.value().text(0))
            item = item.__iadd__(1)
        return res

    def __update(self):
        self.userTree.update()
        self.machineTree.update()
        self.update()

    def exportRegistryTable(self):
        dialog = PathDialog(self)

        def slotFunc(msg: str):
            self.message = msg

        dialog.connectWithThis(slotFunc)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setWeight(75)
        dialog.valueLabel.setFont(font)
        dialog.valueLabel.setText("Registry File Save Path:")
        dialog.valueLabel.setStyleSheet("")
        self.setWindowOpacity(0.5)
        res = dialog.exec_()
        self.setWindowOpacity(1.0)
        if res == 0:
            print("dialog is rejected")
            return
        self.registryTool.exportEnv(self.message)

    @classmethod
    def showInformation(cls):
        dialog = InfoDialog(None)
        dialog.exec()
        pass
