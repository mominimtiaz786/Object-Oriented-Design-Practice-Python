"""
“Imagine you’re at a grocery store, filling your cart with fresh produce, snacks, and household essentials. At the checkout, the cashier scans each item, and the system instantly tracks the order, applies any discounts, and displays the final total. Behind the scenes, the system is seamlessly managing the item catalog, updating inventory as stock arrives or sells, and ensuring every transaction is smooth and accurate. Now, let’s design a grocery store system that does all this.”
"""


"""
Requirements

This question has multiple requirements, so grouping similar ones makes it easier to manage and track. The requirements can be broken down into four groups.

Catalog management

Admins can add, update, and remove items from the catalog.
The catalog tracks item details, including name, category, price, and barcode.
Inventory management

Shipment handlers can update inventory when shipments arrive.
The system should automatically decrease inventory when items are sold.
Checkout process

Cashiers can scan barcodes or manually enter item codes to build an order.
Cashiers can view details of the active order, including items, discounts, and the subtotal.
The system calculates and applies relevant discounts automatically.
Cashiers can finalize an order, calculate the total, handle payments, and calculate change.
A detailed receipt is generated.
Discount campaigns

Admins can define discount campaigns for specific items or categories.
If multiple discounts apply to an item, the system selects the highest discount.
Below are the non-functional requirements:

The system should provide clear, user-friendly error messages (e.g., for invalid barcodes or insufficient inventory) to the cashier.
The system’s components (catalog, inventory, checkout, discounts) must be modular to allow updates or replacements of individual modules without affecting the entire system.
"""


from .catalog import Catalog
from .inventory import Inventory
from .discount_campaign import DiscountCampaign
from .item import Item
from .checkout_system import Checkout


class GroceryStoreSystem:
    def __init__(self):
        self.__catalog = Catalog()
        self.__inventory = Inventory()
        self.__active_discounts: list[DiscountCampaign] = []
        self.__checkout = Checkout(self.__active_discounts)

    def addOrUpdateItem(self, item: Item):
        self.__catalog.addItem(item)

    def updateInventory(self, barcode, quanity):
        existing_quantity = self.__inventory.getCurrentStock(barcode)

        if existing_quantity > quanity:
            self.__inventory.removeStock(barcode, existing_quantity - quanity)
        else:
            self.__inventory.addStock(barcode, quanity - existing_quantity)


    def removeItem(self, barcode):
        self.__catalog.removeItem(barcode)

    def getItemByBarcode(self, barcode):
        return self.__catalog.getItemFromBarcode()

    def addDisountCampaign(self, discount: DiscountCampaign):
        self.__active_discounts.append(discount)