from abc import ABC, abstractmethod

from .account import Account, AccountType


class BankInterface(ABC):
    @abstractmethod
    def addAccount(self, account_type: AccountType, card_pin: str, account_number: str, card_number: str) -> None:
        pass

    @abstractmethod
    def validateCard(self, card_number: str) -> bool:
        pass

    @abstractmethod
    def checkPin(self, pin: str, card_number: str) -> bool:
        pass

    @abstractmethod
    def getAccountByCardNumber(self, card_number: str) -> Account:
        pass

    @abstractmethod
    def getAccountByAccountNumber(self, account_number: str) -> Account:
        pass

    @abstractmethod
    def withdrawFunds(self, account: Account, amount: float) -> None:
        pass


class Bank(BankInterface):
    def __init__(self):
        self.accounts_by_number: dict[str, Account] = {}
        self.accounts_by_card_number: dict[str, Account] = {}

    def addAccount(self, account_type: AccountType, card_pin: str, account_number: str, card_number: str) -> None:
        account = Account(account_type, account_number, card_number, card_pin)
        self.accounts_by_number[account_number] = account
        self.accounts_by_card_number[card_number] = account

    def validateCard(self, card_number: str) -> bool:
        return self.accounts_by_card_number.get(card_number) is not None

    def checkPin(self, pin: str, card_number: str) -> bool:
        if self.validateCard(card_number):
            return self.accounts_by_card_number[card_number].validatePin(pin)
        return False

    def getAccountByCardNumber(self, card_number: str) -> Account:
        return self.accounts_by_card_number.get(card_number)

    def getAccountByAccountNumber(self, account_number: str) -> Account:
        return self.accounts_by_number.get(account_number)

    def withdrawFunds(self, account: Account, amount: float) -> None:
        if account.getBalance() - amount < 0:
            raise Exception("Insufficient Balance")
        account.updateBalanceWithTransaction(-1 * amount)
