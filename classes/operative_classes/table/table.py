from openpyxl import Workbook
from conf.var import DB_NAME, MAIN_PAGE, USERLIST_TITLES


class Table:

    def __init__(self) -> None:
        self.table = Workbook()

    def save(self):
        self.table.save(f"{DB_NAME}.xlsx")

    def _user_append(self, login, password):
        page = self.table[MAIN_PAGE]
        page.append([login, password])

    def _userlist_create(self, login):
        self.table.create_sheet(login)
        page = self.table[login]
        page.append(USERLIST_TITLES)

    def user_create(self, login, password):
        self._user_append(login, password)
        self._userlist_create(login)
        self.save()
