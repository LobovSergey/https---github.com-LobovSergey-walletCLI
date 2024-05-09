from dataclasses import dataclass
import hashlib
from classes.operative_classes.table.main_page_table import MainPage
from classes.operative_classes.user import User
from time import sleep


@dataclass
class MenuRegistration:
    table: MainPage = None

    def _decode_pass(self, password: str) -> str:
        b_pass = password.encode()
        return hashlib.sha256(b_pass).hexdigest()

    def registration(self) -> None:
        print("\n--Регистрация--\n")
        while True:
            login = input("Ведите логин:\n")
            if self.table.check_login(login):
                break
            print("Ваш логин не уникален. Повторите еще раз")
        password = input("Ведите пароль:\n")
        password_hash = self._decode_pass(password)
        user = User(login, password_hash)
        user.create(self.table)
        print(
            "Регистрация прошла успешно. Сейчас будете перенаправлены на страницу авторизации"
        )
        sleep(0.5)
        print("------")
        sleep(0.5)
