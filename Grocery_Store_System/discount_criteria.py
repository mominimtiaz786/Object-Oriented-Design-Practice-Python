from abc import ABC, abstractmethod
class DiscountCriteria(ABC):
    @abstractmethod
    def isApplicable(self, item: Item)-> bool:
        pass

class CategoryBasedCriteria(DiscountCriteria):
    def __init__(self, category):
        self.category = category

    def isApplicable(self, item):
        return item.getCategory() == self.category        


class ItemBasedCriteria(DiscountCriteria):
    def __init__(self, item_barcode):
        self.item_barcode = item_barcode
    
    def isApplicable(self, item):
        return item.getBarcode() == self.item_barcode   
