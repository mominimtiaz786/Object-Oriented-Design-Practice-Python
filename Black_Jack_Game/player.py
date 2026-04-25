from abc import ABC

from .hand import Hand
from .decision_logic import PlayerDecisionLogic, DealerDecisionLogic, RealPlayerDecisionLogic


class Player(ABC):
    def __init__(self, name: str, player_decision_logic: PlayerDecisionLogic):
        self.name = name
        self.hand = Hand()
        self.decision_logic = player_decision_logic

    def placeBet(self, amount: float):
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Bet amount cannot exceed player's balance.")
        self.bet = amount
        self.balance -= amount

    def loseBet(self):
        self.bet = 0

    def payout(self):
        self.balance += self.bet * 2
        self.bet = 0

    def returnBet(self):
        self.balance += self.bet
        self.bet = 0

    def isBusted(self) -> bool:
        return self.hand.isBusted()

    def getHand(self) -> Hand:
        return self.hand

    def getName(self) -> str:
        return self.name

    def getDecisionLogic(self) -> PlayerDecisionLogic:
        return self.decision_logic


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer", DealerDecisionLogic())

    def payout(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name: str, balance: float):
        super().__init__(name, RealPlayerDecisionLogic())
        self.bet = 0
        self.balance = balance

    def getBalance(self) -> float:
        return self.balance

    def getBet(self) -> float:
        return self.bet
