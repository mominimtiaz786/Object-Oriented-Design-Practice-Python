class Item:
    def __init__(self, barcode, category, price, name):
        self.__barcode = barcode
        self.__category = category
        self.__price = price
        self.__name = name

    def getBarcode(self):
        return self.__barcode
    
    def getCategory(self):
        return self.__category
    
    def getPrice(self):
        return self.__price
    
    def getName(self):
        return self.__name