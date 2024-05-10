from openpyxl import Workbook
from classes.operative_classes.menu.menu import MainMenuCLI
from classes.operative_classes.menu.menu_user import MenuUser


def personal_account(username: str, table):
    """Процесс работы с личным кабиентом пользователя"""
    user_menu = MenuUser(username)
    user_menu.get_usermenu(table)


def entrance(table: Workbook) -> str:
    """Процесс работы со входом в приложение"""
    main_menu = MainMenuCLI(table)
    response = main_menu.start_menu()
    return response


def main_process(table: Workbook):
    """Главный процесс приложения"""
    while True:
        username = entrance(table)
        personal_account(username, table)
