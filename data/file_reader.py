from utils.key import Key
from utils.cost_of_living import CostOfLiving

class FileReader:

    def read_file(self, name: str) -> list:
        mod_list = []
        file = None
        try:
            file = open(name)
            data = file.readlines()
        finally:
            file.close()
        for row in data:
            mod_list.append(row.split(","))
        return mod_list

    def filter(self, data: list, level: CostOfLiving) -> list:
        mod_list = []
        for row in data:
            if row[Key.COST_OF_LIVING] == level:
                mod_list.append(row)
        return mod_list

    def filterAnnuallyTourist(self, data : list) :
        mod_list = []
        sortedData = sorted(data, key=lambda x : x[Key.ANNUAL_TOURIST],reverse=True)
        for index in range(11):
            mod_list.append(sortedData[index])
        return mod_list
    
    def filterSafety(self, data: list, safety: str) -> list:
        mod_list = []
        for row in data:
            if row[Key.SAFETY] == safety:
                mod_list.append(row)

        result_list = []

        for index in range(11):
            result_list.append(mod_list[index])

        return result_list
    
    
    def as_map(self, row: list) -> dict:
        return {
                Key.ID: row[0], 
                Key.DESTINATION: row[1], 
                Key.REGION: row[2], 
                Key.COUNTRY: row[3],
                Key.CATEGORY: row[4],
                Key.ANNUAL_TOURIST: row[5],
                Key.CURRENCY: row[6],
                Key.FAM_FOOD: row[7],
                Key.BEST_TIME: row[8],
                Key.COST_OF_LIVING: row[9],
                Key.SAFETY: row[10],
                Key.DESC: row[11]
        }
    
    def as_two_dimension_list(self, places: list, include_header: bool = False) -> list:
        mod_list = places[1:]
        if include_header:
            mod_list = places[0:]
        result = []
        for row in mod_list:
            result.append(row)
        return result
    
    def transform_data(self, data: list):
        modified_list = []
        for row in data:
            modified_list.append(self.as_map(row))
        return modified_list
    