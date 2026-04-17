from . import (
    Product,
    Rack,
)

class Transaction:
    def __init__(self):
        self.rack: Rack = None
        self.product: Product = None

        self.total_amount: float = 0
    
    def setTotalAmount(self, amount: float):
        self.total_amount = amount


    def getTotalAmount(self):
        return self.total_amount 


    def getProduct(self):
        return self.product


    def getRack(self):
        return self.rack 


    def setProduct(self, product: Product):
        self.product = product
        self.total_amount+=product.price


    def setRack(self, rack: Rack):
        self.rack = rack

