from tkinter import Tk, StringVar, Label, Button, Frame, Menu, Toplevel, BOTTOM
from tkinter.ttk import Notebook
from os.path import exists


class initUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create main window
        self.parent.title("RVZ Support")
        self.parent.geometry("500x200")
        self.parent.resizable(0, 0)
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
        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, text='Tab 2')
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

    def aboutWindow(self):
        # Toplevel object which will
        # be treated as a new window
        self.about = Toplevel(self.parent)
        self.about.title("About")
        self.about.geometry("200x200")
        Label(self.about,
              text="This is a about window").pack()

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    initUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
