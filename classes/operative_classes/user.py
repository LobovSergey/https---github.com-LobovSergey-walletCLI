from dataclasses import dataclass

from classes.operative_classes.table.main_page_table import MainPage


@dataclass
class User:
    login: str = None
    password: str = None

    """Создание нового пользователя"""

    def __str__(self) -> str:
        return self.login

    def create(self, table: MainPage) -> None:
        """Создание нового пользователя в таблице"""
        table.user_create(login=self.login, password=self.password)
