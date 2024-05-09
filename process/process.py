from openpyxl import Workbook
from classes.operative_classes.menu.menu import MainMenuCLI
from classes.operative_classes.menu.menu_user import MenuUser


def personal_account(username: str, table):
    user_menu = MenuUser(username)
    user_menu.get_usermenu(table)


def entrance(table: Workbook) -> str:
    main_menu = MainMenuCLI(table)
    response = main_menu.start_menu()
    return response


def main_process(table: Workbook):
    while True:
        username = entrance(table)
        personal_account(username, table)
