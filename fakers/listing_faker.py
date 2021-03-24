import json

from models.cod import Cod
from models.listing import Listing
from models.location import Location
from models.price import Price
from models.vehicle import Vehicle


class ListingFaker:
    @staticmethod
    def generate_listing():
        origin = vars(Location("Townsend", "54175", "WI"))
        destination = vars(Location("Beverly Hills", "90210", "CA"))
        partner_reference_id = "multi-car"
        trailer_type = "OPEN"
        vehicles = [vars(Vehicle("5", 2008, "nissan", "altima", 1, False, "CAR")),
                    vars(Vehicle("6", 2014, "toyota", "camry", 1, True, "CAR"))]
        has_in_op_vehicle = False
        available_date = "2021-12-31"
        desired_delivery_date = "2021-12-31"
        cod = vars(Cod("1600", "CHECK", "DELIVERY"))
        bla = vars(Price(cod, "1600"))
        price = {'cod': cod, 'total': '1600'}
        price_two = json.loads(json.dumps(Price(cod, "1600"), default=lambda o: o.__dict__))

        return Listing(origin, destination, partner_reference_id, desired_delivery_date, trailer_type, vehicles,
                       has_in_op_vehicle, available_date, price)
