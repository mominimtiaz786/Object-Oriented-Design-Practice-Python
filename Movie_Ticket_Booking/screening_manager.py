from collections import defaultdict

from .screening import Screening
from .movie import Movie
from .ticket import Ticket
from .seat import Seat

class ScreeningManager:
    def __init__(self):
        self.screenings_by_movie: dict[Movie, list[Screening]] = defaultdict(list)
        self.tickets_by_screenings: dict[Screening, list[Ticket]] = defaultdict(list)


    def get_screenings_by_movie(self, movie: Movie) -> list[Screening]:
        return self.screenings_by_movie[movie]


    def get_tickets_by_screenings(self, screening: Screening) -> list[Ticket]:
        return self.tickets_by_screenings[screening]


    def add_ticket(self, ticket: Ticket):
        screening = ticket.get_screening()
        self.tickets_by_screenings[screening].append(ticket)


    def add_screening(self, screening: Screening):
        movie = screening.get_movie()
        self.screenings_by_movie[movie].append(screening)


    def get_available_seats(self, screening: Screening) -> list[Seat]:
        all_seats = screening.get_room().get_layout().getAllSeats()
        booked_tickets = self.get_tickets_by_screenings(screening)

        available_seats = set(all_seats)  

        for ticket in booked_tickets:
            available_seats.remove(ticket.get_seat())

        return list(available_seats)
     
