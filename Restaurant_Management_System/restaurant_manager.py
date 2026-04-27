from __future__ import annotations

from datetime import datetime

from .layout import Layout
from .menu import Menu
from .menu_item import MenuItem
from .order_command import CancelCommand, DeliverCommand, SendToKitchenCommand
from .order_manager import OrderManager
from .reservation_manager import ReservationManager
from .table import Table


class RestaurantManager:
    def __init__(self, name: str):
        self.name = name
        self.menu = Menu()
        self.layout = Layout()
        self.reservation_manager = ReservationManager(self.layout)
        self.order_manager = OrderManager()

    def findAvailableTimeSlots(self, start: datetime, end: datetime, party_size: int) -> set[datetime]:
        return self.reservation_manager.findAvailableTimeSlots(start, end, party_size)

    def createScheduledReservation(self, party_name: str, party_size: int, reservation_time: datetime):
        self.reservation_manager.createReservation(party_name, party_size, reservation_time)

    def createWalkinReservation(self, party_name: str, party_size: int):
        now = datetime.now()
        slot = now.replace(minute=0, second=0, microsecond=0)
        self.reservation_manager.createReservation(party_name, party_size, slot)

    def orderItem(self, table: Table, item: MenuItem):
        table.addOrder(item)
        self.__executeRelevantCommand(table, item, SendToKitchenCommand)

    def cancelItem(self, table: Table, item: MenuItem):
        self.__executeRelevantCommand(table, item, CancelCommand)
        table.removeOrder(item)

    def deliverItem(self, table: Table, item: MenuItem):
        self.__executeRelevantCommand(table, item, DeliverCommand)

    def calculateTableBill(self, table: Table) -> float:
        return table.calculateBill()

    def __executeRelevantCommand(self, table: Table, item: MenuItem, cls):
        ordered_items = table.getOrderedItems().get(item)
        if ordered_items:
            command = cls(ordered_items[-1])
            self.order_manager.addCommand(command)
            self.order_manager.executeCommands()
