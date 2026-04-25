from enum import Enum


class Suit(Enum):
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"
    CLUBS = "CLUBS"
    SPADES = "SPADES"


class Rank(Enum):
    ACE = [1, 11]
    TWO = [2]
    THREE = [3]
    FOUR = [4]
    FIVE = [5]
    SIX = [6]
    SEVEN = [7]
    EIGHT = [8]
    NINE = [9]
    TEN = [10]
    JACK = [10]
    QUEEN = [10]
    KING = [10]

    def __init__(self, rank_values):
        super().__init__()
        self.value = rank_values

    def getRankValues(self):
        return self.value


class GamePhase(Enum):
    STARTED = "STARTED"
    BET_PLACED = "BET_PLACED"
    INITIAL_CARD_DRAWN = "INITIAL_CARD_DRAWN"
    DEALING = "DEALING"
    PLAYER_TURN = "PLAYER_TURN"
    DEALER_TURN = "DEALER_TURN"
    ROUND_END = "ROUND_END"


class Action(Enum):
    HIT = "HIT"
    STAND = "STAND"
    BET = "BET"
