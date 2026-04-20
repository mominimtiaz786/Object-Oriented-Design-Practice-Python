from abc import ABC, abstractmethod
class DiscountCalculationStrategy(ABC):
    def calculateDiscountedPrice(self, original_price: float):
        pass

class AmountBasedStrategy(DiscountCalculationStrategy):
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount

    def calculateDiscountedPrice(self, original_price: float):
        return original_price - self.discount_amount


class PercentageBasedStrategy(DiscountCalculationStrategy):
    def __init__(self, discount_percentage: float):
        self.discount_percentage = discount_percentage

    def calculateDiscountedPrice(self, original_price: float):
        return original_price - original_price*self.discount_percentage/100.0
