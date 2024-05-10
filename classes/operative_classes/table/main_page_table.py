from classes.operative_classes.table.table import Table
from conf.var import MAIN_PAGE


class MainPage(Table):
    """Дочерний класс создания таблицы"""

    def check_login(self, login: str) -> bool:
        """Проверка вводимого логина на наличие зарегистрированного пользователя в программе. В противном случае будет отказано в доступе."""
        main = self.table[MAIN_PAGE]
        if login not in main:
            return True
        return False

    def main_list_create(self) -> None:
        """Создание главного листа таблицы, в которой будут храниться все пользователи и хэши их паролей"""
        main_page = self.table.active
        main_page.title = MAIN_PAGE
        self.save()
