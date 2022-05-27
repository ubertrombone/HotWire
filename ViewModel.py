import csv
from datetime import date
import calendar


class ViewModel:

    def __init__(self):
        super(ViewModel, self).__init__()
        self.start_macros = False
        self.list_of_typed_chars = list()
        self.hot_keys = {}

    def set_macros(self, enabled):
        self.start_macros = enabled

    def clear_macros(self):
        self.hot_keys.clear()

    def read_csv(self, file):
        data = csv.reader(open(file, "r", encoding='utf-8-sig'))
        self.hot_keys[".day"] = calendar.day_name[date.today().weekday()]
        self.hot_keys[".month"] = calendar.month_name[date.today().month]
        for row in data:
            self.hot_keys[row[0]] = row[1]
