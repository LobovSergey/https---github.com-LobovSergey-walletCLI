from openpyxl import Workbook
from classes.operative_classes.menu.menu import MainMenuCLI
from classes.operative_classes.menu.menu_user import MenuUser
from classes.operative_classes.table.main_page_table import MainPage


def personal_account(username: str, table):
    """Процесс работы с личным кабиентом пользователя"""
    user_menu = MenuUser(username)
    user_menu.get_usermenu(table)


def entrance(table: Workbook) -> str:
    """Процесс работы со входом в приложение"""
    main_menu = MainMenuCLI(table)
    response = main_menu.start_menu()
    return response


def prepare_table() -> Workbook:
    """Процесс создания таблицы(файла)"""
    table = MainPage()
    table.main_list_create()
    return table


def main_process() -> None:
    """Главный процесс приложения"""
    table = prepare_table()
    while True:
        username = entrance(table)
        personal_account(username, table)
