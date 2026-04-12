from abc import ABC, abstractmethod
from datetime import datetime

from Parking_Lot_Py.fare_calculator import FareCalculator
from Parking_Lot_Py.parking_manager import ParkingManager
from Parking_Lot_Py.ticket import Ticket
from Parking_Lot_Py.vehicle import Vehicle


class ParkingLot:
    parking_manager: ParkingManager 
    fare_calculator: FareCalculator 

    def __init__(self, parking_manager: ParkingManager, fare_calculator: FareCalculator):
        self.parking_manager = parking_manager
        self.fare_calculator = fare_calculator

    def enter_vehicle(self, vehicle: Vehicle) -> Ticket:
        spot = self.parking_manager.park_vehicle(vehicle)
        if spot:
            ticket_id = f"{vehicle.get_license_plate()}_{spot.get_spot_id()}"
            return Ticket(ticket_id, vehicle, entry_time=datetime.now(), parking_spot=spot)
        else:
            raise Exception("No available parking spot for this vehicle.")

    def exit_vehicle(self, ticket: Ticket) -> float:
        fare = self.fare_calculator.calculate_fare(ticket)
        self.parking_manager.unpark_vehicle(ticket.vehicle)
        return fare


