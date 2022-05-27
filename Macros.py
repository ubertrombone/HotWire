from pynput import keyboard

from globals import view_model


class Macros:

    def __init__(self):
        super().__init__()
        self.controller = keyboard.Controller()
        self.resetting_keys = [keyboard.Key.backspace, keyboard.Key.space, keyboard.Key.enter, keyboard.Key.tab]
        self.record = False

    def on_execute(self):
        self.record = False
        command = view_model.hot_keys["".join(view_model.list_of_typed_chars)]
        for i in range(0, len(view_model.list_of_typed_chars)):
            self.controller.tap(keyboard.Key.backspace)
        self.controller.type(command)
        view_model.list_of_typed_chars.clear()

    def on_press(self, key):
        if not view_model.start_macros:
            return

        try:
            if key.char == "`":
                self.record = True
        except AttributeError:
            pass

        if self.record:
            try:
                view_model.list_of_typed_chars.append(key.char)
            except AttributeError:
                pass

            try:
                if "".join(view_model.list_of_typed_chars) in view_model.hot_keys.keys():
                    self.on_execute()
            except TypeError:
                view_model.list_of_typed_chars.clear()
                pass

    def on_release(self, key):
        if not view_model.start_macros:
            return

        if key in self.resetting_keys:
            self.record = False
            view_model.list_of_typed_chars.clear()
        if key == keyboard.Key.esc:
            # Stop listener
            self.record = False
            view_model.list_of_typed_chars.clear()
            view_model.set_macros(False)
            # return False

    def start(self):
        listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)
        listener.start()
