from faker import Faker

from models.vehicle import Vehicle


class VehicleFaker:

    @staticmethod
    def generate_vehicle():
        fake = Faker()

        year = 2014
        make= ""
        model = ""
        qty = 1
        wide_load = True
        vehicle_type= ""
        vehicle = Vehicle(id, year, make, model, qty, wide_load, vehicle_type)