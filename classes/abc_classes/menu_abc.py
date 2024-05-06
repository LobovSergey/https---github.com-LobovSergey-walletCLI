from abc import ABC, abstractmethod


class MenuABC(ABC):

    @abstractmethod
    def _greetengs_user(self):
        pass

    @abstractmethod
    def _login_user(self):
        pass

    @abstractmethod
    def start_menu(self):
        pass
