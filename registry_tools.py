# -*- coding: gbk -*-

import os
import re

import chardet
import traceback
import winreg
from datetime import datetime
from threading import Thread


def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ


def get_encoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        return str(chardet.detect(data)['encoding'])


def async_(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


class RegistryTools:

    def __init__(self):
        self.__path = os.getcwd()
        self.__userEnv = "Environment"
        self.__machineEnv = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        self.__userName = os.getlogin()
        self.__envVariable = {
            "%ALLUSERSPROFILE%": r"C:\ProgramData",
            "%APPDATA%": rf"C:\Users\{self.__userName}\AppData\Roaming",
            "%COMMONPROGRAMFILES%": r"C:\Program Files\Common Files",
            "%COMMONPROGRAMFILES(x86)%": r"C:\Program Files (x86)\Common Files",
            "%COMSPEC%": r"C:\Windows\System32\cmd.exe",
            "%HOMEDRIVE%": "C:",
            "%SystemDrive%": "C:",
            "%HOMEPATH%": rf"\Users\{self.__userName}",
            "%LOCALAPPDATA%": rf"C:\Users\{self.__userName}\AppData\Local",
            "%PROGRAMDATA%": r"C:\ProgramData",
            "%PROGRAMFILES%": r"C:\Program Files",
            "%PROGRAMFILES(X86)%": r"C:\Program Files (x86)",
            "%PUBLIC%": r"C:\Users\Public",
            "%SystemRoot%": r"C:\Windows",
            "%TEMP%": rf"C:\Users\{self.__userName}\AppData\Local\Temp",
            "%USERPROFILE%": rf"C:\Users\{self.__userName}",
            "%WINDIR%": r"C:\Windows"
        }
        self.__modify()
        self.__backupEnv(self.__path)
        self.__userEnvVariables = self.__getEnv("User")
        self.__machineEnvVariables = self.__getEnv("Machine")

    def __getitem__(self, action: str):

        def getCommand(role: str):
            if role == "User" or role == "Machine":
                return self.__run(role, "Get")
            else:
                raise ValueError(f"role {role} is invalid")

        def setCommand(role: str, key: str, value: str):
            if role == "User" or role == "Machine":
                return self.__run(role, "Set", key, value)
            else:
                raise ValueError(f"role {role} is invalid")

        def delValueCommand(role: str, key: str, value: str):
            if role == "User" or role == "Machine":
                return self.__run(role, "DelValue", key, value)
            else:
                raise ValueError(f"role {role} is invalid")

        def delKeyCommand(role: str, key: str):
            if role == "User" or role == "Machine":
                return self.__run(role, "DelAll", key)
            else:
                raise ValueError(f"role {role} is invalid")

        def backCommand(path: str):
            self.__backupEnv(path)

        action_function_map = {
            "Get": getCommand,
            "Set": setCommand,
            "DelValue": delValueCommand,
            "DelKey": delKeyCommand,
            "BackUp": backCommand
        }

        if action in action_function_map:
            return action_function_map[action]
        else:
            raise ValueError(f"action {action} is invalid")

    def __run(self, role: str, action: str, key=None, value=None):
        print(f"role: {role}, command: {action}, key: {key}, value: {value}")
        if action == "Get":
            return self.__getEnv(role)
        elif action == "Set":
            return self.__setEnv(role, key, value)
        elif action == "DelValue":
            return self.__delEnvValue(role, key, value)
        elif action == "DelAll":
            return self.__delEnv(role, key)
        else:
            raise ValueError(f"action {action} is invalid")

    def __modify(self):
        for key, value in self.__envVariable.items():
            self.__envVariable[key] = winreg.ExpandEnvironmentStrings(key)

    @async_
    def __backupEnv(self, path: str):
        if not os.path.isdir(path):
            return

        path = os.path.join(path, f"backUp_{datetime.now().strftime('%Y-%m-%d')}.reg")

        res_1 = self.runCMD("REG EXPORT HKCU\\Environment 1.reg /y")
        res_2 = self.runCMD('REG EXPORT "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" '
                            '2.reg /y')
        print(f"res_1: {res_1.strip()}, res_2: {res_2.strip()}")
        userEnvFilePath = os.path.join(self.__path, "1.reg")
        machineEnvFilePath = os.path.join(self.__path, "2.reg")
        if os.path.isfile(userEnvFilePath) and os.path.isfile(machineEnvFilePath):
            try:
                resFile = [f"; User: {self.__userName}\n"]
                encoding = get_encoding(userEnvFilePath)
                with open(userEnvFilePath, "r", encoding=encoding) as f:
                    lines = f.readlines()
                resFile.extend(lines[1:-1])

                resFile.append("\n; System variables\n")
                with open(machineEnvFilePath, "r", encoding=encoding) as f:
                    lines = f.readlines()
                resFile.extend(lines[1:-1])

                with open(path, "w", encoding=encoding) as f:
                    f.writelines(resFile)
            except Exception as e:
                traceback.print_exc()
            finally:
                os.remove(userEnvFilePath)
                os.remove(machineEnvFilePath)

    def __getEnv(self, role: str):
        handle_type = None
        env = None
        res = {}
        if role == "User":
            handle_type = winreg.HKEY_CURRENT_USER
            env = self.__userEnv
        else:
            handle_type = winreg.HKEY_LOCAL_MACHINE
            env = self.__machineEnv

        handle = winreg.OpenKey(handle_type, env)
        try:
            i = 0
            while 1:
                name, value, _type = winreg.EnumValue(handle, i)
                res[name] = {
                    "value": value,
                    "type": _type
                }
                i += 1
        except WindowsError as e:
            print(e)
        finally:
            winreg.CloseKey(handle)
            return res

    def __setEnv(self, role: str, key: str, value: str) -> bool:
        flag = True
        reg_root = winreg.HKEY_CURRENT_USER if role == "User" else winreg.HKEY_LOCAL_MACHINE
        reg_path = self.__userEnv if role == "User" else self.__machineEnv
        handle = None
        try:
            handle = winreg.OpenKeyEx(reg_root, reg_path, 0, winreg.KEY_ALL_ACCESS)
            if not self.__isKeyExists(role, key):
                _ = winreg.CreateKeyEx(handle, key)
            winreg.SetValueEx(handle, key, 0, self.__typeOfValue(value), value)
        except WindowsError as e:
            print(e)
            flag = False
        finally:
            winreg.CloseKey(handle)
            return flag

    def __delEnvValue(self, role: str, key: str, value: str) -> bool:
        reg_root = winreg.HKEY_CURRENT_USER if role == "User" else winreg.HKEY_LOCAL_MACHINE
        reg_path = self.__userEnv if role == "User" else self.__machineEnv
        reg_flag = winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY | winreg.KEY_WRITE

        res = True
        handle = None
        tuples = None
        try:
            handle = winreg.OpenKey(reg_root, reg_path, 0, reg_flag)
            tuples = winreg.QueryValueEx(handle, key)
            print(tuples)
        except KeyError:
            res = False
        finally:
            if not res or len(tuples) != 2:
                winreg.CloseKey(handle)
                return res
            else:
                values = tuples[0].split(";")
                if value not in values:
                    return False
                else:
                    values.remove(value)
                    value = ";".join(values)
                    return self.__setEnv(role, key, value)

    def __delEnv(self, role: str, key: str) -> bool:
        reg_root = winreg.HKEY_CURRENT_USER if role == "User" else winreg.HKEY_LOCAL_MACHINE
        reg_path = self.__userEnv if role == "User" else self.__machineEnv
        flag = True
        handle = None

        try:
            handle = winreg.OpenKeyEx(reg_root, reg_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(handle, key)
        except WindowsError as e:
            traceback.print_exc()
            flag = False
        finally:
            winreg.CloseKey(handle)
            return flag

    def __typeOfValue(self, value: str) -> int:
        for key in self.__envVariable:
            if key in value:
                return winreg.REG_EXPAND_SZ
        return winreg.REG_SZ

    def __isKeyExists(self, role: str, key: str) -> bool:
        reg_root = winreg.HKEY_CURRENT_USER if role == "User" else winreg.HKEY_LOCAL_MACHINE
        reg_path = self.__userEnv if role == "User" else self.__machineEnv
        reg_flag = winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY | winreg.KEY_WRITE
        res = True
        handle = None
        try:
            handle = winreg.OpenKey(reg_root, reg_path, 0, reg_flag)
            _, _ = winreg.QueryValueEx(handle, key)
        except KeyError:
            res = False
        finally:
            winreg.CloseKey(handle)
            return res

    @classmethod
    def runCMD(cls, cmd: str) -> str:
        r = os.popen(cmd)
        text = "".join([line for line in r.readlines()])
        r.close()
        return text

    def getExpandPath(self, path: str, role: str) -> str:
        for env in self.__envVariable:
            if env in path:
                path = path.replace(env, self.__envVariable[env])
                break
        variables = self.__userEnvVariables if role == "User" else self.__machineEnvVariables
        for env in variables:
            if env in path:
                path = path.replace(f"%{env}%", variables[env]["value"])
                break
        if path.endswith(";"):
            path = path[0:-1]
        return path

    def isCompressedPath(self, path: str, role: str) -> bool:
        pattern = re.compile(".*%.*%.*")
        if not pattern.match(path):
            return False

        flag = False
        for env in self.__envVariable:
            if env in path:
                flag = True
                break

        for env in (self.__userEnvVariables if role == "User" else self.__machineEnvVariables):
            if env in path:
                flag = True
                break
        return flag

    def exportEnv(self, path):
        self.__backupEnv(path)
