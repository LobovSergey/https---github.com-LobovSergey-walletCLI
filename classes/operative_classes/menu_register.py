from classes.operative_classes.menu import MainMenuCLI


class MenuRegistration(MainMenuCLI):

    @classmethod
    def registration(self):
        print("-Регистрация-")
        while True:
            login = input("Ведите логин:\n")
            if table.is_unique(login):
                break
            print("Ваш логин не уникален. Повторите еще раз")
        password = input("Ведите пароль:\n")
