from abc import ABC, abstractmethod
from enum import Enum

from .account import Account


class TransactionType(Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"


class Transaction(ABC):
    def __init__(self, transaction_type: TransactionType):
        self.transaction_type = transaction_type

    def getTransactionType(self) -> TransactionType:
        return self.transaction_type

    @abstractmethod
    def validateTransaction(self) -> bool:
        pass

    @abstractmethod
    def executeTransaction(self) -> None:
        pass


class WithdrawTransaction(Transaction):
    def __init__(self, account: Account, amount: float):
        super().__init__(TransactionType.WITHDRAW)
        self.account = account
        self.amount = amount
        if not self.validateTransaction():
            raise Exception("Cannot complete withdrawal: Insufficient funds in account")

    def validateTransaction(self) -> bool:
        assert self.account
        return self.account.getBalance() - self.amount >= 0

    def executeTransaction(self) -> None:
        self.account.updateBalanceWithTransaction(-1 * self.amount)


class DepositTransaction(Transaction):
    def __init__(self, account: Account, amount: float):
        super().__init__(TransactionType.DEPOSIT)
        self.account = account
        self.amount = amount

    def validateTransaction(self) -> bool:
        return True

    def executeTransaction(self) -> None:
        self.account.updateBalanceWithTransaction(self.amount)
