from openpyxl import Workbook
from conf.var import DB_NAME
from main_page_table import MainPage


class Table:

    def __init__(self) -> None:
        self.table = Workbook()

    def _save(self):
        self.table.save(f"src/{DB_NAME}.xls")

    def create_table(self):
        main_page = MainPage()
        main_page.main_list_create()
        self._save()
