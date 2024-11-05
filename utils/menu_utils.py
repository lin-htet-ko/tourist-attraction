class MenuUtils:

    menu_utils = None

    def max_row_size(self, menu: dict):
        max_list = []
        for key in menu:
            max_list.append(len(menu[key]))
        return max(max_list)
    
    @staticmethod
    def instance():
        if MenuUtils.menu_utils is None:
            MenuUtils.menu_utils = MenuUtils()
        return MenuUtils.menu_utils