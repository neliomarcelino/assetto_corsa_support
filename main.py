from main_frame import MainFrame
from initial_frame import InitialConfig
from tkinter import Tk
import config_ini
import configparser
import const


def inital_configuration():
    config = None
    config = config_ini.read_config_file()
    if config.sections() == []:
        # If config file 'config.ini' has no data, then Run first configuration
        print("No 'config.ini' found. Runing first configuration")
        init_config_window = Tk()
        initconfig = InitialConfig(init_config_window)
        init_config_window.mainloop()
        config = initconfig.getConfig()

    return config


def main():
    # Reads config file
    config = config_ini.read_config_file()

    # Goes to initial configuration if no data oon config file
    if config.sections() == []:
        config = inital_configuration()

    # Goes to main window if has config data
    if config.sections() != []:
        root = Tk()
        MainFrame(root).pack(side="top", fill="both", expand=True)
        root.mainloop()


if __name__ == "__main__":
    main()
