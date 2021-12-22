import sys
import winreg
import const
import os

# Read Steam installation path from windows registery


def getGamePath(reg_key=str) -> str:
    """
    Get game path by the Windows Registery

    :param reg_key: registry key
    :return: returns the game path
    """
    hkey = None
    game_path = const.STEAM_DEFAULT_PATH
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key)
    except Exception as e:
        print("Registery key could not be opened:", e)
        print(sys.exc_info())
        return None

    try:
        game_path = winreg.QueryValueEx(hkey, "InstallLocation")
    except Exception as e:
        print("Registery 'InstallLocation' value could not be obtained:", e)
        print(sys.exc_info())
        return None

    if game_path[1] == winreg.REG_SZ and game_path[0].strip():
        print("Installation Path:", game_path)
        return game_path[0]
    else:
        return None


def isPath(path):
    return os.path.isdir(path)
