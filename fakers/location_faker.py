
from models.location import Location


class LocationFaker:


    def location_generate(self):
        city = ""
        state = ""
        zip = ""
        location = Location(city, zip, state)

        return vars(location)
