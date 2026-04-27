from abc import ABC, abstractmethod

from .order_item import OrderItem

class OrderCommand(ABC):
    @abstractmethod
    def execute(self): pass

class SendToKitchenCommand(OrderCommand):
    def __init__(self, order_item: OrderItem):
        self.order_item = order_item

    def execute(self):
        self.order_item.sendToKitchen()

class DeliverCommand(OrderCommand):
    def __init__(self, order_item: OrderItem):
        self.order_item = order_item

    def execute(self):
        self.order_item.deliverToCustomer()

class CancelCommand(OrderCommand):
    def __init__(self, order_item: OrderItem):
        self.order_item = order_item

    def execute(self):
        self.order_item.cancel()

