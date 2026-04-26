import hashlib
from enum import Enum


class AccountType(Enum):
    SAVING = "SAVING"
    CHECKING = "CHECKING"


class Account:
    def __init__(
            self,
            account_type: AccountType, account_number: str, card_number: str, card_pin: str):
        self.account_type: AccountType = account_type
        self.balance: float = 0
        self.account_number: str = account_number
        self.card_number: str = card_number
        self.card_pin_hash: str = self.__generatePinHash(card_pin)

    def validatePin(self, entered_pin: str) -> bool:
        return self.__generatePinHash(entered_pin) == self.card_pin_hash

    def updateBalanceWithTransaction(self, balance_change: float) -> None:
        self.balance += balance_change

    def getBalance(self) -> float:
        return self.balance

    def __generatePinHash(self, pin: str) -> str:
        return hashlib.sha256(pin.encode()).hexdigest()
