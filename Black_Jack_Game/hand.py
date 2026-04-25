from .card import Card


class Hand:
    def __init__(self):
        self.hand_cards: list[Card] = []
        self.possible_values: set[int] = set()

    def addCard(self, card: Card):
        if not card:
            raise ValueError("Card cannot be None")

        self.hand_cards.append(card)

        if not self.possible_values:
            for rank_value in card.getRankValues():
                self.possible_values.add(rank_value)
        else:
            new_possible_values = set()
            for existing_value in self.possible_values:
                for rank_value in card.getRankValues():
                    new_possible_values.add(existing_value + rank_value)
            self.possible_values = new_possible_values

    def calculateValue(self) -> int:
        self.hand_cards.sort(key=lambda card: card.getRankValues()[0], reverse=True)
        total_value = 0
        for card in self.hand_cards:
            rank_values = card.getRankValues()
            if len(rank_values) == 2:  # Ace
                if total_value + rank_values[1] <= 21:
                    total_value += rank_values[1]
                else:
                    total_value += rank_values[0]
            else:
                total_value += rank_values[0]
        return total_value

    def isBusted(self) -> bool:
        if not self.possible_values:
            return False
        return max(self.possible_values) > 21

    def getCards(self) -> list[Card]:
        return self.hand_cards.copy()

    def getPossibleValues(self) -> set[int]:
        return self.possible_values

    def clearHand(self):
        self.hand_cards.clear()
        self.possible_values.clear()
