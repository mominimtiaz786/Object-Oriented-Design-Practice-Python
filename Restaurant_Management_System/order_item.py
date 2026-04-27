from .menu_item import MenuItem
from .order_status import OrderStatus


class OrderItem:
    def __init__(self, item: MenuItem):
        self.__item = item
        self.__order_status: OrderStatus = OrderStatus.QUEUED

    def getItem(self) -> MenuItem:
        return self.__item

    def getStatus(self) -> OrderStatus:
        return self.__order_status

    def sendToKitchen(self):
        if self.__order_status == OrderStatus.QUEUED:
            self.__order_status = OrderStatus.SENT_TO_KITCHEN

    def deliverToCustomer(self):
        if self.__order_status == OrderStatus.SENT_TO_KITCHEN:
            self.__order_status = OrderStatus.SERVED

    def cancel(self):
        if self.__order_status in (OrderStatus.QUEUED, OrderStatus.SENT_TO_KITCHEN):
            self.__order_status = OrderStatus.CANCELLED
