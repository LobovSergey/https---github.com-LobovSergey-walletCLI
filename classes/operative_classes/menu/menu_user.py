from dataclasses import dataclass
import os
from openpyxl import load_workbook
from openpyxl import Workbook
from pandas import DataFrame
import numpy as np
from numpy.typing import NDArray
from datetime import datetime
from classes.operative_classes.table.main_page_table import MainPage
from conf.var import (
    DB_NAME,
    USERLIST_TITLES,
    USERMENU_CHOISES,
    HISTORY_CHOISES,
    SEARCH_CHOISES,
    SORT_CHOISES,
)


@dataclass
class MenuUser:
    user: str
    balance = int

    def _add_value_at_balance(self, value: int, operand: bool) -> None:
        if operand:
            self.balance += value
        else:
            self.balance -= value

    def _set_balance(self) -> None:
        data = self._get_frame()
        self.balance = data[USERLIST_TITLES[2]].sum()

    def _get_frame(self) -> DataFrame:
        book = self._get_book()
        data = self._get_array(book)
        data_frame = DataFrame(data=data[1:], columns=data[0])
        return data_frame

    def _edit_balance(self, table: MainPage, flag: bool = None) -> None:
        if flag:
            operand = "Пополнение"
        else:
            operand = "Списание"
        while True:
            try:
                value = int(input(f"\n--{operand}--\nВведите сумму:\n"))
                if not flag:
                    if self.balance >= value:
                        break
                else:
                    break
                print("Недопустимая сумма")
            except ValueError:
                print("Некорректный ввод")

        description = input("Введите описание операциии (опционально)\n")
        page = table.table[self.user]
        page.append([datetime.now(), operand, value, description])
        self._add_value_at_balance(value=value, operand=flag)
        table.save()

    def _get_array(self, table: Workbook) -> NDArray:
        return np.array([val for val in table[self.user].values])

    def _get_book(self) -> Workbook:
        return load_workbook(os.path.abspath(f"{DB_NAME}.xlsx"))

    def _sort_by(self, frame: DataFrame) -> None:
        while True:
            choise = input(SORT_CHOISES)
            if choise == "0":
                return
            elif choise in ["1", "2", "3"]:
                print(frame.sort_values(USERLIST_TITLES[int(choise) - 1]))
            else:
                print("Некорректный выбор. Попробуйте еще раз")

    def _search_by(self, frame: DataFrame):
        while True:
            choise = input(SEARCH_CHOISES)
            if choise == "0":
                return
            elif choise in ["1", "2", "3"]:
                searched = input("Искомое значение:\n")
                if choise != "2":
                    choise = int(choise)
                print(frame[frame[USERLIST_TITLES[int(choise) - 1]] == searched])
            else:
                print("Некорректный выбор. Попробуйте еще раз")

    def _edit_operation(self, frame: DataFrame) -> None:
        while True:
            choise = input("Введите номер строки: (< - назад)")
            if choise == "<":
                return
            try:
                string = frame.iloc[[]]
                print("Выберите поле по которому хотите изменить данные")
                for i in range(len(USERLIST_TITLES)):
                    print(f"{i+1} - {USERLIST_TITLES[i]}")
                choise_col = int(input())
                value = input("Введите новое значение:\n")
                frame.at[int(choise), USERLIST_TITLES[choise_col - 1]] = value

            except ValueError:
                print("Некорректный выбор. Попробуйте еще раз")
            except KeyError:
                print("Такого столбца нет")

    def _get_histiry(self) -> None:
        data_frame = self._get_frame()
        while True:
            print(f"--История операций--\n{data_frame}")
            choise = input(HISTORY_CHOISES)
            if choise == "0":
                return
            elif choise == "1":
                self._sort_by(data_frame)
            elif choise == "2":
                self._search_by(data_frame)
            elif choise == "3":
                self._edit_operation(data_frame)
            else:
                print("Некорректный выбор. Попробуйте еще раз")

    def get_usermenu(self, table: Workbook, choise: int = None) -> None:
        self._set_balance()
        while True:
            print(
                f"\n--Личный кабинет --\nПользователь : {self.user}\nБаланс: {self.balance}"
            )
            choise = input(USERMENU_CHOISES)
            if choise == "0":
                return
            elif choise == "1":
                self._edit_balance(table=table, flag=True)
            elif choise == "2":
                self._edit_balance(table=table, flag=False)
            elif choise == "3":
                self._get_histiry()
            else:
                print("Некорректный выбор. Попробуйте еще раз")
