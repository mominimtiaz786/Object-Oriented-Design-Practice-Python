from datetime import datetime

from Parking_Lot_Py.parking_spot import ParkingSpot
from Parking_Lot_Py.vehicle import Vehicle


class Ticket:
    def __init__(self, ticket_id, vehicle: Vehicle, entry_time: datetime, parking_spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.parking_spot = parking_spot
        self.exit_time = None
    

    def calculate_duration(self, exit_time: datetime) -> float:
        self.exit_time = exit_time
        duration = self.exit_time - self.entry_time
        return duration.total_seconds() / 3600

