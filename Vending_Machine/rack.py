from . import (
    Product,
)

class Rack:
    def __init__(self, rack_number, product):
        self.rack_number = rack_number
        self.product = product
        self.__product_count = 0

    @property
    def product_count(self):
        return self.__product_count
    
    def setCount(self, count):
        self.__product_count = count
    

    def getProduct(self) -> Product:
        return self.product
