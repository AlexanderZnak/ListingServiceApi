class Location(object):
    def __init__(self, city, zip, state, **kwargs):
        self.city = city
        self.zip = zip
        self.state = state

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.city == other.city and self.zip == other.zip and self.state == other.state
