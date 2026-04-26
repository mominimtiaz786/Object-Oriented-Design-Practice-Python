from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .atm_machine import ATMMachine


class ATMState(ABC):
    @staticmethod
    def renderDefaultAction(atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Invalid action, please try again.")

    def processCardInjection(self, atm: ATMMachine, card_number: str) -> None:
        ATMState.renderDefaultAction(atm)

    def processPinEntry(self, atm: ATMMachine, pin: str) -> None:
        ATMState.renderDefaultAction(atm)

    def processWithdrawRequest(self, atm: ATMMachine) -> None:
        ATMState.renderDefaultAction(atm)

    def processAmountEntry(self, atm: ATMMachine, amount: float) -> None:
        ATMState.renderDefaultAction(atm)

    def processDepositRequest(self, atm: ATMMachine) -> None:
        ATMState.renderDefaultAction(atm)

    def processDepositCollection(self, atm: ATMMachine, amount: float) -> None:
        ATMState.renderDefaultAction(atm)

    def processCardEjection(self, atm: ATMMachine) -> None:
        ATMState.renderDefaultAction(atm)


class IdleState(ATMState):
    def processCardInjection(self, atm: ATMMachine, card_number: str) -> None:
        if atm.getBankInterface().validateCard(card_number):
            atm.getDisplay().showMessage("Please enter your PIN")
            atm.transitionToState(PinEntryState())
        else:
            atm.getDisplay().showMessage("Invalid card. Please try again.")


class PinEntryState(ATMState):
    _pin_attempts: dict[str, int] = {}
    MAX_ATTEMPTS_ALLOWED = 3

    def processPinEntry(self, atm: ATMMachine, pin: str) -> None:
        card_number = atm.getCardProcessor().getCardNumber()
        if atm.getBankInterface().checkPin(pin, card_number):
            PinEntryState._pin_attempts.pop(card_number, None)
            atm.getDisplay().showMessage("Pin Validated. Please select Your Transaction")
            atm.transitionToState(TransactionSelectionState())
        elif PinEntryState._pin_attempts.get(card_number, 0) + 1 >= PinEntryState.MAX_ATTEMPTS_ALLOWED:
            atm.getDisplay().showMessage(
                f"Attempt Number {PinEntryState.MAX_ATTEMPTS_ALLOWED} failed. "
                "Your Card is being retained. Please contact Bank Administration for card retrieval."
            )
            PinEntryState._pin_attempts.pop(card_number, None)
            atm.transitionToState(IdleState())
        else:
            PinEntryState._pin_attempts[card_number] = PinEntryState._pin_attempts.get(card_number, 0) + 1
            atm.getDisplay().showMessage(
                f"Attempt Number {PinEntryState._pin_attempts[card_number]} failed. Please try Again."
            )

    def processCardEjection(self, atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Transaction cancelled, card ejected")
        atm.transitionToState(IdleState())


class TransactionSelectionState(ATMState):
    def processWithdrawRequest(self, atm: ATMMachine) -> None:
        card_number = atm.getCardProcessor().getCardNumber()
        account = atm.getBankInterface().getAccountByCardNumber(card_number)
        atm.getDisplay().showMessage(
            f"Please Enter the Amount to withdraw. Current Balance: {account.getBalance()}"
        )
        atm.transitionToState(WithdrawAmountEntryState())

    def processDepositRequest(self, atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Please deposit the cash in the deposit box")
        atm.transitionToState(DepositCollectionState())

    def processCardEjection(self, atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Transaction cancelled, card ejected")
        atm.transitionToState(IdleState())


class WithdrawAmountEntryState(ATMState):
    def processAmountEntry(self, atm: ATMMachine, amount: float) -> None:
        card_number = atm.getCardProcessor().getCardNumber()
        account = atm.getBankInterface().getAccountByCardNumber(card_number)
        # FIX: withdrawFunds returns None and raises on failure — checking is_success was always False
        try:
            atm.getBankInterface().withdrawFunds(account, amount)
            atm.getCashDispenser().dispenseCash(amount)
            atm.getDisplay().showMessage("Please take your cash.")
        except Exception:
            atm.getDisplay().showMessage("Insufficient funds, please try again.")
        atm.transitionToState(TransactionSelectionState())

    def processCardEjection(self, atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Transaction cancelled, card ejected")
        atm.transitionToState(IdleState())


class DepositCollectionState(ATMState):
    def processDepositCollection(self, atm: ATMMachine, amount: float) -> None:
        card_number = atm.getCardProcessor().getCardNumber()
        account = atm.getBankInterface().getAccountByCardNumber(card_number)
        account.updateBalanceWithTransaction(amount)
        atm.getDisplay().showMessage(
            f"Cash is deposited in the account. Current Balance {account.getBalance()}"
        )
        atm.transitionToState(TransactionSelectionState())

    def processCardEjection(self, atm: ATMMachine) -> None:
        atm.getDisplay().showMessage("Transaction cancelled, card ejected")
        atm.transitionToState(IdleState())
