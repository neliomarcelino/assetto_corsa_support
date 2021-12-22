from tkinter import Tk, StringVar, Label, Button, Frame, Menu, Toplevel, BOTTOM, filedialog
from tkinter.ttk import Notebook
import const


class MainFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create main window
        self.parent.title(const.LABEL_PROGRAM_TITLE)
        self.parent.geometry(const.MAIN_WINDOW_WIDTH +
                             'x' + const.MAIN_WINDOW_HEIGHT)
        self.parent.resizable(False, False)
        self.parent.iconbitmap('./cx_freeze/icon.ico')
        self.parent.text = StringVar()
        self.parent.text.set("Main window")

        self.parent.l1 = Label(
            self, textvariable=self.parent.text).pack(pady=15)
        self.parent.b1 = Button(self, text="Button",
                                command=self.changeText).pack(side=BOTTOM)

        # Configure Tabs
        tabControl = Notebook(self.parent)
        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tabControl.add(tab1, text=const.LABEL_VERSION_CONTROL)
        tabControl.add(tab2, text='Support')
        tabControl.pack(expand=1, fill="both")
        Label(tab1, text="Welcome to GeeksForGeeks").grid(
            column=0, row=0, padx=30, pady=30)
        Label(tab2, text="Lets dive into the world of computers").grid(
            column=0, row=0, padx=30, pady=30)

        # Create the Status bar
        # self.statusbar = Statusbar(self)
        # self.statusbar.pack(side="bottom", fill="x")

        # Configure Toolbar
        # self.toolbar = Toolbar(self)
        menubar = Menu(self.parent)

        # 'File' Cascade
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Settings", command=self.settingsWindow)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        # 'Help' Cascade
        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="About", command=self.aboutWindow)
        menubar.add_cascade(label="Help", menu=helpMenu)

        # Create the Navigation bar
        # self.navbar = Navbar(self)
        # self.navbar.pack(side="left", fill="y")

        # Create the Main window
        # self.main = Main(self)
        # self.main.pack(side="right", fill="both", expand=True)

        self.parent.config(menu=menubar)

    def changeText(self):
        self.parent.text.set("label changed")

    # Opens 'Settings' window
    def settingsWindow(self):
        self.settings = Toplevel(self.parent)
        self.settings.grab_set()
        self.settings.title(const.LABEL_ABOUT)
        self.settings.geometry("300x200")
        self.settings.grid_rowconfigure(0, weight=3)
        self.settings.grid_columnconfigure(0, weight=3)
        self.settings.save = Button(self.settings, text=const.LABEL_BTN_SAVE,
                                    command=self.realeseMainWindow)
        self.settings.cancel = Button(self.settings, text=const.LABEL_BTN_CANCEL,
                                      command=self.realeseMainWindow)
        self.settings.save.grid(row=2, column=3)
        self.settings.cancel.grid(row=2, column=2)
        self.settings.l1 = Label(self.settings,
                                 text="This is the settings window")
        self.settings.l1.grid(row=0, column=1)

    def realeseMainWindow(self):
        self.settings.grab_release()
        self.settings.destroy()
        self.settings.update()

    # Opens 'About' Window
    def aboutWindow(self):
        self.about = Toplevel(self.parent)
        self.about.title("About")
        self.about.geometry("200x200")
        Label(self.about,
              text="This is a about window").pack()

    def onExit(self):
        self.quit()
