from . import (
    InventoryManager,
    PaymentProcessor,
    Transaction,
)

class VendingMachineSystem:
    def __init__(self):
        self.inventory_management = InventoryManager()
        self.payment_processor = PaymentProcessor()
        self.current_transaction = Transaction()
        self.transaction_history: list[Transaction] = []


    def insertMoney(self, amount: float):
        self.payment_processor.addBalance(amount)


    def chooseProduct(self, rack_id):
        product = self.inventory_management.getProductInRack(rack_id)
        self.current_transaction.setProduct(product)
        self.current_transaction.setRack(self.inventoryManager.getRack(rack_id))


    def confirmTransaction(self)-> Transaction:
        self.__validateTransaction()

        self.payment_processor.charge(self.current_transaction.getProduct().getPrice())

        self.inventory_management.dispenseProductFromRack(
            self.current_transaction.getRack()
        )

        completed_transaction = self.current_transaction
        
        self.current_transaction.setTotalAmount(self.payment_processor.returnChange())

        self.transaction_history.append(self.current_transaction)

        self.current_transaction = Transaction()

        return completed_transaction


    def __validateTransaction(self):
        if (self.current_transaction.getProduct() == None):
            raise Exception("Invalid product selection")
        elif (self.current_transaction.getRack().getProductCount() == 0):
            raise Exception("Insufficient inventory for product.")
        elif (self.payment_processor.current_balance < self.current_transaction.getProduct().getPrice()):
            raise Exception("Insufficient fund")


    def cancelTransaction(self) -> Transaction:
        self.payment_processor.returnChange()
        self.current_transaction = Transaction()


    def getTransactionHistory(self)-> list[Transaction]:
        return self.transaction_history.copy()
    