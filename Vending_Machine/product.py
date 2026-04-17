class Product:
    def __init__(self, price, unique_code, description=""):
        self.price = price
        self.unique_code = unique_code
        self.description = description

    def getPrice(self):
        return self.price