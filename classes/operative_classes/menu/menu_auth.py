from dataclasses import dataclass
import hashlib
from classes.operative_classes.table.main_page_table import MainPage
from conf.var import MAIN_PAGE


@dataclass
class MenuAuthentication:
    table: MainPage = None

    def _decode_pass(self, password: str) -> str:
        b_pass = password.encode()
        return hashlib.sha256(b_pass).hexdigest()

    def _find_user(self, login: str, password: str):
        main_page = self.table.table[MAIN_PAGE]
        login_col = main_page["A"]
        index = -1
        for i in range(len(login_col)):
            if login_col[i].value == login:
                index = i
                break
        if index >= 0 and main_page["B"][index].value == self._decode_pass(password):
            return True
        return False

    def authentication(self) -> str:
        print("-Авторизация-")
        while True:
            login = input("Ведите логин:\n")
            password = input("Ведите пароль:\n")
            if self._find_user(login, password):
                break
            print("Неверный логин или пароль. Пропробуйте снова")
        print("Вы в системе")
        return login
