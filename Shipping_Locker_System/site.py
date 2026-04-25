from __future__ import annotations
from datetime import datetime

from .locker_size import LockerSize
from .locker import Locker
from .shipping_status import ShippingStatus


class Site:
    def __init__(self):
        self.site_lockers: dict[LockerSize, list[Locker]]

    def findAvailableLocker(self, locker_size: LockerSize):
        for locker in self.site_lockers.get(locker_size):
            if locker.isAvailable():
                return locker

        return None

    def placePackage(self, package, date: datetime) -> Locker:
        locker_size = package.getLockerSize()
        locker = self.findAvailableLocker(locker_size)
        if locker:
            locker.assignPackage(package, date)
            package.updateShippingStatus(ShippingStatus.IN_LOCKER)
            return locker
        else:
            raise Exception("No Locker Available with this size.")
