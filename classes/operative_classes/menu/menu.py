from classes.operative_classes.menu.menu_auth import MenuAuthentication
from classes.operative_classes.menu.menu_register import MenuRegistration


class MainMenuCLI:

    def __make_choise(self, choice):
        if choice == 1:
            MenuRegistration().registration()
        MenuAuthentication().authentication()

    def __choise_auth(self):
        while True:
            choice = int(
                input(
                    "Добро пожаловать!\n Если вы хотите зарегистрироваться или войти в систему,"
                    "то выберите необходимый пункт (1 или 2)\n1 - Регистрация\n2 - Авторизация\n"
                )
            )
            if choice in [1, 2]:
                break
            print("Некорректный выбор. Повторите еще раз")
        self.__make_choise(choice)

    def __greetengs_user(self):
        print("Доброе пожаловать\n")

    def start_menu(self) -> None:
        self.__greetengs_user()
        self.__choise_auth()
