from classes.operative_classes.table.table import Table
from conf.var import MAIN_PAGE


class MainPage(Table):

    def check_login(self, login):
        main = self.table[MAIN_PAGE]
        if login not in main:
            return True
        return False

    def main_list_create(self):
        main_page = self.table.active
        main_page.title = MAIN_PAGE
        self._save()
