from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    EXTRA_FUEL = 0.9

    def drive(self, distance):
        required_fuel = (self.fuel_consumption + Car.EXTRA_FUEL) * distance
        if self.fuel_quantity - required_fuel >= 0:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_FUEL = 1.6
    HOLE_DECREASE = 0.95

    def drive(self, distance):
        required_fuel = (self.fuel_consumption + Truck.EXTRA_FUEL) * distance
        if self.fuel_quantity - required_fuel >= 0:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * Truck.HOLE_DECREASE)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
