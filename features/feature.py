from data.file_reader import FileReader
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView

class Feature:

    HEADER = -1
    EXIT = 0

    selected_menu = 0

    def __init__(self, reader: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        self.reader = reader
        self.menu_utils = menu_utils
        self.util_view = util_view
        self.table_view = table_view
        self.selected_menu = Feature.HEADER

    def get_menu_size(self, menu):
        return self.menu_utils.max_row_size(menu = menu)

    def show_menu(self, menu: dict):
        size = self.get_menu_size(menu) + 4
        self.util_view.show_line(size = size, deco = "=")
        for key in menu:
            m_key = f"{key} : "
            if key == -1:
                m_key = ""
            print(f"  {m_key}{menu[key]}")
            if key == -1:
                self.util_view.show_line(size= size, deco= "=")
        self.util_view.show_line(size = size, deco = "=")

    def start(self):
        self.selected_menu = int(input("Enter menu id: "))
