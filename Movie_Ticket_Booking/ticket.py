from .screening import Screening
from .seat import Seat

class Ticket:
    def __init__(self, seat: Seat, screening: Screening, price: int):
        self.seat = seat
        self.screening = screening
        self.price = price

    def get_screening(self):
        return self.screening

    def get_seat(self):
        return self.seat