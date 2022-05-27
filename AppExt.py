from tkinter import END, filedialog

from App import App
from globals import view_model


class AppExt(App):

    def __init__(self):
        super().__init__()
        self.browse_btn["command"] = self.browse
        self.activate_btn["command"] = self.activate_command

    def browse(self):
        self.file_entry.delete(0, END)
        file = filedialog.askopenfilename(filetypes=[('CSV', '*.csv')], title='Choose a file')
        self.file_entry.insert(0, file)
        if len(self.file_entry.get()) > 0:
            view_model.clear_macros()
            view_model.read_csv(self.file_entry.get())
            self.activate_btn.configure(state='normal')

    def activate_command(self):
        if self.button_text.get() == "Activate":
            view_model.set_macros(True)
            self.button_text.set("Deactivate")
        else:
            view_model.set_macros(False)
            view_model.list_of_typed_chars.clear()
            self.button_text.set("Activate")
