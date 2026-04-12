from datetime import datetime

from Parking_Lot_Py.parking_lot import Ticket
from abc import ABC, abstractmethod

from Parking_Lot_Py.vehicle import VehicleSize


class FareStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, ticket: Ticket, input_fare):
        pass

class BaseFareStrategy(FareStrategy):
    SMALL_VEHICLE_FARE = 1.0
    MEDIUM_VEHICLE_FARE: 2.0
    LARGE_VEHICLE_FARE: 3.0
    RATE_PER_HOUR = {
        VehicleSize.SMALL: SMALL_VEHICLE_FARE,
        VehicleSize.MEDIUM: MEDIUM_VEHICLE_FARE,
        VehicleSize.LARGE: LARGE_VEHICLE_FARE
    }

    def calculate_fare(self, ticket: Ticket, input_fare):
        vehicle_size = ticket.vehicle.get_size()
        rate = self.RATE_PER_HOUR.get(vehicle_size, 0)
        return input_fare + rate * ticket.calculate_duration(datetime.now())


class PeekHourFareStrategy(FareStrategy):
    PEEK_HOUR_MULTIPLIER = 1.5

    def calculate_fare(self, ticket: Ticket, input_fare):
        fair = input_fare
        if self.is_peek_hour(datetime.now()):
            fair = input_fare * self.PEEK_HOUR_MULTIPLIER
        return fair

    def is_peek_hour(self, time: datetime) -> bool:
        return 7 <= time.hour <= 10 or 16 <= time.hour <= 19
    
    
class FareCalculator:
    fare_strategies: list[FareStrategy]

    def __init__(self, fare_strategies: list[FareStrategy] = None):
        self.fare_strategies = fare_strategies if fare_strategies is not None else [BaseFareStrategy(), PeekHourFareStrategy()]

    def calculate_fare(self, ticket: Ticket):
        fare = 0
        for strategy in self.fare_strategies:
            fare = strategy.calculate_fare(ticket, fare)
        return fare

