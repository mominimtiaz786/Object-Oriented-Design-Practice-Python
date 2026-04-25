from abc import ABC, abstractmethod

from .account import Account


class LockerEventObserver(ABC):
    @abstractmethod
    def update(self, message: str, account: Account):
        pass
