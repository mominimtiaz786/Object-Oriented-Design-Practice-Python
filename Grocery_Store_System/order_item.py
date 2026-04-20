from __future__ import annotations
from .item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .discount_campaign import DiscountCampaign


class OrderItem:
    def __init__(self, item: Item, quantity: int = 1):
        self.__item = item
        self.__quantity = quantity

    def getItem(self):
        return self.__item
    
    def getQuantity(self):
        return self.__quantity
    
    def updateQuantity(self, quantity):
        self.__quantity = quantity

    def calculatePrice(self)-> float:
        return self.__item.getPrice() * self.__quantity
    
    def calculatePriceWithDiscount(self, discount: DiscountCampaign)-> float:
        return self.calculatePrice() - discount.calculateDiscount(self)
