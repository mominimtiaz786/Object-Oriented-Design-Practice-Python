class PaymentProcessor:
    def __init__(self):
        self.__current_balance: float = 0
    

    @property
    def current_balance(self):
        return self.__current_balance


    def addBalance(self, amount: float):
        self.__current_balance+=amount
    

    def charge(self, amount: float):
        self.__current_balance-=amount

    
    def returnChange(self) -> float:
        change, self.__current_balance = self.current_balance, 0
        return change
    
