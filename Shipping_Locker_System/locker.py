from __future__ import annotations
from datetime import datetime

from .locker_size import LockerSize
from .exceptions import MaximumStoragePeriodException


class Locker:
    def __init__(self, locker_size: LockerSize):
        self.size: LockerSize = locker_size
        self.current_package = None
        self.access_code: str = None
        self.assignment_date: datetime = None

    def assignPackage(self, shipping_package, date: datetime):
        self.current_package = shipping_package
        self.assignment_date = date
        self.access_code = self.__generateAccessCode()

    def releaseLock(self):
        self.current_package = None
        self.assignment_date = None
        self.access_code = None

    def getAccessCode(self):
        return self.access_code

    def getCurrentPackage(self):
        return self.current_package

    def calculateStorageCharges(self) -> float:
        if not self.current_package or not self.assignment_date:
            return 0

        account_locker_policy = self.current_package.getUser().getLockerPolicy()
        total_days_used = (datetime.now() - self.assignment_date).days

        if total_days_used < account_locker_policy.getFreeDays():
            return 0

        elif total_days_used < account_locker_policy.getMaximumDays():
            chargeable_days = total_days_used - account_locker_policy.getFreeDays()
            return chargeable_days * self.size.get_daily_charge()

        else:
            raise MaximumStoragePeriodException(
                f"Package has exceeded maximum allowed storage period of "
                f"{account_locker_policy.getMaximumDays()} days"
            )

    def isAvailable(self):
        return self.current_package is None

    def checkAccessCode(self, code: str):
        return code == self.access_code

    def __generateAccessCode(self):
        pass
