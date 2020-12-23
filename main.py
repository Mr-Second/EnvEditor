import ctypes


def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except WindowsError as e:
        print(e)
        return False


if __name__ == "__main__":

    pass


