from data.file_reader import FileReader
from data.utils import DataUtils
from features.feature import Feature
from utils.menu_utils import MenuUtils
from view.table import TableView
from view.utils import UtilView


class UpdateFeature(Feature):
    BY_ID = 1

    menu = {
        Feature.HEADER: "Please choose the menu id to perform the operation",
        BY_ID: "Update the destination's info by id.",
        Feature.EXIT: "Exit"
    }

    feature = None

    def start(self):
        while True:
            UpdateFeature.show_menu(self=self, menu=UpdateFeature.menu)
            Feature.start(self)

            match self.selected_menu:
                case UpdateFeature.BY_ID:
                    self.__update()
                case Feature.EXIT:
                    break

    def __load_data(self):
        places = self.reader.read_file(DataUtils.SOURCE_PATH)
        return self.reader.as_two_dimension_list(places, include_header=True)

    def __update(self):

        datas = self.__load_data()[1:]

        # Extract IDs from the first column of each row
        ids = [row[0] for row in datas]

        msg_ask_id = "Enter the unique ID of the row you want to update: "
        self.util_view.show_line(size=len(msg_ask_id), deco="=")
        # Ask the user for the ID of the row they want to update
        selected_id = input(msg_ask_id)

        # Ensure the selected ID exists in the data
        if selected_id in ids:
            row_index = ids.index(selected_id)  # Find the index of the row by ID

            # Update columns, skipping the first column (ID)
            for col_index in range(1, len(datas[row_index])):

                self.util_view.show_border(f"Current value for {datas[0][col_index]} - {datas[row_index][col_index]}")
                update = input(
                    f"Enter new data for {datas[0][col_index]} (or press Enter to keep the current value) - ")
                # Only update if a new value is entered
                if update:
                    datas[row_index][col_index] = update

            # Write the updated data back to the file manually
            with open(DataUtils.SOURCE_PATH, mode='w') as f:
                for row in datas:
                    f.write(",".join(row))  # Join each row with commas and add newline
            self.util_view.show_border("Data updated successfully!")

            # print the updated row!!!
            for x in range(1, 12):
                print(f"Value for {datas[0][x]} : {datas[row_index][x]}")

        else:
            self.util_view.show_border("Invalid ID selected.")

    @staticmethod
    def instance(self: FileReader, table_view: TableView, util_view: UtilView, menu_utils: MenuUtils):
        if UpdateFeature.feature is None:
            UpdateFeature.feature = UpdateFeature(reader=self, table_view=table_view, util_view=util_view,
                                                  menu_utils=menu_utils)
        return UpdateFeature.feature
