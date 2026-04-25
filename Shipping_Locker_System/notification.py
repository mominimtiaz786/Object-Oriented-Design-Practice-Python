from abc import ABC, abstractmethod

from .account import Account


class NotificationInterface(ABC):
    @abstractmethod
    def sendNotification(self, message: str, user: Account):
        pass
