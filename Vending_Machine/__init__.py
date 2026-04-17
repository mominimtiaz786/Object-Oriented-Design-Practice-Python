"""
Imagine you’re at a vending machine, craving a snack. You insert some cash, select your favorite item, and within seconds, it drops into the tray. The machine also gives you the right change if needed. Behind the scenes, the system is working smoothly to track inventory, handle payments, and make sure everything runs efficiently. Now, let’s design a vending machine that does all this.



questions
multiple items?
change management | for example the remaning change for the customers is 5 and vending has a minimum note of 10

Requirements
Here are the functional requirements based on the conversation:

Product selection: Users should be able to select from a set of products. Each product has a unique product code, description, and price tag. While description is not talked about, it is a common-sense attribute to make the product model more realistic.
Inventory management: Products are stored in specific racks within the vending machine. The system keeps track of the inventory level for each product in its respective rack.
Payment processing: The system only accepts cash payments and can calculate change when needed.
Below are the non-functional requirements:

The user interface must be intuitive, allowing users to complete a purchase (insert money, select product, receive product, and change) with minimal instructions, and error messages should be clear and concise to guide users effectively.
The system must protect against unauthorized access to the vending machine, ensuring only admins can add, remove, or update products, and securely handle cash transactions to prevent tampering or fraud.
"""

from .product import Product
from .rack import Rack
from .inventory_manager import InventoryManager
from .payment_processor import PaymentProcessor
from .transaction import Transaction
from .vending_machine import VendingMachineSystem






