from datetime import datetime
import datetime as datetime_main
from collections import defaultdict
from .seat import Seat
from .screening import Screening
import threading


class SeatLock:
    def __init__(self, user_id, expiration_time):
        self.user_id = user_id
        self.expiration_time = expiration_time

    def is_expired(self):
        return datetime.now()>self.expiration_time

    def get_user_id(self):
        return self.user_id


class SeatLockManager:
    def __init__(self, lock_duration: datetime_main.timedelta):
        self.lock_duration = lock_duration
        self.locked_seats: dict[str, SeatLock] = defaultdict(SeatLock)
        self._lock = threading.Lock()

    def lock_seat(self, screening: Screening, seat: Seat, user_id: str):
        lock_key = self.generate_lock_key(screening, seat)
        with self._lock:
            self.cleanup_lock_if_expired(lock_key)
            if lock_key in self.locked_seats:
                return False

            self.locked_seats[lock_key] = SeatLock(
                user_id=user_id,
                expiration_time=datetime.now() + self.lock_duration
            )
            return True


    def is_locked(self, screening, seat) -> bool:
        lock_key = self.generate_lock_key(screening, seat)
        with self._lock:
            self.cleanup_lock_if_expired(lock_key)
            return lock_key in self.locked_seats

    def cleanup_lock_if_expired(self, lock_key: str):
        lock: None|SeatLock = self.locked_seat.get(lock_key)
        
        if lock and lock.is_expired():
            self.locked_seats.pop(lock_key)


    def generate_lock_key(self, screening: Screening, seat: Seat):
        return screening.get_id() + "-" + seat.get_seat_number()