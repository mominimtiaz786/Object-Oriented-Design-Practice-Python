from abc import ABC, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Vehicle(ABC):
    license_plate : str
    size: VehicleSize

    def __init__(self, license_plate):
        self.license_plate = license_plate
        
    def get_size(self) -> VehicleSize:
        return self.size

    def get_license_plate(self):
        return self.license_plate
    

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.size = VehicleSize.MEDIUM

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.size = VehicleSize.SMALL

class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.size = VehicleSize.LARGE

