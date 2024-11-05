from utils.menu_utils import MenuUtils
from view.utils import UtilView


class Menu:

    def __init__(self, util_view: UtilView, menu_utils: MenuUtils):
        self.menu_utils = menu_utils
        self.util_view = util_view

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