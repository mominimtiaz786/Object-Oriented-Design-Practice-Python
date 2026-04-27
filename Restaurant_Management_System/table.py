from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from .menu_item import MenuItem
from .order_item import OrderItem

if TYPE_CHECKING:
    from .reservation import Reservation


class Table:
    def __init__(self, table_number: str, seating_capacity: int):
        self.table_number = table_number
        self.seating_capacity = seating_capacity
        self.reservations: dict[datetime, "Reservation"] = {}
        self.ordered_items: dict[MenuItem, list[OrderItem]] = defaultdict(list)

    def addOrder(self, menu_item: MenuItem, quantity: int = 1) -> None:
        for _ in range(quantity):
            self.ordered_items[menu_item].append(OrderItem(menu_item))

    def addReservation(self, reservation: "Reservation") -> None:
        self.reservations[reservation.getTime()] = reservation

    def removeOrder(self, item: MenuItem) -> None:
        orders = self.ordered_items.get(item)
        if orders:
            orders.pop()
        else:
            self.ordered_items.pop(item, None)

    def removeReservation(self, reservation: "Reservation") -> None:
        self.reservations.pop(reservation.getTime(), None)

    def isAvailableAt(self, party_time: datetime) -> bool:
        # Each reservation holds the table for exactly one hour; check for any overlap.
        one_hour = timedelta(hours=1)
        for reserved_time in self.reservations:
            if reserved_time < party_time + one_hour and party_time < reserved_time + one_hour:
                return False
        return True

    def calculateBill(self) -> float:
        return sum(item.getPrice() * len(order_items) for item, order_items in self.ordered_items.items())

    def getOrderedItems(self):
        return self.ordered_items.copy()