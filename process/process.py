from openpyxl import Workbook
from classes.operative_classes.menu.menu import MainMenuCLI
from classes.operative_classes.menu.menu_user import MenuUser


def personal_account(username: str, table):
    user_menu = MenuUser(username)
    user_menu.get_menu(table)


def entrance(table: Workbook) -> str:
    main_menu = MainMenuCLI(table)
    response = main_menu.start_menu()
    if not response:
        quit()
    return response


def main_process(table: Workbook):
    username = entrance(table)
    personal_account(username, table)


### продолжение логики
