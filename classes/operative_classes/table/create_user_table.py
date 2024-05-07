from classes.operative_classes.table.table import Table
from conf.var import MAIN_PAGE


class TableUserCreate(Table):

    def _user_append(self, login, password):
        page = self.table[self.table.sheetnames[0]]
        page.append([login, password])

    def _userlist_create(self, login):
        self.table.create_sheet(login)

    def user_create(self, login, password):
        self._user_append(login, password)
        self._userlist_create(login)
        self._save()
