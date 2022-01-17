class Cod:
    def __init__(self, amount: str, paymentMethod, paymentLocation, **kwargs):
        self.amount = amount
        self.paymentMethod = paymentMethod
        self.paymentLocation = paymentLocation

    def __eq__(self, other):
        if isinstance(other, Cod):
            return self.amount == other.amount and self.paymentLocation == other.paymentLocation and self.paymentMethod \
                   == self.paymentMethod
