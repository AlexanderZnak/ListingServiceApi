import json

from entities.factories.encoders.listing_encoder import ListingEncoder
from fakers.listing_faker import ListingFaker
from models.listing import Listing


class ListingFactory:
    @staticmethod
    def generate_fake_listing():
        with open("resources/listing.json") as listing_file:
            listing = Listing(**json.load(listing_file))
        return ListingFaker().generate_listing()

    @staticmethod
    def listing_to_json(listing):
        return json.dumps(vars(listing), cls=ListingEncoder)
