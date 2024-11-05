from view.utils import UtilView
from utils.header_info_key import Header_Info_Key
from utils.key import Key

class TableView:

    def __init__(self, utils: UtilView):
        self.utils = utils

    def show_header(self, headers: dict):
        org_size = len(headers)
        size = org_size * 3
        message = ""
        for key in headers:
            size += headers[key][Header_Info_Key.SIZE]
        self.utils.show_deco(size= size, deco= "=")
        for key in headers:
            message += f"| {headers[key][Header_Info_Key.TITLE].removesuffix("\n")} "
        message += "|"
        print(message)
        self.utils.show_deco(size= size, deco= "=")
    
    def header_as_map(self, header: list, key: Key, message: str):
        return {
            Header_Info_Key.TITLE : header[key],
            Header_Info_Key.SIZE : len(header[key]),
            Header_Info_Key.TEXT_INDEX: len(message)
        }
    
    """
        {
            ID: {
                title: ID,
                size: 2
            }
        }
    """
    def get_header_info(self, header: list):
        message = ""
        mod_dict = {}
        org_list = Key.default_as_list()
        for key in org_list:
            message += "| "
            mod_dict[key] = self.header_as_map(header, key, message)
            message += f"{header[key].removesuffix("\n")} "
        return mod_dict
    
    def row_with_deco(self, row: dict, header_infos: dict):
        message = ""
        size = 0
        for key in header_infos:
            size += header_infos[key][Header_Info_Key.SIZE]
        message = " " * size
        for key in header_infos:
            index = header_infos[key][Header_Info_Key.TEXT_INDEX]
            head_size = header_infos[key][Header_Info_Key.SIZE]
            cell = str(row[key]).removesuffix("\n")
            cell_size = len(cell)
            if not key == Key.ID and cell_size > head_size:
                cell = cell[0:(head_size-3)] + "..."
            message = message[: index] + cell + message[(len(cell) + index - 3):]
        print(message)
        self.utils.show_deco(size= int(len(message)), step= 0)