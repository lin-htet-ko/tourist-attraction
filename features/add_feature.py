from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class AddFeature(Feature):

    ADD_ITEM = 1

    menu = {
        Feature.HEADER: "Please choose the menu id to perform the task",
        ADD_ITEM: "Add a new destination",
        Feature.EXIT: "Exit"
    }

    feature = None

    def start(self):
        while True:
            self.show_menu(menu=AddFeature.menu)

            Feature.start(self)

            match self.selected_menu:
                case AddFeature.ADD_ITEM:
                    self.__display_info()
                case Feature.EXIT:
                    break

    def __load_data(self):
        self.places = self.reader.read_file(DataUtils.SOURCE_PATH)
        return self.reader.as_two_dimension_list(self.places[1:])

    def __display_info(self):

        destination = self.__input_destination()
        region = self.__input_region()
        country = self.__input_country()
        category = self.__input_category()

        annual_tourists = input("Enter Annual Tourists of the attraction (or Press enter to skip) : ")
        currency = input("Enter Currency of the attraction (or Press enter to skip) : ")
        famous_foods = input("Enter Famous Foods of the attraction (or Press enter to skip) : ")
        best_time = input("Enter Best Time to Visit the attraction (or Press enter to skip) : ")
        cost_of_living = input("Enter Cost of Living of the attraction (or Press enter to skip) : ")
        safety = input("Enter Safety of the attraction (or Press enter to skip) : ")
        description = input("Enter Description of the attraction (or Press enter to skip) : ")

        self.__set_default_values(destination, region, country, category, annual_tourists, currency, famous_foods, best_time, cost_of_living, safety, description)

    def __input_destination(self):
        destination = input("Enter Destination of the attraction : ")
        if destination == "":
            self.util_view.show_border("Destination is a required field. Please try again.")
            destination = self.__input_destination()
        return destination

    def __input_region(self):
        region = input("Enter Region of the attraction : ")
        if region == "":
            self.util_view.show_border("Region is a required field. Please try again.")
            region = self.__input_region()
        return region

    def __input_country(self):
        country = input("Enter Country of the attraction : ")
        if country == "":
            self.util_view.show_border("Country is a required field. Please try again.")
            country = self.__input_country()
        return country

    def __input_category(self):
        category = input("Enter Category of the attraction : ")
        if category == "":
            self.util_view.show_border("Category is a required field. Please try again.")
            category = self.__input_category()
        return category

    def __set_default_values(self, destination, region, country, category, annual_tourists, currency, famous_foods, best_time, cost_of_living, safety, description):
        # Get the _id of the new item
        _id = 0
        try:
            _id = len(self.__load_data()[-1][0]) + 1
        finally:
            _id = len(self.__load_data()) + 2

        # if the user skips the input, set the default value
        if annual_tourists == "":
            annual_tourists = "Not Available"
        if currency == "":
            currency = "Not Available"
        if famous_foods == "":
            famous_foods = "Not Available"
        if best_time == "":
            best_time = "Not Available"
        if cost_of_living == "":
            cost_of_living = "Not Available"
        if safety == "":
            safety = "Not Available"
        if description == "":
            description = "Not Available"

        self.__add_item(_id, destination, region, country, category, annual_tourists, currency, famous_foods, best_time, cost_of_living, safety, description)

    def __add_item(self, _id, destination, region, country, category, annual_tourists, currency, famous_foods, best_time,
                 cost_of_living, safety, description):
        # Open the file in append mode with newline='' to avoid extra blank lines
        with open(DataUtils.SOURCE_PATH, mode='a', newline='', encoding='utf-8') as file:
            row = f"{_id},{destination},{region},{country},{category},{annual_tourists},{currency},\"{famous_foods}\",{best_time},{cost_of_living},{safety},\"{description}\"\n"
            file.write(row)

        self.__display_added_item(_id, destination, region, country, category, annual_tourists, currency, famous_foods,
                                best_time, cost_of_living, safety, description)

    def __display_added_item(self, _id, destination, region, country, category, annual_tourists, currency, famous_foods,
                           best_time, cost_of_living, safety, description):
        # Display the added item
        print("\nSuccessfully added the following item:")
        print("\n" + "=" * 40)
        print(
            f"{_id} | {destination} | {region} | {country} | {category} | {annual_tourists} | {currency} | {famous_foods} | {best_time} | {cost_of_living} | {safety} | {description}")
        print("=" * 40 + "\n")

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if AddFeature.feature is None:
            AddFeature.feature = AddFeature(reader=self, table_view=table_view, util_view=util_view, menu_utils=menu_utils)
        return AddFeature.feature