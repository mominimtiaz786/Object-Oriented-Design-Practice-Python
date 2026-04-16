from .screening_manager import ScreeningManager
from .screening import Screening
from .movie import Movie
from .ticket import Ticket
from .seat import Seat
from .seat_lock_manager import SeatLockManager
from datetime import timedelta

class MovieBookingSystem:
    def __init__(self):
        self.screening_manager = ScreeningManager()
        self.seat_lock_manager = SeatLockManager(timedelta(minutes=5))
        self.movies = []
        self.cinemas = []


    def add_movie(self, movie) -> None:
        self.movies.append(movie)


    def add_cinema(self, cinema) -> None:
        self.cinemas.append(cinema)


    def add_screening(self, screening) -> None:
        self.screening_manager.add_screening(screening)


    def book_ticket(self, screening: Screening, seat: Seat, user_id: str) -> Ticket:
        acquired = self.seat_lock_manager.lock_seat(screening, seat, user_id)
        if not acquired:
            raise Exception("Seat is already locked")

        return Ticket(
            seat=seat,
            screening=screening,
            price=seat.get_pricing_strategy().getPrice()
        )

    
    def get_screenings_by_movie(self, movie: Movie) -> list[Screening]:
        return self.screening_manager.get_screenings_by_movie(movie)


    def get_available_seats(self, screening: Screening) -> list[Seat]:
        return self.screening_manager.get_available_seats(screening)


    def get_ticket_count(screening: Screening) -> int:
        return len(ScreeningManager.get_tickets_by_screenings(screening))