from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class DeleteFeature(Feature):
    BY_COL_NAME_VAL = 1
    BY_ROW_COUNT = 2

    menu = {
        Feature.HEADER: "Please choose the menu id to delete",
        BY_COL_NAME_VAL: "Delete the entire row by column name and value",
        BY_ROW_COUNT: "Delete by the rows count",
        Feature.EXIT: "Exit"
    }

    feature = None

    def start(self):
        while True:
            Feature.show_menu(self, menu=DeleteFeature.menu)
            Feature.start(self)

            match self.selected_menu:
                case DeleteFeature.BY_COL_NAME_VAL: self.delete_rows_by_column_and_value()
                case DeleteFeature.BY_ROW_COUNT: self.delete_rows_by_count()
                case Feature.EXIT: break

    def __load_data(self):
        places = self.reader.read_file(DataUtils.SOURCE_PATH)
        headers = places[0]  # First line is the header
        data = places[1:]
        return headers, data

    def __save_csv(self, headers, data):
        #Save the updated data back to the CSV file
        with open(DataUtils.SOURCE_PATH, mode='w', encoding='utf-8') as file:
            file.write(','.join(headers))  # Write headers
            for row in data:
                file.write(','.join(row))  # Write each row

    def delete_rows_by_column_and_value(self):
        try:
            # Delete rows where a specific column matches the value.
            headers, data = self.__load_data()
            column_name = str(input("Enter the name of the column you want to delete from: "))
            value = str(input("Enter the value of the column you want to delete: "))

            if column_name not in headers:
                raise ValueError(f"Column '{column_name}' not found in CSV headers.")

            # Find index of the column
            col_index = headers.index(column_name)

            # Find matching rows
            matching_rows = [row for row in data if row[col_index] == value]

            if len(matching_rows) == 0:
                self.util_view.show_border(f"No rows found where '{column_name}' is '{value}'. No deletion performed.")
                return

            self.util_view.show_border(f"Found {len(matching_rows)} row(s) matching '{column_name} = {value}':")
            for row in matching_rows:
                print(row)
            print()

            # Confirm with the user before deletion
            confirm = str(input(f"Do you want to delete all rows where '{column_name}' is '{value}'? (yes/no): ").strip().lower())

            if confirm == "yes":
                # Filter out rows where the column matches the value
                filtered_data = [row for row in data if row[col_index] != value]

                # Save the filtered data back to the file
                self.__save_csv(headers, filtered_data)
                self.util_view.show_border(f"Deleted all rows where '{column_name}' is '{value}'.")

            elif confirm == "no":
                self.util_view.show_border("Deletion cancelled")

            else:
                self.util_view.show_border("Invalid choice")

        except ValueError as e:
            self.util_view.show_border(f"ValueError: {e}")
        except Exception as e:
            self.util_view.show_border(f"An error occurred: {e}")

    def delete_rows_by_count(self):
        try:
            headers, data = self.__load_data()
            total_rows = len(data)
            self.util_view.show_border(f"The CSV file contains {total_rows} rows excluding headers.")
            num_rows_to_delete = int(input("Enter the number of rows you want to delete: "))

            if num_rows_to_delete <= 0 or num_rows_to_delete > total_rows:
                self.util_view.show_border(f"Invalid input. You can only delete between 1 and {total_rows} row(s).")
                return

            position = input("Do you want to delete from the (top/bottom)? ").strip().lower()

            confirm = input(f"Do you want to delete {num_rows_to_delete} row(s) from the {position}? (yes/no): ").strip().lower()

            if confirm == "yes":
                if position == "top":
                    filtered_data = data[num_rows_to_delete:]  # Remove the first 'num_rows_to_delete' rows
                elif position == "bottom":
                    filtered_data = data[:-num_rows_to_delete]  # Remove the last 'num_rows_to_delete' rows
                else:
                    self.util_view.show_border("Invalid position entered. Deletion cancelled.")
                    return

                # Save the filtered data back to the file
                self.__save_csv(headers, filtered_data)
                self.util_view.show_border(f"Deleted {num_rows_to_delete} row(s) from the {position}.")
            elif confirm == "no":
                self.util_view.show_border("Deletion cancelled.")
            else:
                self.util_view.show_border("Invalid choice.")
        except ValueError:
            self.util_view.show_border("Invalid input for the number of rows. Please enter a valid integer.")
        except Exception as e:
            self.util_view.show_border(f"An error occurred: {e}")

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if DeleteFeature.feature is None:
            DeleteFeature.feature = DeleteFeature(reader=self, table_view=table_view, util_view=util_view, menu_utils=menu_utils)
        return DeleteFeature.feature