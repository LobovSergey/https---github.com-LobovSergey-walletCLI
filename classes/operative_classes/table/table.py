from dataclasses import dataclass
from openpyxl import Workbook
from conf.var import DB_NAME, MAIN_PAGE, USERLIST_TITLES


@dataclass
class Table:
    """Родительский класс таблицы. Инициализирует пустую таблицу"""

    def __init__(self) -> None:
        self.table = Workbook()

    def save(self) -> None:
        """Переопределение базового .save() для присвоения имени файла"""
        self.table.save(f"{DB_NAME}.xlsx")

    def _user_append(self, login: str, password: str) -> None:
        """Внутренний метод создания пользователя на главной странице. Вызывается только в том случае, если пользователь прошел регистрацию"""
        page = self.table[MAIN_PAGE]
        page.append([login, password])

    def _userlist_create(self, login: str) -> None:
        """После регистрации пользователя будет создан отдельный лист, в котором будет храниться вся информация о его операциях. Доступ к ней будет только после авторизации"""
        self.table.create_sheet(login)
        page = self.table[login]
        page.append(USERLIST_TITLES)

    def user_create(self, login: str, password: str) -> None:
        """Создание нового пользователя и его листа в таблице"""
        self._user_append(login, password)
        self._userlist_create(login)
        self.save()
