from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.cost_of_living import CostOfLiving
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class DisplayFeature(Feature):
    EXP_LIVING = 1
    BUDGET_LIVING = 2
    ANNUAL_TOUR = 3
    SAFETY = 4

    menu = {
        Feature.HEADER: "Please choose the information you would like to display",
        EXP_LIVING: "Display Most Expensive Cost of Living.",
        BUDGET_LIVING: "Display Budget Cost of Living.",
        ANNUAL_TOUR: "Display Most Approximate Annual Tourists.",
        SAFETY: "Display Most Safety Tourist Attractions.",
        Feature.EXIT: "Exit"
    }

    feature = None

    def start(self):
        while True:
            self.__loadInitData()
            Feature.show_menu(self, menu=DisplayFeature.menu)
            Feature.start(self)

            match self.selected_menu:
                case DisplayFeature.EXP_LIVING:
                    self.__displayExpensiveCostOfLiving()
                case DisplayFeature.BUDGET_LIVING:
                    self.__displayBudgetCostOfLiving()
                case DisplayFeature.ANNUAL_TOUR:
                    self.__displayMostAnnualTourists()
                case DisplayFeature.SAFETY:
                    self.__displayBudgetCostOfLiving()
                case Feature.EXIT:
                    break

    def __loadInitData(self):
        self.places = self.reader.read_file(DataUtils.SOURCE_PATH)
        self.file_result = self.reader.transform_data(self.places)
        self.header_info = self.table_view.get_header_info(header=self.file_result[0])

    def __displayInfo(self, title: str):
        col = self.file_result[1:]
        print(f"\n{title}\n")
        self.table_view.show_header(self.header_info)
        for row in col:
            self.table_view.row_with_deco(row=row, header_infos=self.header_info)

    def __displayExpensiveCostOfLiving(self):
        self.__displayInfo(
            title="The most expensive cost of living"
        )

    def __displayBudgetCostOfLiving(self):
        self.__displayInfo(
            title="The most budget cost of living"
        )

    def __displayMostAnnualTourists(self):
        self.__displayInfo(
            title="Top 10 most Annual tourist attractions"
        )

    def __displayMostSafetyAttraction(self):
        self.__displayInfo(
            title="Top 10 most Safety tourist attractions"
        )

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if DisplayFeature.feature is None:
            DisplayFeature.feature = DisplayFeature(reader=self, table_view=table_view, util_view=util_view, menu_utils=menu_utils)
        return DisplayFeature.feature
