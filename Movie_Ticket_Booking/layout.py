from .seat import Seat
class Layout:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.seats_by_number: dict[str, Seat] = {}
        self.seats_by_position: dict[int, dict[int, Seat]] = {}

    def add_seat(self, row, col, seat: Seat):
        self.seats_by_number[seat.number] = seat
        self.seats_by_position[row][col] = seat \
                if row in self.seats_by_position \
                else self.seats_by_position[row] = {col:seat}


    def get_seat_by_number(self, seat_number: str):
        return self.seats_by_number.get(seat_number, None)


    def getAllSeats(self) -> list[Seat]:
        return list(self.get_seat_by_number.values())
    
    
    def initialize_layout(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.add_seat(i,j, Seat(f'{i}-{j}'))
