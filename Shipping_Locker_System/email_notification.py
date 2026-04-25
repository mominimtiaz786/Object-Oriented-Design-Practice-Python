from .account import Account
from .locker_event_observer import LockerEventObserver
from .notification import NotificationInterface


class EmailNotification(LockerEventObserver, NotificationInterface):
    def update(self, message: str, account: Account):
        self.sendNotification(message, account)

    def sendNotification(self, message: str, user: Account):
        pass
