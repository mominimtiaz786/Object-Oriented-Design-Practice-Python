from .enums import Suit, Rank


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def getRankValues(self) -> list[int]:
        return self.rank.getRankValues()

    def getSuit(self) -> Suit:
        return self.suit
