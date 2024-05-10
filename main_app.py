from classes.operative_classes.table.main_page_table import MainPage

from process.process import main_process


def start_app() -> None:
    """Старт приложения"""
    table = MainPage()
    table.main_list_create()
    main_process(table)


if __name__ == "__main__":
    start_app()
