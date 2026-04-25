from datetime import datetime

from .locker import Locker
from .site import Site
from .shipping_status import ShippingStatus
from .exceptions import MaximumStoragePeriodException
from .locker_manager_change import LockerManagerChange
from .account import Account


class LockerManager:
    def __init__(self, site: Site, locker_manager_change: LockerManagerChange):
        self.site = site
        self.locker_manager_change = locker_manager_change
        self.accounts: dict[str, Account] = {}
        self.locker_access: dict[str, Locker] = {}

    def assignPackage(self, shipping_package, date: datetime) -> Locker:
        locker = self.site.placePackage(shipping_package, date)
        if locker:
            self.locker_access[locker.getAccessCode()] = locker
            self.locker_manager_change.next(
                "Package assigned to locker" + locker.getAccessCode(), shipping_package.getUser()
            )

    def pickupPackage(self, access_code: str) -> Locker:
        locker = self.locker_access.get(access_code)
        if locker and locker.getAccessCode() == access_code:
            try:
                charges = locker.calculateStorageCharges()
                package = locker.getCurrentPackage()
                locker.releaseLock()
                package.getUser().addUsageCharges(charges)
                package.updateShippingStatus(ShippingStatus.RETRIEVED)
                return locker
            except MaximumStoragePeriodException:
                locker.releaseLock()
                return locker

        return None
