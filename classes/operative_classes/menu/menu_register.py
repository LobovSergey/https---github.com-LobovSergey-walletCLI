from classes.operative_classes.table.main_page_table import MainPage
from classes.operative_classes.user import User
from time import sleep


class MenuRegistration:

    def registration(self):
        print("-Регистрация-")
        while True:
            login = input("Ведите логин:\n")
            if MainPage().check_login(login):
                break
            print("Ваш логин не уникален. Повторите еще раз")
        password = input("Ведите пароль:\n")
        user = User(login, password)
        user.create()
        print("Регистрация прошла успешно. Сейчас будете перенаправлены на страницу авторизации")
        sleep(0.5)
        print("------")
        sleep(0.5)
