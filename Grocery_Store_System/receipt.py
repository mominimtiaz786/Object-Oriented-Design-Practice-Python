from datetime import datetime
from .auto_increment_id import AutoIncrementId
from .order import Order


class Receipt(AutoIncrementId):
    def __init__(self, order: Order):
        super().__init__()
        self.__order: Order = order
        self.__issue_date: datetime = datetime.now()

    def getReceiptId(self):
        return self.getId()

    def printReceipt(self):
        print(f"RECEIPT ID: {self._id}")
        print(f"RECEIPT DATE: {self.__issue_date}")
        
        print("\nORDER DETAILS:")

        print("Sr Num \t Item Name \t Quantity \t Unit Price \t Amount \t Discount Applied \t Sub Total")
        
        for i, order_item in enumerate(self.__order.getOrderItems().values()):
            applied_discount = self.__order.getAppliedDiscounts()[order_item]
            price = order_item.calculatePrice()
            discounted_price = order_item.calculatePriceWithDiscount(applied_discount) \
                    if applied_discount else order_item.calculatePrice()

            print(f"{i+1} \
                  \t {order_item.getItem().getName()} \
                  \t {order_item.getQuantity()} \
                  \t {order_item.getItem().getPrice()} \
                  \t {price} \
                  \t {price - discounted_price} \
                  \t {discounted_price}")

        print(f"ORDER TOTAL: {self.__order.calculateTotal()}")
