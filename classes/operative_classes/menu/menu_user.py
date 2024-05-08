from dataclasses import dataclass
import os
from openpyxl import load_workbook
from openpyxl import Workbook
import pandas as pd
import numpy as np
from datetime import datetime

from classes.operative_classes.table.main_page_table import MainPage
from conf.var import DB_NAME, USERLIST_TITLES


@dataclass
class MenuUser:
    user: str

    def _find_by(self, value):
        pass

    def _edit_balance(self, table: MainPage, value: int, description: str):
        page = table.table[self.user]
        if value > 0:
            operand = "Пополнение"
        else:
            operand = "Списание"
        page.append([datetime.now(), operand, value, description])
        table.table.save(f"{DB_NAME}.xlsx")

    def _get_data(self, book: Workbook):
        data = np.array([val for val in book[self.user].values])
        return data

    def _get_book(self):
        return load_workbook(os.path.abspath(f"{DB_NAME}.xlsx"))

    def get_menu(self, table):
        val = int(input("Add balance\n"))
        description = input("Add description\n")
        self._edit_balance(table, val, description)
        book = self._get_book()
        data = self._get_data(book)
        df = pd.DataFrame(data=data[1:], columns=data[0])
        print(df)

    # def get_user_histiry(self, col=None):
    #     while
    #     if col is None
