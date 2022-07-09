import dataclasses
import string
import random
from dataclasses import dataclass

@dataclass
class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def compute_tax(self):
        tax_percentage = 0.02 if self.electric else 0.05
        return tax_percentage * self.catalogue_price

    def print(self):
        print(F"Brand: {self.brand}")
        print(F"Payable tax: {self.compute_tax()}")

@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def print(self):
        print(F"ID: {self.id}")
        print(F"License place: {self.license_plate}")
        self.info.print()

class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)

app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
vehicle.print()