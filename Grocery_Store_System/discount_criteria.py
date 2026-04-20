from .item import Item
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


class CompositeCriteria(DiscountCriteria):
    def __init__(self, criterial_list: list[DiscountCriteria]):
        self.criterial_list = criterial_list

    def isApplicable(self, item):
        for criteria in self.criterial_list:
            if not criteria.isApplicable(item):
                return False
        
        return True

    def addCriteria(self, criteria: DiscountCriteria):
        self.criterial_list.append(criteria)

    def removeCriteria(self, criteria: DiscountCriteria):
        self.criterial_list.remove(criteria)