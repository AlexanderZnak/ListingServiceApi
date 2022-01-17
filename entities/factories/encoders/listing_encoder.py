import json

from models.cod import Cod
from models.location import Location
from models.price import Price
from models.vehicle import Vehicle


class ListingEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Location):
            return obj.__dict__
        elif isinstance(obj, Cod):
            return obj.__dict__
        elif isinstance(obj, Price):
            return obj.__dict__
        elif isinstance(obj, Vehicle):
            return obj.__dict__
        return super(ListingEncoder, self).default(obj)
