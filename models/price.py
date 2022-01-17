from models.cod import Cod


class Price:
    def __init__(self, cod, total: str, **kwargs):
        self.cod = Cod(**cod)
        self.total = total

    def __eq__(self, other):
        if isinstance(other, Price):
            return self.cod == other.cod and self.total == other.total
