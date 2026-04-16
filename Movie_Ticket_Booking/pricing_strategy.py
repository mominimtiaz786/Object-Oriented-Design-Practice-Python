from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def getPrice(self) -> int:
        pass

class NormalRate(PricingStrategy):
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price


class PremiumRate(PricingStrategy):
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price


class VIPRate(PricingStrategy):
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price