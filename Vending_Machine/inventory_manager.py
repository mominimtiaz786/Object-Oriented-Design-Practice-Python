from . import (
    Product,
    Rack,
)

class InventoryManager:
    def __init__(self):
        self.product_to_rack: dict[Product, Rack] = {}
        self.id_to_rack: dict[str, Rack] = {}


    def getProductInRack(self, rack_code)-> Product:
        if rack_code in self.id_to_rack:
            return self.id_to_rack[rack_code].getProduct()
        else:
            raise Exception("No Rack found with this code")
        

    def dispenseProductFromRack(self, rack: Rack):
        if rack.product_count < 1:
            raise Exception("No Item in the rack.")
        rack.setCount(rack.product_count-1)
            


    def updateRack(self, racks: dict[str, Rack]): 
        self.id_to_rack = racks


    def getRack(self, rack_id)-> Rack:
        if rack_id in self.id_to_rack:
            return self.id_to_rack[rack_id]
        else:
            raise Exception("No Rack found with this code")

        
