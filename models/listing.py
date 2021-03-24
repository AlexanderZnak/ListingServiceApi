from models.location import Location
from models.price import Price
from models.vehicle import Vehicle


class Listing:
    def __init__(self, origin, destination, partnerReferenceId, desiredDeliveryDate, trailerType,
                 vehicles, hasInOpVehicle: bool, availableDate, price, **kwargs):
        self.origin = Location(**origin)
        self.destination = Location(**destination)
        self.partnerReferenceId = partnerReferenceId
        self.desiredDeliveryDate = desiredDeliveryDate
        self.trailerType = trailerType
        self.vehicles = [Vehicle(**x) for x in vehicles]
        self.hasInOpVehicle = hasInOpVehicle
        self.availableDate = availableDate
        self.price = Price(**price)

    def __eq__(self, other):
        if isinstance(other, Listing):
            return self.origin == other.origin and self.destination == other.destination and self.partnerReferenceId \
                   == other.partnerReferenceId and self.desiredDeliveryDate == other.desiredDeliveryDate and self. \
                       trailerType == other.trailerType and self.vehicles == other.vehicles and self.hasInOpVehicle == \
                   other.hasInOpVehicle and self.availableDate == other.availableDate and self.price == other.price
