from .item import Item


class Catalog:
    def __init__(self):
        self.__items = dict[str, Item] = {}

    def addItem(self, item: Item):
        self.__items[item.getBarcode()] = item
    
    def removeItem(self, barcode: str):
        self.__items.pop(barcode, None)

    def getItemFromBarcode(self, barcode):
        return self.__items.get(barcode, None)

    def getAllItems(self):
        return list(self.__items.values()).copy()
