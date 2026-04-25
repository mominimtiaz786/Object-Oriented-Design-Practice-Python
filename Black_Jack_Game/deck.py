import random

from .enums import Suit, Rank
from .card import Card


class Deck:
    def __init__(self):
        self.cards: list[Card] = self.createDeck()
        self.next_card_index = 0

    def createDeck(self) -> list[Card]:
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
        self.next_card_index = 0

    def drawCard(self) -> Card:
        if self.isEmpty():
            raise Exception("Deck is empty. Cannot draw more cards.")
        card = self.cards[self.next_card_index]
        self.next_card_index += 1
        return card

    def getRemainingCardsCount(self) -> int:
        return len(self.cards) - self.next_card_index

    def isEmpty(self) -> bool:
        return self.getRemainingCardsCount() == 0

    def resetDeck(self):
        self.next_card_index = 0
        self.shuffle()
