from pynput import keyboard

from globals import view_model


class Macros:

    def __init__(self):
        super().__init__()
        self.controller = keyboard.Controller()

    def on_execute(self):
        command = view_model.hot_keys["".join(view_model.list_of_typed_chars)]
        for i in range(0, len(view_model.list_of_typed_chars)):
            self.controller.press(keyboard.Key.backspace)
            self.controller.release(keyboard.Key.backspace)
        self.controller.type(command)
        view_model.list_of_typed_chars.clear()

    def on_press(self, key):
        if not view_model.start_macros:
            return
        try:
            view_model.list_of_typed_chars.append(key.char)
        except AttributeError:
            pass

        print(view_model.list_of_typed_chars)
        try:
            if "".join(view_model.list_of_typed_chars) in view_model.hot_keys.keys():
                self.on_execute()
        except TypeError:
            view_model.list_of_typed_chars.clear()
            pass

    @staticmethod
    def on_release(key):
        if not view_model.start_macros:
            return

        if key == keyboard.Key.backspace or key == keyboard.Key.space:
            view_model.list_of_typed_chars.clear()
        if key == keyboard.Key.esc:
            # Stop listener
            view_model.list_of_typed_chars.clear()
            view_model.set_macros(False)
            # return False

    def start(self):
        listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)
        listener.start()