class Vehicle(object):
    def __init__(self, id, year: int, make, model, qty: int, wideLoad: bool, vehicleType, **kwargs):
        self.id = id
        self.year = year
        self.make = make
        self.model = model
        self.qty = qty
        self.wideLoad = wideLoad
        self.vehicleType = vehicleType

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vehicleType == other.vehicleType and self.qty == other.qty and self.wideLoad == other.wideLoad \
                   and self.make == other.make and self.model == other.model and self.year == other.year
