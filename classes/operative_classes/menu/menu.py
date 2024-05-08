from dataclasses import dataclass
from typing import Union
from openpyxl import Workbook
from classes.operative_classes.menu.menu_auth import MenuAuthentication
from classes.operative_classes.menu.menu_register import MenuRegistration


@dataclass
class MainMenuCLI:
    table: Workbook

    def __greetengs_user(self) -> None:
        print("Добро пожаловать!\n")

    def __make_choise(self, choice: int) -> Union[str, bool]:
        if choice == 0:
            return False
        elif choice == 1:
            MenuRegistration(self.table).registration()
        return MenuAuthentication(self.table).authentication()

    def __choise_auth(self) -> Union[str, bool]:
        while True:
            choice = int(
                input(
                    "Если вы хотите зарегистрироваться или войти в систему,"
                    "то выберите необходимый пункт (1 или 2)\n1 - Регистрация\n2 - Авторизация\n0 - Закрыть приложение\n"
                )
            )
            if choice in [0, 1, 2]:
                break
            print("Некорректный выбор. Повторите еще раз")
        return self.__make_choise(choice)

    def start_menu(self) -> Union[str, bool]:
        self.__greetengs_user()
        return self.__choise_auth()
