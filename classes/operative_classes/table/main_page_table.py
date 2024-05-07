from classes.operative_classes.table.table import Table
from conf.var import MAIN_PAGE


class MainPage(Table):

    def check_login(self, login):
        print(self.table.worksheets)
        input()
        main = self.table[MAIN_PAGE]
        if login not in main:
            return True
        return False

    def check_user(self, login, password):
        main = self.table[MAIN_PAGE]

    def main_list_create(self):
        main_page = self.table.worksheets[0]
        main_page.title = MAIN_PAGE
        self._save()
