from data.file_reader import FileReader
from features.add_feature import AddFeature
from features.delete_feature import DeleteFeature
from features.display_feature import DisplayFeature
from features.feature import Feature
from features.search_feature import SearchFeature
from features.total_feature import TotalFeature
from features.update_feature import UpdateFeature
from utils.menu_utils import MenuUtils
from view.menu import Menu
from view.table import TableView
from view.utils import UtilView


class TouristAttractionApp:
    DISPLAY = 1
    TOTAL = 2
    TOURIST = 3
    SEARCH = 4
    DELETE = 5
    UPDATE = 6

    menu = {
        Feature.HEADER: "Please choose the information you would like to display",
        DISPLAY: "Display Tourist Attraction Information.",
        TOTAL: "Display Total Number of Tourist Attraction.",
        TOURIST: "Add New Tourist Attraction.",
        SEARCH: "Search Tourist Attraction.",
        DELETE: "Delete Tourist Attraction.",
        UPDATE: "Update Tourist Attraction.",
        Feature.EXIT: "Exit"
    }

    # Initialize function
    def __init__(self):
        self.__reader = FileReader()
        self.__menu_utils = MenuUtils()
        self.__util_view = UtilView()
        self.__table_view = TableView(self.__util_view)
        self.menu = Menu(self.__util_view, self.__menu_utils)

    def start(self):
        # Get user input
        while True:

            self.menu.show_menu(menu=TouristAttractionApp.menu)
            menu_id = int(input("Enter menu : "))

            # Excute function base on user input
            try:
                if 0 <= menu_id < 7:
                    match menu_id:
                        case TouristAttractionApp.DISPLAY:
                            DisplayFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                    self.__menu_utils).start()
                        case TouristAttractionApp.TOTAL:
                            TotalFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                  self.__menu_utils).start()
                        case TouristAttractionApp.TOURIST:
                            AddFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                self.__menu_utils).start()
                        case TouristAttractionApp.SEARCH:
                            SearchFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                   self.__menu_utils).start()
                        case TouristAttractionApp.DELETE:
                            DeleteFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                   self.__menu_utils).start()
                        case TouristAttractionApp.UPDATE:
                            UpdateFeature.instance(self.__reader, self.__table_view, self.__util_view,
                                                   self.__menu_utils).start()
                        case Feature.EXIT:
                            break
                else:
                    self.__util_view.show_border("Invalid Choice!")
            except ValueError as ve:
                self.__util_view.show_border(f"Value error ===> {ve}")
            except Exception as e:
                self.__util_view.show_border(f"Value error ===> {e}")


TouristAttractionApp().start()
