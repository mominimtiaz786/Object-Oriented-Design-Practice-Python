from .auto_increment_id import AutoIncrementId
from .order_item import OrderItem
from .discount_campaign import DiscountCampaign


class Order(AutoIncrementId):
    def __init__(self):
        super().__init__()
        self.__order_items: dict[str, OrderItem] = {}
        self.__applied_discounts: dict[OrderItem, DiscountCampaign] = {}
        self.__payment_amount: float = 0

    def getOrderId(self):
        return self.getId()
    
    def getAppliedDiscounts(self):
        return self.__applied_discounts.copy()
    
    def getOrderItems(self)-> dict[str, OrderItem]:
        return self.__order_items.copy()
    
    def getOrderItemByBarcode(self, barcode):
        return self.__order_items.get(barcode)
    
    def addItem(self, item, quantity):
        barcode = item.getBarcode()
        stored_item = self.__order_items.get(barcode)
        stored_item_quantity = stored_item.getQuantity()
        
        if stored_item:
            stored_item.updateQuantity(stored_item_quantity + quantity)
        else:
            self.__order_items[barcode] = OrderItem(item, quantity)
        
    def updateQuantity(self, order_item:OrderItem, quantity):
        order_item.updateQuantity(quantity)

    def applyDiscount(self, order_item: OrderItem, discount: DiscountCampaign):
        self.__applied_discounts[order_item] = discount

    def calculateTotal(self):
        total = 0
        for order_item in self.__order_items.values():
            discount = self.__applied_discounts.get(order_item, None)
            total+=(order_item.calculatePriceWithDiscount(discount) if discount else order_item.calculatePrice())

        return total

    def calculateChange(self):
        return self.__payment_amount - self.calculateTotal()
    
    def processPayment(self, amount):
        self.__payment_amount = amount

    def getPaymentAmount(self):
        return self.__payment_amount
    