from .category import Category


class MenuItem:
    def __init__(self, name: str, description: str, price: float, category: Category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def getPrice(self) -> float:
        return self.price

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getCategory(self) -> Category:
        return self.category
