from .account import Account
from .locker_event_observer import LockerEventObserver


class LockerManagerChange:
    def __init__(self):
        self.observers: list[LockerEventObserver] = []

    def subscribe(self, observer: LockerEventObserver):
        self.observers.append(observer)

    def removeObserver(self, observer: LockerEventObserver):
        self.observers.remove(observer)

    def next(self, message: str, account: Account):
        for observer in self.observers:
            observer.update(message, account)

    def assignPackage(self, pkg):
        locker = self.assignLockerToPackage(pkg)
        if locker:
            self.next("Package assigned to locker", pkg.getUser())

    def assignLockerToPackage(self, pkg):
        return None
