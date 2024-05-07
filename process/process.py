from classes.operative_classes.menu.menu import MainMenuCLI


def main_process(table):
    menu = MainMenuCLI(table)
    if not menu.start_menu():
        quit()
    pass


### продолжение логики
