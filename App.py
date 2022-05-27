import platform
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk


class App(tk.ThemedTk):

    def __init__(self):
        super().__init__()
        self.set_theme_advanced('plastik', brightness=1, saturation=1, hue=1)
        self.title('HotKeys')
        self.geometry('450x150')
        self.resizable(False, False)
        self.configure(background='#35A9EF')
        # TODO: Try this on Windows
        # self.iconphoto(False, PhotoImage(file='resources/DataForce_Icon.png'))
        if platform.system() == "Windows":
            self.iconbitmap = "resources/DataForce_Icon.ico"
        else:
            self.iconbitmap = "resources/DataForce_Icon.icns"
        ttk.Style().configure('TFrame', background='#35A9EF')
        ttk.Style().configure('TLabel', font=('arial', 10), foreground='#FFFFFF', background='#35A9EF')

        self.label = ttk.Label(self, text='Choose your file, then press Select')
        self.label.grid(row=0, pady=(10, 5))

        self.browse_frame = ttk.Frame(self, width=50)
        self.browse_frame.grid(row=1, column=0, pady=5)

        self.file_entry = ttk.Entry(self.browse_frame, width=35, foreground='#000000')
        self.file_entry.grid(sticky=W + E)

        self.browse_btn = ttk.Button(self.browse_frame, width=10, text="Browse")
        self.browse_btn.grid(row=0, column=1, sticky=W)

        self.activate_frame = ttk.Frame(self)
        self.activate_frame.grid(row=2, column=0, pady=5)

        self.button_text = StringVar()
        self.button_text.set("Activate")
        self.activate_btn = ttk.Button(self, width=46, textvariable=self.button_text, state="disabled")
        self.activate_btn.grid(padx=10, pady=5, sticky=W + E)

        self.version_label = ttk.Label(self, text="Version V1.0")
        self.version_label.grid(row=4, column=0, pady=(5, 10))
