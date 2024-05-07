
from dataclasses import dataclass

from classes.operative_classes.table.create_user_table import TableUserCreate


@dataclass
class User:
    login: str = None
    password: str = None

    def __str__(self) -> str:
        return self.login

    def create(self):
        TableUserCreate().user_create(login=self.login, password=self.password)
