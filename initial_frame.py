from tkinter import Frame, filedialog, Label, Button, BOTTOM, Entry, E, W, StringVar
from tkinter.constants import RIGHT
import config_ini
import const
from os.path import exists
import configparser
import utils


class InitialConfig(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config_ini = config_ini.read_config_file()

        # Create window
        self.parent.title(const.LABEL_PROGRAM_TITLE)
        self.parent.resizable(False, False)
        self.parent.iconbitmap('./cx_freeze/icon.ico')
        self.parent.geometry(const.INITIAL_WINDOW_WIDTH +
                             'x' + const.INITIAL_WINDOW_HEIGHT)

        # Set config_ini to defaults
        config_ini.set_default_assetto_config(self.config_ini)
        config_ini.set_default_csp_config(self.config_ini)
        config_ini.set_default_sol_config(self.config_ini)

        # Components
        self.ac_path_strv = StringVar()
        game_dir = utils.getGamePath(const.AC_REG_KEY)
        if game_dir:
            self.ac_path_strv.set(game_dir)
        else:
            self.ac_path_strv.set(const.AC_DEFAULT_PATH)

        self.config_ini["ASSETTOCORSA"]["path"] = self.ac_path_strv.get()

        lab_ac_path = Label(self.parent, text="AC path:")
        path = Entry(self.parent, textvariable=self.ac_path_strv)
        choose_path = Button(self.parent, text=const.LABEL_CHOOSE,
                             command=self.askDirectory)
        ok = Button(self.parent, text=const.LABEL_OK,
                    command=self.apply_configuration)
        cancel = Button(
            self.parent, text=const.LABEL_BTN_CANCEL, command=self.onCancel)

        # Grid
        lab_ac_path.grid(column=0, row=0, sticky=W)
        path.grid(column=0, row=1, columnspan=3, sticky=W)
        choose_path.grid(column=4, row=1, sticky=W)
        ok.grid(column=3, row=2, sticky=E)
        cancel.grid(column=4, row=2, sticky=E)

    def apply_configuration(self):
        print("Applying configuration...")
        self.config_ini["ASSETTOCORSA"]["path"] = self.ac_path_strv.get()

        # Validate path
        if not utils.isPath(self.ac_path_strv.get()):
            print("Path not found, exiting...")
            self.exitWithError(self)

        # Save on config.ini file
        if config_ini.save_configuration(self.config_ini):
            print("Saving configuration...")
            self.parent.destroy()
        else:
            print("App exited with an error...")
            self.exitWithError(self)

    def exitWithError(self):
        self.parent.destroy()

    def onCancel(self):
        self.config_ini = config_ini.delete_configuration()
        self.parent.destroy()

    def askDirectory(self):
        ac_path = filedialog.askdirectory()
        if ac_path:
            self.ac_path_strv.set(self.ac_path)
            self.config_ini["ASSETTOCORSA"]["path"] = self.ac_path

    def getConfig(self):
        return self.config_ini
