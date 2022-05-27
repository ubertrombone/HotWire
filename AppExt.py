from tkinter import END, filedialog

from App import App


class AppExt(App):
    def __init__(self):
        super().__init__()
        self.browse_btn["command"] = self.browse

    def browse(self):
        self.file_entry.delete(0, END)
        file = filedialog.askopenfilename(filetypes=(('Excel Worksheet', '*.xlsx'),
                                                     ('CSV', '*.csv')), title='Choose a file')
        self.file_entry.insert(0, file)
        if len(self.file_entry.get()) > 0:
            self.activate.configure(state='normal')
