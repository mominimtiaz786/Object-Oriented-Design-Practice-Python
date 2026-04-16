from datetime import datetime

from .ticket import Ticket
class Order:
    def __init__(self):
        self.booked_tickets: list[Ticket] = []
        self.order_date = datetime.now()

    def add_ticket(self, ticket: Ticket):
        self.booked_tickets.append(ticket)
    
    def calculate_total_price(self) -> float:
        return sum([ticket.calculate_price() for ticket in self.booked_tickets])

    def get_all_tickets(self) -> list[Ticket]:
        return self.booked_tickets