class Key:
    ID = "ID"
    DESTINATION = "Destination"
    REGION = "Region"
    COUNTRY = "Country"
    CATEGORY = "Category"
    ANNUAL_TOURIST = "Approximate Annual Tourists"
    CURRENCY = "Currency"
    FAM_FOOD = "Famous Foods"
    BEST_TIME = "Best Time to Visit"
    COST_OF_LIVING = "Cost of Living"
    SAFETY = "Safety"
    DESC = "Description"

    @staticmethod
    def default_as_list():
        return [
            Key.ID, 
            Key.DESTINATION, 
            Key.REGION, 
            Key.COUNTRY,
            Key.CATEGORY,
            Key.ANNUAL_TOURIST,
            Key.CURRENCY,
            Key.FAM_FOOD,
            Key.BEST_TIME,
            Key.COST_OF_LIVING,
            Key.SAFETY,
            Key.DESC
        ]