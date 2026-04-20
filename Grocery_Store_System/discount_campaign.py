from .auto_increment_id import AutoIncrementId
from .discount_calculation_strategy import DiscountCalculationStrategy
from .discount_criteria import DiscountCriteria
from .item import Item
from .order_item import OrderItem


class DiscountCampaign(AutoIncrementId):
    def __init__(
            self,
            discount_strategy: DiscountCalculationStrategy,
            discount_criteria: DiscountCriteria,
            name: str
        ):
        super().__init__()
        self.__name = name
        self.__discount_strategy: DiscountCalculationStrategy = discount_strategy
        self.__discount_criteria: DiscountCriteria = discount_criteria

    def getCampaignId(self):
        return self.getId()
    
    def isApplicable(self, item: Item):
        return self.__discount_criteria.isApplicable(item)
    
    def calculateDiscount(self, order_item: OrderItem)-> float:
        return self.__discount_strategy.calculateDiscountedPrice(
            order_item.calculatePrice()
        )