from abc import ABC, abstractmethod
from .vehicle import Vehicle, VehicleSize

class ParkingSpot(ABC):
    def __init__(self, size: VehicleSize):
        self.vehicle = None
        self.spot_id = None
        self.size = size

    def is_available(self):
        return self.vehicle is None

    def get_size(self) -> VehicleSize:
        return self.size

    def get_spot_id(self) -> str:
        return self.spot_id

    def occupy_spot(self, vehicle: Vehicle):
        if self.is_available():
            self.vehicle = vehicle

    def vacate_spot(self):
        self.vehicle = None


class SmallSpot(ParkingSpot):
    def __init__(self):
        super().__init__(VehicleSize.SMALL)


class MediumSpot(ParkingSpot):
    def __init__(self):
        super().__init__(VehicleSize.MEDIUM)


class LargeSpot(ParkingSpot):
    def __init__(self):
        super().__init__(VehicleSize.LARGE)
    
