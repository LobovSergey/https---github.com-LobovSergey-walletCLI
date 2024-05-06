from classes.operative_classes.table.table import Table
from conf.var import MAIN_PAGE


class MainPage(Table):

    def main_list_create(self):
        main_page = self.table.active
        main_page.title = MAIN_PAGE
