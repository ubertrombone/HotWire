class ViewModel:

    def __init__(self):
        super(ViewModel, self).__init__()
        self.start_macros = False
        self.list_of_typed_chars = list()
        self.hot_keys = {".gr": "Hello world!", ".ww": "Have a wonderful Wednesday!"}

    def set_macros(self, enabled):
        self.start_macros = enabled
