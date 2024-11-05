from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class SearchFeature(Feature):
    feature = None

    def start(self):
        self.__search_attraction()

    def __load_data(self):
        places = self.reader.read_file(DataUtils.SOURCE_PATH)
        return self.reader.as_two_dimension_list(places)

    def __search(self, keyword):
        search_list = self.__load_data()
        results = []
        for row in search_list:
            if any(keyword.lower() in str(cell).lower() for cell in row):
                results.append(row)
        return results if results else None

    def __print_table(self, results):
        if results:
            # Define the headers
            headers = ["ID", "Destination", "Region", "Country", "Category", "Annual Tourists", "Currency",
                       "Famous Foods", "Best Time to Visit", "Cost of Living", "Safety", "Description"]

            # Calculate the maximum width for each column including headers and data
            max_column_count = max(len(row) for row in results)  # Max length of any row in results
            header_widths = [len(header) for header in headers]
            column_widths = [max(len(str(cell)) for cell in column) for column in zip(*results)]

            # Use min to avoid index errors if results have fewer columns than headers
            max_widths = [max(header_widths[i], column_widths[i]) if i < len(header_widths) else column_widths[i]
                          for i in range(max_column_count)]

            # Create the header row
            header_row = ' | '.join(f"{str(headers[i]):<{max_widths[i]}}" for i in range(len(headers)))
            print(header_row)

            # Create a separator line based on the total width of the columns and separators
            separator_length = sum(max_widths) + 3 * (len(headers) - 1)  # Adjust for spacing
            separator_line = '-' * separator_length
            print(separator_line)

            # Print the data rows without text wrapping
            for row in results:
                formatted_row = []
                for i in range(max_column_count):
                    if i < len(row):  # Check to prevent IndexError
                        cell = row[i]
                        # Truncate if cell is longer than the maximum width
                        cell_str = str(cell)[:max_widths[i] - 3] + '...' if len(str(cell)) > max_widths[i] else str(
                            cell)
                        formatted_row.append(f"{cell_str:<{max_widths[i]}}")
                    else:
                        formatted_row.append(' ' * max_widths[i])  # Fill empty cells with spaces
                print(' | '.join(formatted_row))
        else:
            self.util_view.show_border("No matches found.")

    def __search_attraction(self):
        while True:
            keyword = input("\nEnter a keyword to search (or type 'back' to return): ")
            if keyword.lower() == 'back':
                self.util_view.show_border("Returning to the main menu.....")
                break  # Exit the loop to return to the main menu

            search_results = self.__search(keyword)

            # Display the results in a table format if matches are found
            if search_results:
                print("\nHere are the search results:")
                self.__print_table(search_results)
            else:
                self.util_view.show_border("Sorry... No matches found.")

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if SearchFeature.feature is None:
            SearchFeature.feature = SearchFeature(reader=self, table_view=table_view, util_view=util_view, menu_utils=menu_utils)
        return SearchFeature.feature