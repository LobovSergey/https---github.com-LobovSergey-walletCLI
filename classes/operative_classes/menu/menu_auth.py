from classes.operative_classes.table.main_page_table import MainPage


class MenuAuthentication:

    @classmethod
    def authentication(self):
        print("-Авторизация-")
        while True:
            login = input("Ведите логин:\n")
            password = input("Ведите пароль:\n")
            break
        print("Вы в системе")
