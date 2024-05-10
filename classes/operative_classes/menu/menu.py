from dataclasses import dataclass
from typing import Union
from openpyxl import Workbook
from classes.operative_classes.menu.menu_auth import MenuAuthentication
from classes.operative_classes.menu.menu_register import MenuRegistration


@dataclass
class MainMenuCLI:
    table: Workbook

    """Главное меню входа
    Здесь вы можете осуществитель авторизацию, регистрацию и завершение работы приложения.
    
    ВАЖНО: После завершения экземпляр MainPage() будет удален и данные в БД ,при новом запуске, будут перезаписаны.
    (!) Здесь можно поставить доп. проверку на то, чтобы файл удалял старые данные при новом запусе приложении."""

    def __greetengs_user(self) -> None:
        """Приветствие"""
        print("\n--Меню входа--\n")

    def __make_choise(self, choice: int) -> Union[str, bool]:
        """Логика выбора
        После отказа в аутентификации можно вернутся к логике регистрации.
        На выходе будет либо отказ в доступе, либо логин пользователя (login), по которому будет осуществен переход к странице опрераций конткретного пользователя
        """
        if choice == "0":
            return None
        elif choice == "1":
            MenuRegistration(self.table).registration()
        return MenuAuthentication(self.table).authentication()

    def __choise_auth(self) -> Union[Union[str, bool], None]:
        """Меню входа"""
        while True:
            choice = input(
                "Если вы хотите зарегистрироваться или войти в систему,"
                "то выберите необходимый пункт (1 или 2)\n1 - Регистрация\n2 - Авторизация\n0 - Закрыть приложение\n"
            )
            if choice in ["0", "1", "2"]:
                break
            print("\nНекорректный выбор. Повторите еще раз\n")
        return self.__make_choise(choice)

    def start_menu(self) -> Union[str, bool]:
        """Логика  меню входа
        Будет работать до тех пор, пока пользователь не закроет приложение, либо принудительно через консоль через ctrl+C не вырубит процесс
        """
        self.__greetengs_user()
        while True:
            response = self.__choise_auth()
            if response is None:
                quit()
            elif not response:
                continue
            return response
