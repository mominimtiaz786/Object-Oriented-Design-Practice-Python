class AccountLockerPolicy:
    def __init__(self, free_period_days: int, maximum_period_days: int):
        self.free_period_days = free_period_days
        self.maximum_period_days = maximum_period_days

    def getFreeDays(self):
        return self.free_period_days

    def getMaximumDays(self):
        return self.maximum_period_days


class Account:
    def __init__(self, owner_name: str, locker_policy: AccountLockerPolicy, usage_charges: float = 0):
        self.owner_name = owner_name
        self.locker_policy = locker_policy
        self.usage_charges = usage_charges

    def addUsageCharges(self, charges: float):
        self.usage_charges += charges

    def getAccountId(self) -> str:
        pass

    def getLockerPolicy(self):
        return self.locker_policy
