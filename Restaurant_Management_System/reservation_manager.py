from __future__ import annotations

from datetime import datetime, timedelta

from .layout import Layout
from .reservation import Reservation


class ReservationManager:
    def __init__(self, layout: Layout):
        self.layout = layout
        self.reservations: set[Reservation] = set()

    def createReservation(self, party_name: str, party_size: int, reservation_time: datetime):
        # Normalize to the start of the requested hour so reservation keys are consistent.
        reservation_time = reservation_time.replace(minute=0, second=0, microsecond=0)
        table = self.layout.findAvailableTable(party_size, reservation_time)
        if table is None:
            raise ValueError(f"No table available for {party_size} guests at {reservation_time}")
        reservation = Reservation(party_name, party_size, table, reservation_time)
        table.addReservation(reservation)
        self.reservations.add(reservation)

    def removeReservation(self, party_name: str, party_size: int, reservation_time: datetime):
        reservation_time = reservation_time.replace(minute=0, second=0, microsecond=0)
        to_remove = None
        for reservation in self.reservations:
            if (reservation.getTime() == reservation_time
                    and reservation.getPartyName() == party_name
                    and reservation.getPartySize() == party_size):
                to_remove = reservation
                break
        if to_remove:
            self.reservations.remove(to_remove)
            to_remove.getTable().removeReservation(to_remove)

    def findAvailableTimeSlots(self, start: datetime, end: datetime, party_size: int) -> set[datetime]:
        current = start.replace(minute=0, second=0, microsecond=0)
        available = set()
        while current <= end:
            if self.layout.findAvailableTable(party_size, current):
                available.add(current)
            current += timedelta(hours=1)
        return available
