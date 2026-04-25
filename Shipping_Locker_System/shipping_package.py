from __future__ import annotations
from abc import ABC, abstractmethod

from .locker_size import LockerSize
from .shipping_status import ShippingStatus
from .account import Account


class ShippingPackage(ABC):
    def __init__(self, order_id, height, width, depth, account: Account, status=ShippingStatus.CREATED):
        self.height, self.width, self.depth = height, width, depth
        self.status = status
        self.account = account
        self.order_id = order_id

    def getOrderId(self) -> str:
        return self.order_id

    def getUser(self) -> Account:
        return self.account

    def getHeight(self) -> float:
        return self.height

    def getWidth(self) -> float:
        return self.width

    def getDepth(self) -> float:
        return self.depth

    def getStatus(self) -> ShippingStatus:
        return self.status

    def updateShippingStatus(self, shipping_status: ShippingStatus) -> None:
        self.status = shipping_status

    def getLockerSize(self) -> LockerSize:
        for size in LockerSize:
            if (size.width >= self.width and
                    size.height >= self.height and
                    size.depth >= self.depth):
                return size

        raise Exception("No locker size available for the package")

    def get_dimensions(self):
        return self.width, self.height, self.depth


class BasicShippingPackage(ShippingPackage):
    def __init__(self, height, width, depth, status=ShippingStatus.CREATED):
        super().__init__(height, width, depth, status)
