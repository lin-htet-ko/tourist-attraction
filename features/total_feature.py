from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.key import Key
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class TotalFeature(Feature):

    BY_COUNTRY = 1
    BY_TRAVELTIME = 2
    BY_CURRENCY = 3

    menu = {
        Feature.HEADER: "Please choose the menu id to see the total value",
        BY_COUNTRY: "Display the total number by country.",
        BY_TRAVELTIME: "Display the total number by travel-time.",
        BY_CURRENCY: "Display the total number by currency.",
        Feature.EXIT: "Exit"
    }

    feature = None

    def start(self):
        while True:
            Feature.show_menu(self, menu=TotalFeature.menu)
            Feature.start(self)

            match self.selected_menu:
                case TotalFeature.BY_COUNTRY:
                    self.__total_destinations_by_country()
                case TotalFeature.BY_TRAVELTIME:
                    self.__total_destinations_by_traveltime()
                case TotalFeature.BY_CURRENCY:
                    self.__choose_currency()
                case Feature.EXIT:
                    break

    def __load_dimen_list(self):
        places = self.reader.read_file(DataUtils.SOURCE_PATH)
        return self.reader.as_two_dimension_list(places)

    def __load_map_list(self):
        places = self.reader.read_file(DataUtils.SOURCE_PATH)
        return self.reader.transform_data(places)

    def __total_destinations_by_country(self):
        data = self.__load_map_list()
        # Extract unique countries from the data
        unique_countries = set(row[Key.COUNTRY] for row in data)

        # Display the list of available countries
        self.util_view.show_border(message="The list of countries:", deco="=")
        for country in unique_countries:  # Changed to iterate over unique countries
            print(country)
            self.util_view.show_line(size=len(country))

        # Showing the total number of destinations by country
        country_name = input("Enter your desired country name: ").strip().capitalize()
        count = sum(1 for row in data if row['Country'] == country_name)
        self.util_view.show_border(f'Total number of destinations in {country_name}: {count}')

        # Showing the list of destinations
        if count > 0:
            self.util_view.show_border(f"Here are the Destinations you can travel in {country_name}:")
            for row in data:
                if row['Country'] == country_name:
                    message = f"{row['Country']} - {row['Destination']}"
                    print(message)
                    self.util_view.show_line(len(message))

    def __total_destinations_by_traveltime(self):
        travel_time = input(
            "Which time would you like to travel (e.g., Summer, Winter, Spring, Fall, Year-round)? ").strip().capitalize()
        matched_countries = set()

        # Filter the data for countries that match the travel time
        data = self.__load_map_list()
        for row in data:
            if travel_time in row['Best Time to Visit']:
                matched_countries.add(row['Country'])

        num_countries = len(matched_countries)

        # Showing the list of countries
        if num_countries > 0:
            self.util_view.show_border(f"You can travel to {num_countries} countries during {travel_time}:")
            for country in matched_countries:
                print(country)
                self.util_view.show_line(len(country))

            # Ask the user to select a country
            country = input("Which country would you like to travel to? ").strip().capitalize()
            if country in matched_countries:
                destinations = [f"{row[Key.COUNTRY]} - {row[Key.DESTINATION]}" for row in data
                                if row[Key.COUNTRY] == country and travel_time in row['Best Time to Visit']]
                if destinations:
                    num_destinations = len(destinations)
                    msg = f"You can travel to {num_destinations} destinations in {country} during {travel_time}:"
                    print(msg)
                    print(f"Here are the destinations you can travel in {country}:")
                    self.util_view.show_line(len(msg))
                    print('\n'.join(destinations))
                else:
                    self.util_view.show_border(f"Sorry, no destinations found for {country}.")
            else:
                self.util_view.show_border(f"Sorry, {country} is not in the list of countries you can travel to.")
        else:
            self.util_view.show_border(f"Sorry, there are no countries available for {travel_time}.")

    def __choose_currency(self):
        currencies = {
            -1: "Please choose the currency",
            1: ("Euro", "Euros"),
            2: ("DKK", "Danish krone (DKK)"),
            3: ("RUB", "Russian Ruble (RUB)"),
            4: ("NOK", "Norwegian krone (NOK)"),
            5: ("SEK", "Swedish krona (SEK)"),
            6: ("CHF", "Swiss franc (CHF)"),
            7: ("TRY", "Turkish lira (TRY)"),
            8: ("UAH", "Ukrainian hryvnia (UAH)"),
            9: ("GBP", "British Pound Sterling (GBP)"),
            10: ("ISK", "Icelandic kr¢na (ISK)"),
            11: ("RSD", "Serbian dinar (RSD)"),
            12: "Exit"
        }

        while True:
            self.show_menu(currencies)

            selected_menu = int(input("Choose Currency: "))

            if selected_menu == 12:
                break

            two_dimen_list = self.__load_dimen_list()
            currency_data = currencies.get(selected_menu)
            if currency_data:
                data = []
                city_count = 0
                currency_code = currency_data[0]
                currency_name = currency_data[1]
                for row in two_dimen_list:
                    if currency_code in row[6]:
                        city_count += 1
                        data.append(row[1])  # Assuming country name is in the second column

                print(f'There are a total of {city_count} places where {currency_name} are used')
                print(f"Destinations where you can use {currency_name} Currency are:")
                print("\n".join([f"- {country}" for country in data]))
            else:
                self.util_view.show_border("Invalid selection. Please try again.")

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if TotalFeature.feature is None:
            TotalFeature.feature = TotalFeature(reader=self, table_view=table_view, util_view=util_view, menu_utils=menu_utils)
        return TotalFeature.feature
