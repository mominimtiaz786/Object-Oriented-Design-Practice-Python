from .discount_campaign import DiscountCampaign
from .order import Order
from .receipt import Receipt
from .item import Item
from .order_item import OrderItem


class Checkout:
    def __init__(self, active_discounts: list[DiscountCampaign]):
        self.__current_order = Order()
        self.__active_discounts: list[DiscountCampaign] = active_discounts
        self.__transaction_history: dict[str, Receipt] = {}

    def startNewOrder(self):
        self.__current_order = Order()
    
    def addItemToOrder(self, item: Item, quantity: int):
        barcode = item.getBarcode()
        self.__current_order.addItem(item, quantity)
        order_item = self.__current_order.getOrderItemByBarcode(barcode)
        best_discount = self.__find_best_discount_for_order_item(order_item)

        if best_discount:
            self.__current_order.applyDiscount(best_discount)

    def __find_best_discount_for_order_item(self, order_item: OrderItem) -> DiscountCampaign:
        if not self.__active_discounts:
            return None
        return min(self.__active_discounts, key=order_item.calculatePriceWithDiscount)


    def getOrderTotal(self):
        return self.__current_order.calculateTotal()
    
    def processPayment(self, amount):
        self.__current_order.setPayment(amount);
        return self.__current_order.calculateChange();

    def getReceipt(self):
        receipt = self.generateReceipt()
        self.__transaction_history[receipt.getReceiptId()] = receipt

        return receipt
    
    def generateReceipt(self):
        if self.__current_order.getPaymentAmount() < self.__current_order.calculateTotal():
            raise Exception("Payment is yet to be processed")
        
        return Receipt(self.__current_order)

    def getTransactionHistory(self):
        return list(self.__transaction_history.values()).copy()

