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

class FixedDiscountDecorator(DiscountCalculationStrategy):
    def __init__(self, strategy: DiscountCalculationStrategy, fixed_amount: float):
        self.strategy = strategy
        self.fixed_amount = fixed_amount

    def calculateDiscountedPrice(self, original_price: float):
        return self.strategy.calculateDiscountedPrice(original_price).subtract(self.fixed_amount);

class PercentageDiscountDecorator(DiscountCalculationStrategy):
    def __init__(self, strategy: DiscountCalculationStrategy, additional_percentage: float):
        self.strategy = strategy
        self.additional_percentage = additional_percentage
    
    def calculateDiscountedPrice(self, original_price: float):
        base_discounted_price = self.strategy.calculateDiscountedPrice(original_price)
        return base_discounted_price * ( 1 - self.additional_percentage/100)
