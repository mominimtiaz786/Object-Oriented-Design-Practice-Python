class Inventory:
    def __init__(self):
        self.__inventory: dict[str, int] = {}
    
    def addStock(self, barcode, count):
        self.__inventory[barcode] = self.__inventory.get(barcode, 0) + count

    def removeStock(self, barcode, count):
        if self.__inventory.get(barcode, 0) < count:
            raise Exception("Not enough quantity in the stock.")
        
        self.__inventory[barcode] = self.__inventory.get(barcode, 0) - count
    
    def getCurrentStock(self, barcode):
        return self.__inventory.get(barcode, 0)
