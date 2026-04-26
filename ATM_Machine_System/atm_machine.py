from __future__ import annotations

from typing import TYPE_CHECKING

from .bank import BankInterface

if TYPE_CHECKING:
    from .atm_state import ATMState


class ATMMachine:
    def __init__(self, bank: BankInterface, card_processor, keypad, depositbox, cash_dispenser, display):
        # Deferred import to break circular dependency with atm_state
        from .atm_state import IdleState
        self.atm_state: ATMState = IdleState()
        self.bank = bank
        self.card_processor, self.keypad = card_processor, keypad
        self.depositbox, self.cash_dispenser = depositbox, cash_dispenser
        self.display = display

    def insertCard(self, card_number: str) -> None:
        self.atm_state.processCardInjection(self, card_number)

    def enterPin(self, pin: str) -> None:
        self.atm_state.processPinEntry(self, pin)

    def requestWithdraw(self) -> None:
        self.atm_state.processWithdrawRequest(self)

    def requestDeposit(self) -> None:
        self.atm_state.processDepositRequest(self)

    def enterWithdrawAmount(self, amount: float) -> None:
        self.atm_state.processAmountEntry(self, amount)

    def collectDeposit(self, amount: float) -> None:
        self.atm_state.processDepositCollection(self, amount)

    def ejectCard(self) -> None:
        self.atm_state.processCardEjection(self)

    def transitionToState(self, next_state: ATMState) -> None:
        self.atm_state = next_state

    def getDisplay(self):
        return self.display

    def getCardProcessor(self):
        return self.card_processor

    def getCashDispenser(self):
        return self.cash_dispenser

    def getDepositBox(self):
        return self.depositbox

    def getKeypad(self):
        return self.keypad

    def getBankInterface(self) -> BankInterface:
        return self.bank
